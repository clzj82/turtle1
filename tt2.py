import math,sys
import turtle as tt

def ffw(lns,fs=20,ls=24):
    tw = tt.clone()
    tw.ht()
    tw.pu()
    tw.speed(0)
    def f1(i,pc='white'):
        tw.pencolor(pc)
        tw.goto(tt.Screen().window_width()//-2+fs,
                tt.Screen().window_height()//2-ls*(i+3))
        tw.write(lns[i],font=('Courier',fs))
    for i in range(len(lns)): f1(i,'yellow' if i<1 else 'white')
    return f1

def ffs(lns,wr):
    def f2(x,y):
        exec('tt.'+lns[tt.nln])
        wr(tt.nln,'white')
        tt.nln = (tt.nln+1)%len(lns)
        wr(tt.nln,'yellow')
    return f2

def main(fp):
    tt.bgcolor('black')
    tt.pencolor('white')
    tt.shape('turtle')
    tt.shapesize(2,2)
    tt.speed(2)
    tt.nln = 0

    plns = open(fp).readlines()
    wtr = ffw(plns)
    fs1 = ffs(plns,wtr)
    tt.Screen().onclick(fs1)
    tt.onclick(lambda x,y:[fs1(0,0) for i in range(len(plns)-tt.nln-1)])
    tt.done()
if __name__=='__main__': main(sys.argv[1])
