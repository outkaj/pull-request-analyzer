
This program lists all pull requests for repositores in an existing GitHub organization. 

It assumes you have set up a [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/), as described further in the [GitHub Developer API v3 docs](https://developer.github.com/v3/auth/). Setting up this token will increase the rate limit when accessing the GitHub API. It also assumes that, given the sensitivity of the token, you have set it up as an environment variable on your system called `GITHUB_TOKEN`. You can do so following the general guidelines for setting up environment variables on your system. 
