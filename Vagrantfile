# -*- mode: ruby -*-
# vi: set ft=ruby :
#
BOX_BASE = "ubuntu/focal64"
RAM = "512"
CPUS = "2"
SERVER = "server"
CLIENT = "client"

Vagrant.configure("2") do |config|
  config.vm.box = BOX_BASE
  config.vm.define CLIENT do |client|
    client.vm.hostname = CLIENT
    client.vm.provider :virtualbox do |vb|
        vb.customize [ 'modifyvm', :id, '--memory', RAM ]
        vb.customize [ 'modifyvm', :id, '--cpus', CPUS ]
        vb.customize [ 'modifyvm', :id, '--name', CLIENT ]
    end
    client.vm.provision "shell", inline: <<-SHELL
        #!/usr/bin/env bash
        cp /vagrant/client.py /home/vagrant/client.py
    SHELL
    client.vm.network "private_network", ip: "192.168.56.100"
    #client.vm.network "forwarded_port", guest: 5000, host: 5000
  end
  config.vm.define SERVER do |server|
    server.vm.hostname = SERVER
    server.vm.provider :virtualbox do |vb|
        vb.customize [ 'modifyvm', :id, '--memory', RAM ]
        vb.customize [ 'modifyvm', :id, '--cpus', CPUS ]
        vb.customize [ 'modifyvm', :id, '--name', SERVER ]
    end
    server.vm.provision "shell", inline: <<-SHELL
        #!/usr/bin/env bash
        cp /vagrant/server.py /home/vagrant/server.py      
    SHELL
    server.vm.network "private_network", ip: "192.168.56.50"
  end
end


