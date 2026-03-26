from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  # changed

@app.route('/api', methods=['POST'])
def api():
    data = request.json
    user_input = data.get("input")

    return jsonify({
        "message": f"You entered: {user_input}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)