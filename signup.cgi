#!/usr/bin/perl

use strict;
use warnings;
use FindBin;
use lib "$FindBin::Bin/lib/", "FindBin::Bin/local/lib/perl5";
use Grid::HTML5;
use CGI;

my $query = CGI->new;

Grid::HTML5::begin_html("Grid");
Grid::HTML5::generate_header();
print "<h2>Sign up</h2>";
print <<EOT;
  <form method="POST" action="newuser.cgi">
	Desired User Name: <input type="text" name="username" required><br>
	Password: . . . . . . . . <input type="password" name="password" required><br>
	Re-Enter Password: <input type="password" name="password2" required><br>
    <input type="submit" formaction="newuser.cgi">
  </form>
EOT
Grid::HTML5::generate_footer();
Grid::HTML5::end_html();
