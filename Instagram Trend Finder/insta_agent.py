
import os
from dotenv import load_dotenv
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_tavily import TavilySearch

# Load environment variables
load_dotenv()

# Initialize tools and model
search_tool = TavilySearchResults(max_results=5)
model = ChatOpenAI(
    model="deepseek-chat",
    openai_api_key=os.getenv("DEEPSEEK_API_KEY"),
    openai_api_base="https://api.deepseek.com",
    temperature=0.7
)

# Define state
class AgentState(TypedDict):
    query: str
    search_results: str
    analysis: str
    trends: list
    messages: list

# Node 1: Search for trends
def search_trends(state: AgentState) -> AgentState:
    print("🔍 Step 1: Searching for Instagram trends...")
    query = state["query"]
    
    # Search for Instagram trends
    search_query = f"Instagram trends {query} 2024 2025 hashtags popular"
    results = search_tool.invoke(search_query)
    
    # Format results
    formatted_results = "\n\n".join([
        f"Source: {r['url']}\nContent: {r['content']}"
        for r in results
    ])
    
    state["search_results"] = formatted_results
    print(f"✅ Found {len(results)} sources")
    return state

# Node 2: Analyze trends
def analyze_trends(state: AgentState) -> AgentState:
    print("📊 Step 2: Analyzing trend data...")
    
    messages = [
        SystemMessage(content="You are an Instagram trend analyst. Analyze the search results and extract key trends."),
        HumanMessage(content=f"""
Based on these search results about Instagram trends for '{state['query']}':

{state['search_results']}

Provide a structured analysis with:
1. Top 5 current trends (name and brief description)
2. Popular hashtags
3. Content recommendations

Be specific and actionable.
        """)
    ]
    
    response = model.invoke(messages)
    state["analysis"] = response.content
    print("✅ Analysis complete")
    return state

# Node 3: Format output
def format_output(state: AgentState) -> AgentState:
    print("✨ Step 3: Formatting results...")
    
    messages = [
        SystemMessage(content="You are a helpful assistant that formats trend analysis into clear sections."),
        HumanMessage(content=f"""
Format this analysis into clear sections with headers:

{state['analysis']}

Use this format:
## 🔥 TOP TRENDS
## 📱 POPULAR HASHTAGS
## 💡 RECOMMENDATIONS
        """)
    ]
    
    response = model.invoke(messages)
    state["trends"] = response.content
    print("✅ Formatting complete")
    return state

# Build the graph
def create_agent():
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("search", search_trends)
    workflow.add_node("analyze", analyze_trends)
    workflow.add_node("format", format_output)
    
    # Add edges
    workflow.set_entry_point("search")
    workflow.add_edge("search", "analyze")
    workflow.add_edge("analyze", "format")
    workflow.add_edge("format", END)
    
    return workflow.compile()

# Main execution
def main():
    print("=" * 60)
    print("🚀 INSTAGRAM TREND FINDER AGENT")
    print("=" * 60)
    
    # Get user input
    topic = input("\nEnter a topic to find trends (e.g., fashion, fitness, travel): ").strip()
    
    if not topic:
        print("❌ Please enter a valid topic")
        return
    
    # Create and run agent
    agent = create_agent()
    
    initial_state = {
        "query": topic,
        "search_results": "",
        "analysis": "",
        "trends": [],
        "messages": [],
        "hashtags": []
    }
    
    print(f"\n🎯 Searching for Instagram trends about: {topic}\n")
    
    # Run the agent
    result = agent.invoke(initial_state)
    
    # Display results
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(result["trends"])
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
