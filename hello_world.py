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
#print(value.problem) #nr of correct letters
#print(result.path())
