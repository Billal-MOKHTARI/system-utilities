# system-utilities

This repository provides some important system commands.

## Example Usage

1. To manage swap file and system settings using the `swap_manager.py` script, you can run the following command:

```bash
python swap_manager.py 2G --permanent --swappiness 10 --cache-pressure 50
```

## Enable the swap partition
```bash
sudo swapon /dev/nvme0n1p3
```
To make the swap permanent, copy the following line `/dev/nvme0n1p3` to `/etc/fstab`

## References
- For more information on adding swap space on Ubuntu 20.04, you can refer to the following **DigitalOcean tutorial**: [How To Add Swap Space on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-add-swap-space-on-ubuntu-20-04)

