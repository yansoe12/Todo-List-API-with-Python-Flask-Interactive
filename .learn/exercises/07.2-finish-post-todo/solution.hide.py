from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
          { "label": "My first task", "done": False },
          { "label": "My second task", "done": False }
          
         ]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request.get_json(force=True)
    request_body = request.data
    print(request_body)
        
    decoded_object = json.loads(request_body)
    print(decoded_object)
    todos.append(decoded_object)

    # return todos
    
    json_text = jsonify(todos)
    print("Incoming request with the following body", request_body)
    return json_text


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)