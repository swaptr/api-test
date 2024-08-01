from pydantic import BaseModel

class ConversationRequest(BaseModel):
    question: str

class ConversationResponse(BaseModel):
    answer: str
