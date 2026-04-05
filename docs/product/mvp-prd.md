# Acrilus Personal Information Management System
## MVP Product Requirements Document

## Overview

The Acrilus MVP introduces a structured metadata layer on top of existing file storage systems. Instead of replacing storage platforms, Acrilus indexes files and enables search, tagging, lifecycle tracking, and structured retrieval.

## Problem statement

Traditional folder systems degrade as collections grow. Users struggle with scattered storage locations, inconsistent names, duplicates, and weak retrieval.

## Goals

- enable structured classification of files
- enable fast retrieval via metadata queries
- track lifecycle states
- remain usable with thousands of records

## Non-goals for MVP

- OCR-heavy ingestion
- AI classification
- mobile apps
- collaboration features
- custom storage hosting

## Core features

### 1. File metadata management
Supported fields:
- category
- document type
- entity
- document date
- lifecycle state
- tags
- notes

### 2. File indexing
Store file path, file name, extension, timestamps, and metadata fields.

### 3. Search and retrieval
Support filters by filename, category, entity, type, lifecycle, tags, and date range.

### 4. Lifecycle management
States:
- Inbox
- Current
- Reference
- Archive

### 5. Tagging
Flexible tags such as `utilities`, `medical`, `vehicle`, `tax`.

## User workflows
- ingest file
- process file
- search and retrieve
- maintain system

## Example stack
- frontend: React
- backend: Python FastAPI
- database: PostgreSQL or SQLite
- storage: existing file locations

## Success criteria
- users can classify files quickly
- users can retrieve important documents quickly
- the system remains clear and usable at scale
