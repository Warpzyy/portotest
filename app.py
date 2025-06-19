from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/paket')
def paket():
    return "Halaman Paket"

@app.route('/kupon')
def kupon():
    return "Halaman Kupon"

@app.route('/contact/')
def contact():
    return "Halaman Kontak"


if __name__ == '__main__':
    app.run(debug=True)
