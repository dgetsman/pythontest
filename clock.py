from datetime import datetime
import time
import os
from colorama import Fore, Style

zero = """
■■■■
■  ■
■  ■
■  ■
■■■■
"""
one = """
   ■
   ■
   ■
   ■
   ■
"""
two = """
■■■■
   ■
■■■■
■   
■■■■
"""
three = """
■■■■
   ■
■■■■
   ■
■■■■
"""
four = """
■  ■
■  ■
■■■■
   ■
   ■
"""
five = """
■■■■
■   
■■■■
   ■
■■■■
"""
six = """
■■■■
■   
■■■■
■  ■
■■■■
"""
seven = """
■■■■
   ■
   ■
   ■
   ■
"""
eight = """
■■■■
■  ■
■■■■
■  ■
■■■■
"""
nine = """
■■■■
■  ■
■■■■
   ■
   ■
"""
dot_pos1 = """
 ■■ 
    
    
    
    
"""
dot_pos2 = """
    
 ■■ 
    
    
    
"""
dot_pos3 = """
    
    
 ■■ 
    
    
"""
dot_pos4 = """
    
    
    
 ■■ 
    
"""
dot_pos5 = """
    
    
    
    
    
 ■■ 
"""

numbers = {
   '1': one,
   '2': two,
   '3': three,
   '4': four,
   '5': five,
   '6': six,
   '7': seven,
   '8': eight,
   '9': nine,
   '0': zero,
   'dot_position':{
   1:dot_pos1,
   2:dot_pos2,
   3:dot_pos3,
   4:dot_pos4,
   5:dot_pos5
    }
}

def get_view(number: str):
   if len(number) == 1:
      first = numbers["0"]
      second = numbers[number]
   else:
      first = numbers[number[0]]
      second = numbers[number[1]]
   return combine_views(first, second)

def combine_views(first, second):
   combine_numbers = [f"{first}  {second}" for first, second in zip (first.splitlines(), second.splitlines())]
   result = "\n".join(i for i in combine_numbers)
   return result

def clock():
   colors = [
            Fore.MAGENTA,\
            Fore.BLUE, \
            Fore.CYAN,\
            Fore.GREEN, \
            Fore.RESET,\
            Fore.YELLOW,\
            Fore.RED,\
            ]
   counter_position = 1
   colors_id = 0
   while True:
      color_print = colors[colors_id]
      if counter_position == 5: 
         step = -1
      elif counter_position == 1:
         step = 1
      os.system('CLS')
      current_time = datetime.now().time()
      hour_views = get_view(str(current_time.hour))
      minute_views = get_view(str(current_time.minute))
      second_views = get_view(str(current_time.second))
      result = combine_views(hour_views, numbers["dot_position"][counter_position])
      result = combine_views(result, minute_views)
      result = combine_views(result, numbers["dot_position"][counter_position])
      result = combine_views(result, second_views)  
      print(color_print + result)
      counter_position += step
      colors_id = (colors_id + 1) % len(colors)
      time.sleep(1)
clock()