# cli.py
# typer is a python library used to build CLI applications
import typer
from scanner import run_scan

app = typer.Typer()

# Decorator that defines scan as a CLI command
@app.command()
def scan(domain: str):
  run_scan(domain)

if _name_ == "_main_":
  app()
  
