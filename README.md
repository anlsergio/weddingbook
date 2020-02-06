# WeddingBook

This website is a wedding image gallery which includes the following features:

Public (non-authenticated) users can:
 - Register themselves
 - Ask for password recovery (email)
 - See approved photos on gallery
 - Filter gallery listing by most recently posted or by most liked pictures

Regular users can:
 - Log in/ Log out
 - Change profile/user info
 - Upload new photos
 - Like existing approved photos
 
Admin users (Wife and Husband) can:
 - See a list of non-approved pictures (Waiting List)
 - Approve or discard pictures
 - Log into Django's admin page


# Application Architecture

This application makes use of the Django MVC pattern, so the whole project relies on Model, View and Controller design.

It also makes use of Django Rest Framework (DRF) for AJAX capabilities.


# Main Technologies Used

- Python 3.6
- Django 2.1.8
- Django Rest Framework
- MongoDB
- Amazon Cloudfront
- Amazon S3

Check `requirements.txt` file for the complete list of technologies and libraries used

## Storage

This project stores all static and media files onto Amazon S3 bucket which are served by Cloudfront.

## Database

- MongoDB through djongo interpreter library

Why MongoDB? A NoSQL database is not the best approach for this project at all, but I wanted to challenge myself.


# Parameters (Environment Variables)

The parameters below are supposed to be provided as environment variables.

## Amazon Cloudfront

```
AWS_CLOUDFRONT_DOMAIN=your_cloudfront_distribution_domain
```

## Amazon S3

```
S3_ACCESS_ID
S3_SECRET_KEY
S3_BUCKET_NAME
```

## MongoDB

```
DB_NAME
DB_HOST
DB_USER
DB_PASSWD
DB_PORT
```

## Google ReCaptcha

```
RECAPTCHA_SITE_KEY
RECAPTCHA_SECRET_KEY
```

## Email Service (for the application to send emails through. I.e. password recovery)

```
EMAIL_HOST=your_service_provider
EMAIL_PORT=smtp_or_relay_port
EMAIL_USER=your@email.com (use 'None' for non authenticated mail relay)
EMAIL_PASSWD=your_password (use 'None' for non authenticated mail relay)
EMAIL_USE_TLS=True/False
```

# Other necessary variables

```
SECRET_KEY=djangos_secret_key
ALLOWED_HOSTS=.localhost, 127.0.0.1, your_app_public_domain
DEBUG=True/False
```

# Running the application as a Docker container

## Build image

In order to run this app as a Docker container, you can just run a docker build command to generate an image for the application and it should be good to go.


# Running the application as a Docker container

## Build the Docker image

In order to run this app as a Docker container, you may just run a [docker build](https://docs.docker.com/engine/reference/commandline/build/) command to generate an image for the application and it should be good to go.
> For example: **`docker build -t asergio/weddingbook:latest .`**


## Docker Compose

Be sure to inject all the necessary variables during the service definition inside your **`docker-compose.yaml`** file.
> More information on [Docker Compose reference page](https://docs.docker.com/compose/).
