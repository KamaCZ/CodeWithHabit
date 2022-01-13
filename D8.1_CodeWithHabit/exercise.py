class MacBook:

    def __init__(self,type,model,displayName,displaySize,processorName,processorCores,
    processorGHz,storage,memory):
        self.type = type
        self.model = model
        self.displayName = displayName
        self.displaysize = displaySize
        self.processorName= processorName
        self.processorCores = processorCores
        self.processorGHz = processorGHz
        self.storage = storage
        self.memory = memory

    def displayConversion(self):
        return self.displaysize * 2.54

    
