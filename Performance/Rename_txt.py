import os

def renamefile():
    # make a duplicate of an existing file
    try:
        os.rename(r'Performance/turtle.txt',
                  r'Performance/海龜.txt')
        os.rename(r'Performance/turtle_FF.txt',
                  r'/Performance/海龜+固定分數.txt')
        os.rename(r'Performance/turtle_FR.txt',
                  r'/Performance/海龜+固定比率.txt')
        os.rename(r'Performance/turtle_kelly.txt',
                  r'/Performance/海龜+凱利.txt')
        os.rename(r'Performance/turtle_optimalF.txt',
                  r'/Performance/海龜+最佳F值.txt')
        os.rename(r'Performance/turtle_william.txt',
                  r'/Performance/海龜+LarryWilliams.txt')
        # Do something with the file
    except IOError:
        print("File already renamed")




# if __name__ == "__main__":
#     renamefile()