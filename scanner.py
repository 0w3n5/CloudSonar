# import our modules
from modules.discovery import discover_assets
from modules.misconfig import check_s3, check_env
from modules.secret_detector import detect_secrets
from moodules.risk_engine import calculate_risks
from report.html_report import generate_report
from report.visualizer import create_graph

def run_scan(domain): 
  print(f"[+] Discovery assets for {domain} ...")
  print(f"[+] Found {len(subdomains)} subdomains.")
  
  findings = {"public_bucket": False, "env_exposed": [], "secrets": []}
  nodes = []

  for sub in subdomains:
    if check_s3(sub):
      findings["public_bucket"] = True
    env_files = check_env(sub)
    if env_files:
      findings["env_exposed"].extend(env_files)
    for f in env_files:
      content = "DB_PASSWORD=123"   # Placeholder for Demo
      secrets = detecy_secrets(content)
      findings["secrets"].extend(secrets)
      nodes.append(("domain", sub))

    risk_score = calculate_risk(findings)
    generate_report({"domain": domain, "risk_score": risk_score, "findings": findings}, "report.html")
    create_graph(nodes)

print(f"[+] Scan complete! Risk Score:{risk_score}")
print("[+] HTML report saved as CloudSonarReport.html")
print("[+] Attack surface graph saved as attack_surface.png")
