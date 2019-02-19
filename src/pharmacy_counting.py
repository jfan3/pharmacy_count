import sys
import os
import csv


class Drugbook:
    class Drug:
        def __init__(self, name):
            self.name = name.upper()
            self.costs = 0
            self.prescriptions = dict()

        def add_prescription(self, prescription):
            self.prescriptions[prescription.person] = self.prescriptions.get(prescription.person,
                                                                             0) + prescription.drug_cost
            self.costs+=prescription.drug_cost

        def __lt__(self, other):
            return self.costs>other.costs or ((self.costs==other.costs )and (self.name<other.name))
        def __repr__(self):
            return f"{self.name}: {self.costs}"
    def __init__(self):
        self.drugs = dict()

    def add_prescription(self,prescription):
        self.drugs[prescription.drug_name]=self.drugs.get(prescription.drug_name,self.Drug(prescription.drug_name))
        self.drugs[prescription.drug_name].add_prescription(prescription)
    def sort(self):
        # self.drugs = dict(sorted(self.drugs.items(), key=lambda x: x[1]))
        # temp = list(self.drugs.values())
        # print(temp)
        # temp = sorted(temp)
        # print(temp)
        # new = dict()
        # for drug in temp:
        #     new[drug.name]=drug
        # self.drugs=new
        self.drugs = dict(sorted(self.drugs.items(), key=lambda x: (-x[1].costs, x[0])))
    def output(self, filename='../output/top_cost_drug.txt'):
        # temp = dict(sorted(self.drugs.items(), key=lambda x: (-x[1].costs, x[0])))
        self.sort()
        if not os.path.exists(filename[:9]):
            os.makedirs(filename[:9])
        with open(filename,'w') as out:
            out.write(",".join(['drug_name','num_prescriber','total_cost']) + '\n')
            for name in self.drugs:
                prescribers = self.drugs[name].prescriptions.keys()
                total_cost = self.drugs[name].costs
                # print(",".join([name,str(len(prescribers)),str(total_cost)]))
                out.write(",".join([name,str(len(prescribers)),str(int(total_cost))])+ '\n')

    def __repr__(self):

        # temp_string=""
        # for name in self.drugs:
        #     temp_string+= name+"\n"
        #     temp_string += str(self.drugs[name].prescriptions)+"\n"
        #     temp_string += "total costs "+str( self.drugs[name].costs)+ "\n"
        # return temp_string
        return (str(self.drugs.items()))
    def populate(self, filename="../input/itcont.txt"):
        script_dir = os.path.dirname(__file__)
        with open(f'{filename}','r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    pass
                else:
                    prep = Prescription(int(row[0]), row[1], row[2], row[3], int(float(row[4])))
                    self.add_prescription(prep)

class Prescription:
    def __init__(self, id, last_name,first_name, drug_name,drug_cost):
        self.drug_name = drug_name
        self.drug_cost = drug_cost
        self.person = (first_name.capitalize(),last_name.capitalize())



if __name__ == "__main__":
    db = Drugbook()
    db.populate(filename=sys.argv[1])
    # print(db)
    # db.populate()
    # db.output()
    db.output(filename=sys.argv[2])