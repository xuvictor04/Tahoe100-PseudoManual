---
symbol: "SFMBT2"
type: "gene"
col: 12719
ensembl_id: "ENSG00000198879"
name: "Scm like with four mbt domains 2"
location: "10p14"
module: 152
arm: "+"
pooled_cpm: 40.02
n_lines_expressing: 31
n_dd_up: 11
n_dd_down: 39
n_dd_up_clean: 11
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 10
direction_downstream: 3
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# SFMBT2

*Scm like with four mbt domains 2* — 10p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.36× (z +22.6, q 0e+00, up in 27 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.600× (z -9.4, q 2e-18, down in 21 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.637× (z -8.3, q 2e-14, down in 18 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST8SIA4]] (+0.68, fdr 7e-06), [[SLITRK5]] (+0.67, fdr 1e-05), [[NEFL]] (+0.65, fdr 1e-05); moves opposite to [[QRICH2]] (-0.50, fdr 5e-05), [[ZNF621]] (-0.48, fdr 5e-05), [[ITGA9-AS1]] (-0.47, fdr 2e-04).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[VWDE]] → it (grade B ⚠); 3 go from it, the strongest it → [[PGAP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12719.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.36×** | +22.6 | 0e+00 | 27/29 (C32, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.27×** | +15.2 | 0e+00 | 20/28 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.27×** | +15.2 | 0e+00 | 25/29 (NCI-H2030, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.10×** | +13.8 | 6e-41 | 23/29 (NCI-H2030, A-427, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.05×** | +13.3 | 2e-38 | 21/29 (A-427, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.92×** | +12.1 | 1e-31 | 22/29 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.27×** | +7.9 | 2e-13 | 21/30 (NCI-H2030, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +5.5 | 2e-06 | 12/28 (SK-MEL-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +5.4 | 4e-06 | 16/28 (HOP62, SW 900, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.64×** | +4.8 | 8e-05 | 13/30 (NCI-H1573, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.084 | 3/30 (HOP62, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Decitabine (drug)]] 5 µM |  | 1.19× | +3.1 | 0.084 | 5/28 (RPMI-7951, LOX-IMVI, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +3.1 | 0.084 | 2/29 (C-33 A, HEC-1-A) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.12× | +3.1 | 0.084 | 3/29 (LOX-IMVI, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12719.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.600×** | -9.4 | 2e-18 | 21/28 (SW 900, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.637×** | -8.3 | 2e-14 | 18/29 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.659×** | -7.7 | 2e-12 | 20/28 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.745×** | -7.7 | 2e-12 | 16/29 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.666×** | -7.5 | 7e-12 | 20/28 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.680×** | -7.1 | 1e-10 | 16/28 (NCI-H460, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.673×** | -7.0 | 2e-10 | 16/29 (NCI-H460, NCI-H2030, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.692×** | -6.3 | 2e-08 | 18/25 (C-33 A, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **0.719×** | -6.1 | 7e-08 | 17/27 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.727×** | -5.9 | 2e-07 | 17/29 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.735×** | -5.7 | 7e-07 | 13/29 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.737×** | -5.6 | 9e-07 | 17/27 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.742×** | -5.3 | 5e-06 | 14/27 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.580×** | -5.3 | 6e-06 | 15/27 (SW 900, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.742×** | -5.2 | 8e-06 | 19/29 (SW 900, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.819×** | -5.2 | 8e-06 | 18/30 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.760×** | -5.1 | 1e-05 | 13/27 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Neratinib (drug)]] 5 µM |  | **0.775×** | -4.7 | 7e-05 | 12/28 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.788×** | -4.4 | 3e-04 | 13/29 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.792×** | -4.3 | 4e-04 | 11/27 (SK-MEL-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.644×** | -4.2 | 5e-04 | 11/27 (RPMI-7951, PANC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12719. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 55.6 | 5 | 14 (9 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.51× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -18.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 65.9 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -22.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.120× (z -17.1) |
| [[SW 900 (line)]] | alt | 167 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.317× (z -10.8) |
| [[C32 (line)]] | wt | 33.2 | 4 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.25× (z +14.6) | [[Dinaciclib (drug)]] 0.05 µM 0.0904× (z -13.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 210 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0177× (z -32.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.321× (z -9.5) |
| [[HOP62 (line)]] | alt | 47.3 | 3 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.23× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 120 | 2 (1 ⚠) | 4 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.07× (z +9.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.30× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -22.5) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -16.5) |
| [[NCI-H23 (line)]] | alt | 76.7 | 0 | 6 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0942× (z -17.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -12.2) |
| [[A-427 (line)]] | wt | 25.2 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.14× (z +12.7) | — |
| [[PANC-1 (line)]] | alt | 58.4 | 0 | 4 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.387× (z -9.8) ⚠ transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.397× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 63.6 | 1 | 3 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.96× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -21.1) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A498 (line)]] | wt | 17.5 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 2.60× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 12.4 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 5.17× (z +10.9) | — |
| [[RPMI-7951 (line)]] | alt | 52.8 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.87× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -13.1) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 16.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +12.3) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.40× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 45.5 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.18× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -9.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 29.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.70× (z +12.3) | — |
| [[LoVo (line)]] | wt | 15.4 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +13.6) ⚠ cell-cycle shift, explains ~46% of this change | [[Belinostat (drug)]] 5 µM 0.175× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 83.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -13.2) ⚠ cell-cycle shift, explains ~46% of this change |
| [[Panc 03.27 (line)]] | alt | 25.0 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.30× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -11.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 185 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -14.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 73.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -14.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.08 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.40 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.05 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.29 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.55 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.11 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.12 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.42 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.65 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.37 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.24 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12719), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST8SIA4]] | +0.68 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[SLITRK5]] | +0.67 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[NEFL]] | +0.65 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[EBF2]] | +0.64 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[GLRB]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[MEIS1]] | +0.60 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[ASXL3]] | +0.59 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[BCL11A]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[VWDE]] | +0.57 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[TMEM178B]] | +0.56 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[TRIM9]] | +0.56 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[VAV3]] | +0.56 | +0.43 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QRICH2]] | -0.50 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[ZNF621]] | -0.48 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[ITGA9-AS1]] | -0.47 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[LTO1]] | -0.47 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[PPP3CB-AS1]] | -0.46 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[CC2D1B]] | -0.46 | -0.42 / -0.37 | both halves | 7e-05 |  |
| [[ZNF529-AS1]] | -0.46 | -0.45 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VWDE]] | B | VWDE activity raises SFMBT2's level | lines that do not express VWDE (22) vs lines expressing it (28) | 2.87× lower at baseline in the lines without VWDE | 0.021 | ⚠ within organs, on part of the lines; also absent: RBM11, L3MBTL4, RPS6KA6 |
| [[GPRIN3]] | B | GPRIN3 activity raises SFMBT2's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 3.01× lower at baseline in the lines without GPRIN3 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031 |
| [[EBF2]] | B | EBF2 activity raises SFMBT2's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 2.73× lower at baseline in the lines without EBF2 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[NOL4]] | B | NOL4 activity raises SFMBT2's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 3.26× lower at baseline in the lines without NOL4 | 0.060 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent |
| [[MEIS1]] | B | MEIS1 activity raises SFMBT2's level | lines that do not express MEIS1 (11) vs lines expressing it (39) | 2.97× lower at baseline in the lines without MEIS1 | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC01798, DYNC1I1, CAMK4 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SFMBT2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers SFMBT2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TMEM170B]] | B | TMEM170B activity raises SFMBT2's level | lines that do not express TMEM170B (8) vs lines expressing it (42) | 3.32× lower at baseline in the lines without TMEM170B | 0.089 | ⚠ within organs, on part of the lines; also absent: KCNK13, KDM2B-DT, LINC02609 |
| [[EYA2]] | C | EYA2 activity raises SFMBT2's level | lines that do not express EYA2 (34) vs lines expressing it (16) | 3.44× lower at baseline in the lines without EYA2 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL22A1, LGSN, EPGN; co-absent with the target |
| [[VAV3]] | C | VAV3 activity raises SFMBT2's level | lines that do not express VAV3 (30) vs lines expressing it (20) | 4.33× lower at baseline in the lines without VAV3 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RSPO3, ENSG00000289418, NRCAM; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGAP1]] | B | SFMBT2 activity raises PGAP1's level | lines that do not express SFMBT2 (19) vs lines expressing it (31) | 1.03× lower at baseline in the lines without SFMBT2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ANKRD6, LONRF2, GHR |
| [[LRCH2]] | B | SFMBT2 activity raises LRCH2's level | lines that do not express SFMBT2 (19) vs lines expressing it (31) | 1.30× lower at baseline in the lines without SFMBT2 | 0.097 | ⚠ within organs, on part of the lines; also absent: ANKRD6, LONRF2, GHR |
| [[WDR17]] | C | SFMBT2 activity raises WDR17's level | lines that do not express SFMBT2 (19) vs lines expressing it (31) | 3.73× lower at baseline in the lines without SFMBT2 | 0.058 | ⚠ within organs, on part of the lines; also absent: ANKRD6, LONRF2, GHR; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.1, 35.6); signed map (39.1, 39.0). **Vector** length 94.1, 24.1% of its response variance represented; |z| ≥ 3 in 1,012 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.1 | +22.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.0 | +12.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.8 | +15.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | -9.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +7.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.9 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +2.4 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -4.5 | -3.7 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.6 | -5.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.6 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.5 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.3 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -7.5 |

## What is on record

|  |  |
|---|---|
| Name | Scm like with four mbt domains 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p14 — chr10:7,158,624-7,411,488 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1617 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; MBT domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VUG0](https://www.uniprot.org/uniprotkb/Q5VUG0) (Scm-like with four MBT domains protein 2):

> Transcriptional repressor of HOXB13 gene.

**Summary**, from NCBI Gene [57713](https://www.ncbi.nlm.nih.gov/gene/57713):

> Enables histone binding activity. Involved in negative regulation of gene expression. Located in nuclear speck. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20256](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20256) · Entrez [57713](https://www.ncbi.nlm.nih.gov/gene/57713) · UniProt [Q5VUG0](https://www.uniprot.org/uniprotkb/Q5VUG0) · Ensembl [ENSG00000198879](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198879)

## Data

Gene col 12719: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12719); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12719, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12719]; `tensor/DDL_lfc|DDL_z.npy` [12719]; `embed/gene_vectors.npy` [12719]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12719 or target_col == 12719). Every well: [[SFMBT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFMBT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
