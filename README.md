# Insta-autoDM

<a href="https://www.instagram.com/harshithlaxman/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Instagram_logo.svg/1200px-Instagram_logo.svg.png" alt="Auto DMer"/></a>



## Preparations

* Open DMer.py File and Edit The Following Lines:

1) `username = 'USERNAME'  # Enter your username here` 

2) `password = 'PASSWORD'  # Enter your password here` 

3) `scheduledtime = "00:07:00"  # Specific Time (in 00:00:00 format) When The message will be send` 

4) `textbox.send_keys(f"Hi @{usrnames} ! What's up ?")  # Messege that you want to send` 

5) `usrnames = ['username1', 'username2']  # username whom you will send the message`


Ensure that you have Chrome installed and the
[`chromedriver` ](https://chromedriver.chromium.org/downloads) that matches
your Chrome version available on your `$PATH`. You may have to update this from time to time.

# Requirements
* Python (added to path)
* The Requests Library for python : `pip install requests`
* Selenium 

``` bash
pip install selenium
```

* Schedule

```bash
pip install schedule
```


Or just install alll the packeges via requirements.txt file

```bash
pip install -r requirements.txt
```

#Run
* Run the program using:

```bash
python  DMer.py
```
