import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **var):
    self.contents = []
    for i in var:
      for n in range(var[i]):
        self.contents.append(i)
    #print(self.contents)
    self.total = len(self.contents)
    self.hat = copy.deepcopy(self.contents)
  
  def draw(self, num):
    lis = []

    if(num > self.total):
      return self.contents
     
    for i in range(num):
      #print(len(self.contents))
      if(len(self.contents) == 0):
        self.contents = copy.copy(self.hat)
      ran = random.randrange(len(self.contents))
      lis.append(self.contents[ran])
      self.contents.pop(ran)
   
    return sorted(lis)




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  expect_lis = []
  count = 0;
  for i in expected_balls:
    for n in range(expected_balls[i]):
      expect_lis.append(i)
  
  expect_lis = sorted(expect_lis)
  exper_lis = []
  for i in range(num_experiments):
    lhat = copy.deepcopy(hat)
    exper_lis = lhat.draw(num_balls_drawn)
    for i in expect_lis:
      if(i in exper_lis):
        exper_lis.remove(i)
    if(num_balls_drawn > lhat.total):
      if(len(exper_lis) == lhat.total - len(expect_lis)):
        count += 1;
    if(len(exper_lis) == num_balls_drawn - len(expect_lis)):
      count += 1

    #if(all(item in exper_lis for item in expect_lis)):
      #print(exper_lis)
      #count += 1

  #print(count)

  return count/num_experiments