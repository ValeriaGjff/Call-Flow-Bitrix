# Setup

## 1. Environment

Copy `.env.example` to `.env` and provide your own credentials.

## 2. Start n8n

```bash
docker compose up -d
```

## 3. Import workflows

Import the JSON files from `workflows/`.

All imported workflows are intentionally disabled. Review them before activation.

## 4. Configure Data Tables

Follow `data-tables.md`, then re-select each created table inside the imported Data Table nodes.

## 5. Configure CRM

Create a Bitrix24 inbound webhook with only the permissions required for the CRM/task/chat methods you actually use.

Set `BITRIX_WEBHOOK_BASE` and `BITRIX_PORTAL_URL` in `.env`.

## 6. Configure speech services

Create your own Yandex Cloud API key/folder and set `YANDEX_API_KEY` and `YANDEX_FOLDER_ID`.

## 7. Adapt routing

The public `lead_processor` contains synthetic manager IDs and extensions. Replace the demo configuration with your own CRM users.

## 8. Test

Use only synthetic phone numbers and test CRM records until the complete route has been verified.
