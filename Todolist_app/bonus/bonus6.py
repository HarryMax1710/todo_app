Descriptions = ["AR GOAT of Football", "POR GOAT of Football","God of Football", "King of Football", "GodFather of Football"]
Footballers = ["Lionel Messi.txt", "Cristiano Ronaldo.txt", "Diego Maradona.txt", "Pele.txt", "Johan Cryuff.txt"]

for Description, Footballer in zip(Descriptions, Footballers):
    file = open(f"files/{Footballer}","w")
    file.write(Description)