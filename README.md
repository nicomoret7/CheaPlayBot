# CheaPlay Bot
Discord bot that compares prices of a given game name in common buying webs.

It implements a demo to test the scrapper and a Python API for no bot usage in other apps, the discord bot is dockerizable and a Dockerfile is provided that automates the whole image creation and configuration.

As for now, the search parameters are:
- Plataform: Steam
- Currency: Euro €
- Region: Global or Europe

If requested, I might add options to change that parameters.

## Build
To build and test the Discord bot implementation on your own you have to create a `.env` file on the proyect directory with the following info:
```
DISCORD_TOKEN=<your_bot_token>
PREFIX=<command_prefix>
```

Now build the docker image with:
```
docker build -t <image_name> .
```

And create a container:
```
sudo docker run -it -d --restart unless-stopped --name <container_name> <image_name>
```

## Demo
A demo is provided for the scraper only. To try it, type the following on the proyect directory:
```
python3 demo.py
```

<p align="center">
  <img src="https://github.com/nicomoret7/CheaPlayBot/blob/master/assets/demo.png">  
</p>

## API
A Flask Restful basic API is also provided. You can test it by executing `python3 api.py` and sending a GET request to
"localhost:5000/price/<game_name>" in your browser or via curl:
```
curl localhost:5000/price/<game_name>
```
