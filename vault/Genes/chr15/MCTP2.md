---
symbol: "MCTP2"
type: "gene"
col: 6432
ensembl_id: "ENSG00000140563"
name: "multiple C2 and transmembrane domain containing 2"
location: "15q26.2"
module: 56
arm: "+"
pooled_cpm: 96.39
n_lines_expressing: 30
n_dd_up: 2
n_dd_down: 34
n_dd_up_clean: 2
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 13
direction_downstream: 33
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# MCTP2

*multiple C2 and transmembrane domain containing 2* — 15q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.31× (z +6.5, q 4e-08, up in 19 of 28 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 1 line (HOP62 2.11×).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.320× (z -27.5, q 0e+00, down in 28 of 28 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALNT3]] (+0.67, fdr 1e-05), [[FBXO16]] (+0.62, fdr 2e-05), [[ESRP1]] (+0.59, fdr 2e-05); moves opposite to [[ZMYND11]] (-0.53, fdr 1e-04), [[UBTF]] (-0.52, fdr 1e-04), [[BICRAL]] (-0.50, fdr 2e-04).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 33 go from it, the strongest it → [[LRBA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6432.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 1 line (HOP62 2.11×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +6.5 | 4e-08 | 19/28 (HOP62, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +6.2 | 2e-07 | 19/29 (HOP62, SW1417, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.14× | +3.3 | 0.18 | 3/28 (HT-29, SW 900, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.42× | +3.1 | 0.25 | 10/29 (HOP62, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6432.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.320×** | -27.5 | 0e+00 | 28/28 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.391×** | -22.6 | 0e+00 | 28/29 (A498, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.314×** | -19.0 | 0e+00 | 27/28 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.322×** | -18.6 | 0e+00 | 23/24 (SK-MEL-2, SW48, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.308×** | -18.6 | 0e+00 | 24/25 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.337×** | -18.5 | 0e+00 | 27/29 (RPMI-7951, NCI-H2347, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.380×** | -16.5 | 0e+00 | 26/28 (NCI-H1573, SW480, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.410×** | -15.2 | 0e+00 | 27/28 (KATO III, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.428×** | -14.5 | 1e-45 | 25/28 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.450×** | -13.6 | 3e-40 | 27/28 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.476×** | -12.2 | 3e-32 | 27/28 (A498, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.493×** | -11.6 | 3e-29 | 26/27 (CFPAC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.320×** | -10.2 | 1e-22 | 23/29 (KATO III, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.545×** | -9.9 | 1e-21 | 23/27 (SK-MEL-2, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.597×** | -8.8 | 7e-17 | 23/28 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.601×** | -8.3 | 3e-15 | 24/30 (A498, SW 900, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.729×** | -7.6 | 1e-12 | 23/28 (A498, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.691×** | -6.3 | 1e-08 | 21/28 (A498, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.713×** | -5.7 | 2e-07 | 18/28 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.715×** | -5.7 | 3e-07 | 16/28 (SW 900, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.748×** | -4.9 | 2e-05 | 17/28 (RPMI-7951, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.769×** | -4.5 | 2e-04 | 15/28 (CFPAC-1, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6432. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 550 | 0 | 17 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0939× (z -34.2) |
| [[CFPAC-1 (line)]] | alt | 111 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -23.2) |
| [[NCI-H2347 (line)]] | alt | 375 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -31.9) |
| [[KATO III (line)]] | alt | 141 | 0 | 14 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0781× (z -28.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.188× (z -26.6) |
| [[A498 (line)]] | wt | 117 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -38.8) |
| [[NCI-H2030 (line)]] | alt | 91.2 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -23.4) |
| [[RPMI-7951 (line)]] | alt | 594 | 0 | 13 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -27.7) |
| [[NCI-H1573 (line)]] | alt | 116 | 0 | 12 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.144× (z -20.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.282× (z -18.6) |
| [[SK-MEL-2 (line)]] | alt | 166 | 0 | 11 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0704× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.238× (z -19.5) |
| [[NCI-H1792 (line)]] | alt | 146 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -27.9) |
| [[H4 (line)]] | wt | 278 | 0 | 9 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.130× (z -16.1) |
| [[SW480 (line)]] | alt | 60.8 | 0 | 9 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -19.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.214× (z -17.4) |
| [[HT-29 (line)]] | alt | 199 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -14.9) |
| [[SW48 (line)]] | wt | 134 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0696× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -14.3) |
| [[HOP62 (line)]] | alt | 72.4 | 1 | 6 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.11× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.313× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.481× (z -9.2) |
| [[LoVo (line)]] | wt | 230 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -11.5) |
| [[RKO (line)]] | wt | 66.4 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -22.4) |
| [[HEC-1-A (line)]] | alt | 50.0 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -16.8) |
| [[SW1417 (line)]] | alt | 53.2 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -13.8) |
| [[BT-474 (line)]] | alt | 44.2 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.270× (z -13.0) |
| [[LS 180 (line)]] | wt | 309 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 79.4 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.203× (z -15.9) |
| [[COLO 205 (line)]] | alt | 314 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.427× (z -10.9) |
| [[HCT15 (line)]] | alt | 107 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -14.6) |
| [[HepG2_C3A (line)]] | wt | 55.0 | 0 | 2 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.253× (z -10.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.411× (z -9.8) |
| [[A-427 (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.325× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 40.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -9.3) |
| [[SW 1088 (line)]] | alt | 80.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0430× (z -10.1) |
| [[A-172 (line)]] | wt | 6.92 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.03 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.13 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.10 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.28 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.38 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.40 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.88 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.54 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.04 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.47 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.27 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.23 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.03 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.21 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 8.67 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6432), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNT3]] | +0.67 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[FBXO16]] | +0.62 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ESRP1]] | +0.59 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[CREB3L2]] | +0.57 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[GFPT1]] | +0.55 | +0.62 / +0.37 | both halves | 8e-05 |  |
| [[FKBP14]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[COG6]] | +0.54 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[RASAL1]] | +0.54 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[ZNF511]] | +0.54 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[EAF2]] | +0.54 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[CLINT1]] | +0.53 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[SLC15A2]] | +0.53 | +0.45 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND11]] | -0.53 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[UBTF]] | -0.52 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[BICRAL]] | -0.50 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[HIPK3]] | -0.50 | -0.26 / -0.36 | both halves | 3e-04 |  |
| [[TMEM80]] | -0.49 | -0.52 / -0.23 | both halves | 5e-04 |  |
| [[PLBD1-AS1]] | -0.48 | -0.48 / -0.24 | both halves | 5e-04 |  |
| [[MCPH1-AS1]] | -0.48 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[TRAF3IP2-AS1]] | -0.46 | -0.31 / -0.28 | both halves | 3e-04 |  |
| [[MAD2L1-DT]] | -0.46 | -0.49 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[ITPA]] | -0.46 | -0.46 / -0.26 | both halves | 3e-04 |  |
| [[DPH6-DT]] | -0.46 | -0.50 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[IDNK]] | -0.46 | -0.50 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[ANXA2R-OT1]] | -0.45 | -0.37 / -0.26 | both halves | 4e-04 |  |
| [[MIER3]] | -0.45 | -0.41 / -0.27 | both halves | 3e-04 |  |
| [[ERMAP]] | -0.45 | -0.41 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 3, C 10. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MCTP2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ADAM28]] | B | ADAM28 activity raises MCTP2's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 1.97× lower at baseline in the lines without ADAM28 | 0.088 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[DCLK2]] | B | DCLK2 activity lowers MCTP2's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 2.55× higher at baseline in the lines without DCLK2 | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[GALNT3]] | C | GALNT3 activity raises MCTP2's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 5.54× lower at baseline in the lines without GALNT3 | 8e-04 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1; co-absent with the target |
| [[SNTB1]] | C | SNTB1 activity raises MCTP2's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 5.61× lower at baseline in the lines without SNTB1 | 0.002 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises MCTP2's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.33× lower at baseline in the lines without TMPRSS4 | 0.006 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[TMEM125]] | C | TMEM125 activity raises MCTP2's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 5.08× lower at baseline in the lines without TMEM125 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[FUT3]] | C | FUT3 activity raises MCTP2's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 4.01× lower at baseline in the lines without FUT3 | 0.011 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004; co-absent with the target |
| [[TMEM92]] | C | TMEM92 activity raises MCTP2's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 3.80× lower at baseline in the lines without TMEM92 | 0.012 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises MCTP2's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 5.14× lower at baseline in the lines without ATP2C2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[PRSS8]] | C | PRSS8 activity raises MCTP2's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 3.81× lower at baseline in the lines without PRSS8 | 0.014 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2; co-absent with the target |
| [[LYPD6B]] | C | LYPD6B activity raises MCTP2's level | lines that do not express LYPD6B (23) vs lines expressing it (27) | 3.94× lower at baseline in the lines without LYPD6B | 0.024 | ⚠ within organs, on part of the lines; also absent: GPR35, ATP2C2, EPHB6; co-absent with the target |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 23, C 10. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRBA]] | B | MCTP2 activity raises LRBA's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.67× lower at baseline in the lines without MCTP2 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |
| [[TRAF3IP2-AS1]] | B | MCTP2 activity lowers TRAF3IP2-AS1's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.70× higher at baseline in the lines without MCTP2 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |
| [[SLC15A2]] | B | MCTP2 activity raises SLC15A2's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.73× lower at baseline in the lines without MCTP2 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |
| [[GPR160]] | B | MCTP2 activity raises GPR160's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 2.02× lower at baseline in the lines without MCTP2 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |
| [[EAF2]] | B | MCTP2 activity raises EAF2's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.62× lower at baseline in the lines without MCTP2 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |
| [[PDXDC1]] | B | MCTP2 activity raises PDXDC1's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.56× lower at baseline in the lines without MCTP2 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |
| [[CDS1]] | B | MCTP2 activity raises CDS1's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 2.82× lower at baseline in the lines without MCTP2 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |
| [[RAPGEF5]] | B | MCTP2 activity raises RAPGEF5's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 3.25× lower at baseline in the lines without MCTP2 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |
| [[GFPT1]] | B | MCTP2 activity raises GFPT1's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.69× lower at baseline in the lines without MCTP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |
| [[GFPT1]] | B | MCTP2 activity strengthens GFPT1's drug response | lines that do not express MCTP2 (20) vs lines expressing it (29) | the lines without MCTP2 respond 0.76× as strongly (z diff +1.80); strongest at Digitoxin 5 µM: 0.74x vs 0.49x (z diff +3.6) | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3; target measured in part of the lines; artifact flags |
| [[SEC23A]] | B | MCTP2 activity raises SEC23A's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.21× lower at baseline in the lines without MCTP2 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |
| [[GOLPH3L]] | B | MCTP2 activity raises GOLPH3L's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.58× lower at baseline in the lines without MCTP2 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.533). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.0, -35.3); signed map (-53.4, 12.1). **Vector** length 108, 33.7% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +6.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.7 | +1.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -1.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +3.1 | -4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | -0.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.7 | -0.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.7 | +1.0 |
|  | [[EX229 (drug)]] 0.5 µM |  | +1.7 | -0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.5 | -13.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -12.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.7 | -11.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -2.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | multiple C2 and transmembrane domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.2 — chr15:94,231,538-94,483,952 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11175, FLJ33303 |
| Gene groups (HGNC) | Multiple C2 and transmembrane domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6DN12](https://www.uniprot.org/uniprotkb/Q6DN12) (Multiple C2 and transmembrane domain-containing protein 2):

> Might play a role in the development of cardiac outflow tract.

**Summary**, from NCBI Gene [55784](https://www.ncbi.nlm.nih.gov/gene/55784):

> Enables calcium ion binding activity. Predicted to be involved in regulation of neurotransmitter secretion. Located in cytosol; membrane; and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25636](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25636) · Entrez [55784](https://www.ncbi.nlm.nih.gov/gene/55784) · UniProt [Q6DN12](https://www.uniprot.org/uniprotkb/Q6DN12) · Ensembl [ENSG00000140563](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140563)

## Data

Gene col 6432: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6432); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6432, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6432]; `tensor/DDL_lfc|DDL_z.npy` [6432]; `embed/gene_vectors.npy` [6432]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6432 or target_col == 6432). Every well: [[MCTP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCTP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
