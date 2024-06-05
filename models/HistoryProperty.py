from datetime import datetime


class HistoryProperty:
    def __init__(self, propertyName, value):
        self.propertyName = propertyName
        self.historicalValues = [self.asHistoricalValue(value)]

    def addValue(self, value):
        self.historicalValues.append(self.asHistoricalValue(value))

    def asHistoricalValue(self, value):
        return {
            "value": value,
            "timestamp": datetime.now()
        }

    def __str__(self):
        formatted_values = [{'value': val['value'], 'timestamp': val['timestamp'].strftime('%d/%m/%Y')} for val in
                            self.historicalValues]
        return f"HistoryProperty(propertyName={self.propertyName}, historicalValues={formatted_values})"