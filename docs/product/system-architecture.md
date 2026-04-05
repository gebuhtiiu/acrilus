# System Architecture

## Conceptual layers

### User Interface
Browse, search, tag, edit metadata, and review lifecycle state.

### Application Layer
Handles metadata operations, lifecycle changes, and query logic.

### Metadata Database
Stores structured relationships and search fields.

### Storage Layer
Files remain in user-owned storage systems such as local folders or cloud drives.

### Backup / Resilience Layer
Tracks whether key files have backup coverage and whether recovery paths exist.

## Design principle

Acrilus should improve organization and retrieval without requiring full storage lock-in.
