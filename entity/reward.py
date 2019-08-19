from gym_fourrooms.envs.shaping_reward import ShapingRewardBase


class ShapingReward(ShapingRewardBase):
    def __init__(self, value, gamma, subgoals):
        super(ShapingReward, self).__init__()
        self.value = value
        self.gamma = gamma
        self.subgoals = subgoals

    def perform(self, state, next_state):
        phi = 0
        phi_dash = 0
        if state in self.subgoals:
            phi = self.value
        if next_state in self.subgoals:
            phi_dash = self.value
        return self.gamma*phi_dash - phi
