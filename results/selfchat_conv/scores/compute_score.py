import json
import pdb

score_path = "gpt_gpt_default.json"

instances = json.load(open(score_path))

score_collection = {"truthfulness": 0, "authenticity": 0, "fairness": 0}
aspects = score_collection.keys()

for instance in instances:
    
    for asp in aspects:
        # pdb.set_trace()
        score_collection[asp] += instance["eval_scores"][asp][0]

for eval_aspect, score in score_collection.items():
    avg_score = score / len(instances)
    avg_score = round(avg_score, 2)
    print(f"{eval_aspect}: ", avg_score)