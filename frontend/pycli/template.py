class Template:

    
    def __init__(self, action_name, stateful=False, *args, **kwargs):
        self.stateful = stateful
        self.action_name = action_name
        self.const = None
        self.types = None
        self.interfaces = None
        self.namespaces={
            'camel_case': self._camel_case(),
            'snake_case': self._snake_case()
        }


    def connect_actiontypes(self, filename):
        print(filename)



    def _camel_case(self):
        if self.stateful:
            begin = self.action_name+"Begin"
            success = self.action_name+"Success"
            error = self.action_name+"Error"
            return [begin, success, error]
        else:
            return [self.action_name]

 
    def _snake_case(self):

        indexes = []
        [indexes.append(counter) for counter, element in enumerate(
            list(self.action_name)) if element.isupper()]

        last_index = 0
        text = ""
 

        last_index = 0
        text = ""

        for counter, item in enumerate(list(self.action_name)):
            if counter == 0:
                text += item.lower()
            elif counter > 0 and item.isupper() == True:
                text += "_"+item.lower()
            else:
                text += item.lower()
        if self.stateful is True:
            begin = text +"_begin"
            success = text + "_success"
            error = text + "_error"
            return [begin, success, error]
        else:
            return [text]

    def __repr__(self):
        return str(self.namespaces)



 
 
 
