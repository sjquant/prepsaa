from textwrap import dedent
from pydantic import BaseModel, Field

from prepsaa.constants import NOTE_CONTENT_DESCRIPTION, QNA_EXAMPLE, NOTE_EXAMPLE


class QnAModel(BaseModel):
    explanation: str = Field(
        description=dedent(
            """\
            - Analyze the problem requirements to identify the core concepts.
            - Evaluate each answer choice, explaining the strengths and weaknesses, and clarify why a particular choice is correct or incorrect.
            - Write in Korean, following the format shown in the examples field."""
        ),
        examples=[QNA_EXAMPLE],
    )
    answer: list[str] = Field(
        description="Answer to the question",
    )
    used_services: set[str] = Field(
        description=dedent(
            """\
            - List ALL AWS services mentioned in the question and answer choices.
            - Normalize the service names: remove prefixes like 'AWS' and use the standard abbreviation (e.g., 'SQS' instead of 'Simple Queue Service').
            - Ensure every mentioned service is included, using its normalized name.
            - Do not skip any service, even if it appears multiple times."""
        ),
        examples=["EC2", "SQS", "CloudTrail", "EventBridge"],
    )


class StudyNoteModel(BaseModel):
    content: str = Field(description=NOTE_CONTENT_DESCRIPTION, examples=[NOTE_EXAMPLE])
