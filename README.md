# TIP 103 Problem Sets

A curated collection of problem sets for TIP 103, organized by week and session. Problems are regularly updated as the course progresses.

## Branches

- **`main`** - Contains problem statements only. Updated as new weeks are added.
- **`solutions`** - Your personal branch for working through solutions. Periodically merges from `main` to pick up new problems.

## Structure

- [problems/](./problems) - Problem sets organized by week and session
  - `week1/`, `week2/`, ... - One folder per week
  - Each week contains two sessions, each with around 6-8 problems
- [starters/](./starters) - Boilerplate files to copy when starting a new week

## Workflow

### Getting new problems

When new weeks are added to `main`, pull them into your solutions branch:

```bash
git checkout solutions
git merge main
```

### Starting a new week

Copy the starter folder and rename it for the current week:

```bash
cp -r starters/weekX problems/weekN  # replace N with the week number
```

Then fill in your solutions in the copied folder.

### Staying in sync

Your solutions stay on the `solutions` branch and are never overwritten by merges from `main`, since `main` only adds new problem files.

## Organization

- Each week has two sessions
- Each session has two problem sets
- Each problem set has around 6-8 problems
