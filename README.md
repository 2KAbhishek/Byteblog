<div align = "center">

<h1><a href="https://2kabhishek.github.io/Byteblog">BareMinimum</a></h1>

<a href="https://github.com/2KAbhishek/Byteblog/blob/main/LICENSE">
<img alt="License" src="https://img.shields.io/github/license/2kabhishek/Byteblog?style=flat&color=eee&label="> </a>

<a href="https://github.com/2KAbhishek/Byteblog/graphs/contributors">
<img alt="People" src="https://img.shields.io/github/contributors/2kabhishek/Byteblog?style=flat&color=ffaaf2&label=People"> </a>

<a href="https://github.com/2KAbhishek/Byteblog/stargazers">
<img alt="Stars" src="https://img.shields.io/github/stars/2kabhishek/Byteblog?style=flat&color=98c379&label=Stars"></a>

<a href="https://github.com/2KAbhishek/Byteblog/network/members">
<img alt="Forks" src="https://img.shields.io/github/forks/2kabhishek/Byteblog?style=flat&color=66a8e0&label=Forks"> </a>

<a href="https://github.com/2KAbhishek/Byteblog/watchers">
<img alt="Watches" src="https://img.shields.io/github/watchers/2kabhishek/Byteblog?style=flat&color=f5d08b&label=Watches"> </a>

<a href="https://github.com/2KAbhishek/Byteblog/pulse">
<img alt="Last Updated" src="https://img.shields.io/github/last-commit/2kabhishek/Byteblog?style=flat&color=e06c75&label="> </a>

</div>

<a href="https://www.producthunt.com/posts/byteblog?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-byteblog" target="_blank">
  <img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=281145&theme=dark"
       alt="Byteblog - Open Source blogging platform, share your thoughts in bytes. | Product Hunt"
       style="width: 250px; height: 54px;" width="250" height="54" /></a>

Byteblog is a minimalist micro-blogging platform built with Pyhton Flask for anyone seeking a quieter "Social Media".

[Visit](https://byteblog.herokuapp.com)

A user can easily register for Byteblog with their email id and password and then can easily share their bytes (similar to tweets in twitter) and also follow other people to read their thoughts, users can also message other users who follow them.

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
