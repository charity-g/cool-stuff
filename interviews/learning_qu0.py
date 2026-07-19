# Government Secure Package Registry
"""
The government maintains an internal software package registry.

Developers **cannot install packages directly from the public internet.**
Instead, all application inside the government installs packages only from this registry.

## Initial APIs 
- Assume these are REST APIs that succeed or fail
- Assume these are already implemented
- Assume authentication is handled for you within these APIs

upload_package_file_to_registry(package_name, version) -> Succes or Failure
remove_package_file_to_registry(package_name) -> Success or Failure

install_package_on_server(server: IP, ) -> Success or Failure
"""

"""
YOUR TASK 1:
"""
 
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List
from enum import Enum
 
 
# ---------------------------------------------------------------------------
# Stubs for the "already implemented" external REST APIs.
# Replace these with real HTTP calls in production; kept sync/boolean here
# to match the signatures given in the prompt.
# ---------------------------------------------------------------------------
 
def upload_package_file_to_registry(package_name: str, version: str) -> bool:
    return True
 
def remove_package_file_to_registry(package_name: str) -> bool:
    return True
 
def install_package_on_server(server_ip: str, package_name: str, version: str) -> bool:
    return True


# ---------------------------------------------------------------------------
# Result type — avoids throwing exceptions across a service boundary for
# expected failure modes (not found, already exists, etc). Callers can check
# `.success` and read `.message` instead of try/except on business logic.
# ---------------------------------------------------------------------------
 
@dataclass
class Result:
    success: bool
    message: str = ""
 
    def __bool__(self) -> bool:
        return self.success
 
    @staticmethod
    def ok(message: str = "") -> "Result":
        return Result(True, message)
 
    @staticmethod
    def fail(message: str) -> "Result":
        return Result(False, message)
 
 
@dataclass
class PackageVersion:
    name: str
    version: str
    files: List[str]
 

# ---------------------------------------------------------------------------
# The Registry: source of truth for what packages/versions exist.
# ---------------------------------------------------------------------------
 
class PackageRegistry:
    def __init__(self) -> None:
        # name -> version -> PackageVersion
        self._packages: Dict[str, Dict[str, PackageVersion]] = {}
 
    def publishPackage(self, name: str, version: str, files: List[str]) -> Result:
        if not name or not version:
            return Result.fail("name and version are required")
        if not files:
            return Result.fail("files cannot be empty")
 
        versions = self._packages.setdefault(name, {})
        if version in versions:
            return Result.fail(f"{name}=={version} already published (packages are immutable)")
 
        if not upload_package_file_to_registry(name, version):
            return Result.fail("upload to registry failed")
 
        versions[version] = PackageVersion(name, version, files)
        return Result.ok(f"published {name}=={version}")
 
    def removePackage(self, packageName: str) -> Result:
        if packageName not in self._packages:
            return Result.fail(f"{packageName} not found in registry")
 
        if not remove_package_file_to_registry(packageName):
            return Result.fail("remove from registry failed")
 
        del self._packages[packageName]
        return Result.ok(f"removed {packageName} (all versions)")
 
    def exists(self, name: str, version: str) -> bool:
        return name in self._packages and version in self._packages[name]
 
    def get_versions(self, name: str) -> List[str]:
        return list(self._packages.get(name, {}).keys())
 
 
# ---------------------------------------------------------------------------
# Server-side install tracking. Kept as a separate class from the registry
# because it has a different key space (server IP) and different lifecycle
# (install/uninstall vs publish/remove) — no reason to conflate them.
# ---------------------------------------------------------------------------
 
class ServerInstallManager:
    def __init__(self, registry: PackageRegistry) -> None:
        self._registry = registry
        # serverIp -> package name -> installed version
        self._installed: Dict[str, Dict[str, str]] = {}
 
    def installPackage(self, serverIp: str, packageName: str, version: str) -> Result:
        if not self._registry.exists(packageName, version):
            return Result.fail(f"{packageName}=={version} not found in registry")
 
        server_state = self._installed.setdefault(serverIp, {})
 
        if server_state.get(packageName) == version:
            return Result.ok(f"{packageName}=={version} already installed on {serverIp}")
 
        if not install_package_on_server(serverIp, packageName, version):
            return Result.fail(f"install failed on {serverIp}")
 
        # NOTE: this overwrites any prior version of the same package.
        # No policy yet for "can two versions of A coexist on one server" —
        # that's a Task 2 question once dependencies/versioning semantics
        # are introduced. Here: one version of a package per server.
        server_state[packageName] = version
        return Result.ok(f"installed {packageName}=={version} on {serverIp}")
 
    def getInstalledPackages(self, serverIp: str) -> Dict[str, str]:
        """Returns {package_name: version} currently installed on serverIp."""
        return dict(self._installed.get(serverIp, {}))
 
    def installFromRequirements(self, serverIp: str, requirements_text: str) -> List[Result]:
        """
        requirements_text: newline-separated "name==version" entries,
        mirroring a requirements.txt handed over by another team.
        """
        results: List[Result] = []
        for line in requirements_text.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "==" not in line:
                results.append(Result.fail(f"malformed requirement line: '{line}'"))
                continue
            name, version = line.split("==", 1)
            results.append(self.installPackage(serverIp, name.strip(), version.strip()))
        return results
 
 
# ---------------------------------------------------------------------------
# Demo / smoke test
# ---------------------------------------------------------------------------
 
if __name__ == "__main__":
    registry = PackageRegistry()
    servers = ServerInstallManager(registry)
 
    print(registry.publishPackage("numpy", "1.26.0", ["numpy.whl"]))
    print(registry.publishPackage("numpy", "1.26.0", ["numpy.whl"]))  # duplicate -> fail
    print(registry.publishPackage("requests", "2.31.0", ["requests.whl"]))
 
    print(servers.installPackage("10.0.0.5", "numpy", "1.26.0"))
    print(servers.installPackage("10.0.0.5", "numpy", "1.26.0"))  # idempotent -> ok
    print(servers.installPackage("10.0.0.5", "flask", "2.0.0"))   # not in registry -> fail
 
    reqs = "numpy==1.26.0\nrequests==2.31.0\n"
    print(servers.installFromRequirements("10.0.0.6", reqs))
 
    print("Installed on 10.0.0.5:", servers.getInstalledPackages("10.0.0.5"))
    print("Installed on 10.0.0.6:", servers.getInstalledPackages("10.0.0.6"))
 
    print(registry.removePackage("numpy"))
    print(registry.removePackage("numpy"))  # already gone -> fail

"""
Questions:
    0. what is External APIs (upload_package_file_to_registry, etc.) are stubbed
       here to simulate success/failure so the module is runnable/testable
       standalone. In production these would be the real REST calls.
    1. if another team discovers an error in an existing package with a specific version,
       and they will want to remove it from government registry, what will you tell them to do?.
`removePackage(packageName)` removes ALL versions of that package.
       (Task 1 has no dependency concept yet — that's introduced in Task 2 —
       so there's no blocking here. This file is intentionally "naive".)
    2. Re-publishing the exact same (name, version) is treated as an error
       (packages should be immutable once published) rather than silently
       overwritten. This is a policy choice worth stating out loud.
    3. is install Package: Pure deterministic 	Impure deterministic 	Pure Nondeterministic 	Impure Nondeterministic 	Idempotent
    
    `installPackage` is idempotent: installing a package/version that's
       already installed on that server is a no-op success, not an error.

       
"""



"""
YOUR TASK 2:
Dependencies 


Package metadata now must include = {
 name: string
 version: version is any string following X.X.X
 dependencies: list of you decide
}


Your task: ensure your code can behave:
- All apps installing packages must install all necessary dependencies, even if they are not listed in requirements.
"""
publishPackage(
    name="pandas",
    version="2.0",
    files=["pandas.whl"],
    dependencies=[
        ("numpy", "1.26.0"),
        ("python-dateutil", "2.8.2")
    ]
)


""" task 3: """
* "Can we revoke a package?"
* "How do we find everything affected?"
* "How do we support exceptions to automatic patching?"
* "How do we prevent deleting a dependency in use?"

The candidate's job is to recognize that the current data model is no longer sufficient and evolve it incrementally. That's a hallmark of [REDACTED]'s Learning interview: your ability to absorb new rules, identify the missing abstractions, and adapt your design without starting over.

"""task 4: rollback"""


"""

Questions:
B depends on A
I Install B in server A.
What should happen if I run  getInstalledPackages on a server
Expected A, B


If A 1.0.0 already exists, should another copy A 2.0.0 be installed?
If A 1.0.0 already exists, should another copy A 1.0.1 be installed?


If A 1.0.0 already exists and I want to install


Delete A while B depends on it.

Should it succeed?

Expected answer

No.

Need dependency tracking.

---

The candidate typically implements

'''
Package Registry

Dependency Graph

Application Install List
'''


Question

How do you efficiently find every application that must be updated?

Instead they keep introducing new operational requirements:


This problem also has plenty of room for follow-up questions about scalability (millions of packages), concurrency (simultaneous publishes and installs), and consistency (ensuring applications don't see partially approved dependency trees), making it a strong approximation of the style of discussion reported by [REDACTED] candidates.


 """