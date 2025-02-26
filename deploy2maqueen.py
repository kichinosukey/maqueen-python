import subprocess
import sys

# コマンドライン引数の確認（デプロイ用ファイル1つのみ指定）
if len(sys.argv) != 2:
    print("使い方: python deploy_to_maqueen.py DEPLOY_FILE_NAME.py")
    sys.exit(1)

deploy_filename = sys.argv[1]

# 固定のライブラリファイルを読み込む
try:
    with open("maqueen.py", "r") as f:
        library_code = f.read()
    print("maqueen.py の読み込み完了")
except FileNotFoundError:
    print("エラー: maqueen.py が見つかりません。")
    sys.exit(1)

# 任意に指定されたデプロイ用ファイルを読み込む
try:
    with open(deploy_filename, "r") as f:
        deploy_code = f.read()
    print(f"{deploy_filename} の読み込み完了")
except FileNotFoundError:
    print(f"エラー: {deploy_filename} が見つかりません。")
    sys.exit(1)

# 2つのファイルを結合（ライブラリ部分を先頭に、ユーザーのデプロイ用コードを後ろに）
combined_code = library_code + "\n\n" + deploy_code

# 結合済みコードの出力ファイル名を生成（例: deploy_combined.py）
output_filename = deploy_filename.replace(".py", "_combined.py")

# 結合済みコードを出力ファイルに書き出す
with open(output_filename, "w") as f:
    f.write(combined_code)
print(f"結合済みコード生成完了: {output_filename}")

# uflashでmicro:bitに書き込み
try:
    subprocess.run(["uflash", output_filename], check=True)
    print("Micro:Maqueenへの書き込みが完了しました！")
except subprocess.CalledProcessError as e:
    print(f"書き込みに失敗しました: {e}")
except FileNotFoundError:
    print("uflashが見つかりません。'pip install uflash'を確認してください。")
