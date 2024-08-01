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

responses = {
    "what_is_hyperledger_fabric": {
        "answer": "Hyperledger Fabric is an open-source blockchain framework designed for enterprise solutions. It allows for a modular architecture where different components like consensus mechanisms, membership services, and ledger storage can be tailored to specific needs."
    },
    "how_to_install_hyperledger_fabric": {
        "answer": "To install Hyperledger Fabric, follow these steps:\n"
                  "1. Install Docker and Docker Compose.\n"
                  "2. Download the Hyperledger Fabric binaries and docker images using the Fabric CA and Fabric binaries script.\n"
                  "3. Set up the environment variables for Fabric binaries.\n"
                  "4. Verify the installation by running Fabric sample network scripts."
    },
    "how_to_deploy": {
        "answer": "To deploy a Hyperledger Fabric network:\n"
                  "1. Define the network topology and configuration files (e.g., 'configtx.yaml').\n"
                  "2. Use the 'fabric-cli' or scripts to create channel artifacts.\n"
                  "3. Launch the network by starting the necessary Docker containers and services using 'docker-compose' or Kubernetes.\n"
                  "4. Instantiate and upgrade chaincode as needed."
    },
    "how_to_run": {
        "answer": "To run a Hyperledger Fabric network:\n"
                  "1. Start the network by running 'docker-compose up' or the appropriate command for your setup.\n"
                  "2. Use the Fabric CLI tools or SDKs to interact with the network, including creating and joining channels, and submitting transactions.\n"
                  "3. Monitor the network's health and performance using Fabric's built-in tools or external monitoring solutions."
    },
    "how_to_ensure_data_privacy": {
        "answer": "To ensure data privacy in Hyperledger Fabric:\n"
                  "1. Use private data collections to restrict access to sensitive data.\n"
                  "2. Implement access control policies and endorsement policies.\n"
                  "3. Utilize encryption for data at rest and in transit.\n"
                  "4. Regularly review and update security configurations and practices."
    }
}

@app.post("/conversation", response_model=ConversationResponse)
def post_conversation(item: ConversationRequest) -> ConversationResponse:
    question_key = item.question.lower().replace(" ", "_").replace("?", "")
    if question_key in responses:
        return ConversationResponse(answer=responses[question_key]['answer'])
    else:
        raise HTTPException(status_code=404, detail="Question not found. Please check the question and try again.")
