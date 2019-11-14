from flask import request
from itertools import combinations
from flask_restful import Resource

class Identifier(Resource):
    from flask import jsonify

    def get(self):
        return {"message" : "hello,world"}


    def post(self):
        data = request.get_json()
        if not data:
            return {"message" : "No input data provided"}, 400
        ps = processing(data).calc()
        return ps




class processing:

    def __init__(self, data={}):
        self.data = data

    def calc(self):
        from flask import jsonify
        print(self.data['Lines'])


        #Processing str from request
        ls = []
        for i in self.data['Lines']:
            ls.append(i.split(', '))

        #Create list of vetrice
        nls = []
        for x in ls:
            for item in x:
                nls.append(item)
        print(nls)

        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        #Shape identifier
        length_list = len(nls)
        comls = []
        while length_list >= 3:
            counting = length_list
            comls.append(combinations(nls, counting))

            counting -= 1
            length_list -= 1

        new_dict = {}
        list_dict = []
        for c in comls:
            for item in c:
                if len(item) == 20:
                    new_dict['name'] = "Icosagon"
                    new_dict['Vertices'] = item
                    list_dict.append(new_dict.copy())
                elif len(item) == 19:
                    new_dict['name'] = "Enneadecagon"
                    new_dict['Vertices'] = item
                    list_dict.append(new_dict.copy())
                elif len(item) == 18:
                    new_dict['name'] = "Octadecagon"
                    new_dict['Vertices'] = item
                    list_dict.append(new_dict.copy())
                elif len(item) == 17:
                    new_dict['name'] = "Heptadecagon"
                    new_dict['Vertices'] = item
                    list_dict.append(new_dict.copy())
                elif len(item) == 16:
                    new_dict['name'] = "Hexadecagon"
                    new_dict['Vertices'] = item
                    list_dict.append(new_dict.copy())
                elif len(item) == 15:
                    new_dict['name'] = "Pentadecagon"
                    new_dict['Vertices'] = item
                    list_dict.append(new_dict.copy())
                elif len(item) == 14:
                    new_dict['name'] = "Tetradecagon"
                    new_dict['Vertices'] = item
                    list_dict.append(new_dict.copy())
                elif len(item) == 13:
                    new_dict['name'] = "Tridecagon"
                    new_dict['Vertices'] = item
                    list_dict.append(new_dict.copy())
                elif len(item) == 12:
                    new_dict['name'] = "Dodecagon"
                    new_dict['Vertices'] = item
                    list_dict.append(new_dict.copy())
                elif len(item) == 11:
                    new_dict['name'] = "Hendecagon"
                    new_dict['Vertices'] = item
                    list_dict.append(new_dict.copy())
                elif len(item) == 10:
                    new_dict['name'] = "Decagon"
                    new_dict['Vertices'] = item
                    list_dict.append(new_dict.copy())
                elif len(item) == 9:
                    new_dict['name'] = "Nonagon"
                    new_dict['Vertices'] = item
                    list_dict.append(new_dict.copy())
                elif len(item) == 8:
                    new_dict['name'] = "Octagon"
                    new_dict['Vertices'] = item
                    list_dict.append(new_dict.copy())
                elif len(item) == 7:
                    new_dict['name'] = "Heptagon"
                    new_dict['Vertices'] = item
                    list_dict.append(new_dict.copy())
                elif len(item) == 6:
                    new_dict['name'] = "Hexagon"
                    new_dict['Vertices'] = item
                    list_dict.append(new_dict.copy())
                    continue
                elif len(item) == 5:
                    new_dict['name'] = "Pentagon"
                    new_dict['Vertices'] = item
                    #print(new_dict)
                    list_dict.append(new_dict.copy())
                    continue
                elif len(item) == 4:
                    new_dict['name'] = "Quadrilateral"
                    new_dict['Vertices'] = item
                    #print(new_dict)
                    list_dict.append(new_dict.copy())
                    continue
                elif len(item) == 3:
                    new_dict['name'] = "Triangle"
                    new_dict['Vertices'] = item
                    list_dict.append(new_dict.copy())
                    #print(new_dict)
                else:
                    print(item)

        final_res = {"shape" : list_dict}
        return final_res



