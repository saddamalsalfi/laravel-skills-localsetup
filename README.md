---
name: "laravel-skills-localsetup"
title: "Laravel 13 Local Development Setup & Verification"
description: "Professional, deterministic AI agent skill and Cursor rule for setting up, configuring, and verifying a local Laravel 13 development environment"
version: "1.0.0"
author: "Saddam Al-Slfi"
repository: "https://github.com/saddamalsalfi/laravel-skills-localsetup"
license: "MIT"
created_at: "2026-09-12"
---

# Laravel 13 Local Development Setup & Verification 🐘⚡

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Open Plugins Compliant](https://img.shields.io/badge/Open%20Plugins-Compliant-success.svg)](https://open-plugins.com)
[![Cursor Rule](https://img.shields.io/badge/Cursor%20Rule-.mdc-purple.svg)](rules/laravel-skills-localsetup.mdc)
[![Laravel](https://img.shields.io/badge/Laravel-13.x-red.svg)](https://laravel.com)

A battle-tested, production-grade AI agent skill and **Cursor Rule** engineered to guide AI coding assistants (Cursor, Google Antigravity / Gemini, Claude Code, GitHub Copilot, LangChain agents) through configuring, provisioning, and verifying modern **Laravel 13** local development environments with deterministic accuracy and zero hallucinations.

Optimized for submission to **[cursor.directory](https://cursor.directory)**, **[LangChain Hub](https://smith.langchain.com/hub)**, and **[Open Plugins](https://open-plugins.com)**.

---

## 🎯 What This Skill Solves

Standard AI models frequently fail when provisioning local Laravel projects: they hallucinate outdated artisan commands, ignore host vs. container environments, corrupt database configs, and miss vital 2FA or Livewire requirements.

This skill forces the AI agent to follow a strict, deterministic, step-by-step engineering protocol:
- **Runtime Pre-flight & Discovery:** Probes the operating system (Host, WSL2, Docker, remote container) before executing commands; asks for explicit confirmation before installing tools.
- **Modern Laravel 13 Stack:** Scaffolds starter kits with **Livewire Single-File Components (SFC)**, Team management, and Tailwind CSS.
- **Complete Auth & Security:** Integrates registration, email verification, two-factor authentication (2FA), passkeys, and test user seeders.
- **AI Coding Integration:** Out-of-the-box setup for Laravel Boost, coding agent guidelines, and MCP server configuration.
- **Deterministic Health Checks:** Verifies dev servers (`artisan serve`, `npm run dev`), database connections, and resolves port collisions safely.

---

## 📂 Repository Structure (Open Plugins Standard)

This repository follows the **[Open Plugins Standard](https://open-plugins.com)** for plug-and-play installation across agent platforms:

```text
├── skills/
│   └── laravel-skills-localsetup/
│       └── SKILL.md                 # Agent workflow for Antigravity, Claude Code, etc.
├── rules/
│   └── laravel-skills-localsetup.mdc # Optimized rule for Cursor IDE
├── mcp.json                         # Model Context Protocol configuration
├── plugin.json                      # Open Plugins manifest
├── LICENSE                          # MIT License with explicit AI Agent Grant
└── README.md                        # Documentation and usage guides
```

---

## 🚀 Quick Start & Installation

### 1. Cursor IDE (via `cursor.directory` or local)
Copy the `.mdc` rule into your project's `.cursor/rules/` directory:
```bash
mkdir -p .cursor/rules
curl -o .cursor/rules/laravel-skills-localsetup.mdc https://raw.githubusercontent.com/saddamalsalfi/laravel-skills-localsetup/main/rules/laravel-skills-localsetup.mdc
```

### 2. Google Antigravity / Gemini IDE
Add the skill into your project's `.agents/skills/` directory:
```bash
mkdir -p .agents/skills/laravel-skills-localsetup
curl -o .agents/skills/laravel-skills-localsetup/SKILL.md https://raw.githubusercontent.com/saddamalsalfi/laravel-skills-localsetup/main/skills/laravel-skills-localsetup/SKILL.md
```

### 3. Open Plugins CLI / Package Manager
Install directly using the repository URL:
```bash
open-plugins install https://github.com/saddamalsalfi/laravel-skills-localsetup
```

### 4. Claude Code / LangChain Hub / Custom Agents
Load [`skills/laravel-skills-localsetup/SKILL.md`](skills/laravel-skills-localsetup/SKILL.md) directly into your agent's system prompt or project knowledge base.

---

## 📋 Execution Phases Overview

When activated, the agent executes the following stages in order:

| Phase | Description | Key Deliverables |
| :--- | :--- | :--- |
| **1. Runtime Discovery** | Inspects host OS, WSL distribution, PHP 8.2+, Composer, Node.js, and DB engines | Pre-flight compatibility matrix |
| **2. Scaffolding** | Creates starter-kit Laravel 13 app with single-file components | Clean app skeleton & git init |
| **3. Database & Cache** | Provisions MySQL / PostgreSQL / SQLite, configures `.env`, runs migrations | Verified database connection |
| **4. Auth & Security** | Configures Fortify / starter auth with 2FA, passkeys, and seeded accounts | Working authentication suite |
| **5. AI Tooling** | Sets up guidelines, MCP configuration, and agent instructions | Optimized developer workflow |
| **6. Verification** | Boots dev servers, tests endpoints, performs end-to-end smoke check | Verified working URLs & ports |

---

## 🛡️ Guiding Principles

1. **Safety First:** Never overwrite existing files, databases, or environment variables without explicit user authorization.
2. **Deterministic Outputs:** Every command flag is verified against official Laravel 13 release specifications.
3. **Reproducibility:** Generates reproducible scripts and idempotent configurations suitable for solo devs and teams.

---

## 📄 License & Attribution

Authored by **Saddam Al-Slfi** ([@saddamalsalfi](https://github.com/saddamalsalfi)).

This repository is licensed under the **[MIT License](LICENSE)** with a **Special Grant for Artificial Intelligence (AI) Agents & Automated Systems**, permitting free ingestion, adaptation, and execution by all AI agents and developers.