import sys
import os
from pprint import pprint

import collections








class container(collections.UserDict):
    def __init__(self, *args, **kwargs):
        pass

 
class Template:

    def __init__(self, action_name, stateful=False, *args, **kwargs):
        self.stateful = stateful
        self.action_name = action_name
        self.const = None
        self.types = None
        self.interfaces = None
        self.namespaces = {
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
            begin = text + "_begin"
            success = text + "_success"
            error = text + "_error"
            return [begin, success, error]
        else:
            return [text]

    def __repr__(self):
        return str(self.namespaces)




     





def getTemplate(component_name="defaultTitle"):
    component_name = component_name[0].upper() + component_name[1:]
    COMPONENT_TEMPLATE=f'''
    import * as React from "react";
 

    import {"{"} AllAppActions {"}"} from '../reducers/actions/AllActionsTypes';

    import {"{"} ThunkDispatch {"}"}  from "redux-thunk";
    import {"{"} bindActionCreators {"}"}  from 'redux';
    import {"{AppState}"} from "../reducers/ConfigureStore";
    import {"{connect}"} from 'react-redux';

    export interface {component_name}Props{"{}"}

    interface LinkStateToProps{"{}"}

    const mapStateToProps=(state:AppState,
    ownProps:{component_name}Props):LinkStateToProps=>
    ({"{"} {"}"} ) 

    interface LinkDispatchToProps{"{}"}

    const mapDispatchToProps=(
        dispatch: ThunkDispatch<any, any, AllAppActions>,
        ownProps: {component_name}Props
    ):LinkDispatchToProps=>({"{}"})

    type Props ={component_name}Props & LinkStateToProps & LinkDispatchToProps;

    const {component_name}Component=(Props:Props)=>{"{"}
    return(
        <div> </div>
    )
    
    {"}"}

    export default connect(null, null)({component_name}Component)
    '''
    
    return COMPONENT_TEMPLATE

def getComponent(component_title="defaultTitle"):
    component_title = component_title[0].upper() + component_title[1:]
    f = open(component_title+"Component.tsx", "w")
    f.write(getTemplate(component_title))
    f.close()

 

def getPath():
    os.chdir("root/frontend/src/components")


def braces(name):
    return f'{"{"}'+name+f'{"}"}'

def get_reducer_template(reducer_name):
    name = reducer_name[0].upper()+reducer_name[1:]
    template = f'''
import {braces("I"+name+"State")} from "./{name}Types";
import {braces(name+"ActionTypes" )} from "./{name}Actions";
import * as constants from './{name}Actions';

const {name}ReducerDefaultState : I{name}State = {"{"}
{"}"}


const {name}Reducer=(
        state = {name}ReducerDefaultState,
        action: {name}ActionTypes
        ):I{name}State => {"{"}
            switch(action.type){"{"}
                default:
                    return state;
            {"}"}
        {"}"}

        
export {braces(name+"Reducer")}


'''
    return template
def get_actions_template(reducer_name):
    name = reducer_name[0].upper()+reducer_name[1:]
    template = f'''

export const TEST_DATA_BEGIN = "TEST_DATA_BEGIN"



//INTERFACES
export interface TestDataBegin{"{"}
    type: typeof TEST_DATA_BEGIN


{"}"} 

//TYPES
export type {name}ActionTypes=
    | TestDataBegin

export type AppActions = {name}ActionTypes;


'''

    return template

def get_types_template(reducer_name):
    name = reducer_name[0].upper()+reducer_name[1:]
    template=f'''

export interface I{name}State{"{"}

{"}"}

'''
    return template
    
def create_reducer(reducer_name):
    
    os.mkdir("reducer_"+reducer_name.lower())
    os.chdir("reducer_"+reducer_name.lower())
    with open(reducer_name[0].upper()+reducer_name[1:]+"Reducer.tsx", "w") as f:
        f.write(get_reducer_template(reducer_name))
        f.close()
    with open(reducer_name[0].upper()+reducer_name[1:]+"Types.tsx", "w") as f:
        f.write(get_types_template(reducer_name))
        f.close()     
    with open(reducer_name[0].upper()+reducer_name[1:]+"Actions.tsx", "w") as f:
        f.write(get_actions_template(reducer_name))
        f.close()
    os.chdir("..")


def connect_reducer(reducer_name):
    name = reducer_name[0].upper()+reducer_name[1:]
 
    result = ""
    with open("ConfigureStore.tsx", "r") as f:
        cur = f.read()
        necesary_index = cur.find("combineReducers({")+ "combineReducers({".__len__()+1 
        result += cur[:necesary_index]

        result += f"    {name}Reducer,\n"
        result += cur[necesary_index:]

    with open("ConfigureStore.tsx", "w") as f:
         f.write(result)

    result = "import {"+ name+"Reducer} from './reducer_"+name.lower()+"/"+name+"Reducer' ;\n"

    with open("ConfigureStore.tsx", "r") as f:
        result+= f.read()

    with open("ConfigureStore.tsx", "w") as f:
        f.write(result)

    os.chdir('actions')
    allactionstypes = ""
    with open('AllActionsTypes.tsx', 'r') as f:
        content = f.read()

    allactionstypes+="import {"+ name+"ActionTypes} from '../reducer_"+name.lower()+f"/{name}Actions';\n"

    index_start = content.find("export type AllActionTypes=")
    index_end = index_start + len("export type AllActionTypes=")

    allactionstypes +=content[:index_end]
    allactionstypes += f"\n         | {name}ActionTypes"

    allactionstypes+=content[index_end:]
            
        
    with open('AllActionsTypes.tsx', 'w') as f:
        f.write(allactionstypes)

    with open('AllActions.tsx', 'r') as f:
        content = f.read()

    result = f"import * as {name.lower()}Constants from '../reducer_{name.lower()}/{name}Actions'\n"
    result += content

    with open('AllActions.tsx', 'w') as f:
        f.write(result)
        
    
def connect_action(reducer, action, stateful=False):
    a_file = reducer[0].upper()+reducer[1:]+"Actions.tsx"
    r_file = reducer[0].upper()+reducer[1:]+"Reducer.tsx"
    t_file = reducer[0].upper()+reducer[1:]+"Types.tsx"
    extension = ""
    template = Template(action, stateful=stateful)
    content = None
    with open(a_file, "r") as f:
        content = f.read()

    print("ADDING NEW EXPORTS")
    for element in template._snake_case():
        extension += f"export const {element.upper()} = '{element.upper()}';\n"


    print("CURRENT FILE IS ")
    print(" --------------------------------------------------------------------------------")
    print(extension)
    print(" --------------------------------------------------------------------------------")
    

    

    queryOne = r"//INTERFACES"
    indexOne = int(content.find(queryOne))+len(queryOne)
    print("ADDING OLD EXPORTS")
    extension += content[: indexOne] + "\n"
    
    print("CURRENT FILE IS ")
    print(" --------------------------------------------------------------------------------")
    print(extension)
    print(" --------------------------------------------------------------------------------")


    print("ADDING NEW INTERFACES")
    for counter, element in enumerate(template._camel_case()):
        extension += f'export interface {element}{"{"}\n    type: typeof {template.namespaces["snake_case"][counter].upper()}\n{"}"} '

        
    print("CURRENT FILE IS ")
    print(" --------------------------------------------------------------------------------")
    print(extension)
    print(" --------------------------------------------------------------------------------")

    queryTwo = f"export type {reducer}ActionTypes="
    indexTwo = int(content.find(queryTwo)) + len(queryTwo)

    print("ADDING OLD INTERFACES")
    extension += content[indexOne:indexTwo]
    extension += "\n"


    print("CURRENT FILE IS ")
    print(" --------------------------------------------------------------------------------")
    print(extension)
    print(" --------------------------------------------------------------------------------")



    print("ADDING NEW TYPES")
    for element in template._camel_case():
        extension += f"    | {element} "

    print("CURRENT FILE IS ")
    print(" --------------------------------------------------------------------------------")
    print(extension)
    print(" --------------------------------------------------------------------------------")


    
    print("ADDING OLD TYPES AND REST OF FILE")
    
    extension += content[indexTwo:]

    print("CURRENT FILE IS ")
    print(" --------------------------------------------------------------------------------")
    print(extension)
    print(" --------------------------------------------------------------------------------")



    with open("TEST.tsx", "w") as f:
        f.write(extension)

    with open(a_file, "w") as f:
        f.write(extension)

    with open(r_file, "r") as f:
        content = f.read()

    reducer_temp = ""
    breakpoint = "switch(action.type){\n"
    checkpoint = content.find(breakpoint)
    reducer_temp += content[:checkpoint+len(breakpoint)]+"\n"

    for element in template._snake_case():
        reducer_temp += f'''        case constants.{element.upper()}:\n            return state;\n'''
    reducer_temp += content[checkpoint+len(breakpoint):]

    with open(r_file, "w") as f:
        f.write(reducer_temp)



    
 

def main():
 
    for counter, arg in enumerate(sys.argv):
        if arg=="create-component":
            try:
                os.chdir("src/components")
                component_name = sys.argv[counter+1]
                component_name = component_name[0].upper() + component_name[1:]
                getComponent(component_name)
                os.chdir("..")
                print("current dir is " + os.getcwd(), sep=" ")
                with open("Master.tsx", "r") as f: data = f.read()
                
                f = open("Master.tsx", "w")
                
                f.write(f'import {component_name}Component from "./components/{component_name}Component" \n'+data)
                f.close()
                
            except:
                print("Please enter component name", file = sys.stderr)
        if arg=="create-reducer":
             
            try:
                print("creating reducer", sys.argv[counter+1], sep=" ")
     
                if "src" in os.listdir(os.getcwd()):
                    os.chdir('src')
                    if 'reducers' in os.listdir(os.getcwd()):
                        os.chdir('reducers')
                        if not set(['actions', 'ConfigureStore.tsx']).issubset(os.listdir(os.getcwd())):
                            print("Reducer folder not properly terminated. Make sure to have both ConfigureStore.tsx and actions folder",file=sys.stderr)
                        reducer_name = sys.argv[counter+1]
                        create_reducer(reducer_name)
                        connect_reducer(reducer_name)                                                                                        
                    else:
                        print("Reducers directory is not existing. Please create reducer store",file=sys.stderr)
                    
                else:
                    print("Wrong directory. Make sure to be inside frontend directory. ", file=sys.stderr)
                                                                
            except:
                pass
        if arg=="create-action":
            action_name = sys.argv[counter+1]
            reducer_name = sys.argv[counter+2].lower()
            

    
            os.chdir('src')
            os.chdir('reducers')
            
             
            reducers = [ file.split("_")[1] for file in os.listdir(os.getcwd()) if "_" in file and "." not in file]

            if reducer_name in reducers:
                os.chdir(f"reducer_{reducer_name}")
                
        
                if "-stateful" in sys.argv:

                    connect_action(reducer_name, action_name, stateful=True)
                else:
                    connect_action(reducer_name, action_name, stateful=False)

            else:
                print("it does not exists")
        if arg=="debug":
            print(os.getcwd())

    


class Project:
    def __init__(self):
        self.base_dir=os.getcwd()
        self.components = []
        self.reducers = []
        self.get_components()
        self.get_reducers()

    @property
    def c(self):
        return self.components

    @property
    def r(self):
        return self.reducers
    
    def get_components(self):
        os.chdir('src/components')
        for x in os.listdir(os.getcwd()):
            self.components.append((x, os.path.abspath(x)))
        os.chdir(self.base_dir)

    def get_reducers(self):
 
        os.chdir("src/reducers")
        
        for x in os.listdir(os.getcwd()):
            if x!="actions" and x!="ConfigureStore.tsx":
                self.reducers.append((x, os.path.abspath(x)))
        os.chdir(self.base_dir)
        
        
  
        
        
    


if __name__=="__main__":
    main()


 
