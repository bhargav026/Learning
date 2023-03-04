class diction:
  def __init__(self,a):
    self.a = a
  def is_dic(self):
    if type(self.a) == dict:
      return True
    else:
      raise Exception('input is not a dictionary')
  def dic_keys(self):
    if self.is_dic():
        return list(self.a.keys())
  def dic_values(self):
    if self.is_dic():
      return list(self.a.values())
  def dic_item(self):
    if self.is_dic():
      n = input('enter dictionary key:')
      try:
        print(n,':',self.a[n])
      except KeyError as e:
        try:
          print(n,':',self.a[int(n)])
        except Exception as e:
          print('Enter a valid key')
    def userinput(self):
      self.a = eval(input())
      print(self.a, type(self.a))
      print(self.dic_keys())
      print(self.dic_keys())
  def append_item(self,key,value):
    if self.is_dic():
      self.a[key] = value
