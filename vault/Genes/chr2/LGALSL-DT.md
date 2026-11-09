---
symbol: "LGALSL-DT"
type: "gene"
col: 13369
ensembl_id: "ENSG00000223935"
name: "LGALSL divergent transcript"
location: "2p14"
module: 68
arm: "+"
pooled_cpm: 6.27
n_lines_expressing: 46
n_dd_up: 22
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 5
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# LGALSL-DT

*LGALSL divergent transcript* — 2p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 9.93× (z +40.6, q 0e+00, up in 36 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.361× (z -12.7, q 2e-34, down in 31 of 42 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LGALSL]] (+0.74, fdr 7e-06, ⚠ same locus), [[MARVELD2]] (+0.71, fdr 1e-05), [[PATL2]] (+0.70, fdr 3e-05), [[PLD6]] (+0.70, fdr 1e-05); moves opposite to [[KATNB1]] (-0.65, fdr 7e-05), [[GTF2E2]] (-0.63, fdr 1e-04), [[CTNNBL1]] (-0.63, fdr 1e-04).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TLCD4-RWDD3]] → it (grade B ⚠); 5 go from it, the strongest it → [[PLEKHG3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13369.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **9.93×** | +40.6 | 0e+00 | 36/36 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.66×** | +18.8 | 0e+00 | 34/34 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.50×** | +18.1 | 0e+00 | 36/41 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.9 | 5e-13 | 21/35 (A498, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.68×** | +6.5 | 1e-08 | 15/40 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.36×** | +5.3 | 9e-06 | 10/42 (SW480, J82, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +5.3 | 1e-05 | 18/39 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.1 | 2e-05 | 11/30 (A-172, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +5.1 | 2e-05 | 18/43 (HEC-1-A, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +5.1 | 2e-05 | 17/42 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.7 | 1e-04 | 11/43 (A498, HEC-1-A, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +4.6 | 2e-04 | 10/38 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +4.5 | 3e-04 | 8/43 (NCI-H1792, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.42×** | +4.4 | 5e-04 | 7/40 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.44×** | +4.3 | 5e-04 | 9/39 (A-172, NCI-H23, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +3.9 | 0.003 | 5/40 (NCI-H1573, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13369.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.361×** | -12.7 | 2e-34 | 31/42 (SW48, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.394×** | -11.6 | 7e-29 | 32/43 (HEC-1-A, SW48, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.475×** | -9.3 | 3e-18 | 27/43 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.554×** | -7.4 | 2e-11 | 20/41 (COLO 205, HT-29, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.647×** | -5.4 | 6e-06 | 17/36 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.657×** | -5.3 | 1e-05 | 15/42 (A549, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.694×** | -4.6 | 4e-04 | 15/43 (HEC-1-A, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | **0.762×** | -3.3 | 0.064 | 6/41 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Relugolix (drug)]] 5 µM |  | 0.836× | -3.2 | 0.10 | 3/43 (PANC-1, SNU-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.768× | -3.1 | 0.10 | 9/37 (NCI-H2030, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13369. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 22.9 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.46× (z +23.0) | [[Panobinostat (drug)]] 5 µM 0.149× (z -15.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.205× (z -12.9) |
| [[SW48 (line)]] | wt | 18.8 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +14.1) | [[Panobinostat (drug)]] 0.5 µM 0.0359× (z -13.6) |
| [[A-172 (line)]] | wt | 11.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.0× (z +22.8) | — |
| [[A498 (line)]] | wt | 5.27 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.114× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 7.02 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 8.11× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.0690× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 2.81 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.4× (z +16.9) | — |
| [[SW480 (line)]] | alt | 6.25 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.93× (z +14.3) | [[Belinostat (drug)]] 5 µM 0.193× (z -8.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A549 (line)]] | wt | 7.90 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.78× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 13.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +13.6) | [[Docetaxel (drug)]] 0.05 µM 0.0932× (z -8.8) ⚠ transcription drop; cell-cycle shift, explains ~93% of this change |
| [[HT-29 (line)]] | alt | 9.81 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +16.8) | — |
| [[LoVo (line)]] | wt | 7.14 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.00× (z +15.5) | — |
| [[NCI-H1573 (line)]] | alt | 11.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.28× (z +16.3) | — |
| [[NCI-H1792 (line)]] | alt | 11.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 20.1× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0828× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 3.37 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.8× (z +14.9) | — |
| [[PANC-1 (line)]] | alt | 2.24 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.9× (z +14.7) | — |
| [[A-427 (line)]] | wt | 9.23 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 8.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +11.5) | — |
| [[BT-474 (line)]] | alt | 6.91 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +14.9) | — |
| [[CFPAC-1 (line)]] | alt | 4.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.45× (z +10.1) | — |
| [[HepG2_C3A (line)]] | wt | 4.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.7× (z +13.1) | — |
| [[HOP62 (line)]] | alt | 2.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.0× (z +12.9) | — |
| [[Hs 766T (line)]] | wt | 3.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.68× (z +9.3) | — |
| [[J82 (line)]] | alt | 2.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.5× (z +13.5) | — |
| [[KATO III (line)]] | alt | 4.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +11.3) | — |
| [[LS 180 (line)]] | wt | 5.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.68× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 9.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.29× (z +13.2) | — |
| [[NCI-H23 (line)]] | alt | 7.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 15.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +11.0) | — |
| [[RKO (line)]] | wt | 8.19 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0232× (z -13.1) |
| [[SNU-423 (line)]] | alt | 2.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 3.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.7× (z +12.4) | — |
| [[SW1417 (line)]] | alt | 7.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.984 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.918 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13369), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LGALSL]] | +0.74 | +0.78 / +0.68 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[MARVELD2]] | +0.71 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[PATL2]] | +0.70 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[PLD6]] | +0.70 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[COL28A1]] | +0.69 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[FAM169A]] | +0.69 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[OXA1L-DT]] | +0.69 | +0.71 / +0.32 | both halves | 2e-04 | same gene group |
| [[LINC00240]] | +0.69 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[HACD1]] | +0.68 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[FAM200B]] | +0.68 | +0.73 / +0.41 | both halves | 4e-05 |  |
| [[STAP2]] | +0.68 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[SBF2-AS1]] | +0.68 | +0.65 / +0.39 | both halves | 5e-05 |  |
| [[ZC3H7B]] | +0.67 | +0.66 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KATNB1]] | -0.65 | -0.66 / -0.38 | both halves | 7e-05 |  |
| [[GTF2E2]] | -0.63 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[CTNNBL1]] | -0.63 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[SHQ1]] | -0.63 | -0.61 / -0.36 | both halves | 1e-04 |  |
| [[GRB2]] | -0.61 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[RTTN]] | -0.61 | -0.62 / -0.29 | both halves | 2e-04 |  |
| [[ST6GALNAC4]] | -0.60 | -0.61 / -0.25 | both halves | 4e-04 |  |
| [[RPA1]] | -0.60 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[IGSF8]] | -0.60 | -0.56 / -0.26 | both halves | 4e-04 |  |
| [[STRAP]] | -0.60 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[LPCAT4]] | -0.60 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[TUFM]] | -0.60 | -0.52 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLCD4-RWDD3]] | B | TLCD4-RWDD3 activity raises LGALSL-DT's level | lines that do not express TLCD4-RWDD3 (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without TLCD4-RWDD3 | 0.025 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent |
| [[WIPF3]] | B | WIPF3 activity raises LGALSL-DT's level | lines that do not express WIPF3 (21) vs lines expressing it (29) | 1.46× lower at baseline in the lines without WIPF3 | 0.044 | ⚠ within organs, on part of the lines; also absent: RBM11, EPB41L4A, COL4A3 |
| [[MTUS1-DT]] | B | MTUS1-DT activity raises LGALSL-DT's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 1.99× lower at baseline in the lines without MTUS1-DT | 0.056 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[HDAC6]] | B | HDAC6 activity raises LGALSL-DT's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ADAL]] | C | ADAL activity weakens LGALSL-DT's drug response | lines that do not express ADAL (3) vs lines expressing it (40) | the lines without ADAL respond 1.74× as strongly (z diff -2.47); strongest at Panobinostat 0.5 µM: 0.06x vs 0.38x (z diff -6.3) | 0.010 | ⚠ few lines (3 vs 47); across organs; co-occurs with EP300, RNF43, MSH6; also absent: SPAG4, PDE4A, ZNF532; target measured in part of the lines; artifact flags |
| [[PLEKHG3]] | C | PLEKHG3 activity raises LGALSL-DT's level | lines that do not express PLEKHG3 (5) vs lines expressing it (45) | 3.03× lower at baseline in the lines without PLEKHG3 | 0.011 | ⚠ across organs; also absent: ATP11A, SHC2, PPP1R26; maybe low, not absent; co-absent with the target |
| [[ADAL]] | C | ADAL activity lowers LGALSL-DT's level | lines that do not express ADAL (3) vs lines expressing it (47) | 2.74× higher at baseline in the lines without ADAL | 0.045 | ⚠ few lines (3 vs 47); across organs; co-occurs with EP300, RNF43, MSH6; also absent: SPAG4, PDE4A, ZNF532 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHG3]] | C | LGALSL-DT activity raises PLEKHG3's level | lines that do not express LGALSL-DT (4) vs lines expressing it (46) | 4.60× lower at baseline in the lines without LGALSL-DT | 0.004 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: PLEKHG3, PPP1R26, IMPA2; maybe low, not absent; co-absent with the target |
| [[SLC12A7]] | C | LGALSL-DT activity raises SLC12A7's level | lines that do not express LGALSL-DT (4) vs lines expressing it (46) | 3.80× lower at baseline in the lines without LGALSL-DT | 0.018 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: PLEKHG3, PPP1R26, IMPA2; maybe low, not absent |
| [[MTARC2]] | C | LGALSL-DT activity raises MTARC2's level | lines that do not express LGALSL-DT (4) vs lines expressing it (46) | 3.10× lower at baseline in the lines without LGALSL-DT | 0.087 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: PLEKHG3, PPP1R26, IMPA2; maybe low, not absent |
| cells under [[Vinblastine (sulfate) (drug)]] 0.05 µM | C | [[ATP11A]], [[LGALSL]], LGALSL-DT activity raises the cells' numbers under Vinblastine (sulfate) 0.05 µM (protects the cells) | lines that do not express ATP11A, LGALSL, LGALSL-DT (4) vs lines expressing them (44) | the lines without ATP11A, LGALSL, LGALSL-DT: 0.81× the cells of the other lines | 0.088 | ⚠ few lines (4 vs 46); across organs; also absent: PLEKHG3, PPP1R26, IMPA2; maybe low, not absent; co-absent genes |
| [[ANKRD18A]] | C | LGALSL-DT activity raises ANKRD18A's level | lines that do not express LGALSL-DT (4) vs lines expressing it (46) | 3.55× lower at baseline in the lines without LGALSL-DT | 0.098 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: PLEKHG3, PPP1R26, IMPA2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.820). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (17.3, 10.9); signed map (18.8, -15.7). **Vector** length 96.0, 20.3% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.0 | +40.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.7 | +18.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.6 | +18.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +6.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +4.6 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.4 | -11.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.3 | -9.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.2 | -12.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -7.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.2 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | LGALSL divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p14 — chr2:64,395,220-64,453,967 (-) |
| Ensembl biotype | lncRNA |
| Also known as | LOC105374771 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53951](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53951) · Entrez [105374771](https://www.ncbi.nlm.nih.gov/gene/105374771) · Ensembl [ENSG00000223935](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223935)

## Data

Gene col 13369: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13369); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13369, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13369]; `tensor/DDL_lfc|DDL_z.npy` [13369]; `embed/gene_vectors.npy` [13369]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13369 or target_col == 13369). Every well: [[LGALSL-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LGALSL-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
