from langchain.tools import Tool
from langchain_community.utilities import WikipediaAPIWrapper
import numexpr
from duckduckgo_search import DDGS
from pypdf import PdfReader

wiki = WikipediaAPIWrapper()

def wiki_search(query):
    return wiki.run(query)

def calculator(expression):
    return numexpr.evaluate(expression)

def web_search(query):
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=3))
        return results
    
def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text[:2000]  # limit text

wiki_tool = Tool(
    name="Wikipedia",
    func=wiki_search,
    description="Search information from Wikipedia"
)

calc_tool = Tool(
    name="Calculator",
    func=calculator,
    description="Solve math expressions"
)
web_tool = Tool(
    name="Web Search",
    func=web_search,
    description="Search the internet for recent information"
)
pdf_tool = Tool(
    name="PDF Reader",
    func=read_pdf,
    description="Read text from a PDF document"
)

tools = [wiki_tool, calc_tool,web_tool,pdf_tool]