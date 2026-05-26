from langchain_core.tools import Tool

from tools.file_tools import create_file, update_file, delete_file

from tools.vector_tools import vector_search_tool

from middleware.human_loop import human_approval

from middleware.retry_middleware import retry_tool

from middleware.pii_detection import mask_pii

from middleware.summarization import summarize_context

# File Agent Wrapper
def safe_create_file(file_name, content):
    content = mask_pii(content)
    content = summarize_context(content)
    action = (f"Create file {file_name}")

    approved = human_approval(action)

    if not approved:
        return "Action denied"

    return retry_tool(create_file, file_name, content)

# Tool Definitions
tools = [
    Tool(name="CreateFile", func=lambda x: safe_create_file("sample.txt", x),
    description="Create a file"),

    Tool( name="SearchKnowledgeBase", func=vector_search_tool,
        description="Search vector knowledge base")
]

# Demo Execution
print("Vector Search...\n")

result = vector_search_tool("What is LangChain?")
print(result)

print("\nFILE TOOL....")

result = safe_create_file("notes.txt",
    '''
    Contact:
    anil@gmail.com
    Phone: 9999999999
    '''
)

print(result)