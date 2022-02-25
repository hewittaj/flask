# Installs within regular terminal
`pip install flask`
`pip install wtf` - wt forms
`pip install email_validator`
`pip install flask-sqlalchemy`

# Commands ran within regular terminal
- `export FLASK_APP=flask_blog.py` - Environment variable that enables us to just type "flask run" to initialize local server

- `export FLASK_DEBUG=1` - Turns on live server reload
    - *Running the environment variables is necessary every time you reload terminal. Use the code below to not have to enter environment variables each time.*
    ```
    if __name__ = '__main__': 
        app.run(debug=True)
    ```

## Run within python terminal
- `from flask_blog import db` - Imports sqlalchemy db file that we created in flask_blog.py
    - `db.create_all()` - Creates database `site.db`

- `from flask_blog import User, Post` - Imports User, Post db info

- `user_1 = User(username="Alex", email="test@email.com", password="password")` - Creation of a user
    - `db.session.add(user_1)` - Add change request to DB (doesn't actually add to db)
    - `db.session.commit()` - Commit changes to database
    - `User.query.all()` - Returns query of DB
    - `User.query.first()` - Returns first value
    - `User.query.filter_by(username="Test").all()` - Returns query specified by filter
    - `user = User.query.get(1)` - Returns query where user.id equals 1
    - `user.posts` - Returns posts from specific user
    - `post_1 = Post(title="Blog one", content = "My first blog", user_id=user.id)` - Creates and associates post with a user
