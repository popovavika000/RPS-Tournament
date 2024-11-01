import random
from utils.get_score import get_score  # Импорт функции подсчета очков

#Агент всегда выбирает Камень -1 
def agent_rock(obs, config):
    return 0

#Агент всегда выбирает Бумагу -2
def agent_paper(obs, config):
    return 1

#Агент всегда выбирает Ножницы -3 
def agent_scissors(obs, config):
    return 2

#Агент случайно выбирает действие -4 
def agent_random(obs, config):
    return random.randrange(0, config.signs)

#Агент копирует последний ход противника -5
def agent_copy(obs, config):
    if obs.step > 0:
        return obs.lastOpponentAction
    else:
        return random.randrange(0, config.signs)

#Агент реагирует на последний ход противника -6
last_action_react = None
def agent_react(obs, config):
    global last_action_react
    if obs.step == 0:
        last_action_react = random.randrange(0, config.signs)
    elif get_score(last_action_react, obs.lastOpponentAction) <= 1:
        last_action_react = (obs.lastOpponentAction + 1) % config.signs
    return last_action_react

# Агент пытается перехитрить противника -7
last_action_counter = None
def agent_counter(obs, config):
    global last_action_counter
    if obs.step == 0:
        last_action_counter = random.randrange(0, config.signs)
    elif get_score(last_action_counter, obs.lastOpponentAction) == 1:
        last_action_counter = (last_action_counter + 2) % config.signs
    else:
        last_action_counter = (obs.lastOpponentAction + 1) % config.signs
    return last_action_counter

#Агент использует статистику и выбирает наиболее частый ход противника -8
action_stats = {}
def agent_stats(obs, config):
    global action_stats
    if obs.step == 0:
        action_stats = {}
    action = obs.lastOpponentAction
    if action not in action_stats:
        action_stats[action] = 0
    action_stats[action] += 1
    most_common_action = max(action_stats, key=action_stats.get, default=0)
    return (most_common_action + 1) % config.signs

# выбирает только между Камнем и Ножницами -9
def agent_rock_scissors(obs, config):
    return random.choice([0, 2])

#склонный выбирать Камень, но с небольшим шансом выбирет случайный ход -10
def agent_biased(obs, config):
    return random.choices([0, 1, 2], weights=[0.7, 0.15, 0.15])[0]

#агент меняющий ход после каждого раунда -11
def agent_rotate(obs, config):
    return obs.step % config.signs

#Агент, который выбирает ход против предыдущего действия противника -12
def agent_anti(obs, config):
    if obs.step == 0:
        return random.randrange(0, config.signs)
    else:
        return (obs.lastOpponentAction + 2) % config.signs

#словарь всех агентов
agents = {
    "agent_rock": agent_rock,
    "agent_paper": agent_paper,
    "agent_scissors": agent_scissors,
    "agent_random": agent_random,
    "agent_copy": agent_copy,
    "agent_react": agent_react,
    "agent_counter": agent_counter,
    "agent_stats": agent_stats,
    "agent_rock_scissors": agent_rock_scissors,
    "agent_biased": agent_biased,
    "agent_rotate": agent_rotate,
    "agent_anti": agent_anti
}
