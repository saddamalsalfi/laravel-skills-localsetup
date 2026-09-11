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

---

## ⚙️ Quick Start

To apply any Laravel skill to your coding assistant:

### Option A: Cursor IDE
Place the rule inside your project root:
```bash
# Create a dedicated rule for localization
mkdir -p .cursor/rules
cp "path/to/skills/laravel/Laravel Multilingual Implementation.md" .cursor/rules/laravel-multilingual.mdc