import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'shared'))
from kira_bioelectric_generator import generate_bioelectric_scenario
from kreagriculture import PlantVeritas
import numpy as np

csv, x, y = generate_bioelectric_scenario(scenario='depolarization')
pv = PlantVeritas(csv, sampling_hz=100)
pv.cell_x = x
pv.cell_y = y

print("--- kreagriculture results ---")
print("Apoplastic pH (mean):", np.mean(pv.compute_apoplastic_ph(np.mean(pv.vmem, axis=1))))
print("Stomatal closure score:", pv.detect_stomatal_closure())
print("Drought stress score (0-1):", pv.detect_drought_stress())
print("Nutrient deficiency score (0-1):", pv.detect_nutrient_deficiency())
print("Root stress score (0-1):", pv.detect_root_stress())
