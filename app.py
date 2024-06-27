from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('')
def home()
    return Welcome to my API!

@app.route('apiv1resource', methods=['GET'])
def get_resource()
    sample_data = {
        id 1,
        name Sample Resource,
        description This is a sample resource.
    }
    return jsonify(sample_data)

@app.route('apiv1resource', methods=['POST'])
def create_resource()
    data = request.get_json()
    response = {
        message Resource created successfully,
        data data
    }
    return jsonify(response), 201

if __name__ == '__main__'
    app.run(debug=True)
