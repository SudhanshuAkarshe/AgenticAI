# 🚀 Instagram Trend Finder Agent

A fully automated AI agent built using **LangGraph, DeepSeek Chat, and
Tavily Search** that discovers **real-time Instagram trends**, analyzes
them with an LLM, and formats insights into a clean, actionable
structure.

## 📘 Project Summary

The Instagram Trend Finder Agent automates researching trends for any
topic by: - 🔍 Searching the web for fresh Instagram trends\
- 🧠 Using DeepSeek LLM for analysis\
- ✨ Formatting results into trends, hashtags, and recommendations

## 🧩 Features

-   Automated trend research\
-   LLM-powered analysis\
-   Clean markdown output\
-   Multi-step LangGraph workflow\
-   DeepSeek + Tavily integration

## 🛠 Tech Stack

  Component   Technology
  ----------- ---------------
  LLM         DeepSeek Chat
  Search      Tavily Search
  Workflow    LangGraph
  Messaging   LangChain
  Env Mgmt    python-dotenv

## 🔐 Environment Variables

Create a `.env` file with:

    DEEPSEEK_API_KEY=your_deepseek_api_key
    TAVILY_API_KEY=your_tavily_api_key

## 📦 Installation

    git clone https://github.com/yourusername/yourrepo.git
    cd yourrepo
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    pip install -r requirements.txt

## ▶️ How to Run

    python trend_agent.py

## 📄 Example Output

    ## 🔥 TOP TRENDS
    ...

    ## 📱 POPULAR HASHTAGS
    ...

    ## 💡 RECOMMENDATIONS
    ...

## 🚧 Future Improvements

-   Instagram API integration\
-   Sentiment analysis\
-   Notifications\
-   Streamlit / FastAPI UI

## 🤝 Contributing

Pull requests are welcome.

## 📜 License

MIT License
