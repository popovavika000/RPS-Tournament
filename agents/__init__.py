from .rock_agent import agents as rock_agents
from .copy_opponent import agents as copy_agents
from .custom_agents import agents as custom_agents

#объединение всех агентов в один словарь
all_agents = {
    **rock_agents,
    **copy_agents,
    **custom_agents
}
