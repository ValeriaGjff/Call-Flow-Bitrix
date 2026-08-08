# Architecture

The project is split into small n8n workflows instead of one monolithic flow.

## Voice stage

`stt_test_name`, `stt_test_type`, and `stt_test_city` accept audio, call STT and return synthesized audio responses.

`voice_dialog_name`, `voice_dialog_type`, and `voice_dialog_city` maintain dialog state and normalize the caller's answers.

`voice_dialog_reset` removes dialog state for a phone number.

## CRM stage

`lead_processor` receives the final normalized dialog result and:

1. normalizes lead data;
2. chooses a routing candidate;
3. searches CRM for a duplicate by phone;
4. preserves an existing active owner where appropriate;
5. creates or updates the lead;
6. adds timeline information;
7. creates a callback task;
8. sends a CRM notification;
9. stores the final transfer extension.

## PBX transfer stage

`save_transfer_info` stores the resolved transfer route.

`get_transfer_info` lets the PBX retrieve the route by normalized phone number.

## Public-edition differences

The public edition deliberately replaces:
- production CRM URLs and webhook tokens with environment variables;
- real staff identities and CRM IDs with synthetic managers;
- the real duty schedule with a deterministic demo rotation;
- n8n instance/table IDs with placeholders;
- real service cities with `City A` and `City B`.
