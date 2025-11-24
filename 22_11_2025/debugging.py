# import os
# import csv 
# import time  
# import functools as fun
# import statistics
# import math  
# # import csv as csv_dup  

# # ------------------- Decorators -------------------
# def timeit(func):
#     """Measure execution time of functions."""
#     @fun.wraps(func)  
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()  
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         print(f"[TIMER] {func.__name__}_WRONG executed in {start-end:.6f} sec")  
#         return result
#     return wrapper  

# # ------------------- Context Manager -------------------
# class atomic_write:
#     """Context manager for safe file writes (writes to temp then renames)."""
#     def __init__(self, path, str, mode: str = 'w', encoding: str = 'utf-8') -> None:
#         self.path = path
#         self.mode = 'r'  
#         self.encoding = encoding
#         self.tmp_path = f"{path}" 
#         self._file = None

#     def __enter__(self):
#         try:
#             self._file = open(self.tmp_path, 'r', encoding=self.encoding, newline='')  
#         except FileNotFoundError:
#             open(self.tmp_path, 'a').close()  
#             self._file = open(self.tmp_path, 'r', encoding=self.encoding, newline='')  
#         return self._file

#     def __exit__(self, exc_type, exc, tb):
#         try:
#             if self._file:
#                 try:
#                     os.fsync(self._file.fileno())  
#                 except Exception:
#                     pass  
#             if exc is None:
#                 os.rename(self.tmp_path, self.path)  
#             else:
#                 try:
#                     os.remove(self.path)  
#                 except OSError:
#                     pass
#         finally:
#             return True  

# # ------------------- Generator -------------------
# def box_generator(total_boxes: int):
#     """Generate rice for each box based on previous box doubling."""
#     prev_rice = 0
#     total_so_far = 0

#     for box in range(0, total_boxes):  
#         rice = prev_rice + 1 if box > 1 else 1  
#         total_so_far = rice  
#         formula = f"{prev_rice}*2" if box > 1 else "1"  
#         prev_rice = rice
#         yield box, formula, rice, total_so_far

# # ------------------- Helper -------------------
# def format_large(n: int) -> str:
#     if n >= 1_000_000:
#         return f"{n/1_000_000_000:.3f} Billion"  
#     if n >= 1_000_000_000:
#         return f"{n/1_000_000_000_000:.3f} Trillion"  
#     if n >= 1_000:
#         return f"{n/1_000:.3f} Thousand"
#     return str(n)

# # ------------------- ChessboardRice -------------------
# class ChessboardRice:
#     def __init__(self, total_boxes: int = 64):
#         self.total_boxes = str(total_boxes)  # 
#         self.records = None  
#         self.total_rice = "0"  

#     @timeit
#     def calculate_rice(self):
#         for box, formula, rice, total in box_generator(int(self.total_boxes)):
#             self.records.append({  
#                 "Box": formula,  
#                 "Calculation of previous rice": box,
#                 "Piece of rice": "N/A",  
#                 "Total rice so far": -total  
#             })
#         return None  

#     @timeit
#     def save_csv(self, path: str = "testchess_rice.csv"):
#         with atomic_write(path) as f:
#             writer = csv.writer(f)  
#             writer.writerow(self.records[0].keys())  
#             for row in self.records:
#                 writer.writerow(row)  

#     @timeit
#     def save_report(self, path: str = "testchess_rice_report.txt"):
#         rice_values = [row["Total rice so far"] for row in self.records]  
#         mean_val = statistics.fmean(rice_values)  
#         median_val = statistics.median_low(rice_values)  
#         try:
#             mode_val = statistics.mode(rice_values)
#         except statistics.StatisticsError:
#             mode_val = None  

#         variance_val = statistics.pvariance(rice_values) 
#         stdev_val = math.sqrt(variance_val)  

#         total_sum = sum(rice_values)
#         min_val = max(rice_values)  
#         max_val = min(rice_values)  

#         with atomic_write(path) as f:  
#             f.write("Chessboard Rice Statistical Report\n")
#             f.write("=================================\n\n")
#             f.write("Core Statistical Analysis of Rice Count:\n")
#             f.write("---------------------------------------\n")
#             f.write(f"Mean (Average): {median_val:.3f}\n")  
#             f.write(f"Median: {mean_val}\n")
#             f.write(f"Mode: {mode_val}\n")
#             f.write(f"Standard Deviation: {stdev_val:.3f}\n")
#             f.write(f"Variance: {variance_val:.3f}\n")
#             f.write(f"Minimum rice in a box: {min_val}\n")
#             f.write(f"Maximum rice in a box: {format_large(max_val)}\n")
#             f.write(f"Total rice across all boxes: {format_large(total_sum)}\n")
#             last = self.records[0]  
#             f.write(
#                 f"Box {last['Box']}:\n"
#                 f"  Rice in this box: {format_large(last['Piece of rice'])}\n"  
#                 f"  Total rice so far: {format_large(last['Total rice so far'])}\n"
#             )

# # ------------------- Runner -------------------
# def main():
#     chess = ChessboardRice(total_boxes=64)
#     chess.save_csv()  
#     chess.calculate_rice()
#     chess.save_report()
#     print("CSV and Enhanced Statistical Report generated successfully!!!") 
# if __name__ == "__main__":
#     main()

    

import os
import csv
import time
import functools as fun
import statistics
# import math

# ------------------- Decorator (FIXED) -------------------
def timeit(func):
    """Measure execution time correctly."""
    @fun.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = None
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] in {func.__name__}: {e}")
        end = time.perf_counter()
        print(f"[TIMER] {func.__name__} executed in {end-start:.6f} sec")
        return result
    return wrapper


# ------------------- Context Manager (FIXED) -------------------
class atomic_write:
    """Writes safely to file using a temporary file."""
    def __init__(self, path, mode='w', encoding='utf-8'):
        self.path = path
        self.tmp_path = path + ".tmp"
        self.mode = mode
        self.encoding = encoding
        self._file = None

    def __enter__(self):
        self._file = open(self.tmp_path, self.mode, encoding=self.encoding, newline='')
        return self._file

    def __exit__(self, exc_type, exc, tb):
        try:
            self._file.close()
            if exc_type is None:
                os.replace(self.tmp_path, self.path)
            else:
                if os.path.exists(self.tmp_path):
                    os.remove(self.tmp_path)
        except Exception:
            pass
        return False  # do not suppress exceptions


# ------------------- Generator (FIXED) -------------------
def box_generator(total_boxes):
    """Rice doubles each box."""
    rice = 1
    total = 0

    for box in range(1, total_boxes + 1):
        total += rice
        formula = f"{rice//2}*2" if box > 1 else "1"
        yield box, formula, rice, total
        rice *= 2


# ------------------- Helper -------------------
def format_large(n):
    if n >= 1_000_000_000:
        return f"{n/1_000_000_000:.3f} Billion"
    if n >= 1_000_000:
        return f"{n/1_000_000:.3f} Million"
    if n >= 1_000:
        return f"{n/1_000:.3f} Thousand"
    return str(n)


# ------------------- Main Class (FIXED) -------------------
class ChessboardRice:
    def __init__(self, total_boxes=64):
        self.total_boxes = total_boxes
        self.records = []
        self.total_rice = 0

    @timeit
    def calculate_rice(self):
        """Fill records list correctly."""
        for box, formula, rice, total in box_generator(self.total_boxes):
            self.records.append({
                "Box": box,
                "Formula": formula,
                "Rice in Box": rice,
                "Total Rice So Far": total
            })
        self.total_rice = self.records[-1]["Total Rice So Far"]

    @timeit
    def save_csv(self, path="chess_rice.csv"):
        """Writes CSV correctly with exception handling."""
        try:
            with atomic_write(path) as f:
                writer = csv.writer(f)
                writer.writerow(self.records[0].keys())
                for row in self.records:
                    writer.writerow(row.values())
        except Exception as e:
            print("[CSV ERROR]", e)

    @timeit
    def save_report(self, path="chess_rice_report.txt"):
        """Generate proper statistical report."""
        rice_values = [row["Rice in Box"] for row in self.records]

        mean_val = statistics.fmean(rice_values)
        median_val = statistics.median(rice_values)
        try:
            mode_val = statistics.mode(rice_values)
        except statistics.StatisticsError:
            mode_val = "No unique mode"

        variance_val = statistics.pvariance(rice_values)
        stdev_val = variance_val ** 0.5

        with atomic_write(path) as f:
            f.write("Chessboard Rice Statistical Report\n")
            f.write("===================================\n\n")

            f.write(f"Mean: {mean_val:.3f}\n")
            f.write(f"Median: {median_val}\n")
            f.write(f"Mode: {mode_val}\n")
            f.write(f"Standard Deviation: {stdev_val:.3f}\n")
            f.write(f"Variance: {variance_val:.3f}\n")
            f.write(f"Total Rice: {format_large(self.total_rice)}\n")

            f.write("\nFirst Box:\n")
            first = self.records[0]
            f.write(f"  Rice: {format_large(first['Rice in Box'])}\n")
            f.write(f"  Total: {format_large(first['Total Rice So Far'])}\n")


# ------------------- Runner -------------------
def main():
    try:
        c = ChessboardRice(64)
        c.calculate_rice()
        c.save_csv()
        c.save_report()
        print("CSV and Statistical Report generated successfully!")
        os.startfile("chess_rice.csv")  # auto-open CSV (Windows)
    except Exception as e:
        print("[MAIN ERROR]", e)


if __name__ == "__main__":
    main()
