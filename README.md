To set up virtual environment:
1. create a project directory then change directory:

```
mkdir ~/Developer/project_name
cd ~/Developer/project_name
```

2. create a virtual environment

`python3 -m venv venv`

The second 'venv' in the above command is the environment name and so can be named anything.

3. install flask in the virtual environment

```
source venv/bin/activate
pip install flask
```

4. Export global venv variable

`export FLASK_APP=microblog.py`

If you wish to avoid running the export command above, within the venv run

```
pip install python-dotenv
cat "FLASK_APP=microblog.py">.flaskenv
```

5. Run the flask project

`flask run`

6. Install flask package WTF
'pip install flask-wtf'

7. Install Flask SQLAlchemy and migrate packages
'pip install flask-sqlalchemy'
'pip install flask-migrate'
'pip install flask-dotenv'
'pip install flask-login'
'pip install flask-mail'
'pip install pyjwt'
'pip install flask-bootstrap'
'pip install flask-moment'
