# maqueen-python

DFRobot社のmicro:MaqueenをMicroPythonで制御するためのサンプルコードをまとめたものです。I²C通信を用いて、maqueenのモーターやサーボ（超音波センサー用）の制御を行います。

---

## 開発ロードマップ チェックリスト

### Phase 1: 基本的なモーター制御の実装とテスト
- [x] **モーター制御関数の実装（maqueen.py）**  
  - `move_forward()`, `move_backward()`, `turn_left()`, `turn_right()`, `stop_motors()` を実装
- [x] **モーター制御のテストコード作成**  
  - 各動作（前進・後退・旋回）の動作確認用テストコードの実装および実機での確認

### Phase 2: センサの統合とフィードバック制御
- [x] **超音波センサーの統合**  
  - `get_distance()` の実装（HC-SR04を用いた距離計測）完了
  - 超音波センサーのテストコード（距離をLEDに表示）の実装済み
- [ ] **ラインセンサーの基礎動作確認**  
  - `get_line()` 関数の実装（左右のラインセンサー値の取得）完了（※キャリブレーションや安定性の確認は未完了）
  - ラインセンサーのテストコード（LEDに左右の値を表示）の作成
- [ ] **フィードバック制御ロジックの検討**  
  - センサ値に応じたモーター制御（障害物検出で停止、ライン検出で追従など）の基礎設計

### Phase 3: 自律走行と複合モードの実装
- [ ] **ライントレース機能の実装**  
  - ラインセンサーの値に基づいた左右モーターの速度調整で、ラインに沿って走行させるアルゴリズムの開発
- [ ] **障害物回避ロジックの実装**  
  - 超音波センサーの距離情報を活用し、障害物が近づいた場合の自動旋回ロジックの実装
- [ ] **複数モード切替機能の検討**  
  - 手動操作、自律走行、混合モードなど、ユーザが動作モードを切り替えられる仕組みの設計と実装

### Phase 4: 無線通信および拡張機能の統合
- [ ] **無線通信機能の実装**  
  - micro:bit の radio や BLE を利用したリモート制御機能の検討と実装
- [ ] **外部コントローラーや追加センサとの連携**  
  - 複数のmicro:bit間や外部デバイスとの連携方法の検討

### Phase 5: コードのリファクタリングとドキュメント整備
- [ ] **コードのモジュール化・リファクタリング**  
  - 各機能を整理し、使いやすいAPIを提供するためのコード改善
- [ ] **ドキュメントの充実**  
  - READMEやWikiに、開発ルール・注意事項（例：デプロイ対象コードからの `from maqueen import ...` 行禁止、micro:bitのファイルシステムの制約など）を明示
- [ ] **テスト自動化・ユニットテストの導入**  
  - MicroPython環境で実施可能なテストコードの自動実行環境の検討

---

## 現状の進捗状況

- **Phase 1:**  
  - 基本的なモーター制御関数とテストコードは実装済み（ただし、実機での微調整が必要）。
- **Phase 2:**  
  - 超音波センサーの統合は完了、テストコードで距離計測と表示が可能。  
  - ラインセンサーの基礎動作確認は実装済み（キャリブレーションと安定動作の検証が未完了）。
- **Phase 3～Phase 5:**  
  - 自律走行、無線通信、及びコード整理・ドキュメント整備は今後の課題として予定中。

---

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