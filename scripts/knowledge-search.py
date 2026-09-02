#!/usr/bin/env python3
"""
knowledge-search.py — Search PRODUCT-KNOWLEDGE.md for patterns, anti-patterns
Part of bright improvement #3 + Anti-Repeat Score
Usage:
  python scripts/knowledge-search.py "tabs"
  python scripts/knowledge-search.py "patch1.md" --anti
  python scripts/knowledge-search.py --score
"""
import pathlib, sys, re, json

root = pathlib.Path(".").resolve()
pk_path = root / "PRODUCT-KNOWLEDGE.md"
if not pk_path.exists():
    pk_path = root / "agent-repo-template/PRODUCT-KNOWLEDGE.md"
if not pk_path.exists():
    print("PRODUCT-KNOWLEDGE.md not found")
    sys.exit(1)

text = pk_path.read_text(encoding="utf-8", errors="ignore")

def search(query):
    lines = text.splitlines()
    hits = []
    for i, line in enumerate(lines):
        if query.lower() in line.lower():
            # Get context
            context = "\n".join(lines[max(0,i-1):i+2])
            hits.append({"line": i+1, "content": line.strip(), "context": context})
    return hits

def anti_repeat_score():
    # Count how many times anti-patterns section exists and how many rows
    anti_section = re.findall(r"## 2\. Anti-Patterns.*?(?=##|$)", text, re.DOTALL)
    validated = re.findall(r"## 1\. Validated Patterns.*?(?=##|$)", text, re.DOTALL)
    anti_count = 0
    if anti_section:
        anti_count = anti_section[0].count("|") // 5  # rough rows
    validated_count = 0
    if validated:
        validated_count = validated[0].count("|") // 5
    # Count blocked attempts from census reports?
    blocked = 0
    for census_file in (root / ".agent/census").glob("*.json") if (root / ".agent/census").exists() else []:
        try:
            data = json.loads(census_file.read_text())
            if data.get("status") == "FAIL":
                blocked += 1
        except: pass
    return {"validated_patterns": validated_count, "anti_patterns": anti_count, "census_fails_blocked": blocked, "knowledge_score": validated_count*10 + anti_count*20 - blocked*5}

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("query", nargs="?", default="", help="Search query")
    parser.add_argument("--anti", action="store_true", help="Search only Anti-Patterns")
    parser.add_argument("--score", action="store_true", help="Show anti-repeat score")
    args = parser.parse_args()

    if args.score:
        score = anti_repeat_score()
        print(json.dumps(score, indent=2))
        print(f"\nKnowledge Score: {score['knowledge_score']} (higher = more knowledge prevents repeat errors)")
        print(f"Validated: {score['validated_patterns']}, Anti-Patterns: {score['anti_patterns']}, Blocked fails: {score['census_fails_blocked']}")
    elif args.query:
        hits = search(args.query)
        if args.anti:
            hits = [h for h in hits if "Anti-Pattern" in h["context"] or "DONT" in h["context"] or "Dead End" in h["context"]]
        if not hits:
            print(f"No hits for '{args.query}' — safe to proceed (not in Anti-Patterns)")
        else:
            print(f"Found {len(hits)} hits for '{args.query}':")
            for h in hits[:10]:
                print(f" Line {h['line']}: {h['content']}")
            if any("Anti-Pattern" in h["context"] or "DONT" in h["context"] for h in hits):
                print(f"\n⚠️  WARNING: '{args.query}' is in Anti-Patterns — DO NOT REPEAT. Check PRODUCT-KNOWLEDGE.md")
    else:
        print("Usage: python scripts/knowledge-search.py <query> [--anti] [--score]")
