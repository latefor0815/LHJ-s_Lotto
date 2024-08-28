import random
from collections import Counter

# 과거 당첨 번호 데이터 예시 (보너스 번호 제외, 전체 494회차 데이터 추가)
past_winning_numbers = [
    [10, 23, 29, 33, 37, 40],
    [9, 13, 21, 25, 32, 42],
    [11, 16, 19, 21, 27, 31],
    [14, 27, 30, 31, 40, 42],
    [16, 24, 29, 40, 41, 42],
    [14, 15, 26, 27, 40, 42],
    [2, 9, 16, 25, 26, 40],
    [8, 19, 25, 34, 37, 39],
    [2, 4, 16, 17, 36, 39],
    [9, 25, 30, 33, 41, 44],
    [1, 7, 36, 37, 41, 42],
    [2, 11, 21, 25, 39, 45],
    [22, 23, 25, 37, 38, 42],
    [2, 6, 12, 31, 33, 40],
    [3, 4, 16, 30, 31, 37],
    [6, 7, 24, 37, 38, 40],
    [3, 4, 9, 17, 32, 37],
    [3, 12, 13, 19, 32, 35],
    [6, 30, 38, 39, 40, 43],
    [10, 14, 18, 20, 23, 30],
    [6, 12, 17, 18, 31, 32],
    [4, 5, 6, 8, 17, 39],
    [5, 13, 17, 18, 33, 42],
    [7, 8, 27, 29, 36, 43],
    [2, 4, 21, 26, 43, 44],
    [4, 5, 7, 18, 20, 25],
    [1, 20, 26, 28, 37, 43],
    [9, 18, 23, 25, 35, 37],
    [1, 5, 13, 34, 39, 40],
    [8, 17, 20, 35, 36, 44],
    [7, 9, 18, 23, 28, 35],
    [6, 14, 19, 25, 34, 44],
    [4, 7, 32, 33, 40, 41],
    [9, 26, 35, 37, 40, 42],
    [2, 3, 11, 26, 37, 43],
    [1, 10, 23, 26, 28, 40],
    [7, 27, 30, 33, 35, 37],
    [16, 17, 22, 30, 37, 43],
    [6, 7, 13, 15, 21, 43],
    [7, 13, 18, 19, 25, 26],
    [13, 20, 23, 35, 38, 43],
    [17, 18, 19, 21, 23, 32],
    [6, 31, 35, 38, 39, 44],
    [3, 11, 21, 30, 38, 45],
    [1, 10, 20, 27, 33, 35],
    [8, 13, 15, 23, 31, 38],
    [14, 17, 26, 31, 36, 45],
    [6, 10, 18, 26, 37, 38],
    [4, 7, 16, 19, 33, 40],
    [2, 10, 12, 15, 22, 44],
    [2, 3, 11, 16, 26, 44],
    [2, 4, 15, 16, 20, 29],
    [7, 8, 14, 32, 33, 39],
    [1, 8, 21, 27, 36, 39],
    [17, 21, 31, 37, 40, 44],
    [10, 14, 30, 31, 33, 37],
    [7, 10, 16, 25, 29, 44],
    [10, 24, 25, 33, 40, 44],
    [6, 29, 36, 39, 41, 45],
    [2, 8, 25, 36, 39, 42],
    [14, 15, 19, 30, 38, 43],
    [3, 8, 15, 27, 29, 35],
    [3, 20, 23, 36, 38, 40],
    [14, 15, 18, 21, 26, 36],
    [4, 25, 33, 36, 40, 43],
    [2, 3, 7, 17, 22, 24],
    [3, 7, 10, 15, 36, 38],
    [10, 12, 15, 16, 26, 39],
    [5, 8, 14, 15, 19, 39],
    [5, 19, 22, 25, 28, 43],
    [5, 9, 12, 16, 29, 41],
    [2, 4, 11, 17, 26, 27],
    [3, 12, 18, 32, 40, 43],
    [6, 15, 17, 18, 35, 40],
    [2, 5, 24, 32, 34, 44],
    [1, 3, 15, 22, 25, 37],
    [2, 18, 29, 32, 43, 44],
    [10, 13, 25, 29, 33, 35],
    [3, 12, 24, 27, 30, 32],
    [17, 18, 24, 25, 26, 30],
    [5, 7, 11, 13, 20, 33],
    [1, 2, 3, 14, 27, 42],
    [6, 10, 15, 17, 19, 34],
    [16, 23, 27, 34, 42, 45],
    [6, 8, 13, 23, 31, 36],
    [2, 12, 37, 39, 41, 45],
    [4, 12, 16, 23, 34, 43],
    [1, 17, 20, 24, 30, 41],
    [4, 26, 28, 29, 33, 40],
    [17, 20, 29, 35, 38, 44],
    [1, 21, 24, 26, 29, 42],
    [3, 14, 24, 33, 35, 36],
    [6, 22, 24, 36, 38, 44],
    [5, 32, 34, 40, 41, 45],
    [8, 17, 27, 31, 34, 43],
    [1, 3, 8, 21, 22, 31],
    [6, 7, 14, 15, 20, 36],
    [6, 9, 16, 23, 24, 32],
    [1, 3, 10, 27, 29, 37],
    [1, 7, 11, 23, 37, 42],
    [1, 3, 17, 32, 35, 45],
    [17, 22, 24, 26, 35, 40],
    [5, 14, 15, 27, 30, 45],
    [17, 32, 33, 34, 42, 44],
    [8, 10, 20, 34, 41, 45],
    [4, 10, 12, 22, 24, 33],
    [1, 4, 5, 6, 9, 31],
    [7, 18, 22, 23, 29, 44],
    [1, 5, 34, 36, 42, 44],
    [7, 20, 22, 23, 29, 43],
    [7, 18, 31, 33, 36, 40],
    [26, 29, 30, 33, 41, 42],
    [4, 9, 28, 33, 36, 45],
    [11, 14, 19, 26, 28, 41],
    [1, 2, 6, 9, 25, 28],
    [2, 4, 25, 31, 34, 37],
    [5, 10, 22, 34, 36, 44],
    [3, 4, 10, 17, 19, 22],
    [3, 11, 13, 14, 17, 21],
    [4, 6, 10, 11, 32, 37],
    [12, 28, 30, 34, 38, 43],
    [1, 11, 16, 17, 36, 40],
    [7, 17, 18, 28, 30, 45],
    [4, 16, 23, 25, 29, 42],
    [2, 8, 32, 33, 35, 36],
    [7, 20, 22, 27, 40, 43],
    [3, 5, 10, 29, 32, 43],
    [12, 30, 34, 36, 37, 45],
    [19, 23, 25, 28, 38, 42],
    [7, 19, 24, 27, 42, 45],
    [8, 10, 11, 14, 15, 21],
    [3, 17, 23, 34, 41, 45],
    [4, 7, 15, 18, 23, 26],
    [3, 12, 20, 23, 31, 35],
    [6, 14, 22, 28, 35, 39],
    [2, 16, 30, 36, 41, 42],
    [7, 9, 20, 25, 36, 39],
    [10, 11, 27, 28, 37, 39],
    [9, 11, 15, 20, 28, 43],
    [3, 13, 17, 18, 19, 28],
    [8, 12, 29, 31, 42, 43],
    [12, 16, 30, 34, 40, 44],
    [26, 27, 28, 42, 43, 45],
    [4, 15, 17, 26, 36, 37],
    [2, 3, 13, 20, 27, 44],
    [2, 19, 27, 35, 41, 42],
    [4, 6, 13, 21, 40, 42],
    [21, 25, 33, 34, 35, 36],
    [2, 11, 21, 34, 41, 42],
    [2, 18, 25, 28, 37, 39],
    [1, 2, 10, 13, 18, 19],
    [1, 5, 13, 26, 29, 34],
    [3, 8, 11, 12, 13, 36],
    [6, 19, 21, 35, 40, 45],
    [16, 19, 20, 32, 33, 41],
    [5, 18, 28, 30, 42, 45],
    [19, 26, 30, 33, 35, 39],
    [4, 9, 13, 18, 21, 34],
    [1, 18, 30, 41, 42, 43],
    [3, 7, 8, 34, 39, 41],
    [22, 34, 36, 40, 42, 45],
    [1, 5, 21, 25, 38, 41],
    [7, 11, 26, 28, 29, 44],
    [6, 9, 10, 11, 39, 41],
    [5, 13, 18, 19, 22, 42],
    [9, 12, 27, 36, 39, 45],
    [24, 27, 28, 30, 36, 39],
    [3, 10, 31, 40, 42, 43],
    [16, 27, 35, 37, 43, 45],
    [2, 11, 13, 15, 31, 42],
    [4, 16, 25, 29, 34, 35],
    [4, 19, 21, 24, 26, 41],
    [3, 9, 24, 30, 33, 34],
    [13, 14, 18, 22, 35, 39],
    [19, 26, 28, 31, 33, 36],
    [4, 17, 30, 32, 33, 34],
    [1, 10, 13, 16, 37, 43],
    [1, 5, 11, 12, 18, 23],
    [5, 9, 17, 25, 39, 43],
    [2, 15, 20, 21, 29, 34],
    [14, 21, 23, 32, 40, 45],
    [13, 15, 27, 29, 34, 40],
    [2, 18, 24, 34, 40, 42],
    [1, 2, 6, 16, 20, 33],
    [1, 2, 4, 8, 19, 38],
    [4, 10, 14, 19, 21, 45],
    [1, 2, 8, 18, 29, 38],
    [19, 24, 27, 30, 31, 34],
    [8, 14, 32, 35, 37, 45],
    [8, 14, 18, 30, 31, 44],
    [5, 6, 24, 25, 32, 37],
    [4, 8, 11, 18, 37, 45],
    [6, 14, 18, 26, 36, 39],
    [15, 20, 23, 26, 39, 44],
    [7, 10, 19, 22, 35, 40],
    [35, 36, 37, 41, 44, 45],
    [7, 12, 16, 34, 42, 45],
    [12, 19, 20, 25, 41, 45],
    [14, 21, 22, 25, 30, 36],
    [5, 6, 13, 14, 17, 20],
    [3, 11, 24, 38, 39, 44],
    [12, 14, 27, 33, 39, 44],
    [1, 3, 11, 24, 30, 32],
    [3, 12, 14, 35, 40, 45],
    [1, 3, 21, 29, 35, 37],
    [1, 2, 3, 15, 20, 25],
    [3, 11, 14, 31, 32, 37],
    [14, 25, 31, 34, 40, 44],
    [2, 7, 18, 20, 24, 33],
    [10, 19, 22, 23, 25, 37],
    [12, 13, 17, 20, 33, 41],
    [11, 12, 18, 21, 31, 38],
    [2, 3, 4, 5, 20, 24],
    [5, 7, 20, 25, 28, 37],
    [2, 3, 7, 15, 43, 44],
    [7, 16, 17, 33, 36, 40],
    [16, 20, 27, 33, 35, 39],
    [1, 8, 14, 18, 29, 44],
    [4, 11, 20, 26, 35, 37],
    [5, 11, 19, 21, 34, 43],
    [2, 20, 33, 35, 37, 40],
    [5, 7, 28, 29, 39, 43],
    [1, 3, 18, 20, 26, 27],
    [4, 19, 26, 27, 30, 42],
    [5, 11, 13, 19, 31, 36],
    [2, 6, 8, 14, 21, 22],
    [4, 5, 15, 16, 22, 42],
    [17, 25, 35, 36, 39, 44],
    [4, 5, 9, 11, 23, 38],
    [5, 11, 14, 29, 32, 33],
    [5, 10, 19, 31, 44, 45],
    [8, 9, 10, 12, 24, 44],
    [4, 6, 13, 17, 28, 40],
    [13, 21, 22, 24, 26, 37],
    [21, 22, 26, 27, 31, 37],
    [1, 4, 8, 13, 37, 39],
    [1, 11, 17, 21, 24, 44],
    [2, 4, 15, 28, 31, 34],
    [11, 15, 24, 39, 41, 44],
    [6, 10, 16, 40, 41, 43],
    [2, 16, 24, 27, 28, 35],
    [4, 19, 20, 21, 32, 34],
    [2, 12, 17, 19, 28, 42],
    [13, 16, 25, 36, 37, 38],
    [9, 11, 27, 31, 32, 38],
    [13, 18, 21, 23, 26, 39],
    [12, 15, 28, 36, 39, 40],
    [3, 8, 17, 23, 38, 45],
    [3, 8, 27, 31, 41, 44],
    [19, 23, 30, 37, 43, 45],
    [6, 7, 19, 25, 28, 38],
    [14, 23, 26, 31, 39, 45],
    [8, 19, 25, 31, 34, 36],
    [1, 5, 19, 20, 24, 30],
    [1, 5, 6, 24, 27, 42],
    [4, 11, 14, 21, 23, 43],
    [6, 13, 27, 31, 32, 37],
    [14, 27, 30, 31, 38, 40],
    [4, 5, 14, 35, 42, 45],
    [7, 12, 15, 24, 37, 40],
    [6, 11, 16, 18, 31, 43],
    [9, 12, 24, 25, 29, 31],
    [1, 27, 28, 32, 37, 40],
    [9, 16, 27, 36, 41, 44],
    [5, 9, 34, 37, 38, 39],
    [3, 4, 9, 11, 22, 42],
    [7, 8, 24, 34, 36, 41],
    [3, 10, 19, 24, 32, 45],
    [5, 18, 20, 36, 42, 43],
    [5, 9, 12, 20, 21, 26],
    [3, 8, 9, 27, 29, 40],
    [7, 9, 12, 27, 39, 43],
    [1, 8, 24, 31, 34, 44],
    [13, 14, 15, 26, 35, 39],
    [14, 19, 20, 35, 38, 40],
    [4, 15, 21, 33, 39, 41],
    [10, 12, 13, 15, 25, 29],
    [3, 11, 37, 39, 41, 43],
    [7, 16, 31, 36, 37, 38],
    [10, 11, 23, 24, 36, 37],
    [1, 3, 4, 6, 14, 41],
    [2, 5, 10, 18, 31, 32],
    [6, 8, 18, 31, 38, 45],
    [2, 7, 15, 24, 30, 45],
    [13, 33, 37, 40, 41, 45],
    [1, 15, 19, 40, 42, 44],
    [6, 12, 24, 27, 35, 37],
    [1, 12, 17, 28, 35, 41],
    [3, 14, 33, 37, 38, 42],
    [8, 13, 18, 32, 39, 45],
    [3, 7, 8, 18, 20, 42],
    [17, 18, 31, 32, 33, 34],
    [1, 9, 17, 21, 29, 33],
    [6, 10, 17, 30, 37, 38],
    [1, 4, 12, 16, 18, 38],
    [3, 8, 15, 27, 30, 45],
    [6, 11, 19, 20, 28, 32],
    [5, 9, 27, 29, 37, 40],
    [1, 3, 20, 25, 36, 45],
    [7, 9, 10, 12, 26, 38],
    [7, 11, 13, 33, 37, 43],
    [13, 19, 20, 32, 38, 42],
    [2, 14, 17, 30, 38, 45],
    [4, 10, 16, 26, 33, 41],
    [7, 8, 18, 21, 23, 39],
    [4, 18, 23, 30, 34, 41],
    [5, 15, 21, 23, 25, 45],
    [14, 15, 17, 19, 37, 45],
    [1, 2, 5, 11, 18, 36],
    [1, 5, 19, 28, 34, 41],
    [4, 12, 24, 27, 28, 32],
    [2, 3, 5, 6, 12, 20],
    [9, 17, 34, 35, 43, 45],
    [15, 17, 19, 34, 38, 41],
    [1, 13, 33, 35, 43, 45],
    [10, 11, 21, 27, 31, 39],
    [3, 10, 11, 22, 36, 39],
    [2, 17, 19, 20, 34, 45],
    [5, 8, 22, 28, 33, 42],
    [16, 19, 23, 25, 41, 45],
    [12, 18, 20, 21, 25, 34],
    [9, 18, 29, 32, 38, 43],
    [10, 14, 15, 32, 36, 42],
    [2, 4, 21, 25, 33, 36],
    [7, 17, 20, 32, 44, 45],
    [16, 23, 25, 33, 36, 39],
    [6, 12, 13, 17, 32, 44],
    [1, 6, 9, 16, 17, 28],
    [9, 17, 19, 30, 35, 42],
    [3, 4, 16, 17, 19, 20],
    [4, 9, 14, 26, 31, 44],
    [16, 17, 34, 36, 42, 45],
    [5, 14, 27, 30, 39, 43],
    [13, 15, 21, 29, 39, 43],
    [5, 9, 16, 23, 26, 45],
    [3, 5, 20, 34, 35, 44],
    [1, 5, 14, 18, 32, 37],
    [2, 13, 34, 38, 42, 45],
    [6, 8, 14, 21, 30, 37],
    [18, 24, 26, 29, 34, 38],
    [1, 8, 19, 34, 39, 43],
    [1, 13, 14, 33, 34, 43],
    [1, 10, 17, 29, 31, 43],
    [1, 2, 15, 28, 34, 45],
    [15, 20, 23, 29, 39, 42],
    [5, 13, 14, 22, 44, 45],
    [3, 8, 13, 27, 32, 42],
    [3, 14, 17, 20, 24, 31],
    [5, 13, 14, 20, 24, 25],
    [1, 8, 18, 24, 29, 33],
    [5, 25, 27, 29, 34, 36],
    [5, 16, 17, 20, 26, 41],
    [11, 16, 19, 22, 29, 36],
    [14, 19, 36, 43, 44, 45],
    [5, 8, 29, 30, 35, 44],
    [2, 8, 14, 25, 29, 45],
    [10, 14, 18, 21, 36, 37],
    [1, 9, 10, 12, 21, 40],
    [1, 10, 19, 20, 24, 40],
    [4, 16, 23, 25, 35, 40],
    [5, 10, 16, 24, 27, 35],
    [2, 3, 22, 27, 30, 40],
    [11, 12, 14, 21, 32, 38],
    [2, 5, 7, 14, 16, 40],
    [5, 15, 21, 25, 26, 30],
    [5, 12, 19, 26, 27, 44],
    [3, 22, 25, 29, 32, 44],
    [11, 21, 24, 30, 39, 45],
    [17, 20, 35, 36, 41, 43],
    [16, 18, 24, 42, 44, 45],
    [7, 9, 15, 26, 27, 42],
    [8, 11, 14, 16, 18, 21],
    [15, 26, 37, 42, 43, 45],
    [11, 13, 15, 17, 25, 34],
    [4, 8, 19, 25, 27, 45],
    [1, 11, 13, 24, 28, 40],
    [6, 22, 29, 37, 43, 45],
    [5, 22, 29, 31, 34, 39],
    [6, 10, 22, 31, 35, 40],
    [1, 2, 8, 17, 26, 37],
    [1, 5, 10, 12, 16, 20],
    [10, 15, 22, 24, 27, 42],
    [4, 15, 28, 33, 37, 40],
    [11, 22, 24, 32, 36, 38],
    [7, 12, 19, 21, 29, 32],
    [4, 7, 10, 19, 31, 40],
    [1, 26, 31, 34, 40, 43],
    [1, 8, 9, 17, 29, 32],
    [7, 16, 18, 20, 23, 26],
    [16, 17, 28, 37, 39, 40],
    [10, 11, 18, 22, 28, 39],
    [1, 3, 7, 8, 24, 42],
    [9, 16, 28, 40, 41, 43],
    [1, 13, 20, 22, 25, 28],
    [11, 15, 20, 26, 31, 35],
    [18, 20, 31, 34, 40, 45],
    [12, 13, 17, 22, 25, 33],
    [10, 15, 20, 23, 42, 44],
    [1, 2, 9, 17, 19, 42],
    [9, 21, 27, 34, 41, 43],
    [6, 12, 18, 31, 38, 43],
    [5, 9, 15, 19, 22, 36],
    [10, 14, 22, 24, 28, 37],
    [5, 20, 21, 24, 33, 40],
    [1, 2, 10, 25, 26, 44],
    [7, 12, 21, 24, 27, 36],
    [6, 7, 13, 16, 24, 25],
    [9, 20, 21, 22, 30, 37],
    [6, 9, 21, 31, 32, 40],
    [1, 3, 18, 32, 40, 41],
    [11, 14, 22, 35, 37, 39],
    [4, 7, 39, 41, 42, 45],
    [2, 9, 15, 23, 34, 40],
    [2, 14, 15, 22, 23, 44],
    [7, 17, 20, 26, 30, 40],
    [5, 6, 8, 11, 22, 26],
    [4, 5, 14, 20, 22, 43],
    [11, 13, 15, 26, 28, 34],
    [2, 11, 13, 14, 28, 30],
    [4, 9, 10, 29, 31, 34],
    [6, 11, 26, 27, 28, 44],
    [8, 15, 19, 21, 34, 44],
    [1, 17, 27, 28, 29, 40],
    [10, 11, 26, 31, 34, 44],
    [8, 10, 14, 27, 33, 38],
    [4, 17, 18, 27, 39, 43],
    [6, 7, 15, 24, 28, 30],
    [12, 16, 19, 22, 37, 40],
    [3, 23, 28, 34, 39, 42],
    [1, 3, 16, 18, 30, 34],
    [18, 22, 25, 31, 38, 45],
    [2, 3, 5, 11, 27, 39],
    [19, 23, 29, 33, 35, 43],
    [3, 13, 20, 24, 33, 37],
    [8, 16, 26, 30, 38, 45],
    [9, 14, 20, 22, 33, 34],
    [11, 16, 29, 38, 41, 44],
    [6, 12, 20, 26, 29, 38],
    [17, 20, 30, 31, 37, 40],
    [10, 22, 28, 34, 36, 44],
    [1, 23, 28, 30, 34, 35],
    [25, 27, 29, 36, 38, 40],
    [4, 6, 10, 19, 20, 44],
    [11, 13, 23, 35, 43, 45],
    [13, 20, 21, 30, 39, 45],
    [1, 11, 12, 14, 26, 35],
    [2, 7, 8, 9, 17, 33],
    [3, 7, 13, 27, 40, 41],
    [3, 10, 20, 26, 35, 43],
    [6, 14, 19, 21, 23, 31],
    [12, 15, 20, 24, 30, 38],
    [8, 10, 18, 30, 32, 34],
    [12, 24, 33, 38, 40, 42],
    [13, 25, 27, 34, 38, 41],
    [4, 19, 20, 26, 30, 35],
    [1, 7, 12, 18, 23, 27],
    [8, 10, 18, 23, 27, 40],
    [4, 9, 10, 32, 36, 40],
    [4, 6, 10, 14, 25, 40],
    [8, 11, 28, 30, 43, 45],
    [11, 18, 26, 31, 37, 40],
    [3, 20, 24, 32, 37, 45],
    [23, 29, 31, 33, 34, 44],
    [6, 12, 15, 34, 42, 44],
    [1, 8, 11, 13, 22, 38],
    [4, 10, 13, 23, 32, 44],
    [2, 12, 14, 17, 24, 40],
    [8, 13, 15, 28, 37, 43],
    [4, 21, 22, 34, 37, 38],
    [10, 16, 20, 39, 41, 42],
    [6, 13, 29, 37, 39, 41],
    [16, 25, 26, 31, 36, 43],
    [8, 13, 20, 22, 23, 36],
    [4, 13, 18, 31, 33, 45],
    [1, 9, 14, 16, 21, 29],
    [9, 12, 13, 15, 37, 38],
    [14, 25, 29, 32, 33, 45],
    [18, 29, 30, 37, 39, 43],
    [8, 23, 25, 27, 35, 44],
    [3, 5, 10, 17, 30, 31],
    [3, 4, 23, 29, 40, 41],
    [1, 10, 16, 24, 25, 35],
    [12, 15, 19, 22, 28, 34],
    [1, 3, 27, 28, 32, 45],
    [17, 22, 26, 27, 36, 39],
    [1, 2, 23, 25, 38, 40],
    [4, 8, 25, 27, 37, 41],
    [2, 8, 17, 30, 31, 38],
    [2, 4, 8, 15, 20, 27],
    [2, 7, 26, 29, 40, 43],
    [8, 17, 35, 36, 39, 42],
    [22, 27, 31, 35, 37, 40],
    [20, 22, 26, 33, 36, 37],
    [5, 7, 8, 15, 30, 43],
    [5, 10, 11, 17, 28, 34],
    [1, 5, 8, 16, 28, 33],
    [10, 15, 24, 30, 31, 37],
    [1, 2, 6, 14, 27, 38],
    [15, 19, 21, 25, 27, 28],
    [4, 5, 9, 11, 37, 40],
    [6, 14, 25, 33, 40, 44],
    [3, 8, 17, 30, 33, 34],
    [13, 19, 21, 24, 34, 35],
    [3, 6, 21, 30, 34, 35],
    [2, 19, 26, 31, 38, 41],
    [1, 9, 12, 13, 20, 45],
    [6, 7, 19, 28, 34, 41],
    [13, 14, 20, 28, 29, 34],
    [3, 7, 9, 13, 19, 24],
]

def calculate_frequencies(past_numbers):
    """
    과거 당첨 번호들의 빈도를 계산합니다.
    """
    flat_numbers = [num for sublist in past_numbers for num in sublist]
    return Counter(flat_numbers)

def weighted_random_choice(frequencies):
    """
    번호의 빈도를 가중치로 사용하여 무작위로 번호를 선택합니다.
    """
    total = sum(frequencies.values())
    rand = random.uniform(0, total)
    upto = 0
    for number, freq in frequencies.items():
        if upto + freq >= rand:
            return number
        upto += freq
    return list(frequencies.keys())[0]

def generate_weighted_lotto_numbers(frequencies, count=6):
    """
    가중치 기반으로 번호를 선택하여 로또 번호 세트를 생성합니다.
    """
    selected_numbers = set()
    while len(selected_numbers) < count:
        selected_numbers.add(weighted_random_choice(frequencies))
    return sorted(selected_numbers)

if __name__ == "__main__":
    print("Starting the program...")
    frequencies = calculate_frequencies(past_winning_numbers)
    print("Frequencies:", frequencies)

    num_sets = 5  # 생성할 세트의 개수
    sets = []
    for i in range(num_sets):
        weighted_numbers = generate_weighted_lotto_numbers(frequencies)
        sets.append(weighted_numbers)
        print(f"Generated Lotto Numbers (Weighted) - Set {i + 1}: {weighted_numbers}")

    print("Program finished.")

    # 결과를 파일에 저장
    with open("generated_lotto_sets.txt", "w") as file:
        for i, lotto_set in enumerate(sets):
            file.write(f"Set {i + 1}: {lotto_set}\n")
    print("Results saved to generated_lotto_sets.txt")
