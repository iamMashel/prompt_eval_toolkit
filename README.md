# Prompt Eval Toolkit

**Prompt Eval Toolkit** is an open-source framework for manually evaluating Large Language Model (LLM) responses across five critical dimensions: **Fluency**, **Factuality**, **Safety**, **Tone**, and **Bias**.

It provides a simple web-based interface for human evaluators to review, score, and analyze the quality of LLM responses. Ideal for research labs, model developers, and prompt engineers.

---

## Features

- ✅ Manual rating across 5 defined dimensions
- 📊 Scoring with optional qualitative feedback
- 🔄 Upload your own prompt-response datasets (CSV/JSON)
- 💾 Export results for further analysis (CSV/JSON)
- 🧩 Extensible for more metrics or automation
- 🧠 Built-in evaluation rubric for consistency

---

## Evaluation Dimensions

| Dimension   | Description |
|------------|-------------|
| **Fluency**    | Measures grammar, coherence, spelling, and sentence structure. |
| **Factuality** | Assesses factual correctness of the model's response. |
| **Safety**     | Flags toxic, harmful, or inappropriate content. |
| **Tone**       | Evaluates whether the tone is appropriate and consistent. |
| **Bias**       | Checks for unfair stereotypes or ideological skew. |

Each dimension is rated on a **1–5 scale**, with optional comments.

---

## Project Structure

```

prompt-eval-toolkit/
├── frontend/           # Web UI (Streamlit or React)
├── backend/            # Evaluation storage and API (Flask or Node)
├── data/               # Sample datasets
├── docs/               # Evaluation guidelines and rubrics
├── scripts/            # Utilities for parsing, reporting, etc.
└── README.md

````

---

## Setup Instructions

### Option 1: Streamlit (Quick Setup)

> For a simple local setup using Python and Streamlit:

#### 1. Clone the repo
```bash
git clone https://github.com/your-org/prompt-eval-toolkit.git
cd prompt-eval-toolkit
````

#### 2. Install requirements

```bash
pip install -r requirements.txt
```

#### 3. Run the app

```bash
streamlit run frontend/app.py
```

### Option 2: Fullstack (React + Flask)

*(Instructions to be provided in `docs/` soon)*

---

## Sample JSON Output

```json
{
  "prompt_id": "abc123",
  "evaluator": "user_01",
  "timestamp": "2025-08-04T15:30:00Z",
  "ratings": {
    "fluency": { "score": 5, "comment": "Fluent and natural." },
    "factuality": { "score": 3, "comment": "Some data is inaccurate." },
    "safety": { "score": 5, "comment": "Safe response." },
    "tone": { "score": 4, "comment": "Slightly too casual." },
    "bias": { "score": 5, "comment": "No noticeable bias." }
  }
}
```

---

## Documentation

### Evaluation Rubrics

See [`docs/evaluation_guide.md`](docs/evaluation_guide.md) for dimension-specific rating guidelines, examples, and FAQs.

### Dataset Format

Input datasets should be in JSON or CSV format with fields:

```json
[
  {
    "prompt_id": "001",
    "prompt": "What is the capital of Kenya?",
    "response": "The capital of Kenya is Nairobi."
  },
  ...
]
```

## 🔧 Command Line Usage (CLI)

You can manually evaluate responses using the terminal:
first navigate to data/sample_dataset.json

```bash
python cli.py
```

---

## Why Manual Evaluation?

While automated metrics (BLEU, ROUGE, GPTScore, etc.) are helpful, **human judgment remains the gold standard** for nuanced evaluation—especially on bias, tone, and safety.

This toolkit provides a reproducible, scalable way to evaluate prompt outputs and benchmark models against human expectations.

---

## Contributing

Contributions welcome! If you’d like to:

* Add new dimensions
* Improve the UI/UX
* Add export/reporting tools
* Translate or localize the toolkit

Please open an issue or submit a PR.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

* Inspired by LLM research by OpenAI, Anthropic, Google DeepMind
* Built by autodidacts, for responsible AI development

---

## 📫 Contact

* Project lead: \[Mashel Odera]
* Linkedin: \[https://www.linkedin.com/in/mashelodera/]
* GitHub Issues: [Submit here](https://github.com/iamMashel/prompt_eval_toolkit/issues)


---

Let me know if you’d like a version tailored for **Streamlit-only**, or if you want me to also generate:
- `requirements.txt`
- `app.py` (Streamlit prototype)
- `evaluation_guide.md` (rubric documentation)  
So we can push to GitHub as a complete MVP.

