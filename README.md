# microblog
## Setting things up
To set up virtual environment:
1. create a project directory then change directory:

```
mkdir ~/Developer/project_name
cd ~/Developer/project_name
```

2. create a virtual environment

`python3 -m venv venv`

The second 'venv' in the above command is the environment name and so can be named anything.

3. Run the virtual environment:

```
source venv/bin/activate
```

4. Within the `(venv)` install all dependencies:

`pip install -r requirements.txt`

Note: Moving forward, ALL commands should be issued from within the virtual environment created in step 2. Fresh command lines should now start with `(venv)`. For the sake of convenience, I will leave the prompt heading off and simply give commands that can be easily be copied and pasted.


This command will start a SQLAlchemy server to run your application with.
5. There are several services that must be setup before the project can run in it's full glory. Microblog is configured to read from a `.env` file, so this is where we can store several environment variables if they are not already set in your user environment. In the root folder of this project with run
`touch .env`

then add the following:
```
<!-- contents of .env -->
SECRET_KEY=a-really-long-and-unique-key-that-nobody-knows
MAIL_SERVER=localhost
MAIL_PORT=8025
MAIL_USE_TLS=
MAIL_USERNAME=
MAIL_PASSWORD=
MS_TRANSLATOR_KEY=<your-translator-key-here>
ELASTICSEARCH_URL=http://localhost:9200
```

 For each of the following services, open a new terminal tab (tabs are more convenient for grouping) and run the command:
#### SMTP debugging server:
`python3 -m smtpd -n -c DebuggingServer localhost:8025`

Note: this runs a SMTP (Simple Mail Transport Protocol) server on localhost 8025.

#### Elasticsearch
`elasticsearch`

#### Redis Server
`redis-server`

#### Redis worker
`rq worker microblog-tasks`
<!-- TODO: add directions for password reset by e-mail -->

6. Run the flask project.

`flask run`

7. Open an internet browser and go to `http://localhost:5000`

## For L18n and L10n language support:
1. To support a new language:

`flask translate init [LANG]`

2. Translate the .po file that is generated with the `init` command. [poedit](https://poedit.net/) is a popular open-source translation application.

3. Compile the .po translations:

`flask translate compile`

If you want to check to see that the translations worked, you have two options:
  1. Change the language setting of your browser, or
  2. Change the get_locale() method in `app/__init__.py` file to return es (`return es`)

1. Update:

`flask translate update`
