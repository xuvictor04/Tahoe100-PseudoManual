---
symbol: "GCG"
type: "gene"
col: 3643
ensembl_id: "ENSG00000115263"
name: "glucagon"
location: "2q24.2"
module: 128
arm: "+"
pooled_cpm: 5.37
n_lines_expressing: 4
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 13
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# GCG

*glucagon* — 2q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.46× (z +10.0, q 8e-21, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 3.68× (z +9.5, q 4e-19, up in 0 of 2 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.148×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.147×).
> Its strongest partners by |cos| (77 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPC3]] (+0.63, fdr 1e-05), [[NR5A2]] (+0.62, fdr 2e-05), [[MMRN1]] (+0.61, fdr 1e-04); moves opposite to [[GPCPD1]] (-0.35, fdr 3e-04), [[NOS3]] (-0.35, fdr 9e-04, ⚠ not reproduced), [[MAP4K3-DT]] (-0.35, fdr 0.001, ⚠ not reproduced), [[PYROXD2]] (-0.34, fdr 6e-04).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MSRB3-AS1]] → it (grade C ⚠); 13 go from it, the strongest it → [[MSRB3-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3643.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.46×** | +10.0 | 8e-21 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.68×** | +9.5 | 4e-19 | 0/2 | rises with dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.82×** | +9.1 | 1e-17 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.08×** | +8.6 | 8e-16 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +5.5 | 4e-06 | 0/2 | top dose only | cell-cycle shift (explains ~8% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.81×** | +4.9 | 7e-05 | 0/1 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +4.6 | 4e-04 | 0/2 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.90×** | +4.3 | 0.001 | 0/1 | top dose only | noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.93×** | +4.0 | 0.005 | 0/1 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.10×** | +3.8 | 0.007 | 0/2 | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +3.8 | 0.009 | 0/1 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **2.03×** | +3.7 | 0.011 | 0/1 | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +3.6 | 0.011 | 0/1 | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.94×** | +3.4 | 0.026 | 0/1 | inconsistent across doses | low cells (technical?) |
| [[Saquinavir (drug)]] 5 µM |  | **1.57×** | +3.3 | 0.039 | 0/2 | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +3.2 | 0.054 | 0/2 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.34×** | +3.1 | 0.055 | 0/1 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.80×** | +3.0 | 0.074 | 1/2 (A-427) | two highest doses | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.77×** | +3.0 | 0.087 | 0/2 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +2.9 | 0.093 | 0/2 | rises with dose | cell-cycle shift (explains ~25% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3643.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.148×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.147×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | 0.520× | -3.4 | 0.38 | 0/2 | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.850× | -3.1 | 0.63 | 0/2 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3643. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 229 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -12.9) |
| [[A-172 (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.266 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.289 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.514 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.340 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.316 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.531 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.310 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.406 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.329 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.315 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.368 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.303 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3643), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 21 of them with an alert (⚠; 21 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPC3]] | +0.63 | +0.55 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[NR5A2]] | +0.62 | +0.65 / +0.47 | both halves | 2e-05 | **novel candidate** |
| [[MMRN1]] | +0.61 | +0.74 / +0.36 | both halves | 1e-04 | **novel candidate** |
| [[LINC02643]] | +0.56 | +0.65 / +0.32 | both halves | 2e-04 | **novel candidate** |
| [[JPH3]] | +0.52 | +0.55 / +0.22 | both halves | 6e-04 |  |
| [[CACNA1B]] | +0.50 | +0.48 / +0.32 | both halves | 2e-04 |  |
| [[KIF26A]] | +0.50 | +0.28 / +0.49 | both halves | 3e-04 |  |
| [[MAGEA4]] | +0.49 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[FBXO27]] | +0.48 | +0.46 / +0.26 | both halves | 4e-04 |  |
| [[ELFN1]] | +0.48 | +0.60 / +0.25 | both halves | 4e-04 |  |
| [[DPYSL5]] | +0.48 | +0.42 / +0.29 | both halves | 2e-04 |  |
| [[RFPL1S]] | +0.47 | +0.45 / +0.17 | ⚠ not reproduced | 0.001 |  |
| [[KCNQ2]] | +0.47 | +0.34 / +0.40 | both halves | 1e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPCPD1]] | -0.35 | -0.28 / -0.35 | both halves | 3e-04 |  |
| [[NOS3]] | -0.35 | -0.18 / -0.31 | ⚠ not reproduced | 9e-04 | STRING 480 |
| [[MAP4K3-DT]] | -0.35 | -0.28 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[PYROXD2]] | -0.34 | -0.33 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSRB3-AS1]] | C | MSRB3-AS1 activity raises GCG's level | lines that do not express MSRB3-AS1 (42) vs lines expressing it (8) | 3.11× lower at baseline in the lines without MSRB3-AS1 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2; co-absent with the target |
| [[MMRN1]] | C | MMRN1 activity raises GCG's level | lines that do not express MMRN1 (43) vs lines expressing it (7) | 3.59× lower at baseline in the lines without MMRN1 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, KRT5; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSRB3-AS1]] | C | GCG activity raises MSRB3-AS1's level | lines that do not express GCG (46) vs lines expressing it (4) | 7.40× lower at baseline in the lines without GCG | 0.009 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, LINC01205, APOB; co-absent with the target |
| [[GPC3]] | C | GCG activity raises GPC3's level | lines that do not express GCG (46) vs lines expressing it (4) | 11.66× lower at baseline in the lines without GCG | 0.009 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, LINC01205, APOB; co-absent with the target |
| [[GREM1]] | C | GCG activity raises GREM1's level | lines that do not express GCG (46) vs lines expressing it (4) | 6.03× lower at baseline in the lines without GCG | 0.021 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, LINC01205, APOB; co-absent with the target |
| [[ERBB4]] | C | GCG activity raises ERBB4's level | lines that do not express GCG (46) vs lines expressing it (4) | 19.01× lower at baseline in the lines without GCG | 0.026 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, LINC01205, APOB; co-absent with the target |
| [[LINC01429]] | C | GCG activity raises LINC01429's level | lines that do not express GCG (46) vs lines expressing it (4) | 3.85× lower at baseline in the lines without GCG | 0.030 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, LINC01205, APOB |
| [[UNC5C]] | C | GCG activity raises UNC5C's level | lines that do not express GCG (46) vs lines expressing it (4) | 4.77× lower at baseline in the lines without GCG | 0.036 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, LINC01205, APOB; co-absent with the target |
| [[LINC01203]] | C | GCG activity raises LINC01203's level | lines that do not express GCG (46) vs lines expressing it (4) | 3.63× lower at baseline in the lines without GCG | 0.057 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, LINC01205, APOB; co-absent with the target |
| [[MMRN1]] | C | GCG activity raises MMRN1's level | lines that do not express GCG (46) vs lines expressing it (4) | 8.57× lower at baseline in the lines without GCG | 0.061 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, LINC01205, APOB; co-absent with the target |
| [[LINC00470]] | C | GCG activity raises LINC00470's level | lines that do not express GCG (46) vs lines expressing it (4) | 9.37× lower at baseline in the lines without GCG | 0.063 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, LINC01205, APOB; co-absent with the target |
| [[CTNNA2]] | C | GCG activity raises CTNNA2's level | lines that do not express GCG (46) vs lines expressing it (4) | 7.99× lower at baseline in the lines without GCG | 0.063 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, LINC01205, APOB; co-absent with the target |
| [[COL11A1]] | C | GCG activity raises COL11A1's level | lines that do not express GCG (46) vs lines expressing it (4) | 8.24× lower at baseline in the lines without GCG | 0.067 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, LINC01205, APOB; co-absent with the target |
| [[TERT]] | C | GCG activity raises TERT's level | lines that do not express GCG (46) vs lines expressing it (4) | 2.95× lower at baseline in the lines without GCG | 0.088 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, LINC01205, APOB |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.555). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.8, 37.0); signed map (25.5, 25.8). **Vector** length 7.02, 2.66% of its response variance represented; |z| ≥ 3 in 37 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.3 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.3 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.2 | +0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.2 | +10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.2 | +1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.1 | +3.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.1 | +2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.1 | +0.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +0.1 | +3.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.3 | -0.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.2 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.2 | -0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.2 | -3.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.1 | +0.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | -0.1 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.1 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.1 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | glucagon |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.2 — chr2:162,142,882-162,152,404 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GLP1, GLP2, GRPP, GLP-1 |
| Gene groups (HGNC) | Receptor ligands |
| Hallmark sets | PANCREAS_BETA_CELLS |
| Reactome | 15 pathways, smallest: Synthesis, secretion, and deacylation of Ghrelin; Synthesis, secretion, and inactivation of Glucagon-like Peptide-1 (GLP-1); Incretin synthesis, secretion, and inactivation |
| Matched by | ensembl_id |

**Function**, from UniProt [P01275](https://www.uniprot.org/uniprotkb/P01275) (Pro-glucagon):

> [Glucagon]: Plays a key role in glucose metabolism and homeostasis. Regulates blood glucose by increasing gluconeogenesis and decreasing glycolysis. A counterregulatory hormone of insulin, raises plasma glucose levels in response to insulin-induced hypoglycemia. Plays an important role in initiating and maintaining hyperglycemic conditions in diabetes. Binds to and activates the glucagon receptor GCGR, which couples to the G(s) G protein and elevates intracellular cAMP, triggering downstream …

**Summary**, from NCBI Gene [2641](https://www.ncbi.nlm.nih.gov/gene/2641):

> The protein encoded by this gene is a proglucagon precursor that is cleaved into four distinct mature peptides. One of these, glucagon, is a pancreatic hormone that counteracts the glucose-lowering action of insulin by stimulating glycogenolysis and gluconeogenesis in the liver. In addition, glucagon promotes lipolysis and ketone body formation during prolonged fasting or stress. Glucagon secretion is stimulated by low blood glucose and inhibited by high glucose or insulin. Glucagon is a ligand …

**Accessions** — [HGNC:4191](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4191) · Entrez [2641](https://www.ncbi.nlm.nih.gov/gene/2641) · UniProt [P01275](https://www.uniprot.org/uniprotkb/P01275) · Ensembl [ENSG00000115263](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115263)

## Data

Gene col 3643: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3643); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3643, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3643]; `tensor/DDL_lfc|DDL_z.npy` [3643]; `embed/gene_vectors.npy` [3643]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3643 or target_col == 3643). Every well: [[GCG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
