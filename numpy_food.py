import matplotlib.pyplot as plt
from DbConnect import DbConnect


class NumpyFood(DbConnect):
    def __init__(self):
        self.generate_pivot()

    @staticmethod
    def generate_pivot():
        connect = DbConnect()
        all_violations = connect.violations_per_month()
        # highest_violations = connect.highest_violations_per_month()
        # lowest_violations = connect.lowest_violations_per_month()

        # h_month = 0
        # h_no_of_violations = 0
        # for item in highest_violations:
        #     h_month = int(item["month"])
        #     h_no_of_violations = int(item["noofviolations"])
        #     break
        
        # l_month = ''
        # l_no_of_violations = 0
        # for item in lowest_violations:
        #     l_month = int(item["month"])
        #     l_no_of_violations = int(item["noofviolations"])
        #     break

        # # x-coordinates of left sides of bars
        # left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        # # heights of bars
        # height = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # print(h_no_of_violations)
        # print(l_no_of_violations)

        # height[h_month - 1] = h_no_of_violations


        # # labels for bars
        # tick_label = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        # colors = ['black', 'red', 'green', 'blue', 'cyan']
        # colors2 = ['green', 'blue', 'cyan']
        # plt.figure(1)
        # # plotting a bar chart
        # plt.bar(left, height, tick_label=tick_label,
        #         width=0.8, color=colors)
        # height[l_month - 1] = l_no_of_violations
        # plt.bar(left, height, tick_label=tick_label,
        #         width=0.8, color=colors2)

        # # naming the x-axis
        # plt.xlabel('Month')
        # # naming the y-axis
        # plt.ylabel('No of Violations')
        # # plot title
        # plt.title('Total Violations per month')

        tick_labels = []
        height_highest = []
        height_lowest = []
        height_average = []
        for col in (all_violations):
            tick_labels.append(col[0])
            height_highest.append(col[1])
            height_lowest.append(col[2])
            height_average.append(col[3])
            print(col[0], col[1], col[2], col[3])


        ax = plt.figure().add_subplot(111)
        ax.plot()
        ax.set_ylabel('No of Violations')
        ax.set_xlabel('Month')
        ax.set_title('Violations per month')
        ax.set_xticklabels(tick_labels)  # add monthlabels to the xaxis

        plt.plot(tick_labels, height_highest, 'go',label='Highest Violations')
        plt.plot(tick_labels, height_lowest, 'rs',label='Lowest Violations')
        plt.plot(tick_labels, height_average, 'b^',label='Average Violations')

        plt.xticks(tick_labels, tick_labels, rotation='vertical')

        legend = ax.legend(loc='best', shadow=False, fontsize='small')

        ## function to show the plot
        ## plt.figure(2)

        # McD and Burger King Data
        # Get average data
        avg_violations_of_mcd = connect.average_mcdonalds_violations_per_month()
        avg_violations_of_burger_king = connect.average_burger_king_violations_per_month()

        tick_label = []
        height = []
        for idx, col in (avg_violations_of_mcd):
            height.append(col)
            tick_label.append(idx)

        ax = plt.figure().add_subplot(111)
        ax.plot()
        ax.set_ylabel('No of Violations')
        ax.set_xlabel('Month')
        ax.set_title('Violations per month')
        ax.set_xticklabels(tick_label)  # add monthlabels to the xaxis

        plt.plot(tick_label,
                 height, 'go',label='McDonald\'s')

        plt.xticks(tick_label, tick_label, rotation='vertical')

        tick_label_burger_king = []
        height_burger_king = []
        for idx, col in (avg_violations_of_burger_king):
            height_burger_king.append(col)
            tick_label_burger_king.append(idx)

        plt.plot(tick_label_burger_king,
                 height_burger_king, 'ro',label='Burger King')

        # naming the x-axis
        plt.xlabel('Month')

        # naming the y-axis
        plt.ylabel('No of Violations')

        # plot title
        plt.title('Total Violations per month')

        legend = ax.legend(loc='best', shadow=False, fontsize='small')

        # function to show the plot
        plt.show()

def main():
    NumpyFood()


if __name__ == '__main__': main()
