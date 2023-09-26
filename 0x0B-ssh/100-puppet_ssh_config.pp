# Ensure SSh client configuration
file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  ensure => present,
}

file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  ensure => present,
}

# Reload SSH service if configuration changes
service { 'ssh':
  ensure  => running,
  enable  => true,
  require => File_line['Turn off passwd auth', 'Declare identity file'],
}
