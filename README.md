# TDD-course using Python, and Jenkins.

The purpose is to learn some basic python (classes and functions), to learn how to write your code using a Test Driven Development approach, and to get a small hands on feeling of how to run these tests from a Continuous Integration platform (Jenkins).

## Requirements:
* Machine with Python installed (recommend using Miniconda, but we don't need to, beacause we need no libraries).
* A suitable editor for code (sublime, notepad(!), emacs, vim, VS Code) or a IDE suited for Python (PyCharm community edition is recommended)
* Machine with Git installed
* An internet connection.
* Ability to clone this repo via SSH or https (github.com/flikka/TDD-course)
* (optional) PyCharm community edition.

## Part 1, a very simplistic and naive "start from scratch" example.
Check out the code from this repository (as you are here, you might already have done that).

### Step-1, a driver.
Go into the Step-1 folder, we're making a driver. If you manage to keep up, you never need to leave this folder.


Open the file DriverTest.py in your favourite browser. Try to run the test either from your IDE, or from the command line by writing ```python -m unittests DriverTest.py``` and follow the instructions. At this point you'll start with a non-working test. 

When you are finished with this, you should have a Driver class in a separate file, some methods and tests that checks that the functionality is as expected.

### Step-2, a car.
Either continue from the previous step, or go into the Step-2 folder.

Now, we'll make a car with some bells and whistles. Create a test file first, and TDD you'r way to a Car with a model name, a registration number, and mileage. The model name and registration number are simple properties to be set and read, but the mileage is a bit different. It should be possible to get the mileage, but not to set it directly. It should be zero when the Car (object) is new, and it should increase by one kilometer by the call of a function (eg. "add_km()")

Remember, each step of the way, you first write your failing test, and then in small increments write the functionality in question.

### Step-3, a driver in a car.
Now you should have a Driver.py, DriverTest.py, Car.py and CarTest.py file. If not, you might consider entering the folder "Step-3".

Now put the driver into the car (a Car can have a driver). Add some goodnes to the car. Perhaps it should have the ability to drive (a drive function, and perhaps a boolean is_driving variable?), and maybe to crash (car.crash(), can only crash if actually driving?), with a non-deterministic fatal accident for the driver? Perhaps some damage (percentage? price to fix?) will incur on the car? 

Which new properties and methods does the car need, take it step by step. Add functionality to the Car and Driver as needed.

TDD your way through this. Ask for help! Either from the instructor or from other participants. 

**We are all here to learn, sharing is caring!**

## Part 2 - running the tests on Jenkins.
Go to the open Jenkins in your browser (let's use http://bg-dev.statoil.no:8080/).

Create your own job, a freestyle project, use your name or similar. Set it up to check out the relevant code (your repo, or this one). 

Create a shell script in the job that run the tests. 
See if you can set the job up to run when a change in the git repo is found.

The Jenkins server might get a bit clogged if many people run stuff at the same time, but hey, lets try.
