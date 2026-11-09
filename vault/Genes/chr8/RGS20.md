---
symbol: "RGS20"
type: "gene"
col: 7193
ensembl_id: "ENSG00000147509"
name: "regulator of G protein signaling 20"
location: "8q11.23"
module: 202
arm: "+"
pooled_cpm: 38.68
n_lines_expressing: 38
n_dd_up: 22
n_dd_down: 12
n_dd_up_clean: 17
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 6
direction_downstream: 9
tags: ["gene", "module/202"]
generated_by: "tahoemap"
---

# RGS20

*regulator of G protein signaling 20* — 8q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.32× (z +12.2, q 2e-31, up in 30 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.380× (z -12.2, q 2e-31, down in 26 of 36 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGM5P2-1]] (+0.67, fdr 1e-05), [[LTO1]] (+0.66, fdr 1e-05), [[SOCS2-AS1]] (+0.65, fdr 2e-05); moves opposite to [[EFNA4]] (-0.65, fdr 1e-05), [[TTLL5]] (-0.62, fdr 1e-05), [[ATG4C]] (-0.61, fdr 3e-05).
> It is in [[Module 202]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[GCNT4]] → it (grade B ⚠); 9 go from it, the strongest it → [[KANTR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7193.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.32×** | +12.2 | 2e-31 | 30/35 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +11.9 | 4e-30 | 27/36 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +7.7 | 3e-12 | 18/30 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +7.0 | 4e-10 | 18/35 (A549, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +6.3 | 4e-08 | 22/36 (NCI-H460, A549, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +6.0 | 2e-07 | 24/36 (A498, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.53×** | +5.9 | 3e-07 | 20/35 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.58×** | +5.9 | 3e-07 | 17/35 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.49×** | +5.8 | 6e-07 | 24/35 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.0 | 3e-05 | 19/35 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +4.9 | 4e-05 | 20/37 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +4.8 | 9e-05 | 16/35 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.6 | 1e-04 | 20/35 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.37×** | +4.6 | 2e-04 | 20/35 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +4.6 | 2e-04 | 18/35 (NCI-H460, A549, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.010 | 13/36 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.010 | 14/35 (SW 900, NCI-H1573, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.010 | 14/35 (A498, NCI-H2030, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.023 | 13/35 (A549, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7193.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.380×** | -12.2 | 2e-31 | 26/36 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.490×** | -10.4 | 1e-22 | 26/36 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.620×** | -6.9 | 7e-10 | 22/35 (PANC-1, A549, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.762×** | -5.6 | 3e-06 | 18/36 (J82, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.698×** | -5.2 | 2e-05 | 18/35 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.691×** | -5.2 | 2e-05 | 22/36 (A-172, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.704×** | -4.4 | 8e-04 | 19/35 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.593×** | -4.0 | 0.005 | 18/34 (RPMI-7951, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.779×** | -3.6 | 0.018 | 14/36 (A-172, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.778×** | -3.5 | 0.031 | 17/36 (NCI-H23, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.803×** | -3.2 | 0.071 | 17/35 (HS-578T, PANC-1, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.806×** | -3.1 | 0.082 | 13/35 (HepG2/C3A, NCI-H2030, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.812× | -3.0 | 0.11 | 12/35 (RPMI-7951, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7193. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 119 | 2 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.182× (z -13.7) |
| [[A-172 (line)]] | wt | 56.8 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -15.9) |
| [[A549 (line)]] | wt | 77.0 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +14.8) | [[Panobinostat (drug)]] 5 µM 0.213× (z -13.0) |
| [[HOP62 (line)]] | alt | 37.0 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.2× (z +17.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +13.4) | — |
| [[PANC-1 (line)]] | alt | 137 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -17.3) |
| [[NCI-H460 (line)]] | wt | 14.2 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +14.9) | — |
| [[A-427 (line)]] | wt | 68.9 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.32× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.278× (z -9.6) |
| [[A498 (line)]] | wt | 32.2 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.307× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 67.7 | 3 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 6.29× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.298× (z -9.0) |
| [[SW 900 (line)]] | alt | 39.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.54× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 20.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +12.2) | — |
| [[HEC-1-A (line)]] | alt | 28.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -9.4) |
| [[J82 (line)]] | alt | 54.2 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.479× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 46.3 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.05× (z +12.2) | — |
| [[SK-MEL-2 (line)]] | alt | 64.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.276× (z -10.4) |
| [[AN3 CA (line)]] | alt | 33.7 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0897× (z -8.6) |
| [[Hs 766T (line)]] | wt | 22.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +11.1) | — |
| [[HS-578T (line)]] | alt | 38.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +12.6) | — |
| [[hTERT-HPNE (line)]] | wt | 45.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +9.7) | — |
| [[SNU-1 (line)]] | wt | 34.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.117× (z -8.6) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.01 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.21 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.64 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.23 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.79 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7193), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGM5P2-1]] | +0.67 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[LTO1]] | +0.66 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[SOCS2-AS1]] | +0.65 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[SLC39A10]] | +0.63 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[SAMD4A]] | +0.63 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[ITPRIPL2]] | +0.63 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[GRK4]] | +0.62 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[AXL]] | +0.62 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[FRMD6-AS2]] | +0.62 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[GJC1]] | +0.62 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[DLGAP4-AS1]] | +0.62 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[ANKRD18B]] | +0.62 | +0.57 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFNA4]] | -0.65 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[TTLL5]] | -0.62 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[ATG4C]] | -0.61 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[MED23]] | -0.61 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[KANTR]] | -0.60 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[ALAD]] | -0.60 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[SUFU]] | -0.60 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[EFNA3]] | -0.60 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[NFRKB]] | -0.59 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[RALGAPA2]] | -0.59 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[MKRN2]] | -0.59 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[PLEKHH3]] | -0.58 | -0.46 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GCNT4]] | B | GCNT4 activity raises RGS20's level | lines that do not express GCNT4 (10) vs lines expressing it (40) | 2.37× lower at baseline in the lines without GCNT4 | 0.010 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SOCS2-AS1]] | B | SOCS2-AS1 activity raises RGS20's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 2.28× lower at baseline in the lines without SOCS2-AS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |
| [[TREM1]] | B | TREM1 activity raises RGS20's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 1.10× lower at baseline in the lines without TREM1 | 0.031 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[FAM171A1]] | B | FAM171A1 activity raises RGS20's level | lines that do not express FAM171A1 (7) vs lines expressing it (43) | 1.73× lower at baseline in the lines without FAM171A1 | 0.050 | ⚠ within organs, on part of the lines; also absent: PORCN, CMTM7, ANXA6 |
| [[PRDM5]] | B | PRDM5 activity raises RGS20's level | lines that do not express PRDM5 (13) vs lines expressing it (37) | 2.08× lower at baseline in the lines without PRDM5 | 0.089 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| [[GJC1]] | C | GJC1 activity raises RGS20's level | lines that do not express GJC1 (13) vs lines expressing it (37) | 3.79× lower at baseline in the lines without GJC1 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KANTR]] | B | RGS20 activity lowers KANTR's level | lines that do not express RGS20 (12) vs lines expressing it (38) | 1.33× higher at baseline in the lines without RGS20 | 0.008 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, ENSG00000286964, SIX1 |
| [[GCNT4]] | B | RGS20 activity raises GCNT4's level | lines that do not express RGS20 (12) vs lines expressing it (38) | 1.66× lower at baseline in the lines without RGS20 | 0.009 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, ENSG00000286964, SIX1 |
| [[TRHDE]] | B | RGS20 activity raises TRHDE's level | lines that do not express RGS20 (12) vs lines expressing it (38) | 1.23× lower at baseline in the lines without RGS20 | 0.026 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, ENSG00000286964, SIX1 |
| [[L2HGDH]] | B | RGS20 activity lowers L2HGDH's level | lines that do not express RGS20 (12) vs lines expressing it (38) | 1.41× higher at baseline in the lines without RGS20 | 0.073 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, ENSG00000286964, SIX1 |
| [[PXDC1]] | B | RGS20 activity raises PXDC1's level | lines that do not express RGS20 (12) vs lines expressing it (38) | 2.67× lower at baseline in the lines without RGS20 | 0.078 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, ENSG00000286964, SIX1 |
| [[PSMD6-AS1]] | B | RGS20 activity raises PSMD6-AS1's level | lines that do not express RGS20 (12) vs lines expressing it (38) | 1.11× lower at baseline in the lines without RGS20 | 0.080 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, ENSG00000286964, SIX1 |
| [[CNOT8]] | B | RGS20 activity raises CNOT8's level | lines that do not express RGS20 (12) vs lines expressing it (38) | 1.26× lower at baseline in the lines without RGS20 | 0.085 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, ENSG00000286964, SIX1 |
| [[FGF2]] | C | RGS20 activity raises FGF2's level | lines that do not express RGS20 (12) vs lines expressing it (38) | 4.95× lower at baseline in the lines without RGS20 | 0.004 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, ENSG00000286964, SIX1; co-absent with the target |
| [[GJC1]] | C | RGS20 activity raises GJC1's level | lines that do not express RGS20 (12) vs lines expressing it (38) | 4.55× lower at baseline in the lines without RGS20 | 0.028 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, ENSG00000286964, SIX1; co-absent with the target |

## Where it sits

- **Module**: [[Module 202]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.795). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.5, 13.2); signed map (27.1, 10.0). **Vector** length 116, 31.1% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.6 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +12.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +11.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.9 | +4.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.9 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +3.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.6 | -12.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.5 | -10.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.0 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -5.2 |
|  | [[NG25 (drug)]] 5 µM |  | -3.0 | -4.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.9 | -5.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.8 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | -2.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | regulator of G protein signaling 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q11.23 — chr8:53,851,795-53,959,303 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RGSZ1, ZGAP1 |
| Gene groups (HGNC) | Regulators of G-protein signaling |
| Reactome | 4 pathways, smallest: G alpha (z) signalling events; G alpha (i) signalling events; GPCR downstream signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [O76081](https://www.uniprot.org/uniprotkb/O76081) (Regulator of G protein signaling 20):

> Inhibits signal transduction by increasing the GTPase activity of G protein alpha subunits thereby driving them into their inactive GDP-bound form. Binds selectively to G(z)-alpha and G(alpha)-i2 subunits, accelerates their GTPase activity and regulates their signaling activities. The G(z)-alpha activity is inhibited by the phosphorylation and palmitoylation of the G protein. Negatively regulates mu-opioid receptor-mediated activation of the G proteins (By similarity).

**Summary**, from NCBI Gene [8601](https://www.ncbi.nlm.nih.gov/gene/8601):

> The protein encoded by this gene belongs to the family of regulator of G protein signaling (RGS) proteins, which are regulatory and structural components of G protein-coupled receptor complexes. RGS proteins inhibit signal transduction by increasing the GTPase activity of G protein alpha subunits, thereby driving them into their inactive GDP-bound forms. This protein selectively binds to G(z)-alpha and G(alpha)-i2 subunits, and regulates their signaling activities. Alternatively spliced …

**Accessions** — [HGNC:14600](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14600) · Entrez [8601](https://www.ncbi.nlm.nih.gov/gene/8601) · UniProt [O76081](https://www.uniprot.org/uniprotkb/O76081) · Ensembl [ENSG00000147509](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147509)

## Data

Gene col 7193: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7193); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7193, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7193]; `tensor/DDL_lfc|DDL_z.npy` [7193]; `embed/gene_vectors.npy` [7193]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7193 or target_col == 7193). Every well: [[RGS20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGS20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
