from flask import Flask, jsonify, render_template
import socket


app = Flask(__name__)

# Function to fetch hostname and ip of the server
def fetchDetails():
    host_name = socket.gethostname()
    print (host_name)
    # host_ip = socket.gethostbyname(host_name)
    return host_name

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route("/details")
def details():
    host_name= fetchDetails()
    return render_template('index.html', host_name=host_name, host_ip='0.0.0.0' )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
