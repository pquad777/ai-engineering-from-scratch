import os
import anthropic
from dotenv import load_dotenv
from pathlib import Path

# 프로젝트 루트 경로
ROOT_DIR = Path(__file__).resolve().parents[2]

# .env 파일 로드
load_dotenv(ROOT_DIR / ".env")

client = anthropic.Anthropic()
MODEL = os.environ.get("LLM_MODEL")

if not MODEL:
    raise ValueError("LLM_MODEL is not set in .env")

response = client.messages.create(
    model=MODEL,
    max_tokens=256,
    messages=[
        {
            "role": "user",
            "content": "What is a neural network in one sentence?"
        }
    ]
)

print(response.content[0].text)