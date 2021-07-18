import csv


class Tcalculator:
    def calculate(self, file_name):
        print(file_name)
        x_axis = y_axis = None
        vgx1 = vgx2 = vgy1 = vgy2 = None
        max_slope = max_x = max_y = max_x1 = max_y1 = None
        with open(file_name, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == "DataName":
                    for index, r in enumerate(row):
                        row[index] = r.strip()
                    x_axis = row.index("Vg")
                    y_axis = row.index("abs_Id")
                    vd_axis = row.index("Vd")
                if row[0] == "DataValue":
                    vd = float(row[vd_axis])
                    if vd != -1 * 0.1 and vd != -1 * 0.05:
                        continue
                    vgx2 = float(row[x_axis])
                    vgy2 = float(row[y_axis])
                    if vgy1 is not None:
                        delta_x = vgx2 - vgx1
                        delta_y = vgy2 - vgy1
                        if delta_x == 0:
                            break
                        # calculate slope
                        slope = delta_y / delta_x
                        if max_slope is None:
                            max_slope = slope
                            max_x, max_y, max_x1, max_y1 = vgx2, vgy2, vgx1, vgy1
                        else:
                            if abs(slope) > abs(max_slope):
                                max_slope = slope
                                max_x, max_y, max_x1, max_y1 = vgx2, vgy2, vgx1, vgy1
                    vgx1 = vgx2
                    vgy1 = vgy2
            print(max_slope)
            print(f"{max_x1}, {max_y1}")
            print(f"{max_x}, {max_y}")
            b = max_y1 - (max_slope * max_x1)
            x_intercept = -1 * (b / max_slope)
            print(f"x_intercept: {x_intercept}")
