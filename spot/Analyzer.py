import os
import subprocess

ANALYZERS = {
    "python": ["bandit", "pylint", "rats", "devskim", "sonarqube", "joern", "semgrep"],
    "c": ["infer", "ikos", "frama-c", "rats", "devskim", "cppcheck", "sonarqube", "joern", "semgrep"],
    "cpp": ["infer", "ikos", "rats", "devskim", "cppcheck", "sonarqube", "joern", "semgrep"],
    "java": ["infer", "spotbugs", "rats", "devskim", "sonarqube", "joern", "semgrep"]
}

def get_language_and_analyzers(filename):
    ext = os.path.splitext(filename)[1].lower()
    if ext == ".py":
        return "python", ANALYZERS["python"]
    elif ext == ".c":
        return "c", ANALYZERS["c"]
    elif ext in [".cpp", ".cc", ".cxx", ".hpp", ".h"]:
        return "cpp", ANALYZERS["cpp"]
    elif ext == ".java":
        return "java", ANALYZERS["java"]
    else:
        return None, []
    
def run_docker_analyzer(analyzer, filename):
    try:
        env = os.environ.copy()
        env["TARGET_FILE"] = filename
        
        command = [
            "docker-compose", "run", "--rm", analyzer
        ]
        result = subprocess.check_output(command, text=True, encoding="utf-8", env=env)
        return {f"{analyzer}_log": result}
    except subprocess.CalledProcessError as e:
        return {f"{analyzer}_error": str(e)}
        
def analyze_file(filename):
    language, analyzers = get_language_and_analyzers(filename)
    if not analyzers:
        return {"error": "지원되지 않는 파일 형식이거나 사용 가능한 분석기가 없습니다."}

    print(f"[ 언어 감지됨 ]: {language}")
    results = {}

    for analyzer in analyzers:
        print(f"[ 실행 중: {analyzer} 분석기 ]...")
        results.update(run_docker_analyzer(analyzer, filename))

    return results
if __name__ == "__main__":
    filename = input("분석할 파일명을 입력하세요: ")
    filepath = os.path.join('./input', filename)  
    
    if not os.path.isfile(filepath):
        print(f"파일을 찾을 수 없습니다: {filepath}")
    else:
        analysis_results = analyze_file(filepath)
        print("[ 분석 결과 ]: \n", analysis_results)