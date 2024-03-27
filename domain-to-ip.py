import socket

def domain_to_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        print(f"Hata: {domain} domaini çözümlenemiyor: {e}")
        return None

def main():
    while True:
        domains = input("Çözümlenmesini istediğiniz domainleri virgülle ayırarak girin (örneğin: example.com,google.com): ").strip().split(',')
        ip_addresses = []
        for domain in domains:
            ip_address = domain_to_ip(domain.strip())
            if ip_address:
                ip_addresses.append((domain, ip_address))
        if ip_addresses:
            print("Çözümlenen IP adresleri:")
            for domain, ip_address in ip_addresses:
                print(f"{domain}: {ip_address}")
        else:
            print("Hiçbir domain çözümlenemedi.")

        devam_et = input("Başka bir domain çözümlensin mi? (E/H): ")
        if devam_et.lower() != 'e':
            break

if __name__ == "__main__":
    main()
