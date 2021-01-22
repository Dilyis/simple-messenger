# simple-messenger


Here is my api: https://messenger-for-heroku-p4jowicde.herokuapp.com/admin/

Also swagger is available by link: https://messenger-for-heroku-p4jowicde.herokuapp.com/docs/swagger/

API contains:
- Login by email/password     
/login POST     
Authentication through JWT
- Write message    
/messages POST
- Get all messages for a specific user   
/users/pk/messages/ GET
- Get all unread messages for a specific user    
/users/pk/messages/?unread=True GET
- Read message (return one message)    
/messages/pk/read/ POST     
It's better to have another POST method to "read" it instead of base GET method (/messages/pk/ GET), 
because it is unpredictable behaviour to change data by GET method. 
And also can be situations like this: fronted requested GET method to show message, 
end-user doesn't see the message yet, but it is already marked as read)
- Delete message (as owner or as receiver)    
/message/pk/ DELETE

Also:
- A common set of user's methods
- GET one message    
/messages/pk GET