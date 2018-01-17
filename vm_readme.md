# vm
A minimal VirtualBox wrapper

# Setup
* Have a VM with an ssh server running.
* It must be configured with a port forward rule for some port on host to the
  ssh port on guest.
* The very first usbfilter rule must be the one you want to toggle. Typically
  this is generic and matches all USB ports, essentially letting you switch all
  ports between host and guest.

## Update script's configuration variables...
* user    - The user to SSH as
* target  - Name of VM in VirtualBox
* port    - The host port which forwards to guest SSH port

# Usage
```
vm {cmd}
    start - Start the VM
    stop - Stop the VM
    save - Save state and close the VM
    port - Print port which forwards to guest
    list - List all VMs
    stat - List all running VMs
    usb {on|off} - Turn first usbfilter rule on or off.
    ssh - SSH into the VM
```
