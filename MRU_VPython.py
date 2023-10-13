from vpython import *

# Criação de objetos 3D
objeto = sphere(pos=vector(-80, 1, 0), radius=1, color=color.red)
solo = box(pos=vector(0, 0, 0), size=vector(200, 0.5, 2), color=color.blue)

# Criação de gráficos
graph = gcurve(color = color.cyan)

# Variáveis iniciais
t = 0
dt = 0.01 # Incremento de variação tempora de 1 centésimo de segundo
objeto.vel = vector(2, 0, 0)

# Animação do movimento e equação
while True:
    rate(300)
    t = t + dt
    objeto.pos = objeto.pos + objeto.vel*dt # equação do MRU com incremento de variação temporal
    graph.plot(objeto.pos.x, t)