import sys
import argparse

def convert_temperature(from_scale, to_scale, value):
    from_scale = from_scale.lower()
    to_scale = to_scale.lower()

    if from_scale == "c":
        celsius = value
    elif from_scale == "f":
        celsius = (value - 32) * 5/9
    elif from_scale == "k":
        celsius = value - 273.15
    else:
        raise ValueError("Invalid source scale. Use c, f, or k.")

    if to_scale == "c":
        return celsius
    elif to_scale == "f":
        return (celsius * 9/5) + 32
    elif to_scale == "k":
        return celsius + 273.15
    else:
        raise ValueError("Invalid target scale. Use c, f, or k.")

def main():
 while True:
    parser = argparse.ArgumentParser(description="Temperature Converter")
    parser.add_argument("--from", dest="from_scale", required=True,
                        help="Source scale: c, f, k")
    parser.add_argument("--to", dest="to_scale", required=True,
                        help="Target scale: c, f, k")
    parser.add_argument("--value", required=True,
                        help="Numeric temperature value")
    args = parser.parse_args()
    try:
        value = float(args.value)
    except ValueError:
        sys.exit("ERROR: Value must be numeric.")

    try:
        result = convert_temperature(args.from_scale, args.to_scale, value)
    except ValueError as e:
        sys.exit(f"ERROR: {e}")

    print("\nConversion Successful")
    print(f"From: {value} {args.from_scale.upper()}")
    print(f"To:   {result:.2f} {args.to_scale.upper()}")

if __name__ == "__main__":
    main()
