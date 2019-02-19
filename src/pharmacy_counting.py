import sys
import os
import csv

class Drugbook:
    '''
    The Drugbook class is an aggregate of Drugs
    '''
    class Drug:
        '''The Drug class is a subclass of Drugbook class. It keeps tracks of all the prescriptions taken place,
        down to the individual level, and the total costs'''
        def __init__(self, name):
            '''Initializing drug names to be all capital, total costs to be 0, and empty prescriptoins.'''
            self.name = name.upper()
            self.costs = 0
            self.prescriptions = dict()

        def add_prescription(self, prescription):
            '''Add prescription identifiable by person (lastname and firstname). Keeps track of total costs.'''
            self.prescriptions[prescription.person] = self.prescriptions.get(prescription.person,
                                                                             0) + prescription.drug_cost
            self.costs+=prescription.drug_cost

        def __lt__(self, other):
            '''Comparing drug objects. A drug is considered to be greater if it has higher costs and lower alphabetical name'''
            if self.costs>other.costs:
                return True
            elif (self.costs==other.costs )and (self.name<other.name):
                return True
            else:
                return False

        def __repr__(self):
            '''Print name and costs of the drug'''
            return f"{self.name}: {self.costs}"
    def __init__(self):
        '''Create empty dictionary of drug. The key of the dictionary is the drug name and the value is the drug object'''
        self.drugs = dict()

    def add_prescription(self,prescription):
        '''Add prescription at the Drugbook level.'''
        self.drugs[prescription.drug_name]=self.drugs.get(prescription.drug_name,self.Drug(prescription.drug_name))
        self.drugs[prescription.drug_name].add_prescription(prescription)
    def sort(self):
        '''Sort the drugs in the drug book. '''
        self.drugs = dict(sorted(self.drugs.items(), key=lambda x: x[1]))

    def output(self, filename='../output/top_cost_drug.txt'):
        '''Write aggregate report as ouptput'''
        # temp = dict(sorted(self.drugs.items(), key=lambda x: (-x[1].costs, x[0])))
        self.sort()
        #If there is no directory for output make one
        if not os.path.exists(filename[:8]):
            os.makedirs(filename[:8])
        with open(filename,'w') as out:
            out.write(",".join(['drug_name','num_prescriber','total_cost']) + '\n')
            for name in self.drugs:
                prescribers = self.drugs[name].prescriptions.keys()
                total_cost = self.drugs[name].costs
                #casting total cost to integer to fit the standard provided
                out.write(",".join([name,str(len(prescribers)),str(int(total_cost))])+ '\n')

    def __repr__(self):
        '''String representation of drugbook for debugging'''
        temp_string=""
        for name in self.drugs:
            temp_string+= name+"\n"
            temp_string += str(self.drugs[name].prescriptions)+"\n"
            temp_string += "total costs "+str( self.drugs[name].costs)+ "\n"
        return temp_string
        return temp_string
    def populate(self, filename="../input/itcont.txt"):
        '''Populate the drugbook by intput'''
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
    '''The Prescription class keeps track of records from input.'''
    def __init__(self, id, last_name,first_name, drug_name,drug_cost):
        self.drug_name = drug_name
        self.drug_cost = drug_cost
        self.person = (first_name.capitalize(),last_name.capitalize())



if __name__ == "__main__":
    db = Drugbook()
    db.populate(filename=sys.argv[1])
    db.output(filename=sys.argv[2])