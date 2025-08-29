import json

root_path = "default__Resilient_strategy.json"

instances = json.load(open(root_path))

exp_list = [
    'default__Emotionally-Sensitive',
    'default__Conflict-Averse',
    'default__Info-Overwhelmed',
    'default__Anxious',
    'default__Resilient'
]

per_instance = 50

# Loop through each experiment and slice the instances list sequentially
for idx, exp in enumerate(exp_list):
    start = idx * per_instance
    end = start + per_instance
    # Get the slice of instances for the current file
    exp_instances = instances[start:end]
    
    # Write the slice to a JSON file named after the experiment
    with open(f"../scores/{exp}.json", "w") as f:
        json.dump(exp_instances, f, indent=4)