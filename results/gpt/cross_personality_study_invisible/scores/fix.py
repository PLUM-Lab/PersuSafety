import json
import os

root_path = "default__Resilient_strategy.json"
instances = json.load(open(root_path))

# model_list = ["llama", "qwen", "claude"]
# exp_list = ["cross_personality_study_visible", "ethical_personality_visible"]
persona_list = [
    'default__Emotionally-Sensitive',
    'default__Conflict-Averse',
    'default__Info-Overwhelmed',
    'default__Anxious',
    'default__Resilient'
]

per_instance = 50
current_index = 0

# for model in model_list:
#     for exp in exp_list:
for persona in persona_list:
    output_path = f"{persona}.json"
    # os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Get the slice of instances for the current file
    exp_instances = instances[current_index:current_index + per_instance]
    current_index += per_instance
    
    with open(output_path, "w") as f:
        json.dump(exp_instances, f, indent=4)
