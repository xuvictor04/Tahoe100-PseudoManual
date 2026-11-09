---
symbol: "CRYZL2P"
type: "gene"
col: 14305
ensembl_id: "ENSG00000242193"
name: "crystallin zeta like 2, pseudogene"
location: "1q25.2"
module: 8
arm: "+"
pooled_cpm: 7.55
n_lines_expressing: 36
n_dd_up: 20
n_dd_down: 33
n_dd_up_clean: 13
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 9
direction_downstream: 7
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# CRYZL2P

*crystallin zeta like 2, pseudogene* — 1q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.52× (z +8.7, q 3e-15, up in 7 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 1.55× (z +4.1, q 0.009, up in 10 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.175× (z -24.0, q 0e+00, down in 26 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC16B]] (+0.76, fdr 7e-06, ⚠ same locus), [[LY75]] (+0.65, fdr 7e-06), [[DHX15]] (+0.61, fdr 3e-05), [[PLA2R1]] (+0.55, fdr 2e-05); moves opposite to [[ZXDC]] (-0.48, fdr 5e-05), [[DNAJB2]] (-0.48, fdr 1e-04), [[NKAP]] (-0.46, fdr 4e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[RNF128]] → it (grade B ⚠); 7 go from it, the strongest it → [[PLA2R1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14305.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.52×** | +8.7 | 3e-15 | 7/10 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.47×** | +5.3 | 3e-05 | 15/34 (LS 180, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.55×** | +4.1 | 0.009 | 10/34 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.53×** | +3.8 | 0.015 | 13/32 (LS 180, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.51×** | +3.8 | 0.015 | 9/34 (CFPAC-1, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Arbutin (drug)]] 0.5 µM |  | **1.49×** | +3.8 | 0.015 | 7/34 (PANC-1, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.023 | 10/34 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.29×** | +3.5 | 0.036 | 5/34 (COLO 205, SW1417, …) | all doses, flat |  |
| [[Folic acid (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.074 | 3/34 (COLO 205, SW1417, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.39×** | +3.2 | 0.074 | 4/34 (NCI-H2030, A498, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.075 | 8/34 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +3.1 | 0.075 | 5/34 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.075 | 9/34 (SK-MEL-2, A498, …) | inconsistent across doses | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.075 | 2/34 (CFPAC-1, SW48) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.075 | 2/34 (CFPAC-1, PANC-1) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.085 | 4/34 (AsPC-1, NCI-H1792, …) | top dose only |  |
| [[Anethole trithione (drug)]] 0.05 µM |  | **1.36×** | +3.0 | 0.085 | 4/34 (SW1417, NCI-H2347, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.087 | 8/34 (COLO 205, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14305.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.175×** | -24.0 | 0e+00 | 26/30 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.243×** | -13.7 | 2e-40 | 33/34 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.265×** | -12.9 | 6e-36 | 25/30 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.261×** | -12.6 | 5e-34 | 29/33 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.314×** | -11.3 | 2e-27 | 32/33 (LS 180, COLO 205, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.356×** | -9.7 | 2e-20 | 27/33 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.377×** | -9.5 | 2e-19 | 27/34 (SW1417, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.409×** | -8.7 | 2e-16 | 27/33 (RPMI-7951, SW1417, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.412×** | -8.6 | 4e-16 | 25/34 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.438×** | -8.0 | 7e-14 | 26/33 (PANC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.446×** | -7.4 | 7e-12 | 23/34 (HepG2/C3A, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.613×** | -6.7 | 9e-10 | 22/33 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.537×** | -6.0 | 7e-08 | 22/33 (HEC-1-A, RPMI-7951, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.529×** | -6.0 | 1e-07 | 19/30 (Panc 03.27, COLO 205, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.548×** | -5.8 | 2e-07 | 19/32 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.566×** | -5.5 | 1e-06 | 19/34 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.702×** | -4.9 | 4e-05 | 15/34 (COLO 205, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14305. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 50.9 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0123× (z -28.6) |
| [[PANC-1 (line)]] | alt | 15.7 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.0647× (z -26.6) |
| [[NCI-H460 (line)]] | wt | 6.25 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0931× (z -15.1) |
| [[KATO III (line)]] | alt | 17.9 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0919× (z -16.7) |
| [[HepG2_C3A (line)]] | wt | 9.13 | 0 | 5 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0430× (z -9.9) |
| [[HT-29 (line)]] | alt | 21.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0327× (z -22.0) |
| [[SW1417 (line)]] | alt | 12.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0584× (z -14.9) |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0648× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.165× (z -11.8) |
| [[A-172 (line)]] | wt | 5.96 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0881× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.188× (z -8.9) |
| [[HOP62 (line)]] | alt | 3.70 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0270× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 16.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -13.1) |
| [[A-427 (line)]] | wt | 12.8 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.160× (z -8.9) |
| [[A498 (line)]] | wt | 10.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0896× (z -18.6) |
| [[A549 (line)]] | wt | 6.15 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0605× (z -18.4) |
| [[HEC-1-A (line)]] | alt | 9.23 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -14.8) |
| [[RPMI-7951 (line)]] | alt | 8.44 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0414× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -12.3) |
| [[NCI-H2347 (line)]] | alt | 5.24 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -13.8) |
| [[SK-MEL-2 (line)]] | alt | 9.92 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -11.0) |
| [[SW 900 (line)]] | alt | 5.34 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0776× (z -11.1) |
| [[AN3 CA (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.704 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.799 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.650 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.745 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.720 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.53 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14305), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC16B]] | +0.76 | +0.81 / +0.66 | both halves | 7e-06 | ⚠ same locus (23.8 kb, same strand: neighbours can correlate without regulation) |
| [[LY75]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[DHX15]] | +0.61 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[PLA2R1]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[MANSC1]] | +0.54 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[GABRP]] | +0.54 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[PRTFDC1]] | +0.54 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[ARSL]] | +0.53 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[SORL1]] | +0.53 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[ALDH5A1]] | +0.53 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[VILL]] | +0.53 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[ST6GALNAC1]] | +0.52 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[UNG]] | +0.52 | +0.38 / +0.58 | both halves | 6e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDC]] | -0.48 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[DNAJB2]] | -0.48 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[NKAP]] | -0.46 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[MSX1]] | -0.46 | -0.42 / -0.37 | both halves | 7e-05 |  |
| [[PPFIA1]] | -0.46 | -0.37 / -0.55 | both halves | 9e-05 |  |
| [[PPP2R5B]] | -0.46 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[FAM219A]] | -0.46 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[NPHP3]] | -0.45 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[DLGAP4]] | -0.44 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[LRSAM1]] | -0.44 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[NPIPP1]] | -0.44 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[SNHG32]] | -0.43 | -0.36 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF128]] | B | RNF128 activity raises CRYZL2P's level | lines that do not express RNF128 (23) vs lines expressing it (27) | 2.45× lower at baseline in the lines without RNF128 | 0.013 | ⚠ within organs, on part of the lines; also absent: AZGP1, RNF43, PROM1 |
| [[PLA2R1]] | B | PLA2R1 activity raises CRYZL2P's level | lines that do not express PLA2R1 (19) vs lines expressing it (31) | 1.79× lower at baseline in the lines without PLA2R1 | 0.043 | ⚠ within organs, on part of the lines; also absent: CYP2S1, RARRES1, IL18 |
| [[LY75]] | B | LY75 activity raises CRYZL2P's level | lines that do not express LY75 (30) vs lines expressing it (20) | 1.90× lower at baseline in the lines without LY75 | 0.055 | ⚠ within organs, on part of the lines; also absent: IL20RA, TINAGL1, CARD11 |
| [[TCN1]] | B | TCN1 activity raises CRYZL2P's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 2.23× lower at baseline in the lines without TCN1 | 0.058 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[MUC5B]] | B | MUC5B activity raises CRYZL2P's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 2.18× lower at baseline in the lines without MUC5B | 0.085 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[MAP2K6]] | B | MAP2K6 activity raises CRYZL2P's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 1.74× lower at baseline in the lines without MAP2K6 | 0.086 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[LYZ]] | B | LYZ activity raises CRYZL2P's level | lines that do not express LYZ (40) vs lines expressing it (10) | 2.76× lower at baseline in the lines without LYZ | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17 |
| [[SEC16B]] | C | SEC16B activity raises CRYZL2P's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 4.22× lower at baseline in the lines without SEC16B | 4e-04 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3; co-absent with the target |
| [[ERBB2]] | C | ERBB2 activity raises CRYZL2P's level | lines that do not express ERBB2 (3) vs lines expressing it (47) | 3.23× lower at baseline in the lines without ERBB2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: UGDH, IQSEC2, APOBEC3F; its own permutation p |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLA2R1]] | B | CRYZL2P activity raises PLA2R1's level | lines that do not express CRYZL2P (14) vs lines expressing it (36) | 2.81× lower at baseline in the lines without CRYZL2P | 0.032 | ⚠ within organs, on part of the lines; also absent: SEC16B |
| [[LY75]] | B | CRYZL2P activity raises LY75's level | lines that do not express CRYZL2P (14) vs lines expressing it (36) | 2.50× lower at baseline in the lines without CRYZL2P | 0.045 | ⚠ within organs, on part of the lines; also absent: SEC16B |
| cells under [[PH-797804 (drug)]] 0.05 µM | B | CRYZL2P activity lowers the cells' numbers under PH-797804 0.05 µM (makes them more sensitive) | lines that do not express CRYZL2P (14) vs lines expressing it (34) | the lines without CRYZL2P: 1.20× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: SEC16B |
| [[HNMT]] | B | CRYZL2P activity raises HNMT's level | lines that do not express CRYZL2P (14) vs lines expressing it (36) | 2.34× lower at baseline in the lines without CRYZL2P | 0.065 | ⚠ within organs, on part of the lines; also absent: SEC16B |
| [[MYOM3]] | B | CRYZL2P activity raises MYOM3's level | lines that do not express CRYZL2P (14) vs lines expressing it (36) | 1.89× lower at baseline in the lines without CRYZL2P | 0.074 | ⚠ within organs, on part of the lines; also absent: SEC16B |
| cells under [[Ipatasertib (drug)]] 0.5 µM | B | CRYZL2P activity raises the cells' numbers under Ipatasertib 0.5 µM (protects the cells) | lines that do not express CRYZL2P (14) vs lines expressing it (34) | the lines without CRYZL2P: 0.66× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: SEC16B |
| [[SEC16B]] | C | CRYZL2P activity raises SEC16B's level | lines that do not express CRYZL2P (14) vs lines expressing it (36) | 2.77× lower at baseline in the lines without CRYZL2P | 0.005 | ⚠ within organs, on part of the lines; also absent: SEC16B; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.424). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.3, 56.6); signed map (62.9, -0.4). **Vector** length 67.6, 14.0% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.7 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +4.3 | +5.3 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.7 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.1 | -12.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -9.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -8.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | +0.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | crystallin zeta like 2, pseudogene |
| Locus type | pseudogene |
| Location | 1q25.2 — chr1:178,008,081-178,037,946 (-) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52164](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52164) · Entrez [730102](https://www.ncbi.nlm.nih.gov/gene/730102) · Ensembl [ENSG00000242193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242193)

## Data

Gene col 14305: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14305); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14305, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14305]; `tensor/DDL_lfc|DDL_z.npy` [14305]; `embed/gene_vectors.npy` [14305]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14305 or target_col == 14305). Every well: [[CRYZL2P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRYZL2P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
