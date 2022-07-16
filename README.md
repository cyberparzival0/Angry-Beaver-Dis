# Angry Beaver Disassembly
- For those cyber noobs that aren't down with the NSA, OR just don't care about learning disassembly of programs.
- This is a basic function parser that can be used with Python and C.
- Currently, it does not support classes. This is in the works.

## Why
- For your needs if you want to load dlls, easier integration with C Types.
- Want to compete in Google's AI4Code – Understand Code in Python Notebooks on Kaggle (Watch Out Google, but Really)!!!

## Story Behind The Name
- It's named after the cartoon I used to watch as a kid. 

## Main Program - angrybeaverdis.py
* `from angrybeaverdis import Patterns` - Importing angrybeaverdis
* `obj = Patterns(fileNameWithLocation, Language)` - Initialize the Patterns class with your filename/location and the language. By default, the lang parameter equals Python. Currently only supports Python and C
* `print(obj.extractSignatures())` - Print a dictionary with all the metadata associated with that function
