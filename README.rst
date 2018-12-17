
Local Search - Metaheuristic
============================

Project GIT address: https://github.com/anduralex/LSpackage.git

This lib implements some algorithms described on the book "Metaheuristics - From Design to Implementation", from El-Ghazali Talbi.

I am testing the lib and it is available via pip install.

At this moment, the implementation includes:

* Search
    * Local Search algorithms - Hill Climbing

Creating your problem
---------------------
The problem class will need to implement several methods, some of them depending on the algorithms.

You will always have to implement:
* **actions**: this method receives a state, and must return the list of actions that can be performed from that particular state.
* **result**: this method receives a state and an action, and must return the resulting state of applying that particular action from that particular state.
* **value**: This method receives a state, and returns a valuation ("score") of that value. Better states must have higher scores.

Installation
============

Just get it:

.. code-block:: none

    pip install LSpackage

You will need to have pip installed on your system. On linux install the 
python-pip package.

Usage
=====
If you want to run the example hello_world.py follow next steps:
* Download the project from github address: https://github.com/anduralex/LSpackage.git 
* Open Terminal and go to the LSpackage-master folder 
* Type into the terminal:
.. code-block:: none 
	python hello_world.py

Examples
========

LSpackage allows you to define problems and look for the solution with
different strategies. A sample are in the ``hello_word.py``.

The problem will try to create the string "HELLO WORLD" using localSearchAlg algorithm:

.. code-block:: python

 from code.models import SearchProblem
 from code.local import hillClimbing,localSearchAlg,firstExpander

 WORD = 'HELLO WORLD'

  class HelloProblem(SearchProblem):
    def actions(self, state):
        if len(state) < len(WORD):
            return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        else:
            return []

    def result(self, state, action):
        return state+action

    def value(self, state):
        # how many correct letters there are?
        count=sum(1 if state[i] == WORD[i] else 0
                   for i in range(min(len(WORD), len(state))))
        return count

 result = localSearchAlg(HelloProblem(initial_state=''),firstExpander)
 print(result.state)

More detailed documentation
===========================

You can read the book "Metaheuristics - From Design to Implementation", from El-Ghazali Talbi. Or for offline access, you can clone the project code repository and work with it.
    
Authors
=======

* Andurnache Alexandru
