#!/usr/bin/python3
import sys
import argparse
import xml.etree.ElementTree as ET

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--file', help='Input file containint nmap xml file')
    parser.add_argument('-v','--verbose', action='store_true', help='A port per line and include nmaps service.')
    args = parser.parse_args()

    tree = ET.parse(args.file)
    root = tree.getroot()

    results = []

    
    for host in root.findall('host'):
        address = host.find('address').get('addr')
        ports = host.find('ports')
        portlist = ports.findall('port')
        ports_out = []
        for port in portlist:
            if port.find('state').get('state') == 'open':
                ports_out.append(port.get('portid'))
                service = port.find('service').get('name')
                if args.verbose:
                    results.append(f"{address},{service},{port.get('portid')}")
        if not args.verbose:
            results.append(f"{address},{','.join(ports_out)}")


    for result in results:
        print(result)

if __name__ == "__main__":
    main()
