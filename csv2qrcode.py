import os
import csv
import pyqrcode
from datetime import datetime
import time
import tkinter as tk
from tkinter import filedialog
import sys

########################################

# SVGファイル作成の設定 (0: 作成しない, 1: 作成する)
OUTPUT_SVG = 1

# EPSファイル作成の設定 (0: 作成しない, 1: 作成する)
OUTPUT_EPS = 1

# QRコード出力時の拡大率
RENDERING_SCALE = 4

########################################

def select_csv_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    return file_path

def create_folder():
    current_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
    os.makedirs(current_datetime)
    return current_datetime

def process_csv(file_path, folder_name):
    processed_count = 0
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
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
            print(f"+ {row[0]}")
            processed_count += 1

    return processed_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        file_path = select_csv_file()
        if not file_path:
            print("CSVファイルが選択されませんでした。")
            exit()
    else:
        file_path = sys.argv[1]
        if not os.path.isfile(file_path):
            print("指定されたファイルが見つかりません。")
            sys.exit(1)
      
    folder_name = create_folder()
    print(f"{folder_name}/\n")

    processed_count = process_csv(file_path, folder_name)

    print(f"\n{processed_count}件のQRコードを生成しました。")

    print("何かキーを押して終了します", end='')
    input()
