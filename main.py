from fastapi import FastAPI
app = FastAPI()
DataBase = {
1:{'number': 88001112233, 'fullname': 'Ivanov Ivan Ivanovich', 'payment': '1799.86 rub'},
2:{'number': 88002223344, 'fullname': 'Petrov Petr Petrovich', 'payment': '334755.57 rub'},
3:{'number': 88003334455, 'fullname': 'Sidorov Sidor Sidorovich', 'payment': '59.32 rub'}
}
@app.get("/clients")
def getClients():
    return DataBase
@app.get("/clients/{id}")
def getClient(id:int):
    return DataBase[id]
@app.post("/clients/")
def addClient(number:str, fullname:str, payment:str):
    newId = len(DataBase.keys()) + 1
    DataBase[newId] = {"number":number, 'fullname':fullname, 'payment':payment}
    return DataBase
@app.put("/clients/{id}")
def updateClient(id:int, number:str, fullname:str, payment:str):
    DataBase[id] = {"number":number, 'fullname':fullname, 'payment':payment} 
    return DataBase
@app.delete("/clients/{id}")
def deleteClient(id:int):
    del DataBase[id]
    return DataBase
@app.get("/clients/{id}/payment")
def getClientPayment(id:int):
    return DataBase[id]['payment']