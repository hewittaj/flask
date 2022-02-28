# Installs within regular terminal
- `pip install flask`
- `pip install wtf` - wt forms
- `pip install email_validator`
- `pip install flask-sqlalchemy`
- `pip install flask-bcrypt` - encryption
- `pip install flask-login` - handles user login sessions

# Commands ran within regular terminal
- `export FLASK_APP=flask_blog.py` - Environment variable that enables us to just type "flask run" to initialize local server

- `export FLASK_DEBUG=1` - Turns on live server reload
    - *Running the environment variables is necessary every time you reload terminal. Use the code below to not have to enter environment variables each time.*
    ```
    if __name__ = '__main__': 
        app.run(debug=True)
    ```

## Run within python terminal

### DB Commands
- `from flask_blog import db` - Imports sqlalchemy db file that we created in flask_blog.py
    - `db.create_all()` - Creates database `site.db`

- Creating a user:
    1. `user_1 = User(username="Alex", email="test@email.com", password="password")` - Creation of a user
    2. `db.session.add(user_1)` - Add change request to DB (doesn't actually add to db)
    3. `db.session.commit()` - Commit changes to database
    4. `User.query.all()` - Returns query of DB
    5. `User.query.first()` - Returns first value
    6. `User.query.filter_by(username="Test").all()` - Returns query specified by filter
    7. `user = User.query.get(1)` - Returns query where user.id equals 1
    8. `user.posts` - Returns posts from specific user
    9. `post_1 = Post(title="Blog one", content = "My first blog", user_id=user.id)` - Creates and associates post with a user

### Class Commands
- `from flask_blog import User, Post` - Imports User, Post db info

### Encryption Commands
1. `from flask_bcrypt import Bcrypt`
2. `bcrypt = Bcrypt()`
3. `bcrypt.generate_password_hash('test')` - can add `.decode('utf-8')` to the end to change from bytes to a string
    - `hashed_pw = bcrypt.generate_password_hash('test')` - store to variable
4. `bcrypt.check_password_hash(hashed_pw, 'password')` 
    - ^ will return false since our password is 'test' 
    - `bcrypt.check_password_hash(hashed_pw, 'test')` - will return true
