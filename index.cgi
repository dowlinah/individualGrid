#!/usr/bin/perl

use strict;
use warnings;
use FindBin;
use lib "$FindBin::Bin/lib/", "$FindBin::Bin/local/lib/perl5";
use Grid::HTML5;

Grid::HTML5::begin_html("Grid");
Grid::HTML5::generate_header();
print "<h2>Home</h2>";
print <<EOT;
Welcome to Grid! <br><br>
Grid is a simple Forum application.<br>
EOT
Grid::HTML5::generate_footer();
Grid::HTML5::end_html();
