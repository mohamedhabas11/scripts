class Atom:
  def __init__(self, label):
    self.label = label
  def add(self,other):
      return list(Atom) + list(Atom)
    
class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms
      
sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
# salt = sodium + chlorine