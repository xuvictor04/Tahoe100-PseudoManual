---
symbol: "SGO1-AS1"
type: "gene"
col: 13790
ensembl_id: "ENSG00000231304"
name: "SGO1 antisense RNA 1"
location: "3p24.3"
module: 26
arm: "+"
pooled_cpm: 26.2
n_lines_expressing: 49
n_dd_up: 45
n_dd_down: 30
n_dd_up_clean: 42
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# SGO1-AS1

*SGO1 antisense RNA 1* — 3p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.56× (z +34.1, q 0e+00, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.415× (z -11.3, q 9e-27, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRGAP3]] (+0.74, fdr 7e-06), [[CFAP418-AS1]] (+0.73, fdr 7e-06), [[LINC01135]] (+0.72, fdr 1e-05); moves opposite to [[HERC2P9]] (-0.72, fdr 7e-06), [[GTF2E2]] (-0.70, fdr 1e-05), [[IQCB1]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC00504]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 3 with an alert ⚠; shown: the 15 strongest. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13790.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.56×** | +34.1 | 0e+00 | 46/46 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.17×** | +25.9 | 0e+00 | 43/45 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.59×** | +16.3 | 0e+00 | 37/42 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.30×** | +14.7 | 0e+00 | 39/46 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.81×** | +12.7 | 7e-35 | 36/46 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.99×** | +12.4 | 2e-33 | 40/46 (SK-MEL-2, KATO III, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.65×** | +12.0 | 2e-31 | 36/46 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.31×** | +10.7 | 7e-25 | 32/45 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +10.4 | 1e-23 | 35/47 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.78×** | +10.4 | 1e-23 | 33/47 (A-172, SW1417, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.17×** | +9.9 | 3e-21 | 34/47 (SK-MEL-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.93×** | +8.4 | 2e-15 | 35/47 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.90×** | +7.9 | 2e-13 | 30/46 (HEC-1-A, C32, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +7.8 | 2e-13 | 26/46 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.78×** | +7.4 | 5e-12 | 30/45 (SK-MEL-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13790.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.415×** | -11.3 | 9e-27 | 36/46 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.511×** | -8.6 | 2e-15 | 30/46 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.524×** | -8.3 | 2e-14 | 29/45 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.525×** | -8.3 | 2e-14 | 29/46 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.553×** | -7.6 | 3e-12 | 25/46 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.557×** | -7.5 | 5e-12 | 30/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.544×** | -7.5 | 5e-12 | 25/41 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.540×** | -7.5 | 6e-12 | 30/46 (NCI-H1573, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.568×** | -7.3 | 2e-11 | 27/46 (SW 900, NCI-H23, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.611×** | -6.3 | 1e-08 | 26/46 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.404×** | -6.1 | 6e-08 | 22/43 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.719×** | -6.0 | 9e-08 | 25/47 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.643×** | -5.7 | 6e-07 | 26/45 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.685×** | -4.9 | 5e-05 | 21/47 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.497×** | -4.7 | 1e-04 | 19/46 (NCI-H1573, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.710×** | -4.4 | 4e-04 | 19/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Vilanterol (drug)]] 5 µM |  | **0.805×** | -3.9 | 0.003 | 17/47 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.742×** | -3.7 | 0.006 | 15/45 (HT-29, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13790. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 26.0 | 11 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.4× (z +28.2) | — |
| [[NCI-H1573 (line)]] | alt | 68.6 | 1 | 10 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.5) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.182× (z -13.7) |
| [[SW480 (line)]] | alt | 18.1 | 5 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.81× (z +18.9) | [[Digitoxin (drug)]] 5 µM 0.237× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -8.5) |
| [[COLO 205 (line)]] | alt | 35.7 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0432× (z -16.8) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0796× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 78.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +16.5) | — |
| [[KATO III (line)]] | alt | 14.3 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 5.05× (z +11.4) | — |
| [[LoVo (line)]] | wt | 18.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +24.3) | — |
| [[NCI-H23 (line)]] | alt | 37.7 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.04× (z +18.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.214× (z -9.2) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 87.4 | 5 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.27× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.155× (z -13.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 35.4 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 6.30× (z +10.9) | [[Ixazomib citrate (drug)]] 5 µM 0.213× (z -9.2) |
| [[HOP62 (line)]] | alt | 26.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.00× (z +18.2) | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +19.8) | — |
| [[PANC-1 (line)]] | alt | 17.1 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 27.9× (z +30.9) | [[Ixazomib citrate (drug)]] 5 µM 0.207× (z -10.3) |
| [[RKO (line)]] | wt | 10.1 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.95× (z +13.1) | — |
| [[HCT15 (line)]] | alt | 33.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +17.4) | — |
| [[NCI-H460 (line)]] | wt | 8.61 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.59× (z +18.1) | — |
| [[Panc 03.27 (line)]] | alt | 54.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.25× (z +16.5) | [[Digitoxin (drug)]] 5 µM 0.267× (z -8.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 13.2 | 3 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 4.93× (z +10.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 8.88× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 8.86 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +14.2) | — |
| [[LS 180 (line)]] | wt | 34.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.01× (z +18.7) | — |
| [[NCI-H2030 (line)]] | alt | 19.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +20.2) | — |
| [[SNU-423 (line)]] | alt | 18.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +16.1) | — |
| [[SW1417 (line)]] | alt | 18.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +12.0) | — |
| [[BT-474 (line)]] | alt | 8.50 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +12.9) | — |
| [[CFPAC-1 (line)]] | alt | 12.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +12.6) | — |
| [[HepG2_C3A (line)]] | wt | 11.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.17× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 14.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +15.9) | — |
| [[SW 900 (line)]] | alt | 41.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.211× (z -8.9) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 15.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.0× (z +15.2) | — |
| [[AsPC-1 (line)]] | alt | 7.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +12.0) | — |
| [[C-33 A (line)]] | alt | 23.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +10.9) | — |
| [[C32 (line)]] | wt | 95.9 | 1 | 0 | [[Cobimetinib (drug)]] 0.5 µM 4.90× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 15.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 29.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.90× (z +15.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.41× (z +11.9) | — |
| [[RPMI-7951 (line)]] | alt | 23.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.37× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 8.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.74× (z +10.2) | — |
| [[SW 1271 (line)]] | alt | 80.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +11.5) | — |
| [[A549 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 90.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.43 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13790), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGAP3]] | +0.74 | +0.84 / +0.63 | both halves | 7e-06 |  |
| [[CFAP418-AS1]] | +0.73 | +0.78 / +0.70 | both halves | 7e-06 | same gene group |
| [[LINC01135]] | +0.72 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[CHODL]] | +0.71 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[PDCL3P4]] | +0.71 | +0.85 / +0.52 | both halves | 1e-05 |  |
| [[AK9]] | +0.71 | +0.81 / +0.61 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.70 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[UNC79]] | +0.70 | +0.79 / +0.58 | both halves | 7e-06 |  |
| [[CGGBP1]] | +0.70 | +0.80 / +0.46 | both halves | 3e-05 |  |
| [[PCNX4-DT]] | +0.70 | +0.84 / +0.51 | both halves | 1e-05 |  |
| [[SLC38A4-AS1]] | +0.70 | +0.70 / +0.63 | both halves | 7e-06 | same gene group |
| [[PKN2-AS1]] | +0.70 | +0.83 / +0.53 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2P9]] | -0.72 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[GTF2E2]] | -0.70 | -0.75 / -0.52 | both halves | 1e-05 |  |
| [[IQCB1]] | -0.69 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[HERC2P2]] | -0.68 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[HERC2P3]] | -0.67 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[FAM20B]] | -0.67 | -0.71 / -0.59 | both halves | 7e-06 |  |
| [[TAF5L]] | -0.66 | -0.71 / -0.59 | both halves | 7e-06 |  |
| [[PACC1]] | -0.66 | -0.68 / -0.35 | both halves | 1e-04 |  |
| [[WDR5]] | -0.66 | -0.69 / -0.56 | both halves | 1e-05 |  |
| [[ANKS6]] | -0.66 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[ZNF496]] | -0.65 | -0.72 / -0.55 | both halves | 1e-05 |  |
| [[HSF1]] | -0.65 | -0.77 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00504]] | B | LINC00504 activity raises SGO1-AS1's level | lines that do not express LINC00504 (31) vs lines expressing it (19) | 1.85× lower at baseline in the lines without LINC00504 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC02930, ENSG00000287474 |
| [[TOP2A]] | B | TOP2A activity lowers SGO1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MIR583HG]] | B | MIR583HG activity raises SGO1-AS1's level | lines that do not express MIR583HG (10) vs lines expressing it (40) | 1.98× lower at baseline in the lines without MIR583HG | 0.080 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RGS17, GNAI1, KLF12; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.674). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.7, 15.4); signed map (26.3, 1.0). **Vector** length 102, 28.9% of its response variance represented; |z| ≥ 3 in 1,487 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.9 | +34.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.4 | +14.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.2 | +16.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.1 | +10.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.5 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +12.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.5 | +7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +10.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.5 | -7.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.4 | -8.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.8 | -11.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.6 | -7.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.3 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -7.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.4 | -6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.9 | -5.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -3.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | SGO1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p24.3 — chr3:20,174,244-21,145,967 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously SGOL1-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41081](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41081) · Entrez [100874028](https://www.ncbi.nlm.nih.gov/gene/100874028) · Ensembl [ENSG00000231304](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231304)

## Data

Gene col 13790: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13790); `tables/drug_effects.parquet` (75 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13790, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13790]; `tensor/DDL_lfc|DDL_z.npy` [13790]; `embed/gene_vectors.npy` [13790]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13790 or target_col == 13790). Every well: [[SGO1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGO1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
