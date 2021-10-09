class DnaSequence:
    def __init__(self,dna_string,name,id):
        for i in dna_string:
            if i not in "actg":
                print("not a right sequence")
                raise
        self.dna_string=dna_string
        self.name=name
        self.id=id

    def __str__(self):
        return "{}".format(self.dna_string)

    def __eq__(self, other):
        if self.dna_string!=other.dna_string:
            return False
        return True

    def __ne__(self,other):
        return not self.__eq__(other)

    def __len__(self):
        return len(self.dna_string)
    def __setitem__(self, key, value):
         self.dna_string[key]=value

    def __getitem__(self, key):
        return self.dna_string[key]

    def __add__(self, other):
        if type(other)==str:
             self.dna_string+=other
        if type(other)==DnaSequence:
             self.dna_string += other.dna_string
        return self

    def  assignment(self,other):
        if type(other)==str:
            self.dna_string=other
        elif type(other)==DnaSequence:
            self.dna_string=other.dna_string

    def insert(self, nucleotide,key):
        if nucleotide not in "actg":
            print("not a right nucleotide")
            return
        self.dna_string= self.dna_string[:key]+nucleotide+self.dna_string[key:]


