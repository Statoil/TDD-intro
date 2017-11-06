# TDD-course using Python, and Jenkins.

The purpose is to learn some basic python (classes and functions), to learn how to write your code using a Test Driven Development approach, and to get a small hands on feeling of how to run these tests from a Continuous Integration platform (Jenkins).

## Requirements:
* Machine with Python installed (recommend using Miniconda, but we don't need to, beacause we need no libraries).
* A suitable editor for code (sublime, notepad(!), emacs, vim, VS Code) or a IDE suited for Python (PyCharm community edition is recommended)
* Machine with Git installed
* An internet connection.
* Ability to clone this repo via SSH or https (github.com/Statoil/TDD-intro)
* (optional) PyCharm community edition.

## Part 1 - capture some information about a car

We start with one file, containing one failing test.
From there, we will use test driven development to create some code that captures:

1. Car (with a model name, and functions crash() (that might kill the driver)).
2. Driver (with a name, a function "kill()", and a function "is_alive()").

To start -> check out the code from this repository (as you are here, you might already have done that).

You can sneak peak into the Step-X-suggestion folders to get some hints as to how to proceed.

**We are all here to learn, sharing is caring!**

### TDD Step 1, a car.

Now, we'll make a Car. In the Step-1 folder, you'll find a file (testcar.py).

Try to run the test either from your IDE, or from the command line by writing ```python -m unittests``` (or in Python 2.7 ```python -m unittests discover```).

The unit test runner will pick up files that start with test. If everything works, you'll get an error message stating ```NameError: name 'Driver' is not defined```

Now - TDD you'r way to a Car:
* You should first be able to just create a car (car = Car())
* Add a test where you try to set a model name attribute (eg. car.name). You can also create a constructor (```__init__```) that takes the model as an argument.
* A crash() function. The function should make sure a "has_crashed" attribute is set.

Remember, each step of the way, you first write your failing test, and then
in small increments write the functionality in question.

### TDD Step  2, expand the car with some driver info.
The car class now has a model name and a crash() function.

Add a couple of features to your Car, that keeps track of the driver:
* A driver name
* When the car's crash() function is called, the driver should either survive, or not. Expand the crash() to capture this (eg. car.is_driver_alive()).


### TDD Step - 3, refactor the driver properties to a driver class ++

This is when you should create your TestDriver class, in a separate file called ```testdriver.py```.
Start moving the driver related stuff (name, is_alive) to a new  ```driver.py``` file.

This is refactoring. Take small (by the book), or bigger steps.

Write tests for the new driver class, while changing/adding/updating the tests for the Car class.

If time permits you can for example:
* Make the tests for the crash() function check that if the car model is Volvo, the driver survives.
* Make the tests for the crash() function demand that if the driver is Superman, the driver should survive.
* Move the repetitive ```car = Car("Name of car")``` into a setUp() function (```def setUp(self):```)

You now have a number of tests, hopefully all running OK, and two classes (Car and Driver). Next step is to run this on
a "continuous integration" server (Jenkins).

## Part 2 - running the tests on Jenkins.
Go to the open Jenkins in your browser (let's use http://bg-dev.statoil.no:8080/).

Create your own job, a freestyle project, use your name or similar. Set it up to check out the relevant code (your repo, or this one). 

Create a shell script in the job that run the tests. 
See if you can set the job up to run when a change in the git repo is found.

The Jenkins server might get a bit clogged if many people run stuff at the same time, but hey, lets try.
