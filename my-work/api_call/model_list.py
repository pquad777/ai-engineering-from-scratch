import os
import anthropic
from pathlib import Path
from dotenv import load_dotenv

# 프로젝트 최상위 폴더 찾기
ROOT_DIR = Path(__file__).resolve().parents[2]

# .env 불러오기
env_path = ROOT_DIR / ".env"
print("env path:", env_path)
print("env exists:", env_path.exists())

load_dotenv(env_path, override=True)

# API Key 확인 (실제 키는 출력하지 않음)
api_key = os.getenv("ANTHROPIC_API_KEY")
print("API Key loaded:", bool(api_key))

# 클라이언트 생성
client = anthropic.Anthropic(api_key=api_key)

# 모델 목록 조회
models = client.models.list()

for model in models:
    print(model.id)