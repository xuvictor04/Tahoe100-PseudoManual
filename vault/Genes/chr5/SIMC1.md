---
symbol: "SIMC1"
type: "gene"
col: 9900
ensembl_id: "ENSG00000170085"
name: "SUMO interacting motifs containing 1"
location: "5q35.2"
module: 36
arm: "+"
pooled_cpm: 47.63
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# SIMC1

*SUMO interacting motifs containing 1* — 5q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.43× (z +6.4, q 7e-08, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.558× (z -14.9, q 0e+00, down in 38 of 46 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.721× (z -8.3, q 7e-15, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKS6]] (+0.74, fdr 7e-06), [[ZNF496]] (+0.72, fdr 7e-06), [[CHCHD6]] (+0.68, fdr 7e-06); moves opposite to [[CGGBP1]] (-0.62, fdr 1e-05), [[SGO1-AS1]] (-0.61, fdr 2e-05), [[PAN2]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[EBF4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9900.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +6.4 | 7e-08 | 28/46 (SW 900, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +5.1 | 1e-04 | 24/45 (SW 900, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.69×** | +5.0 | 1e-04 | 24/46 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.018 | 19/46 (SW 900, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.027 | 15/45 (SNU-423, SW 1271, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.47×** | +3.6 | 0.027 | 14/41 (NCI-H460, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.20× | +3.2 | 0.095 | 11/45 (MIA PaCa-2, A498, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.19× | +3.2 | 0.095 | 9/46 (NCI-H2347, SNU-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.19× | +3.1 | 0.11 | 13/46 (HS-578T, MIA PaCa-2, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9900.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.558×** | -14.9 | 0e+00 | 38/46 (A-172, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.561×** | -10.0 | 3e-21 | 27/37 (A-427, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.590×** | -9.5 | 3e-19 | 28/46 (RKO, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.585×** | -9.3 | 2e-18 | 30/46 (A-172, A498, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.604×** | -9.1 | 1e-17 | 32/45 (NCI-H23, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.721×** | -8.3 | 7e-15 | 30/46 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.619×** | -8.3 | 7e-15 | 31/45 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.637×** | -8.1 | 3e-14 | 31/45 (LoVo, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.616×** | -8.1 | 4e-14 | 32/42 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.651×** | -7.7 | 5e-13 | 36/46 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.446×** | -7.6 | 1e-12 | 33/47 (A-172, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.671×** | -6.9 | 2e-10 | 29/46 (NCI-H23, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.720×** | -5.9 | 1e-07 | 25/46 (A-172, NCI-H460, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.796×** | -4.1 | 0.002 | 19/46 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.808×** | -3.7 | 0.008 | 18/45 (A-427, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.825×** | -3.5 | 0.018 | 18/46 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.822×** | -3.4 | 0.021 | 14/46 (A549, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.884× | -3.1 | 0.046 | 15/46 (A-172, SW 1271, …) | top dose only |  |
| [[Aprepitant (drug)]] 0.05 µM |  | 0.845× | -3.0 | 0.062 | 10/46 (RKO, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9900. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 72.1 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -22.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 65.7 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -14.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 49.5 | 0 | 8 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.279× (z -13.1) ⚠ cell-cycle shift, explains ~50% of this change |
| [[J82 (line)]] | alt | 50.4 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -11.8) |
| [[LoVo (line)]] | wt | 95.6 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -24.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 90.8 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -15.2) |
| [[A498 (line)]] | wt | 38.1 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -18.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H23 (line)]] | alt | 42.7 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -14.4) |
| [[PANC-1 (line)]] | alt | 49.7 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -12.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 65.9 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -11.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-427 (line)]] | wt | 71.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -16.1) |
| [[A549 (line)]] | wt | 40.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -14.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[C32 (line)]] | wt | 37.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.273× (z -10.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 83.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -16.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -9.4) |
| [[SW48 (line)]] | wt | 92.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -8.7) |
| [[SW480 (line)]] | alt | 65.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LS 180 (line)]] | wt | 47.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.253× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1573 (line)]] | alt | 29.1 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -10.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H2030 (line)]] | alt | 33.0 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.281× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 49.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -18.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 68.0 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.292× (z -11.0) ⚠ transcription drop; cell-cycle shift, explains ~93% of this change |
| [[AN3 CA (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -15.4) ⚠ cell-cycle shift, explains ~47% of this change |
| [[C-33 A (line)]] | alt | 98.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.392× (z -8.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 60.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -8.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 55.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HOP62 (line)]] | alt | 40.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -11.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[HS-578T (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.0) ⚠ cell-cycle shift, explains ~47% of this change |
| [[HT-29 (line)]] | alt | 29.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.319× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[hTERT-HPNE (line)]] | wt | 34.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -8.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H2347 (line)]] | alt | 39.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -9.7) |
| [[SHP-77 (line)]] | alt | 70.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -15.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[AsPC-1 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.57 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9900), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKS6]] | +0.74 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[ZNF496]] | +0.72 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[RNF216]] | +0.67 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ADCY3]] | +0.66 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[CMTM8]] | +0.65 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[RRP1B]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[PACC1]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[RANBP17]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[GARNL3]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[PCGF6]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[HERC2P9]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGGBP1]] | -0.62 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | -0.61 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[PAN2]] | -0.55 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[THBS3]] | -0.54 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[TRAPPC6B]] | -0.54 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[SRGAP3]] | -0.54 | -0.57 / -0.21 | both halves | 7e-04 |  |
| [[CCDC159]] | -0.54 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[FBXO8]] | -0.53 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[PRKAR1A]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[TSPAN31]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[TSGA10]] | -0.53 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[HMGN2]] | -0.52 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EBF4]] | B | EBF4 activity raises SIMC1's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.57× lower at baseline in the lines without EBF4 | 0.007 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[HDAC6]] | B | HDAC6 activity lowers SIMC1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MSI1]] | B | MSI1 activity raises SIMC1's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.59× lower at baseline in the lines without MSI1 | 0.080 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[MSI1]] | B | MSI1 activity strengthens SIMC1's drug response | lines that do not express MSI1 (24) vs lines expressing it (22) | the lines without MSI1 respond 0.72× as strongly (z diff +1.70); strongest at Dinaciclib 5 µM: 0.70x vs 0.36x (z diff +4.8) | 0.090 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B; target measured in part of the lines; artifact flags |
| [[FGD1]] | B | FGD1 activity raises SIMC1's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.26× lower at baseline in the lines without FGD1 | 0.093 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[TOP2A]] | B | TOP2A activity raises SIMC1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MCOLN2]] | B | MCOLN2 activity strengthens SIMC1's drug response | lines that do not express MCOLN2 (17) vs lines expressing it (29) | the lines without MCOLN2 respond 0.73× as strongly (z diff +1.46); strongest at Dinaciclib 5 µM: 0.90x vs 0.39x (z diff +5.2) | 0.099 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.673). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-5.7, -31.2); signed map (-15.1, -53.0). **Vector** length 97.7, 25.0% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.9 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +1.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | +4.7 | +3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | +2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.2 | +6.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +5.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +0.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -5.6 | -14.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.5 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.3 | -9.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | +1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.1 | -0.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | SUMO interacting motifs containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:176,238,367-176,345,991 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ44216, OOMA1, PLEIAD; previously C5orf25 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDZ2](https://www.uniprot.org/uniprotkb/Q8NDZ2) (SUMO-interacting motif-containing protein 1):

> Plays a role in SMC5-SMC6 complex recruitment for viral restriction. Forms a complex with SLF2 and this complex is required to recruit SMC5-SMC6 complex to PML nuclear bodies and sites of viral replication.; [Isoform 1]: Inhibits the protease activity of CAPN3.; [Isoform 5]: Inhibits the protease activity of CAPN3.

**Summary**, from NCBI Gene [375484](https://www.ncbi.nlm.nih.gov/gene/375484):

> Enables SUMO polymer binding activity and peptidase inhibitor activity. Located in PML body and sarcomere. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24779](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24779) · Entrez [375484](https://www.ncbi.nlm.nih.gov/gene/375484) · UniProt [Q8NDZ2](https://www.uniprot.org/uniprotkb/Q8NDZ2) · Ensembl [ENSG00000170085](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170085)

## Data

Gene col 9900: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9900); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9900, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9900]; `tensor/DDL_lfc|DDL_z.npy` [9900]; `embed/gene_vectors.npy` [9900]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9900 or target_col == 9900). Every well: [[SIMC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIMC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
