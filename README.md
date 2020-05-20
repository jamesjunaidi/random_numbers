This is a simple python script that will generate random numbers. We take inputs for the min number, max number, and amount of numbers we want. The reason why I wrote this program is because for a unit test that I had to make for a C++ program I needed some random numbers to store in a vector, which should be inputted as numbers separated by commas. I could not find a random number generator online that separated the numbers by commas, so I decided to write my own program and just put it on
github for my potential future use or someone else to use if they need random numbers with commas.

The program prints statements telling you what to input, but I reccomend putting the output in a text file to store the numbers and not just have them printed.

For example, on a unix system you would run it like:

python random_generator.py > numbers.txt

1

10

100

There will be no statements on what you need to enter, so you have to input the min number, press enter, input the max number, press enter, and input the amount of numbers, and hit enter. This will then put the numbers into the file "numbers.txt" in the same directory.
