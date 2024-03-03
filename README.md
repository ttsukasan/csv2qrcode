# csv2qrcode

CSVファイルの内容からQRコードを一括作成するスクリプトです。
EPS,SVGファイルの出力に対応しています。

## 動作環境

Windows

## インストール

1. [Python](https://apps.microsoft.com/detail/9p7qfqmjrfp7?hl=ja-jp&gl=JP) をインストール
    - 上記リンクをクリックして Microsoft Store から入手してください。
2. [PyQRCode](https://pypi.org/project/PyQRCode/)をインストール
    - コマンドラインで `pip install pyqrcode` を実行してください。
3. csv2qrcode.py, list.csv を任意のフォルダに保存

## 使い方

1. list.csv にデータを入力
2. list.csv を csv2qrcode.py にドラッグアンドドロップ

コマンドラインが表示され、処理結果が表示されます。
現在時刻のフォルダが作成され、中に出力されたファイルが配置されます。

