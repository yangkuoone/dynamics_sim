__author__ = 'elubin'

from dynamics_sim.payoff_matrix import PayoffMatrix

UNCLASSIFIED_EQUILIBRIUM = 'Unclassified'


class Game(object):
    DEFAULT_PARAMS = {}
    PLAYER_LABELS = None
    STRATEGY_LABELS = None

    def __init__(self, payoff_matrices, player_frequencies, equilibrium_tolerance=None):
        assert payoff_matrices is not None
        assert player_frequencies is not None
        if self.PLAYER_LABELS is not None:
            assert len(player_frequencies) == len(self.PLAYER_LABELS)

        self.pm = PayoffMatrix(len(player_frequencies), payoff_matrices)
        if self.STRATEGY_LABELS is not None:
            for labels_i, num_strats  in zip(self.STRATEGY_LABELS, self.pm.num_strats):
                assert len(labels_i) == num_strats

        self.player_frequencies = player_frequencies
        self.equilibrium_tolerance = equilibrium_tolerance

    # TODO @staticmethod
    def classify(self, params, state, tolerance):
        # state is an array of numpy arrays, one for every player type, function should be overriden if you
        # want the game to support classification of equilibria. The function has
        # params is a dictionary with all of the parameters for the game
        # i.e. params['a'] will return whatever parameter the
        return UNCLASSIFIED_EQUILIBRIUM



