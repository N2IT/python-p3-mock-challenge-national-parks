import datetime

class NationalPark:

    def __init__(self, name):
        self.name = name

        # attribute for visitors
        self._visitors = []

        # attribute for trips
        self._trips = []
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not hasattr(self, "name"):
            if isinstance(name, str) and 3 < len(name):
                self._name = name
        
    def trips(self):
        pass
    
    def visitors(self):
        pass
    
    def total_visits(self):
        pass
    
    def best_visitor(self):
        pass


class Visitor:

    def __init__(self, name):
        self.name = name

        # attribute for national parks
        self._national_parks = []

        # attribute for trips
        self._trips = []

    @property
    def name(self):
        self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 < len(name) < 15:
            self._name = name
        
    def trips(self):
        pass
    
    def national_parks(self):
        pass
    
    def total_visits_at_park(self, park):
        pass


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        # store all trips
        Trip.all.append(self)

        # join to NationalPark
        self.NationalPark._visitors.append(self.visitor)
        self.NationalPark._trips.append(self)

        # join to Visitors
        self.Visitor._national_parks.append(self.national_park)
        self.Visitor._trips.append(self)

    @property
    def start_date(self):
        self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date.strftime("%B %dth")

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date.strftime("%B %dth")