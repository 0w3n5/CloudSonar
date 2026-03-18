import subprocess

def discover_assets(domain):
  subdomains = []
  try:
    results = subprocess.run(
      ["amass", "enum", "-passive", "-d", domain],
      capture_output=True, text=True, check=True)
    output = result.stdout.splitlines()
    subdomains = list(set([line.strip() for line in output if line.strip()]))
  except subprocess.CalledProcessorError as e:
    print(f"Error running Amass: {e}")
  return subdomains
          
      
