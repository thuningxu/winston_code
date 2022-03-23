import xlwings as xw
from string import ascii_uppercase
import pdb

class books:
    def __init__(self):
        print("opening excel sheets...")
        self.eng = xw.Book('Example_CDI_ENG.xlsx')
        self.el = []
        self.ed = {}
        self.pth = xw.Book('Example_CDI_PTH.xlsx')
        self.pl = []
        self.pd = {}
        self.can = xw.Book('Example_CDI_CAN.xlsx')
        self.cl = []
        self.cd = {}
        self.concept_names = xw.Book('CDI_with concept name_win.xlsx')

        print('processing concept catagory mapping')
        self.concept_type = xw.Book('Concept matches_win.xlsx')
        self.concept_cat_map = self.find_concept_map()
        self.concept_type.close()

        print('processing english data...')
        eng_rows = self.read_data(self.eng,12,733-12+1)
        self.eng_rows = self.check_if_can_say(self.eng,eng_rows)
        self.el = self.find_can_say_concept_list(self.eng_rows,self.concept_names,'CDI_ENG')
        self.eng.close()

        print('processing chinese data...')
        pth_rows = self.read_data(self.pth,14,858-14+1)
        self.pth_rows = self.check_if_can_say(self.pth,pth_rows)
        self.pl = self.find_can_say_concept_list(self.pth_rows,self.concept_names,'CDI_PTH')
        self.pth.close()

        print('processing cantonese data...')
        can_rows = self.read_data(self.can,13,862-13+1)
        self.can_rows = self.check_if_can_say(self.can,can_rows)
        self.cl = self.find_can_say_concept_list(self.can_rows,self.concept_names,'CDI_CAN')
        self.can.close()
        self.concept_names.close()

        self.output = xw.Book('Output.xlsx')
        print('writing output data...')
        self.fill_output2()
        self.output.save()
        self.output.close()

    def read_data(self,file , offset, rows):
        sheet = file.sheets[0]
        word_rows = []
        for x in range(rows):
            cell = f'B{x+offset}'
            row = f'{x+offset}'
            if sheet[cell].value != None and sheet[cell].value != ' ':
                word_rows.append(row)

        return word_rows

    def check_if_can_say(self,file,rows):
        sheet = file.sheets[0]
        can_say_list = []
        for row in rows:
            cell = f'D{row}'
            if sheet[cell].value == 1:
                can_say_list.append(row)

        return can_say_list

    def find_can_say_concept_list(self,rows,file,sheet_name):
        sheet = file.sheets[sheet_name]
        can_say_concept_list = []
        for row in rows:
            concept_name = sheet[f'F{row}'].value
            can_say_concept_list.append(concept_name)
        return can_say_concept_list

    def find_concept_map(self):
        file = self.concept_type
        sheet = file.sheets[0]
        concept_cat_map = {}
        for x in range(1232):
            name = sheet[f'C{x+2}'].value
            if name != 'ConceptCatID' and name != 'ConceptName' and name != None:
                cat_id = sheet[f'B{x+2}'].value
                concept_cat_map[name] = cat_id
        return concept_cat_map

    def fill_output(self,concept_cat_map,concept_list):
        row = 2
        index = 0
        file = self.output
        sheet = file.sheets[0]
        for name in concept_list:
            cat_id = concept_cat_map[name]
            sheet[f'B{row}'].value = cat_id
            sheet[f'B{row}'].font.bold = True
            sheet[f'C{row}'].value = name
            sheet[f'F{self.eng_rows[index]}'].value = 1
            sheet[f'E{self.pth_rows[index]}'].value = 1
            sheet[f'D{self.can_rows[index]}'].value = 1
            row += 1
            index += 1
            sleep(0.1)

    def fill_output2(self):
        row = 2
        file = self.output
        sheet = file.sheets[0]
        for name, cat_id in self.concept_cat_map.items():
            #import pdb;pdb.set_trace()
            sheet[f'B{row}'].value = cat_id
            sheet[f'B{row}'].font.bold = True
            sheet[f'C{row}'].value = name

            if name in self.cl: #D
                sheet[f'D{row}'].value = 1
                
            if name in self.pl: #E
                sheet[f'E{row}'].value = 1

            if name in self.el: #F
                sheet[f'F{row}'].value = 1
                
            row += 1

book = books()
