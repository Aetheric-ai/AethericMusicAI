from swarms import Agent, Anthropic

# Initialize the agent
agent = Agent(
    agent_name="Accounting Assistant",
    system_prompt="You're the accounting agent, your purpose is to generate a profit report for a company!",
    agent_description="Generate a profit report for a company!",
    llm=Anthropic(),
    max_loops="auto",
    autosave=True,
    # dynamic_temperature_enabled=True,
    dashboard=False,
    verbose=True,
    streaming_on=True,
    # interactive=True, # Set to False to disable interactive mode
    saved_state_path="accounting_agent.json",
    # tools=[
    #     # calculate_profit,
    #     # generate_report,
    #     # search_knowledge_base,
    #     # write_memory_to_rag,
    #     # search_knowledge_base,
    #     # generate_speech,
    # ],
    stopping_token="Stop!",
    interactive=True,
    # docs_folder="docs",
    # pdf_path="docs/accounting_agent.pdf",
    # sop="Calculate the profit for a company.",
    # sop_list=["Calculate the profit for a company."],
    # user_name="User",
    # # docs=
    # # docs_folder="docs",
    # retry_attempts=3,
    # context_length=1000,
    # tool_schema = dict
    context_length=1000,
    # agent_ops_on=True,
    # tree_of_thoughts=True,
    # long_term_memory=ChromaDB(docs_folder="artifacts"),
)

agent.run(
    "Search the knowledge base for the swarms github framework and how it works"
)
