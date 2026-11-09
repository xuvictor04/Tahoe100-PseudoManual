---
symbol: "NEK5"
type: "gene"
col: 12359
ensembl_id: "ENSG00000197168"
name: "NIMA related kinase 5"
location: "13q14.3"
module: 27
arm: "+"
pooled_cpm: 4.16
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 16
n_dd_up_clean: 19
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# NEK5

*NIMA related kinase 5* — 13q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.52× (z +16.1, q 0e+00, up in 24 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.523× (z -8.0, q 8e-13, down in 22 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EMID1]] (+0.56, fdr 1e-05), [[PSD2]] (+0.55, fdr 1e-05), [[TRD-AS1]] (+0.53, fdr 1e-05); moves opposite to [[MRFAP1]] (-0.42, fdr 1e-04), [[IPO13]] (-0.41, fdr 3e-04), [[CC2D1B]] (-0.41, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CACNG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12359.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.52×** | +16.1 | 0e+00 | 24/35 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.34×** | +10.5 | 2e-23 | 24/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +8.4 | 1e-14 | 24/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +7.0 | 3e-10 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +6.4 | 1e-08 | 17/45 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.4 | 2e-08 | 7/31 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +6.1 | 1e-07 | 16/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +5.8 | 4e-07 | 1/5 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +5.4 | 3e-06 | 3/14 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.46×** | +4.5 | 4e-04 | 0/19 | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +4.3 | 9e-04 | 7/45 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.3 | 1e-03 | 10/38 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.25×** | +3.8 | 0.005 | 6/44 (A-427, COLO 205, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.008 | 3/39 (Panc 03.27, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.4 | 0.021 | 0/9 | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.021 | 2/41 (PANC-1, LOX-IMVI) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.029 | 4/40 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +3.3 | 0.029 | 5/40 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.0 | 0.060 | 3/45 (HEC-1-A, A-172, …) | top dose only |  |
| [[BI-3406 (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.078 | 0/41 | inconsistent across doses |  |
| [[Naproxen (drug)]] 0.05 µM |  | **1.29×** | +2.9 | 0.078 | 2/30 (LoVo, C-33 A) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12359.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.523×** | -8.0 | 8e-13 | 22/44 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.528×** | -7.9 | 9e-13 | 22/43 (SW480, A-427, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.554×** | -7.3 | 6e-11 | 20/28 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.699×** | -6.3 | 6e-08 | 18/44 (LoVo, AN3 CA, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.627×** | -5.8 | 9e-07 | 17/46 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.631×** | -5.5 | 4e-06 | 16/43 (A-427, MIA PaCa-2, …) | two highest doses | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.669×** | -5.0 | 6e-05 | 15/36 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.677×** | -4.8 | 1e-04 | 11/42 (SW480, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.681×** | -4.7 | 1e-04 | 12/42 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.728×** | -3.9 | 0.005 | 11/32 (COLO 205, HepG2/C3A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.732×** | -3.9 | 0.006 | 15/44 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Malotilate (drug)]] 0.5 µM |  | **0.764×** | -3.3 | 0.043 | 11/41 (C-33 A, SW 900, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.770×** | -3.1 | 0.077 | 12/41 (NCI-H2347, SW 900, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.778×** | -3.1 | 0.077 | 10/42 (SW480, NCI-H1573, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.759×** | -3.1 | 0.077 | 15/45 (SW480, HT-29, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12359. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 18.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0922× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 11.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 17.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -15.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.221× (z -8.5) |
| [[SW480 (line)]] | alt | 8.20 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.182× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[A-427 (line)]] | wt | 12.3 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -10.1) |
| [[A498 (line)]] | wt | 4.87 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12359), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMID1]] | +0.56 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[PSD2]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[TRD-AS1]] | +0.53 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[HCN1]] | +0.52 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[CGREF1]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[HUNK]] | +0.52 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[IQGAP2]] | +0.52 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[PDK4-AS1]] | +0.51 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[PRKCQ]] | +0.51 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[FGF20]] | +0.51 | +0.56 / +0.38 | both halves | 6e-05 |  |
| [[PPIL6]] | +0.51 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[CECR2]] | +0.50 | +0.43 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRFAP1]] | -0.42 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[IPO13]] | -0.41 | -0.28 / -0.31 | both halves | 3e-04 |  |
| [[CC2D1B]] | -0.41 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[FAM50A]] | -0.41 | -0.30 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNG2]] | B | CACNG2 activity lowers NEK5's level | lines that do not express CACNG2 (9) vs lines expressing it (41) | 1.95× higher at baseline in the lines without CACNG2 | 0.023 | ⚠ within organs, on part of the lines; also absent: FRMD3, NFATC2, ENSG00000285082; maybe low, not absent |
| [[DLX6-AS1]] | B | DLX6-AS1 activity raises NEK5's level | lines that do not express DLX6-AS1 (23) vs lines expressing it (27) | 1.63× lower at baseline in the lines without DLX6-AS1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000249776, FBXO27, KIF1A; maybe low, not absent |
| [[BMP7]] | B | BMP7 activity raises NEK5's level | lines that do not express BMP7 (23) vs lines expressing it (27) | 1.51× lower at baseline in the lines without BMP7 | 0.058 | ⚠ within organs, on part of the lines; also absent: NFASC, ENSG00000291189, KIF1A |
| [[BMP7]] | B | BMP7 activity weakens NEK5's drug response | lines that do not express BMP7 (22) vs lines expressing it (24) | the lines without BMP7 respond 1.07× as strongly (z diff -0.08); strongest at Dinaciclib 5 µM: 1.11x vs 0.44x (z diff -4.1) | 0.070 | ⚠ within organs, on part of the lines; also absent: NFASC, ENSG00000291189, KIF1A; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.452). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.6, 43.0); signed map (61.3, 16.7). **Vector** length 51.4, 6.56% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +16.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +5.4 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.1 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +4.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.0 | -0.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +1.3 |
|  | [[Bendamustine (drug)]] 5 µM |  | +0.9 | +0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +0.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.8 | -5.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -2.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.8 | -5.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.6 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -6.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.0 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | NIMA related kinase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.3 — chr13:52,033,611-52,129,092 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | NIMA related kinase family |
| Matched by | ensembl_id |

UniProt [Q6P3R8](https://www.uniprot.org/uniprotkb/Q6P3R8) carries no function annotation.

**Summary**, from NCBI Gene [341676](https://www.ncbi.nlm.nih.gov/gene/341676):

> Predicted to enable protein kinase activity. Predicted to act upstream of or within positive regulation of striated muscle cell differentiation. Located in sperm flagellum. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7748](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7748) · Entrez [341676](https://www.ncbi.nlm.nih.gov/gene/341676) · UniProt [Q6P3R8](https://www.uniprot.org/uniprotkb/Q6P3R8) · Ensembl [ENSG00000197168](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197168)

## Data

Gene col 12359: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12359); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12359, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12359]; `tensor/DDL_lfc|DDL_z.npy` [12359]; `embed/gene_vectors.npy` [12359]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12359 or target_col == 12359). Every well: [[NEK5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEK5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
