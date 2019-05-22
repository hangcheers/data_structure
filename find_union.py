class QuickFind:
    def __init__(self, n):
        self.groups = n
        self.id_pts = [x for x in range(n)]

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        return self.id_pts[p]

    def union(self, p, q):
        src = self.find(p)
        tgt = self.find(q)
        if not self.is_connected(p, q):
            for i in range(len(self.id_pts)):
                if self.id_pts[i] == src:
                    self.id_pts[i] = tgt
            self.groups -= 1


class QuickUnion:
    def __init__(self, n):
        self.groups = n
        self.id_pts = [x for x in range(n)]  # id[i] ----- parent of i

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        while (p != self.id_pts[p]):
            p = self.id_pts[p]
        return p

    def union(self, p, q):
        parent = self.find(p)
        child = self.find(q)
        if parent == child: return
        self.groups -= 1
        self.id_pts[child] = parent


class WeightedQuickUnion:
    def __init__(self, n):
        self.groups = n
        self.points = [x for x in range(n)]
        self.weights = [1 for x in range(n)]  # 记录树的节点上有多少个元素

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        if p == self.points[p]:
            return p
        else:
            return self.find(self.points[p])

    def union(self, p, q):
        parent = self.find(p)
        child = self.find(q)
        if parent == child: return
        self.groups -= 1
        # 保证小的树在大的树的子节点上
        if self.weights[child] <= self.weights[parent]:
            self.points[child] = parent
            self.weights[parent] += self.weights[child]
        else:
            self.points[parent] = child
            self.weights[child] += self.weights[parent]


qf = WeightedQuickUnion(10)
print("\ninitial goup:{0}; id_points:{1}".format(qf.groups, qf.points))
list = [
    (4, 3),
    (3, 8),
    (6, 5),
    (9, 4),
    (2, 1),
    (5, 0),
    (7, 2),
    (6, 1),
    (7, 3),
]

for k in list:
    p = k[0]
    q = k[1]
    qf.union(p, q)
    print("%d and %d is connected? %s" % (p, q, str(qf.is_connected(p, q))))

print("\nfinal root list is %s" % (",").join(str(x) for x in qf.points))
# print("\ngoup:{0}; id_points:{1}".format(qf.groups,qf.id_pts))
print("\ncount of components is %d" % qf.groups)
