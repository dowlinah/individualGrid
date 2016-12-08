#!/usr/bin/perl

use FindBin;
use lib "$FindBin::Bin/lib/", "$FindBin::Bin/local/lib/perl5";
use Grid::HTML5;
use CGI;

my $query = CGI->new;
my $post = $query->url_param('post');

$path = "./data/comments/" . $post . "*.cmnt";
@commentsoldnew = glob($path);
@commentsnewold = reverse(@commentsoldnew);

Grid::HTML5::begin_html("Grid");
Grid::HTML5::generate_header();

$imgpath = "./data/img/" . $post . ".jpg";
$txtpath = "./data/text/" . $post . ".txt";

open(FH, $txtpath);
$posttext = <FH>;
close(FH);

print <<EOT;

<h2> Comments on Post $post </h2>

<div id='post'>
<div class = 'text'> $posttext <br><br> </div>
<br> <div class='image'> <a href='$imgpath'>
<img src='$imgpath' width='100';></a></div>
</div><br>

EOT

foreach(@commentsnewold) {
	open(FH, $_);
	$comment = <FH>;
	close(FH);

print <<EOT;
<div style='border:1px #000 solid; padding:10px'>
<div> $comment </div>
</div>
<br>
EOT

}

Grid::HTML5::generate_footer();
Grid::HTML5::end_html();
