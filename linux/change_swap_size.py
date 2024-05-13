import subprocess
import argparse

def create_swap_file(size, permanent):
    # Super-user mode
    subprocess.run(['sudo', 'su'])


    # Create a swap file
    subprocess.run(['fallocate', '-l', size, '/swapfile'])
    subprocess.run(['chmod', '600', '/swapfile'])
    subprocess.run(['mkswap', '/swapfile'])
    subprocess.run(['swapon', '/swapfile'])

    if permanent:
        # Make the swap file permanent
        subprocess.run(['cp', '/etc/fstab', '/etc/fstab.bak'])
        subprocess.run(['echo', '/swapfile none swap sw 0 0', '|', 'sudo', 'tee', '-a', '/etc/fstab'])

def show_swap_info():
    # Show swap information
    subprocess.run(['swapon', '--show'])
    subprocess.run(['free', '-h'])

def set_swappiness(value):
    # Set swappiness value
    subprocess.run(['sysctl', 'vm.swappiness=' + value])
    # Make the setting persistent
    subprocess.run(['sh', '-c', 'echo "vm.swappiness=' + value + '" >> /etc/sysctl.conf'])

def set_cache_pressure(value):
    # Set cache pressure value
    subprocess.run(['sysctl', 'vm.vfs_cache_pressure=' + value])
    # Make the setting persistent
    subprocess.run(['sh', '-c', 'echo "vm.vfs_cache_pressure=' + value + '" >> /etc/sysctl.conf'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Manage swap file and system settings')
    parser.add_argument('size', help='Size of the swap file')
    parser.add_argument('--permanent', action='store_true', help='Make the swap file permanent')
    parser.add_argument('--swappiness', help='Set the swappiness value')
    parser.add_argument('--cache-pressure', help='Set the cache pressure value')
    args = parser.parse_args()

    create_swap_file(args.size, args.permanent)
    show_swap_info()

    if args.swappiness:
        set_swappiness(args.swappiness)

    if args.cache_pressure:
        set_cache_pressure(args.cache_pressure)
