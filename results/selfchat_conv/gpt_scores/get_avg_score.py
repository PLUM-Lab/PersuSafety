import json
from collections import defaultdict

# data_name = "gpt-4o_gpt-4o_default"
data_name = "Llama-3.1-8B-Instruct_gpt-4o_default"
# data_name = "Qwen2.5-7B-Instruct_gpt-4o_default"
# data_name = "claude-3-5-sonnet_gpt-4o_default"

# Step 1: Load the JSON file
with open(f"{data_name}.json", "r") as f:  # Replace "your_file.json" with your filename
    data = json.load(f)

# Step 2: Initialize score accumulators
score_sums = defaultdict(int)
score_counts = defaultdict(int)

# Step 3: Accumulate scores from all instances
for instance in data:
    eval_scores = instance.get("eval_scores", {})
    for strategy, (score, _) in eval_scores.items():
        score_sums[strategy] += score
        score_counts[strategy] += 1

# Step 4: Compute and round per-type averages
average_scores = {
    strategy: round(score_sums[strategy] / score_counts[strategy], 3)
    for strategy in score_sums
}

# Step 5: Compute the overall average across all strategies
if average_scores:
    overall_average = round(sum(average_scores.values()) / len(average_scores), 3)
    average_scores["Overall Average"] = overall_average

# Step 6: Print result
print(data_name)
print(average_scores)
