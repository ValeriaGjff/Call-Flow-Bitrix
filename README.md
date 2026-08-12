# Call Flow Bitrix

A system for automatic processing and routing of incoming calls with telephony integration, n8n and Bitrix24.

The project automates the entire process of handling an incoming call: from receiving the call and speech recognition to determining the client type, searching for the client in the CRM, selecting the responsible manager, and transferring the data for call transfer.

## Task
### When there is a large number of incoming calls, manual routing creates several problems:

- the operator needs to determine who is calling;
- to understand whether the client is an individual or a legal entity;
- check whether the client exists in the CRM;
- determine the current responsible person;
- transfer the call.

The goal of the project is to automate this process and reduce the manual actions performed by employees.

## The system’s actions

- accepts an event from telephony;
- starts a voice dialogue;
- converts the client’s speech into text using Speech-to-Text;
- determines: client name, client type, city;
- searches for an existing client or lead in the CRM;
- checks the current responsible person;
- saves the selected internal manager number;
- creates the CRM events, tasks and messages.

## Architecture

```mermaid
flowchart TD
   A[Incoming call] --> B[Telephony]
   B --> C[Voice Dialog]
   C --> D[Speech-to-Text]

   D --> E[Definition of a name]
   E --> F[Determining the client type]
   F --> G[Definition of a city]

   G --> H[Lead Processor]

   H --> [Phone number normalization]
   I --> J[Searching for a client in CRM]

   J --> K{Has the client been found?}

   K -- Yes --> L{Is the responsible person active?}
   K -- No --> M[Choosing a new responsible person]

   L -- Yes --> N[Keep the current responsible person]
   L -- No --> M

   M --> O[Routing Policy]
   O --> P[Main manager]
   O --> Q[Reserve manager]

   N --> R[Creation / lead update]
   P --> R
   Q --> R

   R --> S[Saving transfer info]
   S --> T[PBX get extension]
   T --> U[Transferring the call to the manager]
```

## Quick start

1. Clone the repository.
2. Copy environment template:

```bash
cp .env.example .env
```

3. Fill in your own credentials and public URLs.
4. Start n8n:

```bash
docker compose up -d
```

5. Open n8n and import JSON files from `workflows/`.
6. Create the required n8n Data Tables using `docs/data-tables.md`.
7. In imported Data Table nodes, select the tables you created.
8. Configure your PBX/telephony provider to call the documented webhooks.

## Important configuration

The exported workflows intentionally contain placeholders such as:

```text
REPLACE_WITH_VOICE_DIALOG_STATE_TABLE_ID
REPLACE_WITH_TRANSFER_TARGETS_TABLE_ID
REPLACE_WITH_LEAD_DUTY_QUEUE_TABLE_ID
```

After importing the workflows, open each Data Table node and select the appropriate table in your own n8n instance.

CRM and cloud secrets are read from environment variables rather than stored in workflow JSON.

## Repository layout

```text
crm-call-router/
├── workflows/          Sanitized n8n workflow exports
├── config/             Example routing configuration
├── examples/           Synthetic webhook payloads
├── docs/               Architecture and deployment notes
├── scripts/            Local security scan
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md
```

## Demo routing policy

The public version intentionally uses synthetic managers (`Manager A`, `Manager B`, etc.) and a deterministic demo duty rotation. Replace it with your own schedule, database lookup or workforce-management API.

The routing behavior retained from the implementation is:

- a new B2B lead is assigned according to the routing policy;
- B2C leads are assigned to a configured B2C manager;
- an existing lead owned by an active manager keeps that manager;
- an existing lead with an inactive/unknown owner is reassigned;
- transfer extensions are stored for the PBX to retrieve.

## Security

Never commit `.env` or production workflow exports. Run:

```bash
python3 scripts/secret_scan.py
```

before every public push.

See `SECURITY.md`.
