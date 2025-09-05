import ipaddress

def subnet_calculator(ip_with_prefix):
    try:
        # Create an IPv4 network object
        network = ipaddress.ip_network(ip_with_prefix, strict=False)

        print("\n🔎 Subnetting Details:")
        print(f"IP Address: {network.network_address}")
        print(f"Subnet Mask: {network.netmask}")
        print(f"Network Address: {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Total Hosts: {network.num_addresses}")
        
        if network.prefixlen < 31:
            first_host = list(network.hosts())[0]
            last_host = list(network.hosts())[-1]
            print(f"First Usable Host: {first_host}")
            print(f"Last Usable Host: {last_host}")
        else:
            print("This subnet has no usable hosts (point-to-point link).")

    except ValueError as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    print("📌 Subnetting Calculator (Python)")
    ip_input = input("Enter IP with CIDR (e.g., 192.168.1.10/24): ")
    subnet_calculator(ip_input)
