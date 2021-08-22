import datetime

from flask import Flask, send_file, request
import qrcode


app = Flask(__name__)


@app.get('/')
def _handle_home():
    return 'Hello, world!'


@app.get('/generate-qr-code')
def _handle_generate_qr_code():
    name = request.args.get('name')

    qr_code_image = qrcode.make(f'Acesta este biletul lui {name}. A fost generat la data de {datetime.datetime.now()}')

    qr_code_image.save('temp_file.png')

    return send_file('temp_file.png')


app.run(host='192.168.99.100', port=80)