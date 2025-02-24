import subprocess
import sys

# コマンドライン引数の確認
if len(sys.argv) != 2:
    print("使い方: python deploy_to_maqueen.py DEPLOYED_FILE_NAME")
    sys.exit(1)

template_filename = sys.argv[1]  # 実行時に指定されたテンプレートファイル名

# テンプレートファイルを読み込む
try:
    with open(template_filename, "r") as f:
        template = f.read()
    print(f"テンプレート読み込み完了: {template_filename}")
except FileNotFoundError:
    print(f"エラー: {template_filename} が見つかりません。")
    sys.exit(1)

# 生成されるファイル名（テンプレート名から"_template"を除去）
output_filename = template_filename.replace("_template", "") if "_template" in template_filename else f"{template_filename}_deployed.py"

# コードをファイルに書き出し
with open(output_filename, "w") as f:
    f.write(template)
print(f"Micro:Maqueen用コード生成完了: {output_filename}")

# uflashでmicro:bitに書き込み
try:
    subprocess.run(["uflash", output_filename], check=True)
    print("Micro:Maqueenへの書き込みが完了しました！")
except subprocess.CalledProcessError as e:
    print(f"書き込みに失敗しました: {e}")
except FileNotFoundError:
    print("uflashが見つかりません。'pip install uflash'を確認してください。")