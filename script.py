import csv
from datetime import datetime
import os
import pyqrcode
import sys
import time

# QRコード出力時の拡大率
RENDERING_SCALE = 4

# SVGファイルを出力するかどうかを制御するグローバル変数 (0: 出力しない, 1: 出力する)
OUTPUT_SVG = 1

# EPSファイルを出力するかどうかを制御するグローバル変数 (0: 出力しない, 1: 出力する)
OUTPUT_EPS = 1

def create_folder():
    current_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
    os.makedirs(current_datetime)
    return current_datetime

def process_csv(file_path, folder_name):
    processed_count = 0
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # ヘッダーをスキップ
        for row in reader:
            # 空行を無視する
            if not row:
                continue
            content = row[1]
            folder_bytes = os.fsencode(folder_name)
            filename_bytes = os.fsencode(f"{row[0]}")
            filepath_bytes = os.path.join(folder_bytes, filename_bytes)
            url = pyqrcode.create(content, encoding='utf-8')
            if OUTPUT_SVG:
                svg_filename = f"{filepath_bytes.decode()}.svg"
                url.svg(svg_filename, scale=RENDERING_SCALE)
            if OUTPUT_EPS:
                eps_filename = f"{filepath_bytes.decode()}.eps"
                url.eps(eps_filename, scale=RENDERING_SCALE)
            print(f"+ {row[0]}.eps / svg")
            processed_count += 1

    return processed_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("CSVファイルを指定してください。")
    else:
        csv_file = sys.argv[1]
        if not os.path.isfile(csv_file):
            print("指定されたファイルが見つかりません。")
            sys.exit(1)
        
        folder_name = create_folder()
        print(f"{folder_name}/\n")

        processed_count = process_csv(csv_file, folder_name)

        print(f"\n{processed_count}件のQRコードを生成しました。")

        print("何かキーを入力してください...", end='')
        input()