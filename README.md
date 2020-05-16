# Byteblog

![Size](https://img.shields.io/github/repo-size/2kabhishek/Byteblog?style=plastic&color=green&label=Size)
![Updated](https://img.shields.io/github/last-commit/2kabhishek/Byteblog?style=plastic&color=red&label=Updated)
![License](https://img.shields.io/github/license/2kabhishek/Byteblog?style=plastic&color=lightgrey&label=License)
![Stars](https://img.shields.io/github/stars/2kabhishek/Byteblog?style=plastic&color=ffd500&label=Stars)
![Forks](https://img.shields.io/github/forks/2kabhishek/Byteblog?style=plastic&color=brightgreen&label=Forks)
![Watchers](https://img.shields.io/github/watchers/2kabhishek/Byteblog?style=plastic&color=orange&label=Watchers)
![Contributors](https://img.shields.io/github/contributors/2kabhishek/Byteblog?style=plastic&color=ff69b4&label=Contributors)
![Followers](https://img.shields.io/github/followers/2kabhishek?style=plastic&color=blue&label=Followers)

Byteblog is a minimalist micro-blogging platform built with Pyhton Flask for anyone seeking a quieter "Social Media".
A user can easily register for Byteblog with their email id and password and then can easily share their bytes (similar to tweets in twitter) and also follow other people to read their thoughts, users can also message other users who follow them.

[Visit](https://byteblog.herokuapp.com)

## Features

- Posts
- Follow/Unfollow Users
- Messages
- Notifications

It was created to learn about various concepts of web application development including concepts like authentication, localization, deployments, testing, REST API building etc.

## Technologies Used

- Python Flask
- SQL Alchemy
- Bootstrap
- WTForms
- Moment.js
- More including various flask plugins

### Technical Features

Here are a few technical highlights of Byteblog.

- Modular Design:
Built with Flask Blueprint to promote code reusability and modular design, parts of this project can be integrated into other projects without much changes.

- Universal Database Support:
Uses SQL Alchemy for database interactions and can work with any database.

- Migrate Database:
Built with Flask Migrate to aid in database migrations, a database migration can be done with one simple command `flask db upgrade`.

- Universal Deployment:
Byteblog comes with all the configurations so that it can be deployed locally, on Docker, on VirtualBox and Heroku.

- Ephemeral Database:
Byteblog's production deployment on Heroku uses an ephemeral database which guarantees user data security and privacy.

- REST API Support:
Byteblog has JSON API support added to it so developers can add new API routes and build apps for any platform they wish.

- Testing Support:
Byteblog has testing support added to it so that changes can be verified before deploying to production, new tests can be added easily too.
