class WeAre(object):
    count = 0

    def __init__(self):
        WeAre.count += 1

    def __del__(self):
        WeAre.count -= 1
    
    def __getattr__(self, key):
        return WeAre.count

    def __setattr__(self, key, value):
        pass

    def __delattr__(self, key):
        pass
