---
symbol: "ATG2A"
type: "gene"
col: 3104
ensembl_id: "ENSG00000110046"
name: "autophagy related 2A"
location: "11q13.1"
module: 192
arm: "+"
pooled_cpm: 24.19
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 13
n_dd_up_clean: 20
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/192"]
generated_by: "tahoemap"
---

# ATG2A

*autophagy related 2A* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.90× (z +22.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.525× (z -9.3, q 6e-18, down in 28 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.517× (z -5.0, q 7e-05, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC34]] (+0.70, fdr 7e-06), [[ABTB1]] (+0.66, fdr 3e-05), [[NOSIP]] (+0.64, fdr 2e-05); moves opposite to [[MANEA]] (-0.61, fdr 1e-05), [[HNRNPR]] (-0.57, fdr 1e-05), [[SUCLG2]] (-0.55, fdr 1e-04).
> It is in [[Module 192]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3104.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.90×** | +22.9 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.28×** | +20.9 | 0e+00 | 48/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.95×** | +19.8 | 0e+00 | 47/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +14.1 | 4e-43 | 38/47 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.32×** | +12.1 | 2e-31 | 39/47 (SW480, KATO III, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **2.12×** | +10.8 | 4e-25 | 44/47 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +9.6 | 4e-20 | 40/47 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.79×** | +8.4 | 5e-15 | 36/48 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.71×** | +7.7 | 8e-13 | 32/48 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.66×** | +7.3 | 2e-11 | 32/47 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.64×** | +7.1 | 5e-11 | 28/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +6.8 | 6e-10 | 30/47 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +6.5 | 3e-09 | 22/47 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.7 | 5e-07 | 26/47 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +4.2 | 0.001 | 17/48 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.004 | 21/48 (PANC-1, LOX-IMVI, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3104.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.525×** | -9.3 | 6e-18 | 28/40 (LS 180, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.552×** | -8.6 | 2e-15 | 33/47 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -7.4 | 4e-11 | 21/32 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.647×** | -5.8 | 7e-07 | 24/36 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.517×** | -5.0 | 7e-05 | 26/47 (NCI-H1792, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.592×** | -4.0 | 0.007 | 18/46 (AsPC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.774×** | -3.6 | 0.028 | 20/47 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.791×** | -3.4 | 0.045 | 15/49 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.779×** | -3.4 | 0.047 | 17/47 (AsPC-1, COLO 205, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.648×** | -3.3 | 0.054 | 14/48 (AsPC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.791×** | -3.3 | 0.054 | 17/47 (CFPAC-1, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.817×** | -3.1 | 0.077 | 13/48 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.862× | -3.1 | 0.083 | 9/48 (SW480, CFPAC-1, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.810×** | -3.1 | 0.083 | 12/47 (Hs 766T, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3104. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 18.6 | 8 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 7.03× (z +13.8) | — |
| [[CFPAC-1 (line)]] | alt | 42.3 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.4) | [[venetoclax (drug)]] 5 µM 0.0231× (z -15.8) |
| [[LS 180 (line)]] | wt | 24.5 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.22× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 31.4 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +17.8) | — |
| [[SW480 (line)]] | alt | 29.6 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.81× (z +18.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.387× (z -8.5) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 28.1 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.94× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.133× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 11.0 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.74× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -8.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 44.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 5.40× (z +12.9) | — |
| [[A-172 (line)]] | wt | 12.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.00× (z +9.7) | — |
| [[A549 (line)]] | wt | 24.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.40× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.170× (z -10.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 31.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +13.2) | — |
| [[J82 (line)]] | alt | 21.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +13.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 42.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0618× (z -20.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 16.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.66× (z +13.9) | — |
| [[SW1417 (line)]] | alt | 45.7 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.64× (z +14.1) | — |
| [[A-427 (line)]] | wt | 19.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.70× (z +13.3) | — |
| [[A498 (line)]] | wt | 10.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 15.9 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.84× (z +11.8) | — |
| [[Hs 766T (line)]] | wt | 27.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.84× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 15.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.99× (z +11.9) | — |
| [[LoVo (line)]] | wt | 22.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.35× (z +15.7) | — |
| [[LOX-IMVI (line)]] | wt | 17.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.64× (z +14.0) | — |
| [[RKO (line)]] | wt | 41.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +13.2) | — |
| [[AsPC-1 (line)]] | alt | 42.1 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.156× (z -12.6) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 12.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.08× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 33.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0631× (z -18.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -10.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 26.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 30.9 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.10× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -9.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3104), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC34]] | +0.70 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ABTB1]] | +0.66 | +0.44 / +0.71 | both halves | 3e-05 |  |
| [[NOSIP]] | +0.64 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[MEF2D]] | +0.64 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[PGPEP1]] | +0.64 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[BAIAP3]] | +0.64 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[MIDN]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[FRMD8]] | +0.62 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[PLIN3]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ZSWIM4]] | +0.61 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[PLEKHM1P1]] | +0.60 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[FAM89B]] | +0.59 | +0.35 / +0.61 | both halves | 1e-04 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MANEA]] | -0.61 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[HNRNPR]] | -0.57 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[SUCLG2]] | -0.55 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[SMG7]] | -0.55 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[NUP205]] | -0.54 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[ATP5PB]] | -0.54 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[RAB11FIP2]] | -0.54 | -0.37 / -0.52 | both halves | 9e-05 |  |
| [[SNX5]] | -0.54 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[PRTFDC1]] | -0.54 | -0.37 / -0.48 | both halves | 9e-05 |  |
| [[TRUB1]] | -0.54 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[FUBP1]] | -0.54 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[RNASEH2B]] | -0.53 | -0.40 / -0.47 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises ATG2A's level | compounds that target MAP2K1: 3 of 4 lower it (Cobimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 192]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.50; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.3, -43.9); signed map (-20.8, 12.6). **Vector** length 105, 28.2% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.8 | +12.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +5.3 | +3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.7 | +20.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.6 | +10.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +19.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +3.4 | +1.6 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +3.1 | +1.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +3.1 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.7 | -8.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.8 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.3 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.2 | -2.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -4.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | autophagy related 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,894,546-64,917,209 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0404, BLTP4A |
| Gene groups (HGNC) | Autophagy related; MicroRNA protein coding host genes; Bridge-like lipid transfer protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2TAZ0](https://www.uniprot.org/uniprotkb/Q2TAZ0) (Autophagy-related protein 2 homolog A):

> Lipid transfer protein involved in autophagosome assembly. Tethers the edge of the isolation membrane (IM) to the endoplasmic reticulum (ER) and mediates direct lipid transfer from ER to IM for IM expansion. Binds to the ER exit site (ERES), which is the membrane source for autophagosome formation, and extracts phospholipids from the membrane source and transfers them to ATG9 (ATG9A or ATG9B) to the IM for membrane expansion. Lipid transfer activity is enhanced by WIPI1 and WDR45/WIPI4, which …

**Summary**, from NCBI Gene [23130](https://www.ncbi.nlm.nih.gov/gene/23130):

> Enables lipid transfer activity. Involved in autophagosome assembly and positive regulation of autophagosome assembly. Is active in organelle membrane contact site. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29028](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29028) · Entrez [23130](https://www.ncbi.nlm.nih.gov/gene/23130) · UniProt [Q2TAZ0](https://www.uniprot.org/uniprotkb/Q2TAZ0) · Ensembl [ENSG00000110046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110046)

## Data

Gene col 3104: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3104); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3104, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3104]; `tensor/DDL_lfc|DDL_z.npy` [3104]; `embed/gene_vectors.npy` [3104]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3104 or target_col == 3104). Every well: [[ATG2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATG2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
