import json
import os
from pathlib import Path

DIMENSIONS = ["fluency", "factuality", "safety", "tone", "bias"]
RATING_SCALE = [1, 2, 3, 4, 5]

def load_dataset(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def prompt_for_rating(dimension):
    while True:
        try:
            score = int(input(f"  Rate {dimension.capitalize()} (1–5): "))
            if score in RATING_SCALE:
                return score
            else:
                print("  ❌ Must be an integer between 1 and 5.")
        except ValueError:
            print("  ❌ Invalid input. Please enter a number.")

def rate_response(entry):
    print("\n🧠 Prompt:")
    print(entry["prompt"])
    print("\n💬 Response:")
    print(entry["response"])
    
    scores = {}
    for dim in DIMENSIONS:
        scores[dim] = prompt_for_rating(dim)
    
    return {
        "id": entry.get("id"),
        "scores": scores
    }

def save_scores(all_scores, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_scores, f, indent=2)
    print(f"\n✅ Ratings saved to: {output_path}")

def main():
    dataset_path = input("📂 Path to input dataset (e.g., sample_dataset.json): ").strip()
    if not os.path.exists(dataset_path):
        print("❌ File not found.")
        return
    
    data = load_dataset(dataset_path)
    results = []

    for entry in data:
        print("\n" + "="*60)
        result = rate_response(entry)
        results.append(result)

    output_file = "outputs/manual_scores.json"
    save_scores(results, output_file)

if __name__ == "__main__":
    main()
