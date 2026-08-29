# quantbot

這個專案以 Clean / Onion Architecture 為核心，重點是把交易系統拆成四個層次：外部入口、應用邏輯、核心領域邏輯，以及基礎設施實作。依賴方向始終朝向核心，讓策略與商業規則不被外部技術細節污染。

## 專案目標

- 監控加密貨幣行情
- 建立交易策略與指標計算流程
- 整合資料存取、回測與績效分析
- 以清楚分層提升可維護性與可測試性
- 維持 domain 層的純粹性與穩定性

## 架構原則

### 分層依賴方向

```text
Entrypoints -> Application -> Domain <- Infrastructure
```

- Entrypoints：CLI、任務入口、外部呼叫點
- Application：用例與協調流程
- Domain：核心業務與策略邏輯
- Infrastructure：資料庫、交易所、下載、解析、圖表等外部技術

重點在於：Domain 是核心，不能知道外部技術細節；Infrastructure 只負責實作，不能干擾核心規則。

### Domain 介面設計

版圖中明確要求：domain 之下設置 interface 層，並讓它成為一個面向核心的抽象邏輯層。這樣可以避免以下問題：

- Application 直接依賴具體技術實作
- Domain 直接知道 Binance、PostgreSQL、plotly 等技術
- 介面不清楚時，資料流與邏輯很難測試

通常命名會採用：

- CandleSource
- CandleRepository
- BinanceArchiveCandleSource
- TimescaleCandleRepository

而不是：

- Manager
- Helper
- Utils

## 命名規範

圖片中也明確給出幾個實務規則：

| 類型     | 規則                                                                     | 範例                           |
| -------- | ------------------------------------------------------------------------ | ------------------------------ |
| 介面     | 能力名稱，不加 I 前綴                                                    | CandleSource, CandleRepository |
| 實作     | 技術 / 來源前綴 + 能力名                                                 | BinanceArchiveCandleSource     |
| 角色命名 | 只保留 Service、Application、Repository、Source、Parser、Renderer、Guard | 可接受                         |
| 命名禁忌 | 不要出現 Manager / Helper / Utils                                        | 禁止                           |
| 檔名     | snake_case，對齊主要型別                                                 | timescale_candle_repository.py |

## 目前狀態

這個 repo 目前仍是專案骨架，重點在於建立基礎架構、依賴規範與工程慣例，而非完整交易邏輯。現階段已具備：

- Python 專案設定與依賴管理
- 用於分層規範的 import-linter
- 清楚的 src 目錄結構
- 測試、型別與 lint 工具鏈

## 技術棧

| 項目       | 技術                      | 用途                   |
| ---------- | ------------------------- | ---------------------- |
| 語言       | Python 3.12+              | 量化與交易系統開發     |
| 交易 API   | ccxt                      | 連接主要加密貨幣交易所 |
| HTTP / API | httpx                     | 非同步 HTTP 呼叫       |
| 資料處理   | pandas, numpy             | 時序資料與數值計算     |
| 儲存       | asyncpg, PostgreSQL       | 行情與交易紀錄存放     |
| 可視化     | plotly                    | 回測與績效圖表         |
| 設定管理   | pydantic-settings, pyyaml | 環境與策略設定         |
| 測試       | pytest, pytest-asyncio    | 單元與整合測試         |
| 程式碼品質 | ruff, mypy, import-linter | 格式、型別與架構約束   |

## 專案結構

```text
quantbot/
├── src/
│   ├── app/
│   ├── domain/
│   ├── entrypoints/
│   └── infrastructure/
├── tests/
├── docs/
│   └── Architecture/
├── main.py
├── pyproject.toml
├── README.md
├── .python-version
├── uv.lock
└── .gitignore
```

## 快速開始

### 1. 建立環境

```bash
uv sync
```

### 2. 執行專案

```bash
uv run main.py
```

### 3. 執行測試

```bash
uv run pytest
```

### 4. 程式碼檢查

```bash
uv run ruff check .
uv run mypy .
```

## 架構守則

目前的設計重點：

- Domain 不知道 Binance、PostgreSQL、plotly 等外部技術
- Application 依賴抽象，不直接依賴實作
- Infrastructure 只提供具體技術實作
- entrypoints 只負責進入點，不應塞入過多業務邏輯

這些規則已在 [pyproject.toml](pyproject.toml) 中透過 import-linter 強制約束，會避免分層被破壞。

## 後續計畫

接下來會依序補齊：

1. 市場資料模型與行情抓取
2. 策略基底類別與指標計算
3. 回測框架與績效評估
4. 交易執行與風控邏輯
5. 設定管理與監控告警
6. 部署與執行流程

## 備註

本專案目前仍在起步階段，README 會隨著功能逐步落地持續更新；實際實作與規範以程式碼與設定為準。
