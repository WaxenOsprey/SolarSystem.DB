class Visit:

    def __init__( self, user, location, discovered = False, altered = False, destroyed = False, id = None ):
        self.user = user
        self.location = location
        self.discovered = discovered
        self.altered = altered
        self.destroyed = destroyed 
        self.id = id

    def mark_discovered(self):
        self.discovered = True

    def mark_altered(self):
        self.altered = True
    
    def mark_destroyed(self):
        self.destroyed = True