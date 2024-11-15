# 1. 베이스 이미지 선택 (Python 설치된 이미지)
FROM python:3.9-slim

# 2. 작업 디렉토리 생성
WORKDIR /app

# 3. Bandit 설치
RUN pip install bandit

# 4. Python 코드 복사
COPY bandit /app

# 5. Bandit 실행 명령어 설정
CMD ["python", "bandit.py"]