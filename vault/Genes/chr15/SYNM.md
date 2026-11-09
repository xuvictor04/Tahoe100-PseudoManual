---
symbol: "SYNM"
type: "gene"
col: 11265
ensembl_id: "ENSG00000182253"
name: "synemin"
location: "15q26.3"
module: 9
arm: "+"
pooled_cpm: 19.28
n_lines_expressing: 36
n_dd_up: 34
n_dd_down: 11
n_dd_up_clean: 22
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 9
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SYNM

*synemin* — 15q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.10× (z +18.6, q 0e+00, up in 22 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.633× (z -5.3, q 5e-05, down in 20 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.05 µM: 0.655× (z -4.9, q 2e-04, down in 17 of 34 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIEZO2]] (+0.64, fdr 1e-05), [[KCTD12]] (+0.57, fdr 1e-05), [[UNC5C]] (+0.56, fdr 3e-05); moves opposite to [[LCMT1]] (-0.47, fdr 3e-04), [[ANKS3]] (-0.45, fdr 2e-04), [[TMEM231]] (-0.44, fdr 2e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[DPY19L2P2-1]] → it (grade B ⚠); 9 go from it, the strongest it → [[SRRM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11265.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.10×** | +18.6 | 0e+00 | 22/33 (NCI-H1792, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.80×** | +12.0 | 1e-30 | 27/34 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.58×** | +11.0 | 6e-26 | 27/34 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.80×** | +9.7 | 5e-20 | 26/34 (SW480, RPMI-7951, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.66×** | +8.3 | 1e-14 | 24/34 (A549, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.63×** | +8.0 | 8e-14 | 19/32 (A549, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.83×** | +6.8 | 9e-10 | 14/24 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +6.7 | 1e-09 | 21/34 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +6.6 | 3e-09 | 17/32 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.73×** | +6.4 | 1e-08 | 22/34 (J82, CFPAC-1, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.74×** | +6.2 | 2e-08 | 19/34 (A498, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.66×** | +5.9 | 2e-07 | 21/33 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.66×** | +5.9 | 2e-07 | 17/28 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.62×** | +5.6 | 1e-06 | 17/34 (PANC-1, NCI-H2030, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +5.5 | 1e-06 | 18/34 (J82, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +5.4 | 2e-06 | 18/34 (HS-578T, NCI-H2347, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +4.9 | 3e-05 | 18/34 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.51×** | +4.8 | 5e-05 | 14/34 (AN3 CA, SK-MEL-2, …) | two highest doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.47×** | +4.5 | 2e-04 | 17/34 (PANC-1, C32, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +4.2 | 8e-04 | 13/34 (J82, PANC-1, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.26×** | +3.7 | 0.004 | 11/34 (C32, PANC-1, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.82×** | +3.6 | 0.006 | 7/34 (Hs 766T, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.007 | 10/34 (PANC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11265.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.633×** | -5.3 | 5e-05 | 20/34 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.655×** | -4.9 | 2e-04 | 17/34 (SW 1271, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.452×** | -4.8 | 3e-04 | 17/34 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.669×** | -4.7 | 4e-04 | 18/34 (PANC-1, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.757×** | -4.6 | 5e-04 | 14/34 (C32, PANC-1, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.678×** | -4.4 | 0.001 | 16/34 (NCI-H661, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.695×** | -4.3 | 0.002 | 17/34 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.500×** | -4.2 | 0.002 | 18/33 (HS-578T, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.707×** | -4.0 | 0.003 | 16/34 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.742×** | -3.4 | 0.045 | 15/34 (hTERT-HPNE, SK-MEL-2, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.761×** | -3.2 | 0.075 | 13/34 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.58 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11265. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 167 | 2 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.97× (z +20.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -14.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.343× (z -11.3) |
| [[PANC-1 (line)]] | alt | 50.7 | 2 (2 ⚠) | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.25× (z +10.0) ⚠ cell-cycle shift, explains ~31% of this change | [[Digitoxin (drug)]] 5 µM 0.284× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.342× (z -9.1) |
| [[A-427 (line)]] | wt | 18.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -10.2) |
| [[A549 (line)]] | wt | 17.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +12.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.81× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 57.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +14.2) | — |
| [[NCI-H460 (line)]] | wt | 36.2 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +11.0) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SW480 (line)]] | alt | 6.71 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +10.3) | — |
| [[A498 (line)]] | wt | 19.8 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.17× (z +12.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.26× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 6.04 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +14.0) | — |
| [[J82 (line)]] | alt | 13.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +12.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.110× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 31.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +20.8) | — |
| [[SK-MEL-2 (line)]] | alt | 56.7 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.52× (z +8.6) ⚠ cell-cycle shift, explains ~31% of this change | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.293× (z -8.5) |
| [[H4 (line)]] | wt | 13.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0809× (z -9.0) |
| [[HOP62 (line)]] | alt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +17.8) | — |
| [[hTERT-HPNE (line)]] | wt | 21.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 24.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 25.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.16× (z +15.2) | — |
| [[A-172 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.36 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.91 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11265), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIEZO2]] | +0.64 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[KCTD12]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[UNC5C]] | +0.56 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[DPY19L2P2-1]] | +0.56 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[DPY19L2P2]] | +0.56 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[DPY19L2]] | +0.55 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[EPHA7]] | +0.55 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[RMEL3]] | +0.54 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[ATRNL1]] | +0.54 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ADAMTS3]] | +0.54 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[CUBN]] | +0.53 | +0.68 / +0.36 | both halves | 1e-04 |  |
| [[CCDC136]] | +0.52 | +0.55 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCMT1]] | -0.47 | -0.58 / -0.27 | both halves | 3e-04 |  |
| [[ANKS3]] | -0.45 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[TMEM231]] | -0.44 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[DZANK1]] | -0.44 | -0.14 / -0.43 | ⚠ not reproduced | 0.002 |  |
| [[BORCS5]] | -0.42 | -0.47 / -0.18 | ⚠ not reproduced | 1e-03 |  |
| [[MTMR12]] | -0.42 | -0.49 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPY19L2P2-1]] | B | DPY19L2P2-1 activity raises SYNM's level | lines that do not express DPY19L2P2-1 (17) vs lines expressing it (33) | 2.73× lower at baseline in the lines without DPY19L2P2-1 | 1e-03 | ⚠ within organs, on part of the lines; also absent: RNF182, ENSG00000234405, FGF2 |
| [[RAB38]] | B | RAB38 activity lowers SYNM's level | lines that do not express RAB38 (23) vs lines expressing it (27) | 1.08× higher at baseline in the lines without RAB38 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000255102, TMEM154, ENSG00000233539 |
| [[TOP2A]] | B | TOP2A activity lowers SYNM's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLCE1]] | B | PLCE1 activity raises SYNM's level | lines that do not express PLCE1 (16) vs lines expressing it (34) | 1.56× lower at baseline in the lines without PLCE1 | 0.068 | ⚠ within organs, on part of the lines; also absent: SLC46A3; maybe low, not absent |
| [[DZIP1]] | C | DZIP1 activity raises SYNM's level | lines that do not express DZIP1 (23) vs lines expressing it (27) | 3.03× lower at baseline in the lines without DZIP1 | 0.093 | ⚠ within organs, on part of the lines; also absent: BVES, LAYN, GLIS1; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRRM2]] | B | SYNM activity lowers SRRM2's level | lines that do not express SYNM (14) vs lines expressing it (36) | 1.32× higher at baseline in the lines without SYNM | 0.015 | ⚠ within organs, on part of the lines; also absent: AKR1B1, GAMT, FHL1; maybe low, not absent |
| [[CYP2U1]] | B | SYNM activity raises CYP2U1's level | lines that do not express SYNM (14) vs lines expressing it (36) | 1.71× lower at baseline in the lines without SYNM | 0.015 | ⚠ within organs, on part of the lines; also absent: AKR1B1, GAMT, FHL1; maybe low, not absent |
| [[TMEM231]] | B | SYNM activity raises TMEM231's level | lines that do not express SYNM (14) vs lines expressing it (36) | 1.54× lower at baseline in the lines without SYNM | 0.031 | ⚠ within organs, on part of the lines; also absent: AKR1B1, GAMT, FHL1; maybe low, not absent |
| [[CCDC136]] | B | SYNM activity raises CCDC136's level | lines that do not express SYNM (14) vs lines expressing it (36) | 1.63× lower at baseline in the lines without SYNM | 0.052 | ⚠ within organs, on part of the lines; also absent: AKR1B1, GAMT, FHL1; maybe low, not absent |
| [[PLEKHA6]] | B | SYNM activity lowers PLEKHA6's level | lines that do not express SYNM (14) vs lines expressing it (36) | 3.58× higher at baseline in the lines without SYNM | 0.059 | ⚠ within organs, on part of the lines; also absent: AKR1B1, GAMT, FHL1; maybe low, not absent |
| [[CCDC144CP]] | B | SYNM activity raises CCDC144CP's level | lines that do not express SYNM (14) vs lines expressing it (36) | 1.91× lower at baseline in the lines without SYNM | 0.079 | ⚠ within organs, on part of the lines; also absent: AKR1B1, GAMT, FHL1; maybe low, not absent |
| [[DPY19L2P2-1]] | B | SYNM activity raises DPY19L2P2-1's level | lines that do not express SYNM (14) vs lines expressing it (36) | 1.83× lower at baseline in the lines without SYNM | 0.090 | ⚠ within organs, on part of the lines; also absent: AKR1B1, GAMT, FHL1; maybe low, not absent |
| [[HSPA2]] | C | SYNM activity raises HSPA2's level | lines that do not express SYNM (14) vs lines expressing it (36) | 2.42× lower at baseline in the lines without SYNM | 0.069 | ⚠ within organs, on part of the lines; also absent: AKR1B1, GAMT, FHL1; maybe low, not absent; co-absent with the target |
| [[AKR1B1]] | C | SYNM activity raises AKR1B1's level | lines that do not express SYNM (14) vs lines expressing it (36) | 5.06× lower at baseline in the lines without SYNM | 0.082 | ⚠ within organs, on part of the lines; also absent: AKR1B1, GAMT, FHL1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.366). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.5, 26.7); signed map (37.2, 32.3). **Vector** length 88.3, 22.2% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +18.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +4.7 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +4.5 | +6.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.6 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +5.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +4.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +4.2 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -4.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -1.9 | +5.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.8 | -2.1 |
|  | [[Neratinib (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | synemin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.3 — chr15:99,098,217-99,135,593 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0353, SYN; previously DMN |
| Gene groups (HGNC) | A-kinase anchoring proteins; Intermediate filaments Type IV |
| Matched by | ensembl_id |

**Function**, from UniProt [O15061](https://www.uniprot.org/uniprotkb/O15061) (Synemin):

> Type-VI intermediate filament (IF) which plays an important cytoskeletal role within the muscle cell cytoskeleton. It forms heteromeric IFs with desmin and/or vimentin, and via its interaction with cytoskeletal proteins alpha-dystrobrevin, dystrophin, talin-1, utrophin and vinculin, is able to link these heteromeric IFs to adherens-type junctions, such as to the costameres, neuromuscular junctions, and myotendinous junctions within striated muscle cells.

**Summary**, from NCBI Gene [23336](https://www.ncbi.nlm.nih.gov/gene/23336):

> The protein encoded by this gene is an intermediate filament (IF) family member. IF proteins are cytoskeletal proteins that confer resistance to mechanical stress and are encoded by a dispersed multigene family. This protein has been found to form a linkage between desmin, which is a subunit of the IF network, and the extracellular matrix, and provides an important structural support in muscle. Two alternatively spliced variants encoding different isoforms have been described for this gene. …

**Accessions** — [HGNC:24466](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24466) · Entrez [23336](https://www.ncbi.nlm.nih.gov/gene/23336) · UniProt [O15061](https://www.uniprot.org/uniprotkb/O15061) · Ensembl [ENSG00000182253](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182253)

## Data

Gene col 11265: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11265); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11265, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11265]; `tensor/DDL_lfc|DDL_z.npy` [11265]; `embed/gene_vectors.npy` [11265]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11265 or target_col == 11265). Every well: [[SYNM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYNM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
