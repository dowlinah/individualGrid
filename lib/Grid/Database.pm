package Grid::Database;

use strict;
use warnings;
use DBI;

# Package variables
my $dbh;
my $username = "stephen";
my $password = "lorenz";

#** @function public connect_database()
# @brief Open a connection to the MySQl database.
#
# Under construction. Connect to the MySQL database as root.
#*.
sub connect_database {
  my $dsn = "DBI:mysql:grid";
  my $username = "root";
  my $password = '';

  my %attr = (PrintError=>0, RaiseError=>1);
  my $dbh  = DBI->connect($dsn, $username, $password, \%attr);
}

#** @function public connect_database()
# @brief Closes a connection to the MySQl database.
#
# Under construction. Disconnect from the MySQL database.
#*.
sub disconnect_databse {
  $dbh->disconnect();
}

sub get_username {
  return $username;
}

sub get_password {
  return $password;
}


1;
