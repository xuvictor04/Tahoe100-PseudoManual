---
symbol: "CCDC169"
type: "gene"
col: 14326
ensembl_id: "ENSG00000242715"
name: "coiled-coil domain containing 169"
location: "13q13.3"
module: 47
arm: "+"
pooled_cpm: 4.24
n_lines_expressing: 33
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# CCDC169

*coiled-coil domain containing 169* — 13q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.78× (z +15.4, q 0e+00, up in 15 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[HI-TOPK-032 (drug)]] 0.05 µM: 0.675× (z -4.0, q 0.038, down in 5 of 26 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (PANC-1 0.164×, SHP-77 0.0903×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.149×; ⚠ cell-cycle shift, explains ~0% of this change); [[Hesperidin (drug)]] 0.5 µM in 1 line (HOP62 0.0518×); [[Loperamide (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0584×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOHLH2]] (+0.71, fdr 7e-06, ⚠ same locus), [[RNLS]] (+0.61, fdr 1e-05), [[C12orf50]] (+0.61, fdr 1e-05), [[SNHG26]] (+0.60, fdr 1e-05); moves opposite to [[SRGAP2D]] (-0.56, fdr 1e-05), [[SAP130]] (-0.56, fdr 1e-05), [[MAP3K3]] (-0.54, fdr 2e-04).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PYDC2-AS1]] → it (grade B ⚠); 3 go from it, the strongest it → [[FAM171B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14326.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.78×** | +15.4 | 0e+00 | 15/26 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.10×** | +11.6 | 1e-28 | 5/7 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.88×** | +9.5 | 4e-19 | 19/30 (A498, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.43×** | +9.5 | 5e-19 | 10/16 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.22×** | +8.5 | 2e-15 | 13/27 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +8.1 | 5e-14 | 10/25 (HS-578T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.97×** | +7.2 | 4e-11 | 17/30 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +6.0 | 1e-07 | 4/8 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.66×** | +5.4 | 5e-06 | 14/30 (LOX-IMVI, J82, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +5.0 | 3e-05 | 11/29 (J82, A498, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +5.0 | 3e-05 | 9/30 (SHP-77, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.58×** | +4.6 | 2e-04 | 6/28 (A-427, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +4.6 | 2e-04 | 9/29 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.49×** | +4.2 | 9e-04 | 10/30 (J82, SW 900, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.002 | 6/30 (LOX-IMVI, SW 900, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +3.9 | 0.003 | 9/30 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +3.8 | 0.005 | 4/28 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.010 | 4/29 (NCI-H23, J82, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.38×** | +3.4 | 0.016 | 2/28 (NCI-H2030, H4) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.0 | 0.059 | 8/30 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14326.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (PANC-1 0.164×, SHP-77 0.0903×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.149×; ⚠ cell-cycle shift, explains ~0% of this change); [[Hesperidin (drug)]] 0.5 µM in 1 line (HOP62 0.0518×); [[Loperamide (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0584×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.675×** | -4.0 | 0.038 | 5/26 (SK-MEL-2, J82, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.728× | -3.2 | 0.36 | 3/29 (HOP62, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14326. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.65 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 3.06 | 0 | 1 | — | [[Hesperidin (drug)]] 0.5 µM 0.0518× (z -9.8) |
| [[J82 (line)]] | alt | 9.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 3.50 | 0 | 1 | — | [[Loperamide (hydrochloride) (drug)]] 0.05 µM 0.0584× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 9.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0903× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.704 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.718 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.811 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.422 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.382 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.448 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14326), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOHLH2]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 | STRING 522; ⚠ same locus (7.4 kb, same strand: neighbours can correlate without regulation) |
| [[RNLS]] | +0.61 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[C12orf50]] | +0.61 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[SNHG26]] | +0.60 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[SLC2A9]] | +0.59 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[LINC02241]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[CPEB1]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[CDKL1]] | +0.56 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[NCR3LG1]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ATP6V1E2]] | +0.56 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[TIAM2]] | +0.55 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[FBXW10B]] | +0.55 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[SLC6A11]] | +0.54 | +0.25 / +0.54 | both halves | 4e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGAP2D]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[SAP130]] | -0.56 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[MAP3K3]] | -0.54 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[GINM1]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[TRIM62]] | -0.53 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[OSTF1]] | -0.52 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[FLYWCH2]] | -0.52 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[FAM89B]] | -0.52 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[MTMR12]] | -0.51 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[HDGFL2]] | -0.50 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[GNA11]] | -0.50 | -0.29 / -0.43 | both halves | 3e-04 |  |
| [[CMC2]] | -0.50 | -0.38 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PYDC2-AS1]] | B | PYDC2-AS1 activity raises CCDC169's level | lines that do not express PYDC2-AS1 (26) vs lines expressing it (24) | 1.68× lower at baseline in the lines without PYDC2-AS1 | 0.038 | ⚠ within organs, on part of the lines; also absent: BCHE, CPED1, CCNYL2 |
| [[FAM171B]] | B | FAM171B activity raises CCDC169's level | lines that do not express FAM171B (7) vs lines expressing it (43) | 2.93× lower at baseline in the lines without FAM171B | 0.058 | ⚠ within organs, on part of the lines; also absent: NXPE3, GXYLT2, TMOD2; maybe low, not absent |
| [[SOHLH2]] | C | SOHLH2 activity raises CCDC169's level | lines that do not express SOHLH2 (21) vs lines expressing it (29) | 3.15× lower at baseline in the lines without SOHLH2 | 0.037 | ⚠ within organs, on part of the lines; also absent: PRR16, LINC00839, GUCY1B1; co-absent with the target |
| [[LINC00882]] | C | LINC00882 activity raises CCDC169's level | lines that do not express LINC00882 (17) vs lines expressing it (33) | 2.81× lower at baseline in the lines without LINC00882 | 0.038 | ⚠ within organs, on part of the lines; also absent: TUSC3, B3GALT1, EVC; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM171B]] | B | CCDC169 activity raises FAM171B's level | lines that do not express CCDC169 (17) vs lines expressing it (33) | 1.80× lower at baseline in the lines without CCDC169 | 0.074 | ⚠ within organs, on part of the lines; also absent: SPART-AS1, SPART, FIGN; its own permutation p |
| [[DPY19L2]] | C | CCDC169 activity raises DPY19L2's level | lines that do not express CCDC169 (17) vs lines expressing it (33) | 2.85× lower at baseline in the lines without CCDC169 | 0.074 | ⚠ within organs, on part of the lines; also absent: SPART-AS1, SPART, FIGN; co-absent with the target; its own permutation p |
| [[KCNT2]] | C | CCDC169 activity raises KCNT2's level | lines that do not express CCDC169 (17) vs lines expressing it (33) | 3.93× lower at baseline in the lines without CCDC169 | 0.096 | ⚠ within organs, on part of the lines; also absent: SPART-AS1, SPART, FIGN; co-absent with the target |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.418). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.7, 22.7); signed map (38.9, 20.0). **Vector** length 46.3, 7.36% of its response variance represented; |z| ≥ 3 in 745 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +9.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.2 | +9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | +15.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +3.6 |
| fall | [[Belinostat (drug)]] 5 µM |  | -1.4 | +5.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -0.9 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -0.8 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 169 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.3 — chr13:36,222,008-36,297,840 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RP11-251J8.1, LOC728591; previously C13orf38 |
| Matched by | ensembl_id |

UniProt [A6NNP5](https://www.uniprot.org/uniprotkb/A6NNP5) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:34361](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34361) · Entrez [728591](https://www.ncbi.nlm.nih.gov/gene/728591) · UniProt [A6NNP5](https://www.uniprot.org/uniprotkb/A6NNP5) · Ensembl [ENSG00000242715](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242715)

## Data

Gene col 14326: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14326); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14326, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14326]; `tensor/DDL_lfc|DDL_z.npy` [14326]; `embed/gene_vectors.npy` [14326]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14326 or target_col == 14326). Every well: [[CCDC169 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC169.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
