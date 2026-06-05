import random
class Sahil:
    def __init__(self):
        print('LLM created')
    
    def predict(self , prompt):
        response_list = [
            'Delhi is the capital of india',
            'IPL is a cricket league',
            'AI stnads for artifical intelligence'
        ]
        return {'response': random.choice(response_list)}
    

class NakliPromptTemplate:
    def __init__(self , template , input_variable):
        self.template = template
        self.input_variables = self.input_variables
    
    def format(self , input_dict):
        return self.template.format(**input_dict)

template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variable = ['length','topic']
)

template.format({'length': 'short' , 'topic': 'india'})


