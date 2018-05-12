class Fields:
    def __init__(self):
        self.chrom = ""
        self.pos = ""
        self.id = ""
        self.ref =""
        self.alt = ""
        self.qual = ""
        self.filter = ""
        self.info = ""

    def get_fields(self):
        return self.chrom,self.pos,self.id,self.ref,self.alt,self.qual,self.filter,self.info

    def parse_row(self,row):
        return row.strip("\n").split(sep="\t")

    def update_fields(self,fields):
        self.chrom = fields[0]
        self.pos = fields[1]
        self.id = fields[2]
        self.ref = fields[3]
        self.alt = fields[4]
        self.qual = fields[5]
        self.filter = fields[6]
        self.info = fields[7]

class Records:
    def __init__(self):
        self.records = {}
        self.metadata = []
        self.total_records = 0

    def get_records(self):
        return self.records

    def get_metadata(self):
        return self.metadata

    def get_totalrecords(self):
        return self.total_records

    def add_row(self,row):
        fields = Fields()
        data = fields.update_fields(fields.parse_row(row))
        self.records[self.total_records] = fields
        self.total_records += 1

    def get_rowinfo(self,row_nr):
        return self.records[row_nr].get_fields()

    def isvalid(self,bases,values):
        for base in bases:
            if base not in values:
                return False
        return True

    def nucleotide_changes(self,ref,alt):
        size = min(len(ref),len(alt))
        changes = []
        for i in range(0,size):
            if (ref[i] != alt[i]):
                changes.append((ref[i],alt[i]))
        return changes

    def nucleotide_deletions(self,ref,alt):
        size = min(len(ref), len(alt))
        changes = []
        #remoção ocorrem no meio de bases
        if len(ref) == len(alt):
            for i in range(0,len(ref)):
                if alt[i] != ref[i]:
                    changes.append((ref[i],alt[i]))
            return changes
        else:
            #remoção no final das bases
            for i in range(0, size):
                if (ref[i] != alt[i]):
                    changes.append((ref[i], alt[i]))
            for i in range(size,len(ref)):
                changes.append((ref[i],"."))
        return changes

    def nucleotide_insertions(self,ref,alt):
        size = min(len(ref), len(alt))
        changes = []
        #percorrer o ref
        i = 0
        #percorrer o alt
        j = 0
        for i in range(0, size):
            if (alt[j] != ref[i]):
                changes.append((".",alt[j]))
                j += 1
        #inserções no final
        for i in range(size, len(alt)):
            changes.append((".",alt[i]))
        return changes

    def parse_file(self,data):
        count = 0
        flag = 0
        row = ""
        print ("Reading meta info ...")
        for line in data:
            #metadata lines
            if flag == 0:
                if "#CHROM" in line:
                    print ("Begining Parsing ...")
                    flag = 1
                self.metadata.append(line.replace("#",""))
            #data lines
            else:
                self.add_row(line)
                count += 1
        print(str(count) + " lines of data read from file ")

