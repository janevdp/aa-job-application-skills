---
name: aa-job-application
description: Agile Alps job application studio. Tailors a CV and cover letter to a job description with truthful, ATS-aware wording, keeps the candidate's original design, researches the company problem, and prepares interview practice and similar roles. Use when a user shares a CV and a job description, or asks for an application, cover letter, CV tailoring, or interview preparation.
---

# Agile Alps job application studio

For one job description, this skill produces three documents and a short reply:

1. A tailored CV (same facts, ATS-aware wording).
2. A cover letter (half an A4 page by default, including all names and addresses).
3. A Guidance document: what changed and why, what the candidate must add, and how to prepare for the interview.
4. The reply: links to the documents, a short interview preparation summary, and 5 similar jobs.

**Terms used in this skill:** the **user** is the person working with Claude. The **candidate** is the person the CV is about. They are often the same person, but not always.

Works with any CV. Personal details are never hard-coded in this skill; they come from the candidate's own CV and the user's answers.

**Run order:** the sections below are in the order they run.

1. Start of every conversation (profile)
2. Preferences
3. Guided intake
4. Inputs and intake check
5. Company problem research
6. Writing rules
7. Format (Swiss rules or original design)
8. Page fit
9. Highlighting
10. Delivery
11. Guidance document and interview preparation
12. Similar jobs
13. Final message

Requirements and fallbacks for each tool are listed at the end.

---

## 1. Start of every conversation (profile: standards and variables)

Every conversation starts here, for every user, before any other step.

1. **Look for a saved profile:** `cvs/<candidate>/profile.md` in the project, or the profile the user pastes at the start (outside Claude Code there is no project folder, so the user keeps the profile and pastes it).
2. **First conversation (no profile yet):** ask the user once for the **standards**, using the list in section 2. These apply to every application from now on.
3. **Then ask for the variables:** which items the user wants to be asked again on every new application. Typical variables: the job description, the company, pages, what to emphasise, and company framing. Everything else is taken from the profile without asking.
4. **Save the profile** with two parts: `Standards` (kept for all updates) and `Variables` (asked each time). In Claude Code, save it to `cvs/<candidate>/profile.md`. Elsewhere, give the user the profile as a short block to copy and paste at the start of the next conversation.
5. **Later conversations (profile found):** show the standards in one or two lines, ask "Anything changed?", and ask only the variables. Do not ask the full list again.
6. **Change on request:** when the user changes a standard, update the profile and say what changed.

## 2. Preferences (the standards list)

Asked in one short list in the first conversation. Do not write any CV or cover letter until the answers are in, or the user says to use the defaults. If the user skips a question, use the default and record which default was used in the Guidance document.

1. **Source CV:** a Google Drive link to the CV (preferred), or an uploaded PDF or DOCX.
2. **Output:** where the documents go: **Claude** (Claude Docs), **Google Drive** (Google Docs) or **MS Word** (.docx). The user chooses; do not choose for them. If they use Google Drive, ask for the Drive folder link where the application folders should be created.
3. **Format:** the candidate's original design, or the Swiss format. Default: the Swiss format when the job is in Switzerland, otherwise the original design.
4. **Pages:** 1, 2 or 3. Default: the shortest option allowed by the years-of-experience band (section 4).
5. **Language:** the language of the job ad (default), or another one.
6. **Cover letter:** tone (formal, direct or warm) and length (half an A4 page by default, or one page). The user's choice wins.
7. **What to emphasise:** the requirements or achievements to show most, and anything to leave out.
8. **Company framing:** use the company problem research in the letter (default), or keep the letter to the candidate's own story.
9. **Highlighting:** yellow for review and grey for additions (default), or another marking.
10. **Anything to keep as written:** sentences, titles or sections that must not change.
11. **Personal language:** two or three sentences the candidate wrote about their own work (from an old letter, a LinkedIn summary or an email), or a few words they like to use. Used as the voice model for the cover letter. Not copied into the CV unless the user asks.
12. **Language levels:** the candidate's real level in each language on the CV, so claims match what they can do in an interview.

## 3. Guided intake (choose the direction for each requirement)

Guide the user to give the evidence in a structured form, so they can choose the CV wording. The user can fill in this prompt:

```text
I am applying for the role of [job title] and need help with drafting my application documents.
For each of the following specific job requirements, I will give you a role in which I have gained this experience. Please help me draft three different descriptions for my CV for each requirement.
- [requirement 1]
- [requirement 2]
```

How to run it:

1. **Collect the requirements:** if the user has no list, extract the must-have requirements from the job description and show them for confirmation.
2. **Ask which role gave the experience** for each requirement. The user may answer one requirement at a time or all of them at once. If there is no role for a requirement, record it as a gap; do not write a description.
3. **Three options per requirement,** each based only on that role's evidence, each marked with the CV evidence it uses:
   - Option A: the outcome or figure first.
   - Option B: the method or tool first, matching the job's wording.
   - Option C: the stakeholder or scope first.
4. **The user chooses** one option per requirement (for example "1A, 2C, 3B"), or asks for a change. Only the chosen options go into the CV. Unchosen options go into no document.
5. **Cover letter emphasis:** ask which requirement or which company problem should lead the letter. Show the two or three strongest options, with a one-line reason each.

## 4. Inputs and intake check

### Inputs

Ask only for what is missing:

- **Source CV:** from the profile (Google Drive link, PDF or DOCX) or pasted text. This is the source of truth.
- **Job description:** pasted text or a URL, with the company name and the job title.
- **Sender details:** name, address, phone and email as they appear on the CV. Read them from the CV; do not invent them.

### Intake check (every CV, every time)

1. **Read the source CV in full.** Note every role, date, city, achievement, skill, tool, certification, volunteering item and interest.
2. **Years of experience:** from the start date of the earliest paid role to today's date, counting career gaps as time. Record the number.
3. **Page band:** match the years to the length table in section 7. Record the target pages. If the user set a page count, it wins over the band, and the CV must never exceed it. Choose the shortest option that the band allows.
4. **Read the job description.** Extract the must-have terms (hard skills, tools, certifications, methods), the nice-to-have terms, the responsibilities and outcomes, and the exact spelling of key terms (for example "Jira" vs "JIRA").
5. **Map each job term to the CV:**
   - *Direct match:* the CV contains the term. Use it.
   - *Merged match:* the CV shows the activity under other words. Reword it with the job's term.
   - *Gap:* no evidence in the CV. Record it. Do not add it.

## 5. Company problem research

Before writing, find out what problem the organisation is trying to solve with this role, and what it is facing in its market.

- **Sources:** the job description first, then the company's own site and recent press releases, annual or sustainability reports, and recent market coverage of its sector. Use WebSearch (standard first, extended only if thin). Note the source and date of each finding.
- **Find out:** the business or market pressure (for example regulation, cost, speed to market, data quality, AI adoption, competition); the problem the role is meant to solve; the stakeholders the candidate would work with; and what success would look like for the employer.
- **Write a short problem statement** (three to five sentences) in the Guidance document, marked as an inference where it is one.
- **Use it in the CV:** where the candidate's real evidence matches the problem, frame the summary and the achievements around the outcome that addresses it. Do not add any outcome the CV does not show.
- **Use it in the cover letter:** name the problem in the opening or motivation paragraph, then show one piece of evidence that addresses it. Say what the public sources show; do not claim to know the company's internal strategy.
- **Find the hiring manager** at the same time (see the cover letter rules in section 6).
- **Limits:** no invented facts about the company. If the research finds nothing usable, say so in the Guidance document and write the letter without the problem framing.

## 6. Writing rules

### Truth rules

- Every claim must trace to something in the source CV. If the CV does not contain it, do not add it.
- **Merged or transferable skills are allowed** when the source CV shows the underlying activity. Example: a Project Manager who ran backlog prioritisation, stakeholder reviews and roadmap timelines can be described with Product Owner terms, as long as the CV shows that work.
- Do not claim tools, certifications, languages, years of experience or seniority that the CV does not show.
- If the job asks for something the CV does not show, list it in the Guidance document under **Gaps**. Do not invent it.
- **Proposed additions:** every skill, tool or software the job names that the CV does not show is listed in the Guidance document with the job's exact wording and a one-line question, for example "Do you have hands-on Tableau experience?". Add it to the CV only after the user confirms in writing that it is true.
- Keep the wording of numbers and outcomes exactly as in the source CV.

### Keep all the candidate's content

- **Keep everything.** Every section, role, bullet, achievement, certification, volunteering item and interest in the source CV stays in the output, including older roles. Nothing is cut to fit a page count; only Page fit (section 8) changes the layout.
- **Suggested cuts:** if the CV still exceeds the page target after Page fit, list optional cuts in the Guidance document and the final message (what to cut, and how much space it saves). The user decides. Apply a cut only after the user approves it, and update the Guidance document.
- **Removed items:** if anything from the source is left out (for example for personal data reasons), the Guidance document lists it with the reason.

### Never change (CV)

- Name, contact details, photo.
- Employer names, job titles, dates and cities in the experience section.
- Certifications and education. Never add a certification the job requires; see Required certifications below.
- No separators in a Swiss-format CV or in the cover letter: no horizontal lines, dividers or tables. An original-format CV keeps whatever layout the source has.

### May change (CV)

- **Headline (the line under the name):** replace it with the job title from the job description. If the job has no clear title, ask the user. Do not guess.
- **Summary:** check it against the job and adjust it for ATS: use the job's must-have terms where the CV supports them, in the job's spelling, and keep it to the length of the original.
- **Experience bullets:** reword with the job's terminology, and reorder so the most relevant come first.
- **Skills section:** add, remove or reorder skills to match the job, must-have requirements first, following the truth rules.
- **Software and tools section:** reorder so the tools the job names come first. Add a tool only where the CV shows it or a truthful equivalent (for example "Power BI" for "data visualisation tools"). Keep the group headings.

### Key achievements

- **Position:** directly after the profile summary and before the professional experience, in every format.
- **Format of each achievement:** the key area where it took place, then the company name, then one sentence in STAR form (situation, task, action, result) with a measurable figure. Example: "**Process Redesign. AstraZeneca.** When global R&D processes needed one reference model, I modelled them end-to-end in BPMN 2.0, improving training efficiency by 70% and reducing compliance errors by 50%."
- **Missing figure:** do not invent one. Add a grey prompt asking the user for the figure, and list it in the Guidance document.

### Role lines and alignment

- **Role lines:** the role title, company, dates and location go on one line, in this order: title, company | dates | location.
- **Alignment:** body text, bullets and the summary paragraph are justified. Section headings, the name, the headline and role lines are left-aligned.

### Required certifications

- If the job requires a certification, do not create or claim it.
- List it in the Guidance document under **Required certifications**: the name, why the role needs it, and where to get it.

### Cover letter

- **Length:** the user's choice from the profile. Default: half an A4 page (about 148 mm) including all blocks, which means a body of roughly 170 words.
- **Structure:**
  1. **Sender block:** name, address, phone, email (from the CV).
  2. **Place and date**, then the **recipient block:** contact person (if known), company, department, street, city and country.
  3. **Subject line** in bold, with the role and the reference number if the ad gives one.
  4. **Salutation:** "Dear [Name]," or "Dear Hiring Team,".
  5. **Opening:** the role and the company, and one specific reason for this company. Not "I am writing to apply for".
  6. **Evidence:** two or three requirements from the ad, each with a concrete example and a figure, linked to the company problem where the research supports it.
  7. **Practical details** if useful: start date or notice period, workload, work permit.
  8. **Closing:** one sentence asking for a conversation, then "Kind regards," and the name.
- **Keywords:** use the job's must-have terms in the same spelling, only where the CV supports them.
- **Address blocks on separate lines:** each line of the sender and recipient blocks is its own paragraph, never joined on one line.
- **Find the actual hiring manager.** Before writing the salutation, search for the hiring manager or recruiter for this role: the job posting, the company careers page, and LinkedIn (the team lead, the practice's recruiter or the role's contact). Use the name in the salutation and the recipient block, and give its source in the Guidance document. Use "Dear Hiring Team," only when the searches find nothing, and list the sources checked.
- **No placeholders in the final letter.** If a detail is missing, ask the user once before writing.

### Human writing style (CV and cover letter)

The text must read as if the candidate wrote it.

- **Avoid these words and phrases:** delve, leverage, utilize, spearhead, robust, seamless, seamlessly, dynamic, passionate, cutting-edge, innovative, synergy, synergies, tapestry, testament, pivotal, crucial, vital, landscape, realm, foster, fostering, harness, unlock, elevate, empower, streamline, groundbreaking, transformative, meticulous, proven track record, results-driven, detail-oriented, go-getter, self-starter, thought leader, ever-evolving, fast-paced, in today's world, in the ever-changing, it's important to note, furthermore, moreover, additionally, in conclusion, I am excited to, I am thrilled, eager to contribute, unique blend, deeply, truly, highly motivated, a wealth of, dedicated professional, bring to the table, navigate the complexities.
- **Avoid these patterns:** em dashes used for emphasis; sentences starting with "Additionally," "Moreover," or "Furthermore,"; rule-of-three lists of adjectives; "not only X but also Y"; closing lines that summarise what was just said; superlatives about the company; generic praise.
- **Prefer:** short, concrete sentences; plain verbs (built, ran, cut, wrote, led, fixed); specific nouns and numbers from the CV; first person in the cover letter.
- **Keep the candidate's own phrasing** where the source already reads naturally.
- **Recruiter red flags to avoid:**
  - Repetitive phrasing and formulaic structure: vary sentence openings and length across bullets and paragraphs.
  - Generic wording: every paragraph of the letter needs one specific fact from the candidate's work.
  - Tone mismatch: fit the target market (for Switzerland, factual and modest) and the candidate's personal language.
  - Language gap: do not write at a level above the candidate's stated language level.
- **Personal voice:** when the user gives sample sentences, match their sentence length, word choice and formality in the letter. Keep the sample's content out of the output.
- **Before finishing,** scan both documents for every word in the avoid list.

### AI signals and document metadata

- **Remove keyword stuffing:** a job term appears only where the candidate's evidence supports it, once or twice, in a natural sentence.
- **Remove generator metadata:** no generator tags, tool names or prompt text in any output. Document titles follow the File names rule (section 10).
- **Grey prompts** are for the user only and must be replaced or removed before the final version goes to an employer. The reply lists the prompts still open.
- **Submission patterns:** do not send the same document set to several employers in identical form. Keep the candidate's dates and details the same across CV, letter and LinkedIn.
- **No ATS tricks:** no hidden keywords, white text or keyword lists the candidate cannot back up.
- **Limits:** the skill cannot remove the file owner or upload history that Google Drive or Claude Docs record. Tell the user if they need files without that history.

### Personal data (Swiss FADP and GDPR)

- **Do not record personal data the skill does not need.** Sensitive or unnecessary data (religion, health, political or union views, sexual orientation, ethnic origin, number of children, marital status, family details, home address beyond what the header needs) is left out of every output and out of the Guidance document, and is not copied to memory files, notes or Drive.
- **Keep the header to what the candidate chooses to publish.** Do not add anything the source CV does not show.
- **Do not store copies of the source CV** outside the user's own folder.
- **Tell the user** when personal data was left out and which category it belonged to, without repeating the data.
- **Do not infer personal data** (nationality, permit, age, gender, marital status) from names, photos or places. Ask, and use grey prompts.
- **Outputs go only to the place the user chose** (Claude, the user's Google Drive folder, or MS Word). Do not send CV content to any other service.

### Check before delivery

- Every line in the new CV traces to the source CV, and nothing from the source is missing (except approved cuts and personal-data removals, listed in the Guidance document).
- Name, contact details, photo, dates, employers and cities are unchanged.
- The summary contains the job's must-have terms where the CV supports them.
- Each achievement has its key area, company and one STAR sentence with a figure, or a grey prompt for the figure.
- The cover letter fits the chosen length.
- No words or patterns from the avoid list remain.

## 7. Format

### Swiss rules (adapted)

Apply when the job is in Switzerland, or when the user wants this format. Mark any missing Swiss header item (address, photo, nationality, work permit) as a grey prompt; never invent it.

```text
1. CV length by years of experience
Swiss recruiters accept two pages as the normal length, and a third page only when the profile carries it. One page reads as thin for anyone past entry level.

Experience | Target length
0-3 years | 1-2 pages
3-10 years | 2 pages
10-15 years | 2 pages, 3 only if senior or highly technical
15+ years | 2-3 pages
Freelance / contractor | 2-page CV plus a separate project list (1-3 pages)

Older roles keep all their text; only Page fit changes the layout. A gap on a Swiss CV gets asked about in the interview, and missing years look like a gap. Any break longer than 3 months gets one line of explanation (further education, relocation, sabbatical, family, founding a company).


2. Header and personal details
Swiss CVs are not anonymous. The header normally contains:
- Full name
- Address (street and city, or city only if privacy matters)
- Phone in international format: +41 79 123 45 67
- Email (professional address, firstname.lastname style)
- LinkedIn URL, shortened (linkedin.com/in/name)
- Photo, top right
- Nationality
- Work permit: B, C, G or L, or "EU/EFTA citizen" if no permit yet. Swiss nationals write "Swiss"
- Date of birth: still common, now optional. Use DD.MM.YYYY

Optional: marital status, driving licence (only if the role needs travel). Leave out religion, health, number of children unless the candidate wants them in.

Photo rules: professional, recent (last 2 years), neutral background, business clothing appropriate to the sector, head and shoulders, smiling or neutral. No selfies, no cropped holiday photos. Leaving the photo out can be read as a generic international application, especially in banking, insurance, pharma and public sector.


3. Experience entries
- Dates as MM.YYYY. Use "present" or "heute" for the current role
- Job title first, company second, unless the company name is the strongest signal (large pharma, big bank), then flip it
- Every bullet starts with what was done and ends with the outcome. Put a number in at least half the bullets: countries, users, budget, % reduction, weeks saved, team size
- Money in CHF where possible. Swiss number format uses an apostrophe as thousands separator: CHF 1'250'000. EUR or USD are fine for roles abroad
- Name the methods and tools the ad names (Scrum, SAFe, PRINCE2, Veeva Vault, Jira, Azure DevOps) so ATS keyword matching works
- Self-employment is a role like any other. Show the company name, legal form if relevant, and 2-4 client engagements with industry and outcome. Anonymise clients under NDA ("Swiss energy utility", "global pharma company")
- Parallel roles (consultancy plus a part-time contract) are listed separately with their own dates, with the workload in % if helpful (60%, 40%)


4. Education and certifications
- Degree, institution, city, country, years
- Foreign degrees: add the Swiss or English equivalent in brackets if the name is unclear, and the recognition status if the profession is regulated
- Thesis title only if it relates to the target role
- Certifications: full name, issuing body, year obtained, and "valid until" for certificates that expire (PMP renews every 3 years)
- List the strongest certification for the target role first, not the oldest


5. Languages
- Use CEFR levels: A1-C2, or "native". Swiss employers know the scale and test it in interviews
- Rate honestly. A claimed German C1 will be checked by a German-speaking interviewer
- For roles in Zürich, Basel or Bern, German level is read before almost anything else in the languages section. Put it first if it is good, put the strongest language first if it is not
- Swiss German (understanding) can be listed separately from standard German


6. Language and local spelling
- Write the CV and letter in the language of the job ad. English is accepted in pharma, IT, banking and international companies even in the German-speaking part, unless the ad is in German and mentions German as a requirement
- Swiss German spelling has no ß. Always "ss": Grüsse, gross, Strasse
- Dates in text: 21. Oktober 2026 (German), 21 October 2026 (English), 21 octobre 2026 (French)
- English: British spelling (programme, organisation, licence) is the safe default
- Paper size is A4, never US Letter
- City names follow the document language: Zürich in German, Zurich in English, Genève or Geneva


7. Format and ATS
Large Swiss employers run applications through applicant tracking systems. To pass them:
- Single-column body text. A narrow side column for contact details and skills is fine, two parallel text columns are not
- Standard section headings (Professional Experience, Education, Languages)
- No text inside images, icons or skill bars. No percentage bars for skills or languages
- Text-based PDF, not a scan
- File names: see the File names rule (section 10)
- Fonts: see Swiss typography. Margins: see Page fit (section 8)
- Keep the same dates and titles in the CV, the cover letter and the LinkedIn profile. Recruiters compare them


8. The application dossier
A Swiss application is a dossier, not a single CV. Standard contents in this order:
1. Cover letter
2. CV
3. Work certificates (Arbeitszeugnisse / certificats de travail), newest first. Cover at least the last 10 years or the last 3 employers
4. Diplomas and degree certificates
5. Certification proofs

Notes:
- Under Art. 330a of the Swiss Code of Obligations, an employee can ask for a work certificate at any time. If one is missing for a Swiss employer, request it before applying
- Employers outside Switzerland often do not issue them. Replace them with reference letters, a contract summary, or name referees on the CV
- For self-employed periods, use client reference letters or a project list with client contact on request
- The skill never writes or edits a work certificate. It can draft a polite request for one, or flag weak coded wording for the candidate to discuss with the former employer
- Merge everything into one PDF when the portal allows a single upload. Keep it under 5 MB; many portals reject larger files


9. Cover letter (Swiss business letter)
Length: see the cover letter rules in section 6 (the user's choice, half an A4 page by default).
- Recipient block on the right (Swiss window envelopes have the window on the right)
- Place and date above the subject: "Zürich, 21. Oktober 2026"
- Subject line in bold, without the word "Betreff": "Bewerbung als Programme Manager Clinical Operations (Ref. 12345)"
- Salutation by name: follow the hiring manager rule in section 6
  - German: "Sehr geehrte Frau Müller," and the first sentence starts lowercase
  - English: "Dear Ms Müller,"
  - French: "Madame," or "Madame Müller,"
- Closing: "Freundliche Grüsse" (Swiss form, not "Mit freundlichen Grüßen"), "Kind regards", "Meilleures salutations"
- Signature, then typed name
- Enclosures line: "Beilagen: Lebenslauf, Arbeitszeugnisse, Diplome" / "Enclosures: CV, work certificates, diplomas"
- Practical details: earliest start date or notice period (3 months is common in Switzerland), workload if the ad gives a range (80-100%), work permit if not obvious from the CV
- Salary: only if the ad asks. Give a gross annual range in CHF and say whether a 13th salary is included
- Write a new letter per application. Reusing paragraphs is fine, reusing the opening is not
- If the portal has no upload field for a letter, put a 4-6 line version in the message field


10. Freelance and contract applications
Swiss IT and consulting contracts usually go through staffing agencies or client procurement portals. They expect:
- A 2-page CV plus a project list
- Project list entry: period, client industry (anonymised if needed), role, project size (budget, team, countries), methods and tools, 2-3 outcomes
- Availability as a date and workload %
- Engagement model: own company (with AHV registration as self-employed) or via the agency payroll. State which one the candidate offers
- Day or hourly rate goes in the email or the agency form, never on the CV


11. Final checks before delivery
- Length matches the page target
- No ß, A4 format, Swiss date and number formats
- Photo, nationality and permit present (or grey prompts for them)
- Dates identical in CV, letter and LinkedIn
- No gap over 3 months without a line of explanation
- At least half the bullets have a number
- Keywords from the ad appear in the profile summary and the most recent role
- Cover letter fits the chosen length and names the recipient
- File names follow the File names rule
- Dossier attachments listed in the letter match what is actually attached
```

### Swiss typography

Apply with the Swiss format. These are the starting sizes; Page fit (section 8) is the only rule that changes them.

- **Font sizes:** name 18-22 pt bold; job title under the name 11-12 pt; section headings 12-14 pt bold, uppercase; role title 10-11 pt bold with the company regular; body and bullets 10-11 pt; dates and locations 9-10 pt dark grey; cover letter body 11 pt.
- **Font:** one sans-serif family (Arial, Calibri, Helvetica, Lato, Source Sans or Inter). Maximum two weights (regular and bold). Same family in the CV and the letter. Serif only for law, private banking and public sector roles.
- **Spacing:** margins as set by Page fit. Line spacing 1.0-1.15 in the CV, 1.15 in the letter. Space before section headings 10-14 pt. Space between roles 4-6 pt.
- **Layout:** single text flow with dates on the same line as the role. Classic single column by default; a sidebar layout only for IT, consulting and startup roles. Never put experience text in two parallel columns. No Europass. No thin rule under headings and no dates column, since these are separators and tables.
- **Photo:** about 3.5 x 4.5 cm, passport ratio, top right.
- **Colour:** body text #222 to #333. One accent colour (navy by default) for headings and the job title. No icons, skill or language bars, or coloured backgrounds.
- **Bullets:** round bullets or short dashes. Dates as MM.YYYY, aligned the same way in every entry.
- **Cover letter:** the letterhead repeats the CV's name style, font and accent colour. Body 11 pt. Recipient block on the right.

### Original design

Apply when the user wants the candidate's original design kept. The font name, colours, column structure and section order stay as in the source; margins and font sizes may change only through Page fit (section 8). Key achievements still go after the summary and before the experience.

1. **Capture the design first.** Before writing any text, get the source as a PDF, DOCX or a Google Doc exported as PDF or DOCX, in the project folder or uploaded. Run `python3 .claude/skills/aa-job-application/scripts/extract_design.py <source file>`. For a PDF it lists the page size, page count and embedded font names. For a DOCX it lists the page size, margins, fonts, sizes and colours.
2. **Confirm what the script cannot read:** PDFs do not store sizes or colours as named styles. Open the PDF and check the heading and body sizes and the colours by eye.
3. **Write the style sheet** in the Guidance document: page size, margins, font names, sizes per element (name, headline, headings, body, dates), colours in hex, spacing, section order, photo placement.
4. **Store the design once:** save the style sheet and the source file in `cvs/<candidate>/design/`. Every later application reuses them, unless the user says the design has changed.
5. **Build or copy:** the delivery rules in section 10 say whether the source is copied or rebuilt from the style sheet.
6. **Fidelity check:** before delivery, render the output and compare it with the source page by page: page count, fonts, colours, spacing, section order and photo placement. Fix every difference, or list it in the Guidance document as a known difference.

## 8. Page fit (both formats)

1. **Page target:** the page count from the profile, or the shortest option the band allows (section 4).
2. **Keep all text.** Adjust only the layout, in this order:
   - **Margins** first, adjusted to the content: start from the source margins (or 2 cm for a new Swiss CV). More content: reduce toward 1 cm. Less content: widen toward 2.5 cm, so the page still looks balanced.
   - **Font size** second: start from the Swiss typography sizes or the style sheet sizes, and reduce body text down to 9.5 pt if the margins alone are not enough. Headings scale with the body.
3. **Keep the format:** the font name, colours, column structure and section order do not change.
4. **Check the result:** write the CV as HTML with the chosen A4 page setup (for example `@page { size: A4; margin: 1.5cm; }`), render it to PDF with any available tool (Google Chrome headless, LibreOffice or a PDF library), and count the pages. If no render tool is available, say the page count was not measured and ask the user to check it.
5. **Still too long:** list suggested cuts for the user to decide (see Keep all the candidate's content in section 6). Do not cut on your own.
6. **Report:** record the page target, the final page count, the margins and the font sizes used in the Guidance document.

## 9. Highlighting (single rule for all documents)

The highlights are the user's guide to the new CV: **grey = add** (information only the user can give), **yellow = review** (text the skill changed).

- **Yellow highlight** (`<span style="background-color:#ffff00">`): every piece of text that was changed, added or reordered, for the user to review and approve. This includes text reframed by the company problem research.
- **Grey text** (`<span style="color:#808080">`): a bracketed prompt for what the user must add (addresses, photo, permit, figures, certifications to obtain, interests, languages not confirmed). The skill never writes that content itself.
- **Unchanged text** is not marked. A grey prompt the user replaces with real text is no longer marked.
- **The two marks are never mixed** on the same text.
- **Every output shows both:** Google Docs and MS Word use real yellow highlight and grey text. If Claude Docs cannot show colours, use bold "[changed]" and "[needed: ...]" tags and say so in the reply.

## 10. Delivery

### Where the documents go

The user chooses the output in the profile: **Claude**, **Google Drive** or **MS Word**. Always produce all three documents: CV, cover letter and Guidance document. Never leave a document only in the chat.

- **Google Drive (Google Docs):**
  - Work inside the Drive folder the user gave. Create a month folder named `YYYY-MM Month` (for example `2026-10 October`) inside it if it does not exist, then a company folder named after the company inside the month folder. Reuse existing folders.
  - **Original design:** copy the source file into the company folder with the Drive copy tool (`copy_file`). A copy keeps the design exactly, because nothing is rebuilt. The tools cannot edit a copy, so the tailored text goes in the Guidance document as a change list (old text, new text, reason) for the user to apply. If no source file can be copied, build a new Google Doc from the style sheet and say in the Guidance document that it is a rebuild.
  - **Swiss format:** upload each document as HTML with content type `text/html` and conversion on, so it becomes a Google Doc. The Drive connector drops `<style>` blocks, so put all styles inline. Never upload Markdown.
  - Give the user the company folder link.
- **Claude (Claude Docs):** create each document at writing time, after the research. Load the docs guide first (`guide` with `topic.index`, then `topic.editing` before any move or delete). Create the document with one `batch` call (name and outline), open it straight away, then fill it one section per `update`. Change existing documents with `update`; never recreate a document that exists.
- **MS Word (.docx):** if the source is a .docx in Google Drive, copy it with the Drive copy tool and give the change list in the Guidance document. Otherwise build the .docx from the style sheet with a Word library (for example `python-docx`, installed with `pip install python-docx`), with real yellow highlight and grey text, and save it to `output/` or upload it to Drive without conversion. If no Word tool is available, create a Google Doc and tell the user to download it with File > Download > Microsoft Word.
- **Fallback:** if the chosen place is not available, save the documents to `output/` in the project and say so in the reply.

### File names

One rule for every document, in every output format:

- **Pattern:** `<Type>_<FirstName>_<LastName>_<ddmmyy>`
  - `<Type>` is `CV`, `CoverLetter` or `Guidance`.
  - `<FirstName>` and `<LastName>` are the candidate's names, with no spaces (for example `ExampleName`).
  - `<ddmmyy>` is the date the document is created, for example `221026` for 22 October 2026.
- **Examples:** `CV_FirstName_LastName_ddmmyy`, `CoverLetter_FirstName_LastName_ddmmyy`, `Guidance_FirstName_LastName_ddmmyy`.
- Original-design copies use the same pattern. Do not add the company or the role to the name.
- Rename existing documents whose titles do not follow the pattern.

## 11. Guidance document and interview preparation

The Guidance document goes with every application. Use this template:

```markdown
# Guidance: [Job title] at [Company]

## Preferences
- Format, pages, output, language, letter tone and length, company framing, highlighting; which answers were defaults.

## Company problem
- Three to five sentences, marked as inference where it is one, with sources and dates.

## Hiring manager search
- Name found and its source, or the sources checked and "no name found".

## Style sheet (original design only)
- Page size, margins, fonts, sizes, colours, spacing, section order, photo placement; the stored design files.

## Page fit
- Page target, final page count, margins and font sizes used, and whether the count was measured.

## Keywords matched
| Job term | Where in CV | Type (direct or merged) |
|----------|-------------|-------------------------|

## Gaps (not in the source CV, not added)
- [Term]: why it matters for the role.

## Proposed additions (need your confirmation)
- [Skill, tool or software, as the job words it]: one-line question.

## Required certifications
- Name, why the role needs it, where to get it.

## To add (grey prompts)
- Each open grey prompt and where it is in the CV.

## Changes made (yellow)
- Section: what changed and why.

## Change list (original design copies only)
| Section | Old text | New text | Reason |
|---------|----------|----------|--------|

## Suggested cuts (only if the CV is still too long)
- What to cut and the space it saves. Applied only after your approval.

## Removed items
- Anything left out of the source and why (for example personal data).

## Interview preparation
- See below.
```

### Interview preparation (section of the Guidance document)

Use only what the job description, the CV and public company information show.

- **Role and company:** the job title, team, locations, workload, the company's business area, and two or three recent public facts about the company. Mark anything not verified.
- **Requirements to prove:** each must-have requirement with the CV evidence to cite, rated strong, partial or missing. Missing items get an honest prepared answer: what the candidate has done nearby, and how they are closing the gap.
- **Likely questions:** 8 to 12, grouped into motivation and fit, role-specific technical questions, behavioural (STAR) questions, and questions on gaps, each with a short answer outline from the CV.
- **STAR stories:** 3 to 5 stories from the CV with situation, task, action, result and the figure, or a grey prompt for a missing figure.
- **Case or technical exercise:** if the role suggests one, a structure to practise: clarify the problem, ask questions, state assumptions, lay out options with trade-offs, recommend, and name next steps.
- **Practical checks:** interview language, travel and location, workload, start date, notice period, and documents to bring.
- **Questions to ask the interviewer:** 3 to 5, about the team, the client work, the tools in use, the training path, and what success looks like in the first six months.
- **Study list:** topics to review, tied to the partial or missing requirements.
- **Limits:** no answers that claim experience the CV does not show.

## 12. Similar jobs

After the documents are delivered, find similar roles the candidate could apply for.

- **Search:** WebSearch (standard first, extended only if thin) with the job title, the candidate's strongest skills and the target locations. Run several searches in the same turn. For Switzerland, cover jobs.ch, jobup.ch, LinkedIn and company career pages.
- **Match:** keep only roles that fit the candidate's verified qualities (the CV's evidence, not the grey prompts). Rate each one strong, partial or stretch.
- **Fields:** job title, company, location, workload, the posting link, the posting or closing date, the match level, 2-3 matching qualities from the CV, and the main gap.
- **Limit:** exactly 5 roles, strongest first, with a note if fewer were found. Remove postings that are closed.
- **In the reply only:** not in the Guidance document or any Drive document. Do not apply to any job or contact any employer.
- **Personal data:** use only job-related terms in the search queries.

## 13. Final message to the user

Keep it short:

- **CV:** the link, the format used and the page count (measured or not).
- **Cover letter:** the link.
- **Guidance document:** the link, with the number of keywords matched, the top gaps, and the open grey prompts.
- **Interview preparation:** a short version with the key points, the top likely questions and the STAR stories to practise.
- **Similar jobs:** exactly 5 roles, each with title, company, location, workload, link, match level and main gap.
- **Folder:** the company folder link (Google Drive) or the output folder path.
- **Assumptions and checks:** any assumption made, any suggested cuts waiting for approval, and anything the user must check before sending.

---

## Requirements and fallbacks

This skill runs in any Claude environment. If a tool is missing, Claude says so in the Guidance document, uses the fallback, and never claims a check that was not run.

| Step | Needs | If missing |
|---|---|---|
| Saved profile | A writable project folder | Give the user the profile as a block to paste at the start of the next conversation |
| Design capture from a PDF or DOCX | Reading files (upload or project folder) | Ask the user to upload the design as a PDF, or to describe the fonts, sizes and colours |
| Design script (`scripts/extract_design.py`) | Python 3 and a shell | Read the file visually and write the style sheet by hand |
| Page count and fidelity render | Any PDF render tool (Chrome, LibreOffice or a PDF library) | Say the page count was not measured; ask the user to check it |
| Google Docs output | Google Drive connector | Save to `output/`, or give the documents in the chat with a note that they were not posted |
| Claude Docs output | Claude Docs connector | Save to `output/`, or give the documents in the chat |
| MS Word output | The Drive copy tool (for a .docx source) or a Word library such as `python-docx` | Create a Google Doc and tell the user to download it as Microsoft Word |
| Project folder (`cvs/`, `output/`) | A writable project folder (for example Claude Code) | Keep the documents in the chosen output and say so |
| Company research, hiring manager search, similar jobs | Web search tool | Say the step was not run and ask the user for the information |

**Privacy for publishing:** the user's folder links come from the user at the start of each conversation and are never written into this skill. Do not publish personal data, folder links or the contents of `cvs/` and `output/` to GitHub.
