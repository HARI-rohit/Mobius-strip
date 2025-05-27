import numpy as np
import matplotlib.pyplot as plt

class MobiusStrip:
    def __init__(self, R, w, n):
        self.R = R  # radius from center
        self.w = w  # width of the strip
        self.n = n  # resolution

        self.u = np.linspace(0, 2 * np.pi, n)
        self.v = np.linspace(-w / 2, w / 2, n)
        self.U, self.V = np.meshgrid(self.u, self.v)

        self.X, self.Y, self.Z = self.compute_mesh()

    def compute_mesh(self):
      #function for creating the mesh
        U, V = self.U, self.V
        X = (self.R + V * np.cos(U / 2)) * np.cos(U)
        Y = (self.R + V * np.cos(U / 2)) * np.sin(U)
        Z = V * np.sin(U / 2)
        return X, Y, Z

    def compute_surface_area(self):
      #/ function for SA
        du = (2 * np.pi) / self.n
        dv = self.w / self.n

        dA = np.sqrt(
            (np.gradient(self.X, axis=0) * np.gradient(self.Y, axis=1) - 
             np.gradient(self.X, axis=1) * np.gradient(self.Y, axis=0)) ** 2 +
            (np.gradient(self.Y, axis=0) * np.gradient(self.Z, axis=1) - 
             np.gradient(self.Y, axis=1) * np.gradient(self.Z, axis=0)) ** 2 +
            (np.gradient(self.Z, axis=0) * np.gradient(self.X, axis=1) - 
             np.gradient(self.Z, axis=1) * np.gradient(self.X, axis=0)) ** 2
        )
        area = np.sum(dA) * du * dv
        return area

    def compute_edge_length(self):
      #function to return the length
        edge_u = self.u
        edge_v_top_x = (self.R + (self.w / 2) * np.cos(edge_u / 2)) * np.cos(edge_u)
        edge_v_top_y = (self.R + (self.w / 2) * np.cos(edge_u / 2)) * np.sin(edge_u)
        edge_v_top_z = (self.w / 2) * np.sin(edge_u / 2)

        dx = np.diff(edge_v_top_x)
        dy = np.diff(edge_v_top_y)
        dz = np.diff(edge_v_top_z)
        length = np.sum(np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)) * 2 
        return length

    def plot(self):
      #function to plot the mobius graph
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, color='cyan', edgecolor='gray', alpha=0.7)
        ax.set_title("Mobius Strip")
        plt.show()



if __name__ == "__main__":
    R = 5  # radius
    w = 2  # width
    n = 200  # resolution

    mobius = MobiusStrip(R, w, n)
    area = mobius.compute_surface_area()
    edge_length = mobius.compute_edge_length()

    print(f"Surface Area ≈ {area:.3f}")
    print(f"Edge Length ≈ {edge_length:.3f}")

    mobius.plot()
