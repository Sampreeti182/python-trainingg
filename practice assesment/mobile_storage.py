class mobile:
    def __init__(self,brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
    def upgrade_storage(self,new_storage):
        if new_storage > self.storage:
            old=self.storage
            self.storage = new_storage
            return f"upgraded from  {old} to  {new_storage}"
        else:
            return (" new storage must br greater than current storage")
m1 = mobile("oneplus", "nord ce5",128)
print(m1.upgrade_storage(236))
