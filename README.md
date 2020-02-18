<h1 align="center">
  <a href="https://github.com/snakypy/snakypy">
    <img alt="snakypy" src="https://raw.githubusercontent.com/snakypy/snakypy-static/master/logotypes/snakypy/png/snakypy.png" width="500">
  </a>
  <br> Snakypy - Facilitating its development. <br>
</h1>

<div align="center">
  <h4>
    | <a href="https://snakypy.github.io">Website</a> |
    <a href="#features">Features</a> |
    <a href="#requirements">Requirements</a> |
    <a href="#installing">Install</a> |
    <a href="#upgrading">Upgrade</a> |
    <a href="#donation">Donation</a> |
  </h4>
  <h5>
    | <a href="#more-commands">More Commands</a> |
  </h5>
</div>

<div align="center">
  <sub>Built with ❤︎ by
  <a href="https://williamcanin.github.io">William Canin</a> in free time.
</div>
<br>

`Snakypy` is a package containing "wheels" which will help the user to get around in development.

## Features

<details>
    <summary>Know some features</summary>

**pick**: A function of the "pick" module. This function creates a selectable menu in a practical and automatic way.

*options*:

- index: Default "index=False". If the position is equal to True, a tuple returns with the index of the element referring to the list.

- answer: Default answer='Answer:'. Response text.

- colorful: Default colorful=False. The name says it, it makes everything colorful.
            NOTE: If you use Windows, you should leave this option colorful=False.

Example:
```shell
>>> from snakypy import pick
>>> title = 'What is your favorite programming language?'
>>> options = ['C', 'C++', 'Java', 'Javascript', 'Python', 'Ruby']
>>> pick(title, options)
```

Output:
```
➜ What is your favorite programming language? (Ctrl+C to Cancel)
[1] C
[2] C++
[3] Java
[4] Javascript
[5] Python
[6] Ruby
➜ Answer: 5
'python'
```
</details>

## Requirements

To work correctly, you will first need:

- [`Python`](https://python.org) (v3.8 or recent).
- [`Pip`](https://pip.pypa.io/en/stable/) (v19.3 or recent) must be installed.

## Installing

It's time to install `Snakypy`. To do this, do:

Globally:

```
$ su -c "pip install snakypy"
```
For the user:

```
$ pip install snakypy --user
```

> NOTE: If you are installing to the user's local environment, be sure to add the environment variables to the `zshrc` file.

## Upgrading

If `Snakypy` has any new features, please update the command line below:

Globally:

```
$ su -c "pip install snakypy -U"
```
For the user:

```
$ pip install snakypy -U --user
```

## Donation

If you liked my work, buy me a coffee :coffee: :smiley:

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YBK2HEEYG8V5W&source)

## License

The project is available as open source under the terms of the [MIT License](https://github.com/snakypy/snakypy/blob/master/LICENSE) © William Canin

## Credits/Author

* Name: William C. Canin
* Country: Brazil - SP
* E-Mail: william.costa.canin@gmail.com
* GitHub: [William Canin](http://github.com/williamcanin)
* Personal page: [William Canin](http://williamcanin.github.io)
