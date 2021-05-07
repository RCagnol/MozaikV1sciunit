import sciunit

class ReceivesDriftingSinusoidalGratingDiskStimulation(sciunit.Capability):
    """ 
    """

    def present_drifting_sinusoidal_grating_disk(
        self,
        num_sizes,
        max_size,
        log_spacing,
        orientation,
        spatial_frequency,
        temporal_frequency,
        grating_duration,
        contrasts,
        num_trials,
        ):
        """
        num_sizes
        max_size
        log_spacing
        orientation
        spatial_frequency
        temporal_frequency
        grating_duration
        contrasts
        num_trials
        """
        raise NotImplementedError()

class ProducesMaxFacilitationRadius(sciunit.Capability):
    """ 
    """
    def get_max_facilitation_radii(self, layer, contrast):
        """
        Get the Maximum facilitation radius of the neurons of the model
        """
        raise NotImplementedError()