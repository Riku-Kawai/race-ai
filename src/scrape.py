import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
url = "https://db.netkeiba.com/horse/2022105839"
response = requests.get(url, headers=headers)
print(response)
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, "html.parser")
prof_table = soup.find("table", class_="db_prof_table")

# 1レコード（辞書型）を格納する変数
horse_data = {}

if prof_table:
    # テーブル内の各行（tr）をループ処理
    for row in prof_table.find_all("tr"):
        th = row.find("th")
        td = row.find("td")
        
        # thとtdが両方存在する場合のみデータを抽出
        if th and td:
            key = th.get_text(strip=True)
            # .strip() で前後の余計な改行やスペースを削除
            value = td.get_text(strip=True)
            horse_data[key] = value

    # 結果の表示
    print(horse_data)