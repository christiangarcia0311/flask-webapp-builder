import os
import sys
import shutil
import time 

class FlaskWeb:
  def __init__(self, project_name):
    self.project_name = project_name
    self.current_directory = os.getcwd()
    self.project_path = os.path.join(self.current_directory, self.project_name)
    self.template_folder = os.path.join(self.project_path, 'templates')
    self.static_folder = os.path.join(self.project_path, 'static')
    self.assets_folder = os.path.join(self.static_folder, 'assets')
    self.fonts_folder = os.path.join(self.static_folder, 'fonts')
    
  def project_structure(self):
    os.makedirs(self.project_path, exist_ok=True)
    
    self.app_script()
    self.folder_template()
    self.folder_static()
    self.server_script()
    
    time.sleep(3)
    print('\033[94mGenerating flask-project-template...\033[0m')
    time.sleep(2)
    print(f'Flask project \033[94m{self.project_name}\033[0m successfully created.')
    time.sleep(1)
    print(f'See project: \033[92m{self.current_directory}\033[0m')
  
  def app_script(self):
    file_content = '''from flask import Flask, render_template
    
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=5000, debug=True)
'''
    
    with open(os.path.join(self.project_path, 'app.py'), 'w') as f:
      f.write(file_content)
    
  def folder_template(self):
    os.makedirs(self.template_folder, exist_ok=True)
    
    file_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='main.css') }}">
  <link rel="icon" href="{{ url_for('static', filename='assets/icon.jpg') }}" type="image/x-icon" />
  <title>Flask App</title>
</head>
<body>
  <div class="container">
    <div class="content">
      <img class="logo" src="{{ url_for('static', filename='assets/logo.png') }}" alt="logo" /> 
      <h1 class="title-text">Flask</h1>
      <p class="description">Welcome to your first Flask web app</p>
      <p class="link-text">Visit <a href="https://github.com/christiangarcia0311/flask-webapp-builder" class="link">github</a> for documentation.</p>
    </div>
  </div>
  <script src="{{ url_for('static', filename='main.js') }}"></script>
</body>
</html>
'''

    with open(os.path.join(self.template_folder, 'index.html'), 'w') as f:
      f.write(file_content)
  
  def folder_static(self):
    os.makedirs(self.static_folder, exist_ok=True)
    os.makedirs(self.assets_folder, exist_ok=True)
    os.makedirs(self.fonts_folder, exist_ok=True)
    
    shutil.copy(os.path.join(os.path.dirname(__file__), 'data_assets/logo.png'), os.path.join(self.assets_folder, 'logo.png'))
    shutil.copy(os.path.join(os.path.dirname(__file__), 'data_assets/icon.jpg'), os.path.join(self.assets_folder, 'icon.jpg'))
    shutil.copy(os.path.join(os.path.dirname(__file__), 'data_assets/Rubik-Regular.ttf'), os.path.join(self.fonts_folder, 'Rubik-Regular.ttf'))
    
    css_file_content = '''@font-face {
  font-family: Primary;
  src: url(fonts/Rubik-Regular.ttf);
}
body {
  background: #fbfbf9;
  font-family: Primary;
  margin: 0;
  padding: 0;
}
.container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}
.content {
  text-align: center;
}
.logo {
  height: 120px;
  width: 120px;
}
.title-text, .description, .link-text {
  color: #333;
}
.link {
  text-decoration: none;
  color: #2393CC;
}
'''
  
    with open(os.path.join(self.static_folder, 'main.css'), 'w') as f:
      f.write(css_file_content)
    
    js_file_content = '''document.addEventListener('DOMContentLoaded', function() {
  console.log("Welcome to your first flask web app!");
});
'''
  
    with open(os.path.join(self.static_folder, 'main.js'), 'w') as f:
      f.write(js_file_content)
  
  def server_script(self):
    file_content = '''#!/usr/bin/env python3
import os 
import subprocess

def run_flask_web():
  project_directory = os.path.dirname(os.path.abspath(__file__))
  os.chdir(project_directory)
  subprocess.run(["python", "app.py"])

if __name__ == "__main__":
  run_flask_web()
'''

    run_server_script = os.path.join(self.project_path, 'run-server')
    with open(run_server_script, 'w') as f:
      f.write(file_content)
    os.chmod(run_server_script, 0o755)
    
    
def main():
  if len(sys.argv) != 2:
    print("Usage: build-flask-webapp [project name]")
    sys.exit(1)
  
  project_name = sys.argv[1]
  flask_webapp = FlaskWeb(project_name)
  flask_webapp.project_structure()

if __name__ == "__main__":
  main()