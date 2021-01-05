# Tier Url Shortener

Hey team! This repo contains the URL shortener application I was tasked to build! I chose to build the application with Flask and Used SQLite for data storage. I added some steps below to get it run on your local machine.

## Environment Variables
These will will be in the `temp.env` file you just need to copy them into a `.env` file and set a `SECRET_KEY`
`FLASK_APP`
`FLASK_ENV`
`SECRET_KEY` You can make this a random set of charectars
`SQLALCHEMY_DATABASE_URI`


## Setup

```
$ git clone https://github.com/bullmoosetr/tier_app_test.git
$ cd tier_app_test
$ . ./deploy.sh
```

## Runing The App

 ```
 $ cd tier_app/
 $ flask run
 ```

## Running

The to shorten a url is to make a POST request, I have a curl request as an example below

Creating a Shortened URL
```
curl -X POST -d 'long_url=https://URL/OF/YOUR/CHOICE.com' http://127.0.0.1:5000/shorten_url
```
If Successful you should recieve a message
`Your new shorter Url tier.app/S9FboU9`

To Use your new shorter and simpler URL,simply type the following in the browser while runing the application
`http://localhost:5000/tier.app/S9FboU9`

