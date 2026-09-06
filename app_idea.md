i think I might want to build a small submission site as well. Honestly, I hate using canvas, so I'm thinking of building a small app that accepts the submissions, runs the chatbot, presents the async learning materials, and helps with scheduling small groups and zoom links. What do you think?


Thought for 11s
Thought for 11s
Build it, but not all four pieces, and not as one app.

The part worth building is the submission-plus-chatbot core. That's the thing Canvas can't do — per-week system prompts, logged transcripts, a "flag this as wrong" button, and submissions landing somewhere you can actually query. It's a small Hono app on Workers with R2 for uploads and an append-only manifest, which is a weekend for you and fits everything else you run.

The other two pieces I'd solve without code:

Async materials: a static Quarto or Astro site. Zoom links and the week-by-week schedule are just content on that site; they don't need an app.
Small-group scheduling: this is the least valuable feature and the most annoying to build correctly. A When2meet link or a Google Form per week gets you 95% of it. If you must automate, the Calendar connector you already have can create the events once you know the groups.
Three things that would bite you:

Student data. Submissions and chat transcripts are education records. Before storing them on Cloudflare under your account, check what CU's ed-tech or IT security office needs — often it's a short data-use review plus a line in the syllabus. Not a blocker, but do it before the block, not after.
Auth. Don't build accounts. Magic links to their CU email addresses are enough for a cohort this size, and it sidesteps the password problem entirely.
Grade of record. Canvas still has to receive the final pass/fail. Keep it as the thing you touch once at the end and link out to your site for everything else.
And plan the failure mode: if the app is down on a Friday, "email it to me" is the fallback, and students should know that up front.

One upside you may not have priced in: the system prompts and the chatbot's failures become course material. Showing students exactly how their reading companion is instructed, and what it got wrong last year, is a better lesson on LLMs than most lectures.
