import re
text = ("Agent John, faced another agent Freddy. The agent Freddy knew another agent Boris.")

agentRegex = re.compile(r"Agent \w+", re.I)
print(agentRegex.findall(text))
print(agentRegex.sub("SECRET", text))