#http://ideone.com/DRnYj1
class AdoptionCenter:
    def __init__(self, name, species_type, location):
        self.name = name
        self.location = float(location[0]),float(location[1])
        self.species_type = species_type
    def get_name(self):
        return self.name
    def get_location(self):
        return self.location
    def get_species_count(self):
        return self.species_type.copy()
    def get_number_of_species(self, species_name):
        if species_name in self.species_type:
            return (self.species_type[species_name])
        return 0
    def adopt_pet(self, species_name):
        if species_name in self.species_type:
            self.species_type[species_name] -= 1
            if self.species_type[species_name] <= 0:
                del self.species_type[species_name]

class Adopter:
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species
    def get_name(self):
        return self.name
    def get_desired_species(self):
        return self.desired_species
    def get_score(self, adoption_center):
        num_desired = adoption_center.get_number_of_species(self.desired_species)
        return float(1 * num_desired)


adopter = Adopter("place", "cat")
place = AdoptionCenter("place", {"cat":4, "dog":5, "horse":3}, (4,5))
print(adopter.get_score(place))
