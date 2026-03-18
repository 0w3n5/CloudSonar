# Simplified Scoring, CVSS will get implemented later

def calculate_risk(findings):
  score = 0
  if findings.get("public_bucket"): score += 4
  if findings.get("env_exposed"): score += 4
  if findings.get("secrets"): score += 5
  if findings.get(sensitive_files): score += 3
  return min(score, 10)
