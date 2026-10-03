"""The agent: a model, some tools, a loop, and a memory."""

from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic
from langgraph.checkpoint.memory import InMemorySaver

from config import MODEL, STEP_LIMIT, SYSTEM_PROMPT
from tools import load_tools

model = ChatAnthropic(model=MODEL)

# The agent's memory: every message of every chat, including each tool call and
# its result. Without it, the model sees only earlier answers and can claim a
# change it never made.
memory = InMemorySaver()


async def ask(question, chat_id):
    """Ask one question in a chat. Returns the answer and the tools it called."""
    agent = create_agent(model, await load_tools(), system_prompt=SYSTEM_PROMPT, checkpointer=memory)

    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": question}]},
        config={"recursion_limit": STEP_LIMIT, "configurable": {"thread_id": chat_id}},
    )

    # Tool calls made for this question: everything after the last user message.
    messages = result["messages"]
    last_question = max(i for i, m in enumerate(messages) if m.type == "human")
    called = [m.name for m in messages[last_question:] if m.type == "tool"]
    return messages[-1].text, called


async def tool_names():
    """The tool names the server offers."""
    return sorted(t.name for t in await load_tools())