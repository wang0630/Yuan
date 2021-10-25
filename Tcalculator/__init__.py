import csv
import math


class Tcalculator:
    def __init__(self):
        self.vg_list = []
        self.abs_id_list = []
        self.log_slope_list = []

    def calculate(self, file_name, vd_constraints):
        print(file_name)
        # Reset all the lists
        self.vg_list = []
        self.abs_id_list = []
        self.log_slope_list = []

        x_axis = y_axis = None
        vgx1 = vgx2 = vgy1 = vgy2 = log_vgy1 = log_vgy2 = None
        max_slope = max_x = max_y = max_x1 = max_y1 = None
        with open(file_name, newline='', encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == "DataName":
                    for index, r in enumerate(row):
                        row[index] = r.strip()
                    x_axis = row.index("Vg")
                    y_axis = row.index("abs_Id")
                    vd_axis = row.index("Vd")
                elif row[0] == "DataValue":
                    vd = float(row[vd_axis])
                    if vd_constraints and vd not in vd_constraints:
                        continue
                    vgx2 = float(row[x_axis])
                    vgy2 = float(row[y_axis])
                    log_vgy2 = math.log(vgy2, 10)
                    if vgy1 is not None:
                        delta_x = vgx2 - vgx1
                        delta_y = vgy2 - vgy1
                        delta_logy = log_vgy2 - log_vgy1
                        if delta_x == 0:
                            break
                        # calculate slope
                        slope = delta_y / delta_x
                        log_slope = delta_logy / delta_x
                        self.log_slope_list.append(log_slope)
                        if max_slope is None:
                            max_slope = slope
                            max_x, max_y, max_x1, max_y1 = vgx2, vgy2, vgx1, vgy1
                        else:
                            if abs(slope) > abs(max_slope):
                                max_slope = slope
                                max_x, max_y, max_x1, max_y1 = vgx2, vgy2, vgx1, vgy1
                    vgx1 = vgx2
                    vgy1 = vgy2
                    log_vgy1 = log_vgy2
                    self.vg_list.append(vgx1)
                    self.abs_id_list.append(vgy1)

            # print(max_slope)
            # print(f"{max_x1}, {max_y1}")
            # print(f"{max_x}, {max_y}")
            b = max_y1 - (max_slope * max_x1)
            x_intercept = -1 * (b / max_slope)
            # print(f"x_intercept: {x_intercept}")
            max_log_slope = self.find_max_log_slope(x_intercept)
            return {
                "x1": f"X1: {'{:0.3e}'.format(max_x1)}",
                "y1": f"Y1: {'{:0.3e}'.format(max_y1)}",
                "x2": f"X2: {'{:0.3e}'.format(max_x)}",
                "y2": f"Y2: {'{:0.3e}'.format(max_y)}",
                "x_intercept": f"X intercept {str(round(x_intercept, 4))}",
                "SS": f"SS: {'{:0.3e}'.format(max_log_slope)}"
            }

    def find_max_log_slope(self, x_intercept):
        # vg the least number which is larger than x_intercept
        least_number = float('inf')
        index = None
        for i, vg in enumerate(self.vg_list):
            if vg < x_intercept:
                continue
            if vg < least_number:
                least_number = vg
                index = i

        abs_id_start_pt = self.abs_id_list[index]
        max_log_slope = float('-inf')
        # max_log_slope_index = None

        for i, abs_id in enumerate(self.abs_id_list[index:]):
            if abs_id < (abs_id_start_pt / 100):
                break

            if abs(self.log_slope_list[index+i]) > max_log_slope:
                # Debug
                # max_log_slope_index = index + i
                max_log_slope = abs(self.log_slope_list[index+i])

        return 1 / max_log_slope
