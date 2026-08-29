# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 專案現況
quantbot 是一個剛建立的專案骨架（uv 管理的 Python 專案），用途為「開發一個幣圈投資量化機器人」（見 pyproject.toml 的 description）。
目前 main.py 只有樣板程式碼，尚未有實際的模組、套件目錄或測試。README.md 目前是空的。

## 常用指令
- 安裝依賴：uv sync
- 執行程式：uv run main.py
- 執行測試：uv run pytest
- 執行單一測試：uv run pytest path/to/test_file.py::test_name
- Lint：uv run ruff check .
- 格式化：uv run ruff format .
- 型別檢查：uv run mypy .
- import 邊界檢查：uv run lint-imports（需先在 pyproject.toml 設定 [tool.importlinter] contracts，目前尚未設定）

Python 版本：pyproject.toml 要求 >=3.12；.python-version 指定 3.14（uv 會依此建立 .venv）。

## 依賴暗示的技術方向（尚未實作，供未來開發參考）
以下為 pyproject.toml 已宣告但尚未使用的正式依賴，暗示此專案未來的架構方向：
- ccxt：加密貨幣交易所 API 串接（下單、行情）
- asyncpg：非同步 PostgreSQL 存取（可能用於儲存行情/交易紀錄）
- pandas / numpy / pyarrow：資料處理與分析（回測、指標計算）
- plotly：視覺化（回測結果、圖表）
- pydantic-settings / pyyaml：設定管理（.env / YAML 設定檔）
- httpx：HTTP 客戶端

實際模組結構、命名慣例、分層方式等，等專案有實際程式碼後應以當時程式碼為準，不應依賴此文件的臆測。
