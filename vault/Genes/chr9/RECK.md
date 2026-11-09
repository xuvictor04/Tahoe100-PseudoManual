---
symbol: "RECK"
type: "gene"
col: 4370
ensembl_id: "ENSG00000122707"
name: "reversion inducing cysteine rich protein with kazal motifs"
location: "9p13.3"
module: 30
arm: "+"
pooled_cpm: 22.36
n_lines_expressing: 38
n_dd_up: 17
n_dd_down: 15
n_dd_up_clean: 14
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 8
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# RECK

*reversion inducing cysteine rich protein with kazal motifs* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.75× (z +14.2, q 3e-43, up in 33 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.381× (z -24.5, q 0e+00, down in 28 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NENF]] (+0.70, fdr 1e-05), [[HEBP1]] (+0.67, fdr 9e-06), [[ECI2]] (+0.65, fdr 1e-05); moves opposite to [[ZC3H4]] (-0.66, fdr 7e-06), [[CYB5D1]] (-0.66, fdr 7e-06), [[INO80D]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[STARD9]] → it (grade C ⚠); 8 go from it, the strongest it → [[SNTA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4370.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.75×** | +14.2 | 3e-43 | 33/36 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.14×** | +13.8 | 1e-40 | 30/36 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.10×** | +13.3 | 3e-38 | 30/36 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +12.1 | 2e-31 | 30/36 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.75×** | +10.1 | 6e-22 | 29/36 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +8.6 | 6e-16 | 24/36 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +8.5 | 2e-15 | 23/34 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.44×** | +8.4 | 3e-15 | 26/36 (PANC-1, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +6.3 | 1e-08 | 20/36 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.20× | +4.6 | 3e-04 | 13/36 (A498, NCI-H23, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.4 | 5e-04 | 13/36 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.28×** | +4.4 | 5e-04 | 8/36 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.27×** | +4.3 | 8e-04 | 13/36 (SNU-423, Hs 766T, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.18× | +4.3 | 8e-04 | 8/36 (SNU-423, Hs 766T, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.54×** | +4.1 | 0.002 | 9/36 (HS-578T, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.006 | 7/36 (Panc 03.27, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.011 | 8/36 (SW1417, SW480, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4370.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.381×** | -24.5 | 0e+00 | 28/36 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.403×** | -15.7 | 0e+00 | 27/36 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.429×** | -15.2 | 0e+00 | 30/35 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.335×** | -10.3 | 1e-22 | 26/36 (H4, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.604×** | -9.1 | 1e-17 | 27/36 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.657×** | -7.3 | 4e-11 | 22/35 (SNU-423, SNU-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.468×** | -7.1 | 8e-11 | 20/36 (C32, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.684×** | -6.8 | 6e-10 | 23/36 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.709×** | -6.2 | 4e-08 | 18/36 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.763×** | -4.9 | 7e-05 | 17/36 (A-172, J82, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.785×** | -4.2 | 0.001 | 14/36 (PANC-1, SNU-423, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.648×** | -4.1 | 0.002 | 13/36 (PANC-1, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.794×** | -3.9 | 0.004 | 15/35 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.791×** | -3.9 | 0.004 | 12/35 (A549, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **0.664×** | -3.8 | 0.005 | 10/36 (NCI-H2030, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.837× | -3.0 | 0.076 | 9/36 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4370. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 31.8 | 3 (1 ⚠) | 4 | [[Panobinostat (drug)]] 5 µM 2.64× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -17.5) |
| [[PANC-1 (line)]] | alt | 60.7 | 2 | 5 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.14× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -18.2) |
| [[A-172 (line)]] | wt | 49.7 | 1 | 5 | [[Tucidinostat (drug)]] 5 µM 1.83× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -27.8) |
| [[NCI-H460 (line)]] | wt | 15.0 | 1 | 5 | [[Tucidinostat (drug)]] 5 µM 2.39× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -17.5) |
| [[J82 (line)]] | alt | 57.7 | 1 | 4 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.93× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -26.1) |
| [[A549 (line)]] | wt | 34.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -17.8) |
| [[HS-578T (line)]] | alt | 51.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -24.2) |
| [[HOP62 (line)]] | alt | 37.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -17.7) |
| [[NCI-H23 (line)]] | alt | 42.7 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.88× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 31.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -19.6) |
| [[H4 (line)]] | wt | 29.1 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.109× (z -12.5) ⚠ transcription drop; cell-cycle shift, explains ~92% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0486× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 23.2 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.04× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 44.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -12.8) |
| [[SNU-1 (line)]] | wt | 24.5 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.155× (z -9.0) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.164× (z -8.7) |
| [[SW480 (line)]] | alt | 15.3 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.49× (z +10.1) | — |
| [[C32 (line)]] | wt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -12.3) |
| [[hTERT-HPNE (line)]] | wt | 38.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -14.2) |
| [[LoVo (line)]] | wt | 6.36 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.74× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.5) |
| [[SHP-77 (line)]] | alt | 26.2 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0870× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 26.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -11.6) |
| [[SW1417 (line)]] | alt | 8.21 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.58× (z +8.7) | — |
| [[A-427 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.44 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.04 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4370), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NENF]] | +0.70 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[HEBP1]] | +0.67 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[ECI2]] | +0.65 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[BLVRA]] | +0.64 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[SLC29A4]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[PCTP]] | +0.63 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[FBXO3]] | +0.63 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.62 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[SLC9A6]] | +0.61 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[CRLF3]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ASAP3]] | +0.60 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[SNTA1]] | +0.60 | +0.63 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H4]] | -0.66 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[CYB5D1]] | -0.66 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[INO80D]] | -0.63 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[LEKR1]] | -0.62 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[TASOR]] | -0.62 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[MEPCE]] | -0.62 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[PDCL3P4]] | -0.61 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[SRCAP]] | -0.61 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[PPP1R10]] | -0.60 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[COQ7]] | -0.60 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ZFP91]] | -0.60 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[LINC00571]] | -0.60 | -0.53 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD9]] | C | STARD9 activity raises RECK's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 5.96× lower at baseline in the lines without STARD9 | 0.011 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent; co-absent with the target |
| [[BVES]] | C | BVES activity raises RECK's level | lines that do not express BVES (19) vs lines expressing it (31) | 4.04× lower at baseline in the lines without BVES | 0.044 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNTA1]] | B | RECK activity raises SNTA1's level | lines that do not express RECK (12) vs lines expressing it (38) | 2.04× lower at baseline in the lines without RECK | 0.042 | ⚠ within organs, on part of the lines; also absent: OSBPL6, DZIP1L, STARD9 |
| [[MFGE8]] | B | RECK activity raises MFGE8's level | lines that do not express RECK (12) vs lines expressing it (38) | 2.49× lower at baseline in the lines without RECK | 0.045 | ⚠ within organs, on part of the lines; also absent: OSBPL6, DZIP1L, STARD9 |
| [[ADCY9]] | B | RECK activity raises ADCY9's level | lines that do not express RECK (12) vs lines expressing it (38) | 1.49× lower at baseline in the lines without RECK | 0.050 | ⚠ within organs, on part of the lines; also absent: OSBPL6, DZIP1L, STARD9 |
| [[GINM1]] | B | RECK activity raises GINM1's level | lines that do not express RECK (12) vs lines expressing it (38) | 1.48× lower at baseline in the lines without RECK | 0.060 | ⚠ within organs, on part of the lines; also absent: OSBPL6, DZIP1L, STARD9 |
| [[LINC00571]] | B | RECK activity lowers LINC00571's level | lines that do not express RECK (12) vs lines expressing it (38) | 1.99× higher at baseline in the lines without RECK | 0.067 | ⚠ within organs, on part of the lines; also absent: OSBPL6, DZIP1L, STARD9 |
| [[MALSU1]] | B | RECK activity raises MALSU1's level | lines that do not express RECK (12) vs lines expressing it (38) | 1.40× lower at baseline in the lines without RECK | 0.068 | ⚠ within organs, on part of the lines; also absent: OSBPL6, DZIP1L, STARD9 |
| [[STARD9]] | C | RECK activity raises STARD9's level | lines that do not express RECK (12) vs lines expressing it (38) | 3.24× lower at baseline in the lines without RECK | 0.004 | ⚠ within organs, on part of the lines; also absent: OSBPL6, DZIP1L, STARD9; co-absent with the target |
| [[BVES]] | C | RECK activity raises BVES's level | lines that do not express RECK (12) vs lines expressing it (38) | 3.59× lower at baseline in the lines without RECK | 0.046 | ⚠ within organs, on part of the lines; also absent: OSBPL6, DZIP1L, STARD9; co-absent with the target |

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-4.3, 1.4); signed map (-37.5, -4.5). **Vector** length 90.9, 21.9% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +14.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +8.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.2 | +10.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.8 | +13.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.6 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +8.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +3.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -15.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -15.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.3 | -24.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.0 | -6.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | +1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -6.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -2.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | reversion inducing cysteine rich protein with kazal motifs |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:36,036,913-36,124,455 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hRECK; previously ST15 |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O95980](https://www.uniprot.org/uniprotkb/O95980) (Reversion-inducing cysteine-rich protein with Kazal motifs):

> Functions together with ADGRA2 to enable brain endothelial cells to selectively respond to Wnt7 signals (WNT7A or WNT7B). Plays a key role in Wnt7-specific responses: required for central nervous system (CNS) angiogenesis and blood-brain barrier regulation (By similarity). Acts as a Wnt7-specific coactivator of canonical Wnt signaling by decoding Wnt ligands: acts by interacting specifically with the disordered linker region of Wnt7, thereby conferring ligand selectivity for Wnt7. ADGRA2 is …

**Summary**, from NCBI Gene [8434](https://www.ncbi.nlm.nih.gov/gene/8434):

> The protein encoded by this gene is a cysteine-rich, extracellular protein with protease inhibitor-like domains whose expression is suppressed strongly in many tumors and cells transformed by various kinds of oncogenes. In normal cells, this membrane-anchored glycoprotein may serve as a negative regulator for matrix metalloproteinase-9, a key enzyme involved in tumor invasion and metastasis. Several transcript variants encoding different isoforms have been found for this gene. [provided by …

**Accessions** — [HGNC:11345](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11345) · Entrez [8434](https://www.ncbi.nlm.nih.gov/gene/8434) · UniProt [O95980](https://www.uniprot.org/uniprotkb/O95980) · Ensembl [ENSG00000122707](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122707)

## Data

Gene col 4370: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4370); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4370, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4370]; `tensor/DDL_lfc|DDL_z.npy` [4370]; `embed/gene_vectors.npy` [4370]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4370 or target_col == 4370). Every well: [[RECK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RECK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
