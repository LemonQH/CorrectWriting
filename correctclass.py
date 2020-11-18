from HomeworkCorrect import *
import os
class Correct():
    def __init__(self,file_paths,grade,result_path):
        self.file_paths=file_paths
        self.grade =grade
        self.result_path=result_path

    def start_correct(self):
        for file_path in self.file_paths:
            self.get_correct_result(file_path)

    def get_correct_result(self,file_path):
        file_type=file_path.split(".")[1]
        if file_type=="txt":
            print(file_path)
            result=connect_context(file_path,self.grade)
            self.save_result(file_path,result)
        elif file_type=="png" or file_type=="jpg" or file_type=="jepg" :
            result=connect_pic(file_path,self.grade)
            self.save_result(file_path,result)

    def save_result(self,file_path,result):
        result_file_name=os.path.basename(file_path).split('.')[0]+'_result.txt'
        f=open(self.result_path+'/'+result_file_name,'w')
        f.write(str(result))
        f.close()

