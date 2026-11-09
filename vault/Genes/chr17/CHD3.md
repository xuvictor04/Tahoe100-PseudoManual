---
symbol: "CHD3"
type: "gene"
col: 9891
ensembl_id: "ENSG00000170004"
name: "chromodomain helicase DNA binding protein 3"
location: "17p13.1"
module: 173
arm: "+"
pooled_cpm: 82.14
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# CHD3

*chromodomain helicase DNA binding protein 3* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.75× (z +18.6, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.77× (z +14.8, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.478× (z -13.6, q 3e-39, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED12]] (+0.70, fdr 1e-05), [[AKT1S1]] (+0.67, fdr 2e-05), [[ARFGAP2]] (+0.66, fdr 2e-05); moves opposite to [[MRPL41]] (-0.66, fdr 1e-05, ⚠ MRPL41 in the vector space only through flagged drug-doses), [[SNU13]] (-0.65, fdr 1e-05), [[ANTKMT]] (-0.63, fdr 6e-05), [[NPM3]] (-0.63, fdr 7e-05).
> It is in [[Module 173]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9891.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.75×** | +18.6 | 0e+00 | 48/49 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +17.2 | 0e+00 | 41/43 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +14.8 | 0e+00 | 39/48 (RPMI-7951, A498, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +12.6 | 3e-34 | 40/45 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +8.9 | 6e-17 | 38/49 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +6.6 | 3e-09 | 35/48 (A-172, C32, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.23×** | +4.6 | 4e-04 | 30/48 (NCI-H23, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.25×** | +4.5 | 4e-04 | 29/50 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.26×** | +4.4 | 8e-04 | 23/49 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.003 | 24/47 (NCI-H23, A549, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.0 | 0.004 | 20/48 (AsPC-1, LoVo, …) | rises with dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.009 | 24/50 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.010 | 25/48 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.014 | 17/48 (J82, NCI-H460, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.018 | 16/47 (MIA PaCa-2, NCI-H23, …) | rises with dose | position effect removed |
| [[RMC-6236 (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.061 | 15/48 (NCI-H23, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +3.1 | 0.062 | 18/47 (HOP62, NCI-H23, …) | rises with dose | position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.093 | 12/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.14× | +2.9 | 0.097 | 14/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9891.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.478×** | -13.6 | 3e-39 | 45/48 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.485×** | -13.3 | 6e-38 | 44/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.515×** | -12.2 | 6e-32 | 44/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.657×** | -7.7 | 2e-12 | 40/48 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.702×** | -6.5 | 9e-09 | 41/48 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.764×** | -4.9 | 7e-05 | 38/49 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.618×** | -4.6 | 3e-04 | 31/48 (SNU-1, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.872× | -3.6 | 0.027 | 16/48 (LOX-IMVI, SW 900, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.702×** | -3.4 | 0.043 | 24/49 (Hs 766T, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.833×** | -3.3 | 0.047 | 15/49 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.840× | -3.2 | 0.070 | 13/49 (LoVo, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9891. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 77.5 | 5 (4 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +17.6) | [[Panobinostat (drug)]] 0.5 µM 0.291× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 115 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +10.5) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.341× (z -12.3) |
| [[A498 (line)]] | wt | 122 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +23.1) | — |
| [[HS-578T (line)]] | alt | 99.4 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +20.4) | — |
| [[J82 (line)]] | alt | 85.0 | 4 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.07× (z +15.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.2) | [[Belinostat (drug)]] 5 µM 0.397× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 107 | 4 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +20.4) | [[Belinostat (drug)]] 5 µM 0.362× (z -12.2) |
| [[A-172 (line)]] | wt | 151 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +16.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.8) | — |
| [[KATO III (line)]] | alt | 68.8 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +10.5) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.313× (z -12.1) |
| [[RKO (line)]] | wt | 82.1 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 5.18× (z +15.4) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.315× (z -10.9) |
| [[A549 (line)]] | wt | 104 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +17.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.70× (z +16.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 48.6 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +12.3) | — |
| [[PANC-1 (line)]] | alt | 74.6 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +18.5) | [[Panobinostat (drug)]] 5 µM 0.536× (z -8.7) |
| [[C32 (line)]] | wt | 106 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.85× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 112 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +15.9) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.459× (z -10.4) |
| [[HOP62 (line)]] | alt | 74.6 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +22.8) | — |
| [[Hs 766T (line)]] | wt | 81.1 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.424× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 86.7 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +18.1) | — |
| [[NCI-H2347 (line)]] | alt | 85.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 117 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.277× (z -10.8) |
| [[LS 180 (line)]] | wt | 57.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.88× (z +12.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 39.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +18.2) | — |
| [[NCI-H2030 (line)]] | alt | 56.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 114 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +10.4) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.411× (z -8.8) |
| [[SW480 (line)]] | alt | 55.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +11.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 44.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +11.1) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 86.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +9.8) ⚠ toxic; transcription drop | [[Niclosamide (olamine) (drug)]] 5 µM 0.329× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 85.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.369× (z -10.2) |
| [[HT-29 (line)]] | alt | 56.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 102 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.9) | — |
| [[RPMI-7951 (line)]] | alt | 60.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.34× (z +25.0) | — |
| [[SK-MEL-2 (line)]] | alt | 32.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.87× (z +18.3) | — |
| [[SNU-423 (line)]] | alt | 75.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.0) | — |
| [[SW48 (line)]] | wt | 50.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +15.3) | — |
| [[A-427 (line)]] | wt | 56.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +9.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 202 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.302× (z -9.5) |
| [[BT-474 (line)]] | alt | 119 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.382× (z -10.5) |
| [[H4 (line)]] | wt | 63.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +9.8) | — |
| [[HepG2_C3A (line)]] | wt | 41.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.54× (z +16.7) | — |
| [[hTERT-HPNE (line)]] | wt | 115 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 87.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +10.0) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 86.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9891), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED12]] | +0.70 | +0.68 / +0.50 | both halves | 1e-05 | pathway: Adipogenesis |
| [[AKT1S1]] | +0.67 | +0.60 / +0.46 | both halves | 2e-05 | pathway: Intracellular signaling by second messengers |
| [[ARFGAP2]] | +0.66 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[THBS3]] | +0.65 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[VPS52]] | +0.64 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ATN1]] | +0.64 | +0.43 / +0.59 | both halves | 3e-05 | pathway: Intracellular signaling by second messengers; STRING 606 |
| [[UBAP2L]] | +0.63 | +0.52 / +0.49 | both halves | 1e-05 | same gene group |
| [[HFE]] | +0.62 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[PLA2G6]] | +0.62 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[GIPC2]] | +0.61 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[HMGN2]] | +0.61 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[DHX38]] | +0.61 | +0.54 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL41]] ⚠ | -0.66 | -0.49 / -0.56 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNU13]] | -0.65 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[ANTKMT]] | -0.63 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[NPM3]] | -0.63 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[ANKS6]] | -0.62 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[POP7]] | -0.61 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[CCNQ]] | -0.61 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[TRIM35]] | -0.61 | -0.52 / -0.40 | both halves | 4e-05 |  |
| [[PUSL1]] | -0.60 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[TMEM147]] | -0.59 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[TMEM120B]] | -0.59 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[NAA10]] ⚠ | -0.59 | -0.42 / -0.39 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MPG]] | -0.57 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[ANAPC11]] | -0.57 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers CHD3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[HDAC6]] | B | HDAC6 activity raises CHD3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-10.1, 5.2); signed map (16.7, -21.9). **Vector** length 137, 43.2% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.9 | +14.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +17.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +18.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.0 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +6.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.5 | +4.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +5.5 | +3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.3 | +4.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -7.8 | -13.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.0 | -12.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.9 | -13.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.7 | -7.7 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -4.0 | -4.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -3.7 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.6 | -2.3 |
|  | [[vincristine (drug)]] 0.05 µM |  | -2.9 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | chromodomain helicase DNA binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,884,796-7,912,760 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Mi-2a, ZFH, Mi2-ALPHA |
| Gene groups (HGNC) | PHD finger proteins; SNF2 related family; NuRD complex subunits; Small nucleolar RNA protein coding host genes |
| Reactome | 34 pathways, smallest: Transcriptional regulation of brown and beige adipocyte differentiation; Transcriptional regulation of brown and beige adipocyte differentiation by EBF2; ERCC6 (CSB) and EHMT2 (G9a) positively regulate rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12873](https://www.uniprot.org/uniprotkb/Q12873) (ATP-dependent chromatin remodeler CHD3):

> ATP-dependent chromatin-remodeling factor that binds and distorts nucleosomal DNA. Acts as a component of the histone deacetylase NuRD complex which participates in the remodeling of chromatin. Involved in transcriptional repression as part of the NuRD complex. Required for anchoring centrosomal pericentrin in both interphase and mitosis, for spindle organization and centrosome integrity.

**Summary**, from NCBI Gene [1107](https://www.ncbi.nlm.nih.gov/gene/1107):

> This gene encodes a member of the CHD family of proteins which are characterized by the presence of chromo (chromatin organization modifier) domains and SNF2-related helicase/ATPase domains. This protein is one of the components of a histone deacetylase complex referred to as the Mi-2/NuRD complex which participates in the remodeling of chromatin by deacetylating histones. Chromatin remodeling is essential for many processes including transcription. Autoantibodies against this protein are found …

**Accessions** — [HGNC:1918](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1918) · Entrez [1107](https://www.ncbi.nlm.nih.gov/gene/1107) · UniProt [Q12873](https://www.uniprot.org/uniprotkb/Q12873) · Ensembl [ENSG00000170004](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170004)

## Data

Gene col 9891: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9891); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9891, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9891]; `tensor/DDL_lfc|DDL_z.npy` [9891]; `embed/gene_vectors.npy` [9891]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9891 or target_col == 9891). Every well: [[CHD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
