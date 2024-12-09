from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def helloworld():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, debug=True)


