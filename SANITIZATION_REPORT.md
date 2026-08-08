# Sanitization report

This report summarizes the transformation from the uploaded production exports to the portfolio-safe copy. It intentionally does not reproduce any secret values.

| Workflow | Cloud secret refs removed | Production CRM URLs removed | Staff/company-specific routing rewritten | n8n instance/table refs sanitized |
|---|---:|---:|---:|---:|
| `voice_dialog_name.json` | 2 | 0 | no | 3 |
| `get_transfer_info.json` | 0 | 0 | no | 2 |
| `voice_dialog_reset.json` | 0 | 0 | no | 2 |
| `voice_dialog_type.json` | 2 | 0 | no | 3 |
| `lead_processor.json` | 2 | 13 | yes | 3 |
| `save_transfer_info.json` | 0 | 0 | no | 2 |
| `stt_test_city.json` | 2 | 0 | no | 1 |
| `stt_test_type.json` | 2 | 0 | no | 1 |
| `stt_test_name.json` | 2 | 0 | no | 1 |
| `voice_dialog_city.json` | 2 | 0 | no | 4 |

## Validation

- Production cloud key value: not present in sanitized workflows.
- Production cloud folder/catalog identifier: not present.
- Production CRM portal domain/webhook tokens: not present.
- Known production staff names and chat identifiers found in the source: not present.
- Original n8n instance metadata: removed.
- Original Data Table IDs: replaced with explicit `REPLACE_WITH_..._TABLE_ID` placeholders.
- All sanitized workflows are exported as inactive.

Run `python3 scripts/secret_scan.py` again immediately before the first public push.

## Required operational action

Credentials that appeared in the original exports should be revoked/reissued before publishing this repository. Sanitizing the public copy does not make the original credentials safe.