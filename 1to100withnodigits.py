'''Program that print numbers from 1 to 100,
but the code have no digits.
Made for a challenge.'''
from math import pi, e;
counter = False; #initializes a counter with 0 (False)
goal = e*pi**pi; #this is almost 100 and will serve as stop point
while (counter<goal):
  counter += True; #increases the counter by 1 (True)
  print(counter);

