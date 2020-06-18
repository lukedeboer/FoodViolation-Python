from DbConnect import DbConnect


class SqlFood(DbConnect):
    def __init__(self):
        self.get_violations()

    @staticmethod
    def get_violations():
        # Getting distinct violation
        connect = DbConnect()
        cursor = connect.distinct_violations()

        for item in cursor:
            print("Serial Number: {}, Name: {}, Address: {}, ZipCode: {}, City: {}, Violations Count: {}"
                  .format(item["serial_number"], item["name"], item["address"], item["zipcode"], item["city"],
                          item["violations"]))
            connect.add_previous_violations(item["serial_number"], item["name"], item["address"], item["zipcode"], item["city"],
                                   int(item["violations"]))


def main():
    SqlFood()


if __name__ == '__main__': main()
