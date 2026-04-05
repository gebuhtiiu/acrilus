# Identity Segmentation Guide

## Purpose

Identity segmentation reduces risk by separating digital activities into distinct identity domains instead of reusing a single email/account context everywhere.

## Why it matters

When too many systems depend on one address or identity, compromise, spam, or lockout can cascade widely.

## Segmentation logic

Possible identity domains include:
- critical / owner identity
- finance
- government and civic
- productivity and app integrations
- shopping and commerce
- public-facing / startup / project identity
- low-trust signup identity

## Design questions

For each identity domain, define:
- what kinds of services belong there
- what level of data sensitivity exists
- whether third-party app access should be allowed
- what backup and recovery methods protect it

## Principle

Segmentation is not about complexity for its own sake. It is about containing blast radius and making account routing intentional.
