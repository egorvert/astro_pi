class MetricController:
    def __init__(self, history):
        self.history = []
        self.deviance = False

    def checkDeviance(self):
        # Works out the average from the past three results stored in history
        # Subtracts the current result from the average
        # Checks whether the deviance is significant
            # If it is - return True
            # Else - False
        pass

    def getTimestamp(self):
        pass