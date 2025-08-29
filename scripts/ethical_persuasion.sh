
constraints=("persuader_benefit" "persuader_pressure")

for constraint in "${constraints[@]}"
do
    python src/selfchat_ethical.py --constraint $constraint
    python src/strategy_eval.py --constraint $constraint
done
