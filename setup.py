# Sets up project scaffold
# Written by Nicholas Cannon
import os, shutil
from sys import argv

def main():
  if len(argv) < 2:
    print('Please supply a project name')
    exit()

  ans = input('Did you run this from the parent dir of flask-scaffold? (y/n): ')

  if ans != 'y':
    print('Please do it then!')
    exit()

  print('\n')
  print('*'*80)
  print('INITIATING PROJECT SETUP')

  PROJECT_NAME = argv[1]
  PACKAGE_NAME = PROJECT_NAME.replace('-', '_')

  # Rename project directory
  print('Renaming project directory')
  os.rename('flask-scaffold', PROJECT_NAME)
  os.chdir(PROJECT_NAME)
  print('Successfully renamed project directory')

  cwd = os.getcwd()

  # Setup virtual environment
  os.system('python3 -m venv env')
  print('Created virtual environment in env/')

  # Rename scaffold package
  os.rename('flask_scaffold', PACKAGE_NAME)
  print('Project package renamed')

  print('Rewriting run.py file')
  # remove old package name from run.py
  with open(os.path.join(cwd, 'run.py'), 'r+') as f:
    data = f.read().replace('flask_scaffold', PACKAGE_NAME)
    f.seek(0)
    f.write(data)
    f.truncate()

  # Remove Scaffold .git file
  if os.path.exists(os.path.join(cwd, '.git')):
    shutil.rmtree(os.path.join(cwd, '.git'))
    print('Removed old .git file')
  
  # Remove README.md
  if os.path.exists(os.path.join(cwd, 'README.md')):
    os.unlink('README.md')
    print('Removed old README file')

  os.system('git init')
  print('Initialized new git repo!')

  print('Activating env and installing dependencies')
  os.system('source env/bin/activate; pip install --upgrade pip; pip install flask flask_sqlalchemy; pip freeze > requirements.txt')

  # Delete this script!
  os.remove(os.path.join(os.getcwd(), 'setup.py'))
  print('Deleted setup.py')

  print('\n')
  print('*'*80)
  print('Successfully set up project directory!')
  print(f'1. Move to project dir with cd {PROJECT_NAME}')
  print('2. Activate virtual env with source env/bin/activate')
  print('3. Run server with python run.py')
  print('4. Create .env file and add FLASK_ENV=development (if in dev mode)')
  print('*'*80)

if __name__ == '__main__':
  main()