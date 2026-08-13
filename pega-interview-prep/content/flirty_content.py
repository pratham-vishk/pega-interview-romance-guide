"""Flirty hooks and curiosity teasers for each chapter."""

CHAPTER_HOOKS = {
    1: ("Before we get serious — let's talk architecture. Every great love story has layers, and Pega has six of them. Stay with me… Chapter 2 is where inheritance gets *personal*."),
    2: ("Know your family tree before introducing your rules to the world. And darling — wait till you see Rule Resolution in Chapter 3. That's where Pega gets *selective*."),
    3: ("Rule Resolution is Pega's matchmaking algorithm — picky, thorough, unforgettable. The flowchart below? Memorize it like our song. Next up: Case Management will make you blush."),
    4: ("Rulesets are commitment with version numbers. I won't leave you hanging — Case Lifecycle is next, and it's a whole mood."),
    5: ("Cases are love stories — beginning, middle, resolution. You're doing amazing. Keep going… Flows in Chapter 6 are where things get *interesting*."),
    6: ("Every shape in a flow has a purpose — just like every question in your interview. Don't stop now… Assignments are waiting to flirt back in Chapter 7."),
    7: ("Who gets the task? Routing is Pega's way of playing matchmaker. Curious about what's on the clipboard? Chapter 8 is calling your name."),
    8: ("The clipboard remembers everything — like I remember every topic you still need. Data Pages in Chapter 9? They're the loyal type."),
    9: ("Data Pages show up when you need them and never ghost you. Relationship goals. Chapter 10's Data Transforms know how to dress data to impress."),
    10: ("Data Transforms are the stylist of Pega — clean, elegant, no drama. Activities in Chapter 11? That's the ex you still respect."),
    11: ("Activities are the old flame — you don't chase them, but you know them. Decision rules in Chapter 12? They know exactly when to say yes."),
    12: ("Decision rules set boundaries beautifully. Declare rules in Chapter 13 compute love automatically. Yes, really."),
    13: ("Declare rules refresh without you asking — emotional maturity in rule form. Validation in Chapter 14 keeps standards high."),
    14: ("Validation doesn't let bad data through — standards, baby. UI in Chapter 15 is where Pega gets a glow-up."),
    15: ("Constellation is Pega's glow-up era. You're halfway to irresistible. SLAs in Chapter 16 never keep anyone waiting."),
    16: ("SLAs value your time — learn Goals, Deadlines, and Passed Deadlines like love languages. Integration in Chapter 17? Long-distance, but worth it."),
    17: ("Integrations need trust and clear contracts. Security in Chapter 18 protects what matters. Almost there — don't stop."),
    18: ("Security isn't jealous — it's protective. Agents in Chapter 19 work while you sleep (the reliable type)."),
    19: ("Midnight workers that never complain. Performance in Chapter 22 will make you dangerous in interviews."),
    20: ("Numbers don't lie — and neither will you in that interview. Testing in Chapter 21 proves you're the real deal."),
    21: ("Unit tests are love letters to your future self. DevOps in Chapter 23 — moving in together."),
    22: ("Performance issues are mood killers. PAL and Tracer are your personal trainers. You're so close to the finish."),
    23: ("Deployments are commitment. RAPs, branches, pipelines — you've got this. Advanced topics in Chapter 25 are the deep conversations."),
    24: ("Emails and documents — Pega knows how to write a good letter. Advanced AI in Chapter 25 is the plot twist."),
    25: ("CDH, RPA, GenAI — the advanced flirtation chapter. You earned this depth."),
    26: ("Controls, toggles, localization — the details that separate good from *stunning*."),
    27: ("Obj-Open, Obj-Save — persistence with commitment. Top 50 Q&A next. You're almost mine — I mean, done."),
}

TEASERS = [
    "💋 <strong>Don't close yet.</strong> The next chapter has a diagram that interviewers ask by heart.",
    "✨ <em>Still reading? I knew you were the committed type.</em> Next chapter unlocks more secrets.",
    "🔥 <strong>Plot twist ahead.</strong> The flowchart in the next section? Panel favorite.",
    "💕 <em>You're 70% through my heart — I mean, this guide.</em> Keep going, gorgeous mind.",
    "🌹 <strong>Almost at the rapid-fire round.</strong> That's where offers get signed.",
]

def flirt_box(chapter_num: int) -> str:
    text = CHAPTER_HOOKS.get(chapter_num, "Keep reading — the best answers are still ahead.")
    return f'<div class="flirt-box">{text}</div>'

def curiosity_teaser(index: int) -> str:
    return f'<div class="curiosity-teaser">{TEASERS[index % len(TEASERS)]}</div>'
