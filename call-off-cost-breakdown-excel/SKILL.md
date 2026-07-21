---
name: call-off-cost-breakdown-excel
version: "0.1.0"
status: beta
description: Web ChatGPT spreadsheet workflow for converting a structured target-price or quotation workbook into a visually faithful call-off cost-breakdown template with three-level dependent dropdowns, formula-driven pricing, a mirrored quotation sheet, and a preserved source-reference sheet. Use when an uploaded Excel template is the visual source of truth and source data must remain auditable without inventing absent fields.
triggers:
  - call-off cost breakdown
  - call off template
  - quotation template
  - dependent dropdown Excel
  - cascading dropdown
  - Target Price template
  - pixel-level Excel replication
  - Excel data validation
  - 报价模板
  - 成本拆分模板
  - 三级联动下拉
  - Excel 像素级复刻
  - call off 模板
do_not_use_for:
  - inventing source fields or prices that are absent
  - general financial modelling without a source workbook
  - accounting certification or tax advice
  - flattening a workbook to CSV
  - claiming native Excel interaction without evidence
  - unrelated spreadsheet cleanup
requires:
  uploaded_files: true
  spreadsheet_tool: true
  web: optional
  github: optional
  local_filesystem: false
  shell: false
  background_work: false
---

# Call-off Cost Breakdown Excel

## Purpose

Use this skill to transform two uploaded workbooks:

1. a **source price / requirement workbook**, commonly containing a `Target Price` sheet; and
2. a **visual template workbook**, commonly containing a call-off cost breakdown and quotation form.

The output is a clean, reusable Excel workbook that:

- visually follows the supplied template;
- preserves source pricing evidence;
- provides a three-level selection flow: `Classification → Product Family → Name`;
- automatically resolves unit price and subtotal;
- mirrors the call-off rows into a quotation sheet;
- embeds the original source sheet as a reference;
- does not invent fields such as `Unit` when the source workbook does not contain them;
- does not expose technical helper addresses in the business-facing sheet.

This skill is designed for Web ChatGPT spreadsheet execution. It must use the spreadsheet tool available in the current surface and may only claim workbook creation or validation that is supported by actual tool output.

## Core principle

**Source schema controls business meaning. The visual template controls presentation. Neither may silently override the other.**

Examples:

- If the visual template contains `Unit` but the price source has no authoritative unit field, remove `Unit`; do not infer `pcs`, `license`, or `repair case` from classification.
- If the source contains a numeric list price and discount, derive unit price deterministically.
- If the source contains a blank price or a textual rule such as `LIST PRICE * 18%` without the underlying base price, mark it for manual pricing; do not fabricate a number.
- If the template contains stale external defined names, broken links, or irrelevant helper columns, build a clean workbook while reproducing its visible style rather than cloning defects.

## Execution boundary

The skill may use:

- uploaded XLSX workbooks;
- the current surface's spreadsheet creation/editing tool;
- workbook inspection, formula inspection, rendering, and export provided by that tool;
- GitHub only when the user asks to save the workflow, code, or documentation there.

The skill must not claim that it:

- opened or clicked dropdowns in native Microsoft Excel unless a real Excel interaction tool produced that evidence;
- ran local shell commands or LibreOffice unless those tools were actually invoked;
- performed a pixel diff unless screenshots or renders were compared;
- validated printing, recalculation, or dropdown interaction in a native client without telemetry.

When native Excel smoke testing is unavailable, report structural validation separately from native-client validation.

## Required inputs

Identify or obtain:

- **Source workbook**: the authoritative price and requirement data.
- **Visual template workbook**: the desired layout and style.
- **Source sheet**: commonly `Target Price`.
- **Selection field**: the demand or quantity column that determines initially populated call-off lines.
- **Tax rule**: preserve the template rule; do not invent a tax rate.
- **Output title and metadata**: frame contract, vendor, quarter, project name.
- **Reference-sheet requirement**: whether the original source sheet must be embedded.

Ask one high-impact clarification only when a missing answer materially changes business meaning. Otherwise infer from workbook evidence and state the assumption.

## Adversarial preflight

Before editing, stress-test the request on these questions:

1. Which workbook is authoritative for business fields?
2. Which workbook or screenshot is authoritative for visual appearance?
3. Is the source's `Quantity` / demand column unambiguous?
4. Are `Classification`, `Product Family`, and `Name` all present and populated?
5. Is unit price numeric, formula-derived, blank, or textual?
6. Does the requested output contain any field absent from the source?
7. Is a visible QA sheet requested, or should QA remain outside the business workbook?
8. Must the source sheet be preserved exactly or only copied as values?
9. Are there external links, stale defined names, or broken validations in the template?
10. What evidence will establish that the dropdowns work?

If a requested field has no source evidence, default to **omit**, not infer.

## Workbook inspection workflow

Inspect both workbooks before writing.

### Source workbook inspection

Record:

- sheet names and used ranges;
- header rows and merged headers;
- exact column mapping;
- total populated source rows;
- selected rows where the demand/quantity field is populated;
- distinct classifications;
- product families by classification;
- item names by classification and family;
- duplicate `(Classification, Product Family, Name)` keys;
- numeric prices, blank prices, textual price rules, and discount formats;
- formulas and cached values in price columns;
- external links and named ranges when observable.

A typical mapping is:

| Business field | Source column role |
|---|---|
| Classification | top-level product class |
| Product Family | second-level family |
| Material-No. | item identifier |
| Name | selectable quotation item |
| Quantity | selected demand / call-off quantity |
| List Price | gross price |
| Discount | fractional discount |
| Unit Price | `List Price × (1 − Discount)` when both inputs are numeric |

Do not hard-code column letters until the header mapping is verified.

### Visual template inspection

Record:

- title and metadata blocks;
- sheet order and names;
- merged ranges;
- used ranges;
- column widths and row heights;
- fonts, fills, borders, number formats, and alignment;
- input-cell color convention;
- calculated-cell color convention;
- totals layout;
- quotation layout;
- freeze panes, gridline visibility, print settings, and margins when observable;
- existing data validation formulas;
- external defined names or broken helper references.

Use the workbook itself as the primary visual source. Use screenshots as acceptance references when supplied.

## Clone-or-rebuild decision

Choose one route.

### Route A — Clone the mother template

Use when:

- the template has no broken external names or links;
- the business columns match the required source fields;
- row extension can preserve formulas and validation safely;
- the template's sheet structure should remain unchanged.

Copy the workbook, then edit only values, formulas, validation ranges, and required row extensions.

### Route B — Clean rebuild from the visual contract

Use when:

- the template contains irrelevant fields absent from the source;
- hidden helper artifacts leak into the business sheet;
- external defined names point to another workbook;
- cloning preserves broken validations or links;
- significant structural redesign is needed for dependent dropdowns.

Create a clean workbook and reproduce the visible template geometry and style. Copy the source reference sheet separately.

Do not use a manual approximation merely because it is faster. Reproduce measurable geometry: merged ranges, widths, heights, fills, borders, alignment, font size, and number format.

## Canonical output structure

Default sheet order:

1. `Call-off Template`
2. `Quotation`
3. `Target Price`
4. `@Template`

Do not add a visible `Mapping & QA` sheet by default. Put QA findings in the final response or a separate report. Add a visible QA sheet only when the user explicitly requests it.

### Call-off Template reference layout

For a source without a Unit field, use:

| Column | Field | Behavior |
|---|---|---|
| B | `#` | sequential number |
| C | `Classification` | dropdown |
| D | `Product Family` | dependent dropdown |
| E | `Name` | dependent dropdown |
| F | `Quantity` | user input / source-prefill, numeric validation |
| G | `WBS #` | dropdown or manual input according to template |
| H | `Unit Price (RMB)` | formula-driven |
| I | `Subtotal (RMB)` | formula-driven |

Do not retain a `Unit` column solely because the visual donor template contains one.

## Source normalization

Create one master row per unique quotation item.

Recommended `@Template` master fields:

| Column | Field |
|---|---|
| A | Lookup Key: `Classification|Product Family|Name` |
| B | Classification |
| C | Product Family |
| D | Name |
| E | Material-No. |
| F | Unit Price |
| G | Pricing Status |
| H | Source Row |
| I | List Price |
| J | Discount |
| K | Source Price Text |

### Pricing rules

Classify each source item:

- `OK numeric price`: list price is numeric; discount is numeric or safely defaults to zero.
- `Manual pricing required`: list price is blank, non-numeric, or depends on an unavailable base price.

For numeric rows:

```text
Unit Price = List Price × (1 − Discount)
```

Do not treat a textual rule such as `LIST PRICE * 16.8%` as a calculable number unless the base list price is independently available and the intended formula is verified.

Do not silently drop manual-price rows. Preserve them in the call-off selection and show a visible missing-price state.

## Three-level dependent dropdown architecture

The required selection sequence is:

```text
Classification → Product Family → Name
```

### Helper-sheet data model

Keep all helper lists on `@Template`, not on the visible business sheet.

Recommended regions:

- `M2:M...`: classification list.
- `N2:N...`: product-family lists grouped contiguously by classification.
- `O:Q`: classification-to-family-range address map.
- `S2:S...`: name lists grouped contiguously by classification and family.
- `T:V`: classification-plus-family-to-name-range address map.
- `X2:X...`: delivery-quarter list.
- `Y2:Y...`: WBS list.

Example classification map:

| O | P | Q |
|---|---:|---|
| HW | 5 | `'@Template'!$N$2:$N$6` |
| SW | 17 | `'@Template'!$N$7:$N$23` |
| Repair HW | 1 | `'@Template'!$N$24:$N$24` |

Example name map key:

```text
HW|VN
SW|CANoe
Repair HW|Repair
```

### Data validation formulas

Excel data validation frequently rejects ordinary cross-sheet list references. Prefer workbook named ranges when the spreadsheet tool can reliably create and preserve them. Otherwise use `INDIRECT` over text addresses stored in the helper map.

Representative formulas for row 12:

```excel
Classification:
=INDIRECT("'@Template'!$M$2:$M$4")

Product Family:
=INDIRECT(VLOOKUP($C12,INDIRECT("'@Template'!$O$2:$Q$4"),3,FALSE))

Name:
=INDIRECT(VLOOKUP($C12&"|"&$D12,INDIRECT("'@Template'!$T$2:$V$24"),3,FALSE))
```

Rules:

- Use absolute references for fixed helper tables.
- Keep the current detail row relative, such as `$C12` and `$D12`.
- Ensure every map result is a valid text range address.
- Do not place range-address formulas in visible columns to the right of the business table.
- Extend each validation to every editable detail row.
- Set `inCellDropDown` to false for numeric validation so Quantity does not display a misleading dropdown arrow.

## Formula architecture

### Unit price lookup

Use the composite key and pricing status. Representative row-12 formula:

```excel
=IF(
  $E12="",
  "Mandatory Field Missing",
  IFERROR(
    IF(
      VLOOKUP($C12&"|"&$D12&"|"&$E12,'@Template'!$A$2:$K$746,7,FALSE)="OK numeric price",
      VLOOKUP($C12&"|"&$D12&"|"&$E12,'@Template'!$A$2:$K$746,6,FALSE),
      "Mandatory Field Missing"
    ),
    "Mandatory Field Missing"
  )
)
```

Generate the last row dynamically. Do not hard-code `746` unless inspection proves it is the correct master-data boundary.

### Subtotal

```excel
=IF(OR($F12="",NOT(ISNUMBER($H12))),"-",ROUND($F12*$H12,2))
```

### Totals

```excel
Total w/o VAT = SUM(all subtotal rows)
VAT           = Total w/o VAT × template tax rate
Total w VAT   = Total w/o VAT + VAT
```

Preserve the tax rate from the visual template or user instruction. Do not infer a jurisdictional tax rule.

## Quotation sheet rule

The quotation sheet must mirror the call-off sheet. It must not maintain a second independent item-selection system.

Recommended quotation columns when Unit is absent:

- Item
- Unit Price
- Quantity
- Subtotal
- Classification
- Product Family

Every quotation line should reference the corresponding call-off line. This prevents two conflicting sources of truth.

## Target Price reference sheet

Copy the original source `Target Price` sheet into the output as a reference.

Preserve when supported:

- values;
- formulas;
- merged cells;
- column widths;
- row heights;
- styles;
- freeze panes;
- source remarks.

Do not alter source prices merely to make call-off formulas easier. Normalize pricing in `@Template`; preserve the source sheet as evidence.

## Visual contract

When the visual target resembles a conventional call-off form, use these defaults unless the supplied template differs:

- business-sheet gridlines hidden;
- centered bold title around 20 pt;
- metadata labels right-aligned and bold;
- metadata values centered with bottom borders;
- descriptive sentence above the table;
- table header: light gray `#D9D9D9`, black bold text, medium black borders;
- selection cells: white;
- manual input cells such as Quantity and WBS: pale yellow `#FFF2CC`;
- calculated cells: light gray `#F2F2F2`;
- missing mandatory values: red text `#C00000` on the normal calculated-cell background;
- totals area: light gray with bold labels;
- numeric formats: thousands separators and two decimal places;
- no helper addresses visible beyond the business table;
- frozen header row when the detail table is long.

Avoid dark dashboards or decorative styling when the reference is a procurement form.

## Style fidelity workflow

1. Inspect computed style for representative cells:
   - title;
   - metadata label and value;
   - header;
   - dropdown cell;
   - numeric input cell;
   - calculated price cell;
   - missing-value cell;
   - total label and total value.
2. Reproduce fill, font, border, alignment, wrap, and number format.
3. Reproduce column widths and row heights.
4. Render the same visible region as the reference screenshot.
5. Compare hierarchy, spacing, proportions, and color semantics.
6. Revise the workbook rather than explaining away visible differences.

A logically correct workbook is not visually accepted when the user explicitly requested template replication.

## Known failure modes

### All dropdown values show `#REF!`

Likely causes:

- helper formulas refer to the wrong sheet name;
- cross-sheet data validation uses unsupported direct references;
- the template sheet is named `@Template` but formulas use `Template`;
- named ranges point to a deleted external workbook.

Fix:

- inspect exact sheet names;
- use quoted sheet names;
- use verified named ranges or `INDIRECT` text addresses;
- remove stale external defined names;
- reopen the generated workbook and inspect formulas again.

### Helper addresses appear in visible columns

Cause: row-specific address formulas were stored on the call-off sheet.

Fix: move classification, family, name, quarter, and WBS lists and maps entirely to `@Template`. Use data validation formulas that query the helper maps directly.

### Unit was invented

Cause: the executor inferred units from classification or item type.

Fix: remove the Unit column from both call-off and quotation sheets unless an authoritative source column exists.

### Visual template looks like a dashboard

Cause: the workbook was restyled generically instead of reproducing the procurement form.

Fix: return to the source template's spacing, light-gray headers, white/yellow inputs, gray calculated fields, thin borders, and restrained typography.

### Quotation and call-off disagree

Cause: both sheets have independent dropdowns or copied static values.

Fix: make quotation formulas reference the call-off rows.

### Manual price rows disappear from totals without explanation

Cause: blank or textual prices were silently excluded.

Fix: retain the item, show `Mandatory Field Missing`, use `-` for subtotal, and report the count and source rows in the final QA summary.

## Validation gate

Before delivering the workbook, verify all of the following.

### Schema and completeness

- Source and template files opened successfully.
- Source sheet and header mapping are explicit.
- Selected source-row count equals populated call-off-row count.
- No duplicate composite lookup keys exist.
- Every selected item is present in `@Template`.
- No field absent from the source was invented.

### Dropdown integrity

- Classification list contains all source classifications.
- Every classification resolves to its product-family list.
- Every classification-family pair resolves to its name list.
- Data validation covers all intended rows.
- Helper range addresses do not appear in visible business cells.
- Quantity uses numeric validation, not list validation.

### Formula integrity

- Unit price returns a number for verified numeric-price items.
- Manual-price items return the intended missing-value message.
- Subtotal is numeric only when quantity and unit price are numeric.
- Total, VAT, and total-with-tax formulas cover the full detail range.
- Search finds no `#REF!`, `#VALUE!`, `#NAME?`, `#DIV/0!`, or unexpected `#N/A`.
- Quotation formulas mirror the call-off rows.

### Workbook hygiene

- Sheet order is correct.
- No stale external links or external defined names remain.
- No visible QA sheet exists unless requested.
- No helper columns are visible on the business sheets.
- `Target Price` is preserved as a reference.
- Output can be reopened by the spreadsheet tool.

### Visual validation

- Render the top call-off region.
- Render representative detail rows and totals.
- Compare against the supplied screenshot or template.
- Confirm the business sheet does not expose gridline-heavy empty columns or helper ranges.

### Native Excel validation

When native Microsoft Excel interaction is available, perform:

1. Open the file.
2. Select a Classification.
3. Confirm Product Family options are filtered.
4. Select a Product Family.
5. Confirm Name options are filtered.
6. Change the Name and confirm Unit Price recalculates.
7. Enter Quantity and confirm Subtotal recalculates.
8. Save, close, reopen, and repeat one dropdown check.

When native Excel interaction is unavailable, state:

```text
Structural workbook validation completed. Native Excel dropdown interaction was not directly observed.
```

Do not call that limitation a full native-client PASS.

## Output contract

Return:

1. **Workbook link**.
2. **Sheet structure**.
3. **Source row count and populated call-off row count**.
4. **Dropdown architecture**.
5. **Removed unsupported fields**, such as Unit.
6. **Manual-pricing count and handling**.
7. **Formula-error scan result**.
8. **Visual changes made**.
9. **Native Excel validation status**.
10. **Residual risks**, if any.

## Stop conditions

Stop instead of producing a misleading workbook when:

- either input workbook cannot be opened;
- the source headers cannot be resolved with reasonable confidence;
- more than one quantity column could materially change the selection set;
- classification-family-name relationships contain unresolved duplicates;
- the requested field is absent but the user insists on an inferred value without a rule;
- data validation cannot be written without broken references;
- the generated workbook cannot be reopened;
- visual acceptance depends on an unavailable reference image or template;
- native Excel behavior is required for certification but cannot be observed.

Report the blocker, evidence, and next required action. Do not fabricate a PASS.
