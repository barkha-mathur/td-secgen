# td-secgen Architecture

Goal: Threat-Driven Security Test Generation for CI/CD pipelines.

## 1. High-Level Components

- **CLI (td-secgen)**  
  Entry point. Commands like:
  - `td-secgen init` – scaffold config in a repo
  - `td-secgen analyze-ci` – inspect CI/CD config
  - `td-secgen generate` – generate security tests from a threat model
  - `td-secgen report` – summarize findings / coverage

- **Project & CI Detector**
  - Detects repo layout (monorepo, services).
  - Detects CI provider (GitHub Actions, GitLab CI, etc.).
  - Normalizes CI config into an internal model: stages, jobs, secrets, artifacts.

- **Threat Model Engine**
  - Models pipeline assets: SCM, runners, artifact store, registries, deploy targets.
  - Uses structured threats (e.g., STRIDE + CI/CD-specific patterns).
  - Stores threats in a machine-readable format (YAML/JSON).

- **Test Generation Engine**
  - Maps threats → test templates.
  - Produces:
    - Pipeline checks (e.g., “fail if secrets are unencrypted”).
    - App/API security tests (DAST/SAST hooks).
    - Supply-chain checks (SBOM, SCA, signing, provenance).
  - Outputs ready-to-use files:
    - CI jobs
    - config snippets
    - security test scripts

- **Plugins / Integrations**
  - Provider-specific adapters:
    - `github-actions`
    - `gitlab-ci`
    - `jenkins`
  - Language-/stack-specific generators:
    - `python-web`, `node-api`, etc.

## 2. Data Model (First Draft)

- `tdsec.yaml` in repo root:
  - project metadata
  - CI provider + integration config
  - enabled threat profiles
  - enabled test suites

- Threat definitions:
  - `threats/*.yaml` – reusable threat patterns with:
    - asset
    - threat description
    - preconditions
    - recommended controls
    - test hooks (pointers into test templates)

- Test templates:
  - `tests/templates/*.j2` or similar:
    - CI job templates
    - scanner configs
    - custom security checks

## 3. Execution Flow (MVP)

1. `td-secgen init`
   - Detect CI/CD provider and create a baseline `tdsec.yaml`.
   - Optionally scaffold a basic threat profile and tests folder.

2. `td-secgen analyze-ci`
   - Parse CI config.
   - Identify obvious misconfigurations and missing controls.
   - Emit a preliminary threat list tied to pipeline stages.

3. `td-secgen generate`
   - Take threat list + profiles.
   - Generate concrete tests / CI jobs.
   - Write changes in a separate branch or folder (later: PR).

## 4. Future Directions

- Integrate LLM-based attack tree → test generation.
- Feedback loop from real pipeline runs (failed tests → refine threats).
- Mapping to MITRE ATT&CK for CI/CD-related techniques.

