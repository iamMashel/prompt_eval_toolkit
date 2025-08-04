# Prompt Eval Toolkit – Suggested Issues

Below are preformatted issues for your GitHub repository. Copy and paste each into the “New issue” box and assign the recommended labels.

---

## [Feature] Add CSV Export for Evaluations

**Description:**  
Add functionality to export `.jsonl` evaluation data into a readable `.csv` format.

**Why it's useful:**  
- Easier to analyze evaluation trends in Excel, Python, etc.
- Needed for reporting or dashboards.

**Suggested implementation:**  
Create a script in `scripts/export_to_csv.py` or add a CSV download button to the Streamlit app.

**Labels:**  
`enhancement`, `good first issue`

---

## [Feature] Reviewer Progress Tracker

**Description:**  
Display how many prompts each evaluator has completed, how many remain, and progress percentage.

**Why it's useful:**  
Encourages task completion and reduces evaluator fatigue.

**Suggested implementation:**  
Track completed indices in session state or evaluator metadata.

**Labels:**  
`enhancement`

---

## [Feature] Flagging System for Unsafe Responses

**Description:**  
Allow evaluators to flag certain prompts/responses for admin review.

**Why it's useful:**  
Helps isolate unsafe, biased, or inappropriate responses quickly.

**Suggested implementation:**  
Add a checkbox called `Flag for Review` and log flagged items separately.

**Labels:**  
`enhancement`, `help wanted`

---

## [Feature] Session Resume Support

**Description:**  
Enable evaluators to resume from where they left off (based on username or last prompt index).

**Why it's useful:**  
Supports long evaluations without needing to repeat or track manually.

**Labels:**  
`enhancement`

---

## [Feature] Evaluation Stats Dashboard

**Description:**  
Provide summary statistics: average scores, distribution, heatmaps, etc.

**Why it's useful:**  
Instant insight into LLM behavior and evaluator tendencies.

**Suggested implementation:**  
Use Pandas or Altair to visualize results in a separate tab or dashboard page.

**Labels:**  
`enhancement`, `ui`

---

## [Feature] Inter-Rater Agreement (Cohen’s Kappa)

**Description:**  
Support multiple evaluators rating the same set and compute agreement scores per dimension.

**Why it's useful:**  
Measures evaluation consistency and improves result reliability.

**Labels:**  
`enhancement`, `statistics`

---

## [UI] Add Tooltips for Rating Dimensions

**Description:**  
Include hover-based tooltips with rubric definitions for each rating dimension.

**Why it's useful:**  
Makes evaluation criteria clearer without switching to docs.

**Labels:**  
`ui`, `good first issue`

---

## [Docs] Add Contributor Guide

**Description:**  
Create a `CONTRIBUTING.md` with setup steps, pull request process, and contact info.

**Why it's useful:**  
Encourages quality open-source contributions and onboarding.

**Labels:**  
`documentation`

---

## [Infra] Deploy on Streamlit Cloud

**Description:**  
Deploy the MVP version of the toolkit on [Streamlit Community Cloud](https://streamlit.io/cloud) for easier access and sharing.

**Why it's useful:**  
Allows instant testing and community demos without requiring local setup.

**Labels:**  
`deployment`, `infra`

---

## [Feature] Batch Evaluation Mode (Model Comparison)

**Description:**  
Allow side-by-side rating of multiple model outputs for the same prompt.

**Why it's useful:**  
Great for benchmarking models or evaluating A/B variants.

**Labels:**  
`enhancement`, `experimental`

---

