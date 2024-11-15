# 1. .NET Core SDK 이미지 사용
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build-env

WORKDIR /app

RUN dotnet tool install --global Microsoft.CST.DevSkim.CLI
RUN apt-get update && apt-get install -y python3

ENV PATH="$PATH:/root/.dotnet/tools"

COPY devskim /app

# 기본 명령어 설정
CMD ["python3", "devskim.py"]