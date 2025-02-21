import requests

# ✅ 네이버 스마트플레이스 검색 URL (API 엔드포인트 확인 필요)
url = "https://map.naver.com/v5/api/search?query=홍대%20미용실&type=all"

# ✅ User-Agent, Referer, Cookie 추가 (403 방지)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://map.naver.com/",
    "Accept-Language": "ko-KR,ko;q=0.9",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest"
}

# ✅ 네이버 세션을 활용한 요청 (쿠키 유지)
session = requests.Session()
session.headers.update(headers)

# ✅ 데이터 요청
response = session.get(url)

# ✅ 응답 확인
if response.status_code == 200:
    print("✅ 데이터 가져오기 성공!")
    print(response.json