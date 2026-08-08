#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

PATTERNS = {
    "possible API key": re.compile(r"\b(?:AQV|AIza|sk-|ghp_|xox[baprs]-)[A-Za-z0-9_\-]{12,}\b"),
    "Bitrix webhook token": re.compile(r"https://[^/\s]+\.bitrix24\.[^/\s]+/rest/\d+/[A-Za-z0-9]+/"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "possible bearer token": re.compile(r"Authorization[^\n]{0,80}Bearer\s+[A-Za-z0-9._\-]{16,}", re.I),
}

SKIP = {".git", ".venv", "venv", "__pycache__"}
findings = []

for path in ROOT.rglob("*"):
    if not path.is_file() or any(part in SKIP for part in path.parts):
        continue
    if path.resolve() == Path(__file__).resolve():
        continue
    if path.name == ".env":
        findings.append((path, ".env must not be committed"))
        continue

    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue

    for label, pattern in PATTERNS.items():
        if pattern.search(text):
            findings.append((path, label))

if findings:
    print("SECRET SCAN FAILED")
    for path, reason in findings:
        print(f"- {path.relative_to(ROOT)}: {reason}")
    sys.exit(1)

print("SECRET SCAN PASSED")
