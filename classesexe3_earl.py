#Earls example
class CharacterTest():
  
  def __init__(self, testString):
    self.testString = testString
  
  def testMethod(self, var1):
    return var1.upper() in self.testString


straightLines = CharacterTest("AEFHIKLMNTVWXYZ")
curvedLines = CharacterTest("COS")
straightAndCurvedLines = CharacterTest("BDGJPQRU")
noEndpoints = CharacterTest("BDO")
twoEndpoints = CharacterTest("ACGIJLMNQRSUVWZ")
threeEndpoints = CharacterTest("EFTY")


print(straightLines.testMethod("a"))
print(straightLines.testMethod("q"))
print(straightLines.testMethod("w"))
print(curvedLines.testMethod("c"))
print(curvedLines.testMethod("o"))
print(curvedLines.testMethod("t"))
print(straightAndCurvedLines.testMethod("c"))
print(straightAndCurvedLines.testMethod("b"))
print(straightAndCurvedLines.testMethod("r"))
print(noEndpoints.testMethod("r"))
print(noEndpoints.testMethod("g"))
print(noEndpoints.testMethod("b"))
print(twoEndpoints.testMethod("a"))
print(twoEndpoints.testMethod("q"))
print(twoEndpoints.testMethod("b"))
print(threeEndpoints.testMethod("b"))
print(threeEndpoints.testMethod("e"))
print(threeEndpoints.testMethod("z"))