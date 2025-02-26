from microbit import i2c, sleep, pin1, pin2
import utime

# I²Cアドレス（DFRobotのMaqueenでは 0x10 と仮定）
I2C_ADDR = 0x10

# レジスタ定義（MakeCode拡張パッケージに準拠）
# 左モーター (M1) 用は 0x00、右モーター (M2) 用は 0x02
REG_LEFT_MOTOR  = 0x00
REG_RIGHT_MOTOR = 0x02

# 方向定義（MakeCodeと同じ）
DIR_FORWARD = 0   # CW: Forward（前進）
DIR_BACK    = 1   # CCW: Backward（後退）


def activate_motor_driver():
    """モータードライバをアクティブにする。
    
    I²C経由でスタンバイ解除コマンドを送信する。
    ※ 本来は専用のスタンバイレジスタがある場合もありますが、pxt-maqueenの実装では
      左モーター用レジスタ0x00が使用されているため、ここではそのレジスタに1を送信しています。
    """
    # ここでは暫定的に、左モーター用レジスタに1を書き込んでスタンバイ解除とする
    i2c.write(I2C_ADDR, bytearray([0x00, 1]))
    sleep(100)


def motor_run(reg, direction, speed):
    """I²Cを介してモーター制御コマンドを送信する。

    3バイトのデータ [レジスタ, 方向, 速度] を作成して送信します。

    Args:
        reg (int): モーター制御用レジスタのアドレス。
                   左モーターの場合は REG_LEFT_MOTOR、右モーターの場合は REG_RIGHT_MOTOR を使用。
        direction (int): モーターの回転方向。DIR_FORWARD（0）は前進、DIR_BACK（1）は後退を示す。
        speed (int): 速度値（0～255）。0は停止、255が最大速度。
    """
    buf = bytearray(3)
    buf[0] = reg
    buf[1] = direction
    buf[2] = speed
    i2c.write(I2C_ADDR, buf)


def stop_motors():
    """両モーターを停止させる。

    両モーターに速度0の前進コマンドを送信し、停止状態にする。
    """
    motor_run(REG_LEFT_MOTOR, DIR_FORWARD, 0)
    motor_run(REG_RIGHT_MOTOR, DIR_FORWARD, 0)


def move_forward(speed, duration_ms):
    """ロボットを前進させる。

    左右のモーターに前進指令を送信し、指定した時間前進させた後に停止する。

    Args:
        speed (int): 速度値（0～255）。
        duration_ms (int): 前進する時間（ミリ秒）。
    """
    motor_run(REG_LEFT_MOTOR, DIR_FORWARD, speed)
    motor_run(REG_RIGHT_MOTOR, DIR_FORWARD, speed)
    sleep(duration_ms)
    stop_motors()


def move_backward(speed, duration_ms):
    """ロボットを後退させる。

    左右のモーターに後退指令を送信し、指定した時間後退させた後に停止する。

    Args:
        speed (int): 速度値（0～255）。
        duration_ms (int): 後退する時間（ミリ秒）。
    """
    motor_run(REG_LEFT_MOTOR, DIR_BACK, speed)
    motor_run(REG_RIGHT_MOTOR, DIR_BACK, speed)
    sleep(duration_ms)
    stop_motors()


def turn_left(speed, duration_ms):
    """ロボットを左に旋回させる。

    左モーターに後退、右モーターに前進の指令を送信して左旋回を実現する。

    Args:
        speed (int): 速度値（0～255）。
        duration_ms (int): 旋回する時間（ミリ秒）。
    """
    motor_run(REG_LEFT_MOTOR, DIR_BACK, speed)
    motor_run(REG_RIGHT_MOTOR, DIR_FORWARD, speed)
    sleep(duration_ms)
    stop_motors()


def turn_right(speed, duration_ms):
    """ロボットを右に旋回させる。

    左モーターに前進、右モーターに後退の指令を送信して右旋回を実現する。

    Args:
        speed (int): 速度値（0～255）。
        duration_ms (int): 旋回する時間（ミリ秒）。
    """
    motor_run(REG_LEFT_MOTOR, DIR_FORWARD, speed)
    motor_run(REG_RIGHT_MOTOR, DIR_BACK, speed)
    sleep(duration_ms)
    stop_motors()


def get_distance():
    """HC-SR04超音波センサーを用いて距離を計測する。

    Trig: P1, Echo: P2 を使用して、障害物との距離をcm単位で計測します。

    Returns:
        float: 計測された距離（cm）。
    """
    # Trigピン（P1）を低レベルにして安定化
    pin1.write_digital(0)
    utime.sleep_us(2)
    # 10μsのパルスを送信
    pin1.write_digital(1)
    utime.sleep_us(10)
    pin1.write_digital(0)
    
    # Echoピン（P2）がHighになるまで待機
    while pin2.read_digital() == 0:
        pass
    start = utime.ticks_us()
    # EchoピンがLowになるまで待機
    while pin2.read_digital() == 1:
        pass
    end = utime.ticks_us()
    
    duration = utime.ticks_diff(end, start)
    distance = duration / 58.0
    return distance