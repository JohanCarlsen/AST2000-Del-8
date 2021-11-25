'''
EGEN KODE
'''
import ast2000tools.utils as utils
from ast2000tools.relativity import RelativityExperiments

seed = utils.get_seed('antonabr')
experiments = RelativityExperiments(seed)

experiments.spaceship_duel(6, write_solutions=True)
