import math,sys
import turtle as tt

def wr_fact(lns):
    wx,wy = -tt.getscreen().canvwidth,tt.getscreen().canvheight
    wt = tt.clone()
    wt.speed(0)
    wt.ht()
    wt.pu()
    def writef1(i,pc='white',fs=20,ls=25):
        wt.pencolor(pc)
        wt.goto(wx,wy-i*ls)
        wt.write(lns[i],font=('Courier',fs))
    return writef1

def step_fact(lns,wtr,stp=0):
    def stepf1(x,y):
        nonlocal stp
        exec('tt.'+lns[stp])
        wtr(stp,'white')
        stp = stp+1 if stp+1<len(lns) else 0
        wtr(stp,'yellow')
    return stepf1

def main(fp1):
    tt.bgcolor('black')
    tt.pencolor('white')
    tt.shape('turtle')
    tt.speed(2)

    plns = open(fp1).readlines()
    wtr = wr_fact(plns)
    for i,ln in enumerate(plns): wtr(i,'white')
    wtr(0,'yellow')
    fstp1 = step_fact(plns,wtr)
    tt.onclick(fstp1)
    tt.done()
if __name__=='__main__': main(sys.argv[1])
