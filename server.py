from pathlib import Path
from typing import Optional
from mcp.server.fastmcp import FastMCP

# Initialize MCP server instance
REPO_ROOT = Path(__file__).parent.resolve()
mcp = FastMCP("laravel-skills-localsetup")

def _get_primary_skill_file() -> Path:
    """Locates the primary markdown skill asset or fallback documentation."""
    skill_files = list(REPO_ROOT.glob("skills/**/SKILL.md"))
    if skill_files:
        return skill_files[0]
    md_files = [f for f in REPO_ROOT.glob("*.md") if f.name.lower() != "readme.md"]
    if md_files:
        return md_files[0]
    return REPO_ROOT / "README.md"

@mcp.resource("skill://content")
def get_skill_resource() -> str:
    """Provides the complete raw skill documentation as an MCP context resource."""
    target_file = _get_primary_skill_file()
    if not target_file.is_file():
        return "No markdown documentation found in repository."
    return target_file.read_text(encoding="utf-8")

@mcp.tool()
def get_guidelines(section: Optional[str] = None) -> str:
    """
    Returns procedural guidelines and domain rules for Laravel 13 local development setup.
    Args:
        section: Optional keyword to filter content sections.
    """
    target_file = _get_primary_skill_file()
    if not target_file.is_file():
        return "No documentation found."
    
    content = target_file.read_text(encoding="utf-8")
    
    if section:
        lines = content.splitlines()
        matched = [line for line in lines if section.lower() in line.lower()]
        return "\n".join(matched) if matched else f"No sections found matching '{section}'."
        
    return content

if __name__ == "__main__":
    mcp.run(transport="stdio")
