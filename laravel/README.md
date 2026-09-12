# Laravel AI Skills & Architecture Rules 🐘

This directory contains production-ready guidelines, constraints, and architecture instructions tailored specifically for modern **Laravel** applications and the **TALL stack** (Tailwind CSS, Alpine.js, Laravel, Livewire) including **Filament**.

These rules enforce Laravel best practices, avoid common AI hallucinations, and ensure strict security, idempotency, and framework conventions across your projects.

---

## 📚 Skills Catalog

### 1. [`Laravel Multilingual Implementation.md`](./Laravel%20Multilingual%20Implementation.md)
* **Goal:** Full-lifecycle internationalization (i18n) and localization (L10n) implementation.
* **Core Philosophy:**
  - **Zero Security Risk in Web Root:** Forbids storing translation files or archives in `public/lang/` to prevent asset exposure. Strictly enforces `<project-root>/lang/` as the sole authoritative path.
  - **SEO & Canonical Routing:** Handles prefix resolution via `mcamara/laravel-localization`, enforces redirect invariants (`hideDefaultLocaleInURL => true`), and prevents redirect loops.
  - **Admin Isolation:** Completely decouples Filament administration panels from public localized routing (no `/ar/admin` or `/en/admin` routes) while keeping language switching seamless via Livewire/Ajax.
  - **Data Integrity:** Manages JSON-backed translatable Eloquent attributes with `spatie/laravel-translatable` without data loss or partial overwrite bugs.
  - **Queue & Worker Safety:** Explicitly isolates and resets locale state inside queue workers and asynchronous jobs to avoid locale leakage across tasks.

### 2. [`laravel local setup.md`](./laravel%20local%20setup.md)
* **Goal:** Setup, configuration, and verification of a local **Laravel 13.x** development environment from scratch or resuming incomplete setups.
* **Core Philosophy:**
  - **Pre-flight & Discovery:** Probes host vs. container/WSL runtime, discovers existing prerequisites (PHP 8.2+, Composer, Node, database engines), and requires explicit approval before installing tools.
  - **Modern Starter Stack:** Configured for Laravel 13.x with Livewire Single-File Components (SFC) preferred, team management support, and choice of frontends (Livewire, Vue, React).
  - **Authentication & Security Suite:** Integrates built-in auth, email verification, two-factor authentication (2FA), passkeys, password confirmation, and pre-seeded test accounts.
  - **AI Agent & Tooling Native:** Out-of-the-box configuration for Laravel Boost, guidelines, skills, MCP configuration, and optimization for coding assistants (GitHub Copilot, Cursor, Gemini, Claude).
  - **Deterministic Verification:** Runs end-to-end health verification for dev servers (`artisan serve`, `npm run dev`), database connections, migrations, and provides actionable troubleshooting for port collisions and missing extensions.

---

## ⚙️ Quick Start

To apply any Laravel skill to your AI coding assistant:

### Option A: Cursor IDE
Place the rule inside your project root (`.cursor/rules/`):
```bash
# Localization skill
mkdir -p .cursor/rules
cp "path/to/skills/laravel/Laravel Multilingual Implementation.md" .cursor/rules/laravel-multilingual.mdc

# Local development setup skill
cp "path/to/skills/laravel/laravel local setup.md" .cursor/rules/laravel-local-setup.mdc
```

### Option B: GitHub Copilot / Antigravity / Gemini / Claude Projects
Attach or reference the markdown file directly in your workspace instructions or system prompts:
- For **Antigravity / Gemini IDE**: Place inside `.agents/skills/<skill-name>/SKILL.md` or invoke as project instruction.
- For **Claude Projects**: Upload the skill file into the Project Knowledge base.
- For **GitHub Copilot**: Add to `.github/copilot-instructions.md` or reference in workspace chat.