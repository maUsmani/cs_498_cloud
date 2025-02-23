import subprocess
import socket
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_private_ip():
    """
    Returns the private IP address of this EC2 instance.
    """
    hostname = socket.gethostname()            # e.g. ip-172-31-XX-XX
    ip_address = socket.gethostbyname(hostname)
    return ip_address

@app.route("/", methods=["POST"])
def start_cpu_stress():
    """
    Spawns a subprocess running "stress_cpu.py".
    Returns immediately so that the Flask server remains responsive.
    """
    # Run stress_cpu.py in a separate process (non-blocking)
    subprocess.Popen(["python3", "stress_cpu.py"])
    
    return "CPU stress started\n"

if __name__ == "__main__":
    # Listen on all interfaces so it's accessible externally.
    # Adjust port as needed. If you choose port 80, you may need sudo.
    app.run(host="0.0.0.0", port=5000)
