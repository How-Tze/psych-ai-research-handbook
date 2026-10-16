-- Mechanical print transformations; substantive text comes from the approved QMD.
local site = 'https://How-Tze.github.io/psych-ai-research-handbook/'

function Link(el)
  local target = el.target
  -- Quarto resolves chapter-to-chapter links. Download resources need web URLs
  -- because the distributable DOCX/PDF does not sit beside the source folders.
  local resource = target:match('^%.%./(examples/.*)')
    or target:match('^%.%./(downloads/.*)')
    or target:match('^%.%./(drafts/.*)')
    or target:match('^(release/.*)')
    or target:match('^(examples/.*)')
    or target:match('^(downloads/.*)')
  if resource then el.target = site .. resource end
  return el
end

function Div(el)
  if el.classes:includes('legacy-anchor') then return {} end
  for _, class in ipairs(el.classes) do
    if class:match('^callout%-') then
      -- Keep the original lead-in and all paragraphs; avoid boxed one-cell
      -- tables that paginate poorly in the print edition.
      if el.content[1] and el.content[1].t == 'Header' then
        el.content[1] = pandoc.Para({pandoc.Strong(el.content[1].content)})
      end
      return el.content
    end
  end
end
