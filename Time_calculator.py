# We will define a function that will help as format the days of the week
def get_days(days):
  if days == 1:
      return "(next day)"
  elif days > 1:
      return f"({days} days later)"
  return 






def add_time(start_time,duration_time, day=False):
    #days of the week
    weekdays=['monday', 'tuesday','wednesday', 'thursday','friday', 'saturday','sunday']
    
    days_after=0
    full_day=24
    half_day=12
    hours,minutes= start_time.split(':')
    minutes,period= minutes.split(" ") #period refers to PM or AM
    duration_hours,duration_minutes=duration_time.split(':')

    #Let's transform the strings to integers
    hours = int(hours)  
    minutes = int(minutes)  
    duration_hours = int(duration_hours)  
    duration_minutes = int(duration_minutes)  
    period = period.strip().lower()
    
    #We find the sum of the hours and the minutes
    sum_of_hours= hours+ duration_hours
    sum_of_minutes= minutes + duration_minutes
    
    # We will transform the hours into minutes if minutes>60
    if sum_of_minutes>60:
        sum_of_hours = int(sum_of_hours+(sum_of_minutes/60))
        sum_of_minutes = int(sum_of_minutes%60) 
    
    # we check if indeed there is a duration time (in hours or minutes
    if duration_hours or duration_minutes:
       if period=='PM' and sum_of_hours>half_day:
           if sum_of_hours%full_day>=1.0:
               days_after=days_after +1
       if sum_of_hours >= half_day:
           hours_left = sum_of_hours /full_day
           days_after = days_after + int(hours_left) 
           

       total_time_hours = sum_of_hours
       while True:
           # constantly reverse period until the total_hours are less than half a day
           if  total_time_hours < half_day:
               break
           if  total_time_hours >= half_day:
               if period == "AM":
                   period = "PM"
               elif period == "PM":
                   period = "AM"
               total_time_hours = total_time_hours - half_day

   # Now, we have to readjust the hours and the minutes so that we can keep only those that they have left
    remaining_hours = int(sum_of_hours % half_day) or hours + 1
    remaining_mins = int(sum_of_minutes % 60)

   # Format the results 
    results = f'{remaining_hours}:{remaining_mins:02} {period.upper()}'
   # In case the day argument is provided:
    if day: 
        day = day.strip().lower()
        selected_day = int((weekdays.index(day) + days_after) % 7)
        current_day = weekdays[selected_day]
        results += f', {current_day.title()} {get_days(days_after)}'

    else: # add days later
        results = " ".join((results, get_days(days_after)))

    return print(results.strip())

add_time("11:30 AM", "2:32", "Monday")
           
        
        