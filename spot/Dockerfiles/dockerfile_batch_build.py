import os
import subprocess

def build_docker_images(dockerfile_paths, image_names):
    if len(dockerfile_paths) != len(image_names):
        raise ValueError("Dockerfile 경로와 이미지 이름의 개수가 일치하지 않습니다.")

    for dockerfile, image_name in zip(dockerfile_paths, image_names):
        try:
            # Docker build 명령어 생성
            command = [
                "docker", "build", "-f", dockerfile, "-t", image_name, os.path.dirname(dockerfile)
            ]
            print(f"[ 빌드 중 ]: {image_name} ({dockerfile})")
            # Docker 이미지 빌드 실행
            subprocess.run(command, check=True)
            print(f"[ 성공 ]: {image_name} 이미지가 성공적으로 생성되었습니다.")
        except subprocess.CalledProcessError as e:
            print(f"[ 실패 ]: {image_name} 이미지 빌드 실패. 오류: {e}")

# 사용 예시
dockerfile_paths = [
    "./Dockerfile.semgrep",
    "./Dockerfile.cppcheck",
    "./Dockerfile.bandit",
    "./Dockerfile.devskim"
]

image_names = [
    "semgrep-analyzer:latest",
    "cppcheck-analyzer:latest",
    "bandit-analyzer:latest",
    "devskim-analyzer:latest"
]

build_docker_images(dockerfile_paths, image_names)