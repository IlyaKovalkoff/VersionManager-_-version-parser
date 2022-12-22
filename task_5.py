class VersionManager:
    def __init__(self, version = False):
        self.__version_input = version

        self.__previous_version = ''

        self.__out_of_range_chek = False

        self.__step_of_ugrade = 0

        self.__major = 0
        self.__minor = 0
        self.__patch = 1

        self.parsing_version_input()
        self.__version_save = ['']

        

    def parsing_version_input(self):
        if self.__version_input :   # 1.2.3   or  1     or     1.2.3.b    or   1.2.b
            version_parts = self.__version_input.split('.')
            version_num = len(version_parts)
            if version_num >= 3:
                try:
                    self.__major = int(version_parts[0])
                    self.__minor = int(version_parts[1])
                    self.__patch = int(version_parts[2])
                except:
                    raise Exception("Error occured while parsing version!")
            elif version_num == 2:
                try:
                    self.__major = int(version_parts[0])
                    self.__minor = int(version_parts[1])
                    self.__patch = 0
                except:
                    raise Exception("Error occured while parsing version!")
            elif version_num == 1:
                try:
                    self.__major = int(version_parts[0])
                    self.__minor = 0
                    self.__patch = 0
                except:
                    raise Exception("Error occured while parsing version!")

        else:
            self.__major = self.__major
            self.__minor = self.__minor
            self.__patch = self.__patch  
            

    def was_upgraded(self):
        self.__step_of_ugrade += 1

    def was_degraded(self):
        self.__version_save.pop(self.__step_of_ugrade)
        self.__step_of_ugrade -= 1
        

    
    def set_to_zero(self, init_name):
        if init_name == 'major':
            self.__major = 0
        elif init_name == 'minor':
            self.__minor = 0
        elif init_name == 'patch':
            self.__patch = 0
        else:
            pass
    
    def save_all_versions(self):
        self.__version_save.append(str(self.__major) + '.' + str(self.__minor) + '.' + str(self.__patch))

    def release(self):
        
        return str(self.__major) + '.' + str(self.__minor) + '.' + str(self.__patch)

    def save_previous_version(self):
        self.__previous_version = str(self.__major) + str(self.__minor) + str(self.__patch)

    def major(self):
        
        self.save_all_versions()
        self.__major += 1
        self.set_to_zero('minor')
        self.set_to_zero('patch')
        self.was_upgraded()

        return self
        
        

    def minor(self):
        
        self.save_all_versions()
        self.__minor += 1
        self.set_to_zero('patch')
        self.was_upgraded()
        return self

    def patch(self):
        
        self.save_all_versions()
        self.__patch += 1
        self.was_upgraded()
        return self


    def rollback(self):
        if self.__step_of_ugrade == 0:
            raise Exception("Cannot rollback!")
            
        else:
            parsing_save = self.__version_save[self.__step_of_ugrade].split('.')
            self.__major = int(parsing_save[0])
            self.__minor = int(parsing_save[1])
            self.__patch = int(parsing_save[2])
            self.was_degraded()
            return self
            

    




v = VersionManager('1.9.1')




