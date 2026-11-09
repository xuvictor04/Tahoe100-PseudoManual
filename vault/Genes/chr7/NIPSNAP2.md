---
symbol: "NIPSNAP2"
type: "gene"
col: 7116
ensembl_id: "ENSG00000146729"
name: "nipsnap homolog 2"
location: "7p11.2"
module: 17
arm: "+"
pooled_cpm: 123.48
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# NIPSNAP2

*nipsnap homolog 2* — 7p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.60× (z +8.1, q 4e-13, up in 39 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (MIA PaCa-2 2.51×, LoVo 2.54×, HEC-1-A 2.32×, LS 180 2.60×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 2.19×, MIA PaCa-2 2.24×, LS 180 2.38×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.505× (z -16.5, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAPPC11]] (+0.73, fdr 7e-06), [[THOC1]] (+0.67, fdr 7e-06), [[ESD]] (+0.66, fdr 7e-06); moves opposite to [[DNAJB6]] (-0.62, fdr 1e-05), [[DDX5]] (-0.60, fdr 1e-05), [[SFXN5]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GABRE]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7116.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (MIA PaCa-2 2.51×, LoVo 2.54×, HEC-1-A 2.32×, LS 180 2.60×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 2.19×, MIA PaCa-2 2.24×, LS 180 2.38×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +8.1 | 4e-13 | 39/49 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +7.4 | 3e-11 | 32/44 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.25×** | +3.5 | 0.091 | 22/45 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7116.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.505×** | -16.5 | 0e+00 | 44/49 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.584×** | -13.0 | 7e-36 | 41/48 (HOP62, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.616×** | -8.3 | 3e-14 | 40/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -7.7 | 2e-12 | 36/48 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.659×** | -7.1 | 1e-10 | 41/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.698×** | -6.1 | 8e-08 | 35/48 (A-172, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.707×** | -5.9 | 3e-07 | 36/48 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.723×** | -5.5 | 2e-06 | 38/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.729×** | -5.4 | 5e-06 | 34/48 (KATO III, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.710×** | -5.3 | 8e-06 | 34/48 (SW480, KATO III, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.729×** | -4.9 | 6e-05 | 37/47 (C32, SW1417, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.758×** | -4.7 | 1e-04 | 26/48 (SHP-77, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.759×** | -4.7 | 1e-04 | 31/48 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.776×** | -4.3 | 7e-04 | 28/48 (SHP-77, KATO III, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.636×** | -4.0 | 0.002 | 31/48 (A-427, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.790×** | -4.0 | 0.002 | 30/48 (SHP-77, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.650×** | -3.8 | 0.004 | 29/49 (A-172, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.803×** | -3.6 | 0.010 | 27/48 (COLO 205, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7116. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 295 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -15.9) |
| [[SW480 (line)]] | alt | 216 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -18.7) |
| [[A-172 (line)]] | wt | 120 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -18.5) |
| [[MIA PaCa-2 (line)]] | alt | 195 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +11.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -21.7) |
| [[C32 (line)]] | wt | 98.7 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -15.4) |
| [[HOP62 (line)]] | alt | 102 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -17.5) |
| [[H4 (line)]] | wt | 166 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -17.9) |
| [[HEC-1-A (line)]] | alt | 135 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +11.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.625× (z -8.5) |
| [[HS-578T (line)]] | alt | 101 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -12.6) |
| [[KATO III (line)]] | alt | 193 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +9.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -13.8) |
| [[LoVo (line)]] | wt | 130 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +11.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -17.2) |
| [[LS 180 (line)]] | wt | 93.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +10.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 47.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 124 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -11.5) |
| [[SNU-423 (line)]] | alt | 115 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -15.1) |
| [[CFPAC-1 (line)]] | alt | 87.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -14.6) |
| [[COLO 205 (line)]] | alt | 138 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -10.5) |
| [[J82 (line)]] | alt | 86.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -14.1) |
| [[LOX-IMVI (line)]] | wt | 86.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -13.7) |
| [[PANC-1 (line)]] | alt | 189 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -15.8) |
| [[SK-MEL-2 (line)]] | alt | 112 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -16.6) |
| [[SW 900 (line)]] | alt | 107 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -13.0) |
| [[SW1417 (line)]] | alt | 111 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -11.3) |
| [[A-427 (line)]] | wt | 168 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -11.4) |
| [[A498 (line)]] | wt | 112 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.579× (z -10.0) |
| [[A549 (line)]] | wt | 127 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -9.4) |
| [[HCT15 (line)]] | alt | 96.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -10.7) |
| [[Hs 766T (line)]] | wt | 122 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 61.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 112 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 85.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 142 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 84.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.566× (z -10.4) |
| [[RKO (line)]] | wt | 115 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -13.3) |
| [[SNU-1 (line)]] | wt | 94.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -12.2) |
| [[SW 1088 (line)]] | alt | 164 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -9.1) |
| [[SW48 (line)]] | wt | 194 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -10.3) |
| [[AN3 CA (line)]] | alt | 170 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 137 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 74.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 93.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7116), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC11]] | +0.73 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[THOC1]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ESD]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[MRPS31P4]] | +0.66 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[RAD17]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ZYG11B]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ABITRAM]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[UBXN2B]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[ACTR10]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ARMC1]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[MTCH2]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[GEMIN2]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB6]] | -0.62 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[DDX5]] | -0.60 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[SFXN5]] | -0.57 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[MC1R]] | -0.57 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[PLEKHA6]] | -0.56 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[UBE2R2-AS1]] | -0.55 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[FSCN2]] | -0.55 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[DNAH1]] | -0.55 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[SLC9A5]] | -0.54 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[CACNG8]] | -0.53 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[IL18BP]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[SRSF5]] | -0.51 | -0.47 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABRE]] | B | GABRE activity lowers NIPSNAP2's level | lines that do not express GABRE (20) vs lines expressing it (30) | 1.35× higher at baseline in the lines without GABRE | 0.062 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.656). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.6, -2.3); signed map (-21.9, -14.3). **Vector** length 96.6, 29.6% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.8 | +2.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.3 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +2.4 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | +2.6 | +2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.2 | +1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.3 | -6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -16.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -7.7 |
|  | [[crizotinib (drug)]] 5 µM |  | -2.8 | -2.7 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | nipsnap homolog 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p11.2 — chr7:55,951,793-56,000,181 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GBAS |
| Reactome | 5 pathways, smallest: RHOH GTPase cycle; RHOJ GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O75323](https://www.uniprot.org/uniprotkb/O75323) (Protein NipSnap homolog 2):

> Protein involved in mitophagy by facilitating recruitment of the autophagy machinery required for clearance of damaged mitochondria. Accumulates on the mitochondria surface in response to mitochondrial depolarization and acts as a 'eat me' signal by recruiting proteins involved in selective autophagy, such as autophagy receptors (CALCOCO2/NDP52, NBR1, SQSTM1/p62, TAX1BP1 and WDFY3/ALFY) and ATG8 family proteins (MAP1LC3A, MAP1LC3B, MAP1LC3C, GABARAP, GABARAPL1 and GABARAPL2).

**Summary**, from NCBI Gene [2631](https://www.ncbi.nlm.nih.gov/gene/2631):

> This gene encodes a member of the NipSnap family of proteins that may be involved in vesicular transport. The encoded protein is localized to mitochondria and plays a role in oxidative phosphorylation. A pseudogene of this gene is located on the long arm of chromosome 2. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:4179](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4179) · Entrez [2631](https://www.ncbi.nlm.nih.gov/gene/2631) · UniProt [O75323](https://www.uniprot.org/uniprotkb/O75323) · Ensembl [ENSG00000146729](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146729)

## Data

Gene col 7116: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7116); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7116, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7116]; `tensor/DDL_lfc|DDL_z.npy` [7116]; `embed/gene_vectors.npy` [7116]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7116 or target_col == 7116). Every well: [[NIPSNAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIPSNAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
