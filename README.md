# WeddingBook

This website is a wedding image gallery which includes the following features:

Public (non-authenticated) users can:
 - Register themselves
 - Ask for password retrieval through email
 - See approved photos on gallery
 - Filter gallery listing by more recent pictures or by more liked pictures

Regular users can:
 - Log in/ Log out
 - Change profile/user info
 - Upload new photos
 - Like existing approved photos
 
Admin users (Wife and Husband) can:
 - See a list of non-approved pictures (Waiting List)
 - Approve or discard pictures
 - Log in to the Django's admin page


# Application Architecture

This application makes use of the Django MVC pattern, so the whole project relies on Model, View and Controller design.


# Main Technologies Used

## Programing Languages

- Python 3.6
- Django 2.1.8

Check requirements.txt file for the complete list of technologies and libraries used

## Storage

This project stores all static and media files onto Amazon S3 bucket

## Database

- MongoDB through djongo interpreter library


# Credentials format (Python Decouple)

## S3

File: `.env`

```
S3_ACCESS_ID
S3_SECRET_KEY
S3_BUCKET_NAME
```

## MongoDB

File: `.env`

```
DB_HOST
DB_USER
DB_PASSWD
```

## Google ReCaptcha

File: `.env`

```
RECAPTCHA_SITE_KEY
RECAPTCHA_SECRET_KEY
```

## Email (for password reset)

File: `.env`

```
EMAIL_USER=your@email.com
EMAIL_PASSWD=yourpassword
```

# Other variables from Python Decouple

File: `.env`

```
SECRET_KEY=djangos_secret_key
ALLOWED_HOSTS=.localhost, 127.0.0.1
DEBUG=True/False
```
