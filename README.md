# Python の準備

pyenv と venv を利用する。

```sh
# Tkinter がインストールしてある状態で Python をインストールしないと起動しない。その場合は一度アンインストールする
# pyenv uninstall 3.12.1
brew install python-tk@3.12
pyenv install 3.12.1
```

# セットアップ

## 初回のみ

```sh
python -m venv ./venv
```

## 必要に応じて毎回

### 依存系のインストール

```sh
pip install -r requirements.txt
```

## pip でパッケージを増やしたら

```sh
pip freeze > requirements.txt
```

# 起動方法

## venv 環境へ入る

```sh
source venv/bin/activate
```

## 起動

```sh
python main.py
```

## 終了

```sh
deactivate
```
