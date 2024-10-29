class SymmetricHash:
    def __init__(self, rep_factor: int = 3) -> None:
        self.ring = [0]*125
        self.map = {}
        self.servers = []
        self.rep_factor = rep_factor

    def add(self, item: int) -> bool:
        hash_key = hash(item)
        if hash_key not in self.map.keys():
            self.map[hash_key] = []
        self.map[hash_key].appemd(item)
        return True
    
    def add_server(self, serverName) -> bool:
        if serverName in self.servers:
            return False
        self.servers.append(serverName)
        # create the ring on the 
        server_hash_nodes = []
        server_hash = hash(serverName) % 125
        server_hash_nodes.append(server_hash)
        for i in range(self.rep_factor):
            server_hash = abs(hash((serverName) + "0" + str(i))) % 125
            if server_hash in server_hash_nodes:
                mid = (server_hash_nodes[0] + server_hash_nodes[len(server_hash_nodes) - 1]) / 2
                server_hash_nodes.append(mid)
            else:
                server_hash_nodes.append(server_hash)
            server_hash_nodes.sort()
        print(server_hash_nodes)
        return True


def main():
    hashh = SymmetricHash(5)
    hashh.add_server("db_instance1")


if __name__ == "__main__":
    main()