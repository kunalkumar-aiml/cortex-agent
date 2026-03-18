from cortex.memory.memory_store import MemoryStore


class AgentExecutor:

    def __init__(self, planner, tools):

        self.planner = planner
        self.tools = tools
        self.memory = MemoryStore()

    def run(self, task):

        print("\nChecking memory...\n")

        memory_result = self.memory.search(task)

        if memory_result:
            print("Memory match found\n")
            return memory_result

        print("\nSearching using tools...\n")

        results = []

        # Run browser search
        if "browser" in self.tools:
            res = self.tools["browser"].search_google(task)
            results.extend(res)

        print("\nGenerating final answer...\n")

        final_prompt = f"""
User Query: {task}

Search Results:
{results}

IMPORTANT RULES:
- Do NOT explain steps
- Do NOT give planning
- Do NOT write long paragraphs
- Only give the final answer

If the user asks for TOP or BEST items,
return a clean numbered list.

Example format:

1. Item name
2. Item name
3. Item name
4. Item name
5. Item name

Only return the list.
"""

        answer = self.planner.create_plan(final_prompt)

        self.memory.save(task, answer)

        return [answer]
