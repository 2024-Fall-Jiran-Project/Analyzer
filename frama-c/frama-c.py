import subprocess, os

def log_result():
    try:
        c_files = [os.path.join('/app/input', f) for f in os.listdir('/app/input') if f.endswith('.c')]
        
        if not c_files:
            return {"error": "No C files found"}, 400
        
        compile_process = subprocess.run(['gcc', '-o', '/app/input/output'] + c_files, capture_output=True, text=True)
        if compile_process.returncode == 0:
            print("C 파일이 성공적으로 컴파일되었습니다.")
            
            result = subprocess.check_output(['fram-c', '/app/input/output']).decode('utf-8')
            
            data = {"log": result}
            return data
        else:
            return {"error": compile_process.stderr}, 500
        
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    log_result()
