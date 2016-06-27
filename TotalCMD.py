import os, sublime_plugin
class TotalcmdCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name=self.view.file_name()
        path=file_name.split("\\")
        current_driver=path[0]
        path.pop()
        current_directory="\\".join(path)
        command= 'cd "'+current_directory+'" & "'+current_driver+'" & start TOTALCMD64.EXE /I="E:\Program Files\TC\Wincmd64.ini" "'+current_directory+'"'
        os.system(command)

class DoublecmdCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name=self.view.file_name()
        print(file_name)
        path=file_name.split("\\")
        current_driver=path[0]
        path.pop()
        current_directory="\\".join(path)
        command= 'cd "'+current_directory+'" & "'+current_driver+'" & start E:\OpenServer\progs\_System\Doublecmd\doublecmd.exe -t "'+current_directory+'"'
        os.system(command)

class CmdrCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name=self.view.file_name()
        print(file_name)
        path=file_name.split("\\")
        current_driver=path[0]
        path.pop()
        current_directory="\\".join(path)
        command= 'cd "'+current_directory+'" & "'+current_driver+'" & start cmdr "'+current_directory+'"'
        os.system(command)

class NppCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name=self.view.file_name()
        print(file_name)
        path=file_name.split("\\")
        current_driver=path[0]
        path.pop()
        current_directory="\\".join(path)
        command= 'cd "'+current_directory+'" & "'+current_driver+'" & start npp "'+file_name+'"'
        os.system(command)

class AkelpadCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name=self.view.file_name()
        print(file_name)
        path=file_name.split("\\")
        current_driver=path[0]
        path.pop()
        current_directory="\\".join(path)
        command= 'cd "'+current_directory+'" & "'+current_driver+'" & start notepad "'+file_name+'"'
        os.system(command)


class PspadCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name=self.view.file_name()
        print(file_name)
        path=file_name.split("\\")
        current_driver=path[0]
        path.pop()
        current_directory="\\".join(path)
        command= 'cd "'+current_directory+'" & "'+current_driver+'" & start pspad "'+file_name+'"'
        os.system(command)

class Npd2Command(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name=self.view.file_name()
        print(file_name)
        path=file_name.split("\\")
        current_driver=path[0]
        path.pop()
        current_directory="\\".join(path)
        command= 'cd "'+current_directory+'" & "'+current_driver+'" & start notepad2 "'+file_name+'"'
        os.system(command)


class NpdCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name=self.view.file_name()
        print(file_name)
        path=file_name.split("\\")
        current_driver=path[0]
        path.pop()
        current_directory="\\".join(path)
        command= 'cd "'+current_directory+'" & "'+current_driver+'" & start npd "'+file_name+'"'
        os.system(command)


class OpenfilesindirCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name=self.view.file_name()
        print(file_name)
        path=file_name.split("\\")
        current_driver=path[0]
        path.pop()
        current_directory="\\".join(path)
        command= 'start sublime_text.exe '+current_directory+'*'
        os.system(command)

