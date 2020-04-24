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

5. Run the flask project.
`flask run`

This command will start a SQLAlchemy server to run your application with.

<!-- TODO: add directions for password reset by e-mail -->

##For L18n and L10n language support:
1. To support a new language:
`flask translate init [LANG]`

2. Translate the .po file that is generated with the `init` command. [poedit](https://poedit.net/) is a popular open-source translation application.

3. Compile the .po translations using the following command:
`flask translate compile`

If you want to check to see that the translations worked, you have two options:
  1. Change the language setting of your browser, or
  2. Change the get_locale() method in `app/__init__.py` file to return es (`return es`)

###Updating an existing translation
1. Run the update procedure:
`flask translate update`
