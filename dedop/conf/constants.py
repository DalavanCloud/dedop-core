from .constants_reader import *


class ConstantsFile(ConstantsFileReader):
    """
    class for loading the Constants file
    """

    @property
    def c(self) -> float:
        """Speed of light"""
        return self["c_cst"]

    @property
    def semi_major_axis(self) -> float:
        """Semi-major axis of WGS84 ellipsoid"""
        return self["semi_major_axis_cst"]

    @property
    def earth_radius(self) -> float:
        """Earth Radius"""
        return self["earth_radius_cst"]

    @property
    def sec_in_day(self) -> float:
        """Number of seconds in a day"""
        return self["sec_in_day_cst"]

    @property
    def pi(self) -> float:
        """Pi number"""
        return self["pi_cst"]

    @property
    def flat_coeff(self) -> float:
        """Flattening coefficient of WGS84 ellipsoid"""
        return self["flat_coeff_cst"]

    @property
    def semi_minor_axis(self) -> float:
        """Semi-minor axis of WGS84 ellipsoid"""
        return self["semi_minor_axis_cst"]