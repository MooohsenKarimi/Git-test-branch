import numpy as np
import matplotlib.pyplot as plt
class McCulloch_Pitts_neuron():
    def __init__(self , weights , threshold):
        self.weights = weights       # وزن‌های ورودی
        self.threshold = threshold   # آستانه فعال‌سازی نورون

    def model(self , x):
        if self.weights @ x >= self.threshold:
            return 1
        else:
            return 0
def Area(x, y):
    # مرز پایین چپ: y >= 2x - 2 → -2x + y >= -2
    neur1 = McCulloch_Pitts_neuron([-2, 1], -2)

    # مرز پایین راست: y >= -2x + 18 → 2x + y >= 18
    neur2 = McCulloch_Pitts_neuron([2, 1], 18)

    # مرز بالا: y <= 6 → -1*y >= -6
    neur3 = McCulloch_Pitts_neuron([0, -1], -6)

    # مرز پایین: y >= 2 → 1*y >= 2
    neur4 = McCulloch_Pitts_neuron([0, 1], 2)

    # نورون نهایی: اگر هر ۴ شرط برقرار بود، داخل ذوزنقه است
    neur5 = McCulloch_Pitts_neuron([1, 1, 1, 1], 4)

    z1 = neur1.model(np.array([x, y]))
    z2 = neur2.model(np.array([x, y]))
    z3 = neur3.model(np.array([x, y]))
    z4 = neur4.model(np.array([x, y]))
    z5 = neur5.model(np.array([z1, z2, z3, z4]))

    return [z5]
num_points = 1000
x_values = np.random.uniform(0, 10, num_points)
y_values = np.random.uniform(0, 10, num_points)
if Area(x_values[i], y_values[i]) == 1:
    green_points.append((x_values[i], y_values[i]))
else:
    red_points.append((x_values[i], y_values[i]))
green_points = []  # نقاط داخل ذوزنقه
red_points = []    # نقاط خارج

for i in range(num_points):
    output = Area(x_values[i], y_values[i])
    if output == [1]:
        green_points.append((x_values[i], y_values[i]))
    else:
        red_points.append((x_values[i], y_values[i]))
# آماده‌سازی نقاط برای رسم
if green_points:
    green_x, green_y = zip(*green_points)
if red_points:
    red_x, red_y = zip(*red_points)

plt.figure(figsize=(8, 6))
if red_points:
    plt.scatter(red_x, red_y, color='red', label='Outside Trapezoid')
if green_points:
    plt.scatter(green_x, green_y, color='green', label='Inside Trapezoid')

# رسم مرز ذوزنقه
trapezoid_x = [2, 4, 6, 8, 2]
trapezoid_y = [2, 6, 6, 2, 2]
plt.plot(trapezoid_x, trapezoid_y, 'b--', label='Trapezoid Border')

plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("McCulloch-Pitts Neuron for Trapezoid Area")
plt.legend()
plt.grid(True)
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.show()
