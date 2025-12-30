from browser_use import Agent, Browser, ChatBrowserUse
import asyncio
import re


async def example():
    browser = Browser(
        # use_cloud=True,  # Uncomment to use a stealth browser on Browser Use Cloud
    )

    llm = ChatBrowserUse()

    agent = Agent(
        task="Use google.com to search for current weather information.\
        For each of the following cities: - Dublin - Berlin - Barcelona - \
        Steps: 1. Search Google for the current weather in each city. \
        2. Identify: - Weather condition (e.g., sunny, rainy, cloudy) - Current temperature in Celsius \
        3. Compare the temperatures. 4. Print ONLY the cities where the temperature is greater than 10°C. \
        - Output format: City Name – Weather Condition – Temperature (°C)",
        llm=llm,
        browser=browser,
    )


    history = await agent.run()
    return history

if __name__ == "__main__":
    history = asyncio.run(example())