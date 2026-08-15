import sys
sys.path.append(r'C:\Users\joels\Projects\kira-agriculture\shared')
from veritas_bioelectric_adapter import BioelectricVeritas
import numpy as np

class PlantVeritas(BioelectricVeritas):
    def compute_apoplastic_ph(self, vmem):
        pH = 5.5 + (vmem - (-120)) / (-80) * 2.0
        return np.clip(pH, 5.0, 8.0)
    
    def detect_stomatal_closure(self):
        wnci = self.run_wnci_on_each_node()
        grad = self.compute_spatial_gradient(self.cell_x, self.cell_y)
        return np.mean(wnci) * 0.6 + (grad.mean() / 1e6) * 0.4

    def detect_drought_stress(self):
        # Drought: hyperpolarized Vmem (< -100mV) + high spatial entropy (uncoupling)
        mean_v = np.mean(self.vmem, axis=1)[-1]
        H = self.compute_spatial_entropy()[-1]
        score = ( (mean_v < -100) * 0.5 + (H > 3.0) * 0.5 )
        return float(np.clip(score, 0, 1))

    def detect_nutrient_deficiency(self):
        # Nutrient deficiency: apoplastic pH drops (< 5.0) + high gradient
        mean_ph = np.mean(self.compute_apoplastic_ph(np.mean(self.vmem, axis=1)))
        grad = self.compute_spatial_gradient(self.cell_x, self.cell_y)[-1]
        score = ( (mean_ph < 5.0) * 0.6 + (grad.mean() / 1e6 > 0.5) * 0.4 )
        return float(np.clip(score, 0, 1))

if __name__ == "__main__":
    print("kreagriculture module ready (expanded with drought & nutrients).")
