from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from main import get_waterbody_info
from map import make_map_with_pointer
app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    waterbody = data.get('waterbody')
    print(waterbody)
    if waterbody and len(waterbody) > 3:
        info = get_waterbody_info(waterbody)
        make_map_with_pointer(info[0], info[1], info[2], info[3], info[4], info[5])
        html_content = read_html_file('map.html')
        print("returning html")
        file_path = os.path.join(os.getcwd(), 'map.html')
        return send_file(file_path, mimetype='text/html')
        #return jsonify({'html': html_content})
    else:
        return jsonify({"error": "Invalid waterbody name"}), 400

def read_html_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
if __name__ == '__main__':
    app.run(debug=True)