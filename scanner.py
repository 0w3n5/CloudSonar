# import our modules
from modules.discovery import discover_assets
from modules.misconfig import check_s3, check_env
from modules.secret_detector import detect_secrets
from moodules.risk_engine import calculate_risks
from report.html_report import generate_report
from report.visualizer import create_graph
