from kaggle_environments import make
from agents.custom_agents import agents

#сооздает окружение
env = make("rps")

#запускает турнир
results = env.run([agents["rock"], agents["paper"], agents["scissors"], agents["random"], agents["copy"]])

#результаты выводит
print(results)
