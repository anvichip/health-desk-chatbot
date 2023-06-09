from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from memory_bot import get_response
# from langchain.chains import LLMChain, SequentialChain 
# from langchain.memory import ConversationBufferMemory
# from langchain.utilities import WikipediaAPIWrapper 

template1="""I have health condition: {condition} with a severity: {severity}. 
         Give me details about my {condition} and considering the {severity}, what should I do. 
         Tell me the precautions or important cautions to follow"""

template2="""I have health condition: {condition}. 
         Give me details about the {condition} and the precautions or important cautions to follow"""

dropdown_template = PromptTemplate(
    input_variables=["condition","severity"],
    template=template1
)

condition_template = PromptTemplate(
    input_variables=["condition"],
    template=template2
)

def handle_form(cond,sever,message):
    if cond != '' and sever != '':
        print("condition 1 executed")
        output = get_response(dropdown_template.format(condition = cond,severity = sever))
        return output
    
    elif cond != '':
        print("condition 2 executed")
        output = get_response(condition_template.format(condition = cond))
        return output
    
    elif cond == '' and sever == '' and message != '':
        print("condition 3 executed")
        output = get_response(message)
        return output
    




