# from anyio import Event
from dotenv import load_dotenv
load_dotenv()
from pydantic import BaseModel
from typing import List, Optional
# pyrefly: ignore [missing-import]
from langchain_core.output_parsers import PydanticOutputParser
# pyrefly: ignore [missing-import]
from langchain_core.prompts import ChatPromptTemplate
# pyrefly: ignore [missing-import]
from langchain_openai import ChatOpenAI
model = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)

class Historica(BaseModel):
    Event_Title: str
    Category: Optional[str]
    Date_Year: str
    Organization: Optional[str]
    People: List[str]
    Location: Optional[str]
    Key_Events: List[str]
    Main_Achievement: Optional[str]
    Significance:Optional[str]
    Summary:str

parser = PydanticOutputParser(pydantic_object=Historica)
prompt_template = ChatPromptTemplate.from_messages([
    (
        "system",
        """
    Extract all the information from the paragraph
    {format_instructions}
        """
    ),
    ('human', 
    "{paragraph}")
])
para = input('Enter you Paragraph: ')
final_prompt = prompt_template.invoke({
    "paragraph": para,
    "format_instructions": parser.get_format_instructions()
})
response = model.invoke(final_prompt)

print(response.content)