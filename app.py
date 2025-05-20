from flask import Flask, request, jsonify
app = Flask(__name__)

PHONE_DATA = {}

@app.route('/upload-files', methods=['POST'])
def upload_files():
    data = request.json
    PHONE_DATA['files'] = data.get('files', [])
    return jsonify({'status': 'success'})

@app.route('/get-files', methods=['GET'])
def get_files():
    return jsonify(PHONE_DATA.get('files', []))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
