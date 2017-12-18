# kodo-dev

Internal repository for testing the kodo top level projects:

* [kodo-rlnc](https://github.com/steinwurf/kodo-rlnc)
* [kodo-fulcrum](https://github.com/steinwurf/kodo-fulcrum)
* [kodo-reed-solomon](https://github.com/steinwurf/kodo-reed-solomon)

Note: `kodo-core` is considered purely a dependency and not a top-level
repository. It provides building blocks for instantiating erasure correcting
codes but no stand-alone functionality.

The basic idea is to allow a developer (you) to work on the kodo projects
as if they were located in the same repository.  

As a simple example. A bug is reported against `kodo-core` you can set the 
branch for `kodo-core` here and rebuild all kodo repositories with that version. 

## Goals

1. Ensure that dependencies of all kodo repositories are in sync. I.e. they use
   the same version of `kodo-core` but also other dependent libraries. This 
   goal is easilty achived since our resolve framework will already ensure that.

2. Make it possible to test changes in a depenedency without having to open 
   branches in each kodo top level repository.



## Work flow

In the master branch of `kodo-dev` we have the kodo top-level repositories in
[resolve.json](https://github.com/steinwurf/kodo-dev/blob/master/resolve.json)

The basic idea is that we use the following approach:,,


1. Locally lock the paths to the repositories you are working on. This can be
   done with the following approach:
   
   1. Add *user paths* to configure, e.g. `--kodo-core-path=/my/path`. Add as 
   many as needed.
   2. Add `--lock_paths` to configure.

   Example:
   ```
   ./waf configure --boost_path ../new-boost --lock_paths
   ```
2. To t


## Todo 

We seem to need the ability to override dependencies. I.e. by using
`override=True` in the `resolve.json` we can force a specific version of some
dependency to be used.

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