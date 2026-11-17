# Releasing

GitHub Releases distribute the plugin ZIP. They do not publish to the public
ChatGPT plugin directory or install/update a user's plugin.

## Prepare

1. Finish the scoped change, preserve notices and inspect the source mapping.
2. For a package change, bump `content/plugin.json`, update `content/README.md`,
   README examples, CHANGELOG.md and a versioned validation report. Never replace
   an already published package with different bytes under the same version.
3. Add `docs/releases/v<version>.md` with concrete behavior, verification and limits.
4. Run the suite, build, inspect the ZIP, and confirm a clean source rebuild.
   Review relevant instruction/discovery behavior separately from static checks.
5. Merge the reviewed change to `main`, then push an annotated matching tag:

   ```sh
   git tag -a v0.2.1 -m "Unified Engineering v0.2.1"
   git push origin v0.2.1
   ```

Replace the example version for later releases. Do not tag uncommitted work or
use a version that differs from the manifest.

## Automated release

The tag workflow checks version equality, runs the suite, builds and inspects the
plugin, and creates a complete Git source archive plus SHA256SUMS.txt. It then
publishes a GitHub **prerelease** with those three assets. A clean runner does not
need any package installation. Actions are pinned to commit SHAs; CI has read
permissions and only the release job receives `contents: write`.

The workflow fails on an existing release rather than overwriting it. Inspect
errors before rerunning; do not delete/recreate an existing tag or clobber assets
to hide a changed payload. A later stable-release policy can be chosen after
target-runtime acceptance; the current workflow intentionally marks test releases.

## Verify

Check the hosted workflow result, release assets, version and checksums. Download
the source ZIP into a clean directory and reproduce the plugin. Record any actual
cloud listing/reference checks and client behavior against the tested version.
Do not infer successful installation from a GitHub upload.

For the initial repository launch, the 0.2.1 plugin payload is unchanged from the
previously delivered ZIP. The repository adds documentation and CI around it.
Existing earlier local archives remain for rollback.
