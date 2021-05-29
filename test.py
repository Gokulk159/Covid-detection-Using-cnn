class Containor:
    def __init__(self,id,ln,br,hr,pr):
        self.id=id
        self.length=ln
        self.bredth=br
        self.height=hr
        self.priceper=pr
    def findVolume(self):
        Volume=self.length*self.bredth*self.height
        return Volume
class Packingc:
    def __init__(self,contar):
        self.ContainorList=contar
    def Containorcost(self,cid):
        for i in self.ContainorList:
            if (i.id==cid):
                k=i.findVolume()
                cost=k*i.priceper
                return cost
            return None
    def Large(self):
        out={}
        for i in self.ContainorList:
            k=i.findVolume()
            out[k]=i.id
        out=out.sort(out.item(),reverse =True)
        return out
if __name__ == '__main__':
    count=int(input())
    clist=[]
    for i in range(count):
        iid=int(input())
        length=int(input())
        bredth=int(input())
        height=int(input())
        priceper=int(input())
        c1=Containor(iid,length,bredth,height,priceper)
        clist.append(c1)
    p1=Packingc(clist)
    cid=int(input())
    cost=p1.Containorcost(cid)
    lcost=p1.Large()





