---
symbol: "YIPF6"
type: "gene"
col: 11207
ensembl_id: "ENSG00000181704"
name: "Yip1 domain family member 6"
location: "Xq12-q13.1"
module: 42
arm: "+"
pooled_cpm: 62.3
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# YIPF6

*Yip1 domain family member 6* — Xq12-q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.50× (z +11.5, q 5e-28, up in 40 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.33× (z +11.4, q 1e-27, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.771× (z -7.4, q 7e-11, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 0.454×, SW480 0.572×; ⚠ toxic; cell-cycle shift, explains ~27% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (KATO III 0.475×, HT-29 0.507×; ⚠ cell-cycle shift, explains ~34% of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (SW1417 0.394×); [[Sonidegib (drug)]] 5 µM in 1 line (H4 0.110×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SW 1271 0.115×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USO1]] (+0.69, fdr 7e-06), [[COPZ1]] (+0.67, fdr 7e-06), [[ARCN1]] (+0.66, fdr 7e-06); moves opposite to [[SRPK2]] (-0.61, fdr 2e-05), [[TSEN54]] (-0.59, fdr 2e-05), [[MFSD14CP]] (-0.59, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11207.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +11.5 | 5e-28 | 40/49 (HEC-1-A, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +11.4 | 1e-27 | 30/47 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +10.8 | 5e-25 | 0/49 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +9.9 | 4e-21 | 30/42 (A-172, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +9.4 | 6e-19 | 29/45 (LOX-IMVI, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +6.9 | 4e-10 | 29/48 (NCI-H1573, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.39×** | +4.9 | 8e-05 | 23/49 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +4.6 | 3e-04 | 19/48 (LS 180, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.17× | +4.5 | 5e-04 | 20/47 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Hesperidin (drug)]] 0.05 µM |  | 1.17× | +4.1 | 0.003 | 9/48 (NCI-H2030, AsPC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.16× | +3.9 | 0.004 | 19/48 (HOP62, NCI-H1573, …) | top dose only | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.073 | 7/48 (KATO III, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.12× | +3.1 | 0.091 | 10/48 (A-172, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11207.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 0.454×, SW480 0.572×; ⚠ toxic; cell-cycle shift, explains ~27% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (KATO III 0.475×, HT-29 0.507×; ⚠ cell-cycle shift, explains ~34% of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (SW1417 0.394×); [[Sonidegib (drug)]] 5 µM in 1 line (H4 0.110×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SW 1271 0.115×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.771×** | -7.4 | 7e-11 | 32/48 (SW1417, KATO III, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.786×** | -6.8 | 2e-09 | 27/48 (KATO III, HT-29, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.810×** | -6.0 | 4e-07 | 25/48 (KATO III, HT-29, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.824×** | -5.3 | 1e-05 | 23/47 (KATO III, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.830×** | -5.3 | 1e-05 | 21/48 (HT-29, KATO III, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.844× | -4.8 | 1e-04 | 18/48 (KATO III, SNU-1, …) | two highest doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.906× | -4.0 | 0.006 | 6/48 (SNU-423, AsPC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.908× | -3.9 | 0.007 | 10/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.873× | -3.9 | 0.007 | 14/48 (NCI-H460, HS-578T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.876× | -3.8 | 0.010 | 19/48 (KATO III, SW1417, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.881× | -3.5 | 0.025 | 15/48 (Hs 766T, SNU-423, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.792×** | -3.5 | 0.025 | 13/49 (RPMI-7951, KATO III, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | 0.892× | -3.2 | 0.051 | 9/48 (SW 900, AsPC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.888× | -3.2 | 0.055 | 14/47 (SW48, NCI-H2347, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.893× | -3.2 | 0.055 | 7/48 (SK-MEL-2, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11207. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 41.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.20× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.7) | — |
| [[KATO III (line)]] | alt | 102 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.458× (z -9.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H460 (line)]] | wt | 77.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +10.3) | — |
| [[H4 (line)]] | wt | 69.3 | 0 | 1 | — | [[Sonidegib (drug)]] 5 µM 0.110× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 44.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +13.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 90.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.507× (z -9.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[LOX-IMVI (line)]] | wt | 32.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 68.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +9.5) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[NCI-H1573 (line)]] | alt | 88.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 41.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +10.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 57.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.39× (z +9.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 76.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 93.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.8) | — |
| [[SW 1088 (line)]] | alt | 64.4 | 0 | 1 | — | [[Lopinavir (drug)]] 0.05 µM 0.0803× (z -8.8) |
| [[SW 1271 (line)]] | alt | 69.8 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.115× (z -8.9) |
| [[SW1417 (line)]] | alt | 75.8 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.394× (z -12.3) |
| [[SW480 (line)]] | alt | 77.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.572× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 68.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 85.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11207), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USO1]] | +0.69 | +0.61 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[COPZ1]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ARCN1]] | +0.66 | +0.63 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[SEC23B]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[HDLBP]] | +0.60 | +0.45 / +0.72 | both halves | 3e-05 |  |
| [[COPB2]] | +0.58 | +0.60 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[LYSMD3]] | +0.58 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[YME1L1]] | +0.57 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[CLTC]] | +0.56 | +0.50 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 554 |
| [[RABL3]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[SLC30A9]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[SRPRA]] | +0.55 | +0.45 / +0.65 | both halves | 3e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRPK2]] | -0.61 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[TSEN54]] | -0.59 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[MFSD14CP]] | -0.59 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[ANKRD13B]] | -0.56 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[BRF1]] | -0.56 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[TMEM131L]] | -0.55 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[NR2F6]] | -0.55 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[PAQR4]] | -0.55 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[SCAF4]] | -0.55 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[GAS2L1]] | -0.54 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[METAP1]] | -0.54 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[LPCAT4]] | -0.54 | -0.48 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises YIPF6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.322). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.5, -16.8); signed map (13.6, -27.6). **Vector** length 99.5, 22.1% of its response variance represented; |z| ≥ 3 in 912 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +11.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +5.5 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +4.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.8 | +1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.7 | +2.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.1 | -7.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~14% of this change | -3.2 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | -2.7 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.9 | -2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -1.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.6 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | Yip1 domain family member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq12-q13.1 — chrX:68,498,562-68,537,282 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC21416, FinGER6, Yip4, YIPFalpha3 |
| Gene groups (HGNC) | Yip1 domain containing |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 4 pathways, smallest: Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EC8](https://www.uniprot.org/uniprotkb/Q96EC8) (Protein YIPF6):

> May be required for stable YIPF1 and YIPF2 protein expression.

**Summary**, from NCBI Gene [286451](https://www.ncbi.nlm.nih.gov/gene/286451):

> Predicted to enable identical protein binding activity. Predicted to be involved in endoplasmic reticulum to Golgi vesicle-mediated transport. Predicted to act upstream of or within intestinal epithelial cell development. Located in Golgi apparatus and endoplasmic reticulum. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28304](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28304) · Entrez [286451](https://www.ncbi.nlm.nih.gov/gene/286451) · UniProt [Q96EC8](https://www.uniprot.org/uniprotkb/Q96EC8) · Ensembl [ENSG00000181704](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181704)

## Data

Gene col 11207: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11207); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11207, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11207]; `tensor/DDL_lfc|DDL_z.npy` [11207]; `embed/gene_vectors.npy` [11207]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11207 or target_col == 11207). Every well: [[YIPF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YIPF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
