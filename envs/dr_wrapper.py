import gymnasium as gym

class DRWrapper(gym.Wrapper, gym.utils.RecordConstructorArgs):
    """Wrapper for DR environment."""

    def __init__(self, env: gym.Env):
        """Initialize the :class:`DRWrapper` wrapper with an environment and a transform function :attr:`f`.

        Args:
            env: The environment to apply the wrapper
            f: A function that transforms the observation
        """
        gym.utils.RecordConstructorArgs.__init__(self)
        gym.Wrapper.__init__(self, env)

    def reset(self, *, seed=None, options=None):
        self.env.unwrapped.reset_random() # domain randomization
        
        return self.env.reset(seed=seed, options=options) 