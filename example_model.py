from layer import Layer

class Model:
  idCounter = 1
  def __init__(self):
    self.id = Model.idCounter
    Model.idCounter +=1
    self.layers = []
  
  def add(self, layer):
    self.layers.append(layer)
  
  def last_layer(self):
    return self.layers[-1]

  def predict(self, instance):
    arr_out = instance.copy()
    for layer in self.layers:
      arr_out = layer.activate(arr_out)
    return arr_out
      
  def predicts(self, instances):
    return [self.predict(instance) for instance in instances]