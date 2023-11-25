from .model import Model

class MindMap:
    class Node:
        def __init__(self, name):
            self.name = name
            self.children = {}
            
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.model = Model()
        self.map = self.create_map(name, text)

    def create_map(self, name, text):
        '''
        Recursively put a "head" with some text through a model to find 
        topics. Start with the name of the brainstorm and the entire text.
        The model will return topics and the parts of the text that belong 
        to each topic (phrases, sentences, etc.). Then perform the same 
        operation with each topic and their corresponding texts to find 
        subtopics. End recursion when the best number of topics for a text 
        is 1.
        '''
        ### METHOD INCOMPLETE ###
        if not self.validate_input(name, text):
            return None

        head = self.Node(name)
        
        return head

    def fill_map(self, parent, text):
        ### METHOD INCOMPLETE ###
        if not text:
            return
        

    def validate_input(self, name, text):
        ### METHOD INCOMPLETE ###
        return False

    def __str__(self) -> str:
        '''This is to help the custom field for the django model'''
        if not self.validate_input(self.name, self.text):
            return 'Unable to create mind map'
        return str(self.map.name)