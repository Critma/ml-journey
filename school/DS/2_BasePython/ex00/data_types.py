def data_types():
    a : int = 1
    b : str = "1"
    c : float = 1.0
    d : bool = True
    e : list = [1]
    f : dict = {1:1}
    g : tuple = (1,)
    m : set = {1}
    l = [type(i).__name__ for i in [ a, b, c, d, e, f, g, m ]]
    print("["+", ".join(l)+"]" )

if __name__ == "__main__":
    data_types()