# UltraBot-2k17

[![Build Status](https://travis-ci.org/Study-Projects/UltraBot-2k17.svg?branch=master)](https://travis-ci.org/Study-Projects/UltraBot-2k17)
[![Coverage Status](https://coveralls.io/repos/github/Study-Projects/UltraBot-2k17/badge.svg?branch=master)](https://coveralls.io/github/Study-Projects/UltraBot-2k17?branch=master)
[![Code Climate][code-climate-badge]][code-climate]
[![License: MIT][license-badge]][license]

[license-badge]: https://img.shields.io/badge/License-MIT-red.svg?branch=master
[license]: https://opensource.org/licenses/MIT
[code-climate-badge]: https://codeclimate.com/github/Study-Projects/UltraBot-2k17.png?branch=master
[code-climate]: https://codeclimate.com/github/Study-Projects/UltraBot-2k17

Little summer project from 2 Python learners. This is a chatbot for [vk.com](https://vk.com) with Russian interface. It could send you weather, news and memes. You can try it [here](https://vk.com/im?sel=-149540554).    

![bot-interface](https://user-images.githubusercontent.com/25745587/28548648-d01c2fac-70dd-11e7-93cb-4b046ad1f9e8.png)

### List of commands
```
Добавь (мемо/новости)группу <название группы> <ссылка>
Удали (мемо/новости)группу <название группы>
Удали все (мемо/новости)группы
Пришли свежие (мемы/новости)
Пришли (мемы/новости) из <название группы>
Пришли список (мемо/новости)групп
Погода <city(EN)>
```

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

For initial deploy and making some changes on heroku, you should commit it on your local machine and push that on heroku:
```
$ git push heroku master
```

Create database on heroku
```
$ heroku addons:add heroku-postgresql:hobby-dev
```

Create tables of your database
```
$ heroku run python db_create.py
```

## Running the tests
From root directory
```
$ python3 -m pytest tests
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

