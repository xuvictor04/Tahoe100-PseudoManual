---
symbol: "STAC"
type: "gene"
col: 6916
ensembl_id: "ENSG00000144681"
name: "SH3 and cysteine rich domain"
location: "3p22.3-p22.2"
module: 13
arm: "+"
pooled_cpm: 25.11
n_lines_expressing: 25
n_dd_up: 6
n_dd_down: 24
n_dd_up_clean: 2
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 13
direction_downstream: 35
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# STAC

*SH3 and cysteine rich domain* — 3p22.3-p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.02× (z +12.6, q 1e-33, up in 7 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.44× (z +9.7, q 8e-20, up in 11 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 2 lines (NCI-H460 2.71×, NCI-H2347 2.89×).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.524× (z -17.0, q 0e+00, down in 21 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLYATL2]] (+0.57, fdr 2e-05), [[ARHGAP22]] (+0.54, fdr 6e-05), [[RASSF2]] (+0.50, fdr 3e-05); moves opposite to [[JADE2]] (-0.47, fdr 3e-05), [[ZNF362]] (-0.46, fdr 7e-05), [[STAT5A]] (-0.46, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[ITGB3]] → it (grade C ⚠); 35 go from it, the strongest it → [[CCDC149]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6916.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 2 lines (NCI-H460 2.71×, NCI-H2347 2.89×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +12.6 | 1e-33 | 7/18 (hTERT-HPNE, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +9.7 | 8e-20 | 11/23 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +8.7 | 8e-16 | 7/23 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +6.5 | 1e-08 | 12/23 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +5.5 | 4e-06 | 7/21 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +4.9 | 7e-05 | 4/23 (NCI-H460, H4, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.093 | 2/23 (NCI-H2347, SK-MEL-2) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.19× | +3.2 | 0.099 | 8/22 (A498, HS-578T, …) | rises with dose |  |
| [[Adenosine (drug)]] 5 µM |  | 1.12× | +3.0 | 0.16 | 1/23 (H4) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6916.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.524×** | -17.0 | 0e+00 | 21/23 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.503×** | -12.3 | 3e-32 | 20/23 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.580×** | -8.6 | 1e-15 | 16/23 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.666×** | -7.6 | 6e-12 | 14/23 (HEC-1-A, NCI-H1792, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.679×** | -7.2 | 6e-11 | 13/23 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.713×** | -6.3 | 3e-08 | 10/23 (RPMI-7951, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -6.2 | 6e-08 | 16/23 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.728×** | -5.9 | 2e-07 | 15/23 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.547×** | -5.9 | 3e-07 | 19/23 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.738×** | -5.7 | 9e-07 | 14/23 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.741×** | -5.6 | 1e-06 | 18/23 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.815×** | -5.4 | 3e-06 | 19/23 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.783×** | -4.5 | 2e-04 | 11/22 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.770×** | -4.5 | 3e-04 | 3/23 (HEC-1-A, A549, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.789×** | -4.4 | 4e-04 | 11/23 (HOP62, H4, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.757×** | -4.4 | 4e-04 | 15/23 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.643×** | -4.3 | 6e-04 | 7/23 (HEC-1-A, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.820×** | -3.7 | 0.006 | 17/23 (HEC-1-A, SW 1271, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6916. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 118 | 0 | 18 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -33.3) |
| [[HOP62 (line)]] | alt | 39.8 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -19.7) |
| [[A-172 (line)]] | wt | 35.3 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -24.8) |
| [[CFPAC-1 (line)]] | alt | 41.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -19.9) |
| [[NCI-H1792 (line)]] | alt | 186 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -31.6) |
| [[HS-578T (line)]] | alt | 83.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -19.3) |
| [[RPMI-7951 (line)]] | alt | 49.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 12.7 | 1 | 4 | [[Tucidinostat (drug)]] 5 µM 2.71× (z +9.9) | [[Digitoxin (drug)]] 0.05 µM 0.224× (z -10.4) |
| [[PANC-1 (line)]] | alt | 34.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -19.8) |
| [[A498 (line)]] | wt | 51.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -19.0) |
| [[NCI-H2030 (line)]] | alt | 54.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -15.2) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.393× (z -11.4) |
| [[SNU-423 (line)]] | alt | 56.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -15.7) |
| [[A549 (line)]] | wt | 15.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -13.2) |
| [[CHP-212 (line)]] | wt | 78.9 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0841× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.279× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0748× (z -13.2) ⚠ toxic; cell-cycle shift, explains ~23% of this change |
| [[SW 1088 (line)]] | alt | 71.1 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0468× (z -9.2) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.134× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 37.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 15.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.89× (z +9.7) | — |
| [[SW 1271 (line)]] | alt | 79.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.107× (z -8.6) |
| [[SW 900 (line)]] | alt | 12.9 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.148× (z -8.9) |
| [[A-427 (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.73 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6916), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLYATL2]] | +0.57 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[ARHGAP22]] | +0.54 | +0.59 / +0.39 | both halves | 6e-05 |  |
| [[RASSF2]] | +0.50 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[IQCA1]] | +0.50 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[TBX20]] | +0.50 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[DNAAF9]] | +0.49 | +0.60 / +0.24 | both halves | 5e-04 |  |
| [[CA12]] | +0.49 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[VSTM4]] | +0.49 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[CHST9]] | +0.48 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[SPANXA2-OT1]] | +0.47 | +0.49 / +0.33 | both halves | 1e-04 |  |
| [[CLDN14-AS1]] | +0.47 | +0.52 / +0.36 | both halves | 9e-05 |  |
| [[AGTR1]] | +0.47 | +0.44 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JADE2]] | -0.47 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ZNF362]] | -0.46 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[STAT5A]] | -0.46 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[ABO]] | -0.45 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[TFAP2A-AS1]] | -0.45 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[SECTM1]] | -0.43 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[UFL1-AS1]] | -0.43 | -0.47 / -0.22 | both halves | 6e-04 |  |
| [[GLDN]] | -0.42 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[MIR4713HG]] | -0.42 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[TGIF1]] | -0.42 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[BAMBI]] | -0.41 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[PAXIP1-DT]] | -0.41 | -0.44 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB3]] | C | ITGB3 activity raises STAC's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 5.58× lower at baseline in the lines without ITGB3 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130; co-absent with the target |
| [[ARHGAP22]] | C | ARHGAP22 activity raises STAC's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 6.96× lower at baseline in the lines without ARHGAP22 | 0.019 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2; co-absent with the target |
| [[PTGFR]] | C | PTGFR activity raises STAC's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 5.15× lower at baseline in the lines without PTGFR | 0.022 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX; co-absent with the target |
| [[C12orf75-AS1]] | C | C12orf75-AS1 activity raises STAC's level | lines that do not express C12orf75-AS1 (22) vs lines expressing it (28) | 3.46× lower at baseline in the lines without C12orf75-AS1 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1; co-absent with the target |
| [[KIRREL3]] | C | KIRREL3 activity raises STAC's level | lines that do not express KIRREL3 (36) vs lines expressing it (14) | 5.48× lower at baseline in the lines without KIRREL3 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN; co-absent with the target |
| [[LRAT]] | C | LRAT activity raises STAC's level | lines that do not express LRAT (30) vs lines expressing it (20) | 4.93× lower at baseline in the lines without LRAT | 0.040 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, NR0B1, IL6; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises STAC's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 4.56× lower at baseline in the lines without INSYN2B | 0.066 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises STAC's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 6.68× lower at baseline in the lines without LINC01411 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[CLDN14-AS1]] | C | CLDN14-AS1 activity raises STAC's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 3.91× lower at baseline in the lines without CLDN14-AS1 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158; co-absent with the target |
| [[UBE2Q2P13]] | C | UBE2Q2P13 activity raises STAC's level | lines that do not express UBE2Q2P13 (23) vs lines expressing it (27) | 3.83× lower at baseline in the lines without UBE2Q2P13 | 0.080 | ⚠ within organs, on part of the lines; also absent: ZFP82, CACNA2D1, BASP1-AS1; co-absent with the target |
| [[DKK3]] | C | DKK3 activity raises STAC's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 5.54× lower at baseline in the lines without DKK3 | 0.082 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; co-absent with the target |
| [[ADAM12]] | C | ADAM12 activity raises STAC's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 5.42× lower at baseline in the lines without ADAM12 | 0.083 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 19, C 16. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC149]] | B | STAC activity raises CCDC149's level | lines that do not express STAC (25) vs lines expressing it (25) | 2.24× lower at baseline in the lines without STAC | 0.011 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[LRRFIP1]] | B | STAC activity raises LRRFIP1's level | lines that do not express STAC (25) vs lines expressing it (25) | 1.49× lower at baseline in the lines without STAC | 0.011 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[ZNF215]] | B | STAC activity raises ZNF215's level | lines that do not express STAC (25) vs lines expressing it (25) | 1.33× lower at baseline in the lines without STAC | 0.013 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[SLC25A51]] | B | STAC activity raises SLC25A51's level | lines that do not express STAC (25) vs lines expressing it (25) | 1.75× lower at baseline in the lines without STAC | 0.016 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[LINC00887]] | B | STAC activity raises LINC00887's level | lines that do not express STAC (25) vs lines expressing it (25) | 2.02× lower at baseline in the lines without STAC | 0.037 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[NHS]] | B | STAC activity raises NHS's level | lines that do not express STAC (25) vs lines expressing it (25) | 3.73× lower at baseline in the lines without STAC | 0.043 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[EFL1]] | B | STAC activity raises EFL1's level | lines that do not express STAC (25) vs lines expressing it (25) | 1.22× lower at baseline in the lines without STAC | 0.051 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| cells under [[Cobimetinib (drug)]] 5 µM | B | STAC activity lowers the cells' numbers under Cobimetinib 5 µM (makes them more sensitive) | lines that do not express STAC (25) vs lines expressing it (23) | the lines without STAC: 1.21× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[MARK2]] | B | STAC activity lowers MARK2's level | lines that do not express STAC (25) vs lines expressing it (25) | 1.41× higher at baseline in the lines without STAC | 0.063 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[ZNF362]] | B | STAC activity weakens ZNF362's drug response | lines that do not express STAC (24) vs lines expressing it (21) | the lines without STAC respond 1.39× as strongly (z diff -1.54); strongest at Digitoxin 5 µM: 0.22x vs 0.35x (z diff -2.3) | 0.063 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11; target measured in part of the lines; artifact flags |
| cells under [[Cobimetinib (drug)]] 0.5 µM | B | STAC activity lowers the cells' numbers under Cobimetinib 0.5 µM (makes them more sensitive) | lines that do not express STAC (25) vs lines expressing it (23) | the lines without STAC: 1.27× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[ATAD2B]] | B | STAC activity lowers ATAD2B's level | lines that do not express STAC (25) vs lines expressing it (25) | 1.19× higher at baseline in the lines without STAC | 0.079 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.419). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.1, 11.1); signed map (15.3, 49.9). **Vector** length 78.3, 22.9% of its response variance represented; |z| ≥ 3 in 684 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.1 | -12.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -4.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | -1.8 | -3.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.8 | -4.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.4 | -2.7 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.2 | -0.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | SH3 and cysteine rich domain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.3-p22.2 — chr3:36,380,503-36,548,007 (+) |
| Ensembl biotype | protein_coding |
| Also known as | STAC1 |
| Gene groups (HGNC) | SH3 and cysteine rich domain family; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99469](https://www.uniprot.org/uniprotkb/Q99469) (SH3 and cysteine-rich domain-containing protein):

> Promotes expression of the ion channel CACNA1H at the cell membrane, and thereby contributes to the regulation of channel activity. Plays a minor and redundant role in promoting the expression of calcium channel CACNA1S at the cell membrane, and thereby contributes to increased channel activity. Slows down the inactivation rate of the calcium channel CACNA1C.

**Summary**, from NCBI Gene [6769](https://www.ncbi.nlm.nih.gov/gene/6769):

> Predicted to enable transmembrane transporter binding activity. Predicted to be involved in positive regulation of protein localization to plasma membrane; positive regulation of voltage-gated calcium channel activity; and skeletal muscle contraction. Predicted to act upstream of or within cellular response to heat; muscle contraction; and regulation of voltage-gated calcium channel activity. Predicted to be located in cytoplasmic side of plasma membrane. [provided by Alliance of Genome …

**Accessions** — [HGNC:11353](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11353) · Entrez [6769](https://www.ncbi.nlm.nih.gov/gene/6769) · UniProt [Q99469](https://www.uniprot.org/uniprotkb/Q99469) · Ensembl [ENSG00000144681](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144681)

## Data

Gene col 6916: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6916); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6916, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6916]; `tensor/DDL_lfc|DDL_z.npy` [6916]; `embed/gene_vectors.npy` [6916]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6916 or target_col == 6916). Every well: [[STAC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
