# Personal Media OS

把個人品牌訪談、日常素材、跨平台草稿、逐篇審核與發布回寫，變成一套可攜的 AI 工作流程。

**狀態：v0.1 流程套件。** 含 Skill、導入提示詞、Notion 結構指南與可執行的本機初始化工具。沒有內建社群發布 API、排程 worker 或跨帳號登入；目前未完成不同帳號的端到端驗證。

## 一句話開始

下載此 repo，將 `START-HERE.md` 和 `skills/personal-media-os/` 的內容交給能讀取附件的 ChatGPT，輸入：

> 請依照 START-HERE.md 導入 Personal Media OS。先檢查可用工具，再訪談我的目標、受眾和口吻；優先沿用我的內容庫。先建立可審核的草稿，不發布。

這是一個**導入入口提示詞**，不是能在所有 ChatGPT 帳號中自動安裝外掛的指令。登入、連線、目的地與必要權限仍由使用者完成。若聊天無法讀取 repo，下載後上傳文件；單貼 GitHub 連結不保證能讀到全部檔案。

### 有 Skills 的環境

使用該環境提供的 Skills 安裝方式匯入 `skills/personal-media-os/`；安裝後選取 Personal Media OS，輸入「幫我建立個人社群工作區」。

Codex 可貼上這一句：

> 請用 skill-installer 從 https://github.com/SuBoYu/personal-media-os 的 skills/personal-media-os 安裝技能，再用它幫我導入個人社群工作區。先訪談，不發布。

私人 repo 需使用者本身有存取權。一般 ChatGPT 不保證有 skill-installer；沒有時請走上方附件入口。

### 本機一個命令

在下載的 repo 目錄執行（Python 3.9+，無第三方套件）：

```sh
python3 scripts/media_os.py init --workspace ./workspace
```

產生私人工作區及空白品牌資料，然後交給 AI 訪談補齊。重跑不覆寫資料；不會連線 Notion 或登入社群。`workspace/` 已排除於 Git。

## 你會得到什麼

- 先討論「希望誰認識我、帶來什麼關係、什麼不像自己」，再決定內容方向。
- 分開管理原始故事、問題選題與各平台版本；計畫本身不混成待發貼文。
- 先選一個平台與一篇內容跑通流程，再按需要擴展 Threads、IG、Facebook、LinkedIn、X。
- 每份核准綁定帳號、文字、附件、標籤和時間；修改就重新確認。
- 只有在平台確認成功後才回填網址與時間；結果不明先查證，避免重複。
- 沒有 Notion／瀏覽器／發布權限也能先產生本機草稿與手動操作步驟。

## 入口

| 文件 | 用途 |
| --- | --- |
| [START-HERE.md](START-HERE.md) | AI 導入入口 |
| [Skill](skills/personal-media-os/SKILL.md) | 可重用工作流程 |
| [Notion 指南](skills/personal-media-os/references/notion.md) | 資料庫、沿用及去重 |
| [發布流程](skills/personal-media-os/references/publishing.md) | 預覽、核准、回寫及刪除 |
| [產品範圍](docs/PRODUCT.md) | MVP、限制、驗收與後續路線 |

## 驗證與打包

```sh
python3 -m unittest discover -s tests -v
python3 scripts/media_os.py package --output ./dist
```

只打包明確列出的 Skill 資源；不含 workspace、Git 紀錄或個人素材。打包不等於已被任何平台安裝或接受。

## 隱私

使用者自行登入官方網站或完成 OAuth；本專案不接收 cookies、session、密碼、OTP 或 tokens。個人素材、帳號對應、Notion ID 與發布紀錄放在私人工作區，提交 Git 前需檢查。Repo 內示例均為虛構資料。

## 官方能力依據

- [Build skills](https://learn.chatgpt.com/docs/build-skills)：Skill 格式、選取方式與可用安裝路徑。
- [ChatGPT on the web](https://learn.chatgpt.com/docs/web)：可用工具及技能依使用環境而定。

本專案與 OpenAI、Notion 或社群平台沒有官方隸屬關係。各平台操作能力需在使用者環境實測。
