from wechat.base_api import BaseApi


class Department(BaseApi):

    def create(self, data=None):
        data = self.get_data("../steps/department.yaml", data)
        return self.send(data)

    def update(self, data=None):
        data = self.get_data("../steps/department.yaml", data)
        return self.send(data)

    def delete(self, data):
        data = self.get_data("../steps/department.yaml", data)
        return self.send(data)

    def list(self, ID=None):
        data = self.get_data("../steps/department.yaml", ID)
        return self.send(data)

    def find_departments_by_parentid(self, parentID):
        deps = []

        departments = self.list()["department"]
        for depatment in departments:
            if depatment["parentid"] == parentID:
                deps.append(depatment)
        return deps

    def is_exist_name(self, parentID, name):
        deps = self.find_departments_by_parentid(parentID)

        for dep in deps:
            if dep["name"] == name:
                return dep["id"]
        return 0

    def is_exist_id(self, id):
        departments = self.list()["department"]
        for depatment in departments:
            if depatment["id"] == id:
                return True
        return False
