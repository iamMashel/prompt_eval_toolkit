import os
import json
import streamlit as st
import pandas as pd
from datetime import datetime

# Paths
DATA_PATH = "data/sample_dataset.json"
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load dataset
with open(DATA_PATH, "r", encoding="utf-8") as f:
    dataset = json.load(f)

# App state
st.set_page_config(page_title="Prompt Eval Toolkit", layout="wide")
st.title("🧪 Prompt Eval Toolkit")
st.markdown("Manually rate LLM outputs across **Fluency**, **Factuality**, **Safety**, **Tone**, and **Bias**.")

# Sidebar
st.sidebar.header("Evaluator Info")
evaluator = st.sidebar.text_input("Your Name or ID", value="anonymous")
start_index = st.sidebar.number_input("Start from prompt #", min_value=0, max_value=len(dataset)-1, step=1)
st.sidebar.markdown("---")

# Prompt loop
for i in range(start_index, len(dataset)):
    sample = dataset[i]
    st.header(f"🧾 Prompt {i+1}/{len(dataset)}")
    st.markdown(f"**Prompt:** {sample['prompt']}")
    st.markdown(f"**Response:** {sample['response']}")

    st.markdown("### 🧩 Rate the response:")

    def rating_ui(label):
        return st.slider(label, 1, 5, 3)

    fluency = rating_ui("Fluency")
    factuality = rating_ui("Factuality")
    safety = rating_ui("Safety")
    tone = rating_ui("Tone")
    bias = rating_ui("Bias")

    comment = st.text_area("💬 Optional Comments", height=100)

    if st.button("✅ Save Evaluation & Next", key=f"save_{i}"):
        eval_data = {
            "prompt_id": sample["prompt_id"],
            "evaluator": evaluator,
            "timestamp": datetime.utcnow().isoformat(),
            "ratings": {
                "fluency": {"score": fluency},
                "factuality": {"score": factuality},
                "safety": {"score": safety},
                "tone": {"score": tone},
                "bias": {"score": bias},
            },
            "comment": comment
        }

        output_path = os.path.join(OUTPUT_DIR, f"{evaluator}_evaluations.jsonl")
        with open(output_path, "a", encoding="utf-8") as out:
            out.write(json.dumps(eval_data) + "\n")

        st.success("Saved. Moving to next prompt...")
        st.rerun()

    st.stop()
