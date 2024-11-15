import subprocess
import os

def log_result():
    
    try:
        files = [os.path.join('/app/input', f) for f in os.listdir('/app/input') if f.endswith('.py')]
        if not files:
            return {"error": "No Java files found"}, 400
        
        command = ["bandit", "-r",  f"/app/input/{files}", "-f", "txt"]
        # Run the Docker command and capture output
        compile_process = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        
        # Print the output for debugging
        # print("Standard Output:\n", compile_process.stdout)
        # print("Standard Error:\n", compile_process.stderr)
        if compile_process.returncode == 0:
            result = "파일에 취약점이 없습니다."
            return result
        
        else:
            print("파일에 취약점이 존재합니다..")
            result = compile_process.stdout 
            data = {"log": result}
            return result

    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    log_result()