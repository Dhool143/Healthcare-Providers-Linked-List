

import unittest
from main import PatientNode, merge_patient_lists

     
def build_list(values):
    dummy = PatientNode(0)
    current = dummy
    
    for value in values:
        current.next = PatientNode(value)
        current = current.next
        
    return dummy.next



def to_list(head):
    result = []
    
    while head:
        result.append(head.ssn)
        head = head.next
        
        
    return result



class TestMergePatient_list(unittest.TestCase):
    
    
    # Normal case
    
    
    def  test_equal_lenght_lists(self):
        l1 = build_list([100, 300, 500])
        l2 = build_list([200, 400, 600])
        
        self.assertEqual(to_list(merge_patient_lists(l1, l2)),
               [100, 200, 300, 400, 500, 600] 
        )
      
      
    def test_different_lenght_lists(self):
        l1 = build_list([100, 300])
        l2 = build_list([200, 400, 500, 600])
        
        self.assertEqual(to_list(merge_patient_lists(l1,l2)),
                         
                [100, 200, 300, 400, 500, 600]           
                         
        
        )
        
        
        
    def  test_duplicate_ssns(self):
        
        l1 = build_list([100, 300, 500])
        l2 = build_list([100, 400, 500])
        
        self.assertEqual(to_list(merge_patient_lists(l1,l2)),
                
                [100, 100,300, 400, 500 ,500]
        
        )
        
        
        
        # Edge case
        
    def test_first_list_empty(self):
        
        l1 = None
        l2 = build_list([100, 200, 300])
        
        
        self.assertEqual(to_list(merge_patient_lists(l1, l2)),
                         
                         [100, 200, 300]
                         
        )
        
        
        
    def test_second_list_empty(self):
        
        l1 = build_list([100, 200, 300])
        l2 = None
        
        
        self.assertEqual(to_list(merge_patient_lists(l1, l2)),
                         
                [100, 200, 300]   
                         
        )
        
        
        
    def test_both_list_empty(self):
        self.assertEqual(to_list(merge_patient_lists(None, None)),
                         
                 []  
                         
    )
        
        
if __name__ == "__main__":
    
 unittest.main()
        
        
        
        
    