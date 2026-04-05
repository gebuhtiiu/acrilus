# Acrilus Personal Digital Security Architecture

## Purpose

Modern digital life is usually managed as disconnected pieces: passwords in one place, files in another, recovery methods improvised, and high-risk accounts mixed with low-risk ones. This creates fragility.

The Acrilus Personal Digital Security Architecture provides a structured framework for designing a resilient personal digital environment. It integrates identity architecture, credential strategy, account segmentation, device security, backups, and recovery planning.

## Core principle

A digital life should be designed like a system, not accumulated like a pile.

## Architecture domains

1. Identity Architecture
2. Credential Architecture
3. Account Segmentation
4. Device Security
5. Backup and Recovery
6. Governance and Maintenance

## 1. Identity Architecture

Identity architecture defines how online identities are separated and what each is used for.

Recommended domains may include:
- primary personal identity
- financial identity
- government identity
- public-facing identity
- shopping identity
- productivity / app-integration identity
- low-trust or disposable identity

Benefits:
- reduced cross-service exposure
- clearer communications routing
- lower blast radius during compromise

## 2. Credential Architecture

Credential architecture defines how passwords, passkeys, 2FA, backup codes, and recovery methods are handled.

### High-risk accounts
Use the strongest available stack:
- unique random password
- password manager
- strong MFA
- recovery methods documented and protected

### Moderate-risk accounts
May use structured deterministic systems if they are private, unique, and not reused for top-tier accounts.

## 3. Account Segmentation

Accounts should be categorized by sensitivity and impact.

### Tier 1 — Critical
Examples: primary email, banking, password manager, cloud-storage owner account, phone carrier

### Tier 2 — Sensitive
Examples: medical portals, tax platforms, insurance, work systems

### Tier 3 — Standard
Examples: shopping, subscriptions, community services

### Tier 4 — Disposable
Examples: one-time signups and low-trust services

## 4. Device Security

Each device should have a role and baseline controls.

Recommended controls:
- full-disk encryption
- strong screen lock
- automatic updates
- secure backup configuration
- remote wipe where possible
- browser/profile separation where useful

## 5. Backup and Recovery

Security without recoverability is incomplete.

For each critical account, define:
- primary login identifier
- password storage method
- second factor
- recovery email
- recovery phone
- backup code location
- fallback recovery path

## 6. Governance and Maintenance

### Monthly
- review alerts
- verify backup code capture for new critical accounts
- review suspicious logins

### Quarterly
- test recovery paths
- review 2FA on critical accounts
- audit old accounts and stale permissions

### Yearly
- full critical-account review
- backup restoration drill
- segmentation review

## Publication boundary

Publish the architecture and worksheets, but never publish live secrets, exact account-routing details, or examples that mirror real credentials.
