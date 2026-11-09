---
symbol: "AFF1"
type: "gene"
col: 10262
ensembl_id: "ENSG00000172493"
name: "ALF transcription elongation factor 1"
location: "4q21.3-q22.1"
module: 187
arm: "+"
pooled_cpm: 250.34
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 11
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/187"]
generated_by: "tahoemap"
---

# AFF1

*ALF transcription elongation factor 1* — 4q21.3-q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.42× (z +7.3, q 2e-10, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.430× (z -20.2, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[venetoclax (drug)]] 5 µM: 0.594× (z -5.5, q 4e-06, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CASP4]] (+0.50, fdr 3e-05), [[DENND4C]] (+0.50, fdr 5e-05), [[PLEKHA5]] (+0.50, fdr 3e-05); moves opposite to [[MORN1]] (-0.43, fdr 1e-04), [[RNASEH1]] (-0.43, fdr 3e-05), [[QSOX2]] (-0.43, fdr 2e-04).
> It is in [[Module 187]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[STYK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10262.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +7.3 | 2e-10 | 33/48 (PANC-1, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +6.3 | 1e-07 | 32/48 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +5.5 | 6e-06 | 22/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +5.4 | 8e-06 | 28/48 (C32, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +4.5 | 6e-04 | 23/48 (J82, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +4.1 | 0.004 | 20/48 (SW480, SW1417, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.005 | 22/49 (A549, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.9 | 0.007 | 21/48 (LoVo, hTERT-HPNE, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.9 | 0.007 | 22/48 (C32, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.8 | 0.007 | 22/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.15× | +3.3 | 0.046 | 20/49 (SW480, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.1 | 0.10 | 20/48 (NCI-H460, LoVo, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.14× | +3.0 | 0.11 | 15/49 (AN3 CA, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10262.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.430×** | -20.2 | 0e+00 | 45/49 (RKO, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.474×** | -16.5 | 0e+00 | 43/45 (LOX-IMVI, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.523×** | -14.9 | 0e+00 | 40/44 (SK-MEL-2, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.699×** | -8.5 | 2e-15 | 30/48 (A498, LoVo, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.728×** | -7.3 | 3e-11 | 33/47 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.594×** | -5.5 | 4e-06 | 32/48 (AsPC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.799×** | -5.4 | 7e-06 | 26/48 (HT-29, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **0.638×** | -4.7 | 2e-04 | 29/48 (NCI-H2347, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.660×** | -4.4 | 8e-04 | 26/48 (NCI-H2347, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.675×** | -4.1 | 0.002 | 24/48 (NCI-H2347, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | 0.839× | -4.0 | 0.003 | 19/47 (NCI-H1573, HepG2/C3A, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.715×** | -3.5 | 0.021 | 22/48 (A498, LoVo, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10262. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 416 | 0 | 11 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -21.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.483× (z -11.6) |
| [[C32 (line)]] | wt | 172 | 7 (3 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.28× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.465× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 406 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -16.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 462 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -16.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 298 | 3 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -12.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 327 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -18.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 289 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -15.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 540 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -15.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 275 | 3 (2 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.03× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +9.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.489× (z -10.4) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 135 | 2 | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.06× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.531× (z -11.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 214 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.70× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.547× (z -9.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 263 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -16.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 340 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.363× (z -15.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 280 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -18.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 204 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -12.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 287 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -12.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 249 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -10.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 300 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -17.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 354 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0965× (z -31.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 348 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -13.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 260 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -26.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 193 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.479× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 153 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.464× (z -9.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 179 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.478× (z -10.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 534 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -23.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 247 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -13.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 297 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.375× (z -11.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 384 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -10.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 155 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 185 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.476× (z -10.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 188 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -12.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 248 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -15.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 306 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 182 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +10.7) | — |
| [[KATO III (line)]] | alt | 224 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -15.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 82.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H661 (line)]] | alt | 195 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -8.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.482× (z -9.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 176 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.162× (z -8.9) |
| [[SW 900 (line)]] | alt | 250 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -14.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 114 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 349 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 82.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 177 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10262), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASP4]] | +0.50 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[DENND4C]] | +0.50 | +0.55 / +0.39 | both halves | 5e-05 |  |
| [[PLEKHA5]] | +0.50 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[GABARAPL1]] | +0.46 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[MBNL2]] | +0.46 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[RALGPS2]] | +0.46 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[PTGR1]] | +0.45 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[HSPB1]] | +0.45 | +0.35 / +0.45 | both halves | 1e-04 |  |
| [[TLE1]] | +0.45 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[NEDD4L]] | +0.44 | +0.30 / +0.55 | both halves | 2e-04 |  |
| [[SPATA6L]] | +0.44 | +0.30 / +0.43 | both halves | 2e-04 |  |
| [[SCN1A-AS1]] | +0.43 | +0.41 / +0.37 | both halves | 9e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MORN1]] | -0.43 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[RNASEH1]] | -0.43 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[QSOX2]] | -0.43 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[SYNCRIP]] | -0.42 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[MTG1]] | -0.42 | -0.29 / -0.42 | both halves | 3e-04 |  |
| [[SETD4]] | -0.42 | -0.29 / -0.47 | both halves | 3e-04 |  |
| [[VARS1]] | -0.41 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[RNPS1]] | -0.41 | -0.26 / -0.48 | both halves | 3e-04 |  |
| [[NCBP1]] | -0.41 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[NUP188]] | -0.41 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[MRPL3]] | -0.41 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[IPO4]] | -0.40 | -0.37 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STYK1]] | B | STYK1 activity raises AFF1's level | lines that do not express STYK1 (20) vs lines expressing it (30) | 1.64× lower at baseline in the lines without STYK1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, TSTD1 |
| [[LINC02967]] | B | LINC02967 activity raises AFF1's level | lines that do not express LINC02967 (34) vs lines expressing it (16) | 1.61× lower at baseline in the lines without LINC02967 | 0.011 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[SPATA6L]] | B | SPATA6L activity raises AFF1's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 1.49× lower at baseline in the lines without SPATA6L | 0.045 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity lowers AFF1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PDZK1IP1]] | B | PDZK1IP1 activity strengthens AFF1's drug response | lines that do not express PDZK1IP1 (32) vs lines expressing it (17) | the lines without PDZK1IP1 respond 0.82× as strongly (z diff +0.83); strongest at c-Kit-IN-1 0.05 µM: 0.76x vs 0.60x (z diff +3.3) | 0.069 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8; target measured in part of the lines; both ways; artifact flags |
| [[PLSCR4]] | B | PLSCR4 activity raises AFF1's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.55× lower at baseline in the lines without PLSCR4 | 0.083 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[PDZK1IP1]] | B | PDZK1IP1 activity raises AFF1's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 1.47× lower at baseline in the lines without PDZK1IP1 | 0.083 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 187]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.332). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.1, -24.5); signed map (10.9, -4.9). **Vector** length 105, 30.9% of its response variance represented; |z| ≥ 3 in 1,275 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.2 | +5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.8 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.7 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.6 | -8.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.6 | -4.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.4 | -4.4 |
|  | [[EX229 (drug)]] 5 µM |  | -4.0 | -3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.9 | -7.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.8 | -5.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | ALF transcription elongation factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.3-q22.1 — chr4:86,935,002-87,141,039 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AF-4, AF4, FEL; previously PBM1, MLLT2 |
| Gene groups (HGNC) | AF4/FMR2 family; Super elongation complex |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [P51825](https://www.uniprot.org/uniprotkb/P51825) (AF4/FMR2 family member 1):

> Plays an essential role in the activation of transcription elongation from RNA polymerase II promoters, after transcriptional pausing in response to DNA damage. Upon DNA damage, AFF1-mediated transcriptional recovery requires AFF1 poly-ADP-ribosylation by PARP1.

**Summary**, from NCBI Gene [4299](https://www.ncbi.nlm.nih.gov/gene/4299):

> This gene encodes a member of the AF4/ lymphoid nuclear protein related to the Fragile X E syndrome (FRAXE) family of proteins, which have been implicated in human childhood lymphoblastic leukemia, fragile chromosome X intellectual disability, and ataxia. It is the prevalent mixed-lineage leukemia fusion gene associated with spontaneous acute lymphoblastic leukemia. Members of this family have three conserved domains: an N-terminal homology domain, an AF4/ lymphoid nuclear protein domain, and a …

**Accessions** — [HGNC:7135](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7135) · Entrez [4299](https://www.ncbi.nlm.nih.gov/gene/4299) · UniProt [P51825](https://www.uniprot.org/uniprotkb/P51825) · Ensembl [ENSG00000172493](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172493)

## Data

Gene col 10262: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10262); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10262, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10262]; `tensor/DDL_lfc|DDL_z.npy` [10262]; `embed/gene_vectors.npy` [10262]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10262 or target_col == 10262). Every well: [[AFF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AFF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
