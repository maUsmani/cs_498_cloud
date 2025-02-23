from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize our seed value to 0.
seed_value = 0

@app.route("/", methods=["GET"])
def get_seed():
    """
    Returns the current seed value as a string.
    """
    return str(seed_value)

@app.route("/", methods=["POST"])
def set_seed():
    """
    Expects a JSON body of the form {"num": some_integer}.
    Updates the global seed value to 'num'.
    Returns the new seed value as a string.
    """
    global seed_value
    data = request.get_json(force=True)  # or request.json
    seed_value = data["num"]
    return str(seed_value)

if __name__ == "__main__":
    # Listen on all interfaces (0.0.0.0) so it's accessible externally.
    # You can choose any port you like, commonly 5000 or 80.
    # If using port 80, you may need sudo privileges.
    app.run(host="0.0.0.0", port=5000)
