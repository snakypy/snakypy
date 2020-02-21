# Usage

It all starts with an import...

    import snakpy

... however, you can find new ways to explore snakypy's functionality. See below the main news features.

> NOTE: If you use Windows, Ansi color settings will not work for your machine.

## Main feature of the package.

### [snakypy.printer](/snakypy.html#snakypy.console.printer)

Example:

    from snakypy import printer, FG, BG, SGR
    printer('Hello, World!', foreground=FG.BLACK, background=BG.WHITE, sgr=SGR.UNDERLINE)
    printer('Hello, World!', foreground=FG.MAGENTA, sgr=SGR.UNDERLINE)

For more customization details supported, see: [Ansi Color](/snakypy.html#module-snakypy.ansi)

### [snakypy.entry](/snakypy.html#snakypy.console.entry)

Example:

    from snakypy import entry, FG
    entry("What's your name?", foreground=FG.QUESTION)
    entry("What's your name?", foreground=FG.BLUE)
    entry("What's your name?", foreground=FG.GREEN)

For more customization details supported, see: [Ansi Color](/snakypy.html#module-snakypy.ansi)

### [snakypy.pick](/snakypy.html#snakypy.console.pick)

Example:

    from snakypy import pick
    title = 'What is your favorite programming language?'
    options = ['C', 'C++', 'Java', 'Javascript', 'Python', 'Ruby']
    pick(title, options)

**output**

    What is your favorite programming language? (Ctrl+C to Cancel)
    [1] C
    [2] C++
    [3] Java
    [4] Javascript
    [5] Python
    [6] Ruby
    Answer: 5
    'python'
    >>>

Taking the index from the menu list and receiving a tuple:

    snakypy.pick(title, options, index=True)

**output**

    What is your favorite programming language? (Ctrl+C to Cancel)
    [1] C
    [2] C++
    [3] Java
    [4] Javascript
    [5] Python
    [6] Ruby
    Answer: 5
    (4, 'python')
    >>>

To find out more about this feature, see [here](/snakypy.html#snakypy.console.pick).

### [snakypy.console.loading](/snakypy.html#snakypy.console.loading)

Example:

    from snakypy.console import loading
    loading()

**output**

    >>> loading()
    [Loading]
    100%
    >>> 

Using bar instead of percentage and setting the time (Default: set_time=0.030):

    loading(set_time=0.20, bar=True)

**output**

    >>> loading(bar=True)
    [Loading]
    [#########################]
    >>>

For more customization details supported, see: [Ansi Color](/snakypy.html#snakypy.console.loading)

### [snakypy.console.credence](/snakypy.html#snakypy.console.credence)

Example:

    from snakypy.console import credence

    data = {
        "credence": [
            {
                "my_name": "William Canin",
                "email": "example@domain.com",
                "website": "http://williamcanin.me",
                "locale": "Brazil - SP"
            },
            {
                "my_name": "Maria Canin",
                "email": "example@domain.com",
                "locale": "Brazil - SP"
            }
        ]
    }

    credence('Snakypy', '0.1.0', 'https://github.com/snakypy/snakypy', data)

**output**

         ---------------------------------------------------------         
                       Snakypy - Version 0.1.0                        
         ---------------------------------------------------------
        
                              Credence:
                              
                        My Name: William Canin                        
                      Email: example@domain.com                       
                   Website: http://williamcanin.me                    
                         Locale: Brazil - SP                          

                         My Name: Maria Canin                         
                      Email: example@domain.com                       
                         Locale: Brazil - SP                         

         ---------------------------------------------------------         
                 Snakypy © 2020 - All Right Reserved.                 
               Home: https://github.com/snakypy/snakypy               
         --------------------------------------------------------- 

For more customization details supported, see: [Ansi Color](/snakypy.html#snakypy.console.credence)
