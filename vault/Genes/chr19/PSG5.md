---
symbol: "PSG5"
type: "gene"
col: 12937
ensembl_id: "ENSG00000204941"
name: "pregnancy specific beta-1-glycoprotein 5"
location: "19q13.31"
module: 125
arm: "+"
pooled_cpm: 3.35
n_lines_expressing: 10
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 17
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# PSG5

*pregnancy specific beta-1-glycoprotein 5* — 19q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 12.0× (z +13.0, q 1e-35, up in 3 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.40× (z +6.7, q 3e-09, up in 3 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LOX-IMVI 0.202×, SNU-423 0.291×, J82 0.331×; ⚠ cell-cycle shift, explains ~44% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0586×; ⚠ cell-cycle shift, explains ~46% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SNU-423 0.174×; ⚠ cell-cycle shift, explains ~87% of this change).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSG4]] (+0.64, fdr 4e-05, ⚠ same locus), [[APBB1IP]] (+0.63, fdr 3e-05), [[PSG9]] (+0.62, fdr 1e-05, ⚠ same locus), [[PDCD1LG2]] (+0.61, fdr 1e-05), [[HDAC2-AS2]] (+0.60, fdr 5e-05); moves opposite to [[TBC1D8]] (-0.44, fdr 2e-04), [[KIF13B]] (-0.43, fdr 8e-05), [[MT1X]] (-0.42, fdr 1e-04).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ROBO4]] → it (grade C ⚠); 17 go from it, the strongest it → [[SLC8A1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12937.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **12.0×** | +13.0 | 1e-35 | 3/3 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.20×** | +9.9 | 1e-20 | 3/4 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.39×** | +9.3 | 3e-18 | 2/3 (J82, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +6.7 | 3e-09 | 3/6 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.81×** | +5.2 | 3e-05 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.54×** | +5.0 | 4e-05 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.44×** | +4.8 | 1e-04 | 2/5 (J82, LOX-IMVI) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.34×** | +4.6 | 3e-04 | 4/7 (A-172, HS-578T, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +4.5 | 4e-04 | 0/5 | top dose only | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +4.1 | 0.003 | 0/4 | top dose only | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +4.0 | 0.003 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +3.8 | 0.007 | 0/5 | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.47×** | +3.5 | 0.018 | 1/3 (SNU-423) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.49×** | +3.5 | 0.018 | 1/4 (LOX-IMVI) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.91×** | +3.5 | 0.019 | 0/5 | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.019 | 1/8 (LOX-IMVI) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.89×** | +3.4 | 0.020 | 2/5 (MIA PaCa-2, LOX-IMVI) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +3.1 | 0.056 | 1/7 (HS-578T) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.76×** | +3.1 | 0.065 | 1/7 (SNU-423) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.75×** | +3.0 | 0.069 | 5/6 (SNU-423, LOX-IMVI, …) | two highest doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +3.0 | 0.073 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.46×** | +2.9 | 0.092 | 3/8 (J82, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12937.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LOX-IMVI 0.202×, SNU-423 0.291×, J82 0.331×; ⚠ cell-cycle shift, explains ~44% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0586×; ⚠ cell-cycle shift, explains ~46% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SNU-423 0.174×; ⚠ cell-cycle shift, explains ~87% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.531× | -3.2 | 0.79 | 2/8 (NCI-H23, A-172) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12937. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 43.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -9.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[LOX-IMVI (line)]] | wt | 18.5 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0586× (z -12.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[J82 (line)]] | alt | 59.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -8.9) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A-172 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.166 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.195 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.233 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.256 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.521 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.251 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.239 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.455 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.202 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.208 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.204 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.921 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.239 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.216 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.195 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.221 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.335 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.205 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.219 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.290 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.775 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12937), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 8 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSG4]] | +0.64 | +0.40 / +0.71 | both halves | 4e-05 | same gene group; pathway: Cell surface interactions at the vascular wall; STRING 782; ⚠ same locus (6.2 kb, same strand: neighbours can correlate without regulation) |
| [[APBB1IP]] | +0.63 | +0.73 / +0.46 | both halves | 3e-05 | **novel candidate** |
| [[PSG9]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 | same gene group; pathway: Cell surface interactions at the vascular wall; STRING 636; ⚠ same locus (25.3 kb, same strand: neighbours can correlate without regulation) |
| [[PDCD1LG2]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[HDAC2-AS2]] | +0.60 | +0.40 / +0.67 | both halves | 5e-05 |  |
| [[LINC01435]] | +0.59 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[PGM5P2-1]] | +0.57 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[PHACTR1]] | +0.56 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[LINC01776]] | +0.56 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[BMPER]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[FGF5]] | +0.54 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[MAP3K7CL]] | +0.53 | +0.30 / +0.63 | both halves | 2e-04 |  |
| [[CALD1]] | +0.53 | +0.38 / +0.47 | both halves | 7e-05 |  |
| [[NTM]] | +0.51 | +0.41 / +0.49 | both halves | 4e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D8]] | -0.44 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[KIF13B]] | -0.43 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[MT1X]] | -0.42 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[ID1]] | -0.42 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[TMEM63A]] | -0.40 | -0.24 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ROBO4]] | C | ROBO4 activity raises PSG5's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.13× lower at baseline in the lines without ROBO4 | 0.024 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1; co-absent with the target |
| [[NETO1]] | C | NETO1 activity raises PSG5's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 1.60× lower at baseline in the lines without NETO1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[APBB1IP]] | C | APBB1IP activity raises PSG5's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 3.46× lower at baseline in the lines without APBB1IP | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749; co-absent with the target |
| [[MIR548XHG]] | C | MIR548XHG activity raises PSG5's level | lines that do not express MIR548XHG (38) vs lines expressing it (12) | 2.24× lower at baseline in the lines without MIR548XHG | 0.088 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000291025, UBBP4-1, COX7B2; co-absent with the target |
| [[POSTN]] | C | POSTN activity raises PSG5's level | lines that do not express POSTN (38) vs lines expressing it (12) | 2.00× lower at baseline in the lines without POSTN | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[CCDC190]] | C | CCDC190 activity raises PSG5's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 2.77× lower at baseline in the lines without CCDC190 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 3, C 14. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC8A1-AS1]] | B | PSG5 activity raises SLC8A1-AS1's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 1.73× lower at baseline in the lines without PSG5 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486 |
| [[TBC1D8]] | B | PSG5 activity lowers TBC1D8's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 1.78× higher at baseline in the lines without PSG5 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486 |
| [[CCDC80]] | B | PSG5 activity raises CCDC80's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 4.88× lower at baseline in the lines without PSG5 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486 |
| [[PHACTR1]] | C | PSG5 activity raises PHACTR1's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 5.27× lower at baseline in the lines without PSG5 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |
| [[FGF5]] | C | PSG5 activity raises FGF5's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 6.09× lower at baseline in the lines without PSG5 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |
| [[ROBO4]] | C | PSG5 activity raises ROBO4's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 3.25× lower at baseline in the lines without PSG5 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |
| [[SLC8A1]] | C | PSG5 activity raises SLC8A1's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 7.19× lower at baseline in the lines without PSG5 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |
| [[PSG4]] | C | PSG5 activity raises PSG4's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 4.12× lower at baseline in the lines without PSG5 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |
| [[FBN2]] | C | PSG5 activity raises FBN2's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 4.41× lower at baseline in the lines without PSG5 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |
| [[NPPB]] | C | PSG5 activity raises NPPB's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 2.05× lower at baseline in the lines without PSG5 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |
| [[DSCAM]] | C | PSG5 activity raises DSCAM's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 2.40× lower at baseline in the lines without PSG5 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |
| [[NETO1]] | C | PSG5 activity raises NETO1's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 2.23× lower at baseline in the lines without PSG5 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.359). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.9, 21.4); signed map (38.5, 24.2). **Vector** length 20.6, 5.00% of its response variance represented; |z| ≥ 3 in 227 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.8 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.7 | +2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.7 | +0.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | +0.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.6 | -2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.6 | -0.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.6 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.6 | +0.1 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | pregnancy specific beta-1-glycoprotein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.31 — chr19:43,166,256-43,186,536 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FL-NCA-3, PSG |
| Gene groups (HGNC) | V-set domain containing; Pregnancy specific glycoproteins |
| Reactome | 2 pathways, smallest: Cell surface interactions at the vascular wall; Hemostasis |
| Matched by | ensembl_id |

UniProt [Q15238](https://www.uniprot.org/uniprotkb/Q15238) carries no function annotation.

**Summary**, from NCBI Gene [5673](https://www.ncbi.nlm.nih.gov/gene/5673):

> The human pregnancy-specific glycoproteins (PSGs) are a group of molecules that are mainly produced by the placental syncytiotrophoblasts during pregnancy. PSGs comprise a subgroup of the carcinoembryonic antigen (CEA) family, which belongs to the immunoglobulin superfamily. For additional general information about the PSG gene family, see PSG1 (MIM 176390).[supplied by OMIM, Oct 2009]

**Accessions** — [HGNC:9522](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9522) · Entrez [5673](https://www.ncbi.nlm.nih.gov/gene/5673) · UniProt [Q15238](https://www.uniprot.org/uniprotkb/Q15238) · Ensembl [ENSG00000204941](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204941)

## Data

Gene col 12937: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12937); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12937, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12937]; `tensor/DDL_lfc|DDL_z.npy` [12937]; `embed/gene_vectors.npy` [12937]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12937 or target_col == 12937). Every well: [[PSG5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSG5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
