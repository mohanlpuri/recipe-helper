
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = OpenAI(temperature=0)
parser = StrOutputParser()

# -----------------------------
# Chain 1: Best dish for a place
# -----------------------------
bestDishTemplate = PromptTemplate(
    input_variables=["place"],
    template=(
        "You are a food expert. For the place: {place}, "
        "name ONE most iconic/local dish. Return ONLY the dish name, nothing else."
    ),
)
dish_chain = bestDishTemplate | llm | parser

# -----------------------------
# Chain 2: Recipe for a dish
# -----------------------------
recipeTemplate = PromptTemplate(
    input_variables=["place", "dish"],
    template=(
        "Give a clear, beginner-friendly recipe for '{dish}' from {place}.\n"
        "Include:\n"
        "1) Ingredients (with quantities)\n"
        "2) Steps\n"
        "3) Optional tips/variations\n"
        "Keep it practical and formatted with headings."
    ),
)
recipe_chain = recipeTemplate | llm | parser

# -----------------------------
# Combined chain: sequential
# Input:  {"place": "..."}
# Output: {"place": "...", "dish": "...", "recipe": "..."}
# -----------------------------
combined_chain = (
    RunnablePassthrough()
    .assign(dish=dish_chain)
    .assign(recipe=recipe_chain)
)
