---
name: "AI Engineering Skills & Instruction Prompts"
description: "A curated collection of production-grade AI system prompts, skills, and architectural rules designed for AI coding assistants"
version: "1.0.0"
author: "Saddam Al-Slfi"
repository: "https://github.com/saddamalsalfi/skills"
license: "MIT"
created_at: "2026-09-12"
---

# AI Engineering Skills & Instruction Prompts 🧠⚙️

A curated collection of production-grade AI system prompts, skills, and architectural rules designed for AI coding assistants (such as Cursor Rules, Claude Projects, Windsurf, GitHub Copilot, and Google Antigravity / Gemini).

These instructions guide Large Language Models (LLMs) to produce robust, secure, and production-ready code while strictly avoiding common architectural pitfalls, security flaws, and hallucinated patterns.

---

## 📂 Repository Structure

The repository strictly adheres to the **[Open Plugins Standard](https://open-plugins.com)** and Agent Customization specifications, ensuring automatic discovery across Cursor, Google Antigravity, Claude Code, GitHub Copilot, and other agent platforms:

```text
├── skills/
│   ├── laravel-multilingual/
│   │   └── SKILL.md
│   └── laravel-local-setup/
│       └── SKILL.md
├── rules/
│   ├── laravel-multilingual.mdc
│   └── laravel-local-setup.mdc
├── mcp.json
├── plugin.json
├── LICENSE
└── README.md
```

---

## 📦 Available Skills & Rules

### 🐘 Laravel Ecosystem

| Skill (Open Plugins / Agents) | Cursor Rule (.mdc) | Description | Target |
| --- | --- | --- | --- |
| [**laravel-multilingual**](./skills/laravel-multilingual/SKILL.md) | [**laravel-multilingual.mdc**](./rules/laravel-multilingual.mdc) | Full-lifecycle internationalization (i18n) and localization (L10n). Covers prefix routing via `mcamara/laravel-localization`, strict Filament admin panel isolation, queue-safe locale resets, and translatable Eloquent models. | Laravel 10 / 11 / 12 / 13 |
| [**laravel-local-setup**](./skills/laravel-local-setup/SKILL.md) | [**laravel-local-setup.mdc**](./rules/laravel-local-setup.mdc) | Comprehensive, deterministic workflow to prepare and verify a local Laravel 13 development environment. Configures starter kits (Livewire SFC / Teams), authentication (2FA, passkeys), database engines, and AI coding agent integration (GitHub Copilot, Cursor, MCP). | Laravel 13.x |

---

## 🚀 How to Use

### 1. Open Plugins & Agent Discovery (Automatic)
Because this repository follows the Open Plugins standard (`skills/*/SKILL.md`, `rules/*.mdc`, `mcp.json`, `plugin.json`), tools that support Open Plugins can automatically discover and install all skills directly from the repository URL.

### 2. Cursor IDE
Copy the ready-made `.mdc` rules from the `rules/` directory into your project's `.cursor/rules/`:
```bash
mkdir -p .cursor/rules
cp path/to/rules/*.mdc .cursor/rules/
```

### 3. Google Antigravity / Gemini IDE
Copy or link the skill directories directly into your workspace's `.agents/skills/` directory:
```bash
mkdir -p .agents/skills
cp -r path/to/skills/* .agents/skills/
```

### 4. GitHub Copilot / Claude Projects
Reference or upload any `SKILL.md` directly into `.github/copilot-instructions.md` or Claude Project Knowledge.

---

## 🛡️ Guiding Principles

1. **Production-Ready over Toy Demos:** Every rule is designed for real-world production environments, accounting for race conditions, security, and edge cases.
2. **Zero Hallucination Tolerance:** Exact command flags, correct directory structures, and verified framework conventions.
3. **Idempotency & Safety:** Scripts and steps avoid destructive actions and always confirm before installing software or executing risky operations.

---

## 📄 License & Ownership

This project is authored by **Saddam Al-Slfi** and licensed under the [MIT License](LICENSE). It is open source and freely available for use, reproduction, modification, and integration by human developers, automated systems, and all Artificial Intelligence (AI) agents and models.