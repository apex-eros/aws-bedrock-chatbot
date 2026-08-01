# AWS Bedrock Chatbot

A simple AI chatbot built using **Amazon Bedrock**, **Meta Llama 3**, **LangChain**, and **Streamlit**. This project demonstrates how to integrate foundation models hosted on AWS with a web application, making it a great starting point for understanding cloud-based Generative AI applications.

## 🚀 Overview

This chatbot allows users to interact with a Large Language Model (LLM) through a Streamlit interface. User queries are processed using LangChain and sent to Amazon Bedrock, which invokes the Meta Llama 3 model and returns AI-generated responses.

While intentionally simple, this project provides hands-on experience with:

* Amazon Bedrock
* Foundation Models (Meta Llama 3)
* LangChain Integration
* AWS Authentication & IAM
* Streamlit UI Development
* Cloud-based AI Inference

## 🏗️ Architecture

```text
User
  │
  ▼
Streamlit UI
  │
  ▼
LangChain Prompt
  │
  ▼
Amazon Bedrock Runtime
  │
  ▼
Meta Llama 3 Model
  │
  ▼
Generated Response
```

## 🛠️ Tech Stack

* Python
* Amazon Bedrock
* Meta Llama 3
* LangChain
* Boto3
* Streamlit
* AWS IAM

## ✨ Features

* Interactive chatbot interface
* Multi-language support
* Amazon Bedrock integration
* Prompt templating using LangChain
* Lightweight and beginner-friendly architecture

## 📂 Project Structure

```text
aws-bedrock-chatbot/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Setup

### Clone Repository

```bash
git clone https://github.com/apex-eros/aws-bedrock-chatbot.git
cd aws-bedrock-chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
aws_access_key_id=YOUR_ACCESS_KEY
aws_secret_access_key=YOUR_SECRET_KEY
region_name=YOUR_REGION
```

### Run Application

```bash
streamlit run main.py
```

## 🎯 Learning Outcomes

This project helped me understand:

* How Amazon Bedrock serves foundation models through managed APIs
* Secure authentication and authorization using AWS credentials
* Integrating cloud AI services with Python applications
* Prompt engineering using LangChain
* Building and deploying simple GenAI applications

## 🔮 Future Improvements

* Conversation memory
* Chat history
* RAG (Retrieval-Augmented Generation)
* Knowledge base integration
* Authentication and user sessions
* Deployment on AWS EC2 or ECS

## 👨‍💻 Author

**Jayesh Gangi**

Aspiring Data Scientist passionate about Machine Learning, Generative AI, NLP, Cloud Technologies, and building real-world AI solutions.
