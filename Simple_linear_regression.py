#Applying cost function
def cost_function(x,y,w,b):
    sq_error=0
    m=len(x)
    for i in range(m):
        f=w*x[i]+b
        sq_error+=(f-y[i])**2
    cost=(1/(2*m))*sq_error
    return cost
#Derviative of cost function
def gradient(x,y,w,b):
    m=len(x)
    dc_dw=0
    dc_db=0

    for i in range(m):
        f=w*x[i]+b
        dc_dw+=(f-y[i])*x[i]
        dc_db+=(f-y[i])

    dc_dw=1/m*(dc_dw)
    dc_db=1/m*(dc_db)

    return dc_dw,dc_db

#Applying the gradient descent using the derivative
def gradient_descent(x,y,l,iterations):
    w=0
    b=0

    for i in range(iterations):
        dc_dw,dc_db=gradient(x,y,w,b)
        w=w-l*dc_dw
        b=b-l*dc_db

    return w,b

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]  # True relationship: y = 2x

# Initial cost before training
initial_cost = cost_function(x, y, w=0, b=0)
print(f"Initial cost: {initial_cost:.4f}")

# Train the model
w, b = gradient_descent(x, y, l=0.01, iterations=1000)

# Final cost after training
final_cost = cost_function(x, y, w, b)
print(f"Final cost: {final_cost:.4f}")
print(f"Trained weights: w = {w:.4f}, b = {b:.4f}")
