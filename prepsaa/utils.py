import re
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chat_models.base import BaseChatModel
from prepsaa.settings import settings


def llm_model_factory(
    name: str,
) -> BaseChatModel:
    if name.startswith("claude"):
        return ChatAnthropic(
            model_name=name,
            api_key=settings.anthropic_api_key,
            temperature=0.0,
            max_retries=3,
            timeout=None,
            stop=None,
        )
    elif name.startswith("gpt"):
        return ChatOpenAI(
            name=name,
            model=name,
            api_key=settings.openai_api_key,
            temperature=0.0,
            max_retries=3,
        )
    elif re.match(r"^o\d", name):
        return ChatOpenAI(
            name=name,
            model=name,
            api_key=settings.openai_api_key,
            max_retries=3,
        )
    elif name.startswith("gemini"):
        return ChatGoogleGenerativeAI(
            name=name,
            model=name,
            api_key=settings.google_api_key,
            temperature=0.0,
            max_retries=3,
        )
    else:
        raise ValueError(f"Unknown model: {name}")
