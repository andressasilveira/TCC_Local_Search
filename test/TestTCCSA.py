import unittest

from SimulatedAnneling import SimulatedAnneling


simulatedAnneling = SimulatedAnneling(10, 6, 1, 1, 1, 1, 1)

class FieldTest(unittest.TestCase):

    def test_placeToSwap(self):
        array = [0, 1, 2, 3, 4]
        self.assertTrue(simulatedAnneling.get_place_to_swap(array, 5, True) == 0, 'Review the entry. Should be 0 for Right')
        self.assertTrue(simulatedAnneling.get_place_to_swap(array, 0, False) == 4, 'Review the entry. Should be 5 for Left')
        self.assertTrue(simulatedAnneling.get_place_to_swap(array, 4, True) == 4, 'Review the entry. Should be 5 for Right')

    def test_swapItself(self):
        array = [0, 1, 2, 3, 4]
        self.assertTrue(simulatedAnneling.swap(array, 5, True) == [4, 1, 2, 3, 0], 'Review the entry. Should be [4,1,2,3,0] for Right')
        self.assertTrue(simulatedAnneling.swap(array, 3, True) == [0, 1, 2, 4, 3],
                        'Review the entry. Should be [0, 1, 2, 4, 3] for Right')
        self.assertTrue(simulatedAnneling.swap(array, 0, False) == [4, 1, 2, 3, 0], 'Review the entry. Should be [4,1,2,3,0] for Left')

    def test_value(self):
        # considerando 10 usuários
        field1 = {"times": 8, "step": 4}
        field2 = {"times": 7, "step": 3}
        field3 = {"times": 8, "step": 1}
        field4 = {"times": 2, "step": 2}
        field5 = {"times": 1, "step": 5}

        simulatedAnnelingValue = SimulatedAnneling(10, 6, 1, 1, 1, 1, 1)

        self.assertEqual(simulatedAnnelingValue.value([field1, field2, field3, field4, field5]), 6, 'Not equal')
        self.assertEqual(simulatedAnnelingValue.value([field5, field4, field3, field1, field2]), 12, 'Not equal')

    def test_case1(self):
        fields = [{'id': 4, 'times': 3, 'step': 4},
                  {'id': 11, 'times': 3, 'step': 8},
                  {'id': 1, 'times': 6, 'step': 3},
                  {'id': 2, 'times': 6, 'step': 5},
                  {'id': 5, 'times': 3, 'step': 5},
                  {'id': 3, 'times': 3, 'step': 2}]

        simulatedAnnelingValue = SimulatedAnneling(10, 6, 1, 1, 1, 1, 1)
        self.assertEqual(6, simulatedAnnelingValue.value(fields))

    def test_original_value(self):
        fields = [{'id': 'OrderType', 'times': 10, 'step': 1},
                  {'id': 'SalesOrg', 'times': 10, 'step': 2},
                  {'id': 'DistChannel', 'times': 10, 'step': 3},
                  {'id': 'Division', 'times': 10, 'step': 4},
                  {'id': 'Enter', 'times': 11, 'step': 5},
                  {'id': 'SoldToParty', 'times': 9, 'step': 6},
                  {'id': 'Material', 'times': 9, 'step': 7},
                  {'id': 'OrderQtd', 'times': 9, 'step': 8},
                  {'id': 'Unity', 'times': 2, 'step': 9},
                  {'id': 'ItemCat', 'times': 2, 'step': 10},
                  {'id': 'Plnt', 'times': 6, 'step': 12},
                  {'id': 'ItmCheckBox', 'times': 2, 'step': 12},
                  {'id': 'DetailButton', 'times': 2, 'step': 13},
                  {'id': 'ShippingTab', 'times': 3, 'step': 13},
                  {'id': 'CountryTab', 'times': 9, 'step': 12},
                  {'id': 'TaxCode', 'times': 8, 'step': 13},
                  {'id': 'CFOP', 'times': 8, 'step': 14},
                  {'id': 'SaveBtn', 'times': 10, 'step': 16},
                  {'id': 'CreateWRefBtn', 'times': 1, 'step': 5},
                  {'id': 'BillingDoc', 'times': 1, 'step': 6},
                  {'id': 'HeaderBtn', 'times': 1, 'step': 8},
                  {'id': 'OrderReason', 'times': 1, 'step': 9},
                  {'id': 'BackBtn', 'times': 1, 'step': 10},
                  {'id': 'ItemDClick', 'times': 7, 'step': 10},
                  {'id': 'PONum', 'times': 7, 'step': 7}, {'id': 'ICMSTxt', 'times': 3, 'step': 16},
                  {'id': 'IPITxt', 'times': 3, 'step': 17}, {'id': 'LawCOFINS', 'times': 3, 'step': 18},
                  {'id': 'LawPIS', 'times': 3, 'step': 19}, {'id': 'CondTab', 'times': 3, 'step': 17},
                  {'id': 'CnType', 'times': 3, 'step': 18}, {'id': 'Amount', 'times': 3, 'step': 19}]
        simulatedAnnelingValue = SimulatedAnneling(10, 32, 1, 1, 1, 1, 1)
        self.assertEqual(196, simulatedAnnelingValue.value(fields))

    def test_imaginative_scenario(self):
        fields = [{'id': 'OrderType', 'times': 4, 'step': 1},
                  {'id': 'SalesOrg', 'times': 10, 'step': 2},
                  {'id': 'DistChannel', 'times': 10, 'step': 3},
                  {'id': 'Division', 'times': 10, 'step': 4},
                  {'id': 'Enter', 'times': 11, 'step': 5},
                  {'id': 'SoldToParty', 'times': 9, 'step': 6},
                  {'id': 'Material', 'times': 9, 'step': 7},
                  {'id': 'OrderQtd', 'times': 9, 'step': 8},
                  {'id': 'Unity', 'times': 2, 'step': 9},
                  {'id': 'ItemCat', 'times': 2, 'step': 10},
                  {'id': 'Plnt', 'times': 6, 'step': 12},
                  {'id': 'ItmCheckBox', 'times': 2, 'step': 12},
                  {'id': 'DetailButton', 'times': 2, 'step': 13},
                  {'id': 'ShippingTab', 'times': 3, 'step': 13},
                  {'id': 'CountryTab', 'times': 9, 'step': 12},
                  {'id': 'TaxCode', 'times': 8, 'step': 13},
                  {'id': 'CFOP', 'times': 8, 'step': 14},
                  {'id': 'SaveBtn', 'times': 10, 'step': 16},
                  {'id': 'CreateWRefBtn', 'times': 1, 'step': 5},
                  {'id': 'BillingDoc', 'times': 1, 'step': 6},
                  {'id': 'HeaderBtn', 'times': 1, 'step': 8},
                  {'id': 'OrderReason', 'times': 1, 'step': 9},
                  {'id': 'BackBtn', 'times': 1, 'step': 10},
                  {'id': 'ItemDClick', 'times': 7, 'step': 10},
                  {'id': 'PONum', 'times': 7, 'step': 7}, {'id': 'ICMSTxt', 'times': 3, 'step': 16},
                  {'id': 'IPITxt', 'times': 3, 'step': 17}, {'id': 'LawCOFINS', 'times': 3, 'step': 18},
                  {'id': 'LawPIS', 'times': 3, 'step': 19}, {'id': 'CondTab', 'times': 3, 'step': 17},
                  {'id': 'CnType', 'times': 3, 'step': 18}, {'id': 'Amount', 'times': 3, 'step': 19}]
        simulatedAnnelingValue = SimulatedAnneling(10, 32, 1, 1, 1, 1, 1)
        self.assertEqual(166, simulatedAnnelingValue.value(fields))


    def test_wrong_scenario(self):
        fields = [{'id': 'Division', 'times': 10, 'step': 4},
                  {'id': 'ShippingTab', 'times': 3, 'step': 13},
                  {'id': 'DistChannel', 'times': 10, 'step': 3},
                  {'id': 'CnType', 'times': 3, 'step': 18},
                  {'id': 'Enter', 'times': 11, 'step': 5},
                  {'id': 'CountryTab', 'times': 9, 'step': 12},
                  {'id': 'CFOP', 'times': 8, 'step': 14},
                  {'id': 'Material', 'times': 9, 'step': 7},
                  {'id': 'LawCOFINS', 'times': 3, 'step': 18},
                  {'id': 'SoldToParty', 'times': 9, 'step': 6},
                  {'id': 'IPITxt', 'times': 3, 'step': 17},
                  {'id': 'ICMSTxt', 'times': 3, 'step': 16},
                  {'id': 'OrderQtd', 'times': 9, 'step': 8},
                  {'id': 'Amount', 'times': 3, 'step': 19},
                  {'id': 'SaveBtn', 'times': 10, 'step': 16},
                  {'id': 'SalesOrg', 'times': 10, 'step': 2},
                  {'id': 'ItemDClick', 'times': 7, 'step': 10},
                  {'id': 'PONum', 'times': 7, 'step': 7},
                  {'id': 'HeaderBtn', 'times': 1, 'step': 8},
                  {'id': 'ItmCheckBox', 'times': 2, 'step': 12},
                  {'id': 'LawPIS', 'times': 3, 'step': 19},
                  {'id': 'CondTab', 'times': 3, 'step': 17},
                  {'id': 'OrderType', 'times': 10, 'step': 1},
                  {'id': 'Plnt', 'times': 6, 'step': 12},
                  {'id': 'TaxCode', 'times': 8, 'step': 13},
                  {'id': 'ItemCat', 'times': 2, 'step': 10},
                  {'id': 'BillingDoc', 'times': 1, 'step': 6},
                  {'id': 'CreateWRefBtn', 'times': 1, 'step': 5},
                  {'id': 'OrderReason', 'times': 1, 'step': 9},
                  {'id': 'BackBtn', 'times': 1, 'step': 10}, {'id': 'Unity', 'times': 2, 'step': 9}, {'id': 'DetailButton', 'times': 2, 'step': 13}]
        simulatedAnnelingValue = SimulatedAnneling(10, 32, 1, 1, 1, 1, 1)
        self.assertEqual(166, simulatedAnnelingValue.value(fields))

if __name__ == "__main__":
    unittest.main()
