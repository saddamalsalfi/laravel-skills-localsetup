---
name: "Laravel 13 Local Development Setup"
description: "Comprehensive agent workflow for setting up and verifying a local Laravel 13 development environment, starter kits, authentication, database, and AI tooling"
version: "1.0.0"
author: "Saddam Al-Slfi"
repository: "https://github.com/saddamalsalfi/skills"
license: "MIT"
created_at: "2026-09-12"
---

# Laravel 13 Local Development Setup

## 1. Objective and Execution Boundary

Prepare the developer's local environment and deliver a working Laravel **13.x** project with the selected frontend, database, authentication features, team support, and AI coding tools.

When invoked to perform setup, carry out the authorized work through verification. When asked only to write or review these instructions, produce the requested document without installing software or creating an application.

Before executing commands, establish whether the available terminal belongs to the developer's machine, WSL distribution, container, remote host, or an unrelated sandbox. A successful installation in an agent sandbox does not establish that the developer's workstation is ready.

Inspect existing project instructions and preserve existing files, database records, credentials, and editor configuration. For an existing application, resume only missing setup steps. Do not recreate the application or upgrade its framework under this skill.

## 2. Intended Configuration

Use the following profile unless the developer explicitly overrides it. These are project preferences, not universal Laravel defaults.

| Setting | Requested choice |
| --- | --- |
| Framework | Latest stable compatible Laravel 13.x release |
| Starter kit | Yes |
| Frontend | Livewire preferred; explain available alternatives |
| Authentication provider | Laravel's built-in authentication |
| Livewire component format | Single-file components |
| Teams | Yes |
| Authentication features | Email verification, registration, two-factor authentication, passkeys, password confirmation, where supported |
| Boost features | Guidelines, skills, and MCP configuration |
| Third-party Boost resources | `livewire/blaze` skills, when available and applicable |
| Boost external integrations | None; do not select Laravel Cloud |
| Coding agent | GitHub Copilot |
| Frontend package manager | npm unless the developer chooses pnpm or Bun |
| Database | Ask if not already specified; do not infer SQLite from an example `.env` |
| New isolated MySQL/MariaDB instance | Local database account `root`, requested password `Admin@789` |
| Local test account | Name `admin`, email `admin@example.com`, password `password123` |

Ask only for unresolved information, typically the parent directory, English project name, database engine, and approval for missing software installations. Reuse choices and approvals already supplied in the active session.

Explain the frontend options before asking for a choice. If Livewire has already been selected, acknowledge it and proceed. Do not ask the developer to reconfirm every installer answer.

## 3. Requirements and Version Policy

Distinguish framework requirements from this project's stricter baseline and from requirements introduced by the selected starter kit.

| Component | Acceptance rule |
| --- | --- |
| Laravel | Installed `laravel/framework` must be stable 13.x |
| PHP | At least 8.3; also satisfy all selected Composer dependencies |
| Composer | Project baseline: at least 2.2.0; prefer a current stable compatible Composer 2 release |
| Node.js | A currently supported LTS release satisfying the actual frontend dependency engine constraints |
| npm | Project baseline: at least 9.x when npm is selected; also compatible with Node.js and the generated project |
| pnpm / Bun | Alternative selected package manager, verified against the project and its scripts |
| MySQL | Project baseline: at least 8.0 |
| MariaDB | Project baseline: at least 10.4 |
| PostgreSQL | Project baseline: at least 12.0 |
| SQLite | Project baseline: at least 3.35.0; raise it if required by application queries or dependencies |
| SQL Server | At least 2017, with a compatible PHP driver and ODBC runtime |
| Web server | Local development through the project's dev script, Artisan, or an existing local environment |

Only one selected database engine is required. SQLite does not require a standalone database server or a root account.

The database, Composer, and npm numbers above are the requested project baselines; do not present all of them as Laravel's official minimums. Laravel's documented general database support can be broader, while individual database features can require newer versions.

For new installations, select a vendor-supported stable release satisfying these baselines, not an obsolete release merely because it meets a numeric minimum. Verify current release support and dependency requirements at execution time.

Do not infer Node.js compatibility from `npm -v`. Check `node -v`, `package.json`, package-manager metadata, and Vite's actual engine requirements. Bun or pnpm selection does not automatically remove Node.js requirements from scripts or dependencies.

Nginx and Apache are production-server options, not prerequisites for this local workflow. Do not install or configure production hosting unless separately requested.

### PHP Extensions

Verify the Laravel 13 documented extension set:

```text
ctype, curl, dom, fileinfo, filter, hash, mbstring, openssl,
pcre, pdo, session, tokenizer, xml
```

Also verify:

- `bcmath`, required by this project's setup policy.
- JSON support, which is built into supported PHP versions; do not attempt to install an obsolete standalone JSON extension.
- The PDO driver for the selected database: `pdo_mysql`, `pdo_pgsql`, `pdo_sqlite`, or `pdo_sqlsrv`.
- Additional extensions required by Composer dependencies or development scripts.

A generic PDO extension alone is insufficient. Check CLI PHP and the serving PHP runtime when they differ. Do not make POSIX-only development extensions a universal requirement on native Windows; use a supported process alternative if necessary.

## 4. Discover Existing Tools Before Installing

### Initial Checks

Run the applicable commands separately and record each result, including a missing executable or nonzero exit status:

```text
php -v
composer --version
node -v
npm -v
laravel --version
mysql --version
```

The MySQL probe is relevant to MySQL-compatible environments. For a different selected database, inspect its appropriate client and connection instead. Missing `mysql` does not block a SQLite project.

Also inspect, as applicable:

```text
php --ini
php -m
composer diagnose
git --version
pnpm --version
bun --version
```

`laravel --version` identifies the global installer. It does not identify the framework version inside a project.

### Advanced Discovery When a Command Is Missing

A PATH lookup failure is not proof that software is absent.

1. Identify the operating system, shell, architecture, and execution context.
2. Inspect command resolution and alternate versions.
3. Query installed-package inventories and relevant version managers.
4. Inspect likely installation directories and the IDE terminal's environment.
5. Test discovered executables by their exact paths.
6. Classify the result as absent, outside PATH, incompatible, misconfigured, or not running.

Use platform-appropriate discovery:

| Environment | Useful discovery methods |
| --- | --- |
| Linux / macOS shells | `command -v`, `type -a`, package-manager inventory, version-manager status, known installation roots |
| Windows PowerShell | `Get-Command -All`, `where.exe`, installed-package inventory, service information, known tool directories |
| macOS managed stacks | Homebrew locations, Herd configuration, existing Valet setup |
| Windows managed stacks | Herd, Laragon, XAMPP, WAMP, Scoop, Chocolatey, WinGet installations |
| Node environments | nvm, fnm, Volta, asdf, or the version manager actually present |
| PHP environments | Existing PHP managers, Herd, system alternatives, and their active configuration files |
| WSL / containers | Inspect inside the selected runtime; do not mix host and guest executable assumptions |

Find Composer's global binary directory with:

```bash
composer global config bin-dir --absolute
```

For project text and file discovery, prefer `rg` and `rg --files`. Limit searches to plausible installation locations; do not scan unrelated personal directories or entire disks without a concrete reason.

Prefer using or selecting a compatible installed version over installing a duplicate. Record intended persistent PATH changes and avoid replacing unrelated entries. Verify the resulting PATH from a fresh terminal when needed.

## 5. Present and Approve Missing Installations

Before installing missing machine-level software, provide a concise plan containing:

- Tool and compatible target version.
- Why the existing installation cannot be used.
- Relevant installation options for the detected OS.
- Recommended source or package manager.
- Installation scope and required privileges.
- Any new service, port, or persistent PATH change.

Ask the developer to choose and approve the proposed installation if that approval has not already been given. The requirement to offer installation options applies to genuinely missing or unusable tools, not every read-only check.

Use official distributions or the developer's established trusted package manager. Once approved, install the selected tools, configure them, and rerun the relevant checks.

Do not silently replace an existing global runtime, database instance, authentication method, or root password. Do not disable certificate verification, use Composer's `--ignore-platform-reqs`, or force an unsupported dependency installation to bypass a failure.

If administrative access, downloads, or environment permissions block a step, report the exact unmet requirement and provide the smallest actionable next step. Continue independent authorized work where possible.

## 6. Database Provisioning

Select the engine before finalizing connection settings. Explain practical choices briefly: SQLite for minimal local infrastructure, MySQL/MariaDB for that server ecosystem, PostgreSQL for its features, and SQL Server when required by the target environment.

### New MySQL or MariaDB Instance

For a newly installed, isolated local instance, apply the requested development credentials:

```text
Username: root
Password: Admin@789
```

Keep the service local to the developer's machine. Do not enable unrestricted remote root access.

These values are explicit local-development defaults. Never apply them automatically to an existing database server, shared environment, or production system. If the installed distribution uses socket-based root authentication, explain the mismatch and obtain a concrete decision before changing that authentication method; a dedicated local application account is an alternative.

Pass credentials through the client's password prompt or another supported protected input mechanism. Do not place database passwords in shell command arguments or diagnostic output.

For example, after provisioning:

```bash
mysql --host=127.0.0.1 --port=3306 --user=root --password
```

Use the actual local port. Once connected, verify server identity and version, not just the client version, and create a dedicated project database if it does not exist.

For MySQL/MariaDB, an example inside the authenticated database client is:

```sql
SELECT VERSION();
CREATE DATABASE IF NOT EXISTS app_name
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
```

Replace `app_name` with a validated database identifier. Inspect an existing database before using it; `IF NOT EXISTS` does not prove that it belongs to this project.

### Other Engines

- PostgreSQL: use the selected local role and database; do not assume a role named `root` exists.
- SQL Server: use the configured login and instance; do not equate MySQL's root account with SQL Server authentication.
- SQLite: create the selected database file only if absent and verify directory permissions. Never truncate an existing file. Check the SQLite library used by PHP, since the standalone CLI can use a different version.

The database is ready only when the selected runtime can authenticate and access the intended project database.

## 7. Install or Update the Laravel Installer

After the PHP and Composer checks pass, install the latest stable compatible installer through its existing installation mechanism.

For a Composer-managed installer:

```bash
composer global require laravel/installer
```

This installs or updates the installer; it does not create a project. Respect the machine-level installation approval already obtained.

Avoid a second competing installation if Herd or another environment manager already owns the active installer. Use its supported update mechanism where appropriate.

Verify:

```bash
laravel --version
laravel new --help
```

Read the actual help and prompt behavior. Do not assume a transcript from an older release is still accurate.

## 8. Project Location, Name, and Laravel Major Version

Request the English project name and parent directory if they are not known. Prefer lowercase ASCII kebab-case, such as `inventory-app`.

Reject empty names, path separators, `..`, shell metacharacters, and platform-reserved filenames. Resolve the final absolute destination before executing commands.

Run project creation from the **parent directory**. Let the installer create the project directory; do not accidentally create `app-name/app-name`.

Inspect any existing destination. Never use `--force`, delete the directory, or overwrite a partial installation as routine recovery.

### Laravel 13 Guard

“Latest” means the latest stable compatible release **within Laravel 13.x**.

Before using the current starter kit, verify that its dependency constraints target Laravel 13. A future installer or starter-kit default may target a newer major.

Do not invent a `laravel new --version=13` option. The global version flag commonly reports the installer version instead of selecting the framework.

If current defaults no longer support Laravel 13, use an official documented compatible starter-kit release or installation path. Resolve the release before creating the final project. A version-constrained bare Laravel skeleton is only a fallback foundation; it does not satisfy the selected starter-kit requirements by itself.

Create the application using the actual supported interface:

```bash
laravel new app-name
```

Replace `app-name` with the validated project name. Add only flags confirmed by `laravel new --help`, including the selected database when supported. After creation, enter the generated directory and verify:

```bash
php artisan --version
composer show laravel/framework
composer check-platform-reqs
```

Stop dependent setup if the framework is not 13.x. Do not silently accept another major or blindly downgrade a completed scaffold.

## 9. Starter-Kit Selection and Prompt Handling

### Frontend Explanation

| Choice | Best fit | Practical characteristics |
| --- | --- | --- |
| React | Developers comfortable with React and TypeScript | Uses Inertia to connect React pages to Laravel routing and controllers; a separate REST API is not required for ordinary application pages. It is not a Next.js application. |
| Vue | Developers who prefer Vue's component model | Uses Inertia with Laravel; offers a reactive component workflow and a substantial Laravel ecosystem. |
| Livewire | Developers who prefer PHP and Blade | Supports interactive interfaces with most application logic in PHP. JavaScript tooling and browser-side JavaScript still exist; advanced interactions may use JavaScript or Alpine. |
| Svelte | Developers who prefer Svelte's compiled component model | Uses Inertia with Laravel and concise reactive components; actual bundle size and performance depend on the application. |

Use the developer's existing Livewire preference. Ask only if the choice remains unresolved or the developer wants to reconsider it.

### Intended Installer Answers

| Prompt or capability | Select |
| --- | --- |
| Use a starter kit | Yes |
| Frontend stack | Livewire |
| Authentication provider | Laravel built-in |
| Single-file Livewire components | Yes |
| Teams support | Yes |
| Authentication features | The requested supported feature set below |
| Database | The selected and provisioned engine |
| JavaScript package manager | npm, unless another manager was chosen |
| Testing framework, if asked | Explain available choices; retain an existing preference or use the compatible installer default |

**Single-file clarification:** Livewire 4 has native single-file components. Do not describe every single-file component as Volt or install Volt solely because this option is selected. Modern multi-file components and traditional class-based components are also distinct formats. Inspect the generated version and structure rather than asserting fixed legacy directories.

**Teams clarification:** This profile explicitly enables teams. Do not change the answer to “no” merely because a simple application might not need teams. Explain that teams add membership, invitations, ownership or permissions, and current-team context. Verify the generated implementation rather than assuming every starter-kit release models these identically.

### Interactive Execution Rules

Use a PTY when required. Read each prompt before answering. For multi-select prompts, inspect the selected entries and confirm the intended set; do not blindly stream Enter or positional keystrokes.

Treat “press Enter” as accepting a verified selection, not an instruction to accept any future defaults. Do not select `None` alongside actual features.

Installer and Composer scripts may run additional prompts, install frontend dependencies, or execute migrations. Track what already completed and avoid duplicate provisioning.

For unattended execution, use only documented flags or supported input mechanisms that express the resolved choices. If a required choice cannot be represented safely, use interactive execution or report the specific blocker.

## 10. Authentication Features and Local Behavior

Enable the following requested features when supported by the selected Laravel 13 starter-kit release:

| Feature | Required local outcome |
| --- | --- |
| Registration | Registration interface and backend validation are available |
| Email verification | Verification notification and verified-route behavior are configured |
| Two-factor authentication | Enrollment, confirmation, recovery, and challenge flows are available as implemented by the kit |
| Passkeys | The documented local authentication integration is installed and configured when supported |
| Password confirmation | Sensitive actions use the intended recent-password-confirmation flow |

Do not silently switch to WorkOS to obtain a missing feature. Use the built-in authentication path selected by the developer.

If passkeys or another requested feature is absent from the installed feature menu, inspect official version-compatible support. Complete the supported integration or explicitly report the feature as blocked; do not claim that pressing Enter installed it.

For local email, use the application's log mailer or an approved local mail catcher. Avoid sending real verification or invitation email during setup unless explicitly requested.

Passkey testing depends on a compatible browser/authenticator and a supported secure context. Keep the application origin, configured relying-party settings, and chosen hostname consistent. Configure local HTTPS where required; do not disable WebAuthn origin checks.

Enabling 2FA and passkeys does not mean a test account is already enrolled. Report enrollment-dependent browser checks separately.

## 11. Laravel Boost and Coding-Agent Integration

If the installer has not already installed Boost, run the documented compatible installation flow:

```bash
composer require laravel/boost --dev
php artisan boost:install
```

Use these selections when available:

| Boost prompt | Requested selection |
| --- | --- |
| Features | `guidelines`, `skills`, `mcp` |
| Third-party guidelines/skills | `livewire/blaze` skills |
| External integrations | None |
| AI agents | GitHub Copilot |

Verify whether `livewire/blaze` is already installed and whether its compatible skills are discoverable. Selecting guidance is not proof that the runtime package was installed. If absent, check compatibility before adding a dependency, and distinguish runtime installation from resource selection.

Agent menus evolve. Inspect available integrations rather than hardcoding the historical list of Amp, Antigravity, Claude Code, Codex, Cursor, Factory Droid, GitHub Copilot, Grok Build, Junie, Kiro, OpenCode, Pi, and Zed.

Configure only the requested agent. Preserve unrelated existing editor instructions and MCP servers. Verify the generated files, the configured command, its working directory, and PHP resolution from the editor environment.

If Copilot or its editor extension is not installed, treat that as a separate missing-tool choice. Do not purchase a subscription, sign in, or claim authentication on the developer's behalf.

Check that the configured MCP server can initialize when the editor is available. If editor reload or user trust is needed, report the exact remaining interaction. Do not mark the integration verified solely because configuration files exist.

Do not select Laravel Cloud, provision cloud resources, or deploy this local project.

## 12. Configure the Project Environment

Edit `<project-root>/.env` after confirming the final project and database paths.

If `.env` is absent, copy `.env.example` once. Preserve existing values unrelated to setup. Keep `.env` out of version control; do not copy real credentials into `.env.example`, agent guidelines, or the setup report.

Use local application settings:

```dotenv
APP_NAME="App Name"
APP_ENV=local
APP_DEBUG=true
APP_URL=http://localhost:8000
```

Use the actual application URL and keep it consistent for authentication and passkeys. Bind development services to loopback unless broader access is explicitly requested.

Generate `APP_KEY` only if it is absent:

```bash
php artisan key:generate
```

Do not regenerate an existing key during a rerun.

### MySQL Example

The following is for the newly provisioned local instance with the requested credentials:

```dotenv
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=app_name
DB_USERNAME=root
DB_PASSWORD="Admin@789"
```

Replace the port and database name with verified values. For MariaDB, use the connection name actually defined in the generated `config/database.php`.

### SQLite Example

```dotenv
DB_CONNECTION=sqlite
DB_DATABASE="/absolute/path/to/app-name/database/database.sqlite"
```

Use an absolute path valid inside the selected runtime. Host, port, username, and password entries should be removed or commented for SQLite.

### PostgreSQL and SQL Server

Use the generated `pgsql` or `sqlsrv` connection configuration with the real local host, port or instance, database, and approved credentials. Do not reuse MySQL values mechanically.

After editing:

```bash
php artisan config:clear
```

Inspect effective non-secret connection settings and check for overriding environment variables, `DB_URL`, or cached configuration. Verify the connection from Laravel itself before migrating. Do not print passwords or the full `.env` file.

## 13. Migrate the Selected Database

Confirm the connection targets the intended local project database. Then run:

```bash
php artisan migrate
php artisan migrate:status
```

`migrate` applies pending migrations. It does not recreate every table on each run.

If the installer already migrated SQLite but the final choice is MySQL or another engine, configure and migrate the selected destination. Do not assume the earlier migration created tables there.

Never use `migrate:fresh`, `migrate:refresh`, `db:wipe`, database drops, or destructive rollback as routine setup. A failure requires diagnosis of its actual cause.

Verify required user, authentication, team, invitation, session, cache, and queue tables according to the generated migrations and enabled drivers. Do not invent table names or add duplicate migrations.

## 14. Create the Local Test Account Correctly

Requested local account:

```text
Name: admin
Email: admin@example.com
Password: password123
```

Create it only after verifying `APP_ENV=local` and the local database identity. Reuse an existing account with this email without silently resetting its password, roles, verification status, or team memberships.

A user named `admin` is not automatically an administrator. Do not invent an `is_admin` column or grant permissions that the application does not define. If an actual administrative role is required, use the project's established authorization mechanism and report the assigned role precisely.

### Preferred Creation Path

Inspect the generated registration action, user model, and teams implementation first. Prefer the application's registration action so password validation, hashing, team creation, and associated invariants remain consistent.

For a starter kit with this supported action, enter Tinker:

```bash
php artisan tinker
```

Then adapt this example to the inspected action signature:

```php
if (! app()->environment('local')) {
    throw new RuntimeException('Local development only.');
}

$user = App\Models\User::where('email', 'admin@example.com')->first();

if ($user === null) {
    $user = app(App\Actions\Fortify\CreateNewUser::class)->create([
        'name' => 'admin',
        'email' => 'admin@example.com',
        'password' => 'password123',
        'password_confirmation' => 'password123',
    ]);
}

$user->only(['id', 'name', 'email']);
```

If the action requires additional fields, supply the documented local values. If the requested password fails the actual policy, explain the failure and request an acceptable replacement; do not weaken authentication validation.

Verify the account's team membership and current-team context. If the generated registration action does not provision them, use the kit's supported team-creation flow. Never assume a direct Eloquent insert triggers registration-only behavior.

The original minimal approach:

```php
App\Models\User::create([
    'name' => 'admin',
    'email' => 'admin@example.com',
    'password' => bcrypt('password123'),
]);
```

is illustrative only: it is not idempotent, does not grant administrator privileges, and can bypass team initialization or registration behavior. Do not use it as the default creation path for this teams-enabled profile.

For a project without a suitable registration action, implement a local-only, idempotent provisioning routine using its documented models and hashing facilities. Do not store a plaintext password in the database.

Exit Tinker explicitly:

```text
exit
```

Exercise email verification through the configured local mail channel. Do not silently mark the account verified or bypass 2FA. Keep account existence, email verification, and authenticator enrollment as separate reported states.

## 15. Frontend Dependencies and Local Processes

Inspect `package.json`, `composer.json`, the selected package manager, and existing lockfiles before running setup scripts. Some convenience scripts regenerate keys or force migrations; do not rerun them blindly.

For npm:

- Use `npm ci` when a valid lockfile already exists and reproducible installation is appropriate.
- Use `npm install` for initial dependency resolution when no valid lockfile exists.
- Preserve the chosen package manager and its lockfile; do not create conflicting lockfiles.

Build assets:

```bash
npm run build
```

Use the corresponding commands for pnpm or Bun if selected and supported. Do not globally weaken dependency constraints to suppress an installation failure.

Start local development with the generated script after inspecting what it launches:

```bash
composer run dev
```

If that script is unavailable or a bundled process is unsupported on the platform, use the necessary processes separately, for example:

```bash
php artisan serve --host=127.0.0.1 --port=8000
```

and, in another terminal:

```bash
npm run dev
```

Run a queue worker only when the configured asynchronous features require it. Use the actual queue driver and project script. Do not start duplicate servers or stop unrelated processes to free ports.

If a port is occupied, identify its owner and choose another available local port unless the developer explicitly asks to stop it. Update the application URL and authentication origin settings as needed.

Capture process/session identifiers where available and provide accurate restart and shutdown instructions. Do not claim a server remains running if the execution environment terminates it at the end of the session.

## 16. Verification and Completion Gate

Use observable results, not the absence of obvious errors.

| Area | Evidence required |
| --- | --- |
| Runtime | Correct executable paths, PHP version, extensions, and compatible frontend runtime |
| Framework | `php artisan --version` and installed package metadata show Laravel 13.x |
| Composer | `composer check-platform-reqs` succeeds with the actual PHP runtime |
| Database | Laravel connects to the intended local database; migrations are applied |
| Frontend | Dependency installation and asset build succeed |
| Application | Home or health route responds and the intended UI renders |
| Authentication | Login works; requested feature configuration and routes are present |
| Test account | Exactly the intended account exists; password is hashed; actual privileges are known |
| Teams | Membership and current-team navigation work for the test account |
| Boost | Requested resources are generated; Copilot configuration is present; MCP readiness is accurately reported |
| Tests | Relevant generated tests pass against an isolated test database |

Inspect test configuration before running tests. Never point destructive test fixtures at the developer's working database. Use the generated test runner and supported project scripts; do not change the testing framework just for this verification.

When browser access is available, verify login, team-aware navigation, an interactive Livewire action, and representative enabled authentication settings. Test emails through local delivery. Passkey or hardware-dependent checks may require developer participation; mark those checks as pending when not executed.

Run additional checks only to resolve an observed problem or an explicit project gate. Report failures and skipped checks truthfully.

## 17. Recovery and Idempotency

On reruns:

- Reuse compatible tools and the existing project.
- Preserve `.env`, application keys, lockfiles, database data, and editor configuration.
- Run pending migrations instead of resetting the schema.
- Reuse the local account without silent credential changes.
- Check for an existing personal team before creating one.
- Reuse running services where appropriate.
- Resume from the first incomplete step.

For failures, identify the category: PATH, version, extension, dependency resolution, permissions, network, database authentication, missing database, migration, asset compilation, port conflict, or editor integration.

Use a targeted repair. Do not delete lockfiles, clear unrelated caches, reset database credentials, or reinstall the entire toolchain without evidence that the action is necessary and authorized.

## 18. Final Handoff

Provide a concise setup report containing:

- Project name and absolute location.
- Installed Laravel, PHP, Composer, Node.js, and package-manager versions.
- Database engine, version, database name, and local connection endpoint, excluding secrets.
- Selected starter kit, component format, teams, and authentication features.
- Boost features and configured coding agent.
- Local application URL and process start/stop commands.
- Test-account email and actual role; reference the supplied local password without repeating it unnecessarily.
- Migration, build, test, and browser-check results.
- Any remaining developer action or blocked requirement.

Do not describe the environment as fully ready while required migrations, assets, account/team setup, or requested integrations remain broken. Distinguish installed, configured, verified, and pending states.

## 19. Official References and Maintenance

This skill's technical distinctions were reviewed on **2026-09-12**. Recheck the installed versions and current authoritative documentation during execution; this date does not pin package versions.

- [Laravel 13 installation](https://laravel.com/docs/13.x/installation)
- [Laravel 13 server requirements](https://laravel.com/docs/13.x/deployment#server-requirements)
- [Laravel 13 database support](https://laravel.com/docs/13.x/database)
- [Laravel 13 starter kits and teams](https://laravel.com/docs/13.x/starter-kits)
- [Laravel installer source and options](https://github.com/laravel/installer/blob/master/src/NewCommand.php)
- [Official Livewire starter-kit dependencies](https://github.com/laravel/livewire-starter-kit/blob/main/composer.json)
- [Livewire 4 component formats](https://livewire.laravel.com/docs/4.x/components)
- [Laravel Boost](https://laravel.com/docs/13.x/boost)
- [Livewire Blaze](https://github.com/livewire/blaze)
- [Node.js release support](https://nodejs.org/en/about/previous-releases)
- [Vite runtime requirements](https://vite.dev/guide/)

Treat official documentation and generated source as evidence for version-specific APIs. Preserve this skill's explicit local setup choices unless the developer changes them.
