from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationEntityMemory,ConversationBufferMemory
from langchain.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain.llms import OpenAI
from apikey import api_key

llm = OpenAI(
		temperature=0,
		openai_api_key=api_key,
		verbose=False,
		max_tokens=50,
		model_name="text-davinci-003"
)
	
# Conversation = ConversationChain(
# 	llm=llm, 
# 	prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
# 	memory=ConversationBufferMemory()
# )  

conversation = ConversationChain(
    llm=llm, 
    verbose=True,
    prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
    memory=ConversationEntityMemory(llm=llm)
)
#memory = ConversationBufferMemory()



def get_response(prompt):
	
	#output = Conversation.run(prompt)
	output = conversation.run(input=prompt)  
	print(conversation.memory.entity_store.store)
	return output,prompt
    

