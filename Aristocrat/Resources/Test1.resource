***Settings***
Library		RPA.Excel.Application

***Keyword***
Read From Excel File
	[Documentation]		Keyword For read data from Excel Application
	[Arguments]		File_path	Sheet_name		Column_no	Row_no
	Excel.Application.Open	File_path
	Excel.Application.Set Active Worksheet	Sheet_name
	${Data} =	Excel.Application.Read From Cell	Column_no	Row_no
Get Data From Excel
	[Documentation]		Keyword for Get Data From Excel
	Read From Excel File	File_path	Sheet_name		Column_no	Row_no