#This manifest kills a process killmenow
exec { 'kill_killmenow':
  command =>  'pkill -9 killmenow',
  path    =>  ['/usr/bin/'],
  }
