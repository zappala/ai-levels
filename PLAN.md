# Plan: CS 191 Nov 6 Class Website ("Using AI in the CS Major")

The goal is one static website that students open at the start of class and keep open for the whole period. It holds everything they need: the talk, the AI levels guide, the prompts for each level, and the code to download. Class is Thursday, Nov 6, 2026, so the site should be live by the end of Nov 5 and posted on Canvas.

We'll go through these steps in order and check each one off as we finish it.

**Decisions so far (Nov 4):**
- **Hosting:** GitHub Pages.
- **Fallback:** pair with a cohort member, plus a Colab notebook for Levels 2 and 3.
- **Scope:** one-off for Nov 6; dates and links are hard-coded.
- **Process:** design each level together, one at a time, before building the site.
- **No message limit:** students have ChatGPT accounts and can buy a Claude plan if needed. Any level can use Claude or ChatGPT/Codex.
- **Level 4 reframed:** instead of a password-strength function (contrary to current NIST guidance) with a held-back test, students plan a deliberately vague problem (a bill splitter) with AI before it writes the code, and a change request replaces the held-back test.

---

## Step 1 — Gather inputs (you)

These are things only you have:

- [x] URL for Elder Gong's talk, "An Ear to Wisdom, a Heart to Understanding": https://speeches.byu.edu/talks/gerrit-w-gong/an-ear-to-wisdom-a-heart-to-understanding/
- [x] URL for the AI levels guide: https://claude.ai/public/artifacts/b1e35a55-f03f-4120-ba4f-b83a1ee3fc83
- [x] Slido: not used. For AI levels questions, each cohort agrees on one question and you take a few. For the wrap-up reflection, use a show of hands or cohort report-outs.
- [x] Help channel: none. The help order is cohort first, then raise a hand.
- [x] GitHub repo: `git@github.com:zappala/ai-levels.git` (Pages URL: https://zappala.github.io/ai-levels/)
- [x] Elder Gong section: below the talk link, the site lists (1) discuss the response you turned in on Canvas with your cohort, and (2) group discussion moderated by the instructor.
- [x] Fallback Python environment for students without Python and pytest set up (see Step 4)

## Step 2 — Decide on site structure

Proposed layout. It's a single page with anchor sections, so students never get lost, and it's mobile-friendly for students on laptops or phones.

```
index.html
  1. Today at a glance      (agenda table, 50 min)
  2. Elder Gong talk        (link + discussion prompts, optional)
  3. AI levels guide        (link + the main rule: "never submit anything you can't explain")
  4. The activity           (how levels are assigned in a cohort, timing, which AI tools, help order)
  5. Level 1 — Learn a topic      (topic list + 3 prompts, each with a copy button)
  6. Level 2 — Find the bug       (download, run steps, prompt, rules)
  7. Level 3 — Build with a guide (download, run steps, prompt, rules)
  8. Level 4 — You plan, AI builds (vague problem statement, prompts, no files)
  9. Compare and reflect    (cohort comparison questions; the wrap-up question is on the slides only)
 10. Wrap-up              (header only; wrap-up content is on the slides)
code/
  level2/leap_year.py, test_leap_year.py, test_leap_year_bonus.py
  level3/caesar.py, test_caesar.py, test_caesar_bonus.py
  level2.zip, level3.zip
colab/
  level2.ipynb, level3.ipynb
style.css
site.js        (copy buttons on prompts and commands; fills in code listings from code/)
build.py       (builds the zips and Colab notebooks from code/; rerun after any code change)
```

Decisions:
- [x] One page with anchor sections.
- [x] Code shown inline (in a collapsed "Show the code" section, loaded from `code/`) as well as offered as a zip.
- [x] AI tool instructions: the default path assumes an AI agent in the editor (Codex extension or Claude Code), with a smaller "Using a browser chat instead?" option under each step.
  - Levels 2 and 3: switch to a read-only mode (Codex **Chat** mode; Claude Code **plan mode**), and the prompt says "Don't edit any files." If the AI edits anyway, undo it.
  - Level 4: plan in read-only mode and save the plan as `plan.md`, then switch to an editing mode (Codex **Agent**; leave plan mode in Claude Code) and have the AI read `plan.md` and build it.

## Step 3 — Design each level together, then build it

For each level, one at a time:
1. Agree on the learning goal: what should students be able to explain afterward?
2. Draft the task, prompt(s), and rules, and review them together.
3. For Levels 2 and 3, write the code and tests, then run pytest to confirm the behavior we want.
4. Revise, then move to the next level.

- [x] **Level 1: learn a CS topic (AI as tutor).** Design settled Nov 4:
  - **Goal:** feel the difference between "that made sense" and "I can explain it."
  - **Setup:** students work individually, each in their own chat (Claude or ChatGPT).
  - **Topics** (the site shows the topic name with the question underneath; students paste the question into prompt 1):
    - Public-key cryptography: How can two people who've never met agree on a secret when everyone can see their messages?
    - How LLMs work: How does ChatGPT decide what word comes next, and why does it sometimes make things up?
    - Dark patterns: How do apps and websites use design to get me to do things I didn't intend to do?
    - Shortest-path algorithms: How does a maps app find the fastest route without checking every possible path?
    - Version control: How do teams of programmers work on the same code at the same time without overwriting each other's work?
    - DNS: When I type a web address, how does my computer find the right server among millions?
    - P vs NP: Why are some problems easy to check but seemingly impossible to solve quickly, and why does it matter?
    - Your own: pick a topic from a class you're taking and write it as a question you can't answer yet.
  - **Steps:**
    1. *"I'm a first-year CS student. Help me understand: [question]. Use an everyday example and keep it under 250 words. Don't quiz me yet."*
    2. (No AI.) Scroll the answer off screen and write your own explanation in 3–5 sentences, without looking.
    3. *"Here's my explanation in my own words: … What did I get wrong or leave out? Don't rewrite it for me."*
    4. *"Quiz me with 5 questions that check understanding, not memorization. Ask one at a time, wait for my answer, and tell me what I missed before asking the next."*
  - **Cohort comparison:** explain your topic in 30 seconds without notes, then discuss what worked well, what didn't, and how you'd use this in your own learning.
- [x] **Level 2: find the bug (AI points at it, you fix it).** Design settled Nov 4:
  - **Goal:** read pytest output, use AI to locate a bug rather than fix it, then fix it yourself and confirm with the tests.
  - **`is_leap_year(year)`:** the bug is `return year % 4 == 0` (forgets the century rule). The docstring states the interface only ("Return True if `year` is a leap year in the Gregorian calendar"), not the rule.
    - Tests: 2024 and 2023 pass, 1900 and 2100 fail, and 2000 passes by luck.
    - The common quick fix (`and year % 100 != 0`) breaks 2000, so students have to learn the full rule.
    - Correct solution: `return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)`.
  - **Optional bonus, `count_leap_years(start, end)`:** an off-by-one bug where `range(start, end)` excludes `end`. The docstring says "inclusive."
    - Tests: (2000, 2024) → 7 and (2020, 2020) → 1 fail; (2001, 2003) → 0 and (2021, 2023) → 0 pass.
    - Tests live in a separate `test_leap_year_bonus.py`.
  - **Files:** `leap_year.py` (both functions), `test_leap_year.py`, `test_leap_year_bonus.py`.
  - **Steps:**
    1. Run `pytest test_leap_year.py`.
    2. Paste the function and the failing output into the AI: *"Point me at the bug in this function and explain why these tests fail. Don't rewrite the code or show me a fix."*
    3. Fix it yourself and rerun pytest. If a new test fails, figure out why before asking again.
    4. If the AI rewrites the code, close the chat and fix it on your own.
    5. Bonus: `pytest test_leap_year_bonus.py`.
  - **Codex:** chat only, or tell it "Don't edit my files."
  - **No setup tutorial needed:** students have written Python and used pytest, so the site just lists the commands.
  - **Cohort comparison:** what did the AI point you at, what was your fix, and did a new test break along the way?
- [x] **Level 3: build it with AI as a guide (the Build Day level).** Design settled Nov 4:
  - **Goal:** write a working function yourself, with AI explaining each decision, and be able to explain every line.
  - **`caesar_encrypt(text, shift)`:** a stub whose docstring gives the spec. Shift each letter by `shift`, wrapping from z back to a; preserve case; leave non-letters unchanged. The body is `pass`.
    - Tests: basic shift (`"abc"`, 1 → `"bcd"`), wraparound (`"xyz"`, 3 → `"abc"`), mixed case, punctuation and spaces unchanged, a negative shift, and a shift greater than 26.
  - **Optional bonus, `crack_caesar(ciphertext, crib)`:** return the shift that was used to encrypt `ciphertext`, given a word (`crib`) known to be in the message; return `None` if no shift works. This ties to the CS Passport CTF Caesar challenge.
    - Tests: for example, `crack_caesar(caesar_encrypt("meet at noon", 5), "noon") == 5`, a case with shift 0, and a `None` case.
    - Tests live in a separate `test_caesar_bonus.py`.
  - **Files:** `caesar.py` (both stubs), `test_caesar.py`, `test_caesar_bonus.py`.
  - **Prompt:** *"I need to implement this function. First suggest an approach in plain words. Then walk me through it one step at a time. Don't write the whole function. Give me one piece, explain why, and wait for me to write it and show you before moving on."*
  - **Rules:** type every line yourself. If the AI gives you the full function, don't copy it; ask it to go back to one step at a time.
  - **Codex:** chat only, or tell it "Don't edit my files."
  - **Cohort comparison (explain check):** explain your function line by line to a cohort member, who asks whatever questions they want about the code. There's no fixed question list.
- [x] **Level 4: you plan it, AI builds it.** Design settled Nov 4:
  - **Why the change:** a password-strength function teaches composition rules that NIST SP 800-63B now advises against. AI is also already good at testing; the more valuable skill is planning and designing an underspecified problem before coding, which is also what students will do on Build Day.
  - **Goal:** turn a vague problem into a clear plan with AI as a design partner, then check that the code AI writes does what *you* decided.
  - **Problem statement (deliberately vague):** *"Write a program that splits a restaurant bill among friends."*
    - Ambiguities students should discover: even split or by what each person ordered; tax and tip; shared appetizers; rounding (who pays the leftover penny when $10 is split 3 ways).
  - **No starter files.** Students run the tests the AI writes.
  - **Steps:**
    1. Read the problem statement.
    2. Plan with the AI, no code yet: *"Before writing any code, ask me questions about what this program should do. Ask one at a time. Point out ambiguities and edge cases I haven't thought about."*
    3. Write a short plan yourself: inputs, outputs, the decisions you made, edge cases, and the functions the program needs.
    4. *"Here's my plan: … Critique the design. Then write the code and pytest tests that follow it."*
    5. Run it, try it, and check that it behaves the way your plan says, not just that the tests pass.
  - **Codex:** fine for Codex to write the files; you still run and check everything.
  - **Change request (after work time, replaces the held-back test):** *"One friend is covering someone else's meal."* Students judge how hard it would be to add to their design. Announce it on a slide only, so nobody designs for it in advance.
  - **Cohort comparison:** everyone at Level 4 started from the same sentence. Compare plans: what questions came up, what each person decided, how different the programs are, and how well each design handles the change request.
- [ ] Do a full run-through: unzip Levels 2 and 3 fresh, follow only the on-site instructions, and confirm everything works on Python 3.10+ with a plain `pip install pytest`. Run the Level 4 prompts through Claude and ChatGPT once to check that 15 minutes is enough.

## Step 4 — Fallback for students without Python

Options to choose from:
- **Pair with a cohort member** (zero setup; already in the class plan).
- **Browser environment with pytest** that needs no install, such as GitHub Codespaces, Replit, or a Google Colab notebook running `!pytest`. Colab is free with a Google account and can run pytest, so we could ship one notebook per level.
- **In-page Python (Pyodide)** that runs the tests directly on the website. It needs no accounts, but it's more work to build and test.

- [x] **Decided:** pairing as the default, plus one Colab notebook each for Levels 2 and 3 as the backup. (Level 4 has no starter files; students without Python can run the AI's code in a blank Colab notebook.)

## Step 5 — Build the site

- [x] Plain HTML + CSS + a small JS file, so anyone (including the TA) can edit it.
- [x] Copy buttons on every prompt and command so students spend their time learning, not retyping.
- [x] Readable on a projector as well as on laptops (large type, high contrast, dark mode).
- [x] Zips and Colab notebooks built from `code/` by `build.py`, so they never drift from the source.
- [x] Verified Nov 4: Level 2 and 3 tests behave as designed (shipped, naive-fix, and correct versions); the notebooks run end to end; all local and external links load.

## Step 6 — Level 4 change request

- [x] **Decided:** the held-back test is replaced by the change request ("One friend is covering someone else's meal"). It goes on a slide only, so it doesn't appear on the site before work time.

## Step 7 — Host and publish

See "Hosting options" below. Then:
- [ ] Deploy and test the public URL in a private window, on a phone, and on a non-BYU network.
- [ ] Post the URL on Canvas (announcement + module item) and put it on the first slide, with a short URL or QR code.

## Step 8 — TA dry run (by Nov 5)

- [ ] TA does each level once using only the website, with a timer running. Each level should fit in 15 minutes.
- [ ] Fix anything confusing.

## Step 9 — After class

- [ ] Add the Level 4 change request and a short "what we learned" note.
- [ ] Decide whether to keep the site up as a reference for future semesters.

---

## Hosting options (to discuss)

| Option | Cost | Effort | Pros | Cons |
|---|---|---|---|---|
| **GitHub Pages** | Free | Low: push the repo, turn on Pages | Simple; version history; TA can edit via PR; easy to update during class; reusable next semester | Public URL (fine for this content); needs a GitHub account/org |
| **Netlify / Cloudflare Pages** | Free tier | Very low: drag-and-drop a folder, or connect a repo | Fastest first deploy; preview URLs | Another account to manage; drag-and-drop loses version history |
| **BYU / CS dept web space** | Free | Depends on dept setup | Official byu.edu URL; stays within university systems | Possible access/upload friction; slower to change mid-class |
| **Canvas pages + Files** | Free | Medium | Students already live there; can restrict to the class | Clunky for code blocks, copy buttons, and zips; harder to style; not reusable outside the course |
| **Claude artifact** | Included | Very low | Quick to publish and iterate | Starts private; you'd have to share it; less control over URL/longevity |

**Decided:** GitHub Pages. We'd make this folder a git repo and push it to a GitHub repo (personal or a course org), then turn on Pages. The URL is `https://<user-or-org>.github.io/<repo>/`, and a custom domain is optional. Updating during class is just a push. Link it from Canvas so students still start where they're used to.

Repo: `git@github.com:zappala/ai-levels.git`.
