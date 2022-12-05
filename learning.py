three_tab = "\t\t\t"
line = "*" * 8
line_lower = f'{"*"*9}\t'
two_tab = "\t\t*"
line_vertical = "*\n"*6
text = f"""
*{three_tab}*{line}\t{line}\t*{two_tab}\t   **       
*{three_tab}*{three_tab}*{three_tab}*{two_tab}\t*\t   *    
*{three_tab}*{three_tab}{three_tab}*{two_tab}\t*\t   *  
*{three_tab}*{line}*{two_tab}{two_tab}{line}\t{line}
*{three_tab}*{three_tab}   {three_tab}*{two_tab}\t*\t   *  
*{three_tab}*{three_tab}\t   *\t*{two_tab}\t*\t   *\n{line_lower}{line_lower}{line}\t*{two_tab}\t*\t   *  
"""
print(text.replace("*", input("If you want you can enter another symbol as '*' \nIf you don't enter another symbol please enter '*': ")))



