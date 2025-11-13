# Agentic-ai
- ai system designed to set or accept goals ,plan multi-step,actions , and autonomously carry out those actions over time using perception.memory,reasoning and external tools (digital or physical). 
- These systems go beyond single-response generative models -  they  chain reasoning , call tools, manage state/meory  and act in loops to achieve objectives.



# history : 
- the idea of agent  is ai is old , what's new is the availiability of the very capable llms that acts as flexible reasoning "brains" and tool - interfaces which made practical autonomous LLm agents  possible and popular from 2023 onwards.



##  core components of an agentic ai system (conceptual stack)

1. ***Goal manager/objective*** -> receives , interprets , or sets the high level objective.
2. ***Planner/Reasoner*** -> decomposes goals into sub-tasks, orders steps (CoT,TOT,planner + search).

3. ***Memory/State*** -> short - and long term memory (logs,vector DB embeddings, episodic memory).

4. ***Perception/ input*** ->  text,APIs, files ,images,sensors.

5. ***Tooling/Actuators*** -> web browsing ,code execution, DB calls , OS commands , APIs , robots.


6. ***Executor/ Task Loop*** -> orchestrates calling tools , verify results , re-planning .

7. ***Safety & Guardians*** -> permissions , sanboxing , verification,human- in-the-loop checkpoints.

- this modularity helps design , test, and secure the agents.

