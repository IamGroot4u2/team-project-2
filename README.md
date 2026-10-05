# Team Project — Secure Software Design & Development

**Course:** CYC 386 – Secure Software Design and Development  
**Assignment:** Lab Assignment #1 — Mastering Git and GitHub for Collaboration  
**Student:** Sadat Ali  
**Registration No:** FA23-BCT-034  
**Instructor:** Muhammad Ahmad Nawaz  

---

## 📖 Overview

This repository is the deliverable for **Lab Assignment #1**, which focuses on
practical mastery of **Git and GitHub** for collaborative software development.

The assignment simulates a real-world team workflow using **two GitHub accounts**:

| Role | GitHub Account | Purpose |
|------|----------------|---------|
| **Owner / Maintainer** | [@Sadatali9](https://github.com/Sadatali9) | Creates the repo, works on features, merges PRs, resolves conflicts |
| **Collaborator / Classmate** | [@ImGroot4u](https://github.com/ImGroot4u) | Forks the repo, reviews PRs, contributes via pull requests |

Using two accounts allowed a **complete end-to-end simulation** of:
- Forking an external repository
- Submitting pull requests across accounts
- Reviewing and approving code as a teammate
- Resolving merge conflicts

---

## 🎯 Assignment Objectives

By completing this assignment, the following Git/GitHub skills were practiced:

1. Creating and initializing a GitHub repository
2. Cloning a repository locally
3. Making commits and pushing to remote
4. Branching and feature-based development
5. Creating, reviewing, and merging Pull Requests
6. Forking a repository and contributing upstream
7. Using `git revert` to safely undo a commit
8. Using `git reset --hard` to discard local commits
9. Collaborating between multiple GitHub accounts
10. Resolving merge conflicts

---

## 🧭 Workflow Summary

```
Sadatali9:   Setup repo → branch → PR → merge → revert → reset
                          │
ImGroot4u:   ────────────→ fork → clone → add file → PR back
                          │
Both:        A adds B as collaborator
             A opens PR → B reviews → B approves → merge
             A creates merge conflict → resolves it
```

---

## 📚 Step-by-Step Process

### 🔹 Step 1 — Repository Setup (as `Sadatali9`)

Created a public repository `team-project-2` with:
- A `README.md` file
- A Python `.gitignore` file

**Commands used:**

```bash
gh auth switch --user Sadatali9
git config --global user.name "Sadat Ali"
git config --global user.email "sadatali9@gmail.com"

mkdir -p ~/ssdd-lab && cd ~/ssdd-lab
gh repo create team-project-2 --public --add-readme --gitignore Python --clone
cd team-project-2
```

Created `main.py` with an initial hash utility and committed it:

```bash
git add main.py
git commit -m "Added main.py with initial code"
git push origin main
```

**Repo URL:** https://github.com/Sadatali9/team-project-2

---

### 🔹 Step 2 — Branching + Pull Request (as `Sadatali9`)

Created a feature branch and added a **password strength checker**.

```bash
git checkout -b feature/new-feature
# ... edited main.py to add check_password_strength() ...
git add main.py
git commit -m "Added password strength checker feature"
git push -u origin feature/new-feature

gh pr create --fill --base main --head feature/new-feature
gh pr merge --merge --delete-branch
```

**Feature added:** `check_password_strength(password)` — validates length,
uppercase, lowercase, digits, and special characters.

---

### 🔹 Step 3 — Forking + Upstream PR (as `ImGroot4u`)

Switched to the second account to simulate a classmate contributing.

```bash
gh auth switch --user ImGroot4u
git config --global user.name "ImGroot"
git config --global user.email "imgroot4u@gmail.com"

cd ~/ssdd-lab
gh repo fork Sadatali9/team-project-2 --clone=false
gh repo clone ImGroot4u/team-project-2 forked-repo
cd forked-repo
```

Added `utils.py` with a **cryptographically secure token generator** using
Python's `secrets` module, then pushed and opened a PR back to the original repo:

```bash
git add utils.py
git commit -m "Added secure token generator utility"
git push origin main

gh pr create \
  --repo Sadatali9/team-project-2 \
  --title "Add secure token generator utility" \
  --body "Adds cryptographically secure token generator using Python secrets module." \
  --head ImGroot4u:main \
  --base main
```

**Feature added:** `generate_secure_token(length=32)` — uses `secrets.choice()`
over an alphabet of letters, digits, and symbols.

---

### 🔹 Step 4 — Revert vs Reset (as `Sadatali9`)

Demonstrated two different ways to undo commits.

#### 4.1 `git revert` — Safe Undo

Adds a **new commit** that reverses a previous one, preserving history.

```bash
echo "print('Buggy line')" >> main.py
git add main.py
git commit -m "Added buggy line"

git revert <buggy-hash> --no-edit
```

Result: two commits visible in history — the buggy one **and** the revert.

#### 4.2 `git reset --hard` — Destructive Undo

Discards commits entirely, rewriting history. **Only safe on local-only commits.**

```bash
echo "print('Temporary experiment')" >> main.py
git add main.py
git commit -m "Temporary experiment"

git reset --hard <revert-hash>
```

Result: the temporary commit is gone from history.

**Key difference:**

| | `git revert` | `git reset --hard` |
|---|---|---|
| History | Preserved | Rewritten |
| Safe on shared branches | ✅ Yes | ❌ No |
| Use when | Commit already pushed | Commit is local-only |

---

### 🔹 Step 5 — Collaboration & Merge Conflict

#### 5.1 Add Collaborator

```bash
gh auth switch --user Sadatali9
gh repo edit Sadatali9/team-project-2 --add-collaborator ImGroot4u

gh auth switch --user ImGroot4u
gh api user/repository_invitations
gh api -X PATCH user/repository_invitations/<id>
```

#### 5.2 Cross-Account PR Review

- **Sadatali9** created a branch `feature/input-validation` with a
  `validate_username()` function and opened a PR.
- **ImGroot4u** reviewed the PR, approved it, and merged it:

```bash
gh auth switch --user ImGroot4u
gh pr review <PR-number> --repo Sadatali9/team-project-2 --approve -b "LGTM! Code looks clean."
gh pr merge <PR-number> --repo Sadatali9/team-project-2 --merge --delete-branch
```

#### 5.3 Merge Conflict Resolution

Intentionally created a conflict by editing the **same line** in `main.py` on
two different branches (`feature/version` and `feature/logging`):

```bash
git checkout -b feature/version
# edit line 1 → # VERSION A
git commit -am "Version A"

git checkout main
git checkout -b feature/logging
# edit line 1 → # VERSION B
git commit -am "Version B"

git checkout main
git merge feature/version
git merge feature/logging   # ← CONFLICT
```

Resolved the conflict markers in VS Code, then:

```bash
git add main.py
git commit -m "Resolved merge conflict between version and logging"
git log --oneline --graph -5
```

---

## 🧠 Lessons Learned

### Technical

- **`gh` CLI is faster than the web UI** for creating repos, PRs, and merges.
- **Forking is fundamentally different from branching** — forks are separate
  copies used for external contributions, branches are within one repo for
  team collaboration.
- **`revert` preserves history; `reset` rewrites it.** Prefer `revert` on any
  branch that's already been pushed.
- **Merge conflicts are inevitable** and not scary — just pick the correct
  version, stage, and commit.

### Workflow

- Always run `gh auth switch --user <name>` **and** `git config user.email`
  before making commits when juggling accounts.
- Verify with `gh auth status` whenever a PR appears under the wrong account.
- Small, focused commits make history readable and reverts safe.

### Challenges Faced

1. **Wrong-author commits** — initially forgot to reset `git config user.email`
   after switching accounts. Fixed by adding the config change to the switch
   routine.
2. **PR opened under wrong account** — resolved by always running
   `gh auth status` before `gh pr create`.
3. **Collaborator invite** — the web UI was slow; used
   `gh api user/repository_invitations` to accept it via CLI instead.

---

## 📸 Screenshots

Screenshots of all major milestones (repo creation, branch push, PR creation,
merge, fork, revert, reset, collaboration, and conflict resolution) are included
in the submitted PDF deliverable for this assignment.

---

## 🛠️ Tech Stack

- **Language:** Python 3.11+
- **Version Control:** Git
- **Platform:** GitHub
- **CLI Tool:** `gh` (GitHub CLI)
- **Editor:** VS Code
- **Terminal:** Git Bash (MINGW64) / VS Code integrated terminal

---

## 📁 Repository Structure

```
team-project-2/
├── .gitignore          # Python ignores
├── README.md           # This file
├── main.py             # Core utilities (hash, password check, username validation)
└── utils.py            # Secure token generator (contributed via fork)
```

---

## 🔗 Related Links

- **Original Repository (Sadatali9):** https://github.com/Sadatali9/team-project-2
- **Forked Repository (ImGroot4u):** https://github.com/ImGroot4u/team-project-2

---

## ✅ Deliverables Checklist

- [x] Public GitHub repository with `README.md` and `.gitignore`
- [x] `main.py` with initial code committed and pushed
- [x] Feature branch + Pull Request + Merge
- [x] Forked repository with an upstream PR
- [x] Demonstration of `git revert` and `git reset --hard`
- [x] Collaboration between two GitHub accounts
- [x] Merge conflict created and resolved
- [x] Documentation (this README) + screenshots

---

## 📝 Conclusion

This assignment provided hands-on experience with the **complete Git/GitHub
collaboration workflow** — from initializing a repository to resolving merge
conflicts across two separate GitHub accounts. The skills practiced here
(branching, PRs, forking, revert/reset, conflict resolution) are directly
applicable to real-world team-based software development.

---

*Assignment submitted for CYC 386 – Secure Software Design and Development*  
*Fall 2023 – BS Cyber Security (FA23-BCT-034)*