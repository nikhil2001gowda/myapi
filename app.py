from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory storage for resources
resources = [
    {"id": 1, "name": "Resource 1", "description": "This is the first resource"},
    {"id": 2, "name": "Resource 2", "description": "This is the second resource"}
]

# Helper function to find resource by id
def find_resource(resource_id):
    return next((resource for resource in resources if resource["id"] == resource_id), None)

@app.route('/')
def home():
    return "Welcome to my API!"

# GET all resources
@app.route('/api/v1/resources', methods=['GET'])
def get_resources():
    return jsonify(resources)

# GET a single resource by id
@app.route('/api/v1/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    resource = find_resource(resource_id)
    if resource is None:
        abort(404, description="Resource not found")
    return jsonify(resource)

# POST create a new resource
@app.route('/api/v1/resources', methods=['POST'])
def create_resource():
    if not request.json or not 'name' in request.json:
        abort(400, description="Invalid data")
    
    new_id = max(resource["id"] for resource in resources) + 1
    new_resource = {
        "id": new_id,
        "name": request.json["name"],
        "description": request.json.get("description", "")
    }
    resources.append(new_resource)
    return jsonify(new_resource), 201

# PUT update an existing resource by id
@app.route('/api/v1/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    resource = find_resource(resource_id)
    if resource is None:
        abort(404, description="Resource not found")
    
    if not request.json:
        abort(400, description="Invalid data")
    
    resource["name"] = request.json.get("name", resource["name"])
    resource["description"] = request.json.get("description", resource["description"])
    return jsonify(resource)

# DELETE a resource by id
@app.route('/api/v1/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    resource = find_resource(resource_id)
    if resource is None:
        abort(404, description="Resource not found")
    
    resources.remove(resource)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
