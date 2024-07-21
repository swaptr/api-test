from pydantic import BaseModel, ConfigDict


class ConversationRequest(BaseModel):
    length: int
    text: str

    model_config = ConfigDict(use_enum_values=True)


class ConversationResponse(BaseModel):
    response: str