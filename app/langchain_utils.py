from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize ChatOpenAI
llm = ChatOpenAI(
    model_name="gpt-4",
    temperature=0.7
)

# Template for initial assessment
assessment_prompt = PromptTemplate(
    input_variables=["user_name"],
    template="""
You are a Python learning assistant. Create a short quiz to evaluate the Python knowledge of a user named {user_name}.
The quiz should have:
1. Three multiple-choice questions (easy, medium, and hard).
2. A single coding question that assesses problem-solving skills.
Output the quiz in JSON format.
"""
)

# Create a chain for generating the quiz
def generate_initial_quiz(user_name: str):
    chain = LLMChain(llm=llm, prompt=assessment_prompt)
    return chain.run(user_name=user_name)
