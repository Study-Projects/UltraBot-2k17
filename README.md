# UltraBot-2k17
Some little project on summer from two shit-progers

## Getting Started

For download code on your local machine use:
```
$ git clone https://github.com/REU-Projects/dormitory_site
```

After you cloned repository on your local machine, you should login in heroku client [how to install](https://devcenter.heroku.com/articles/heroku-cli). 
```
$ heroku login
```

Connect with your application
```
$ heroku git:remote -a name-of-your-app
```

Create database
```
$ heroku addons:add heroku-postgresql:hobby-dev
```

For making some changes on heroku, you should commit it on your local machine and push that on heroku:
```
$ git push heroku master
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

