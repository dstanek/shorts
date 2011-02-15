<!DOCTYPE html>
<html>
<head>
    <title>David Stanek's Link Shortener</title>
    <style type="text/css">
        span.created { font-size: .85em; }
    </style>
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.5.0/jquery.min.js"></script>
    <script type="text/javascript">
        $(function() {
            var fragment = location.hash;
            if (fragment) {
                var newurl = fragment.replace('#created:', '');
                $('body').prepend("<span>You've just created: " + newurl + "</span>");
            }
        });
    </script>
</head>
<body>

    <h1>David Stanek's Link Shortener</h1>
    <ul>
        <li><a href="#most_recent">Most Recent Links</a></li>
        <li><a href="#create_new">Create A New Link</a></li>
        <li><a href="#more_info">More Information</a></li>
    </ul>

    <h2 id="most_recent">Most Recent Links</h2>
    <ul>
    % for link in links:
        <li>
            <a class="short_link" href="${link.shortened_url(base_url)}">${link.shortened_url(base_url)}</a>
            <span class="target_url">-&gt; ${link.url}</span>
            <span class="created">{created ${link.created}}</span>
        </li>
    % endfor
    </ul>

    <h2 id="create_new">Create A New Link</h2>
    <p>This only works if you are me :-) That is on purpose. I didn't make this
    to be a general purpose URL shortener.</p>
    <form method="POST" action="/create">
        <label for="url">URL:</label>
        <input type="url" name="url" id="url">
        <input type="submit" id="submit">
    </form>

    <h2 id="more_info">More Information</h2>
    <ul>
        <li>The source code is available <a href="">here</a>.</li>
        <li>Blog post about what this is can be found <a href="">here</a>.</li>
    </ul>

</body>
</html>
