import unittest
import sys
import Function as F

class TestDictForParamTAG(unittest.TestCase):

    def test_1_DictForParamTAG(self):
        one_dic = {}
        one_dic["name"] = "Some.Module"
        one_dic["value"] = "5"
        self.assertEqual(F.DictForParamTAG("Some.Module", 5),
                         one_dic, " DictForParamT1 ")
                         

    def test_2_DictForParamTAG(self):
        one_dic = {}
        one_dic["name"] = "Another.Module"
        one_dic["value"] = "7"
        self.assertEqual(F.DictForParamTAG("Another.Module",7),
                         one_dic, " DictForParamT2 ")

    def test_3_DictForParamTAG(self):
        one_dic = {}
        one_dic["name"] = "stringAndInt"
        one_dic["value"] = "-2"
        self.assertEqual(F.DictForParamTAG("stringAndInt", -2),
                         one_dic, " DictForParamT2 ")                                          
                            
if __name__ == '__main__':
    unittest.main()
