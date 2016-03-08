from django.core.urlresolvers import reverse

from api.models import PlanetaryData
from api.tests.utils import KrakSatAPITestCase


class PlanetaryDataTests(KrakSatAPITestCase):
    """Tests for /sht API endpoint"""

    list_url = reverse('planetarydata-list')
    model = PlanetaryData
    valid_data = {
        'timestamp': KrakSatAPITestCase.TIMESTAMP,
        'mass': 5.97237e24,
        'radius': 6371,
        'escape_velocity': 11.186,
        'average_density': 5.514,
        'earth_similarity_index': 1,
        'avg_atm_molar_mass': 28.97,
        'adiabatic_index': 1.403,
        'atmosphere_density': 1.2922,
        'avg_molecule_mass': 2.992e-23,
        'specific_gas_const': 287.058,
        'refractive_index': 1.0002772,
        'molar_refractivity': 4.143e-6,
        'atm_speed_of_light': 299709.378
    }

    def test_create(self):
        """Ensure we can create a new SHT object"""
        self._test_create()

    def test_invalid_params(self):
        """Ensure sending invalid parameters to /sht returns error 400"""
        self._test_invalid_params(
            ('Invalid timestamp', {'timestamp': 'foobar'}),
            ('Invalid mass', {'mass': 'foobar'}),
            ('mass < 0', {'mass': -0.001}),
            ('Invalid radius', {'radius': 'foobar'}),
            ('radius < 0', {'radius': -0.001}),
            ('Invalid escape velocity', {'escape_velocity': 'foobar'}),
            ('escape velocity < 0', {'escape_velocity': -0.001}),
            ('Invalid average density', {'average_density': 'foobar'}),
            ('average density < 0', {'average_density': -0.001}),
            ('Invalid ESI', {'earth_similarity_index': 'foobar'}),
            ('ESI < 0', {'earth_similarity_index': -0.001}),
            ('ESI > 1', {'earth_similarity_index': 1.001}),
            ('Invalid atm. molar mass', {'avg_atm_molar_mass': 'foobar'}),
            ('atm. molar mass < 0', {'avg_atm_molar_mass': -0.001}),
            ('Invalid adiabatic index', {'adiabatic_index': 'foobar'}),
            ('adiabatic index < 1', {'adiabatic_index': 0.999}),
            ('Invalid atm. density', {'atmosphere_density': 'foobar'}),
            ('atm. density < 0', {'atmosphere_density': -0.001}),
            ('Invalid average molecule mass', {'avg_molecule_mass': 'foobar'}),
            ('average molecule mass < 0', {'avg_molecule_mass': -0.001}),
            ('Invalid specific gas const.', {'specific_gas_const': 'foobar'}),
            ('specific gas const. < 0', {'specific_gas_const': -0.001}),
            ('Invalid refractive index', {'refractive_index': 'foobar'}),
            ('refractive index < 1', {'refractive_index': 0.999}),
            ('Invalid molar refractivity', {'molar_refractivity': 'foobar'}),
            ('molar refractivity < 0', {'molar_refractivity': -0.001}),
            ('Invalid atm. speed of light', {'atm_speed_of_light': 'foobar'}),
            ('atm. speed of light < 0', {'atm_speed_of_light': -0.001})
        )
