import unittest
import csv

def read_txt(file_name="./output/top_cost_drug.txt"):
    '''Read from output for further testing'''
    with open(f'{file_name}', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                result= dict(zip(row, [[] for x in range(len(row))]))
                line_count += 1

            else:
                result['drug_name'].append(row[0])
                result['num_prescriber'].append(int(row[1]))
                result['total_cost'].append(int(row[2]))

                line_count += 1
    return result
def duplicate_location(l):
    '''This function gives a list of list of dupliecate locations'''
    def duplicates(item):
        return [i for i, x in enumerate(l) if x == item]
    return [duplicates(x) for x in set(l) if l.count(x) > 1]

def name_rank(l,n):
    '''This function checks if the names are ranked alphabetically where costs are the same'''
    locations = duplicate_location(l)
    for location in locations:
        alpha=[n[i][0] for i in location]
        if alpha!=sorted(alpha):
            return False
    return True

class Test_problem1(unittest.TestCase):
    def setUp(self):
        '''Set up the output to be tested'''
        self.results=read_txt()
        # l=[1,1,3,3,3,4]
        # n=['a','a','g','g','b','bs']
        # print(name_rank(l,n))
        # print(self.results['total_cost'])
    def test_drugunique(self):
        '''This test tests whether the drug name is unique'''
        self.assertEqual(len(set(self.results['drug_name'])),len(self.results['drug_name']),msg="Drug name not unique")
    #
    def test_costrank(self):
        '''This test tests whether the total costs are sorted correctly'''
        # a= self.results['total_cost']
        # b=sorted(self.results['total_cost'],reverse=True)
        flag = all(earlier >= later for earlier, later in zip(self.results['total_cost'], self.results['total_cost'][1:]))

        self.assertTrue(flag,msg="Total cost not sorted correctly")

    def test_namerank(self):
        '''This test tests when total costs are equal, if names are ranked alphabetically'''
        try:
            self.assertTrue(name_rank(self.results['total_cost'],self.results['drug_name']))
        except Exception as e:
            self.assertEqual(e,"When total costs are equal, names are not ranked alphabetically")
if __name__ == '__main__':
    unittest.main()

