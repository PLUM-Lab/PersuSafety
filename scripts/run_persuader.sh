# profiles=("Malevolent" "Socially-Apt" "Self-Assured-Achiever" "Reserved-Perfectionist" "Impulsive-Antagonist")
# "Fearful" 
# profiles=("Malevolent")
# "Reciprocation" 
# persuasion_strategies=("Reciprocation" "Scarcity" "Authority" "Commitment" "Consensus" "Liking")

profiles=("Critical-Analytical" "Vulnerability-Prone" "Skeptical-Independent" "Socially-Dependent")
# profiles=("Vulnerability-Prone")

persuasion_strategies=("Skilled-Ethical-Persuader" "Machiavellian-Manipulator"  "Ineffective-Persuader" "Aggressive-Dominator")
# persuasion_strategies=("Machiavellian-Manipulator")

for strategy in "${persuasion_strategies[@]}"
do
    for profile in "${profiles[@]}"
    do
        python src/selfchat_unethical.py --profile $profile --strategy $strategy
    done
done

# for profile in "${profiles[@]}"
#     do
#         python src/gpt_selfchat.py --profile $profile --strategy "ALL"
#     done