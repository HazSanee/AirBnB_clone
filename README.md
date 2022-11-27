# AirBnB clone - The console
<p align="center"><img src="airbnb.gif" /></p>

## Overview
The AirBnB project is an extensive project that is mandatory for all ALX Software Engineering students. We are required to build a fullstack AirBnB webapp clone.

In this part, which is the first part, we worked on the backend of the project while interfacing it with a console application with the help of the inbuilt cmd module in python.

Data (python objects) which would later serve as models in the fully developed web app, are generated and stored in a json file which are accessed with the help of the inbuilt json module in python.

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google: <br>
    - How to create a Python package <br>
    - How to create a command interpreter in Python using the cmd module
    - What is Unit testing and how to implement it in a large project
    - How to serialize and deserialize a Class
    - How to write and read a JSON file
    - How to manage datetime
    - What is an UUID
    - What is *args and how to use it
    - What is **kwargs and how to use it
    - How to handle named arguments in a function

## Description of the command interpreter:
The interface of the application is just like the Bash shell except that this has a limited number of accepted commands that were solely defined for the purposes of the usage of the AirBnB website.

This command line interpreter  serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming.

Some of the commands available are:
- ```show```
- ```create```
- ```update```
- ```destroy```
- ```count```

And as part of the implementation of the command line interpreter coupled with the backend and file storage system, the folowing actions can be performed:
-   Creating new objects (ex: a new User or a new Place)
-   Retrieving an object from a file, a database etc…
-   Doing operations on objects (count, compute stats, etc…)
-   Updating attributes of an object
-   Destroying an object

## Execution
It can work in two different modes:

**Interactive** and **Non-interactive**.

In **Interactive mode**, the console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again a wait for a new command. This can go indefinitely as long as the user does not exit the program.

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

In **Non-interactive mode**, the shell will need to be run with a command input piped into its execution so that the command is run as soon as the Shell starts. In this mode no prompt will appear, and no further input will be expected from the user.

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Authors
* **Oluwapelumi Olalekan** - [pelumi-guy](https://github.com/pelumi-guy)
* **Hadiza Sani** - [HazSanee](https://github.com/HazSanee)