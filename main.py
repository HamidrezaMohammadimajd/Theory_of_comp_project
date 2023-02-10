class Dfa : 
    def __init__(self,states,alphabets,start_state,accept_state,transition):
        self.states = states
        self.alphabets = alphabets
        self.start_state = start_state
        self.accept_states = accept_state
        self.transition = transition
        self.accepted_strings = []

    def set_states(self,l):   
        self.states = l

    def set_alphabets(self,l):   
        self.alphabets = l

    def set_start_state(self,l): 
        self.start_state = l

    def set_accept_states(self,l):
        self.accept_states = l

    def set_transition(self,l):
        self.transition = l

    def accept_string(self, input_string):
        current_state = self.start_state
        for i in input_string:
            current_state = self.transition[current_state][i]
        if current_state in self.accept_states:
            return True
        else:
            return False   

    def generate(self, string_len):
        if string_len == 0:
            return ['']
        else:
            ans = []
            for string in self.generate(string_len - 1):
                for symbol in self.alphabets:
                    ans.append(string + symbol)
            return ans

    def get_lang(self,n):
        self.accepted_strings = [string for string in self.generate(n) if self.accept_string(string)]


    def isempty(self):
        all_strings = self.generate(len(self.states))  
        if all_strings:
            return False
        return True    

    def isfinite(self):
        for string in self.generate(2*len(self.states)) :
            if len(string)>=len(self.states):
                if self.accept_string(string) :
                    return False
        return True            

    def get_num(self):
        if self.isfinite():
            return len(self.accepted_string)


    def min_len_string(self):
        if not self.isempty():
            min = self.accepted_strings[0]
            for i in self.accepted_strings:
                if len(i)<min:
                    min = i
            return len(min)         

    def max_len_string(self):
        if self.isfinite():
            max = self.accepted_strings[0]
            for i in self.accepted_strings:
                if len(i)>max:
                    max = i
            return len(max)  

    def complement(self):
        temp = []
        for i in self.states:
            if i not in self.accept_states:
                temp.append(i)
        new_dfa = Dfa(self.states,self.alphabets,self.start_state,temp,self.transition)
        return new_dfa  

    def union(self,dfa2):
        new_start_state = (self.start_state,dfa2.start_state) 
        new_alphabets = self.alphabets
        new_states = []
        new_accept_states = []
        new_transition = {}
        for i in self.states:
            for j in dfa2.states:
                new_states.append((i,j))   
        for state in new_states:
            new_transition[state] = {}
            for symbol in new_alphabets:
                new_transition[state][symbol] = (self.transition[state[0]][symbol], dfa2.transition[state[1]][symbol])
        for state in new_states:
            if state[0] in self.accept_states  or  state[1] in dfa2.accept_states :
                new_accept_states.append(state)      
        return Dfa(new_states,new_alphabets,new_start_state,new_accept_states,new_transition)

    def UNION(self,dfa1,dfa2):
        new_start_state = (dfa1.start_state,dfa2.start_state) 
        new_alphabets = dfa1.alphabets
        new_states = []
        new_accept_states = []
        new_transition = {}
        for i in dfa1.states:
            for j in dfa2.states:
                new_states.append((i,j))   
        for state in new_states:
            new_transition[state] = {}
            for symbol in new_alphabets:
                new_transition[state][symbol] = (dfa1.transition[state[0]][symbol], dfa2.transition[state[1]][symbol])
        for state in new_states:
            if state[0] in dfa1.accept_states  or  state[1] in dfa2.accept_states :
                new_accept_states.append(state)      
        return Dfa(new_states,new_alphabets,new_start_state,new_accept_states,new_transition)

    def intersection(self,dfa2):
        new_start_state = (self.start_state,dfa2.start_state) 
        new_alphabets = self.alphabets
        new_states = []
        new_accept_states = []
        new_transition = {}
        for i in self.states:
            for j in dfa2.states:
                new_states.append((i,j))   
        for state in new_states:
            new_transition[state] = {}
            for symbol in new_alphabets:
                new_transition[state][symbol] = (self.transition[state[0]][symbol], dfa2.transition[state[1]][symbol])
        for state in new_states:
            if state[0] in self.accept_states  and  state[1] in dfa2.accept_states :
                new_accept_states.append(state)      
        return Dfa(new_states,new_alphabets,new_start_state,new_accept_states,new_transition)        

    def INTERSECTION(self,dfa1,dfa2):
        new_start_state = (dfa1.start_state,dfa2.start_state) 
        new_alphabets = dfa1.alphabets
        new_states = []
        new_accept_states = []
        new_transition = {}
        for i in dfa1.states:
            for j in dfa2.states:
                new_states.append((i,j))   
        for state in new_states:
            new_transition[state] = {}
            for symbol in new_alphabets:
                new_transition[state][symbol] = (dfa1.transition[state[0]][symbol], dfa2.transition[state[1]][symbol])
        for state in new_states:
            if state[0] in dfa1.accept_states  and  state[1] in dfa2.accept_states :
                new_accept_states.append(state)      
        return Dfa(new_states,new_alphabets,new_start_state,new_accept_states,new_transition)        

    def difference(self,dfa2):
        new_start_state = (self.start_state,dfa2.start_state) 
        new_alphabets = self.alphabets
        new_states = []
        new_accept_states = []
        new_transition = {}
        for i in self.states:
            for j in dfa2.states:
                new_states.append((i,j))   
        for state in new_states:
            new_transition[state] = {}
            for symbol in new_alphabets:
                new_transition[state][symbol] = (self.transition[state[0]][symbol], dfa2.transition[state[1]][symbol])
        for state in new_states:
            if state[0] in self.accept_states  and  state[1] not in dfa2.accept_states :
                new_accept_states.append(state)      
        return Dfa(new_states,new_alphabets,new_start_state,new_accept_states,new_transition)

    def DIFFERENCE(self,dfa1,dfa2):
        new_start_state = (dfa1.start_state,dfa2.start_state) 
        new_alphabets = dfa1.alphabets
        new_states = []
        new_accept_states = []
        new_transition = {}
        for i in dfa1.states:
            for j in dfa2.states:
                new_states.append((i,j))   
        for state in new_states:
            new_transition[state] = {}
            for symbol in new_alphabets:
                new_transition[state][symbol] = (dfa1.transition[state[0]][symbol], dfa2.transition[state[1]][symbol])
        for state in new_states:
            if state[0] in dfa1.accept_states  and  state[1] not in dfa2.accept_states :
                new_accept_states.append(state)      
        return Dfa(new_states,new_alphabets,new_start_state,new_accept_states,new_transition)

    def issubset(self,dfa2):
        if self.difference(dfa2) :
            return True
        return False      

    def isdisjoint(self,dfa2):
        if self.intersection(dfa2) :
            return False
        return True   

    def ISSUBSET(self,dfa1,dfa2):
        if self.difference(dfa1,dfa2) :
            return True
        return False      

    def ISDISJOINT(self,dfa1,dfa2):
        if self.intersection(dfa1,dfa2) :
            return False
        return True   

class Nfa:
    def __init__(self,states,alphabets,start_state,accept_state,transition):
        self.states = states
        self.alphabets = alphabets
        self.start_state = start_state
        self.accept_states = accept_state
        self.transition = transition     

    def set_states(self,l):   
        self.states = l

    def set_alphabets(self,l):   
        self.alphabets = l

    def set_start_state(self,l): 
        self.start_state = l

    def set_accept_states(self,l):
        self.accept_states = l

    def set_transition(self,l):
        self.transition = l

Language= Dfa(
    ['q0', 'q1', 'q2', 'q3'],
     ['a', 'b'],
      'q0',
       ['q3'],
    {
        'q0': {
            'a': 'q1',
            'b': 'q0'
        },
        'q1': {
            'a': 'q2',
            'b': 'q0'
        },
        'q2': {
            'a': 'q3',
            'b': 'q0'
        },
        'q3': {
            'a': 'q3',
            'b': 'q0'
        }
    }
    )  
print(Language.states)
print(Language.alphabets)
print(Language.start_state)
print(Language.accept_states)
print(Language.transition)
Language.get_lang(8)    
print(Language.accepted_strings)    


                    




