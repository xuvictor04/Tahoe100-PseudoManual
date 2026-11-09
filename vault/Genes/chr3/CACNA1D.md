---
symbol: "CACNA1D"
type: "gene"
col: 8066
ensembl_id: "ENSG00000157388"
name: "calcium voltage-gated channel subunit alpha1 D"
location: "3p21.1"
module: 27
arm: "+"
pooled_cpm: 30.27
n_lines_expressing: 27
n_dd_up: 25
n_dd_down: 26
n_dd_up_clean: 16
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# CACNA1D

*calcium voltage-gated channel subunit alpha1 D* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.34× (z +18.6, q 0e+00, up in 8 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.613× (z -7.6, q 2e-11, down in 21 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRACDL]] (+0.62, fdr 1e-05), [[FREM2]] (+0.61, fdr 1e-05), [[LINC01091]] (+0.59, fdr 1e-05); moves opposite to [[SVIL-AS1-1]] (-0.45, fdr 1e-04), [[CEP104]] (-0.43, fdr 2e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[FREM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8066.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +18.6 | 0e+00 | 8/25 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.21×** | +17.4 | 0e+00 | 16/25 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +11.7 | 4e-29 | 7/21 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.98×** | +10.6 | 7e-24 | 17/24 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +10.3 | 6e-23 | 8/16 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +9.6 | 6e-20 | 11/24 (HEC-1-A, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +6.2 | 5e-08 | 7/20 (SW48, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.39×** | +5.1 | 2e-05 | 4/25 (HEC-1-A, A498, …) | rises with dose |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.38×** | +5.0 | 4e-05 | 5/24 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.05 µM |  | **1.37×** | +4.9 | 6e-05 | 15/25 (A-427, BT-474, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.4 | 5e-04 | 2/25 (A498, HEC-1-A) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.32×** | +4.3 | 9e-04 | 9/24 (HEC-1-A, SW480, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.002 | 2/24 (SK-MEL-2, C-33 A) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.31×** | +4.0 | 0.002 | 1/24 (A498) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +4.0 | 0.003 | 12/24 (SW 900, PANC-1, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.006 | 6/24 (A-427, NCI-H23, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.30×** | +3.7 | 0.007 | 8/24 (SW48, RKO, …) | all doses, flat | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.017 | 3/24 (NCI-H1573, SW1417, …) | all doses, flat | position effect removed |
| [[Meloxicam (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.019 | 2/24 (SW1417, LoVo) | inconsistent across doses |  |
| [[Arbutin (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.019 | 5/24 (A498, SHP-77, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8066.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.613×** | -7.6 | 2e-11 | 21/24 (SNU-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.618×** | -7.5 | 2e-11 | 19/24 (SNU-1, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.650×** | -6.4 | 2e-08 | 19/24 (SNU-1, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.661×** | -6.4 | 2e-08 | 18/24 (SHP-77, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.758×** | -6.1 | 1e-07 | 18/25 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.679×** | -6.0 | 2e-07 | 12/24 (NCI-H23, A-427, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.682×** | -5.7 | 9e-07 | 12/24 (COLO 205, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.697×** | -5.6 | 1e-06 | 14/24 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.702×** | -5.5 | 2e-06 | 18/24 (PANC-1, COLO 205, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.711×** | -5.3 | 7e-06 | 16/24 (A-427, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.720×** | -5.1 | 2e-05 | 16/24 (SNU-1, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.735×** | -4.8 | 8e-05 | 16/24 (NCI-H23, COLO 205, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.742×** | -4.4 | 5e-04 | 15/24 (SHP-77, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.754×** | -4.2 | 0.001 | 7/25 (CFPAC-1, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.763×** | -4.2 | 0.001 | 8/24 (SNU-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.775×** | -4.0 | 0.002 | 15/24 (A-427, COLO 205, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.791×** | -3.6 | 0.008 | 11/24 (COLO 205, NCI-H23, …) | rises with dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.804×** | -3.2 | 0.038 | 0/25 | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.676×** | -3.2 | 0.039 | 7/24 (A549, SHP-77, …) | rises with dose | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8066. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 127 | 0 | 18 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0752× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -13.1) |
| [[SHP-77 (line)]] | alt | 540 | 0 | 17 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -17.4) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -13.0) |
| [[NCI-H23 (line)]] | alt | 31.1 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -18.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.175× (z -10.5) |
| [[SNU-1 (line)]] | wt | 44.0 | 0 | 10 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0507× (z -16.4) |
| [[PANC-1 (line)]] | alt | 96.1 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0765× (z -23.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -11.0) |
| [[A-427 (line)]] | wt | 37.8 | 1 | 7 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.44× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -16.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.127× (z -13.8) |
| [[CFPAC-1 (line)]] | alt | 37.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.102× (z -11.1) |
| [[HT-29 (line)]] | alt | 92.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -8.6) |
| [[A549 (line)]] | wt | 41.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0978× (z -16.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.156× (z -9.4) |
| [[SW480 (line)]] | alt | 9.70 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 3.55× (z +11.2) | — |
| [[A498 (line)]] | wt | 9.20 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 12.4 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 4.41× (z +11.7) | — |
| [[LoVo (line)]] | wt | 37.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -8.8) |
| [[BT-474 (line)]] | alt | 33.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 23.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.74× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 9.04 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.58× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -8.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 39.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 6.02 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.46 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.01 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.23 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.04 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.01 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.92 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.44 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.37 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.20 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.53 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.21 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.31 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.96 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.90 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.62 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.94 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8066), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRACDL]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[FREM2]] | +0.61 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[LINC01091]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[BTNL9]] | +0.56 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[KSR2]] | +0.54 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[ELAVL2]] | +0.52 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[CFTR]] | +0.52 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[DNAH6]] | +0.52 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[IQGAP2]] | +0.51 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[PROM2]] | +0.51 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[PLXDC2]] | +0.51 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[HNF1A-AS1]] | +0.51 | +0.45 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SVIL-AS1-1]] | -0.45 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[CEP104]] | -0.43 | -0.30 / -0.45 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CACNA1D's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FMN1]] | B | FMN1 activity raises CACNA1D's level | lines that do not express FMN1 (17) vs lines expressing it (33) | 2.43× lower at baseline in the lines without FMN1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000278266, LINC02405, ENSG00000286016; maybe low, not absent |
| [[GABRA2]] | B | GABRA2 activity raises CACNA1D's level | lines that do not express GABRA2 (24) vs lines expressing it (26) | 1.79× lower at baseline in the lines without GABRA2 | 0.092 | ⚠ within organs, on part of the lines; also absent: LINC02253, ASXL3, ENSG00000257883; maybe low, not absent |
| [[HNF1A-AS1]] | C | HNF1A-AS1 activity raises CACNA1D's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 2.56× lower at baseline in the lines without HNF1A-AS1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent; co-absent with the target |
| [[GPX2]] | C | GPX2 activity raises CACNA1D's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 2.98× lower at baseline in the lines without GPX2 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31; co-absent with the target |
| [[CTNNA2]] | C | CTNNA2 activity raises CACNA1D's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 1.83× lower at baseline in the lines without CTNNA2 | 0.072 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FREM2]] | B | CACNA1D activity raises FREM2's level | lines that do not express CACNA1D (23) vs lines expressing it (27) | 1.87× lower at baseline in the lines without CACNA1D | 0.020 | ⚠ within organs, on part of the lines; also absent: TESC, ENSG00000291189, CDX2; maybe low, not absent |
| [[SORL1]] | B | CACNA1D activity raises SORL1's level | lines that do not express CACNA1D (23) vs lines expressing it (27) | 2.37× lower at baseline in the lines without CACNA1D | 0.048 | ⚠ within organs, on part of the lines; also absent: TESC, ENSG00000291189, CDX2; maybe low, not absent |
| [[FMN1]] | B | CACNA1D activity raises FMN1's level | lines that do not express CACNA1D (23) vs lines expressing it (27) | 1.82× lower at baseline in the lines without CACNA1D | 0.062 | ⚠ within organs, on part of the lines; also absent: TESC, ENSG00000291189, CDX2; maybe low, not absent |
| [[AK7]] | B | CACNA1D activity raises AK7's level | lines that do not express CACNA1D (23) vs lines expressing it (27) | 1.49× lower at baseline in the lines without CACNA1D | 0.074 | ⚠ within organs, on part of the lines; also absent: TESC, ENSG00000291189, CDX2; maybe low, not absent |
| cells under [[Riluzole hydrochloride (drug)]] 0.05 µM | B | CACNA1D activity raises the cells' numbers under Riluzole hydrochloride 0.05 µM (protects the cells) | lines that do not express CACNA1D (23) vs lines expressing it (25) | the lines without CACNA1D: 0.89× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: TESC, ENSG00000291189, CDX2; maybe low, not absent |
| [[LINC00578]] | B | CACNA1D activity raises LINC00578's level | lines that do not express CACNA1D (23) vs lines expressing it (27) | 1.65× lower at baseline in the lines without CACNA1D | 0.092 | ⚠ within organs, on part of the lines; also absent: TESC, ENSG00000291189, CDX2; maybe low, not absent |
| [[ENTREP2]] | C | CACNA1D activity raises ENTREP2's level | lines that do not express CACNA1D (23) vs lines expressing it (27) | 2.42× lower at baseline in the lines without CACNA1D | 0.037 | ⚠ within organs, on part of the lines; also absent: TESC, ENSG00000291189, CDX2; maybe low, not absent; co-absent with the target |
| [[KSR2]] | C | CACNA1D activity raises KSR2's level | lines that do not express CACNA1D (23) vs lines expressing it (27) | 2.78× lower at baseline in the lines without CACNA1D | 0.046 | ⚠ within organs, on part of the lines; also absent: TESC, ENSG00000291189, CDX2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.401). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.3, 36.6); signed map (44.7, 30.2). **Vector** length 79.5, 20.1% of its response variance represented; |z| ≥ 3 in 854 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.4 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.1 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.9 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +17.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +4.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.6 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +2.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.8 | -2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -6.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.5 | -6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -5.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -5.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | calcium voltage-gated channel subunit alpha1 D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:53,328,963-53,813,733 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Cav1.3, CACH3, CACN4; previously CCHL1A2, CACNL1A2 |
| Gene groups (HGNC) | Calcium voltage-gated channel alpha1 subunits |
| Reactome | 10 pathways, smallest: Adrenaline,noradrenaline inhibits insulin secretion; NCAM1 interactions; NCAM signaling for neurite out-growth |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01668](https://www.uniprot.org/uniprotkb/Q01668) (Voltage-dependent L-type calcium channel subunit alpha-1D):

> Voltage-sensitive calcium channels (VSCC) mediate the entry of calcium ions into excitable cells and are also involved in a variety of calcium-dependent processes, including muscle contraction, hormone or neurotransmitter release, gene expression, cell motility, cell division and cell death. The isoform alpha-1D gives rise to L-type calcium currents. Long-lasting (L-type) calcium channels belong to the 'high-voltage activated' (HVA) group. They are blocked by dihydropyridines (DHP), …

**Summary**, from NCBI Gene [776](https://www.ncbi.nlm.nih.gov/gene/776):

> Voltage-dependent calcium channels mediate the entry of calcium ions into excitable cells, and are also involved in a variety of calcium-dependent processes, including muscle contraction, hormone or neurotransmitter release, and gene expression. Calcium channels are multisubunit complexes composed of alpha-1, beta, alpha-2/delta, and gamma subunits. The channel activity is directed by the pore-forming alpha-1 subunit, whereas the others act as auxiliary subunits regulating this activity. The …

**Accessions** — [HGNC:1391](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1391) · Entrez [776](https://www.ncbi.nlm.nih.gov/gene/776) · UniProt [Q01668](https://www.uniprot.org/uniprotkb/Q01668) · Ensembl [ENSG00000157388](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157388)

## Data

Gene col 8066: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8066); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8066, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8066]; `tensor/DDL_lfc|DDL_z.npy` [8066]; `embed/gene_vectors.npy` [8066]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8066 or target_col == 8066). Every well: [[CACNA1D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACNA1D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
