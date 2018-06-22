# kodo-dev

Internal repository for testing the Kodo top level projects:

* [kodo-rlnc](https://github.com/steinwurf/kodo-rlnc)
* [kodo-fulcrum](https://github.com/steinwurf/kodo-fulcrum)
* [kodo-reed-solomon](https://github.com/steinwurf/kodo-reed-solomon)
* [kodo-slide](https://github.com/steinwurf/kodo-slide)
* [kodo-perpetual](https://github.com/steinwurf/kodo-perpetual)

Note: `kodo-core` is considered purely a dependency and not a top-level
repository. It provides building blocks for instantiating erasure correcting
codes but no stand-alone functionality.

The basic idea is to allow a developer (you) to work on the Kodo projects
as if they were located in the same repository.

As a simple example. A bug is reported against `kodo-core` you can set the
branch for `kodo-core` here and rebuild all kodo repositories with that version.

## Quick start

To quickly get going and build all of Kodo you can run:

```
./waf configure --resolve_path ~/dev/bundle_dependencies --fast_resolve
./waf build --run_tests
```

## Goals

1. Ensure that dependencies of all Kodo repositories are in sync. I.e. they use
   the same version of `kodo-core` but also other dependent libraries. This
   goal is easily achieved since our resolve framework will already ensure that.

2. Make it possible to test changes in a dependency without having to open
   branches in each Kodo top level repository.


## Work flow

In the master branch of `kodo-dev` we have the Kodo top-level repositories in
[resolve.json](https://github.com/steinwurf/kodo-dev/blob/master/resolve.json)

The basic idea is that we use the following approach:

1. Locally lock the paths to the repositories you are working on. This can be
   done with the following approach:

   1. Add *user paths* to configure, e.g. `--kodo-core-path=/my/path`. Add as
   many as needed.
   2. Add `--lock_paths` to configure.

   Example:
   ```
   ./waf configure --boost_path ../new-boost --lock_paths
   ```
2. To ensure that your changes are available on the buildbot add/modify the
   dependencies you are working on in `resolve.json`. Use the `override=True`
   property to make sure that your version of the dependency is used.


## Example: Force all projects to use the `master` branch of `kodo-core`

To do this you can add the following to `resolve.json`:

```
    {
        "name": "kodo-core",
        "resolver": "git",
        "method": "checkout",
        "checkout": "master",
        "override": true,
        "sources": [
            "github.com/steinwurf/kodo-core.git"
        ]
    },
```

You can replace `"master"` with a different branch name you want to test with.