def add_time(start, duration):
	#  >>>==>  START TIME BREAKDOWN
	#print( '>>>==> START TIME BREAKDOWN')
	raw_start_time = start
	#print('raw time : ', raw_start_time)
	split_start_time = raw_start_time.split()
	#print('split time : ', split_start_time)
	start_time_only = split_start_time[0]
	#print('time only: ', start_time_only)
	start_col_pos = start_time_only.find(':')
	#print('colon i position : ', start_col_pos)
	#print('colon index : ', start_time_only[2])
	start_splitter = start_time_only.split(':')
	#print('time hr/min : ', start_splitter)
	start_hour = start_splitter[0]
	#print('hours : ', start_hour)
	#print('hrs length : ', len(start_hour))
	start_mins = start_splitter[1]
	#print('mins : ', start_mins)
	tod_select = split_start_time[1]
	#print('AM/PM : ', start_tod_select)
	#print()
	
	
	#  >>>==>  DURATION TIME BREAKDOWN
	#print('>>>==> DURATION TIME BREAKDOWN')
	#print(duration)
	raw_duration_time = duration
	#print('duration time : ', raw_duration_time)
	split_duration = raw_duration_time.split()
	#print('split duration : ', split_duration)
	duration_time_only = split_duration[0]
	#print('duration : ', duration_time_only)
	duration_col_pos = duration_time_only.find(':')
	#print('colon2 i position : ', duration_col_pos)
	#print('colon2 index : ', duration_time_only[1])
	split_dur = duration_time_only.split(':')
	#print('durs hr/min : ', split_dur)
	dur_hr_side = split_dur[0]
	#print('durs hr : ', dur_hr_side)
	dur_min_side = split_dur[1]
	#print('durs mins : ', dur_min_side)

	

	print()
	print(f' START TIME \n HOURS     : {start_hour}\n COLON     : :\n MINUTES   : {start_mins}\n AM/PM     : {tod_select}\n')
	print(f' DURATION TIME \n HOURS     : {dur_hr_side}\n COLON     : :\n MINUTES   : {dur_min_side}\n')


	new_total_hour = int(start_hour) + int(dur_hr_side)
	print(' NEW TOTAL HOURS : ', new_total_hour)
	new_total_mins = int(start_mins) + int(dur_min_side)
	print(' NEW TOTAL MINS : ', new_total_mins)
	print(' TIME OF DAY : ', tod_select)


	t_o_d = ''
	new_time = ''
	new_time_am = ''
	new_time_pm = ''


	if tod_select == 'AM':
		print('\n ==> WE ARE WORKING ON AM TIME\n')
		print('AM TOTAL MINS : ', new_total_mins)
		print('AM TOTAL HOUR : ', new_total_hour)


		if new_total_mins > 60:
			print('\n ==> MIN > 60MIN CHECK\n')
			print('MIN > 60 : ', new_total_mins)
			new_total_mins -= 60
			print('MIN > 60 - 60 : ', new_total_mins)
			print('NEW TOTAL HOUR : ', new_total_hour)
			new_total_hour += 1
			print('NEW TOTAL HOUR + 1 : ', new_total_hour)


			if new_total_hour > 12:
				print('\n ==> HOUR > 12HR CHECK\n')
				print('HR > 12 : ', new_total_hour)
				new_total_hour -= 12
				print('HR > 12 - 12 :', new_total_hour)
				t_o_d = 'PM'
				print('NEW TOTAL MINS : ', new_total_mins)
				print('TIME OF DAY : ', t_o_d)
				new_time_pm = str(new_total_hour) + ':' + str(new_total_mins) + ' ' + t_o_d
				print('NEW TIME PM : ', new_time_pm)

	return new_time

print(add_time("10:48 AM", "4:35"))