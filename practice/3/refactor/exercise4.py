from abc import ABC, abstractmethod

class ReportGenerator:
    def __init__(self, report_type : 'Report', data):
        self.report_type = report_type  # 'pdf', 'excel', 'html'
        self.data = data

    def generate(self):
        return self.report_type.generate(self.data)
        
class Report(ABC):
    @abstractmethod
    def generate(self,data):
        pass
    
class PDF(Report):
    def generate(self, data):
        return f"Generating PDF Report with data: {data}"
    
class Excel(Report):
    def generate(self,data):
        return f"Generating Excel Sheet with data: {data}"
    
class HTML(Report):
    def generate(self,data):
        return f"<html><body>Report: {data}</body></html>"
        
    
