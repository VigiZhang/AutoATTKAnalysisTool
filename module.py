'''
Created on 2012-7-4

@author: Vigi
'''

class File():
    "File Info."
    
    def __init__(self):
        self.id = ''
        self.path = ''
        self.size = ''
        self.attributes = ''
        self.signer = ''
        self.productName = ''
        self.productVersion = ''
        self.companyName = ''
        self.fileDescription = ''
        self.originalFilename = ''
        self.fileVersionLabel = ''
        self.fileVersionNumber = ''
        self.sha1 = ''
        self.md5 = ''
        self.rootkitInfo = ''
        self.createTime = ''
        self.lastAccessTime = ''
        self.lastWriteTime = ''
        self.checkedFlags = ''
        self.autorun = ''
        self.process = []
        self.service = ''
        self.drivers = ''

    def get_autorun(self):
        return self.__autorun


    def get_process(self):
        return self.__process


    def get_service(self):
        return self.__service


    def get_drivers(self):
        return self.__drivers


    def set_autorun(self, value):
        self.__autorun = value


    def set_process(self, value):
        self.__process = value


    def set_service(self, value):
        self.__service = value


    def set_drivers(self, value):
        self.__drivers = value


    def del_autorun(self):
        del self.__autorun


    def del_process(self):
        del self.__process


    def del_service(self):
        del self.__service


    def del_drivers(self):
        del self.__drivers

        
    def get_id(self):
        return self.__id


    def get_path(self):
        return self.__path


    def get_size(self):
        return self.__size


    def get_attributes(self):
        return self.__attributes


    def get_signer(self):
        return self.__signer


    def get_product_name(self):
        return self.__productName


    def get_product_version(self):
        return self.__productVersion


    def get_company_name(self):
        return self.__companyName


    def get_file_description(self):
        return self.__fileDescription


    def get_original_filename(self):
        return self.__originalFilename


    def get_file_version_label(self):
        return self.__fileVersionLabel


    def get_file_version_number(self):
        return self.__fileVersionNumber


    def get_sha1(self):
        return self.__sha


    def get_md_5(self):
        return self.__md5


    def get_rootkit_info(self):
        return self.__rootkitInfo


    def get_create_time(self):
        return self.__createTime


    def get_last_access_time(self):
        return self.__lastAccessTime


    def get_last_write_time(self):
        return self.__lastWriteTime


    def get_checked_flags(self):
        return self.__checkedFlags


    def set_id(self, value):
        self.__id = value


    def set_path(self, value):
        self.__path = value


    def set_size(self, value):
        self.__size = value


    def set_attributes(self, value):
        self.__attributes = value


    def set_signer(self, value):
        self.__signer = value


    def set_product_name(self, value):
        self.__productName = value


    def set_product_version(self, value):
        self.__productVersion = value


    def set_company_name(self, value):
        self.__companyName = value


    def set_file_description(self, value):
        self.__fileDescription = value


    def set_original_filename(self, value):
        self.__originalFilename = value


    def set_file_version_label(self, value):
        self.__fileVersionLabel = value


    def set_file_version_number(self, value):
        self.__fileVersionNumber = value


    def set_sha1(self, value):
        self.__sha = value


    def set_md_5(self, value):
        self.__md5 = value


    def set_rootkit_info(self, value):
        self.__rootkitInfo = value


    def set_create_time(self, value):
        self.__createTime = value


    def set_last_access_time(self, value):
        self.__lastAccessTime = value


    def set_last_write_time(self, value):
        self.__lastWriteTime = value


    def set_checked_flags(self, value):
        self.__checkedFlags = value


    def del_id(self):
        del self.__id


    def del_path(self):
        del self.__path


    def del_size(self):
        del self.__size


    def del_attributes(self):
        del self.__attributes


    def del_signer(self):
        del self.__signer


    def del_product_name(self):
        del self.__productName


    def del_product_version(self):
        del self.__productVersion


    def del_company_name(self):
        del self.__companyName


    def del_file_description(self):
        del self.__fileDescription


    def del_original_filename(self):
        del self.__originalFilename


    def del_file_version_label(self):
        del self.__fileVersionLabel


    def del_file_version_number(self):
        del self.__fileVersionNumber


    def del_sha1(self):
        del self.__sha


    def del_md_5(self):
        del self.__md5


    def del_rootkit_info(self):
        del self.__rootkitInfo


    def del_create_time(self):
        del self.__createTime


    def del_last_access_time(self):
        del self.__lastAccessTime


    def del_last_write_time(self):
        del self.__lastWriteTime


    def del_checked_flags(self):
        del self.__checkedFlags

    id = property(get_id, set_id, del_id, "id's docstring")
    path = property(get_path, set_path, del_path, "path's docstring")
    size = property(get_size, set_size, del_size, "size's docstring")
    attributes = property(get_attributes, set_attributes, del_attributes, "attributes's docstring")
    signer = property(get_signer, set_signer, del_signer, "signer's docstring")
    productName = property(get_product_name, set_product_name, del_product_name, "productName's docstring")
    productVersion = property(get_product_version, set_product_version, del_product_version, "productVersion's docstring")
    companyName = property(get_company_name, set_company_name, del_company_name, "companyName's docstring")
    fileDescription = property(get_file_description, set_file_description, del_file_description, "fileDescription's docstring")
    originalFilename = property(get_original_filename, set_original_filename, del_original_filename, "originalFilename's docstring")
    fileVersionLabel = property(get_file_version_label, set_file_version_label, del_file_version_label, "fileVersionLabel's docstring")
    fileVersionNumber = property(get_file_version_number, set_file_version_number, del_file_version_number, "fileVersionNumber's docstring")
    sha1 = property(get_sha1, set_sha1, del_sha1, "sha's docstring")
    md5 = property(get_md_5, set_md_5, del_md_5, "md5's docstring")
    rootkitInfo = property(get_rootkit_info, set_rootkit_info, del_rootkit_info, "rootkitInfo's docstring")
    createTime = property(get_create_time, set_create_time, del_create_time, "createTime's docstring")
    lastAccessTime = property(get_last_access_time, set_last_access_time, del_last_access_time, "lastAccessTime's docstring")
    lastWriteTime = property(get_last_write_time, set_last_write_time, del_last_write_time, "lastWriteTime's docstring")
    checkedFlags = property(get_checked_flags, set_checked_flags, del_checked_flags, "checkedFlags's docstring")
    autorun = property(get_autorun, set_autorun, del_autorun, "autorun's docstring")
    process = property(get_process, set_process, del_process, "process's docstring")
    service = property(get_service, set_service, del_service, "service's docstring")
    drivers = property(get_drivers, set_drivers, del_drivers, "drivers's docstring")


class Autorun:
    "Autorun Info."
    
    def __init__(self):
        self.id = ''
        self.fileId = ''
        self.location = ''
        self.itemName = ''
        self.launchString = ''
        self.groupId = ''

    def get_id(self):
        return self.__id


    def get_file_id(self):
        return self.__fileId


    def get_location(self):
        return self.__location


    def get_item_name(self):
        return self.__itemName


    def get_launch_string(self):
        return self.__launchString


    def get_group_id(self):
        return self.__groupId


    def set_id(self, value):
        self.__id = value


    def set_file_id(self, value):
        self.__fileId = value


    def set_location(self, value):
        self.__location = value


    def set_item_name(self, value):
        self.__itemName = value


    def set_launch_string(self, value):
        self.__launchString = value


    def set_group_id(self, value):
        self.__groupId = value


    def del_id(self):
        del self.__id


    def del_file_id(self):
        del self.__fileId


    def del_location(self):
        del self.__location


    def del_item_name(self):
        del self.__itemName


    def del_launch_string(self):
        del self.__launchString


    def del_group_id(self):
        del self.__groupId

    id = property(get_id, set_id, del_id, "id's docstring")
    fileId = property(get_file_id, set_file_id, del_file_id, "fileId's docstring")
    location = property(get_location, set_location, del_location, "location's docstring")
    itemName = property(get_item_name, set_item_name, del_item_name, "itemName's docstring")
    launchString = property(get_launch_string, set_launch_string, del_launch_string, "launchString's docstring")
    groupId = property(get_group_id, set_group_id, del_group_id, "groupId's docstring")
    
    
class Process:
    "Process Info."
    
    def __init__(self):
        self.id = ''
        self.pid = ''
        self.parentPid = ''
        self.commandLine = ''
        self.userName = ''
        self.fileId = ''
        self.dlls = []
        self.children = []
        self.root = False

    def get_id(self):
        return self.__id


    def get_children(self):
        return self.__children


    def get_root(self):
        return self.__root


    def set_id(self, value):
        self.__id = value


    def set_children(self, value):
        self.__children = value


    def set_root(self, value):
        self.__root = value


    def del_id(self):
        del self.__id


    def del_children(self):
        del self.__children


    def del_root(self):
        del self.__root



    def get_pid(self):
        return self.__pid


    def get_parent_pid(self):
        return self.__parentPid


    def get_command_line(self):
        return self.__commandLine


    def get_user_name(self):
        return self.__userName


    def get_file_id(self):
        return self.__fileId


    def get_dlls(self):
        return self.__dlls


    def set_pid(self, value):
        self.__pid = value


    def set_parent_pid(self, value):
        self.__parentPid = value


    def set_command_line(self, value):
        self.__commandLine = value


    def set_user_name(self, value):
        self.__userName = value


    def set_file_id(self, value):
        self.__fileId = value


    def set_dlls(self, value):
        self.__dlls = value



    def del_pid(self):
        del self.__pid


    def del_parent_pid(self):
        del self.__parentPid


    def del_command_line(self):
        del self.__commandLine


    def del_user_name(self):
        del self.__userName


    def del_file_id(self):
        del self.__fileId


    def del_dlls(self):
        del self.__dlls

    id = property(get_id, set_id, del_id, "id's docstring")
    pid = property(get_pid, set_pid, del_pid, "pid's docstring")
    parentPid = property(get_parent_pid, set_parent_pid, del_parent_pid, "parentPid's docstring")
    commandLine = property(get_command_line, set_command_line, del_command_line, "commandLine's docstring")
    userName = property(get_user_name, set_user_name, del_user_name, "userName's docstring")
    fileId = property(get_file_id, set_file_id, del_file_id, "fileId's docstring")
    dlls = property(get_dlls, set_dlls, del_dlls, "dlls's docstring")
    children = property(get_children, set_children, del_children, "children's docstring")
    root = property(get_root, set_root, del_root, "root's docstring")
