# NameAPI
A API that can return random names, last names, and full names. You can technically use it for any language. We would show how to use it for python here.

Get a random first name:
```
import requests

nameReq = requests.get("http://41ad-185-219-167-75.ngrok.io/name/")
name = nameReq.text
```

Get a random last name:
```
import requests

LastNameReq = requests.get("http://41ad-185-219-167-75.ngrok.io/lastname/")
lastName = LastNameReq.text
```

Get a random full name:
```
import requests

fullNameReq = requests.get("http://41ad-185-219-167-75.ngrok.io/fullname/")
fullName = fullNameReq.text
```

NOTE: If you want to use it with a different language just request the correct url depending on what you are trying to get. (name: ```https://NameAPI.jerrylin17.repl.co/name``` last name: ```https://NameAPI.jerrylin17.repl.co/lastname``` full name\; ```https://NameAPI.jerrylin17.repl.co/fullname```)
Then use the get the text response of the request. (in python that would be ```name = requestVar.text```)

Thats basically it!
