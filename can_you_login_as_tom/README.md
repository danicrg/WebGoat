# Can you login as tom?
SQLi

## Challenge

> We now explained the basic steps involved in an SQL injection. In this assignment you will need to combine all the things we explained in the SQL lessons.\
> Goal: Can you login as Tom?\
> Have fun!

![Login](../screenshots/login.png)
![Register](../screenshots/register.png)

## Solution
We will exploit the register window.

If we try to register username `tom` it gives us this message.
  User tom alreay exists please try to register with a different username.

And if we try `tom' and '1'='1` we get
  User tom' and '1'='1 alreay exists please try to register with a different username.
  
If we try another username such as `daniel' or '1'='1`:
  User daniel' or '1'='1 alreay exists please try to register with a different username.

But user daniel does not really exist because when running `daniel`we get:
  User daniel created, please proceed to login page





