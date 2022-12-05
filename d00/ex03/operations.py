import sys
import argparse

if __name__ == "__main__":
    ac = len(sys.argv)
    if ac == 1:
        sys.exit(1)
    parser = argparse.ArgumentParser()
    parser.add_argument('A', type=int)
    parser.add_argument('B', type=int)
    args = parser.parse_args()
    op_list = ["Sum:", "Difference:", "Product:", "Quotient:", "Remainder:"]
    print(op_list[0]+("Difference:".__len__() - op_list[0].__len__() + 1) * " " + str(args.A + args.B))
    print(op_list[1]+("Difference:".__len__() - op_list[1].__len__() + 1) * " " + str(args.A - args.B))
    print(op_list[2]+("Difference:".__len__() - op_list[2].__len__() + 1) * " " + str(args.A * args.B))
    if args.B == 0:
         print(op_list[3]+("Difference:".__len__() - op_list[3].__len__() + 1) * " " + "ERROR (division by zero)")
         print(op_list[4]+("Difference:".__len__() - op_list[4].__len__() + 1) * " " + "ERROR (modulo by zero)")
    else:
        print(op_list[3]+("Difference:".__len__() - op_list[3].__len__() + 1) * " " + str(args.A / args.B))
        print(op_list[4]+("Difference:".__len__() - op_list[4].__len__() + 1) * " " + str(args.A % args.B))
