---
symbol: "TRPV1"
type: "gene"
col: 12266
ensembl_id: "ENSG00000196689"
name: "transient receptor potential cation channel subfamily V member 1"
location: "17p13.2"
module: 38
arm: "+"
pooled_cpm: 14.67
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# TRPV1

*transient receptor potential cation channel subfamily V member 1* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.27× (z +19.2, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.420× (z -10.0, q 1e-20, down in 37 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.281× (z -7.6, q 4e-12, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHPK]] (+0.81, fdr 7e-06, ⚠ same locus), [[QRICH2]] (+0.74, fdr 7e-06), [[UBAP1L]] (+0.67, fdr 7e-06), [[ANKMY1]] (+0.65, fdr 1e-05); moves opposite to [[COMMD8]] (-0.61, fdr 5e-04), [[DLD]] (-0.61, fdr 2e-05), [[IRAK1BP1]] (-0.61, fdr 8e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12266.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.27×** | +19.2 | 0e+00 | 44/45 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.48×** | +10.1 | 3e-21 | 38/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.02×** | +8.1 | 1e-13 | 40/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +6.3 | 5e-08 | 27/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.58×** | +5.2 | 2e-05 | 28/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +4.5 | 7e-04 | 19/47 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.47×** | +4.5 | 7e-04 | 25/47 (BT-474, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.3 | 0.001 | 19/48 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.083 | 11/47 (A-427, RKO, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.30× | +3.0 | 0.13 | 10/47 (PANC-1, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12266.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.420×** | -10.0 | 1e-20 | 37/46 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.417×** | -9.6 | 1e-19 | 37/46 (A-427, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.431×** | -9.6 | 1e-19 | 34/48 (HOP62, SW480, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.281×** | -7.6 | 4e-12 | 40/48 (HOP62, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.540×** | -7.1 | 2e-10 | 29/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.315×** | -6.9 | 4e-10 | 29/44 (HOP62, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.592×** | -5.8 | 6e-07 | 23/43 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.631×** | -5.3 | 9e-06 | 24/47 (LOX-IMVI, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.656×** | -4.8 | 8e-05 | 24/47 (H4, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.663×** | -4.7 | 1e-04 | 27/47 (PANC-1, CFPAC-1, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.690×** | -4.1 | 0.002 | 18/27 (MIA PaCa-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.708×** | -3.9 | 0.004 | 24/47 (PANC-1, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.571×** | -3.4 | 0.034 | 14/44 (C32, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.739×** | -3.2 | 0.056 | 18/45 (A-172, SW48, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12266. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 21.8 | 3 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +13.9) | [[Harringtonine (drug)]] 0.5 µM 0.234× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 12.8 | 2 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.47× (z +16.2) | [[Digitoxin (drug)]] 5 µM 0.135× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.248× (z -9.5) |
| [[A549 (line)]] | wt | 18.8 | 2 | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 9.83× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.0982× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.182× (z -8.9) |
| [[HOP62 (line)]] | alt | 17.4 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.167× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0594× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 21.3 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.159× (z -11.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 10.1 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.218× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 16.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +9.6) | [[Harringtonine (drug)]] 0.05 µM 0.181× (z -9.2) |
| [[A498 (line)]] | wt | 15.9 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 8.99× (z +12.0) | — |
| [[C32 (line)]] | wt | 7.66 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.23× (z +10.0) | [[Ligustrazine (drug)]] 5 µM 0.0963× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 21.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.131× (z -8.5) |
| [[KATO III (line)]] | alt | 13.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +10.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.192× (z -8.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 15.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +15.2) | — |
| [[LS 180 (line)]] | wt | 9.52 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.25× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 11.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +9.2) | [[Harringtonine (drug)]] 0.5 µM 0.178× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 15.4 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.130× (z -11.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[RKO (line)]] | wt | 10.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +9.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.132× (z -8.8) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 6.86 | 0 | 2 | — | [[Bentamapimod (drug)]] 0.05 µM 0.0704× (z -9.2) |
| [[A-427 (line)]] | wt | 12.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0776× (z -13.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0919× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 37.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HEC-1-A (line)]] | alt | 22.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 6.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.43× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -10.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM 0.0676× (z -9.4) |
| [[J82 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[NCI-H1573 (line)]] | alt | 8.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 11.2 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0952× (z -9.7) |
| [[SW1417 (line)]] | alt | 9.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +8.6) | — |
| [[SW48 (line)]] | wt | 19.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12266), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHPK]] | +0.81 | +0.75 / +0.86 | both halves | 7e-06 | STRING 549; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[QRICH2]] | +0.74 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[UBAP1L]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[ANKMY1]] | +0.65 | +0.53 / +0.65 | both halves | 1e-05 | same gene group |
| [[PRPSAP1]] | +0.65 | +0.49 / +0.73 | both halves | 1e-05 |  |
| [[SYCE2]] | +0.64 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[VWCE]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[TTLL3]] | +0.63 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[PPIEL-1]] | +0.63 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.63 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[SLC23A3]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[SLC22A20P]] | +0.63 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[RABGEF1]] | +0.63 | +0.37 / +0.71 | both halves | 8e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD8]] | -0.61 | -0.24 / -0.64 | both halves | 5e-04 |  |
| [[DLD]] | -0.61 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[IRAK1BP1]] | -0.61 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[ESD]] | -0.58 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[PEX2]] | -0.58 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[UBXN2B]] | -0.57 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[NUDT12]] | -0.55 | -0.27 / -0.57 | both halves | 3e-04 | same gene group |
| [[METTL5]] | -0.55 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[LYPLAL1]] | -0.55 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[WDR17]] | -0.55 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[TMEM218]] | -0.55 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[GCOM1]] | -0.55 | -0.45 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TRPV1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers TRPV1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers TRPV1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.6, -15.5); signed map (14.6, 3.0). **Vector** length 77.0, 15.7% of its response variance represented; |z| ≥ 3 in 1,236 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +19.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +10.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +4.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.4 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.6 | +2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.6 | +3.0 |
|  | [[Lucanthone (drug)]] 5 µM |  | +1.5 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -1.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.6 | -9.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -7.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | transient receptor potential cation channel subfamily V member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:3,565,444-3,609,411 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously VR1 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Transient receptor potential cation channel subfamily V |
| Reactome | 4 pathways, smallest: TRP channels; Stimuli-sensing channels; Ion channel transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NER1](https://www.uniprot.org/uniprotkb/Q8NER1) (Transient receptor potential cation channel subfamily V member 1):

> Non-selective calcium permeant cation channel involved in detection of noxious chemical and thermal stimuli. Seems to mediate proton influx and may be involved in intracellular acidosis in nociceptive neurons. Involved in mediation of inflammatory pain and hyperalgesia. Sensitized by a phosphatidylinositol second messenger system activated by receptor tyrosine kinases, which involves PKC isozymes and PCL. Activated by vanilloids, like capsaicin, and temperatures higher than 42 degrees Celsius. …

**Summary**, from NCBI Gene [7442](https://www.ncbi.nlm.nih.gov/gene/7442):

> Capsaicin, the main pungent ingredient in hot chili peppers, elicits a sensation of burning pain by selectively activating sensory neurons that convey information about noxious stimuli to the central nervous system. The protein encoded by this gene is a receptor for capsaicin and is a non-selective cation channel that is structurally related to members of the TRP family of ion channels. This receptor is also activated by increases in temperature in the noxious range, suggesting that it …

**Accessions** — [HGNC:12716](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12716) · Entrez [7442](https://www.ncbi.nlm.nih.gov/gene/7442) · UniProt [Q8NER1](https://www.uniprot.org/uniprotkb/Q8NER1) · Ensembl [ENSG00000196689](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196689)

## Data

Gene col 12266: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12266); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12266, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12266]; `tensor/DDL_lfc|DDL_z.npy` [12266]; `embed/gene_vectors.npy` [12266]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12266 or target_col == 12266). Every well: [[TRPV1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRPV1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
