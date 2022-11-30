from pathlib import Path


ROOT = Path('.').resolve()
DATA_ROOT = ROOT / 'data'

class Datasets:
    DEPENDENCIES_TXT = DATA_ROOT / 'dependencies.txt'
    OVERSIZED_TSV = DATA_ROOT / 'oversized.tsv'
    PRIZE_WEIGHT_TSV = DATA_ROOT / 'prize-weight.tsv'
    PRIZE_WEIGHT_VOLUME_TSV = DATA_ROOT / 'prize-weight-volume.tsv'
