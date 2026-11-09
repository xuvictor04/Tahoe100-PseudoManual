---
symbol: "PTPRG-AS1"
type: "gene"
col: 14277
ensembl_id: "ENSG00000241472"
name: "PTPRG antisense RNA 1"
location: "3p14.2"
module: 6
arm: "+"
pooled_cpm: 13.09
n_lines_expressing: 40
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# PTPRG-AS1

*PTPRG antisense RNA 1* — 3p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.67× (z +15.2, q 0e+00, up in 34 of 38 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.51× (z +14.2, q 3e-43, up in 36 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.458× (z -12.1, q 9e-31, down in 30 of 38 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRME1]] (+0.54, fdr 1e-05), [[TERT]] (+0.53, fdr 2e-05), [[DPY19L2P1]] (+0.51, fdr 2e-05); moves opposite to [[HOXB8]] (-0.49, fdr 1e-04), [[HOXB6]] (-0.48, fdr 2e-04), [[KPNA6]] (-0.48, fdr 4e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HOXB3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[C3orf14]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14277.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.67×** | +15.2 | 0e+00 | 34/38 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.51×** | +14.2 | 3e-43 | 36/38 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +12.7 | 6e-35 | 25/37 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +9.5 | 3e-19 | 27/38 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.84×** | +9.0 | 2e-17 | 9/19 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.78×** | +8.9 | 4e-17 | 21/32 (A498, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.73×** | +8.5 | 2e-15 | 27/37 (LOX-IMVI, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.62×** | +6.9 | 4e-10 | 10/27 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.50×** | +6.2 | 3e-08 | 22/37 (J82, NCI-H2347, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.36×** | +4.5 | 3e-04 | 14/37 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 0.002 | 16/36 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.21×** | +4.1 | 0.002 | 12/38 (J82, HS-578T, …) | top dose only | low cells (technical?) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.31×** | +4.0 | 0.003 | 13/37 (A-427, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.012 | 8/36 (C-33 A, SNU-423, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.040 | 13/37 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.087 | 2/37 (J82, SW480) | inconsistent across doses | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.099 | 5/35 (C32, Hs 766T, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14277.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.458×** | -12.1 | 9e-31 | 30/38 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.525×** | -10.0 | 7e-21 | 29/37 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.528×** | -9.9 | 1e-20 | 29/37 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.565×** | -8.8 | 1e-16 | 24/35 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.645×** | -6.8 | 1e-09 | 18/37 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.667×** | -6.3 | 4e-08 | 16/38 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.481×** | -5.9 | 3e-07 | 21/36 (HEC-1-A, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.732×** | -4.8 | 1e-04 | 16/37 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.562×** | -4.7 | 2e-04 | 15/36 (A-427, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.845× | -3.7 | 0.013 | 7/38 (HEC-1-A, SK-MEL-2, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.677×** | -3.2 | 0.082 | 9/34 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14277. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 29.5 | 2 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +13.9) | [[Digitoxin (drug)]] 5 µM 0.156× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -12.3) |
| [[PANC-1 (line)]] | alt | 26.8 | 2 (1 ⚠) | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.03× (z +9.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.96× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.215× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 24.2 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.245× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 37.9 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.163× (z -12.1) ⚠ toxic; cell-cycle shift, explains ~56% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.287× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 13.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +13.0) | [[Digitoxin (drug)]] 5 µM 0.261× (z -9.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 32.7 | 2 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.71× (z +10.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.24× (z +9.8) | [[TAK-901 (drug)]] 5 µM 0.0452× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 18.0 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.00× (z +12.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.67× (z +11.1) | — |
| [[A498 (line)]] | wt | 3.48 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 13.5× (z +10.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 8.88× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 16.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +10.6) | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0871× (z -10.4) |
| [[C-33 A (line)]] | alt | 57.2 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0478× (z -9.9) |
| [[H4 (line)]] | wt | 12.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -9.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Peretinoin (drug)]] 0.5 µM 0.0813× (z -9.5) |
| [[HOP62 (line)]] | alt | 21.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 10.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 8.41 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +10.8) | — |
| [[SW480 (line)]] | alt | 10.1 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.209× (z -10.6) |
| [[C32 (line)]] | wt | 33.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 9.62 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.183× (z -9.3) |
| [[SHP-77 (line)]] | alt | 28.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -9.4) |
| [[SW1417 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.222× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.21 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14277), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRME1]] | +0.54 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[TERT]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[DPY19L2P1]] | +0.51 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[MNS1]] | +0.50 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[ZNF678]] | +0.50 | +0.52 / +0.39 | both halves | 6e-05 |  |
| [[LINC01036]] | +0.50 | +0.30 / +0.60 | both halves | 2e-04 |  |
| [[LRRCC1]] | +0.50 | +0.40 / +0.51 | both halves | 4e-05 |  |
| [[CAMK4]] | +0.48 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[RNASEH2A]] | +0.48 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[SLFN11]] | +0.48 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[CD163L1]] | +0.48 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[BRCA2]] | +0.48 | +0.62 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXB8]] | -0.49 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[HOXB6]] | -0.48 | -0.50 / -0.29 | both halves | 2e-04 |  |
| [[KPNA6]] | -0.48 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ZNF174]] | -0.47 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[GAPVD1]] | -0.46 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[ZNF224]] | -0.45 | -0.50 / -0.22 | both halves | 6e-04 |  |
| [[AGAP3]] | -0.44 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[TTC9C]] | -0.43 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[UBTD1]] | -0.43 | -0.57 / -0.26 | both halves | 4e-04 |  |
| [[ZNF277]] | -0.43 | -0.55 / -0.24 | both halves | 4e-04 |  |
| [[SAP30L]] | -0.42 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[TMEM59]] | -0.41 | -0.37 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXB3]] | B | HOXB3 activity lowers PTPRG-AS1's level | lines that do not express HOXB3 (9) vs lines expressing it (41) | 1.64× higher at baseline in the lines without HOXB3 | 0.081 | ⚠ within organs, on part of the lines; also absent: HOXB6 |
| [[OLFM1]] | B | OLFM1 activity raises PTPRG-AS1's level | lines that do not express OLFM1 (27) vs lines expressing it (23) | 1.96× lower at baseline in the lines without OLFM1 | 0.089 | ⚠ within organs, on part of the lines; also absent: JPH3, DPYSL5, CHST8 |
| [[C3orf14]] | C | C3orf14 activity raises PTPRG-AS1's level | lines that do not express C3orf14 (12) vs lines expressing it (38) | 3.73× lower at baseline in the lines without C3orf14 | 0.007 | ⚠ within organs, on part of the lines; also absent: PTPRG-AS1, EVC, WIPF1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C3orf14]] | C | PTPRG-AS1 activity raises C3orf14's level | lines that do not express PTPRG-AS1 (10) vs lines expressing it (40) | 4.33× lower at baseline in the lines without PTPRG-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: C3orf14, RECK, PCLO; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.346). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-24.1, -45.9); signed map (-33.4, -51.0). **Vector** length 74.5, 14.5% of its response variance represented; |z| ≥ 3 in 958 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.6 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +5.3 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.3 | +9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +9.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.8 | +0.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +3.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -9.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.5 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.4 | -10.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -5.9 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -1.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | PTPRG antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p14.2 — chr3:62,221,249-62,369,406 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44638](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44638) · Entrez [100506994](https://www.ncbi.nlm.nih.gov/gene/100506994) · Ensembl [ENSG00000241472](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241472)

## Data

Gene col 14277: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14277); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14277, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14277]; `tensor/DDL_lfc|DDL_z.npy` [14277]; `embed/gene_vectors.npy` [14277]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14277 or target_col == 14277). Every well: [[PTPRG-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPRG-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
