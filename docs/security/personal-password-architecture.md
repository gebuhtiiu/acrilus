# Personal Password Architecture

## Purpose

A personal password system should allow a user to generate distinct passwords for different services while relying on a repeatable private method rather than memorizing every password directly.

## Safe publication boundary

This guide teaches how to design a method without revealing any individual’s live secrets.

## Core elements

1. private base component
2. domain-derived variation
3. category modifier
4. formatting rules
5. numbers and special-character rules

## Key principles

### Consistency
The rules should be applied in the same order every time.

### Domain-derived variation
Each site should receive a distinct output based on the service/domain.

### Private secret layer
Not all entropy should come from the domain. A private base component materially strengthens the system.

### Category modifiers
Different account categories should not all follow the exact same observable structure.

### Repeat handling
The system should define how repeated domain letters or repeated transformation outputs are handled.

## Stronger design improvements

- include a secret layer not derived from the domain
- use more than one domain transformation rule
- use category modifiers for different account classes
- reserve password-manager-generated random passwords for critical accounts

## Important note

Acrilus should publish design principles and exercises, not any real-world implementation that could be used to infer live credentials.
