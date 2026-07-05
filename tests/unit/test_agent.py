"""Knowledge Base Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_identify_content_gaps():
    """Test Identify missing knowledge base articles from support ticket analysis."""
    tools = AgentTools()
    result = await tools.identify_content_gaps(period="test", min_ticket_count=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_article():
    """Test Generate a help article from resolved support tickets."""
    tools = AgentTools()
    result = await tools.generate_article(topic="test", source_tickets="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_audit_freshness():
    """Test Audit knowledge base articles for outdated content."""
    tools = AgentTools()
    result = await tools.audit_freshness(max_age_days=1, category="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_optimize_search():
    """Test Optimize article search relevance and tagging."""
    tools = AgentTools()
    result = await tools.optimize_search(category="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.knowledge_base_agent_agent import KnowledgeBaseAgentAgent
    agent = KnowledgeBaseAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
