from typing import cast
from prepsaa.models import QnAModel, StudyNoteModel
from prepsaa.utils import llm_model_factory
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from textwrap import dedent
from notion_client import Client as NotionClient

from prepsaa.settings import settings
from notionize import notionize


def answer_question(model_name: str, question: str) -> QnAModel:
    parser = PydanticOutputParser(pydantic_object=QnAModel)
    prompt = PromptTemplate(
        template=dedent("""\
            You are a helpful assistant that answer a <question> about AWS SAA exam.

            <format>
            {format}
            </format>

            <question>
            {question}
            </question>"""),
        input_variables=["question", "format"],
        partial_variables={"format": parser.get_format_instructions()},
    )
    model = llm_model_factory(model_name)
    chain = prompt | model | parser
    print("🔥 질문에 대한 답변을 생성합니다...")
    result = cast(QnAModel, chain.invoke({"question": question}))
    return result


def explain_service(model_name: str, service_name: str) -> StudyNoteModel:
    parser = PydanticOutputParser(pydantic_object=StudyNoteModel)
    prompt = PromptTemplate(
        template=dedent("""\
            You are an expert AWS tutor specializing in preparing candidates for the AWS Certified Solutions Architect - Associate (SAA-C03) exam. Your primary focus is helping candidates avoid common pitfalls and understand the critical differences between related services.

            Your task is to generate concise, targeted study notes in a **markdown list format** for the following AWS service(s), emphasizing common misconceptions and key differentiators.

            <format>
            {format}
            </format>

            <service>
            {input}
            </service>"""),
        input_variables=["input", "format"],
        partial_variables={"format": parser.get_format_instructions()},
    )
    model = llm_model_factory(model_name)
    chain = prompt | model | parser
    print("🔥 학습 노트를 생성합니다...")
    result = cast(StudyNoteModel, chain.invoke({"input": service_name}))
    return result


def save_to_notion(
    notion_client: NotionClient, service_name: str, content: str
) -> None:
    print("🔥 학습 노트를 Notion에 저장합니다...")
    notion_client.pages.create(
        parent={"database_id": settings.notion_database_id},
        icon={"type": "emoji", "emoji": "📚"},
        properties={
            "title": {
                "title": [
                    {
                        "type": "text",
                        "text": {"content": f"{service_name} 학습 노트"},
                    }
                ]
            },
            "Tags": {
                "multi_select": [
                    {"name": "AWS SAA"},
                    {"name": service_name},
                ]
            },
        },
        children=notionize(content),
    )
