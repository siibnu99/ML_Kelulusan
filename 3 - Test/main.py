from flask import Flask, request
import joblib
import os

app = Flask(__name__)

@app.route('/process_post_data', methods=['POST'])
def process_post_data():
    # 'id_prodi', 'IPS1', 'IPS2', 'IPS3', 'IPS4', 'SKS1', 'SKS2', 'SKS3',
    #    'SKS4'
    id_prodi = float(request.form['id_prodi'])
    ips1 = float(request.form['IPS1'])
    ips2 = float(request.form['IPS2'])
    ips3 = float(request.form['IPS3'])
    ips4 = float(request.form['IPS4'])
    ips5 = float(request.form['IPS5'])
    ips6= float(request.form['IPS6'])
    sks1 = float(request.form['SKS1'])
    sks2 = float(request.form['SKS2'])
    sks3 = float(request.form['SKS3'])
    sks4 = float(request.form['SKS4'])
    sks5 = float(request.form['SKS5'])
    sks6 = float(request.form['SKS6'])
    input_data = (id_prodi, ips1, ips2, ips3, ips4,ips5,ips6, sks1, sks2, sks3, sks4, sks5, sks6)
    print(input_data)
    #get this directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    model = joblib.load(f'{dir_path}/kkn_model_6.pkl')
    prediction = model.predict([input_data])
    if prediction == 0:
        return f'Mahasiswa tidak lulus tepat waktu'
    else:
        return f'Mahasiswa lulus tepat waktu'


if __name__ == '__main__':
    app.run(debug=True)