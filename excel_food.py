from DbConnect import DbConnect

import xlsxwriter


class ExcelFood(DbConnect):
    def __init__(self):
        self.import_violations()

    @staticmethod
    def import_violations():
        # Getting group by violation code
        connect = DbConnect()
        cursor = connect.group_by_violations()

        workbook = xlsxwriter.Workbook('ViolationTypes.xlsx')
        worksheet = workbook.add_worksheet("Violations Types")

        # Start from the first cell.
        # Rows and columns are zero indexed.
        row = 0

        # setting header

        worksheet.write(row, 0, "Code")
        worksheet.write(row, 1, "Description")
        worksheet.write(row, 2, "Count")

        total_violations = 0
        for item in cursor:
            row += 1
            # write operation perform
            worksheet.write(row, 0, item["violation_code"])
            worksheet.write(row, 1, item["violation_description"])
            worksheet.write(row, 2, item["count(violation_code)"])

            total_violations = total_violations + int(item["count(violation_code)"])

        # print( "violation_code: {}, violation_description: {}, count(violation_code): {}".format(item[
        # "violation_code"], item[ "violation_description"], item[ "count(violation_code)"]))

        row += 1
        worksheet.write(row, 1, "Total Violations")
        worksheet.write(row, 2, total_violations)
        workbook.close()


def main():
    ExcelFood()


if __name__ == '__main__': main()
