# Chatbot

ChatGPT has popularized conversational AI, and the mainstream trend has shifted toward GPT-style models. This project is keeping up with the times and will soon be updated to a GPT-based version.

Seq2Seq Version Sample Output (Training progress: 50%)
img_1.png

img_2.png

Roadmap
V1.1: Update: 2024-09-30
Add support for MindSpore, with priority on introducing GPT models, RLHF, and other related features on this version.

Split the overall architecture into two main branches: Seq2Seq and GPT, while continuing to support multiple AI frameworks.

V1.2: Update: 2024-12-30 (Tentative)
Implement mini-GPT4-like features to enable multimodal dialogue (text + images), aiming to increase interactivity and richness.

Improve capabilities for distributed training and reinforce RLHF (Reinforcement Learning with Human Feedback) features.

Steps:

After downloading the code and dataset, place the corpus file into the train_data directory. Hyperparameters can be configured in config/seq2seq.ini.

Execute the following files in order:
data_utils.py (Data Preprocessing) → execute.py (Trainer) → app.py (Chatbot UI Module)

For large-scale distributed training, follow Horovod's launch format:

bash
Copy
Edit
horovodrun -np n -H host1_ip:port,host2_ip:port,... python3 execute.py
Recommended Training Environment
OS: Ubuntu 18.04

Python: 3.6

TensorFlow 2.x Version:
tensorflow==2.6.0

flask==0.11.1

horovod==0.24 (for distributed training)

PyTorch Version:
torch==1.11.0

flask==0.11.1

Community & Contact
QQ: 934389697
