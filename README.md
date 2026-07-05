# Knowledge Base Agent

[![CI](https://github.com/kogunlowo123/knowledge-base-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/knowledge-base-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Customer Service | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Knowledge base management agent that identifies content gaps, generates help articles from resolved tickets, maintains article freshness, optimizes search relevance, and tracks article effectiveness.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `identify_content_gaps` | Identify missing knowledge base articles from support ticket analysis |
| `generate_article` | Generate a help article from resolved support tickets |
| `audit_freshness` | Audit knowledge base articles for outdated content |
| `optimize_search` | Optimize article search relevance and tagging |
| `track_effectiveness` | Track article view rates, helpfulness votes, and deflection rates |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/knowledge-base/analyze` | Run analysis |
| `POST` | `/api/v1/knowledge-base/execute` | Execute action |
| `GET` | `/api/v1/knowledge-base/metrics` | Get metrics |
| `PUT` | `/api/v1/knowledge-base/configure` | Update configuration |
| `POST` | `/api/v1/knowledge-base/report` | Generate report |

## Features

- Knowledge
- Base
- Analytics
- Automation

## Integrations

- Zendesk
- Intercom
- Salesforce Service
- Freshdesk
- Hubspot Service

## Architecture

```
knowledge-base-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── knowledge_base_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Customer Service Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
