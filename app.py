import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from constants import CONST_RAND_STR
from models import ConversationRequest, ConversationResponse

app = FastAPI(title="aifaq")

# TODO: Fix allowed origins, only allow "*" on dev environments
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/conversation")
def post_conversation(item: ConversationRequest) -> ConversationResponse:
    text = " ".join(random.choices(CONST_RAND_STR.split(), k=int(item.length)))
    return ConversationResponse(response=text)