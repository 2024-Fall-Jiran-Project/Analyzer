import subprocess

def log_result(filename):
    try:
        docker_command = ["semgrep", "--config", "auto", f"/app/input/{filename}"]

        # Run the Docker command and capture output
        compile_process = subprocess.run(docker_command, capture_output=True, text=True, encoding="utf-8")
        
        # Print the output for debugging
        print("Standard Output:\n", compile_process.stdout)
        print("Standard Error:\n", compile_process.stderr)
        if compile_process.returncode == 0:
            print("파일에 취약점이 존재합니다..")
            result =  compile_process.stdout 
            return result
        
        else:
            print("파일에 취약점이 없습니다..")
            result = compile_process.stderr 
            
            return result

    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    filename = "test.py"    
    analysis_results = log_result(filename)
    print("[ 분석 결과 ]: \n", analysis_results)

