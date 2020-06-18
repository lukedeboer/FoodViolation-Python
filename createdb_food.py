import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime

from DbConnect import DbConnect


class CreateDbFood(DbConnect):
    def __init__(self):
        self.import_violations()
        self.import_inspections()

    @staticmethod
    def import_violations():
        print("\n===========Reading violations Excel started===========\n")
        # Open the workbook and define the worksheet
        book = xlrd.open_workbook('violations.xlsx')
        sheet = book.sheet_by_name("violations")
        connect = DbConnect()
        print("\n===========Data Import started===========\n")
        counter = 0
        for r in range(1, sheet.nrows):
            points = sheet.cell(r, 0).value
            serial_number = sheet.cell(r, 1).value
            violation_code = sheet.cell(r, 2).value
            violation_description = sheet.cell(r, 3).value
            violation_status = sheet.cell(r, 4).value

            # print(points, serial_number, violation_code, violation_description, violation_status)

            counter = counter + 1
            connect.add_violations(points, serial_number, violation_code, violation_description, violation_status)
            print(f'\n==========={counter} Row Imported===========\n')

    @staticmethod
    def import_inspections():
        print("\n===========Reading inspections Excel started===========\n")
        # Open the workbook and define the worksheet
        book = xlrd.open_workbook('inspections.xlsx')
        sheet = book.sheet_by_name("inspections")

        print("\n===========Data Import started===========\n")

        connect = DbConnect()

        counter = 0
        for r in range(1, sheet.nrows):
            y, m, d, h, i, s = xldate_as_tuple(sheet.cell(r, 0).value, book.datemode)
            date_str = "{0}-{1}-{2}".format(d, m, y)
            activity_date = datetime.strptime(date_str, '%d-%m-%Y').date()

            employee_id = sheet.cell(r, 1).value
            facility_address = sheet.cell(r, 2).value
            facility_city = sheet.cell(r, 3).value
            facility_id = sheet.cell(r, 4).value
            facility_name = sheet.cell(r, 5).value

            facility_state = sheet.cell(r, 6).value
            facility_zip = sheet.cell(r, 7).value
            grade = sheet.cell(r, 8).value
            owner_id = sheet.cell(r, 9).value
            owner_name = sheet.cell(r, 10).value

            pe_description = sheet.cell(r, 11).value
            program_element_pe = sheet.cell(r, 12).value
            program_name = sheet.cell(r, 13).value
            program_status = sheet.cell(r, 14).value
            record_id = sheet.cell(r, 15).value

            score = sheet.cell(r, 16).value
            serial_number = sheet.cell(r, 17).value
            service_code = sheet.cell(r, 18).value
            service_description = sheet.cell(r, 19).value

            counter = counter + 1

            # print(activity_date, employee_id, facility_address, facility_city, facility_id, facility_name,
            #       facility_state, facility_zip,
            #       grade, owner_id, owner_name, pe_description, program_element_pe, program_name,
            #       program_status,
            #       record_id, score,
            #       serial_number, service_code, service_description)

            connect.add_inspections(activity_date,employee_id, facility_address, facility_city, facility_id,
                                    facility_name,
                                    facility_state, facility_zip,
                                    grade, owner_id, owner_name, pe_description, program_element_pe, program_name,
                                    program_status,
                                    record_id, score,
                                    serial_number, service_code, service_description)
            print(f'\n==========={counter} Row Imported===========\n')


def main():
    CreateDbFood()


if __name__ == '__main__': main()
