from scipy import optimize

class Geometry_Optimizer:
    def __init__(self, p_manager, coord):
        self.pot_func = p_manager
        self.coord = coord
    
    def minimize(self):
        coord_shape = self.coord.shape
        pot_1 = self.pot_func.getpot(self.coord)
        print(f"Base Energy: {pot_1}")
        result = optimize.minimize(self.pot_func.getpot, self.coord, method='CG')
        while result.fun < pot_1:
            print(f"New Energy: {result.fun}")
            pot_1 = result.fun
            x = result.x.reshape(coord_shape)
            result = optimize.minimize(self.pot_func.getpot, x, method='Nelder-Mead')
            x = result.x.reshape(coord_shape)
            pot_1 = result.fun
            result = optimize.minimize(self.pot_func.getpot, x, method='CG')
        final = result.x.reshape(coord_shape)
        print(f"Final Energy: {result.fun}")

        return final