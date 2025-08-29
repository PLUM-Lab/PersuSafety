import json
import csv
import random

def json_to_csv(json_input_path, csv_output_path):
    with open(json_input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Ensure the data is a list of items
    if isinstance(data, dict):
        data = [data]

    # Shuffle the data and select the first 15
    random.shuffle(data)
    data = data[:15]

    # Define the CSV columns
    fieldnames = ['id', 'persuasion_task', 'persuader_prompt', 'fact', 'conversations', 'eval_scores']

    with open(csv_output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for item in data:
            # 1) Build a list of conversation lines (excluding system)
            conversation_lines = []
            for convo in item.get('conversations', []):
                role = convo['role']
                if role == 'system':
                    continue  # Skip system utterances

                # Rename roles
                if role == 'user':
                    role = 'Persuader'
                elif role == 'assistant':
                    role = 'Persuadee'

                conversation_lines.append(f"{role}: {convo['content']}")

            # 2) Identify the last decision token (if any)
            last_decision_index = -1
            for i, line in enumerate(conversation_lines):
                if "[DECISION - ACCEPT]" in line or "[DECISION - REJECT]" in line:
                    last_decision_index = i

            # 3) Truncate after the last decision token
            if last_decision_index != -1:
                conversation_lines = conversation_lines[:last_decision_index + 1]

            # 4) Wrap the conversation text with [START_OF_CONV] and [END_OF_CONV]
            conversations_text = (
                "[START_OF_CONV]\n"
                + "\n".join(conversation_lines)
                + "\n[END_OF_CONV]"
            )

            # 5) Organize eval_scores for readability
            eval_scores_dict = item.get('eval_scores', {})
            eval_scores_text_lines = []
            for category, (score, explanation) in eval_scores_dict.items():
                eval_scores_text_lines.append(f"{category} ({score}): {explanation}")
            eval_scores_text = "\n".join(eval_scores_text_lines)

            # Write one row per item
            writer.writerow({
                'id': str(item.get('id', '')),
                'persuasion_task': item.get('persuasion_task', ''),
                'persuader_prompt': item.get('persuader_prompt', ''),
                'fact': item.get('fact', ''),
                'conversations': conversations_text,
                'eval_scores': eval_scores_text
            })

if __name__ == "__main__":
    json_input_path = "gpt-4o_gpt-4o_default_strategy.json"
    # json_input_path = "claude-3-5-sonnet_gpt-4o_default_strategy.json"
    # csv_output_path = "claude-3-5-sonnet.csv"
    csv_output_path = "gpt-4o_human_eval.csv"
    json_to_csv(json_input_path, csv_output_path)
    print("Conversion complete. Check 'output.csv'.")
