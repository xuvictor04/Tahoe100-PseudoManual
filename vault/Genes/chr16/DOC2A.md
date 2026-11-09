---
symbol: "DOC2A"
type: "gene"
col: 7417
ensembl_id: "ENSG00000149927"
name: "double C2 domain alpha"
location: "16p11.2"
module: 45
arm: "+"
pooled_cpm: 3.59
n_lines_expressing: 38
n_dd_up: 15
n_dd_down: 24
n_dd_up_clean: 8
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# DOC2A

*double C2 domain alpha* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.61× (z +11.1, q 1e-25, up in 2 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.31× (z +10.6, q 6e-24, up in 27 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.318× (z -10.3, q 3e-22, down in 20 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACACB]] (+0.63, fdr 7e-06), [[LINC00173]] (+0.63, fdr 1e-05), [[JAK3]] (+0.62, fdr 1e-05); moves opposite to [[ATP6V0A2]] (-0.51, fdr 3e-05), [[ZNF778]] (-0.51, fdr 1e-04), [[AP4E1]] (-0.43, fdr 3e-04).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[RASGEF1A]] → it (grade B ⚠); 2 go from it, the strongest it → [[MAP6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7417.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.61×** | +11.1 | 1e-25 | 2/6 (NCI-H2030, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.31×** | +10.6 | 6e-24 | 27/32 (A498, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.45×** | +8.0 | 2e-13 | 19/29 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.45×** | +8.0 | 2e-13 | 21/34 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.11×** | +6.7 | 3e-09 | 20/34 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +6.1 | 8e-08 | 4/11 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.50×** | +5.1 | 3e-05 | 8/33 (A498, A-172, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +4.7 | 2e-04 | 2/8 (NCI-H2030, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.5 | 5e-04 | 6/33 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.60×** | +4.2 | 0.001 | 12/34 (A498, LS 180, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +3.5 | 0.026 | 8/34 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.027 | 10/30 (CFPAC-1, NCI-H23, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.48×** | +3.4 | 0.033 | 7/22 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.02×** | +3.3 | 0.039 | 2/31 (A498, A-172) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.44×** | +3.2 | 0.044 | 6/29 (A498, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7417.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.318×** | -10.3 | 3e-22 | 20/29 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.319×** | -10.3 | 3e-22 | 22/32 (PANC-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.551×** | -7.6 | 6e-12 | 20/27 (MIA PaCa-2, NCI-H23, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.434×** | -7.5 | 9e-12 | 19/27 (A549, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.446×** | -7.3 | 4e-11 | 22/34 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.503×** | -5.8 | 4e-07 | 17/28 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.632×** | -5.8 | 4e-07 | 14/33 (MIA PaCa-2, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.514×** | -5.7 | 6e-07 | 18/32 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.536×** | -5.6 | 1e-06 | 17/29 (RPMI-7951, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.562×** | -5.2 | 1e-05 | 12/24 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.594×** | -4.7 | 1e-04 | 17/32 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.651×** | -3.9 | 0.005 | 14/31 (PANC-1, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.651×** | -3.9 | 0.005 | 15/19 (NCI-H23, A549, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.653×** | -3.8 | 0.005 | 12/34 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.657×** | -3.8 | 0.006 | 9/34 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.659×** | -3.7 | 0.006 | 15/34 (CFPAC-1, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.677×** | -3.5 | 0.014 | 12/34 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.681×** | -3.5 | 0.016 | 12/33 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.682×** | -3.3 | 0.026 | 13/29 (HCT15, NCI-H2030, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.696×** | -3.1 | 0.047 | 4/33 (MIA PaCa-2, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7417. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 6.84 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0612× (z -10.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0806× (z -9.7) |
| [[PANC-1 (line)]] | alt | 5.67 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.133× (z -10.0) |
| [[LoVo (line)]] | wt | 4.42 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0452× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 21.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -14.6) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.172× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 7.61 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.125× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0666× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.123× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 5.26 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0670× (z -9.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 4.46 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.32× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 8.62 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0513× (z -9.7) |
| [[A-172 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.805 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.680 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.694 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.791 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.363 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.831 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7417), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACACB]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[LINC00173]] | +0.63 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[JAK3]] | +0.62 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[KCNK15-AS1]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[NUDT7]] | +0.56 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[BCAM]] | +0.54 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[GAMT]] | +0.53 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ACBD4]] | +0.53 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[KNDC1]] | +0.53 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ERICH6-AS1]] | +0.52 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[GHDC]] | +0.52 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[PCOLCE]] | +0.52 | +0.57 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V0A2]] | -0.51 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[ZNF778]] | -0.51 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[AP4E1]] | -0.43 | -0.29 / -0.40 | both halves | 3e-04 |  |
| [[LTO1]] | -0.43 | -0.26 / -0.41 | both halves | 3e-04 |  |
| [[DCTN2]] | -0.42 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[MAPKAP1]] | -0.42 | -0.30 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGEF1A]] | B | RASGEF1A activity raises DOC2A's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.96× lower at baseline in the lines without RASGEF1A | 0.029 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[LINC00466]] | B | LINC00466 activity raises DOC2A's level | lines that do not express LINC00466 (15) vs lines expressing it (35) | 1.96× lower at baseline in the lines without LINC00466 | 0.032 | ⚠ within organs, on part of the lines; also absent: FAM124A, NTN1, SSPOP; maybe low, not absent |
| [[RDM1P5]] | B | RDM1P5 activity raises DOC2A's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.91× lower at baseline in the lines without RDM1P5 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[OLFML2A]] | B | OLFML2A activity raises DOC2A's level | lines that do not express OLFML2A (20) vs lines expressing it (30) | 1.70× lower at baseline in the lines without OLFML2A | 0.041 | ⚠ within organs, on part of the lines; also absent: GBX1, FMNL1-DT, SCN5A |
| [[LINC02175]] | B | LINC02175 activity raises DOC2A's level | lines that do not express LINC02175 (7) vs lines expressing it (43) | 1.97× lower at baseline in the lines without LINC02175 | 0.086 | ⚠ within organs, on part of the lines; also absent: CEP41, LRRIQ3, FAM182B; maybe low, not absent |
| [[ID2-AS1]] | B | ID2-AS1 activity raises DOC2A's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.81× lower at baseline in the lines without ID2-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP6]] | B | DOC2A activity raises MAP6's level | lines that do not express DOC2A (12) vs lines expressing it (38) | 1.79× lower at baseline in the lines without DOC2A | 0.039 | ⚠ within organs, on part of the lines; also absent: C12orf56, ENSG00000267405; maybe low, not absent |
| [[ELFN2]] | B | DOC2A activity raises ELFN2's level | lines that do not express DOC2A (12) vs lines expressing it (38) | 1.68× lower at baseline in the lines without DOC2A | 0.093 | ⚠ within organs, on part of the lines; also absent: C12orf56, ENSG00000267405; maybe low, not absent |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-0.7, 33.3); signed map (41.1, -9.1). **Vector** length 53.5, 9.51% of its response variance represented; |z| ≥ 3 in 856 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +10.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +8.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +2.0 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +11.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.8 | +2.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.7 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.6 | -7.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -2.6 | -7.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.5 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.1 | -5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -5.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.5 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | double C2 domain alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,005,514-30,023,270 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Synaptotagmin like tandem C2 proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14183](https://www.uniprot.org/uniprotkb/Q14183) (Double C2-like domain-containing protein alpha):

> Calcium sensor which most probably regulates fusion of vesicles with membranes. Binds calcium and phospholipids. May be involved in calcium dependent neurotransmitter release through the interaction with UNC13A. May be involved in calcium-dependent spontaneous release of neurotransmitter in absence of action potentials in neuronal cells. Regulates Ca(2+)-dependent secretory lysosome exocytosis in mast cells.

**Summary**, from NCBI Gene [8448](https://www.ncbi.nlm.nih.gov/gene/8448):

> There are at least two protein isoforms of the Double C2 protein, namely alpha (DOC2A) and beta (DOC2B), which contain two C2-like domains. DOC2A and DOC2B are encoded by different genes; these genes are at times confused with the unrelated DAB2 gene which was initially named DOC-2. DOC2A is mainly expressed in brain and is suggested to be involved in Ca(2+)-dependent neurotransmitter release. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:2985](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2985) · Entrez [8448](https://www.ncbi.nlm.nih.gov/gene/8448) · UniProt [Q14183](https://www.uniprot.org/uniprotkb/Q14183) · Ensembl [ENSG00000149927](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149927)

## Data

Gene col 7417: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7417); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7417, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7417]; `tensor/DDL_lfc|DDL_z.npy` [7417]; `embed/gene_vectors.npy` [7417]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7417 or target_col == 7417). Every well: [[DOC2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOC2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
