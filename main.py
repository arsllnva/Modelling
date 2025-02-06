import numpy as np 
import matplotlib.pyplot as plt 
 
# Константы 
m = 2  # Масса тела, кг 
R = 4  # Радиус кольца, м 
alpha = np.pi / 2 + np.pi / 3  # Угловой размер дуги, рад 
mu = 0.02  # Коэффициент трения 
g = 9.81  # Ускорение свободного падения, м/с^2 
 
v_fin = 5.83  # Минимальная скорость для прохождения дуги 
 
# Моделирование траектории после отрыва 
def simulate_trajectory(v0, theta, R, g): 
    dt = 0.01  # Шаг по времени 
    x = R * np.sin(theta) 
    y = R * (1 - np.cos(theta))  # Начальные координаты 
    vx = v0 * np.cos(theta) 
    vy = v0 * np.sin(theta)  # Начальные скорости 
    trajectory_x = [x] 
    trajectory_y = [y] 
 
    while y >= 0:  # Пока тело находится выше земли 
        x += vx * dt 
        y += vy * dt - 0.5 * g * dt**2  # Учет ускорения свободного падения 
        vy -= g * dt  # Изменение вертикальной скорости 
        trajectory_x.append(x) 
        trajectory_y.append(y) 
 
    return trajectory_x, trajectory_y 
 
# Угол отрыва (в данном случае, конечный угол дуги) 
theta = alpha 
 
# Траектория после отрыва 
trajectory_x, trajectory_y = simulate_trajectory(v_fin, theta, R, g) 
 
# Параметрическое представление дуги 
theta_values = np.linspace(0, alpha, 100) 
arc_x = R * np.sin(theta_values) 
arc_y = R * (1 - np.cos(theta_values)) 
 
# График траектории 
plt.figure(figsize=(8, 6)) 
plt.plot(trajectory_x, trajectory_y, label='Траектория после отрыва') 
plt.plot(arc_x, arc_y, label='Дуга') 
plt.xlabel('X, м') 
plt.ylabel('Y, м') 
plt.title('Траектория тела после отрыва от дуги') 
plt.legend() 
plt.grid(True) 
plt.show()
