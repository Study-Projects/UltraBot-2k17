# UltraBot-2k17
Little summer project from 2 python learners.
This is a little chatbot for vk.com with russian interface.
It could send you weather, news and memes.    
All funcionality you could see in menu [here](https://vk.com/im?sel=-149540554) typing "Меню" or "Помощь".    
To get some memes or news you must add group into our's bot memory, using commands from menu.     
If you need weather, please, type your town on eng. 
## Getting Started

For download code on your local machine use:
```
$ git clone https://github.com/Study-Projects/UltraBot-2k17
```

After you cloned repository on your local machine, you should login in heroku client - [how to install](https://devcenter.heroku.com/articles/heroku-cli). 
```
$ heroku login
```

Connect with your application
```
$ heroku git:remote -a name-of-your-app
```

Also you can create new app
```
$ heroku create name-of-your-app
```

Create database on heroku
```
$ heroku addons:add heroku-postgresql:hobby-dev
```

For initial deploy and making some changes on heroku, you should commit it on your local machine and push that on heroku:

```
$ git push heroku master
```
Create tables of your database
```
$ heroku run python db_create.py
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

