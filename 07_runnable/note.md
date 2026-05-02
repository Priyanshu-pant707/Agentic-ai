# Runnable :

- a runnable is an object that can be executed with input -> and return output
```
input-> process -> output

```


# why runnable is important in gen ai ?
- in gen ai apps , we often build pipeline like :
   -  user input -> prompt -> llm -> output
   - input-> preprocessing -> model -> postprocessing
- runnable helps you chain these steps cleanly.


# types of runnables in langchain :
1. runnableLambda -> custom function 
2. runnableSequence ->  chain
3. runnableMap -> parallel execution
4. LLMs -> also runnables
5. Prompts -> also runnables

