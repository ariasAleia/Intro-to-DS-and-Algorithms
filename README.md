# Intro to Data Structures and Algorithms

So! Yes! Here we are again. We have already learned a little bit about the basics and a little bit more about OOP in Python. But now comes the interesting part... chan chan chaaaaaaaaaaaaannnn and the reason why we are still triggered with the concept of programming: Data Structures and Algorithms.

Once upon a time there was a girl who knew how to play a little bit with code. 4th semester, I guess. Not great expectations in this new subject but suddenly everything changed for her. The magic of creating with simple concepts. Nodes, graphs, connections. Simple functions that created a whole universe of solutions to solve a single problem. The power of simplicity. The power of understanding. The power of programming. A sheet of paper, a pencil and her mind dancing around with ideas that jumped in her head til the eureka moment comes! Yes. Definitely one of the greatest feelings ever. 

This is the beginning of a new journey that tries to return to that state of flow where everything seemed to be challenging but at the same time so exciting that it felt like a constant game and dance. However, as Heraclitus once said: “No man ever steps in the same river twice, for it's not the same river and he's not the same man.”, this is a new beginning to reinvent ourselves. Discover new patterns and experience new sensations. Sensations? Really? Yep... It may sound kinda strange but every time that I learn sth related with creating, specially when it comes to solve problems with creativity, pencil, sheet of paper and my mind, I feel such a river of sensations that I can't stop. 

This is the chapter where we begin to learn again about the way we can create solutions and understand problems. This is the chapter where we begin to learn again about data structures and algorithms.

<p style="text-align:right"><b> "The desire to create is one of the deepest yearnings of the human soul</b>"<br>Elder Uchtdorf</p>


## How are we going to learn?

Contrary to the previous two steps of this journey, (check them out here in case you missed them -> [Step 1: Basics](https://github.com/ariasAleia/Learning_Python) and [Step 2: OOP](https://github.com/ariasAleia/OOP_Python)) we are now going to learn about data structures and algorithms in Python following along a course grown by Google in Udacity: [Intro to DS and Algorithms](https://www.udacity.com/course/data-structures-and-algorithms-in-python--ud513)

First of all, we needed to check if our knowledge of Python is enough to understand the concepts of data structures and algorithms. We did it by implementing a couple of methods of a class. The source code can be found in the file of the class [classy.py](scripts/classy.py)

Proof of that we did it correctly:
<p align="center">
<img src= "images/done_exercise0.png" alt="Euler" title="Euler" width="550px" height="250px">
</p>

And then we had to do another small example to know if we were familiar with the way Python handles strings and we did it again :) The solution and the problem statement can be found in [this file](scripts/exercise0.py).

<p align="center">
<img src= "images/done_exercise1.png" alt="Euler" title="Euler" width="550px" height="250px">
</p>


## Efficiency and Complexity

Like everything in life, it is all a matter of balance. We must think about algorithms in terms of time and space. How much time does it take us to run the algorithm and get a result? And... How much space do we need? How much memory do we need to process the information til we get a result?

A tradeoff: a balancing of two qualities both of which are desired but that may not have a totally compatible existence.

## Big O notation

Yes... we love coding and most of the time we do it alone with our pencil and sheet of paper, however, we are social beings and the need to communicate the way we are doing things. In this case, we want to be able to communicate how good or bad the behavior of an algorithm is: its complexity. It's also important for us to know how good an algorithm developed by sb else is. That means, we all need a common language and that language in this case is the Big O Notation. 

We will basically describe the complexity of an algorithm depending on the amount of data that we get as input. That amount of data is n.

So we have...
* $O(n)$
* $O(n^2)$
* $O(log (n))$

We don't necessarily have to check every single calculation that is performed, we can approximate. That means that $O(2n +1)$ would be the same as $O(n)$.

### Let's practice with an example

```python
"""input manatees: a list of "manatees", where one manatee is represented by a dictionary
a single manatee has properties like "name", "age", et cetera
n = the number of elements in "manatees"
m = the number of properties per "manatee" (i.e. the number of keys in a manatee dictionary)"""

def example1(manatees):
    for manatee in manatees:
        print manatee['name']

def example2(manatees):
    print manatees[0]['name']
    print manatees[0]['age']

def example3(manatees):
    for manatee in manatees:
        for manatee_property in manatee:
            print manatee_property, ": ", manatee[manatee_property]

def example4(manatees):
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        for manatee2 in manatees:
            if manatee1['age'] < manatee2['age']:
                oldest_manatee = manatee2['name']
            else:
                oldest_manatee = manatee1['name']
    print oldest_manatee
```

Our answers:

![](images/ans_O_notation.png)  

The hipermega great result :):

![](images/exercise_O_notation.png)  