---
symbol: "GRAMD2B"
type: "gene"
col: 7887
ensembl_id: "ENSG00000155324"
name: "GRAM domain containing 2B"
location: "5q23.2"
module: 104
arm: "+"
pooled_cpm: 72.49
n_lines_expressing: 35
n_dd_up: 5
n_dd_down: 31
n_dd_up_clean: 4
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 14
direction_downstream: 19
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# GRAMD2B

*GRAM domain containing 2B* — 5q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.17× (z +8.6, q 6e-15, up in 22 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.418× (z -26.0, q 0e+00, down in 34 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSTPIP2]] (+0.54, fdr 1e-05), [[FGD4]] (+0.52, fdr 3e-05), [[IRAK3]] (+0.50, fdr 4e-05); moves opposite to [[PDE10A]] (-0.49, fdr 3e-05), [[ANKMY1]] (-0.47, fdr 3e-05), [[TCF7]] (-0.46, fdr 5e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[INAVA]] → it (grade B ⚠); 19 go from it, the strongest it → [[IFNLR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7887.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.17×** | +8.6 | 6e-15 | 22/34 (HOP62, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.34×** | +6.2 | 2e-07 | 14/34 (A-172, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +6.1 | 2e-07 | 13/33 (A-172, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | 1.20× | +3.8 | 0.018 | 11/33 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.21×** | +3.7 | 0.021 | 10/32 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.19× | +3.7 | 0.021 | 11/33 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.022 | 11/32 (HOP62, SW480, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.022 | 10/32 (NCI-H1792, A-172, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.5 | 0.029 | 5/33 (LS 180, HOP62, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.12× | +3.5 | 0.030 | 8/33 (HOP62, COLO 205, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.035 | 9/32 (A-172, HOP62, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.17× | +3.3 | 0.040 | 6/33 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.099 | 4/32 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 1.15× | +3.0 | 0.10 | 10/33 (NCI-H1792, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7887.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.418×** | -26.0 | 0e+00 | 34/34 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.445×** | -17.0 | 0e+00 | 28/33 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.448×** | -16.9 | 0e+00 | 30/33 (HEC-1-A, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.462×** | -16.3 | 0e+00 | 26/33 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.463×** | -15.1 | 0e+00 | 24/29 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.529×** | -13.4 | 5e-39 | 24/33 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.532×** | -12.4 | 3e-33 | 29/32 (HEC-1-A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.585×** | -11.3 | 1e-27 | 23/32 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.695×** | -10.8 | 2e-25 | 24/33 (CFPAC-1, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.590×** | -10.3 | 6e-23 | 20/30 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.617×** | -10.2 | 1e-22 | 26/32 (SW 900, HS-578T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.630×** | -9.7 | 1e-20 | 21/33 (LS 180, SW480, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.648×** | -9.1 | 3e-18 | 24/33 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.656×** | -8.9 | 3e-17 | 24/33 (SW 900, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.744×** | -8.8 | 4e-17 | 19/32 (NCI-H2347, HCT15, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.723×** | -6.4 | 4e-09 | 21/33 (J82, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.748×** | -5.7 | 3e-07 | 21/33 (A498, CFPAC-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.609×** | -5.5 | 1e-06 | 13/32 (A498, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.781×** | -5.2 | 5e-06 | 16/32 (NCI-H1792, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.673×** | -4.4 | 3e-04 | 15/33 (SW 900, J82, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.733×** | -3.4 | 0.013 | 11/32 (J82, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.768×** | -2.9 | 0.064 | 13/33 (NCI-H2347, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7887. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 199 | 0 | 17 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -24.6) |
| [[SW480 (line)]] | alt | 58.8 | 0 | 13 (11 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.348× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 203 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -19.8) |
| [[SW 900 (line)]] | alt | 103 | 0 | 11 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -16.4) |
| [[COLO 205 (line)]] | alt | 180 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -12.2) |
| [[LS 180 (line)]] | wt | 127 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -16.6) |
| [[Panc 03.27 (line)]] | alt | 192 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -21.1) |
| [[NCI-H2347 (line)]] | alt | 203 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -22.2) |
| [[LoVo (line)]] | wt | 126 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.357× (z -13.0) |
| [[NCI-H2030 (line)]] | alt | 79.2 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -12.6) |
| [[AsPC-1 (line)]] | alt | 188 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -28.6) |
| [[A498 (line)]] | wt | 77.9 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -12.9) |
| [[HCT15 (line)]] | alt | 53.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -14.8) |
| [[HOP62 (line)]] | alt | 74.5 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 10.4× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -11.6) |
| [[J82 (line)]] | alt | 278 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -17.9) |
| [[MIA PaCa-2 (line)]] | alt | 91.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 47.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -12.6) |
| [[HepG2_C3A (line)]] | wt | 84.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -9.1) |
| [[HT-29 (line)]] | alt | 48.2 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.227× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 50.3 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -11.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -10.5) |
| [[SNU-423 (line)]] | alt | 70.4 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.232× (z -13.3) |
| [[AN3 CA (line)]] | alt | 38.0 | 0 | 1 | — | [[Bendamustine (drug)]] 0.05 µM 0.0589× (z -10.6) |
| [[BT-474 (line)]] | alt | 32.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +13.1) | — |
| [[C32 (line)]] | wt | 42.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SW48 (line)]] | wt | 29.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -9.8) |
| [[A-172 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.6 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.36 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.64 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.62 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.63 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.88 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.27 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.00 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.56 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.58 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 46.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7887), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSTPIP2]] | +0.54 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[FGD4]] | +0.52 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[IRAK3]] | +0.50 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[SRGN]] | +0.49 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[MAPK14]] | +0.49 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[ST6GALNAC5]] | +0.47 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[C1orf115]] | +0.46 | +0.35 / +0.43 | both halves | 1e-04 |  |
| [[EPS8]] | +0.46 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[SUSD6]] | +0.45 | +0.31 / +0.52 | both halves | 2e-04 |  |
| [[PTX3]] | +0.45 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[SORBS2]] | +0.45 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[CNKSR1]] | +0.45 | +0.31 / +0.48 | both halves | 2e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE10A]] | -0.49 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ANKMY1]] | -0.47 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[TCF7]] | -0.46 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[SIRLNT]] | -0.46 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[TTC7B]] | -0.46 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[FIBCD1]] | -0.46 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[ARHGAP21]] | -0.45 | -0.32 / -0.44 | both halves | 1e-04 |  |
| [[BEGAIN]] | -0.44 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[FAM227A]] | -0.43 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[PDE3A]] | -0.43 | -0.46 / -0.26 | both halves | 4e-04 |  |
| [[MFSD1]] | -0.43 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[KCNMA1]] | -0.42 | -0.30 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 11, C 3. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INAVA]] | B | INAVA activity raises GRAMD2B's level | lines that do not express INAVA (29) vs lines expressing it (21) | 3.45× lower at baseline in the lines without INAVA | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[SGPP2]] | B | SGPP2 activity raises GRAMD2B's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 3.15× lower at baseline in the lines without SGPP2 | 0.006 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[IFNLR1]] | B | IFNLR1 activity raises GRAMD2B's level | lines that do not express IFNLR1 (18) vs lines expressing it (32) | 2.26× lower at baseline in the lines without IFNLR1 | 0.008 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |
| [[LPAR5]] | B | LPAR5 activity raises GRAMD2B's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 2.29× lower at baseline in the lines without LPAR5 | 0.022 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[CNKSR1]] | B | CNKSR1 activity raises GRAMD2B's level | lines that do not express CNKSR1 (24) vs lines expressing it (26) | 3.34× lower at baseline in the lines without CNKSR1 | 0.022 | ⚠ within organs, on part of the lines; also absent: SPINT1, SLC52A3, ESRP2 |
| [[MT1F]] | B | MT1F activity raises GRAMD2B's level | lines that do not express MT1F (17) vs lines expressing it (33) | 2.77× lower at baseline in the lines without MT1F | 0.023 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[PSTPIP2]] | B | PSTPIP2 activity raises GRAMD2B's level | lines that do not express PSTPIP2 (20) vs lines expressing it (30) | 2.96× lower at baseline in the lines without PSTPIP2 | 0.028 | ⚠ within organs, on part of the lines; also absent: NEDD9, CARD11, BCAT1 |
| [[ARHGEF5]], [[ARHGEF34P]] | B | ARHGEF5, ARHGEF34P activity raises GRAMD2B's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 3.47× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[TOP2A]] | B | TOP2A activity raises GRAMD2B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HSH2D]] | B | HSH2D activity raises GRAMD2B's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 2.50× lower at baseline in the lines without HSH2D | 0.060 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[SHROOM3]] | B | SHROOM3 activity raises GRAMD2B's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 1.75× lower at baseline in the lines without SHROOM3 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[RNF43]] | C | RNF43 activity raises GRAMD2B's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 3.10× lower at baseline in the lines without RNF43 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 16, C 3. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFNLR1]] | B | GRAMD2B activity raises IFNLR1's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 2.80× lower at baseline in the lines without GRAMD2B | 0.001 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[SUSD6]] | B | GRAMD2B activity raises SUSD6's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 1.58× lower at baseline in the lines without GRAMD2B | 0.011 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[ARHGEF34P]] | B | GRAMD2B activity raises ARHGEF34P's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 3.11× lower at baseline in the lines without GRAMD2B | 0.014 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[EPS8]] | B | GRAMD2B activity raises EPS8's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 2.28× lower at baseline in the lines without GRAMD2B | 0.015 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[INAVA]] | B | GRAMD2B activity raises INAVA's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 3.76× lower at baseline in the lines without GRAMD2B | 0.017 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[CNKSR1]] | B | GRAMD2B activity raises CNKSR1's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 2.86× lower at baseline in the lines without GRAMD2B | 0.020 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[FGD4]] | B | GRAMD2B activity raises FGD4's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 2.65× lower at baseline in the lines without GRAMD2B | 0.020 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[ARHGEF5]] | B | GRAMD2B activity raises ARHGEF5's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 3.12× lower at baseline in the lines without GRAMD2B | 0.022 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[SGPP2]] | B | GRAMD2B activity raises SGPP2's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 3.51× lower at baseline in the lines without GRAMD2B | 0.026 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[FAM227A]] | B | GRAMD2B activity lowers FAM227A's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 1.50× higher at baseline in the lines without GRAMD2B | 0.032 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[PELI1]] | B | GRAMD2B activity raises PELI1's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 1.90× lower at baseline in the lines without GRAMD2B | 0.048 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[LPAR5]] | B | GRAMD2B activity raises LPAR5's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 2.00× lower at baseline in the lines without GRAMD2B | 0.057 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.382). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.8, 15.9); signed map (17.5, 30.2). **Vector** length 101, 26.2% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +8.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.1 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +2.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.8 | +1.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.7 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +6.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.2 | -16.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -26.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -12.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -3.2 | -15.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -3.1 | -13.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -10.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -8.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | GRAM domain containing 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.2 — chr5:126,360,132-126,496,494 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NS3TP2, FLJ21313; previously GRAMD3 |
| Gene groups (HGNC) | GRAM domain containing |
| Matched by | ensembl_id |

UniProt [Q96HH9](https://www.uniprot.org/uniprotkb/Q96HH9) carries no function annotation.

**Summary**, from NCBI Gene [65983](https://www.ncbi.nlm.nih.gov/gene/65983):

> Enables identical protein binding activity. Located in cytoplasmic microtubule. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24911](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24911) · Entrez [65983](https://www.ncbi.nlm.nih.gov/gene/65983) · UniProt [Q96HH9](https://www.uniprot.org/uniprotkb/Q96HH9) · Ensembl [ENSG00000155324](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155324)

## Data

Gene col 7887: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7887); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7887, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7887]; `tensor/DDL_lfc|DDL_z.npy` [7887]; `embed/gene_vectors.npy` [7887]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7887 or target_col == 7887). Every well: [[GRAMD2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRAMD2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
