import json

TIMES_PROPERTY = "times"
STEP_PROPERTY = "step"
ID_PROPERTY = "id"
FATHER_PROPERTY = 'father'
ORDER_OF_FIELDS_PROPERTY = "orderOfFields"

class FileCluster:
    def __init__(self, filenames):
        self.filenames = filenames

    def read_file(self, file_name):
        with open(file_name) as json_file:
            return json.load(json_file)

    def cluster_files(self):
        results = []
        for file_name in self.filenames:
            file_name = './testcases/' + file_name
            data = self.read_file(file_name)
            map_result = self.convert_order_to_map(data)
            results = self.merge(results, map_result)

        return results

    def convert_order_to_map(self, order_data):
        map_result = []
        for data in order_data[ORDER_OF_FIELDS_PROPERTY]:
            id = data[ID_PROPERTY]
            step = data[STEP_PROPERTY]
            if FATHER_PROPERTY in data:
                father = data[FATHER_PROPERTY]
            else:
                father = "no_father_provided"
            known_field = self.find_field_by_id(id, map_result)

            if known_field is not None:
                index = map_result.index(known_field)
                map_result[index][TIMES_PROPERTY] += 1
                map_result[index][STEP_PROPERTY] = int((map_result[index][STEP_PROPERTY] + step) / 2)
            else:
                result = {ID_PROPERTY: id, TIMES_PROPERTY: 1, STEP_PROPERTY: step, FATHER_PROPERTY: father}
                map_result.append(result)

        return map_result

    def find_field_by_id(self, id, array):
        for field in array:
            if field[ID_PROPERTY] == id:
                return field
        return None

    def merge(self, originals, new_items):
        for item in new_items:
            original_item = self.find_field_by_id(item[ID_PROPERTY], originals)
            if original_item is not None:
                index = originals.index(original_item)
                originals[index][TIMES_PROPERTY] += item[TIMES_PROPERTY]
                originals[index][STEP_PROPERTY] = int((originals[index][STEP_PROPERTY] + item[STEP_PROPERTY]) / 2)
            else:
                originals.append(item)
        return originals