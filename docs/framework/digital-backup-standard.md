# Digital Backup Standard

## Purpose

Organization without resilience is incomplete. Backup planning protects against deletion, corruption, hardware failure, and service disruption.

## Core principle

Acrilus recommends the **3-2-1 rule**:

- 3 copies of important data
- 2 storage media or storage contexts
- 1 offsite copy

## Example architecture

| Layer | Example |
|---|---|
| Primary | Google Drive or primary working storage |
| Local backup | External SSD or hard drive |
| Offsite backup | Encrypted cloud backup or separate cloud storage |

## Backup verification

Backups should be tested, not merely assumed. Periodically restore a subset of files and confirm integrity.

## Frequency guidance

- critical records: daily or weekly
- general documents: weekly or monthly
- archives: periodic integrity checks and snapshot retention
