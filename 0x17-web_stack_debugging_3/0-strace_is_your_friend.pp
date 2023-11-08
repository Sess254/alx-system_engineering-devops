# Fix & automate it using strace
exec { 'fix phpp':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => ['/usr/bin', '/bin']
}
