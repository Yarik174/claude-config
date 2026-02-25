# Claude Config — Yarik174

Глобальные конфиги, скиллы и MCP-серверы для Claude Code.
Работают из **любого проекта** — Antigravity и других.

## Структура

```
skills/
  product-interview/   # Продуктовое интервью → PRD
mcp-servers.json       # Шаблон MCP-серверов (без ключей)
```

## Установка на новую машину

### 1. Склонировать репо

```bash
git clone https://github.com/Yarik174/claude-config.git /tmp/claude-config-setup
```

### 2. Скопировать скиллы глобально

```bash
mkdir -p ~/.claude/skills
cp -r /tmp/claude-config-setup/skills/. ~/.claude/skills/
```

### 3. Добавить MCP-серверы

```bash
# Reddit Research (бесплатно, без ключа)
claude mcp add --scope user --transport http reddit-research https://reddit-research-mcp.fastmcp.app/mcp

# Hacker News (бесплатно, без ключа)
claude mcp add --scope user hn-mcp -- npx -y @devabdultech/hn-mcp-server

# SerpApi — Google Trends + поиск (нужен API ключ: serpapi.com)
claude mcp add --scope user --transport http serpapi https://mcp.serpapi.com/YOUR_SERPAPI_KEY/mcp
```

## Скиллы

| Скилл | Когда использовать |
|---|---|
| `product-interview` | Интервью со стейкхолдером, сбор контекста перед PRD |

## MCP-серверы для анализа рынка

| MCP | Что даёт | Цена |
|---|---|---|
| `reddit-research` | 20k+ сообществ Reddit, поиск болей и отзывов | Бесплатно |
| `hn-mcp` | Hacker News: tech-обсуждения, конкуренты | Бесплатно |
| `serpapi` | Google Trends, Google Search, News | 100 req/мес бесплатно |
| `firecrawl` | Скрейпинг любых сайтов | Встроен в Claude Code |
