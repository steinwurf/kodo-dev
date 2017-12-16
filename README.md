# kodo-dev

Internal repository for testing the kodo familiy of repositories.

The basic idea is to allow a developer (you) to work on the kodo projects
as if they were located in the same repository. For example, if you make
a change in `kodo-core` you will rebuild all other kodo repositories and
run their unit tests. 

## Work flow

The basic idea is that we use the following approach 


## Todo 

We seem to need the ability to override dependencies. I.e. by using `override=True` in the
`resolve.json` we can force a specific version of some dependency to be used.

Add back

```
    {
        "name": "kodo-fulcrum",
        "resolver": "git",
        "method": "semver",
        "major": 7,
        "sources": [
            "github.com/steinwurf/kodo-fulcrum.git"
        ]
    },
```