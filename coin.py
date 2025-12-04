import random

class Coin:
    def __init__(self, p_heads: float = 0.5, heads_value: int = 1, tails_value: int = -1):
        """
        A coin with:
        - p_heads: probability of landing on heads
        - heads_value: value added if heads occurs
        - tails_value: value added if tails occurs
        """
        if not 0 <= p_heads <= 1:
            raise ValueError("p_heads must be between 0 and 1")

        self.p_heads = p_heads
        self.heads_value = heads_value
        self.tails_value = tails_value

    def flip(self) -> int:
        """
        Flip the coin and return its value.

        :return: heads_value or tails_value (int)
        """ 
        if random.random() < self.p_heads:
            return self.heads_value
        else:
            return self.tails_value
