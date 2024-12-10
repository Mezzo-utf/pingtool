
import time
from ping3 import ping
import pyfiglet # type: ignore

def ping_host(host):
    response_time = ping(host)
    if response_time is None:
        print("Host {} não está respondendo.".format(host))
    else:
        print("Tempo de resposta para {}: {} ms".format(host, round(response_time * 1000, 2)))

def print_banner():
    banner = pyfiglet.figlet_format("Pyngtool")
    print(banner)


def main():
    print_banner()
    host = input("Digite o endereço IP ou URL que deseja pingar: ")

    try:
        while True:
            ping_host(host)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nEncerrando a ferramenta de ping.")

if __name__ == "__main__":
    main()