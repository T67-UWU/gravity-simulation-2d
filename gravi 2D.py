import math, pyxel, random

G = 6.6743e-11
G = 0.1
dt = 1

class rond:
    def __init__(self, poid, taille, tkt=0, v=0):
        self.poid = poid
        self.taille = taille
        self.x = 40 + tkt
        self.y = 40 + tkt
        self.z = random.randint(0,250)
        self.vx= 0 +v
        self.vy= 0 
        self.vz = 0
        # Accumulateurs pour les accélérations
        self.ax_total = 0
        self.ay_total = 0
        self.az_total = 0

    def calculer_distance(self, vecteur):
        return math.sqrt(vecteur[0]**2 + vecteur[1]**2 + vecteur[2]**2)

    def calculer_vecteur(self, other):
        return (other.x - self.x, other.y - self.y, other.z - self.z)
    
    def calculer_force_gra(self, m1, m2, r):
        return G*(m1*m2)/(r*r) if r != 0 else 0
    
    def attraction(self, other):
        vecteur = self.calculer_vecteur(other)
        r = self.calculer_distance(vecteur)
        if r == 0:
            return
        F = self.calculer_force_gra(self.poid, other.poid, r)
        # Ajouter aux accélérations temporaires
        self.ax_total += (vecteur[0]/r) * (F/self.poid)
        self.ay_total += (vecteur[1]/r) * (F/self.poid)
        self.az_total += (vecteur[2]/r) * (F/self.poid)

    def appliquer_acceleration(self):
        self.vx += self.ax_total
        self.vy += self.ay_total
        self.vz += self.az_total
    
        self.ax_total = 0
        self.ay_total = 0
        self.az_total = 0

    def deplacement(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
        
class jeu:
    def __init__(self):
        pyxel.init(500, 500, title="gravite", fps=60)
        self.planete1 = rond(5000, 50, v=3)
        self.planete3 = rond(10, 50, tkt=150)
        self.planete2 = rond(5000, 290, 250)
        self.i = 0
        self.l = [self.planete1, self.planete2, self.planete3]
        pyxel.run(self.update, self.draw)
    def update(self):
        
        for i, p in enumerate(self.l):
            for j, other in enumerate(self.l):
                if i != j:
                    p.attraction(other)
        
        
        for p in self.l:
            p.appliquer_acceleration()
            p.deplacement()

    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.planete1.x, self.planete1.y, 5, 7)
        pyxel.circ(self.planete2.x, self.planete2.y, 5, 12)
        pyxel.circ(self.planete3.x, self.planete3.y, 5, 7)


jeu()
