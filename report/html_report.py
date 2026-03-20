from jinja2 import Template

def generate_report(data, filename=CloudSonarReport.html):
  template = """
  <h1>Cloud Sonar Report for {{ domain }}</h1>
  <p>Risk Score: {{ risk_score }}</p>
  <h2>Findings</h2>
  <ul>
  {% for f in findings %}
    <li>{{ f }}</li>
  {% endfor %}
  </ul>
  """
  html = Template(template).render(data) with open(filename, "w") as f:
    f.write(html)
