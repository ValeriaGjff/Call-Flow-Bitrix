# Security

This repository must never contain production credentials or personal/customer data.

## Before publishing

- rotate any key or CRM webhook token that has ever appeared in an exported production workflow;
- do not commit `.env`;
- do not commit SSH/private keys;
- do not commit CRM exports, call recordings, transcripts, logs or customer phone numbers;
- do not publish real staff names, extensions, schedules or internal user IDs;
- do not publish production domains/IP addresses unless explicitly intended;
- run `python3 scripts/secret_scan.py`.

## Credential rotation

The source workflows used to create this portfolio edition contained embedded cloud and CRM credentials. Those original credentials should be revoked/reissued before the repository is made public.

## Reporting

If you discover a credential in repository history, remove it from history and rotate it. Deleting it in a later commit is not sufficient.
