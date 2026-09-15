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

The repository is organized modularly by ecosystem and framework:

```text
skills/
├── README.md
├── laravel/
│   ├── README.md
│   ├── Laravel Multilingual Implementation.md
│   └── laravel local setup.md
├── python/             # (Upcoming)
└── nextjs/             # (Upcoming)
```

---

## 📦 Available Skills

### 🐘 Laravel Ecosystem

| Skill | Description | Target |
| --- | --- | --- |
| [**Laravel Multilingual Implementation**](./laravel/Laravel%20Multilingual%20Implementation.md) | Full-lifecycle internationalization (i18n) and localization (L10n). Covers prefix routing via `mcamara/laravel-localization`, strict Filament admin panel isolation, queue-safe locale resets, and translatable Eloquent models. | Laravel 10 / 11 / 12 / 13 |
| [**Laravel 13 Local Development Setup**](./laravel/laravel%20local%20setup.md) | Comprehensive, deterministic workflow to prepare and verify a local Laravel 13 development environment. Configures starter kits (Livewire SFC / Teams), authentication (2FA, passkeys), database engines, and AI coding agent integration (GitHub Copilot, Cursor, MCP). | Laravel 13.x |

---

## 🚀 How to Use These Skills

You can load these instructions directly into your favorite AI tool or coding assistant:

### 1. Cursor IDE
Copy any skill into your project's `.cursor/rules/` directory with a `.mdc` extension:
```bash
mkdir -p .cursor/rules
cp "path/to/skills/laravel/laravel local setup.md" .cursor/rules/laravel-local-setup.mdc
```

### 2. Google Antigravity / Gemini IDE
Add the skill to your project workspace under `.agents/skills/<skill-name>/SKILL.md` or reference it directly in `.gemini/config/`.

### 3. GitHub Copilot
Include the skill contents or reference them in your `.github/copilot-instructions.md`.

### 4. Claude Projects / Custom GPTs
Upload the Markdown skill file directly into the project's knowledge base or attach it as context for specialized development sessions.

---

## 🛡️ Guiding Principles

1. **Production-Ready over Toy Demos:** Every rule is designed for real-world production environments, accounting for race conditions, security, and edge cases.
2. **Zero Hallucination Tolerance:** Exact command flags, correct directory structures, and verified framework conventions.
3. **Idempotency & Safety:** Scripts and steps avoid destructive actions and always confirm before installing software or executing risky operations.

---

## 📄 License & Ownership

This project is authored by **Saddam Al-Slfi** and licensed under the [MIT License](LICENSE). It is open source and freely available for use, reproduction, modification, and integration by human developers, automated systems, and all Artificial Intelligence (AI) agents and models.