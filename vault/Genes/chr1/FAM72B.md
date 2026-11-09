---
symbol: "FAM72B"
type: "gene"
col: 12030
ensembl_id: "ENSG00000188610"
name: "RUMY family member 2"
location: "1p11.2"
module: 22
arm: "+"
pooled_cpm: 2.3
n_lines_expressing: 44
n_dd_up: 25
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 8
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# FAM72B

*RUMY family member 2* — 1p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.66× (z +12.6, q 2e-33, up in 20 of 27 measured lines) ⚠ cell-cycle shift, explains ~59% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.55× (z +12.0, q 9e-31, up in 21 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.505× (z -6.2, q 3e-07, down in 16 of 31 measured lines) ⚠ cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[Cytarabine (hydrochloride) (drug)]] 0.05 µM: 0.580× (z -4.6, q 8e-04, down in 10 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bendamustine (drug)]] 5 µM in 1 line (A-427 0.0685×); [[Bergenin (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0632×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM72D]] (+0.88, fdr 7e-06), [[FAM72A]] (+0.88, fdr 7e-06), [[CCNB1]] (+0.85, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 8 go from it, the strongest it → [[FAM83D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12030.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **2.66×** | +12.6 | 2e-33 | 20/27 (NCI-H2030, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.55×** | +12.0 | 9e-31 | 21/27 (RPMI-7951, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.68×** | +8.9 | 8e-17 | 2/9 (J82, NCI-H2347) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **2.47×** | +8.2 | 4e-14 | 4/11 (NCI-H2030, NCI-H23, …) | all doses, flat | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.16×** | +7.0 | 3e-10 | 15/40 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +7.0 | 3e-10 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.78×** | +5.2 | 1e-05 | 8/18 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +4.9 | 8e-05 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.64×** | +4.5 | 5e-04 | 10/38 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.62×** | +4.4 | 7e-04 | 8/30 (HOP62, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.62×** | +4.2 | 0.001 | 6/35 (PANC-1, C32, …) | top dose only | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +4.1 | 0.002 | 6/36 (KATO III, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +3.9 | 0.005 | 1/38 (SNU-423) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.008 | 5/39 (PANC-1, SW 900, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.50×** | +3.7 | 0.009 | 7/27 (NCI-H2030, HS-578T, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.023 | 6/37 (H4, HOP62, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.027 | 4/39 (KATO III, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.054 | 1/34 (NCI-H1792) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.056 | 5/36 (KATO III, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.42×** | +3.0 | 0.072 | 2/27 (NCI-H1792, H4) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +2.9 | 0.073 | 4/36 (HEC-1-A, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12030.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bendamustine (drug)]] 5 µM in 1 line (A-427 0.0685×); [[Bergenin (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0632×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.505×** | -6.2 | 3e-07 | 16/31 (A-427, NCI-H2030, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.525×** | -5.9 | 1e-06 | 11/37 (A-172, HOP62, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.580×** | -4.6 | 8e-04 | 10/34 (CFPAC-1, SK-MEL-2, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.630×** | -4.2 | 0.003 | 9/37 (A498, BT-474, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.639×** | -3.9 | 0.008 | 13/32 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.650×** | -3.9 | 0.008 | 5/40 (NCI-H661, PANC-1, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.756×** | -3.6 | 0.022 | 10/36 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.686×** | -3.3 | 0.064 | 9/33 (H4, RKO, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.86 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12030. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 4.68 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0685× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 2.01 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0632× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 5.05 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.32× (z +11.8) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[PANC-1 (line)]] | alt | 6.16 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +9.2) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[A-172 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.894 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.956 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.608 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.767 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.000 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.228 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.555 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.961 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 0.919 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12030), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM72D]] | +0.88 | +0.85 / +0.88 | both halves | 7e-06 | STRING 640 |
| [[FAM72A]] | +0.88 | +0.85 / +0.86 | both halves | 7e-06 | STRING 636 |
| [[CCNB1]] | +0.85 | +0.77 / +0.86 | both halves | 7e-06 |  |
| [[PIF1]] | +0.85 | +0.76 / +0.86 | both halves | 7e-06 |  |
| [[TROAP]] | +0.83 | +0.75 / +0.84 | both halves | 7e-06 |  |
| [[BUB1]] | +0.83 | +0.76 / +0.85 | both halves | 7e-06 | STRING 468 |
| [[DLGAP5]] | +0.83 | +0.78 / +0.84 | both halves | 7e-06 | STRING 473 |
| [[CCNB2]] | +0.82 | +0.76 / +0.83 | both halves | 7e-06 |  |
| [[AURKA]] | +0.82 | +0.74 / +0.86 | both halves | 7e-06 |  |
| [[KIF20A]] | +0.82 | +0.73 / +0.84 | both halves | 7e-06 |  |
| [[TACC3]] | +0.81 | +0.71 / +0.85 | both halves | 7e-06 |  |
| [[KNSTRN]] | +0.80 | +0.77 / +0.79 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83D]] | B | FAM72B activity raises FAM83D's level | lines that do not express FAM72B (6) vs lines expressing it (44) | 1.72× lower at baseline in the lines without FAM72B | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC02798, SRGAP2C, ZNF512B; its own permutation p |
| [[PTTG1]] | B | FAM72B activity raises PTTG1's level | lines that do not express FAM72B (6) vs lines expressing it (44) | 1.71× lower at baseline in the lines without FAM72B | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC02798, SRGAP2C, ZNF512B; its own permutation p |
| [[KIF4A]] | B | FAM72B activity raises KIF4A's level | lines that do not express FAM72B (6) vs lines expressing it (44) | 1.54× lower at baseline in the lines without FAM72B | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC02798, SRGAP2C, ZNF512B; its own permutation p |
| [[FAM72A]] | B | FAM72B activity raises FAM72A's level | lines that do not express FAM72B (6) vs lines expressing it (44) | 1.77× lower at baseline in the lines without FAM72B | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC02798, SRGAP2C, ZNF512B |
| [[KPNA2]] | B | FAM72B activity raises KPNA2's level | lines that do not express FAM72B (6) vs lines expressing it (44) | 1.72× lower at baseline in the lines without FAM72B | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC02798, SRGAP2C, ZNF512B; its own permutation p |
| [[TPX2]] | B | FAM72B activity raises TPX2's level | lines that do not express FAM72B (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without FAM72B | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC02798, SRGAP2C, ZNF512B; its own permutation p |
| [[ARHGAP11B]] | B | FAM72B activity raises ARHGAP11B's level | lines that do not express FAM72B (6) vs lines expressing it (44) | 1.21× lower at baseline in the lines without FAM72B | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC02798, SRGAP2C, ZNF512B; its own permutation p |
| [[PRR11]] | B | FAM72B activity raises PRR11's level | lines that do not express FAM72B (6) vs lines expressing it (44) | 2.22× lower at baseline in the lines without FAM72B | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC02798, SRGAP2C, ZNF512B |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.820). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.3, -58.5); signed map (-52.3, -42.3). **Vector** length 51.2, 7.86% of its response variance represented; |z| ≥ 3 in 854 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.65 to 60); *DREAM G2/M down* (control, mean cos +0.77 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.61 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +4.0 | +12.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +12.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | +3.3 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +7.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.7 | +2.6 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.1 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +1.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.1 | +3.4 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.0 | +3.7 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +0.9 | +2.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.2 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -2.1 | -3.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -2.0 | -6.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.3 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -1.9 | -3.9 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -4.6 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.5 | -2.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.5 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | +1.0 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | RUMY family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p11.2 — chr1:121,167,646-121,185,539 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RP11-439A17.6; previously FAM72B |
| Matched by | ensembl_id |

UniProt [Q86X60](https://www.uniprot.org/uniprotkb/Q86X60) carries no function annotation.

**Summary**, from NCBI Gene [653820](https://www.ncbi.nlm.nih.gov/gene/653820):

> Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24805](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24805) · Entrez [653820](https://www.ncbi.nlm.nih.gov/gene/653820) · UniProt [Q86X60](https://www.uniprot.org/uniprotkb/Q86X60) · Ensembl [ENSG00000188610](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188610)

## Data

Gene col 12030: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12030); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12030, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12030]; `tensor/DDL_lfc|DDL_z.npy` [12030]; `embed/gene_vectors.npy` [12030]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12030 or target_col == 12030). Every well: [[FAM72B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM72B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
