
class Rockstar:
    company_name="Rockstar"
    
    
class GTA(Rockstar):
    Series_name="Grand Theft Auto"
    def __init__(self,name):
        self.name=name
class RDR(Rockstar):
    Series_name="Red Dead Redemption"
    def __init__(self,name):
        self.name=name
class Bully(Rockstar):
    Series_name="Bully"
    def __init__(self,name):
        self.name=name
games=[GTA("GTA VC"),RDR("RDR1"),Bully("Bully"),RDR("RDR2")]
for game in games:
    print("-------------------")
    print(game.name)
    print(game.company_name)
    print(game.Series_name)
    print("-------------------")

# output
# -------------------
# GTA VC
# Rockstar
# Grand Theft Auto
# -------------------
# -------------------
# RDR1
# Rockstar
# Red Dead Redemption
# -------------------
# -------------------
# Bully
# Rockstar
# Bully
# -------------------
# -------------------
# RDR2
# Rockstar
# Red Dead Redemption
# -------------------


# ** Process exited - Return Code: 0 **
