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

## Programing Languages

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

Why MongoDB? A NonSQL database is not the best aproach for this project at all, but I wanted to challenge myself.


# Credentials format (Python Decouple)

## Amazon Cloudfront

```
AWS_CLOUDFRONT_DOMAIN=your_cloudfront_distribution_domain
```

## Amazon S3

File: `.env`

```
S3_ACCESS_ID
S3_SECRET_KEY
S3_BUCKET_NAME
```

## MongoDB

File: `.env`

```
DB_NAME
DB_HOST
DB_USER
DB_PASSWD
DB_PORT
```

## Google ReCaptcha

File: `.env`

```
RECAPTCHA_SITE_KEY
RECAPTCHA_SECRET_KEY
```

## Email Service (for the application to send emails through. I.e. password recovery)

File: `.env`

```
EMAIL_HOST=your_service_provider
EMAIL_PORT=smtp_or_relay_port
EMAIL_USER=your@email.com (use 'None' for non authenticated mail relay)
EMAIL_PASSWD=your_password (use 'None' for non authenticated mail relay)
EMAIL_USE_TLS=True/False
```

# Other variables from Python Decouple

File: `.env`

```
SECRET_KEY=djangos_secret_key
ALLOWED_HOSTS=.localhost, 127.0.0.1, your_app_public_domain
DEBUG=True/False
```
