from flask import Flask, request, make_response
from datetime import datetime
from hashlib import sha256

app = Flask(__name__)

FLAG = "flag{hackera_boomboomhunter}"

@app.route('/api/validate', methods=['POST'])
def validate():
    token = request.headers.get('X-Auth-Token')
    signature = request.headers.get('X-Request-Signature')
    ua = request.headers.get('User-Agent')

    today = datetime.today().strftime("%Y%m%d")
    expected_sig = sha256(today.encode()).hexdigest()

    if token == 'abc12346' and signature == expected_sig and ua == 'HeaderHunter/1.0':
        resp = make_response("🎯 Nice header skills.")
        resp.headers['X-Flag'] = FLAG
        return resp

    return "Access Denied", 403

if __name__ == '__main__':
    app.run(port=8080)
