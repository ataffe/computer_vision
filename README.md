# Intro to Computer_Vision 
This is a collection of computer vision programs written in python using opencv. These programs come from the quizes in the udacity class at: https://classroom.udacity.com/courses/ud810. I used python 3, opencv 3, and matpotlib below are instructions for installing them. These programs should still work with python 2 but I have not tested this.

Note to self:
Work flow
1. git add [new file]
2. git commit -m "[commit message]"
3. git push origin [master] (or instead  of master name of branch)
4. git pull (Will fetch and merge remote changes)

note: This is for edits as well.

TODO
1. Filters quiz (Add equations)


# Installing python 3 on Windows

Go to: https://www.python.org/downloads/ and download it.

# Installing pip with python 3
This is a python package manager I believe, and I used it to install opencv 3 for python 3, numpy, and matplotlib. Open a command window by going to the windows search and typing "cmd" then clicking on command prompt.

Run the command: 

```curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py```

Then if you only have python 3 installed run(I have not tested this):

```python get-pip.py```

otherwise if you have python 2 and 3 installed run:

```py -3 get-pip.py```

Note: I got these instruction from the [pip website](https://pip.pypa.io/en/stable/installing)

# Installing opencv with python 3

Run the command:
```python -m pip install opencv-python```

Note: For me this installed numpy too, but if it doesn't I would just replace "opencv-python" with "numpy" 
If you have both python 2 and 3, just substitiue "python" with "py -3" if you have python 1...just get python 2 or 3 i guess ¯\_(ツ)_/¯.


# Installing matplotlib
Run the command...you guessed it:
``` python -m pip install matplotlib```
Note: The same thing goes for versions 2 and 3.
