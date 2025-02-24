from microbit import i2c, sleep

# I²Cアドレス
I2C_ADDR = 0x10

# モーター制御用レジスタ定義
REG_LEFT_MOTOR  = 0x00  # 左モーター(M1)
REG_RIGHT_MOTOR = 0x02  # 右モーター(M2)

# 方向定義（MakeCodeと同じ）
DIR_FORWARD = 0   # CW: Forward
DIR_BACK    = 1   # CCW: Backward

def motor_run(reg, direction, speed):
    # 3バイトのバッファを作成： [レジスタ, 方向, 速度]
    buf = bytearray(3)
    buf[0] = reg
    buf[1] = direction
    buf[2] = speed
    i2c.write(I2C_ADDR, buf)

def move_forward(speed, duration_ms):
    # 前進：左右ともにForward (DIR_FORWARD)
    motor_run(REG_LEFT_MOTOR, DIR_FORWARD, speed)
    motor_run(REG_RIGHT_MOTOR, DIR_FORWARD, speed)
    sleep(duration_ms)
    # 停止（速度0）
    motor_run(REG_LEFT_MOTOR, DIR_FORWARD, 0)
    motor_run(REG_RIGHT_MOTOR, DIR_FORWARD, 0)

# メインプログラム
move_forward(150, 2000)  # 両モーターを速度150で2秒間前進
