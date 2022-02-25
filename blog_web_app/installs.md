# Installs
`pip install flask`
`pip install wtf` - wt forms
`pip install email_validator`

# Commands
- `export FLASK_APP=flask_blog.py` : Environment variable that enables us to just type "flask run" to initialize local server
- `export FLASK_DEBUG=1` - turns on live server reload
*Running the environment variables is necessary every time you reload terminal. Use the code below to not have to enter environment variables each time.*
```
if __name__ = '__main__': 
    app.run(debug=True)
```
