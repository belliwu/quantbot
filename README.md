# quantbot

開發一個幣圈投資量化機器人。

## 技術選型

| 用途 | 選型 | 一句話理由 |
| --- | --- | --- |
| 語言 | Python 3.14 | 量化生態系最完整；算得慢的部分交給 numpy 與 Numba |
| 歷史回補 | data.binance.vision | 免費、不吃 rate limit（Day 03） |
| 連線與下單 | ccxt ＋ 原生 websockets | REST signing 不自己手刻，即時資料走原生 WS 才控制得住重連（Day 03、Day 09） |
| 非同步 | asyncio ＋ httpx | 爬取與行情訂閱是 I/O bound，不用 threading；httpx 同一套 API 同時支援同步與非同步 |
| 資料處理 | pandas ＋ numpy | 全系列一律向量化，NEVER 用 for loop 遍歷 K 線 |
| 儲存 | TimescaleDB ＋ asyncpg | 時序資料要的是 hypertable 分區、時間桶聚合與壓縮（Day 07） |
| 指標 | 自己實作，pandas-ta 當對照組 | 自己算一遍才知道哪裡會錯（Day 04–06） |
| 回測 | VectorBT | 向量化，跟前面的資料處理一脈相承（Day 19） |
| 視覺化 | Plotly ＋ matplotlib | 指標與績效一定要有圖，Plotly 可以縮放看細節 |
| 加速 | Numba | 遞迴型指標向量化不掉時才用（Day 26） |
| 告警 | Telegram Bot API | 免費、有官方 API、手機直接收（Day 25） |
| 設定與密鑰 | pydantic-settings ＋ .env | API key NEVER 寫進程式碼，NEVER 進版控（Day 03） |
| 測試 | pytest | 指標與策略邏輯要有測試，尤其是邊界情況 |
| 程式碼品質 | ruff ＋ mypy ＋ import-linter | 格式、型別、以及「依賴方向有沒有長歪」都交給工具查，不靠人記 |
| 部署 | Docker ＋ Docker Compose ＋ VPS | 本機與雲端同一份映像檔（Day 27） |
