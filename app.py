from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

request_count = 0

def count_files(folder_path):
    files = os.listdir(folder_path)
    num_files = len(files)
    return num_files

@app.route('/', methods=['GET'])
def get_data(): 
    global request_count
    folder_path = "etat-du-traffic"
    
    num_files = count_files(folder_path)
    
    request_count = (request_count + 1) % num_files
    
    csv_file_path = os.path.join(folder_path, f"etat-du-trafic-en-temps-reel-{request_count}.csv")
    df = pd.read_csv(csv_file_path, sep=";")
    
    data_dict = df.to_dict(orient='records')
    
    return jsonify({'data': data_dict})

if __name__ == '__main__':
    app.run(debug=True)
