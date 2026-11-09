---
symbol: "PRTFDC1"
type: "gene"
col: 1787
ensembl_id: "ENSG00000099256"
name: "phosphoribosyl transferase domain containing 1"
location: "10p12.1"
module: 25
arm: "+"
pooled_cpm: 9.95
n_lines_expressing: 39
n_dd_up: 11
n_dd_down: 22
n_dd_up_clean: 7
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# PRTFDC1

*phosphoribosyl transferase domain containing 1* — 10p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.60× (z +12.0, q 2e-30, up in 14 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.37× (z +5.9, q 6e-07, up in 21 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.464× (z -14.2, q 7e-43, down in 30 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNASEH2B]] (+0.63, fdr 2e-05), [[FUCA2]] (+0.62, fdr 2e-05), [[FUBP1]] (+0.62, fdr 2e-05); moves opposite to [[CDC34]] (-0.62, fdr 1e-05), [[ARID3A]] (-0.59, fdr 3e-05), [[RRAS]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1787.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +12.0 | 2e-30 | 14/17 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +9.8 | 2e-20 | 21/30 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +6.6 | 9e-09 | 15/25 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.9 | 6e-07 | 21/36 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +4.6 | 4e-04 | 13/36 (NCI-H1792, AsPC-1, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.013 | 10/36 (NCI-H1792, AsPC-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.029 | 12/35 (NCI-H2030, A549, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.049 | 1/37 (HOP62) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.049 | 10/35 (NCI-H1792, LS 180, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.30×** | +3.3 | 0.049 | 7/35 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.3 | 0.054 | 4/36 (NCI-H1792, HOP62, …) | rises with dose | position effect removed |
| [[venetoclax (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.054 | 2/36 (Hs 766T, HCT15) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1787.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.464×** | -14.2 | 7e-43 | 30/34 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.457×** | -10.2 | 4e-22 | 30/36 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.466×** | -10.0 | 4e-21 | 24/36 (KATO III, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.530×** | -8.3 | 2e-14 | 27/37 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.533×** | -8.2 | 2e-14 | 24/37 (NCI-H23, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.600×** | -6.4 | 1e-08 | 19/35 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.630×** | -6.0 | 1e-07 | 21/34 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.690×** | -4.8 | 9e-05 | 17/35 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.697×** | -4.7 | 2e-04 | 18/34 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.700×** | -4.4 | 6e-04 | 17/36 (PANC-1, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.795×** | -4.2 | 0.001 | 15/36 (SW 1271, HCT15, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.537×** | -4.2 | 0.001 | 13/33 (LS 180, KATO III, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.738×** | -4.0 | 0.003 | 15/35 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.751×** | -3.7 | 0.007 | 10/36 (NCI-H23, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.753×** | -3.6 | 0.014 | 11/33 (NCI-H23, HCT15, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.759×** | -3.5 | 0.016 | 9/35 (SNU-423, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.765×** | -3.5 | 0.016 | 12/35 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.614×** | -3.3 | 0.027 | 9/33 (LoVo, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1787. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 19.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.8) |
| [[PANC-1 (line)]] | alt | 8.61 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -16.0) |
| [[COLO 205 (line)]] | alt | 14.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0916× (z -15.3) |
| [[NCI-H1573 (line)]] | alt | 8.50 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 16.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.285× (z -10.9) |
| [[A498 (line)]] | wt | 7.81 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -14.2) |
| [[CFPAC-1 (line)]] | alt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -9.2) |
| [[HOP62 (line)]] | alt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -8.8) |
| [[KATO III (line)]] | alt | 27.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.247× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -15.7) |
| [[Panc 03.27 (line)]] | alt | 8.06 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -10.4) |
| [[RKO (line)]] | wt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -9.0) |
| [[SW1417 (line)]] | alt | 9.07 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.143× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~57% of this change |
| [[A-172 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.854 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1787), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNASEH2B]] | +0.63 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[FUCA2]] | +0.62 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[FUBP1]] | +0.62 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[MTMR2]] | +0.61 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[EWSR1]] | +0.59 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[DHRS4L2]] | +0.59 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[TIMELESS]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[RBBP8]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[SMG7]] | +0.58 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[HELLS]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[GPD2]] | +0.57 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[HFE]] | +0.57 | +0.51 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC34]] | -0.62 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ARID3A]] | -0.59 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[RRAS]] | -0.58 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[NOSIP]] | -0.58 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[TMEM120A]] | -0.56 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[PPARA]] | -0.56 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[FAM177A1]] | -0.56 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[GUK1]] | -0.56 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[PMM1]] | -0.55 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[TARS3]] | -0.55 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[FAM89B]] | -0.54 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[MT1X]] | -0.54 | -0.48 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.487). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-33.4, -26.5); signed map (13.2, -40.7). **Vector** length 68.5, 14.1% of its response variance represented; |z| ≥ 3 in 745 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.1 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +3.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.3 | -10.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.0 | -10.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.9 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -4.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -4.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | phosphoribosyl transferase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.1 — chr10:24,848,614-24,952,606 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HHGP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRG1](https://www.uniprot.org/uniprotkb/Q9NRG1) (Phosphoribosyltransferase domain-containing protein 1):

> Has low, barely detectable phosphoribosyltransferase activity (in vitro). Binds GMP, IMP and alpha-D-5-phosphoribosyl 1-pyrophosphate (PRPP). Is not expected to contribute to purine metabolism or GMP salvage.

**Summary**, from NCBI Gene [56952](https://www.ncbi.nlm.nih.gov/gene/56952):

> Enables protein homodimerization activity. Predicted to be involved in purine ribonucleoside salvage. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23333](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23333) · Entrez [56952](https://www.ncbi.nlm.nih.gov/gene/56952) · UniProt [Q9NRG1](https://www.uniprot.org/uniprotkb/Q9NRG1) · Ensembl [ENSG00000099256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099256)

## Data

Gene col 1787: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1787); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1787, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1787]; `tensor/DDL_lfc|DDL_z.npy` [1787]; `embed/gene_vectors.npy` [1787]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1787 or target_col == 1787). Every well: [[PRTFDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRTFDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
