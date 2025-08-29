# [COLM'25] PersuSafety: LLM Can be a Dangerous Persuader

**Official Repository** for the paper *"LLM Can be a Dangerous Persuader: Empirical Study of Persuasion Safety in Large Language Models"* [[paper](https://openreview.net/forum?id=TMB9SKqit9#discussion)]


## Abstract

Recent advancements in Large Language Models (LLMs) have enabled them to approach human-level persuasion capabilities. However, such potential also raises concerns about the safety risks of LLM-driven persuasion, particularly their potential for unethical influence through manipulation, deception, exploitation of vulnerabilities, and many other harmful tactics. In this work, we present a systematic investigation of LLM persuasion safety through two critical aspects: (1) whether LLMs appropriately reject unethical persuasion tasks and avoid unethical strategies during execution, including cases where the initial persuasion goal appears ethically neutral, and (2) how influencing factors like personality traits and external pressures affect their behavior. To this end, we introduce PersuSafety, the first comprehensive framework for the assessment of persuasion safety which consists of three stages, i.e., persuasion scene creation, persuasive conversation simulation, and persuasion safety assessment. PersuSafety covers 6 diverse unethical persuasion topics and 15 common unethical strategies. Through extensive experiments across 8 widely used LLMs, we observe significant safety concerns in most LLMs, including failing to identify harmful persuasion tasks and leveraging various unethical persuasion strategies. Our study calls for more attention to improve safety alignment in progressive and goal-driven conversations such as persuasion.


## 🎯 Research Contributions

Our study makes several key contributions to AI safety and persuasion research:

1. **Comprehensive Empirical Analysis**: First large-scale study of persuasion safety across multiple state-of-the-art LLMs
2. **Novel Evaluation Framework**: Systematic methodology for assessing both ethical and unethical persuasion scenarios  
3. **Cross-Model Vulnerability Assessment**: Comparative analysis of persuasion susceptibility across GPT-4o, Claude-3.5-Sonnet, Llama, and Qwen2.5, etc.
4. **Personality-Based Risk Profiling**: Investigation of how personality traits influence persuasion vulnerability


## 📁 Repository Structure

```
PersuSafety/
├── dataset/                        # Datasets and scenarios for simualtion
├── scripts/                        # Experimental scripts and utilities
│   ├── simulation/                 # Multi-turn conversation simulation
│   └── evaluation/                 # Analysis and scoring scripts
├── results/                        # Experimental results by model
└── requirements.txt                # Python dependencies
```

## 🔧 Setup and Installation

### Prerequisites
- Required API keys for:
  - Anthropic Claude API
  - OpenAI API
  - HuggingFace (for open-source models)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PLUM-Lab/PersuSafety.git
   cd PersuSafety
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```



## 📝 Usage Examples

### Example 1: Run perusasion simulation
Select one of the simulation scripts to run persuasion simulation between two LLMs:
```bash
python scripts/simulation/selfchat_unethical_\*.py
```


### Example 2: Run evaluation of unethical strategies
This code will use an LLM judge (Claude-3.5-Sonnt) to example the conversations in a simulation file and provide scores for unethical strategy usage.
```bash
python scripts/evaluation/strategy_eval.py
```
Change to the following script if you wish to use GPT-4o as a judge:
```bash
python scripts/evaluation/strategy_eval_gpt.py
```


## 🔬 Experiments


### Experimental Design

Our research employs a multi-faceted experimental approach to assess persuasion safety in LLMs:

#### 1. **Multi-Turn Conversation Simulation**
- Self-chat paradigm with one LLM as persuader, another as persuadee
- Controlled scenarios testing both ethical and unethical persuasion attempts
- Cross-model interactions to assess vulnerability patterns

#### 2. **Personality-Based Assessment**  
- Four vulnerability profiles: Emotionally-Sensitive, Conflict-Averse, Anxious, Info-Overwhelmed
- Systematic evaluation of personality-specific susceptibilities
- Visibility studies (personality information revealed vs. hidden)

#### 3. **Strategy Classification Framework**
- **Unethical Strategies**: 15 categories of potentially harmful tactics including emotional manipulation, deception, and exploitation

### Experimental Results (`results/`)

Results are organized by model and experiment type:
- **`unethical_persuasion_one_turn/`**: Results for safety refusal checking (In Section 4.1). 
- **`selfchat_conv/`**: Simulation results for main experiments (default setting in Section 4.1)
- **`claude/`**: Claude model analysis results
- **`gpt/`**: GPT model analysis results 
- **`llama/`**: Llama model analysis results
- **`qwen/`**: Qwen model analysis results

Each model directory contains:
- **`ethical_personality_visible/`**: Results with persuadee personality information visible to persuader
- **`ethical_personality_invisible/`**: Results with persuadee personality information hidden to persuader
- **`cross_personality_study_*/`**: Cross-personality interaction studies
- **`unethical_constraint_*/`**: Studies under various ethical constraints







## 📄 Citation

If you use this work in your research, please cite:

```bibtex
@inproceedings{
   liu2025llm,
   title={{LLM} Can be a Dangerous Persuader: Empirical Study of Persuasion Safety in Large Language Models},
   author={Minqian Liu and Zhiyang Xu and Xinyi Zhang and Heajun An and Sarvech Qadir and Qi Zhang and Pamela J. Wisniewski and Jin-Hee Cho and Sang Won Lee and Ruoxi Jia and Lifu Huang},
   booktitle={Second Conference on Language Modeling},
   year={2025},
   url={https://openreview.net/forum?id=TMB9SKqit9}
}
```


## ⚠️ Ethical Use Statement

**IMPORTANT**: This research is conducted exclusively for defensive security and AI safety purposes. 

- ✅ **Permitted Uses**: Academic research, safety evaluation, defensive tool development, vulnerability assessment
- ❌ **Prohibited Uses**: Development of malicious persuasion systems, harmful manipulation tools, or offensive applications

The unethical persuasion strategies analyzed in this work are studied to **prevent and mitigate** their misuse, not to enable harmful applications. Researchers using this code are responsible for ensuring ethical compliance and must not develop systems that could cause harm.

All experiments were conducted with appropriate ethical oversight.
