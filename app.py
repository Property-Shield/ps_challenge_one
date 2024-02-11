from flask import Flask, request, jsonify
import json  # Add this line

app = Flask(__name__)

@app.route('/update_properties', methods=['POST'])
def update_properties():
    try:
        data = request.get_json(force=True)  # This will ignore the content type and try to parse JSON
        with open("received_properties.json", "w") as f:
            json.dump(data, f, indent=4)
        return jsonify({'message': 'Properties updated successfully'}), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)