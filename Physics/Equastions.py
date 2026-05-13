ap_physics_rotational_essentials = [

# Linear Kinematics
"Kinematic equation: v = v0 + a*t",
"Kinematic equation: x = x0 + v0*t + (1/2)a*t^2",
"Kinematic equation: v^2 = v0^2 + 2a(x - x0)",
"Kinematic equation: x - x0 = ((v + v0)/2)t",

# Rotational Dynamics
"Torque: tau = r*F*sin(theta)",
"Rotational Newtons 2nd Law: sum(tau) = I*alpha",

"Tangential speed: v = r*w",
"Rolling without slipping: v = r*w",

"Rotational kinetic energy: K_rot = (1/2)I*w^2",
"Rolling energy conservation: mgh = (1/2)m*v^2 + (1/2)I*w^2",

"Static equilibrium (forces): sum(F) = 0",
"Static equilibrium (torques): sum(tau) = 0",

"Angular momentum: L = I*w",
"Angular impulse: delta(L) = tau*delta(t)",
"Conservation of angular momentum: Ii*omegai = If*omegaf",

]

for equastion in ap_physics_rotational_essentials:
    print(equastion)
    input("")