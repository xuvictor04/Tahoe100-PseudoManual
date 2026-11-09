---
symbol: "CPPED1"
type: "gene"
col: 2362
ensembl_id: "ENSG00000103381"
name: "calcineurin like phosphoesterase domain containing 1"
location: "16p13.12"
module: 64
arm: "+"
pooled_cpm: 30.86
n_lines_expressing: 45
n_dd_up: 5
n_dd_down: 20
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# CPPED1

*calcineurin like phosphoesterase domain containing 1* — 16p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.23× (z +5.8, q 5e-06, up in 21 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.499× (z -19.0, q 0e+00, down in 33 of 42 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM7]] (+0.50, fdr 6e-05), [[MICU2]] (+0.49, fdr 3e-05), [[TRIP4]] (+0.48, fdr 1e-05); moves opposite to [[PTCH1]] (-0.45, fdr 3e-04), [[CDC42EP4]] (-0.44, fdr 8e-05), [[ING1]] (-0.43, fdr 1e-04).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[CDKN2C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2362.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +5.8 | 5e-06 | 21/43 (KATO III, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | 1.18× | +4.5 | 0.002 | 14/43 (A-172, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.020 | 9/43 (A-427, LS 180, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.21×** | +3.7 | 0.025 | 11/36 (SK-MEL-2, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.060 | 7/42 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.091 | 9/43 (AsPC-1, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.14 | 9/28 (A-172, HEC-1-A, …) | two highest doses | composition shift |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.14 | 10/43 (A549, A-172, …) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 5 µM |  | 1.35× | +3.1 | 0.14 | 4/43 (SW480, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.12× | +3.0 | 0.14 | 6/43 (SW480, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2362.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.499×** | -19.0 | 0e+00 | 33/42 (SNU-423, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.530×** | -17.4 | 0e+00 | 33/42 (NCI-H460, SW1417, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.596×** | -10.0 | 3e-21 | 28/42 (SNU-423, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.603×** | -9.4 | 8e-19 | 28/42 (NCI-H460, SNU-423, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.607×** | -9.3 | 2e-18 | 25/41 (SNU-423, NCI-H23, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.631×** | -8.6 | 1e-15 | 27/43 (SNU-423, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.660×** | -8.0 | 7e-14 | 30/42 (SK-MEL-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.649×** | -8.0 | 7e-14 | 23/40 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.665×** | -7.9 | 2e-13 | 28/43 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.695×** | -7.0 | 1e-10 | 23/42 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.718×** | -6.4 | 8e-09 | 24/43 (CFPAC-1, J82, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.735×** | -6.0 | 1e-07 | 22/41 (NCI-H460, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.735×** | -6.0 | 1e-07 | 23/43 (SNU-423, NCI-H460, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.740×** | -5.8 | 2e-07 | 22/42 (NCI-H460, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.581×** | -5.5 | 2e-06 | 19/40 (KATO III, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.767×** | -5.1 | 9e-06 | 22/42 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.857× | -3.0 | 0.079 | 14/42 (SW480, C32, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.747×** | -2.9 | 0.088 | 10/43 (NCI-H460, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2362. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.8 | 0 | 16 (12 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -19.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.289× (z -18.9) |
| [[SNU-423 (line)]] | alt | 139 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -22.2) |
| [[SW480 (line)]] | alt | 52.8 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -15.4) |
| [[C32 (line)]] | wt | 25.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -11.1) |
| [[H4 (line)]] | wt | 27.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0896× (z -19.0) |
| [[SK-MEL-2 (line)]] | alt | 27.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -15.7) |
| [[AsPC-1 (line)]] | alt | 33.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 23.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 42.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -13.7) |
| [[HepG2_C3A (line)]] | wt | 102 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -13.9) |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.280× (z -9.5) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.432× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 31.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -15.0) |
| [[SW1417 (line)]] | alt | 64.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -16.0) |
| [[A-172 (line)]] | wt | 63.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -12.0) |
| [[A498 (line)]] | wt | 54.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -12.0) |
| [[A549 (line)]] | wt | 48.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -9.6) |
| [[BT-474 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.148× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[C-33 A (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[CHP-212 (line)]] | wt | 19.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0970× (z -9.9) |
| [[HOP62 (line)]] | alt | 30.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -9.9) |
| [[HS-578T (line)]] | alt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 8.69 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 22.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -21.5) |
| [[NCI-H2030 (line)]] | alt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 20.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.118× (z -13.9) |
| [[NCI-H2347 (line)]] | alt | 20.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 20.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -10.4) |
| [[RKO (line)]] | wt | 28.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -10.4) |
| [[SNU-1 (line)]] | wt | 38.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -9.1) |
| [[A-427 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.35 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.61 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.82 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2362), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM7]] | +0.50 | +0.52 / +0.39 | both halves | 6e-05 |  |
| [[MICU2]] | +0.49 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[TRIP4]] | +0.48 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ZDHHC13]] | +0.44 | +0.39 / +0.41 | both halves | 5e-05 |  |
| [[CEBPZOS]] | +0.43 | +0.27 / +0.52 | both halves | 3e-04 |  |
| [[PLPP4]] | +0.43 | +0.44 / +0.36 | both halves | 9e-05 |  |
| [[PISD]] | +0.43 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[SHLD1]] | +0.41 | +0.34 / +0.45 | both halves | 1e-04 |  |
| [[NRDE2]] | +0.41 | +0.45 / +0.39 | both halves | 5e-05 |  |
| [[MANBAL]] | +0.41 | +0.30 / +0.41 | both halves | 2e-04 |  |
| [[DMAP1]] | +0.41 | +0.27 / +0.44 | both halves | 3e-04 |  |
| [[CUEDC1]] | +0.41 | +0.31 / +0.43 | both halves | 2e-04 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTCH1]] | -0.45 | -0.29 / -0.49 | both halves | 3e-04 |  |
| [[CDC42EP4]] | -0.44 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[ING1]] | -0.43 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[NFKBID]] | -0.41 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[NPAT]] | -0.41 | -0.18 / -0.53 | ⚠ one half (not replicated) | 9e-04 |  |
| [[ICAM3]] | -0.41 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[NSUN6]] | -0.40 | -0.40 / -0.30 | both halves | 2e-04 |  |
| [[SEMA4A]] | -0.40 | -0.38 / -0.38 | both halves | 6e-05 |  |
| [[SIM2]] | -0.40 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[SEPTIN9-DT]] | -0.39 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[IL2RG]] | -0.39 | -0.37 / -0.38 | both halves | 7e-05 |  |
| [[KATNA1]] | -0.39 | -0.35 / -0.32 | both halves | 2e-04 |  |
| [[NSD3]] | -0.38 | -0.25 / -0.46 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDKN2C]] | B | CPPED1 activity lowers CDKN2C's level | lines that do not express CPPED1 (5) vs lines expressing it (45) | 1.83× higher at baseline in the lines without CPPED1 | 0.051 | ⚠ within organs, on part of the lines; also absent: CCDC144CP |
| [[CREB3L1]] | B | CPPED1 activity lowers CREB3L1's level | lines that do not express CPPED1 (5) vs lines expressing it (45) | 4.61× higher at baseline in the lines without CPPED1 | 0.068 | ⚠ within organs, on part of the lines; also absent: CCDC144CP |
| [[PIGB]] | B | CPPED1 activity raises PIGB's level | lines that do not express CPPED1 (5) vs lines expressing it (45) | 1.40× lower at baseline in the lines without CPPED1 | 0.081 | ⚠ within organs, on part of the lines; also absent: CCDC144CP |

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.314). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (25.9, -24.0); signed map (-18.3, -20.4). **Vector** length 75.3, 14.2% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +3.9 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.0 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +5.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +0.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -17.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.1 | -8.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.2 | -8.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -9.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.3 | -19.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.8 | -1.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.4 | -2.7 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | calcineurin like phosphoesterase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.12 — chr16:12,659,799-12,803,887 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CSTP1, FLJ11151 |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRF8](https://www.uniprot.org/uniprotkb/Q9BRF8) (Serine/threonine-protein phosphatase CPPED1):

> Protein phosphatase that dephosphorylates AKT family kinase specifically at 'Ser-473', blocking cell cycle progression and promoting cell apoptosis. May play an inhibitory role in glucose uptake by adipocytes.

**Summary**, from NCBI Gene [55313](https://www.ncbi.nlm.nih.gov/gene/55313):

> Predicted to enable metal ion binding activity and protein serine/threonine phosphatase activity. Located in cytosol and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25632](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25632) · Entrez [55313](https://www.ncbi.nlm.nih.gov/gene/55313) · UniProt [Q9BRF8](https://www.uniprot.org/uniprotkb/Q9BRF8) · Ensembl [ENSG00000103381](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103381)

## Data

Gene col 2362: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2362); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2362, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2362]; `tensor/DDL_lfc|DDL_z.npy` [2362]; `embed/gene_vectors.npy` [2362]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2362 or target_col == 2362). Every well: [[CPPED1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPPED1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
