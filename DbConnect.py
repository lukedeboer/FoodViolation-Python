import sqlite3


class DbConnect:
    def __init__(self):
        self._db = sqlite3.connect("assignment2.db")
        self._db.row_factory = sqlite3.Row
        self._db.execute(
            "create table if not exists "
            "violations(ID integer primary key autoincrement,"
            "points int,"
            "serial_number text, "
            "violation_code text, "
            "violation_description text, "
            "violation_status text) ")
        self._db.execute(
            "create table if not exists "
            "inspections(ID integer primary key autoincrement,"
            "activity_date text,employee_id text,facility_address text,facility_city text, facility_id text,"
            "facility_name text,facility_state text,facility_zip text,grade text,owner_id text,owner_name text,"
            "pe_description text,program_element_pe int,program_name text,program_status text,record_id text,"
            "score int,serial_number text,service_code int,service_description text) ")
        self._db.execute(
            "create table if not exists "
            "previous_violations(ID integer primary key autoincrement,serial_number text,name text,address text,"
            "zipcode text,city text,violations int)")
        self._db.commit()

    def add_violations(self, points, serial_number, violation_code, violation_description, violation_status):
        self._db.row_factory = sqlite3.Row
        # Add Records
        self._db.execute("insert into violations(points,serial_number,violation_code, violation_description,"
                         "violation_status) values(?,?,?,?,?)", (points, serial_number, violation_code,
                                                                 violation_description, violation_status))
        self._db.commit()

    def add_inspections(self, activity_date, employee_id, facility_address, facility_city, facility_id, facility_name,
                        facility_state, facility_zip,
                        grade, owner_id, owner_name, pe_description, program_element_pe, program_name, program_status,
                        record_id, score,
                        serial_number, service_code, service_description):
        self._db.row_factory = sqlite3.Row
        # Add Records
        self._db.execute("insert into inspections(activity_date,employee_id,facility_address,facility_city, "
                         "facility_id, "
                         "facility_name,facility_state,facility_zip,grade,owner_id,owner_name,pe_description,"
                         "program_element_pe,program_name,program_status,record_id,score,serial_number,service_code,"
                         "service_description) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                         (activity_date,
                          employee_id,
                          facility_address,
                          facility_city,
                          facility_id,
                          facility_name,
                          facility_state,
                          facility_zip,
                          grade,
                          owner_id,
                          owner_name,
                          pe_description,
                          program_element_pe,
                          program_name,
                          program_status,
                          record_id,
                          score,
                          serial_number,
                          service_code,
                          service_description))
        self._db.commit()

    def add_previous_violations(self, serial_number, name, address, zipcode, city, violations):
        self._db.row_factory = sqlite3.Row
        # Add Records
        self._db.execute("insert into previous_violations(serial_number,name, address,zipcode,city,violations) "
                         "values(?,?,?,?,?,?)", (serial_number, name,
                                                 address, zipcode, city, violations))
        self._db.commit()

    def group_by_violations(self):
        self._db.row_factory = sqlite3.Row
        # List Records
        cursor = self._db.execute("select violation_code,violation_description, count(violation_code) from violations "
                                  "GROUP by violation_code")

        return cursor

    def distinct_violations(self):
        self._db.row_factory = sqlite3.Row
        # List Records
        cursor = self._db.execute("select DISTINCT(violations.serial_number),activity_date, inspections.facility_name "
                                  "as name, "
                                  "inspections.facility_address as address, inspections.facility_zip as zipcode, "
                                  "inspections.facility_city as city,  count(violations.serial_number) as violations  "
                                  "from violations JOIN inspections on violations.serial_number = "
                                  "inspections.serial_number GROUP BY violations.serial_number ORDER by "
                                  "violations")
        return cursor

    # def highest_violations_per_month(self):
    #     self._db.row_factory = sqlite3.Row
    #     # List Records
    #     cursor = self._db.execute("select activity_date,facility_zip,violations.serial_number, "
    #                               "count(violations.serial_number) as noofviolations, strftime('%m', activity_date) "
    #                               "as month from violations inner join  inspections on violations.serial_number = "
    #                               "inspections.serial_number group by month, violations.serial_number, facility_zip "
    #                               "having count(violations.serial_number) = (select max(noofviolations) from (select "
    #                               "facility_zip,violations.serial_number, count(violations.serial_number) as "
    #                               "noofviolations, strftime('%m', activity_date) as month from violations inner join  "
    #                               "inspections on violations.serial_number = inspections.serial_number group by "
    #                               "month, violations.serial_number, facility_zip ) )")
    #     return cursor

    def violations_per_month(self):
        self._db.row_factory = sqlite3.Row
        cursor = self._db.execute("select month, max(noofviolations) as maxofviolations ,min(noofviolations) as minofviolations , avg(noofviolations) as avgofviolations  from ( select facility_zip, count(violations.serial_number) as noofviolations, strftime('%Y-%m', activity_date) as month from violations inner join inspections on violations.serial_number = inspections.serial_number group by month, facility_zip ) group by month")
        return cursor


    # def lowest_violations_per_month(self):
    #     self._db.row_factory = sqlite3.Row
    #     # List Records
    #     cursor = self._db.execute("select activity_date,facility_zip,violations.serial_number, "
    #                               "count(violations.serial_number) as noofviolations, strftime('%m', activity_date) "
    #                               "as month from violations inner join  inspections on violations.serial_number = "
    #                               "inspections.serial_number group by month, violations.serial_number, facility_zip "
    #                               "having count(violations.serial_number) = (select min(noofviolations) from (select "
    #                               "facility_zip,violations.serial_number, count(violations.serial_number) as "
    #                               "noofviolations, strftime('%m', activity_date) as month from violations inner join  "
    #                               "inspections on violations.serial_number = inspections.serial_number group by "
    #                               "month, violations.serial_number, facility_zip ) )")
    #     return cursor

    def average_mcdonalds_violations_per_month(self):
        self._db.row_factory = sqlite3.Row
        # List Records
        cursor = self._db.execute("select month, (sum(noofviolations) / count(*) ) as average from ( select strftime( '%Y-%m', activity_date) as month,  count(inspections.facility_name ) as noofviolations, inspections.facility_name from inspections inner join violations on violations.serial_number = inspections.serial_number where facility_name like '%MCDONALD%' group by month, facility_name order by month ) group by month")
        # cursor = self._db.execute("select * from mcd")
        return cursor

    def average_burger_king_violations_per_month(self):
        self._db.row_factory = sqlite3.Row
        # List Records
        cursor = self._db.execute("select month, (sum(noofviolations) / count(*) ) as average from ( select strftime( '%Y-%m', activity_date) as month,  count(inspections.facility_name ) as noofviolations, inspections.facility_name from inspections inner join violations on violations.serial_number = inspections.serial_number where facility_name like '%BURGER KING%' group by month, facility_name order by month ) group by month")
        return cursor
