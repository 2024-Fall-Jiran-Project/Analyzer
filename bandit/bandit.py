import subprocess
import os

def log_result():
    try:
        # '/app/input' 디렉토리에서 '.py' 확장자를 가진 모든 파일을 리스트에 저장
        files_py = [os.path.join('/app/input', f) for f in os.listdir('/app/input') if f.endswith('.py')]
        print("찾은 Python 파일:", files_py)
        
        if not files_py:
            # Python 파일이 없을 경우 에러 메시지 반환
            return {"error": "파일이 존재하지 않습니다."}, 400

        results = []  # 결과를 저장할 리스트
        
        # 각 Python 파일에 대해 Bandit 명령 실행
        for file in files_py:
            command = ["bandit", "-r", file, "-f", "txt"]
            
            # Bandit 명령 실행 및 출력 캡처
            compile_process = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
            
            # 디버깅용 출력
            # print(f"Bandit 실행 파일: {file}")
            # print("표준 출력:\n", compile_process.stdout)
            # print("표준 에러:\n", compile_process.stderr)
            
            if compile_process.returncode == 0:
                # Bandit 실행 결과 취약점이 없는 경우 메시지 추가
                results.append(f"파일 {file} 에 취약점이 없습니다.")
            else:
                # 취약점이 있는 경우 상세한 결과 추가
                results.append(f"파일 {file} 에 취약점이 발견되었습니다:\n{compile_process.stdout}")

        # 모든 결과를 하나의 문자열로 결합하여 요약 반환
        result_summary = "\n".join(results)
        print("결과 요약:\n", result_summary)
        return result_summary

    except Exception as e:
        # 예외 발생 시 에러 메시지 출력 및 반환
        print("에러 발생:", str(e))
        return {"error": str(e)}

if __name__ == '__main__':
    log_result()
