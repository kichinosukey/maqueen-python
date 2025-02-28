from microbit import display, Image, button_a, sleep, pin13, pin14

# カスタムイメージ定義
line_detected = Image("99999:00000:00000:00000:00000")  # ライン検出時表示
no_line = Image("00000:00000:00000:00000:00000")  # ライン非検出時表示

# 起動時メッセージ
display.show(Image.HEART)
sleep(500)

# メインループ
while True:
    # デジタルセンサー値を取得（0=黒、1=白）
    left = pin13.read_digital()
    right = pin14.read_digital()
    
    # Aボタンが押されたら生の値を表示（デバッグ用）
    if button_a.is_pressed():
        display.scroll("L:{} R:{}".format(left, right), delay=80)
        continue
    
    # センサー状態の視覚化（シンプルなパターン）
    if left == 0 and right == 0:
        # 両方ライン上（黒）
        display.show(Image("99999:99999:00000:00000:00000"))
    elif left == 0:
        # 左だけライン上（黒）
        display.show(Image("99900:99900:00000:00000:00000"))
    elif right == 0:
        # 右だけライン上（黒）
        display.show(Image("00999:00999:00000:00000:00000"))
    else:
        # 両方ライン外（白）
        display.show(Image("00000:00000:00000:00000:00000"))
    
    sleep(100)