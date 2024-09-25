import seaborn as sns

ENVIRONMENTS_MAP = {
    "MOHopperDR-v5": [
        "MOHopperDefault-v5",
        "MOHopperLight-v5",
        "MOHopperHeavy-v5",
        "MOHopperSlippery-v5",
        "MOHopperLowDamping-v5",
        "MOHopperHard-v5"
    ],
    "MOHalfCheetahDR-v5": [
        "MOHalfCheetahDefault-v5",
        "MOHalfCheetahLight-v5",
        "MOHalfCheetahHeavy-v5",
        "MOHalfCheetahSlippery-v5",
        "MOHalfCheetahHard-v5"
    ],
    "MOHumanoidDR-v5": [
        "MOHumanoidDefault-v5",
        "MOHumanoidLight-v5",
        "MOHumanoidHeavy-v5",
        "MOHumanoidLowDamping-v5",
        "MOHumanoidHard-v5"
    ],
    "MOLunarLanderDR-v0": [
        "MOLunarLanderDefault-v0",
        "MOLunarLanderHighGravity-v0",
        "MOLunarLanderWindy-v0",
        "MOLunarLanderTurbulent-v0",
        "MOLunarLanderHard-v0",
        "MOLunarLanderLowMainEngine-v0",
        "MOLunarLanderStartLow-v0",
        "MOLunarLanderStartRight-v0",
    ],
}

CONTINUOUS_ALGORITHMS = [
    'MORL-D(MOSAC)-SB+PSA', 
    'MORL-D(MOSAC)-SB', 
    'GPI-PD Continuous Action', 
    'GPI-LS Continuous Action', 
    'PGMORL', 
    'CAPQL', 
    'PCN continuous action',
    'SAC Continuous Action',
]

DISCRETE_ALGORITHMS = [
    'MORL-D(MOSACDiscrete)-SB+PSA', 
    'MORL-D(MOSACDiscrete)-SB', 
    'GPI-PD', 
    'GPI-LS', 
    'Envelope',
    'PCN',
    'SAC Discrete Action',
]

PIXEL_ALGORITHMS = [
    'GPI-LS', 
    'Envelope',
    'PCN',
    'SAC Discrete Action',
]

ENVIRONMENT_TO_ALGORITHMS_MAP = {
    'MOHopperDR-v5': CONTINUOUS_ALGORITHMS,
    'MOHalfCheetahDR-v5': CONTINUOUS_ALGORITHMS,
    'MOHumanoidDR-v5': CONTINUOUS_ALGORITHMS,
    'MOLunarLanderDR-v0': DISCRETE_ALGORITHMS,
    'MOLavaGrid-v0': DISCRETE_ALGORITHMS,
    'MOSuperMarioBrosZeroShot-v2': PIXEL_ALGORITHMS,
}

ALGORITHMS_NAME_MAP = {
    'PCN continuous action': 'PCN',
    'PGMORL': 'PGMORL',
    'CAPQL': 'CAPQL',
    'GPI-LS Continuous Action': 'GPI-LS',
    'GPI-PD Continuous Action': 'GPI-PD',
    'MORL-D(MOSAC)-SB': 'MORL-D(SB)',
    'MORL-D(MOSAC)-SB+PSA': 'MORL-D(SB+PSA)',
    'SAC Continuous Action': 'SAC',
    'SAC Discrete Action': 'SAC',
    'GPI-LS': 'GPI-LS',
    'GPI-PD': 'GPI-PD',
    'MORL-D(MOSACDiscrete)-SB': 'MORL-D(SB)',
    'MORL-D(MOSACDiscrete)-SB+PSA': 'MORL-D(SB+PSA)',
    'PCN': 'PCN',
    'Envelope': 'Envelope',
}

colors = sns.color_palette('colorblind')
ALGORITHMS_COLOR_MAP = {
    'CAPQL': colors[1],
    'GPI-LS': colors[3],
    'GPI-PD': colors[4],
    'MORL-D(SB)': colors[5],
    'MORL-D(SB+PSA)': colors[0],
    'PGMORL': colors[2],
    'PCN': colors[8],
    'SAC': colors[7],
    'Envelope': colors[6],
}

def get_algorithms(env_name):
    return ENVIRONMENT_TO_ALGORITHMS_MAP[env_name]