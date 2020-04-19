from datetime import datetime, timedelta
import app
from app import db
from app.models import User, Post

users = [
    {
        'user': User(username='john-data', email='john@example-data.com'),
        'password': 'cat'
    },
    {
        'user': User(username='susan-data', email='susan@example-data.com'),
        'password': 'dog'
    },
    {
        'user': User(username='mary-data', email='mary@example-data.com'),
        'password': 'brown'
    },
    {
        'user': User(username='david-data', email='david@example-data.com'),
        'password': 'animal'
    }
]

def dev_add_users():
    ul = []
    for user in users:
        user['user'].set_password(user['password'])
        ul.append(user['user'])
    db.session.add_all(ul)
    db.session.commit()

def dev_show_users():
    dev_users = db.session.execute('SELECT username FROM user WHERE username LIKE "%-data"')
    if dev_users:
        for u in dev_users.fetchall():
            print(u[0])
    else:
        print('No dev_users in database')

def dev_remove_users():
    for user in users:
        db.session.execute('DELETE FROM user WHERE username="{}"'.format(user['user'].username))
    db.session.commit()

posts = [
    {
        'body': 'This is the best planet',
        'author': users[0]['user'],
        'timestamp': datetime.utcnow()+timedelta(seconds=2)
    },
    {
        'body': 'I know right!?',
        'author': users[2]['user'],
        'timestamp': datetime.utcnow()+timedelta(seconds=4)
    },
    {
        'body': 'Yo, how do you know this is the best one? How many have you been on??',
        'author': users[1]['user'],
        'timestamp': datetime.utcnow()+timedelta(seconds=27)
    },
    {
        'body': 'A million and a half man... time travel',
        'author': users[0]['user'],
        'timestamp': datetime.utcnow()+timedelta(seconds=50)
    },
    {
        'body': 'of course. mah bad',
        'author': users[1]['user'],
        'timestamp': datetime.utcnow()+timedelta(seconds=53)
    }
]

def dev_create_posts():
    ups = []
    for post in posts:
        p = Post(body=post['body'], author=post['author'], timestamp=post['timestamp'])
        ups.append(p)
    db.session.add_all(ups)
    db.session.commit()

def dev_show_posts():
    posts = db.session.execute('SELECT * FROM post as p WHERE p.author.username LIKE "%-data"')
    for post in posts:
        print(post)

def dev_remove_posts(arg):
    for post in posts:
        db.session.execute('DELETE FROM post WHERE author={}'.format(post['author']))
    db.session.commit()
