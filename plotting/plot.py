import pickle
import matplotlib.pyplot as plt
with open('/home/dsteam/PycharmProjects/dqn/plotting/statistics.pkl', 'rb') as f:
    stats = pickle.load(f)

# Statistic["mean_episode_rewards"].append(mean_episode_reward)
# Statistic["best_mean_episode_rewards"].append(best_mean_episode_reward)
mean_rewards = stats['mean_episode_rewards']
best_mean_rewards = stats['mean_episode_rewards']
freq= 10000
iters = range(len(mean_rewards))

plt.figure(figsize=(20,10))
plt.xlabel('#iters')
plt.ylabel('reward')
plt.plot(iters, mean_rewards, label='mean_rewards')
plt.plot(iters, best_mean_rewards, label='best_mean_rewards')
plt.legend(loc='best')
plt.show()