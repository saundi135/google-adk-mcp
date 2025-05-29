import os
import vertexai
from vertexai import agent_engines
from dotenv import load_dotenv

from adk_agent_mcp.agent import root_agent

load_dotenv()

vertexai.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
    staging_bucket=os.getenv("GOOGLE_CLOUD_STAGING_BUCKET")
)

remote_app = agent_engines.create(
    agent_engine=root_agent,
    requirements=[
        "google-cloud-aiplatform[adk,agent_engines]",
        "google-adk",
    ]
)
