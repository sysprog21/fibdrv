# fibdrv

Linux kernel module that creates device /dev/fibonacci.  Writing to this device
should have no effect, however reading at offset k should return the kth
fibonacci number.

## References
* [The Linux Kernel Module Programming Guide](https://sysprog21.github.io/lkmpg/)
* [Writing a simple device driver](https://www.apriorit.com/dev-blog/195-simple-driver-for-linux-os)
* [Character device drivers](https://linux-kernel-labs.github.io/refs/heads/master/labs/device_drivers.html)
* [cdev interface](https://lwn.net/Articles/195805/)
* [Character device files](https://sysplay.in/blog/linux-device-drivers/2013/06/character-device-files-creation-operations/)

## License

`fibdrv`is released under the MIT license. Use of this source code is governed by
a MIT-style license that can be found in the LICENSE file.

External source code:
* [git-good-commit](https://github.com/tommarshall/git-good-commit): MIT License
