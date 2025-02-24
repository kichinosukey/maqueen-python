# maqueen-python

DFRobot社のmicro:MaqueenをMicroPythonで制御するためのサンプルコードをまとめたものです。I²C通信を用いて、maqueenのモーターやサーボ（超音波センサー用）の制御を行います。

## 仕様

- **I²Cアドレス**: `0x10`
- **レジスタの割り当て**:
  - `0x00`：左モーター (M1) 用
  - `0x02`：右モーター (M2) 用
- **方向定義**:
  - `0` : Forward (CW)
  - `1` : Backward (CCW)

## 必要なもの

- micro:bit
- micro:Maqueen本体

## 使い方

1. **配線**  
   micro:bitをmicro:maqueenに接続

2. **コードの書き込み**  
   以下のサンプルコードをmicro:bitに書き込みます。

   ```shell
   python deploy2maqueen.py motor_test.py
   ```

3. **動作確認**  
   書き込み完了後、maqueenが前進動作を開始するはず。

## 補足

- このコードは、DFRobotが公開しているMakeCode拡張パッケージ（pxt-maqueen）のソースコードからレジスタの割り当て情報を抽出したもの。詳細は [pxt-maqueen リポジトリ](https://github.com/DFRobot/pxt-maqueen/blob/master/maqueen.ts) を参照のこと。

## ライセンス

このプロジェクトはApache2.0ライセンスの下で公開されています。