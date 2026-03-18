import requests

def check_s3(bucket):
  url =f"https://{bucket}.s3.amazonaws.com"
  try:
    r = requests.get(url, timeout=5)
    if "ListBucketResult" in r.text:
      return True
  except:
    return False
  return False

def check_env(domain):
  paths = ["/.env", "/config.env", "/.env.backup"]
  found = []
  for p in paths:
    url =f"http://{domain}{p}"
    try:
      r = requests.get(url, timeout=5)
      if "DB_PASSWORD" in r.text:
        found.append(url)
    except:
      continue
  return found
