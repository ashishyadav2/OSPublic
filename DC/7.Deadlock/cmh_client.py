import socket

def main():
    try:
        init = int(input("Enter Initiator Site No.: "))
        end = 5 # Assuming there are 5 sites
        a = [
        [0, 1, 0, 0, 0], # Dependency matrix, you need to fill this based on your setup
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0]
        ]
        print("____________________")
        print("\n CHANDY-MISRA-HASS DISTRIBUTED DEADLOCK DETECTION ALGORITHM")
        print("\tS1\tS2\tS3\tS4\tS5")
        for i in range(end):
            print("S" + str(i + 1) + "\t" + "\t".join(map(str, a[i])))
        print("\nEnter Initiator Site No. : ", init)
        print("\n DIRECTION\tPROBE")
        print()
        flag = False
        for k in range(end):
            if a[init - 1][k] == 1:
                print(f" S{init} --> S{k + 1} ({init},{init},{k + 1})")
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(('192.168.1.185', 12345))
                    s.sendall(f"{init},{init},{k + 1}".encode())
                flag = True
            if flag:
                print("\n DEADLOCK DETECTED")
        print("____________________")
    except Exception as e:
        pass
if __name__ == "__main__":
    main()