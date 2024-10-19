from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)
@app.route('/htop')
def htop():
    name = "Your Full Name"
    username = os.getlogin()
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + 19800))  # IST
    top_output = subprocess.getoutput('top -b -n 1')

    return f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h3>Server Time (IST): {server_time}</h3>
    <pre>{top_output}</pre>
    """
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
