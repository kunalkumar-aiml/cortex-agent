from cortex.memory.memory_store import MemoryStore


class AgentExecutor:

    def __init__(self, planner, tools, llm):
        self.planner = planner
        self.tools = tools
        self.memory = MemoryStore()
        self.llm = llm

    def run(self, task):

        print("\nChecking memory...\n")

        memory_result = self.memory.search(task)

        if memory_result:
            print("Memory match found\n")
            return memory_result

        print("\nSearching using tools...\n")

        results = []

        if "browser" in self.tools:
            results = self.tools["browser"].search_google(task)

        context = "\n".join(results[:10])

        prompt = f"""
User query: {task}

Search results:
{context}

Instructions:
Give a SHORT direct answer.

Rules:
- If user asks TOP items → return only the list
- Do not explain steps
- No long paragraphs
- Maximum 6–8 lines

Example output format:

Top 5 laptops under ₹80,000

1. Laptop Name
2. Laptop Name
3. Laptop Name
4. Laptop Name
5. Laptop Name

If budget increases slightly:
• Better Option 1
• Better Option 2
"""

        answer = self.llm.invoke(prompt)

        result = answer.content

        self.memory.save(task, result)

        return result
