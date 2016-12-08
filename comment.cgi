#!/usr/bin/perl

use strict;
use warnings;
use FindBin;
use lib "$FindBin::Bin/lib/", "$FindBin::Bin/local/lib/perl5";
use Grid::HTML5;
use CGI;

my $query = CGI->new;
my $post = $query->url_param('post');



Grid::HTML5::begin_html("Grid");
Grid::HTML5::generate_header();
print "<h2>Comment</h2>";
print <<EOT;
<form enctype="multipart/form-data" action="addcomment.cgi?post=$post" method="post">
Comment: <input type="text" name="comment" required><br>
<br>
Username: <input type="text" name="user" required><br>
Password: .<input type="password" name="pass" required><br>
<br>
<input type="submit" value="Add Comment">
EOT
Grid::HTML5::generate_footer();
Grid::HTML5::end_html();
