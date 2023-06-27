# Spotify Map

## About project

This project detects the top track of the artist and shows on the map where that track is available. This is really tricky and easy way to get top tracks. (Done for the course Basics of Programming at Ukrainian Catholic University)

## Result example

You can try web site here [hellcaster.pythonanywhere.com](https://hellcaster.pythonanywhere.com/)

![Example](./example.png)

## Installation and start

To start the project do the following commands:

### Install requirements

1. Clone the repository and open the folder in the terminal.
2. Create a virtual environment and install requirements:

```cmd
python3 -m venv venv

source venv/bin/activate # if you are using MacOS
venv/bin/activate # for Windows

pip3 install requirements.txt
```

### Start project

```cmd
python3 main.py
```

You will see at which port the application will start in the terminal.

**IMPORTANT:** You will also need a Spotify Secret code and key. Get it in [developer.spotify.com](https://developer.spotify.com).

### Determinate

```cmd
deactivate
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
