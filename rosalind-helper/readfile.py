#!/usr/bin/env python3

# rf = read file
# rfl = read file by line
# rf2d = read file as 2d map

def rf(fp):
    return open(fp,'r').read().strip()

def rfl(fp):
    return [l.strip() for l in open(fp,'r').readlines()]

def rf2d(fp):
    global w, h # returns width and height
    map2d = []
    h = 0
    for l in open(fp,'r').readlines():
        l = l.strip()
        tmp = [x for x in range(len(l))]
        for i in range(len(l)):
            w = i+1
            tmp[i]=l[i]
        map2d.append(tmp)
        h+=1
    return map2d

if __name__ != __file__:
    try:
        import os
        import __main__ # to read the filename of the "main"
        filename = os.path.basename(__main__.__file__).replace(".py",".txt")
        input_file = os.getcwd() + "/rosalind_" + filename
        try:
            mode = __main__.readfile_mode
        except:
            mode = "auto"
        match mode:
            case "auto" : inp = rf(input_file) # TODO automatize matching mode
            case "line" : inp = rfl(input_file) # TODO automatize matching mode
            case "lines": inp = rfl(input_file) # TODO automatize matching mode
            case "2d"   : inp = rf2d(input_file) # TODO automatize matching mode
        #print(f"[INFO] Input file read successfully (\"{mode}\" mode).")
    except:
        print(f"[ERR] Cannot find input file \"{filename}\".")
