#!/usr/bin/env python3
import sys

def main():
    # اطبع كل الوسائط بدون اسم الملف
    for arg in sys.argv[1:]:
        print(arg)

if __name__ == "__main__":
    main()
