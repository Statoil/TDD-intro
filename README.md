# TDD-course using Python, and Jenkins.

The purpose is to learn some basic python (classes and functions), to learn how to write your code using a Test Driven Development approach, and to get a small hands on feeling of how to run these tests from a Continuous Integration platform (Jenkins).

## Requirements:
* Machine with Python installed (recommend using Miniconda, but we don't need to, beacause we need no libraries).
* A suitable editor for code (sublime, notepad(!), emacs, vim, VS Code) or a IDE suited for Python (PyCharm community edition is recommended)
* Machine with Git installed
* An internet connection.
* Ability to clone this repo via SSH or https (github.com/flikka/TDD-course)
* (optional) PyCharm community edition.

## Part 1, create a class representing a driver and a class representing a car

We start with one file, containing one failing test. From there, we will use test driven development to create these two classes:
1. Driver (with a name, a function "kill()", and a function "is_alive()").
2. Car (with a model name, and functions crash() (that might kill the driver)).

To start -> check out the code from this repository (as you are here, you might already have done that).

You can sneak peak into the Step-2 and Final folder if you're a bit stuck.

### TDD Step-1, a driver.
Go into the Step-1 folder. There, you'll find a file ```testdriver.py```. This is the start-point for creating a driver class, using TDD. The driver is supposed to represent some features that a driver of a car has. If you manage to keep up, you never need to leave this folder.

Open the file in your favourite file editor (or IDE). Try to run the test either from your IDE, or from the command line by writing ```python -m unittests```. The unit test runner will pick up files that start with test. If everything works, you'll get an error message stating ```NameError: name 'Driver' is not defined```

This is when you should create your Driver class, in a separate file called ```driver.py```.

When you have your Driver class, the first test should pass.

The next step is to add a couple of "features", by first adding a test for the feature, and then implementing it. It is not really important exactly what you do, but for example a way to set the name in a constructor (using ```__init__```), and a way to set / get the name as an attribute might be a sensible first step.

Then, add a test for the function "is_alive()" and the function "kill()".

### TDD Step-2, a car.
Either continue from the previous step, or go into the Step-2 folder.

Now, we'll make a Car. Create a test file first (testcar.py), and TDD you'r way to a Car with a model name and a crash() function. The model name is a simple attribute, but the "crash()" function might have some other implications (hint: what might happen to the driver? Does the same thing always happen?).

Remember, each step of the way, you first write your failing test, and then in small increments write the functionality in question.

**We are all here to learn, sharing is caring!**

## Part 2 - running the tests on Jenkins.
Go to the open Jenkins in your browser (let's use http://bg-dev.statoil.no:8080/).

Create your own job, a freestyle project, use your name or similar. Set it up to check out the relevant code (your repo, or this one). 

Create a shell script in the job that run the tests. 
See if you can set the job up to run when a change in the git repo is found.

The Jenkins server might get a bit clogged if many people run stuff at the same time, but hey, lets try.
