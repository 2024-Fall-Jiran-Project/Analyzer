# 베이스 이미지로 Debian 사용
FROM debian:latest

# cppcheck 설치
RUN apt-get update && apt-get install -y cppcheck
RUN apt-get update && apt-get install -y python3

# 작업 디렉터리 설정
WORKDIR /app

# 필요한 파일 복사 (필요한 경우만 복사)
COPY cppcheck /app

# 기본 명령어 설정
CMD ["python3", "cppcheck.py"]