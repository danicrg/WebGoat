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

If we try to register username tom it gives us this message.
![tom_already](../screenshots/tom_already.png)

And if we try tom' and '1'='1 we get
![tom_true_already](../screenshots/tom_true_already.png)
