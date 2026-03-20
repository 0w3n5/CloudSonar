import re

patterns = [
  r"AKIA[0-9A-Z]{16}", 
  r"-----BEGIN PRIVATE KEY-----", 
  r"(?i)api[_-]?key.{0,20}[0-9a-zA-Z]{16,}"
]

def detect_secrets(text):
  findings = []
  for p in patterns:
    if re.search(p, text):
      findings.append(p)
  return findings
