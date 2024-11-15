# Frama-C 기반의 이미지 사용
FROM framac/frama-c:20.0

# Python 환경 설치
RUN apt-get update && apt-get install -y python3 python3-pip

# 작업 디렉토리 설정
WORKDIR /app

# Flask 설치
RUN pip3 install flask

# app 폴더 복사
COPY frama-c /app

# Flask 서버 실행
CMD ["python3", "frama-c.py"]
