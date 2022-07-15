import subprocess

def main():
    status, output = subprocess.getstatusoutput("for f in `find . -type f -name '*.xml'`; do xmlformat --outfile $f --infile $f; done")
    print(output)
    return status

if __name__ == '__main__':
    raise SystemExit(main())