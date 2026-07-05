"""Test configuration for Knowledge Base Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "knowledge-base-agent", "category": "Customer Service"}
