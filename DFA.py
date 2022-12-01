'''
Assignment No. 1
Take 2 DFA's, implement it's code (OOP Form).

Chapter # 2,Q #: 1-6,9,10,11,12 <Handwritten>
Chapter # 4,Q #: 1-6 <Handwritten>

'''
class DFA:
    def __init__(self, language_tuple, state_list, start_state, final_state_list, transitions_dict):
        self.language = language_tuple
        self.states = state_list
        self.start_state = start_state
        self.final_states = final_state_list
        self.transitions = transitions_dict

    def transition(self, character, state):
        return self.transitions[state][character]

    def is_valid(self, input_string):   
        current_state = self.start_state
        for c in input_string:
            if c not in self.language:
                raise ValueError("Character doesn't exist in language")
            current_state = self.transition(c, current_state) 
        return current_state in self.final_states


# language = ('a', 'b')
# states, start_state, final_states = ['q0','q1'], 'q0', ['q1']
# transitions_dict = {'q0':{'a':'q1', 'b':'q1'}, 'q1':{'a':'q0', 'b':'q0'}}


if __name__ == '__main__':
    language = ('a', 'b')
    states, start_state, final_states = ['q0','q1', 'q2'], 'q0', ['q2']
    transitions_dict = {
        'q0':{'a':'q2', 'b':'q1'},
        'q1':{'a':'q1', 'b':'q2'},
        'q2':{'a':'q2', 'b':'q0'}
    }

    # Accepted string examples:
    # a, aa, aaa, aaa
    # bb, bbbbb, bbbbbbbb
    # bab, baba

    dfa = DFA(language, states, start_state, final_states, transitions_dict)
    input_string = input(f"Enter a string in the language{language}: ")
    print ("Accepted" if dfa.is_valid(input_string) else "Rejected")
