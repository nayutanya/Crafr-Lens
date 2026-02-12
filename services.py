import os
from openai import OpenAI

# .envから読み込んだAPIキーを使用してクライアントを初期化
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_handmade_image(image_url: str):
    """
    画像をAIに送り、作品の特徴・おすすめ説明文・価格目安を生成する
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # 費用を抑えつつ高性能な最新モデル
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "あなたはハンドメイド作家の専門コンサルタントです。この画像を見て、作品の『魅力的な商品名』『minneで売れる商品説明文』『妥当な販売価格（日本円）』を日本語で提案してください。"},
                        {
                            "type": "image_url",
                            "image_url": {"url": image_url},
                        },
                    ],
                }
            ],
            max_tokens=500,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"