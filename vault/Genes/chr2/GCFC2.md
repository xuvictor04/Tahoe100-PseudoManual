---
symbol: "GCFC2"
type: "gene"
col: 81
ensembl_id: "ENSG00000005436"
name: "GC-rich sequence DNA-binding factor 2"
location: "2p12"
module: 1
arm: "+"
pooled_cpm: 39.54
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# GCFC2

*GC-rich sequence DNA-binding factor 2* — 2p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.95× (z +23.6, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.638× (z -5.9, q 2e-06, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YTHDC2]] (+0.76, fdr 7e-06), [[POGLUT1]] (+0.74, fdr 7e-06), [[FAM169A]] (+0.74, fdr 1e-05); moves opposite to [[MOSPD3]] (-0.70, fdr 8e-06), [[SAP130]] (-0.68, fdr 1e-05), [[ALKBH5]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CACHD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 81.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +23.6 | 0e+00 | 43/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.12×** | +18.8 | 0e+00 | 43/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.13×** | +18.2 | 0e+00 | 41/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +13.8 | 5e-41 | 36/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +10.5 | 7e-24 | 32/45 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +10.5 | 7e-24 | 26/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +9.7 | 4e-20 | 37/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +8.8 | 7e-17 | 35/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +8.6 | 3e-16 | 29/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +7.9 | 1e-13 | 24/48 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +7.8 | 4e-13 | 27/47 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.20× | +6.3 | 1e-08 | 20/48 (J82, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.22×** | +5.0 | 2e-05 | 19/48 (A549, PANC-1, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **1.22×** | +4.6 | 1e-04 | 20/44 (LS 180, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.20×** | +4.6 | 1e-04 | 20/48 (NCI-H2347, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +4.6 | 2e-04 | 14/48 (NCI-H1792, C32, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.20× | +4.5 | 2e-04 | 14/47 (LS 180, A498, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.13× | +4.5 | 3e-04 | 12/48 (HOP62, CFPAC-1, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +4.2 | 7e-04 | 11/47 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.38×** | +4.2 | 7e-04 | 13/47 (MIA PaCa-2, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.38×** | +4.2 | 8e-04 | 10/47 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +4.2 | 8e-04 | 10/48 (LS 180, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 81.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.638×** | -5.9 | 2e-06 | 26/48 (RKO, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.646×** | -5.7 | 3e-06 | 21/47 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.802×** | -5.3 | 2e-05 | 20/47 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -4.9 | 2e-04 | 3/48 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.866× | -3.6 | 0.029 | 16/47 (SW 900, J82, …) | rises with dose | low cells (technical?) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 0.866× | -3.6 | 0.029 | 9/48 (SK-MEL-2, BT-474, …) | inconsistent across doses |  |
| [[Pentoxifylline (drug)]] 0.5 µM |  | 0.868× | -3.6 | 0.031 | 5/48 (BT-474, KATO III, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 81. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 41.6 | 6 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.54× (z +12.2) | — |
| [[RKO (line)]] | wt | 97.0 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.232× (z -9.3) |
| [[SW480 (line)]] | alt | 38.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.5) | — |
| [[A-427 (line)]] | wt | 93.3 | 1 | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.12× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.233× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 45.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.04× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.397× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[LS 180 (line)]] | wt | 29.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +12.8) | — |
| [[NCI-H1792 (line)]] | alt | 34.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.12× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 89.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.19× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.467× (z -8.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 70.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +21.9) | — |
| [[A-172 (line)]] | wt | 25.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +13.1) | — |
| [[C-33 A (line)]] | alt | 72.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[CFPAC-1 (line)]] | alt | 16.7 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.17× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 50.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 40.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +13.6) | — |
| [[NCI-H460 (line)]] | wt | 58.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.31× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 1.83× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 73.3 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.192× (z -9.1) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 18.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +11.3) | — |
| [[CHP-212 (line)]] | wt | 47.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.101× (z -10.6) ⚠ cell-cycle shift, explains ~18% of this change |
| [[HepG2_C3A (line)]] | wt | 40.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 17.7 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.226× (z -9.2) |
| [[HT-29 (line)]] | alt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +10.4) | — |
| [[KATO III (line)]] | alt | 27.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 80.2 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.45× (z +10.0) ⚠ unreliable plate only | — |
| [[NCI-H2347 (line)]] | alt | 13.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +11.1) | — |
| [[SNU-1 (line)]] | wt | 68.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -10.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 51.3 | 0 | 1 | — | [[Riluzole hydrochloride (drug)]] 0.5 µM 0.0727× (z -8.8) |
| [[SW 900 (line)]] | alt | 24.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +9.9) | — |
| [[A498 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 81), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YTHDC2]] | +0.76 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[POGLUT1]] | +0.74 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[FAM169A]] | +0.74 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[GPATCH4]] | +0.72 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[ZC3H7B]] | +0.71 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[MIOS]] | +0.71 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[ABCE1]] | +0.69 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[ST7L]] | +0.69 | +0.76 / +0.49 | both halves | 1e-05 |  |
| [[THUMPD2]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[METTL8]] | +0.69 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[TMA16]] | +0.68 | +0.69 / +0.57 | both halves | 8e-06 |  |
| [[ZNF280D]] | +0.68 | +0.59 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOSPD3]] | -0.70 | -0.71 / -0.58 | both halves | 8e-06 |  |
| [[SAP130]] | -0.68 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[ALKBH5]] | -0.67 | -0.67 / -0.59 | both halves | 7e-06 |  |
| [[MED26]] | -0.65 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[TSEN34]] | -0.65 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[RAB2A]] | -0.65 | -0.74 / -0.55 | both halves | 1e-05 |  |
| [[IGSF8]] | -0.64 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[GNB2]] | -0.64 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.63 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[PLA2G15]] | -0.63 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[GNAI2]] | -0.61 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[MTMR14]] | -0.61 | -0.62 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACHD1]] | B | CACHD1 activity raises GCFC2's level | lines that do not express CACHD1 (7) vs lines expressing it (43) | 1.80× lower at baseline in the lines without CACHD1 | 0.042 | ⚠ within organs, on part of the lines; also absent: KCNK15-AS1 |
| [[FTCDNL1]] | B | FTCDNL1 activity raises GCFC2's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.49× lower at baseline in the lines without FTCDNL1 | 0.058 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[SLC16A9]] | B | SLC16A9 activity raises GCFC2's level | lines that do not express SLC16A9 (18) vs lines expressing it (32) | 1.33× lower at baseline in the lines without SLC16A9 | 0.096 | ⚠ within organs, on part of the lines; also absent: BOC, TLCD4, KIF26A; maybe low, not absent |
| [[LRRC8D]] | C | LRRC8D activity raises GCFC2's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 2.23× lower at baseline in the lines without LRRC8D | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.714). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-6.0, 6.5); signed map (19.8, -31.4). **Vector** length 112, 28.5% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.6 | +18.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +23.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.2 | +18.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +6.4 | +7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.2 | +13.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +7.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +4.2 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.5 | +0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.5 | -0.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.2 | -1.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.5 | -5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -3.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | GC-rich sequence DNA-binding factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p12 — chr2:75,652,000-75,710,985 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DNABF, GCF; previously TCF9, C2orf3 |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P16383](https://www.uniprot.org/uniprotkb/P16383) (Intron Large complex component GCFC2):

> Involved in pre-mRNA splicing through regulating spliceosome C complex formation. May play a role during late-stage splicing events and turnover of excised introns.

**Summary**, from NCBI Gene [6936](https://www.ncbi.nlm.nih.gov/gene/6936):

> The first mRNA transcript isolated for this gene was part of an artificial chimera derived from two distinct gene transcripts and a primer used in the cloning process (see Genbank accession M29204). A positively charged amino terminus present only in the chimera was determined to bind GC-rich DNA, thus mistakenly thought to identify a transcription factor gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1317](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1317) · Entrez [6936](https://www.ncbi.nlm.nih.gov/gene/6936) · UniProt [P16383](https://www.uniprot.org/uniprotkb/P16383) · Ensembl [ENSG00000005436](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005436)

## Data

Gene col 81: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 81); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 81, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 81]; `tensor/DDL_lfc|DDL_z.npy` [81]; `embed/gene_vectors.npy` [81]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 81 or target_col == 81). Every well: [[GCFC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCFC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
