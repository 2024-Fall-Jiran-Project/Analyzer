from flask import Flask, render_template, request
import requests, os

app = Flask(__name__)

UPLOAD_FOLDER = 'shared'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return '파일을 선택해야 합니다!!'
    
    file = request.files['file']
    
    if file.filename == '':
        return '파일을 선택하야 합니다!!'
    
    _, ext = os.path.splitext(file.filename)
    
    if not ext.lower() in {'.py', '.java', '.cpp', '.c'}:
        return '허용되지 않은 파일 형식입니다. Python, Java, C++, C 파일만 업로드 가능합니다.'
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    analysis = fetch_log()

    os.remove(filepath)
    
    return render_template('index.html', content=analysis)

def fetch_log():
    try:
        response = requests.get("http://spotbugs:301/log")
        
        if response.status_code == 200:
            data = response.json()
            return("[ Received log ]: \n", data["log"])
        else:
            return(f"Failed to fetch log. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")