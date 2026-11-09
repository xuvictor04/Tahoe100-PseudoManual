---
symbol: "HCLS1"
type: "gene"
col: 11100
ensembl_id: "ENSG00000180353"
name: "hematopoietic cell-specific Lyn substrate 1"
location: "3q13.33"
module: 39
arm: "+"
pooled_cpm: 5.75
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 21
n_dd_up_clean: 13
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# HCLS1

*hematopoietic cell-specific Lyn substrate 1* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.92× (z +16.5, q 0e+00, up in 32 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.371× (z -8.5, q 1e-14, down in 31 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.374× (z -8.4, q 1e-14, down in 29 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYOCOS]] (+0.87, fdr 7e-06), [[USP50]] (+0.84, fdr 7e-06), [[C3orf20]] (+0.82, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11100.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.92×** | +16.5 | 0e+00 | 32/37 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.00×** | +13.3 | 5e-38 | 36/39 (Panc 03.27, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.20×** | +10.0 | 4e-21 | 26/36 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **2.69×** | +8.5 | 4e-15 | 35/46 (SW480, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.6 | 3e-06 | 15/46 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +5.1 | 3e-05 | 4/12 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +5.0 | 5e-05 | 12/35 (HT-29, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.44×** | +4.4 | 8e-04 | 13/45 (CFPAC-1, J82, …) | rises with dose | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +4.2 | 0.002 | 15/46 (A-427, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +3.9 | 0.005 | 13/33 (MIA PaCa-2, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.56×** | +3.8 | 0.007 | 10/46 (HEC-1-A, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.68×** | +3.7 | 0.009 | 10/42 (LoVo, A498, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.29×** | +3.7 | 0.009 | 3/42 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.5 | 0.017 | 7/47 (NCI-H23, SW 900, …) | inconsistent across doses |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **2.16×** | +3.5 | 0.021 | 2/46 (HOP62, Panc 03.27) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 0.05 µM |  | **1.46×** | +3.2 | 0.045 | 6/44 (H4, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11100.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.371×** | -8.5 | 1e-14 | 31/39 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.374×** | -8.4 | 1e-14 | 29/46 (KATO III, BT-474, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.381×** | -8.3 | 3e-14 | 31/42 (NCI-H1573, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.504×** | -5.9 | 7e-07 | 22/39 (SW 900, J82, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.509×** | -5.8 | 9e-07 | 25/42 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.556×** | -5.0 | 5e-05 | 20/42 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.674×** | -4.8 | 1e-04 | 17/44 (C32, HS-578T, …) | top dose only |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **0.557×** | -4.2 | 0.002 | 16/44 (PANC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.564×** | -4.1 | 0.002 | 12/41 (NCI-H23, LoVo, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.624×** | -4.0 | 0.003 | 20/46 (RPMI-7951, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.730×** | -3.8 | 0.007 | 15/46 (NCI-H1573, H4, …) | rises with dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.739×** | -3.7 | 0.012 | 7/47 (AN3 CA, SNU-1, …) | top dose only |  |
| [[Lonafarnib (drug)]] 0.05 µM |  | **0.628×** | -3.4 | 0.035 | 4/44 (SNU-423, PANC-1, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.668×** | -3.3 | 0.036 | 9/46 (NCI-H2030, HOP62, …) | top dose only | plate-row cell shift |
| [[LB-100 (drug)]] 0.05 µM |  | **0.633×** | -3.3 | 0.037 | 2/45 (HT-29, PANC-1) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.675×** | -3.2 | 0.041 | 13/36 (SW 900, Hs 766T, …) | top dose only | position effect removed |
| [[vincristine (drug)]] 0.05 µM |  | **0.638×** | -3.2 | 0.041 | 6/43 (MIA PaCa-2, J82, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11100. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 16.7 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +14.8) | [[Digitoxin (drug)]] 5 µM 0.0834× (z -13.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 15.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0641× (z -11.4) |
| [[H4 (line)]] | wt | 16.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0536× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 8.06 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.62× (z +8.9) | [[Silodosin (drug)]] 0.5 µM 0.0719× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 8.08 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.174× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 5.76 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0442× (z -9.1) |
| [[C32 (line)]] | wt | 2.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0769× (z -11.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 3.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.81× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 6.63 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.05 µM 0.0446× (z -9.0) |
| [[J82 (line)]] | alt | 3.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.01× (z +8.6) | — |
| [[KATO III (line)]] | alt | 10.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0364× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 7.68 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0561× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 6.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.49× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 3.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +8.5) | — |
| [[SW480 (line)]] | alt | 3.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.40× (z +10.8) | — |
| [[A-172 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11100), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYOCOS]] | +0.87 | +0.85 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[USP50]] | +0.84 | +0.83 / +0.81 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.82 | +0.85 / +0.69 | both halves | 7e-06 |  |
| [[ARL9]] | +0.82 | +0.83 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[FNDC7]] | +0.82 | +0.82 / +0.76 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.81 | +0.78 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[SLC6A13]] | +0.81 | +0.83 / +0.74 | both halves | 7e-06 |  |
| [[ROPN1L]] | +0.81 | +0.81 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[TRIM72]] | +0.81 | +0.79 / +0.77 | both halves | 7e-06 |  |
| [[C21orf91-OT1]] | +0.81 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[OIT3]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.80 | +0.79 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HCLS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC2A9]] | B | SLC2A9 activity raises HCLS1's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without SLC2A9 | 0.065 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[IMPA1P1]] | B | IMPA1P1 activity raises HCLS1's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.85× lower at baseline in the lines without IMPA1P1 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[SEMA4A]] | B | SEMA4A activity raises HCLS1's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without SEMA4A | 0.085 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[TRIM72]] | C | TRIM72 activity raises HCLS1's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.92× lower at baseline in the lines without TRIM72 | 0.070 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |
| [[TTC36]] | C | TTC36's natural level strengthens HCLS1's drug response | TTC36's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.20; direction not clear | 0.080 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.869). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.0, -14.6); signed map (17.0, 9.2). **Vector** length 96.1, 20.4% of its response variance represented; |z| ≥ 3 in 1,261 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.0 | +16.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +13.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.2 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.7 | +1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.0 | +8.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.0 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +5.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.8 | +2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +0.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.8 | -5.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.4 | -1.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.2 | -8.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.1 | -4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -8.5 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.5 | -4.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.5 | -3.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | hematopoietic cell-specific Lyn substrate 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.33 — chr3:121,631,399-121,660,927 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HS1, CTTNL |
| Gene groups (HGNC) | SH3 domain containing |
| Hallmark sets | ALLOGRAFT_REJECTION, DNA_REPAIR |
| Matched by | ensembl_id |

**Function**, from UniProt [P14317](https://www.uniprot.org/uniprotkb/P14317) (Hematopoietic lineage cell-specific protein):

> Substrate of the antigen receptor-coupled tyrosine kinase. Plays a role in antigen receptor signaling for both clonal expansion and deletion in lymphoid cells. May also be involved in the regulation of gene expression.

**Summary**, from NCBI Gene [3059](https://www.ncbi.nlm.nih.gov/gene/3059):

> Enables RNA polymerase II-specific DNA-binding transcription factor binding activity; protein kinase binding activity; and signaling adaptor activity. Involved in several processes, including granulocyte colony-stimulating factor signaling pathway; positive regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction; and positive regulation of protein import into nucleus. Located in cytosol; nucleus; and plasma membrane. Part of transcription regulator complex. [provided by …

**Accessions** — [HGNC:4844](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4844) · Entrez [3059](https://www.ncbi.nlm.nih.gov/gene/3059) · UniProt [P14317](https://www.uniprot.org/uniprotkb/P14317) · Ensembl [ENSG00000180353](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180353)

## Data

Gene col 11100: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11100); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11100, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11100]; `tensor/DDL_lfc|DDL_z.npy` [11100]; `embed/gene_vectors.npy` [11100]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11100 or target_col == 11100). Every well: [[HCLS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HCLS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
