# Folder Structure Standard

## Purpose

The Folder Structure Standard defines how digital storage should be organized so that files remain easy to locate and maintain over long periods.

The Acrilus model uses **category-first organization** with lifecycle folders where needed.

## Recommended top-level categories

- Admin
- Financial
- Health
- Home
- Learning
- Projects
- Reference
- Shopping
- Social
- Travel
- Vehicles

## Lifecycle pattern

When a category benefits from lifecycle separation, use:

`Inbox → Current → Reference → Archive`

### Inbox
Temporary holding area for newly captured material.

### Current
Active items still in day-to-day use or requiring action.

### Reference
Inactive but still useful materials that may need future retrieval.

### Archive
Historical records retained primarily for recordkeeping.

## Design rules

- Avoid mixing unrelated file domains at the top level.
- Use predictable subtrees inside each category.
- Keep permanent structure stable; move files through lifecycle folders instead of reinventing placement.
- Use project-specific folders only where a project genuinely benefits from them.

## Example pattern

```text
Financial/
  Inbox/
  Current/
    Banking/
    Credit Cards/
    Taxes/
  Reference/
    Statements/
    Insurance/
  Archive/
```

## Practical note

Not every category needs every lifecycle folder at every depth. Apply the model where it clarifies retrieval rather than mechanically duplicating empty folders.
