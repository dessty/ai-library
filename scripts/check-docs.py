#!/usr/bin/env python3
"""Check the README contents table against files on disk.

Run from anywhere:

    python3 scripts/check-docs.py

The script exits 1 and prints one line per problem. It does not edit files.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
HEIMDALL = ROOT / "agents" / "heimdall" / "Heimdall.md"

LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
FENCE = re.compile(r"```[^\n]*\n(.*?)```", re.DOTALL)


def front_name(path):
    """Return the name: value from a leading --- block, or None."""
    text = path.read_text()
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    for line in text[3:end].splitlines():
        if line.startswith("name:"):
            return line.split(":", 1)[1].strip().strip("'\"")
    return None


def cells(row):
    parts = [part.strip() for part in row.strip().strip("|").split("|")]
    return parts


def is_dash_row(cols):
    return all(re.fullmatch(r"-+", col) for col in cols if col != "")


def contents_rows(text):
    """Rows of the first ## Contents table. Skips the header and the dash row."""
    start = text.find("## Contents")
    if start == -1:
        return None
    rest = text[start:]
    nxt = rest.find("\n## ", 1)
    block = rest if nxt == -1 else rest[:nxt]
    rows = []
    for line in block.splitlines():
        if not line.startswith("|"):
            continue
        cols = cells(line)
        if not cols or cols[0] == "Name":
            continue
        if is_dash_row(cols):
            continue
        if "colspan" in cols[0] or not LINK.search(cols[0]):
            continue
        rows.append(cols)
    return rows


def disk_items():
    """Skills, rules, and agents that the contents table must list."""
    skills = {}
    for skill_md in sorted((ROOT / "skills").glob("*/SKILL.md")):
        folder = skill_md.parent.name
        skills[folder] = {
            "path": skill_md.relative_to(ROOT).as_posix(),
            "declared": front_name(skill_md),
        }
    rules = {
        path.stem: path.relative_to(ROOT).as_posix()
        for path in sorted((ROOT / "rules").glob("*.md"))
    }
    agents = {}
    for path in sorted((ROOT / "agents").glob("*.yaml")):
        agents[path.stem] = {
            "path": path.relative_to(ROOT).as_posix(),
            "declared": front_name(path) or yaml_name(path),
        }
    return skills, rules, agents


def yaml_name(path):
    for line in path.read_text().splitlines():
        if line.startswith("name:"):
            return line.split(":", 1)[1].strip().strip("'\"")
    return None


def expected_path(kind, name):
    if kind == "Skill":
        return f"skills/{name}/SKILL.md"
    if kind == "Rule":
        return f"rules/{name}.md"
    if kind == "Agent":
        return f"agents/{name}.yaml"
    return None


def layout_agent_line(path):
    """The agents line inside the first fenced block, if any."""
    text = path.read_text()
    match = FENCE.search(text)
    if not match:
        return None
    for line in match.group(1).splitlines():
        if "agents" in line:
            return line.strip()
    return None


def main():
    problems = []
    text = README.read_text()
    rows = contents_rows(text)
    if rows is None:
        problems.append("README.md has no ## Contents section")
        rows = []

    skills, rules, agents = disk_items()
    seen = {"Skill": set(), "Rule": set(), "Agent": set()}

    for cols in rows:
        kind = cols[-1]
        match = LINK.search(cols[0])
        label = match.group(1).replace("`", "").strip()
        href = match.group(2).strip()
        seen.setdefault(kind, set()).add(label)

        if kind not in ("Skill", "Rule", "Agent"):
            problems.append(f"row {label}: kind {kind!r} is not Skill, Rule, or Agent")
            continue

        want = expected_path(kind, label)
        if href != want:
            problems.append(f"row {label}: link is {href}, expected {want}")
        target = ROOT / href
        if not target.is_file():
            problems.append(f"row {label}: link points nowhere: {href}")
            continue

        if kind == "Skill":
            info = skills.get(label)
            if info is None:
                problems.append(f"row {label}: no skills/{label}/SKILL.md on disk")
            elif info["declared"] != label:
                problems.append(
                    f"skill {label}: folder name and name: line disagree ({info['declared']})"
                )
        elif kind == "Rule" and label not in rules:
            problems.append(f"row {label}: no rules/{label}.md on disk")
        elif kind == "Agent":
            info = agents.get(label)
            if info is None:
                problems.append(f"row {label}: no agents/{label}.yaml on disk")
            elif info["declared"] not in (None, label):
                problems.append(
                    f"agent {label}: file name and name: line disagree ({info['declared']})"
                )

    for name in sorted(set(skills) - seen.get("Skill", set())):
        problems.append(f"skill {name} is on disk but missing from the contents table")
    for name, info in sorted(skills.items()):
        if info["declared"] != name and name not in seen.get("Skill", set()):
            problems.append(
                f"skill {name}: folder name and name: line disagree ({info['declared']})"
            )
    for name in sorted(set(rules) - seen.get("Rule", set())):
        problems.append(f"rule {name} is on disk but missing from the contents table")
    for name in sorted(set(agents) - seen.get("Agent", set())):
        problems.append(f"agent {name} is on disk but missing from the contents table")

    readme_agents = layout_agent_line(README)
    heimdall_agents = layout_agent_line(HEIMDALL)
    if readme_agents and heimdall_agents and readme_agents != heimdall_agents:
        problems.append(
            "layout: README.md agents line and agents/heimdall/Heimdall.md agents line differ"
        )
        problems.append(f"  README.md: {readme_agents}")
        problems.append(f"  Heimdall.md: {heimdall_agents}")

    if problems:
        print(f"{len(problems)} problem(s):", file=sys.stderr)
        for problem in problems:
            print(problem, file=sys.stderr)
        return 1
    print("contents table matches skills, rules, and agents")
    return 0


if __name__ == "__main__":
    sys.exit(main())
