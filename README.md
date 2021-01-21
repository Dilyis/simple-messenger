# simple-messenger


Here is my api: https://messenger-for-heroku-p4jowicde.herokuapp.com/admin/

Also swagger is available by link: https://messenger-for-heroku-p4jowicde.herokuapp.com/docs/swagger/

API contains:
- Login by email/password     
/login POST
- Write message    
/messages POST
- Get all messages for a specific user   
/users/pk/messages/ GET
- Get all unread messages for a specific user    
/users/pk/messages/?unread=True GET
- Read message (return one message)    
/message/pk/ GET     
If receiver get message at least once, message "unread" field changes to False (by default True)
- Delete message (as owner or as receiver)    
/message/pk/ DELETE
- Also list of user's methods