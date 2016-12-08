#!/usr/bin/perl
use FindBin;
use lib "$FindBin::Bin/lib/", "FindBin::Bin/local/lib/perl5";
use Grid::HTML5;
use CGI;

###########PERL#################

$path="./data/img/";

my $numfiles = 0;
opendir(my $dh, $path);
while (my $de = readdir($dh)) {
	next if $de =~ /^\./ or $de =~ /config_file/;
	$numfiles++;
}
closedir($dh);


######### HTML #################

### needs a text field for the post's text.
	
Grid::HTML5::begin_html("Grid");
Grid::HTML5::generate_header();
print "<h2>Post</h2>";
print <<EOT;
<form enctype="multipart/form-data" action="upload.cgi" method="post">

<b> $numfiles posts so far.</b> <br>

File to be uploaded: <input name="upload_file" type="file" required> <br><br>
Title for post: <input type="text" name="upload_title" required> <br><br>
Write post here: <input type="textarea" name="upload_text" style='width:400px;' required> <br><br>

Username: <input type="text" name="user" required> <br>
Password: <input type="password" name="pass" required> <br>
<input type="submit" value="Make Post!!">


EOT
Grid::HTML5::generate_footer();
Grid::HTML5::end_html();



########### END MAIN ####################################

