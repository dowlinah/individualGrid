#!/usr/bin/perl 
require ("mylib.pl");

use FindBin;
use lib "$FindBin::Bin/lib/", "$FindBin::Bin/local/lib/perl5";
use Grid::HTML5;
use CGI;
use CGI::Carp qw ( fatalsToBrowser );
$CGI::POST_MAX = 1024 * 4000;    # 4MB

my $path = "./data/usr/";

my $query = new CGI;
my $username = $query->param("username");
my $pass1 = $query->param("password");
my $pass2 = $query->param("password2");

$message = "User Created Successfully!";

chomp($pass1);
chomp($pass2);
chomp($username);

$finalpass = ".";

if($pass1 ne $pass2) {
	$message = "Passwords don't match.";
} else {
	$finalpass = crypt($pass1, 69);
	
	$path = $path . $username . ".usr";

	if (-f $path) {
		$message = "User already exists.";
	} else {
		open( FH, ">$path");
		print FH $finalpass;
		close FH;
	}
}

################# HTML ##################

Grid::HTML5::begin_html();
Grid::HTML5::generate_header();
print<<EOT;
<br>
<b> Desired username:</b> $username <br><br>
<b> $message </b>
<br>
EOT

Grid::HTML5::generate_footer();
Grid::HTML5::end_html();
exit;

