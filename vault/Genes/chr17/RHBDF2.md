---
symbol: "RHBDF2"
type: "gene"
col: 4995
ensembl_id: "ENSG00000129667"
name: "rhomboid 5 homolog 2"
location: "17q25.1"
module: 84
arm: "+"
pooled_cpm: 62.03
n_lines_expressing: 45
n_dd_up: 2
n_dd_down: 39
n_dd_up_clean: 2
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 9
direction_downstream: 5
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# RHBDF2

*rhomboid 5 homolog 2* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Bestatin (hydrochloride) (drug)]] 0.05 µM: 1.26× (z +4.1, q 0.024, up in 15 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HepG2/C3A 2.40×, HT-29 2.49×).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.359× (z -25.4, q 0e+00, down in 37 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH2B2]] (+0.60, fdr 1e-05), [[ARHGAP22]] (+0.59, fdr 1e-05), [[TMEM255B]] (+0.59, fdr 2e-05); moves opposite to [[ADI1]] (-0.56, fdr 2e-04), [[FIGN]] (-0.53, fdr 2e-05), [[NNT]] (-0.52, fdr 1e-04).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CELSR1]] → it (grade B ⚠); 5 go from it, the strongest it → [[CELSR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4995.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HepG2/C3A 2.40×, HT-29 2.49×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.26×** | +4.1 | 0.024 | 15/43 (LoVo, NCI-H2347, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.035 | 15/42 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bicalutamide (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.24 | 9/43 (Panc 03.27, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 18 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4995.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.359×** | -25.4 | 0e+00 | 37/43 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.324×** | -19.0 | 0e+00 | 37/43 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.369×** | -17.5 | 0e+00 | 35/43 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.396×** | -16.2 | 0e+00 | 39/43 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.431×** | -14.7 | 0e+00 | 34/43 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.425×** | -14.4 | 4e-45 | 32/42 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.597×** | -12.7 | 3e-35 | 33/43 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.605×** | -12.4 | 2e-33 | 36/43 (J82, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.504×** | -12.0 | 2e-31 | 35/43 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.517×** | -11.6 | 4e-29 | 38/43 (C32, SNU-423, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.289×** | -11.4 | 3e-28 | 37/44 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.529×** | -11.1 | 4e-27 | 27/41 (NCI-H23, COLO 205, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.518×** | -11.1 | 8e-27 | 32/43 (NCI-H23, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.528×** | -10.8 | 2e-25 | 29/41 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.585×** | -9.4 | 2e-19 | 31/43 (HOP62, H4, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.595×** | -9.1 | 4e-18 | 28/43 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.608×** | -8.7 | 1e-16 | 28/43 (HOP62, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.615×** | -8.5 | 5e-16 | 26/43 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[NG25 (drug)]] 5 µM |  | **0.408×** | -8.2 | 6e-15 | 33/42 (H4, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4995. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 123 | 0 | 29 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0787× (z -28.5) |
| [[HOP62 (line)]] | alt | 197 | 0 | 29 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -19.8) |
| [[RPMI-7951 (line)]] | alt | 71.0 | 0 | 21 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -22.6) |
| [[H4 (line)]] | wt | 130 | 0 | 20 (8 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -16.8) |
| [[NCI-H1792 (line)]] | alt | 110 | 0 | 17 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0678× (z -31.3) |
| [[Panc 03.27 (line)]] | alt | 118 | 0 | 17 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -19.8) |
| [[A-172 (line)]] | wt | 149 | 0 | 16 (8 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.194× (z -17.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.328× (z -17.4) |
| [[J82 (line)]] | alt | 56.5 | 0 | 16 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.120× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.250× (z -16.7) |
| [[CFPAC-1 (line)]] | alt | 94.0 | 0 | 14 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0642× (z -25.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -19.1) |
| [[PANC-1 (line)]] | alt | 70.7 | 0 | 13 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -16.4) |
| [[SNU-423 (line)]] | alt | 130 | 0 | 13 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -17.2) |
| [[HS-578T (line)]] | alt | 47.5 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0826× (z -21.5) |
| [[MIA PaCa-2 (line)]] | alt | 65.4 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -25.0) |
| [[SK-MEL-2 (line)]] | alt | 74.2 | 0 | 10 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0568× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.165× (z -21.0) |
| [[SW480 (line)]] | alt | 66.2 | 0 | 10 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.218× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -17.2) |
| [[LOX-IMVI (line)]] | wt | 47.9 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 34.8 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -14.0) |
| [[COLO 205 (line)]] | alt | 76.0 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.231× (z -16.4) |
| [[NCI-H23 (line)]] | alt | 69.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0565× (z -40.8) |
| [[SW 900 (line)]] | alt | 41.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -13.2) |
| [[A-427 (line)]] | wt | 34.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -16.9) |
| [[A549 (line)]] | wt | 76.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -15.3) |
| [[HepG2_C3A (line)]] | wt | 61.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.323× (z -8.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 46.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -10.3) |
| [[A498 (line)]] | wt | 152 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -9.3) |
| [[HCT15 (line)]] | alt | 66.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -10.2) |
| [[RKO (line)]] | wt | 17.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 29.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.119× (z -8.7) ⚠ toxic |
| [[HT-29 (line)]] | alt | 22.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.3) | — |
| [[KATO III (line)]] | alt | 26.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -9.4) |
| [[LS 180 (line)]] | wt | 24.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[NCI-H1573 (line)]] | alt | 21.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -14.8) |
| [[SW 1088 (line)]] | alt | 103 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -9.2) |
| [[AN3 CA (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 69.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4995), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH2B2]] | +0.60 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[ARHGAP22]] | +0.59 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[TMEM255B]] | +0.59 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[NAV1]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[ZFYVE28]] | +0.58 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[STX1A]] | +0.57 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[MLXIP]] | +0.57 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[GALNT18]] | +0.57 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[SERPINE1]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[PARVB]] | +0.56 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[LOXL2]] | +0.56 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[MYO9B]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 | pathway: Leishmania infection |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADI1]] | -0.56 | -0.56 / -0.32 | both halves | 2e-04 |  |
| [[FIGN]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[NNT]] | -0.52 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[PEG10]] | -0.51 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[DCT]] | -0.51 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[HACD2]] | -0.50 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[CISD2]] | -0.49 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[TSPAN6]] | -0.49 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[RAVER2]] | -0.49 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[CCN3]] | -0.49 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[PLBD1]] | -0.47 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[PON2]] | -0.47 | -0.35 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CELSR1]] | B | CELSR1 activity raises RHBDF2's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 2.12× lower at baseline in the lines without CELSR1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A |
| [[HRH1]] | B | HRH1 activity raises RHBDF2's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 2.11× lower at baseline in the lines without HRH1 | 0.022 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[NAV2]] | B | NAV2 activity strengthens RHBDF2's drug response | lines that do not express NAV2 (16) vs lines expressing it (27) | the lines without NAV2 respond 0.53× as strongly (z diff +3.22); strongest at Idarubicin (hydrochloride) 5 µM: 0.81x vs 0.40x (z diff +5.3) | 0.033 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1; target measured in part of the lines; artifact flags |
| [[GALNT18]] | B | GALNT18 activity raises RHBDF2's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 1.92× lower at baseline in the lines without GALNT18 | 0.060 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[RUNX3]] | B | RUNX3 activity raises RHBDF2's level | lines that do not express RUNX3 (29) vs lines expressing it (21) | 1.68× lower at baseline in the lines without RUNX3 | 0.064 | ⚠ within organs, on part of the lines; also absent: SLC6A15, IGF2BP1, ENSG00000286385 |
| [[FBXO17]] | B | FBXO17 activity raises RHBDF2's level | lines that do not express FBXO17 (18) vs lines expressing it (32) | 2.05× lower at baseline in the lines without FBXO17 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, MRC2, MIR130AHG |
| [[DNAAF9]] | B | DNAAF9 activity raises RHBDF2's level | lines that do not express DNAAF9 (12) vs lines expressing it (38) | 2.04× lower at baseline in the lines without DNAAF9 | 0.089 | ⚠ within organs, on part of the lines; also absent: CHST10, ENSG00000268163, RIMKLB; its own permutation p |
| [[PDGFB]] | B | PDGFB activity raises RHBDF2's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 1.99× lower at baseline in the lines without PDGFB | 0.089 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[NAV1]] | B | NAV1 activity strengthens RHBDF2's drug response | lines that do not express NAV1 (20) vs lines expressing it (23) | the lines without NAV1 respond 0.52× as strongly (z diff +3.23); strongest at Idarubicin (hydrochloride) 5 µM: 0.72x vs 0.39x (z diff +5.1) | 0.095 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CELSR1]] | B | RHBDF2 activity raises CELSR1's level | lines that do not express RHBDF2 (5) vs lines expressing it (45) | 2.38× lower at baseline in the lines without RHBDF2 | 0.018 | ⚠ within organs, on part of the lines; also absent: DBNDD1, PHF11, ARFGEF3; maybe low, not absent |
| [[PDGFB]] | B | RHBDF2 activity raises PDGFB's level | lines that do not express RHBDF2 (5) vs lines expressing it (45) | 3.13× lower at baseline in the lines without RHBDF2 | 0.070 | ⚠ within organs, on part of the lines; also absent: DBNDD1, PHF11, ARFGEF3; maybe low, not absent |
| [[SLCO4A1]] | B | RHBDF2 activity raises SLCO4A1's level | lines that do not express RHBDF2 (5) vs lines expressing it (45) | 2.60× lower at baseline in the lines without RHBDF2 | 0.074 | ⚠ within organs, on part of the lines; also absent: DBNDD1, PHF11, ARFGEF3; maybe low, not absent |
| [[DNAAF9]] | B | RHBDF2 activity raises DNAAF9's level | lines that do not express RHBDF2 (5) vs lines expressing it (45) | 2.28× lower at baseline in the lines without RHBDF2 | 0.083 | ⚠ within organs, on part of the lines; also absent: DBNDD1, PHF11, ARFGEF3; maybe low, not absent |
| [[KCNN4]] | B | RHBDF2 activity raises KCNN4's level | lines that do not express RHBDF2 (5) vs lines expressing it (45) | 2.31× lower at baseline in the lines without RHBDF2 | 0.093 | ⚠ within organs, on part of the lines; also absent: DBNDD1, PHF11, ARFGEF3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.628). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (50.5, 4.3); signed map (1.7, 51.0). **Vector** length 109, 35.9% of its response variance represented; |z| ≥ 3 in 1,523 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +3.7 | -6.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +3.4 | -4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +3.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.0 | -9.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.3 | +3.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.0 | +1.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.9 | +0.1 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.8 | +2.5 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.5 | -12.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.6 | -7.1 |
|  | [[NG25 (drug)]] 5 µM |  | -5.1 | -8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -3.9 | -8.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.9 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -11.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | rhomboid 5 homolog 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:76,470,891-76,501,790 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22341, RHBDL5, TOCG, iRhom2; previously RHBDL6, TOC |
| Gene groups (HGNC) | Rhomboid family |
| Hallmark sets | P53_PATHWAY |
| Reactome | 5 pathways, smallest: CD163 mediating an anti-inflammatory response; Anti-inflammatory response favouring Leishmania parasite infection; Leishmania parasite growth and survival |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PJF5](https://www.uniprot.org/uniprotkb/Q6PJF5) (Inactive rhomboid protein 2):

> Regulates ADAM17 protease, a sheddase of the epidermal growth factor (EGF) receptor ligands and TNF, thereby plays a role in sleep, cell survival, proliferation, migration and inflammation. Does not exhibit any protease activity on its own.

**Summary**, from NCBI Gene [79651](https://www.ncbi.nlm.nih.gov/gene/79651):

> Predicted to enable protein transporter activity. Predicted to be involved in several processes, including hair follicle morphogenesis; negative regulation of protein secretion; and regulation of signal transduction. Predicted to act upstream of or within protein localization to plasma membrane. Located in plasma membrane. Implicated in palmoplantar keratoderma-esophageal carcinoma syndrome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20788](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20788) · Entrez [79651](https://www.ncbi.nlm.nih.gov/gene/79651) · UniProt [Q6PJF5](https://www.uniprot.org/uniprotkb/Q6PJF5) · Ensembl [ENSG00000129667](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129667)

## Data

Gene col 4995: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4995); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4995, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4995]; `tensor/DDL_lfc|DDL_z.npy` [4995]; `embed/gene_vectors.npy` [4995]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4995 or target_col == 4995). Every well: [[RHBDF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHBDF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
