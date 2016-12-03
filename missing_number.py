def find_missing(series_1,series_2):
  """fxn that finds missing item in list"""

  missing_number=[] 
  
  #checks if both list are empty
  if (len(series_1) == 0) and (len(series_2) == 0):
    
      return 0
    
  else:
      
      for x in series_1:
        
          if x not in series_2:
              
              missing_number.append(x)
          
              
      for x in series_2:
        
          if x not in series_1:
              
              missing_number.append(x)
              
      if len(missing_number) == 0:

          missing_number.append(0)

      return  missing_number.pop()
