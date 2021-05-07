import sciunit
import numpy
from capabilities import *
from tscore import StudentsTestScore

class MaxFacilitationRatio(sciunit.Test):
    """ 
    Compare the ratio of mean maximum facilitation radii at 
    high and low contrasts in V1 layers
    with mean ratios from literature
    layers : {'4', '2/3'}
    """
    known_layers = {"V1_L4", "V1_L2/3", "all"}
    score_type = StudentsTestScore

    def __init__(self, layer, contrasts,
                observation={'mean':None},
                name="Max Facilitation Ratio"):
        assert layer in self.known_layers, "Layer %s not found in layer names known to the test: %s" % (layer, self.known_layers)
        assert len(contrasts) == 2, "The contrasts list should contain 2 and only 2 contrast values"
        self.required_capabilities += (ReceivesDriftingSinusoidalGratingDiskStimulation,
                                       ProducesMaxFacilitationRadius)
        self.layer = layer
        self.contrasts = contrasts
        sciunit.Test.__init__(self, observation, name) 

    def validate_observation(self, observation):
        try:
            assert len(observation.keys()) == 1
            for key, val in observation.items():
                assert key in ["mean"]
                assert (isinstance(val, int) or isinstance(val, float))
        except Exception:
            raise sciunit.errors.ObservationError(
                ("Observation must return a dictionary of the form:"
                 "{'mean': NUM1}"))

    def generate_prediction(self, model):
        model.present_drifting_sinusoidal_grating_disk(
        num_sizes=10,
        max_size=5,
        log_spacing=False,
        orientation=0,
        spatial_frequency=0.8,
        temporal_frequency=2,
        grating_duration=490,
        contrasts=self.contrasts,
        num_trials=10)

        low_contrast_mfr = model.get_max_facilitation_radii(self.layer, min(self.contrasts))
        high_contrast_mfr = model.get_max_facilitation_radii(self.layer, max(self.contrasts)) 
        ratio_mfr = numpy.array(low_contrast_mfr)/numpy.array(high_contrast_mfr)
        mean_ratio_mfr = numpy.mean(ratio_mfr)
        std_ratio_mfr = numpy.std(ratio_mfr, ddof = 1)
        return {'mean': mean_ratio_mfr, 'std': std_ratio_mfr, 'n': len(low_contrast_mfr)}

    def compute_score(self, observation, prediction):
        return StudentsTestScore.compute(observation,prediction)