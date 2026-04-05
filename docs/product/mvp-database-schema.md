# MVP Database Schema

## Recommended core tables

### Files
- id
- file_path
- file_name
- file_extension
- file_size
- checksum
- created_at
- modified_at
- ingested_at
- processed_at
- document_date
- original_file_name
- notes
- category_id
- document_type_id
- entity_id
- lifecycle_state_id
- status_id

### Categories
Examples: Admin, Financial, Health, Home, Learning, Projects, Reference, Shopping, Social, Travel, Vehicles

### Document Types
Examples: Invoice, Receipt, Statement, Contract, Manual, Report, Policy, Medical Record

### Entities
Examples: Comcast, Quest Diagnostics, Honda, State Farm

### Lifecycle States
- Inbox
- Current
- Reference
- Archive

### Tags
Flexible cross-cutting labels.

### File Tags
Join table between files and tags.

## Optional later tables
- storage_locations
- backup_statuses
- retention_rules
- audits
