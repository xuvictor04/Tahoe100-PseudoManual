---
symbol: "FAM169A"
type: "gene"
col: 12673
ensembl_id: "ENSG00000198780"
name: "family with sequence similarity 169 member A"
location: "5q13.3"
module: 137
arm: "+"
pooled_cpm: 28.93
n_lines_expressing: 38
n_dd_up: 27
n_dd_down: 11
n_dd_up_clean: 24
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 7
direction_downstream: 13
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# FAM169A

*family with sequence similarity 169 member A* — 5q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 3.10× (z +19.2, q 0e+00, up in 33 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.214× (z -27.2, q 0e+00, down in 35 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC16A9]] (+0.77, fdr 7e-06), [[GCFC2]] (+0.74, fdr 1e-05), [[PHACTR2]] (+0.72, fdr 7e-06); moves opposite to [[RAB40B]] (-0.63, fdr 5e-05), [[SBNO1]] (-0.62, fdr 1e-05), [[DNAAF3]] (-0.61, fdr 6e-05).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[CACHD1]] → it (grade B ⚠); 13 go from it, the strongest it → [[FAIM]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12673.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **3.10×** | +19.2 | 0e+00 | 33/35 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.02×** | +17.6 | 0e+00 | 31/36 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.98×** | +17.0 | 0e+00 | 33/36 (LS 180, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.20×** | +13.9 | 1e-41 | 30/36 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.97×** | +11.9 | 9e-31 | 32/35 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.96×** | +11.9 | 2e-30 | 31/35 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.83×** | +10.7 | 9e-25 | 32/36 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.69×** | +9.3 | 1e-18 | 28/35 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +7.8 | 4e-13 | 25/35 (PANC-1, NCI-H1573, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +6.6 | 2e-09 | 18/35 (LoVo, A-172, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +6.5 | 5e-09 | 18/35 (HOP62, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +6.4 | 1e-08 | 19/36 (HOP62, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +5.8 | 4e-07 | 18/35 (HOP62, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +5.3 | 4e-06 | 15/36 (LoVo, LS 180, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.34×** | +5.2 | 9e-06 | 16/35 (SW480, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +4.0 | 0.002 | 14/35 (HOP62, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12673.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.214×** | -27.2 | 0e+00 | 35/35 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.252×** | -24.3 | 0e+00 | 35/36 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.311×** | -20.6 | 0e+00 | 35/35 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.526×** | -11.4 | 1e-27 | 28/35 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.547×** | -10.7 | 2e-24 | 27/36 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.629×** | -4.3 | 0.002 | 17/36 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.643×** | -4.1 | 0.004 | 16/35 (SW480, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.743×** | -3.8 | 0.012 | 13/35 (NCI-H661, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.813×** | -3.7 | 0.016 | 10/35 (LoVo, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.809×** | -3.6 | 0.017 | 16/36 (RKO, C-33 A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Tetracycline (hydrochloride) (drug)]] 0.5 µM |  | **0.818×** | -3.6 | 0.020 | 4/35 (J82, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12673. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 65.4 | 6 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +20.8) | [[Panobinostat (drug)]] 5 µM 0.0955× (z -29.5) |
| [[RKO (line)]] | wt | 70.4 | 2 | 8 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 3.32× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.155× (z -17.4) |
| [[LoVo (line)]] | wt | 77.7 | 3 | 6 | [[Selinexor (drug)]] 5 µM 2.09× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.121× (z -22.0) |
| [[A-172 (line)]] | wt | 30.5 | 6 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 24.9 | 2 | 6 (3 ⚠) | [[Selinexor (drug)]] 5 µM 2.98× (z +13.5) | [[Belinostat (drug)]] 5 µM 0.167× (z -15.8) |
| [[PANC-1 (line)]] | alt | 33.8 | 5 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +14.9) | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -14.8) |
| [[SW1417 (line)]] | alt | 23.0 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 6.43× (z +19.8) | [[Panobinostat (drug)]] 0.5 µM 0.294× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 26.7 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +16.2) | [[Panobinostat (drug)]] 5 µM 0.166× (z -12.4) |
| [[A-427 (line)]] | wt | 102 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.171× (z -16.3) |
| [[AN3 CA (line)]] | alt | 86.0 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0623× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.188× (z -9.2) |
| [[C-33 A (line)]] | alt | 89.7 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0528× (z -26.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.160× (z -16.5) |
| [[A549 (line)]] | wt | 34.7 | 1 | 3 | [[Selinexor (drug)]] 5 µM 2.14× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.176× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 24.3 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.230× (z -13.2) |
| [[HepG2_C3A (line)]] | wt | 68.2 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.180× (z -13.1) |
| [[J82 (line)]] | alt | 29.3 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.256× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 22.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.122× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 34.6 | 3 | 1 | [[Selinexor (drug)]] 5 µM 3.39× (z +12.6) | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -9.9) |
| [[SHP-77 (line)]] | alt | 49.3 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -12.6) |
| [[SNU-1 (line)]] | wt | 48.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -12.8) |
| [[SW48 (line)]] | wt | 76.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.103× (z -16.4) |
| [[HOP62 (line)]] | alt | 27.2 | 1 | 2 | [[Harringtonine (drug)]] 5 µM 4.25× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -10.9) |
| [[LS 180 (line)]] | wt | 17.9 | 3 | 0 | [[Selinexor (drug)]] 5 µM 5.75× (z +14.7) | — |
| [[NCI-H2030 (line)]] | alt | 49.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.214× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 15.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +12.9) | — |
| [[COLO 205 (line)]] | alt | 31.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 9.64 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +15.0) | — |
| [[BT-474 (line)]] | alt | 18.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.214× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 8.94 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 58.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0974× (z -8.6) |
| [[A498 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.57 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.78 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12673), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC16A9]] | +0.77 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[GCFC2]] | +0.74 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[PHACTR2]] | +0.72 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[FAIM]] | +0.71 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[ZNF564]] | +0.70 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[SLC25A21]] | +0.70 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[LGALSL-DT]] | +0.69 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[SDSL]] | +0.67 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ZNF391]] | +0.67 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[ZNF649]] | +0.66 | +0.63 / +0.32 | both halves | 1e-04 |  |
| [[KLHL42]] | +0.65 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[NSD1]] | +0.65 | +0.60 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB40B]] | -0.63 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[SBNO1]] | -0.62 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[DNAAF3]] | -0.61 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[GNAI2]] | -0.61 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[CARHSP1]] | -0.61 | -0.54 / -0.37 | both halves | 7e-05 |  |
| [[GMCL1]] | -0.60 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[GSDMB]] | -0.60 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[GNB2]] | -0.59 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ADIPOR1]] | -0.59 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[SPSB3]] | -0.58 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[SLC27A1]] | -0.57 | -0.50 / -0.21 | both halves | 7e-04 |  |
| [[MOSPD3]] | -0.57 | -0.65 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACHD1]] | B | CACHD1 activity raises FAM169A's level | lines that do not express CACHD1 (7) vs lines expressing it (43) | 2.17× lower at baseline in the lines without CACHD1 | 0.020 | ⚠ within organs, on part of the lines; also absent: KCNK15-AS1 |
| [[ATF7IP2]] | B | ATF7IP2 activity raises FAM169A's level | lines that do not express ATF7IP2 (12) vs lines expressing it (38) | 2.76× lower at baseline in the lines without ATF7IP2 | 0.036 | ⚠ within organs, on part of the lines |
| [[MACROH2A2]] | B | MACROH2A2 activity raises FAM169A's level | lines that do not express MACROH2A2 (19) vs lines expressing it (31) | 3.06× lower at baseline in the lines without MACROH2A2 | 0.044 | ⚠ within organs, on part of the lines; also absent: MSI1, KCNQ2, GAS7 |
| [[MVB12B]] | B | MVB12B activity raises FAM169A's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 3.66× lower at baseline in the lines without MVB12B | 0.061 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[ULK2]] | B | ULK2 activity raises FAM169A's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 2.07× lower at baseline in the lines without ULK2 | 0.069 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[FAXC]] | B | FAXC activity raises FAM169A's level | lines that do not express FAXC (11) vs lines expressing it (39) | 2.43× lower at baseline in the lines without FAXC | 0.098 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[STOX1]] | C | STOX1 activity raises FAM169A's level | lines that do not express STOX1 (9) vs lines expressing it (41) | 5.05× lower at baseline in the lines without STOX1 | 0.082 | ⚠ within organs, on part of the lines; also absent: CACNA2D2, RIMS3, VASH2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAIM]] | B | FAM169A activity raises FAIM's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 1.80× lower at baseline in the lines without FAM169A | 0.008 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |
| [[THUMPD2]] | B | FAM169A activity raises THUMPD2's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 1.35× lower at baseline in the lines without FAM169A | 0.014 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |
| [[MVB12B]] | B | FAM169A activity raises MVB12B's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 2.40× lower at baseline in the lines without FAM169A | 0.019 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |
| [[KLHL23]] | B | FAM169A activity raises KLHL23's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 1.86× lower at baseline in the lines without FAM169A | 0.025 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |
| [[DIS3L]] | B | FAM169A activity raises DIS3L's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 1.75× lower at baseline in the lines without FAM169A | 0.032 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |
| [[MACROH2A2]] | B | FAM169A activity raises MACROH2A2's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 4.53× lower at baseline in the lines without FAM169A | 0.041 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |
| [[PPIL1]] | B | FAM169A activity raises PPIL1's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 1.40× lower at baseline in the lines without FAM169A | 0.050 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |
| [[TMA16]] | B | FAM169A activity raises TMA16's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 1.26× lower at baseline in the lines without FAM169A | 0.070 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |
| [[ZNF747]] | B | FAM169A activity raises ZNF747's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 1.12× lower at baseline in the lines without FAM169A | 0.074 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |
| [[CACHD1]] | B | FAM169A activity raises CACHD1's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 1.72× lower at baseline in the lines without FAM169A | 0.077 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |
| [[TRAF3]] | B | FAM169A activity raises TRAF3's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 1.32× lower at baseline in the lines without FAM169A | 0.078 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |
| [[GPATCH4]] | B | FAM169A activity raises GPATCH4's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 1.29× lower at baseline in the lines without FAM169A | 0.086 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.729). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-6.0, 7.2); signed map (19.6, -31.2). **Vector** length 119, 31.4% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +13.4 | +17.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.2 | +19.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.2 | +11.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +7.9 | +11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.4 | +13.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.3 | +9.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.2 | +3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.0 | +3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.8 | +3.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.6 | -20.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.3 | -24.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.2 | -27.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.9 | -11.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.0 | -10.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | +1.6 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -4.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.5 | -3.8 |
|  | [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | -1.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 169 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.3 — chr5:74,777,574-74,866,966 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0888, SLAP75, SLAP |
| Reactome | 4 pathways, smallest: RHOF GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

UniProt [Q9Y6X4](https://www.uniprot.org/uniprotkb/Q9Y6X4) carries no function annotation.

**Summary**, from NCBI Gene [26049](https://www.ncbi.nlm.nih.gov/gene/26049):

> Located in nuclear membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29138](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29138) · Entrez [26049](https://www.ncbi.nlm.nih.gov/gene/26049) · UniProt [Q9Y6X4](https://www.uniprot.org/uniprotkb/Q9Y6X4) · Ensembl [ENSG00000198780](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198780)

## Data

Gene col 12673: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12673); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12673, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12673]; `tensor/DDL_lfc|DDL_z.npy` [12673]; `embed/gene_vectors.npy` [12673]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12673 or target_col == 12673). Every well: [[FAM169A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM169A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
