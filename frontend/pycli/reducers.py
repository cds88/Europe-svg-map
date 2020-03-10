 
import os
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



 
 
def connect_action(reducer, action, stateful=False):
    a_file = f"{reducer}Actions.tsx"
    r_file = reducer[0].upper()+reducer[1:]+"Reducer.tsx"
    t_file = reducer[0].upper()+reducer[1:]+"Types.tsx"
    extension = ""
    template = Template(action, stateful=stateful)
    content = None

    for element in template._snake_case():
        extension += f"export const {element.upper()} = '{element.upper()}';\n"


    with open(a_file, "r") as f:
        content = f.read()

    queryOne = r"//INTERFACES"
    indexOne = int(content.find(queryOne))+len(queryOne)

    extension += content[: indexOne] + "\n"


    for counter, element in enumerate(template._camel_case()):
        extension += f'export interface {element}{"{"}\n    type: typeof {template.namespaces["snake_case"][counter].upper()}\n{"}"} '


    queryTwo = f"export type {reducer}ActionTypes="
    indexTwo = int(content.find(queryTwo)) + len(queryTwo)

    extension += content[indexOne:indexTwo]
    extension += "\n"
    for element in template._camel_case():
        extension += f"    | {element} "


    extension += content[indexTwo:]


    with open(a_file, "w") as f:
        f.write(extension)
 



    with open(r_file, "r") as f:
        content = f.read()

    reducer_temp=""
    breakpoint = "switch(action.type){\n"
    checkpoint = content.find(breakpoint)
    reducer_temp+=content[:checkpoint+len(breakpoint)]+"\n"
    
    for element in template._snake_case():
        reducer_temp+=f'''        case constants.{element.upper()}:\n            return state;\n'''
    reducer_temp+=content[checkpoint+len(breakpoint):]

    with open(r_file, "w") as f:
        f.write(reducer_temp)
 
    
         
    
    
 

if __name__=="__main__":
    pass

