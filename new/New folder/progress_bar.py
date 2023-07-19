import time
class progress_bar():
    def __init__(self,progress_total=11,time_of_all=1,bar_long=20)->None:
        self.progress_total=progress_total
        self.time_of_all=time_of_all
        self.bar_long=bar_long
    def bar_progress(self,process):
        filled_length=int(process*self.bar_long)
        bar='\033[34m-\033[0m' * filled_length +'-' * (self.bar_long-filled_length)
        return f'|{bar}| {process*100:.1f}%'
    def print_bar(self):
        for i in range(self.progress_total):
            progress = i/ 10
            progress_bar = self.bar_progress(progress)
            # in end='/r' this way the point will not change the direction
            print(progress_bar, end='\r')
            time.sleep(self.time_of_all)
    def circle_bar(self,process):
        a=process%3
        if a==0:
            return '/'
        elif a==1:
            return '-'
        else:
            return '\\'
    def print_circle(self):
        for i in range(self.progress_total):
            progress_circle=self.circle_bar(i)
            print(progress_circle, end='\r')
            time.sleep(self.time_of_all)
a=progress_bar(progress_total=100,time_of_all=0.1)
a.print_circle()