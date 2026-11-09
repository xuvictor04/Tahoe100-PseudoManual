---
symbol: "PGM5P2-1"
type: "gene"
col: 16529
ensembl_id: "ENSG00000290923"
name: ""
location: ""
module: 202
arm: "+"
pooled_cpm: 8.01
n_lines_expressing: 38
n_dd_up: 19
n_dd_down: 19
n_dd_up_clean: 12
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 6
direction_downstream: 10
tags: ["gene", "module/202"]
generated_by: "tahoemap"
---

# PGM5P2-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.14× (z +15.1, q 0e+00, up in 10 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.56× (z +8.8, q 1e-16, up in 18 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.417× (z -12.2, q 2e-31, down in 27 of 34 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.634× (z -6.0, q 2e-07, down in 14 of 32 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGM5P2]] (+0.76, fdr 7e-06, ⚠ same locus), [[HDAC2-AS2]] (+0.67, fdr 1e-05), [[RGS20]] (+0.67, fdr 1e-05), [[SPON1-AS1]] (+0.64, fdr 1e-05); moves opposite to [[EFNA4]] (-0.56, fdr 6e-05), [[SCRN2]] (-0.53, fdr 6e-05), [[RGS14]] (-0.51, fdr 1e-04).
> It is in [[Module 202]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[GPR176]] → it (grade B ⚠); 10 go from it, the strongest it → [[AXL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16529.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.14×** | +15.1 | 0e+00 | 10/13 (SW 900, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.29×** | +11.5 | 3e-28 | 16/24 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +9.3 | 4e-18 | 8/18 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.56×** | +8.8 | 1e-16 | 18/34 (H4, A-172, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.9 | 3e-13 | 8/30 (PANC-1, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.76×** | +7.9 | 3e-13 | 16/31 (LS 180, SW 900, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.71×** | +7.0 | 2e-10 | 21/34 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +6.8 | 9e-10 | 14/30 (hTERT-HPNE, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.55×** | +6.1 | 6e-08 | 16/34 (A-172, H4, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.52×** | +5.9 | 2e-07 | 17/34 (A-172, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.42×** | +4.9 | 6e-05 | 14/34 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.62×** | +4.8 | 7e-05 | 12/31 (SW 900, A-172, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.89×** | +4.7 | 1e-04 | 8/23 (A-172, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.39×** | +4.6 | 2e-04 | 11/30 (CFPAC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.001 | 4/28 (PANC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.53×** | +3.1 | 0.069 | 2/35 (NCI-H460, SW480) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.070 | 7/32 (HOP62, HS-578T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.24×** | +3.0 | 0.075 | 4/34 (Panc 03.27, SK-MEL-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16529.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.417×** | -12.2 | 2e-31 | 27/34 (J82, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.429×** | -11.8 | 1e-29 | 26/34 (A-172, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.544×** | -8.5 | 4e-15 | 22/34 (J82, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.641×** | -6.2 | 8e-08 | 18/34 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.634×** | -6.0 | 2e-07 | 14/32 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.664×** | -5.7 | 1e-06 | 17/34 (NCI-H1792, C32, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.687×** | -5.2 | 1e-05 | 14/34 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.688×** | -5.2 | 1e-05 | 13/34 (SW 900, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.543×** | -4.5 | 5e-04 | 10/33 (J82, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.737×** | -4.3 | 0.001 | 17/34 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.742×** | -4.2 | 0.002 | 10/31 (SNU-423, H4, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -3.9 | 0.005 | 4/35 (A498, A-427, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.748×** | -3.8 | 0.006 | 16/34 (J82, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.606×** | -3.6 | 0.011 | 9/29 (A498, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.611×** | -3.6 | 0.012 | 9/33 (NCI-H1792, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.776×** | -3.5 | 0.015 | 10/34 (HEC-1-A, A-172, …) | top dose only |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM |  | **0.771×** | -3.4 | 0.021 | 6/34 (NCI-H2030, SW1417, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.720×** | -3.3 | 0.035 | 2/34 (CFPAC-1, RKO) | rises with dose | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.641×** | -3.2 | 0.036 | 7/28 (NCI-H2030, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | 0.860× | -3.0 | 0.081 | 6/34 (SK-MEL-2, A-427, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.742×** | -3.0 | 0.081 | 5/34 (HCT15, SNU-423, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16529. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0715× (z -14.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[XRK3F2 (drug)]] 0.5 µM 0.0885× (z -9.4) |
| [[J82 (line)]] | alt | 40.8 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -13.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 19.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -11.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LOX-IMVI (line)]] | wt | 18.2 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.185× (z -9.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SNU-423 (line)]] | alt | 23.6 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -9.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[H4 (line)]] | wt | 6.54 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 15.6× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 9.69 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -8.7) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H460 (line)]] | wt | 2.95 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.108× (z -9.3) |
| [[SW 900 (line)]] | alt | 37.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -9.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-427 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.977 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16529), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGM5P2]] | +0.76 | +0.73 / +0.72 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[HDAC2-AS2]] | +0.67 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[RGS20]] | +0.67 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[SPON1-AS1]] | +0.64 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SLC39A10]] | +0.62 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[CCDC50]] | +0.62 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[MGLL]] | +0.62 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[GPR176]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[PSG5]] | +0.57 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[SAMD4A]] | +0.57 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[LINC00707]] | +0.56 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[GRK4]] | +0.54 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[ANKRD18B]] | +0.54 | +0.47 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFNA4]] | -0.56 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[SCRN2]] | -0.53 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[RGS14]] | -0.51 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[SDHAF1]] | -0.50 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[MRPL17]] | -0.49 | -0.32 / -0.34 | both halves | 2e-04 |  |
| [[MRPL55]] | -0.48 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[ID1]] | -0.48 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[OCEL1]] | -0.48 | -0.23 / -0.44 | both halves | 5e-04 |  |
| [[RAB3A]] | -0.48 | -0.29 / -0.38 | both halves | 3e-04 |  |
| [[DDIT4]] | -0.48 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[ISCA2]] | -0.47 | -0.22 / -0.42 | both halves | 6e-04 |  |
| [[RAB20]] | -0.47 | -0.41 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR176]] | B | GPR176 activity raises PGM5P2-1's level | lines that do not express GPR176 (18) vs lines expressing it (32) | 2.48× lower at baseline in the lines without GPR176 | 0.041 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, AFAP1L1 |
| [[LINC02057]] | B | LINC02057 activity raises PGM5P2-1's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 2.27× lower at baseline in the lines without LINC02057 | 0.060 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[SMCO2]] | B | SMCO2 activity raises PGM5P2-1's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.75× lower at baseline in the lines without SMCO2 | 0.078 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |
| [[MGLL]] | B | MGLL activity raises PGM5P2-1's level | lines that do not express MGLL (14) vs lines expressing it (36) | 1.96× lower at baseline in the lines without MGLL | 0.083 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[PLCB4]] | B | PLCB4 activity raises PGM5P2-1's level | lines that do not express PLCB4 (13) vs lines expressing it (37) | 1.92× lower at baseline in the lines without PLCB4 | 0.084 | ⚠ within organs, on part of the lines; also absent: SLC39A8, ENSG00000248347, PKIA |
| [[PGM5P2]] | C | PGM5P2 activity raises PGM5P2-1's level | lines that do not express PGM5P2 (9) vs lines expressing it (41) | 3.04× lower at baseline in the lines without PGM5P2 | 0.011 | ⚠ within organs, on part of the lines; also absent: PGM5P2-1, PALM2AKAP2, FKBP7; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AXL]] | B | PGM5P2-1 activity raises AXL's level | lines that do not express PGM5P2-1 (12) vs lines expressing it (38) | 5.14× lower at baseline in the lines without PGM5P2-1 | 0.008 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MAMLD1, HRH1; maybe low, not absent |
| [[MRPL17]] | B | PGM5P2-1 activity raises MRPL17's level | lines that do not express PGM5P2-1 (12) vs lines expressing it (38) | 1.52× lower at baseline in the lines without PGM5P2-1 | 0.038 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MAMLD1, HRH1; maybe low, not absent |
| [[VIM-AS1]] | B | PGM5P2-1 activity raises VIM-AS1's level | lines that do not express PGM5P2-1 (12) vs lines expressing it (38) | 1.91× lower at baseline in the lines without PGM5P2-1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MAMLD1, HRH1; maybe low, not absent |
| [[LINC02057]] | B | PGM5P2-1 activity raises LINC02057's level | lines that do not express PGM5P2-1 (12) vs lines expressing it (38) | 2.63× lower at baseline in the lines without PGM5P2-1 | 0.070 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MAMLD1, HRH1; maybe low, not absent |
| [[CRIM1]] | B | PGM5P2-1 activity raises CRIM1's level | lines that do not express PGM5P2-1 (12) vs lines expressing it (38) | 1.56× lower at baseline in the lines without PGM5P2-1 | 0.079 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MAMLD1, HRH1; maybe low, not absent |
| [[GPR176]] | B | PGM5P2-1 activity raises GPR176's level | lines that do not express PGM5P2-1 (12) vs lines expressing it (38) | 4.19× lower at baseline in the lines without PGM5P2-1 | 0.079 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MAMLD1, HRH1; maybe low, not absent |
| cells under [[Vemurafenib (drug)]] 5 µM | B | PGM5P2-1 activity raises the cells' numbers under Vemurafenib 5 µM (protects the cells) | lines that do not express PGM5P2-1 (12) vs lines expressing it (36) | the lines without PGM5P2-1: 0.85× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MAMLD1, HRH1; maybe low, not absent |
| [[SCRN2]] | B | PGM5P2-1 activity raises SCRN2's level | lines that do not express PGM5P2-1 (12) vs lines expressing it (38) | 1.18× lower at baseline in the lines without PGM5P2-1 | 0.099 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MAMLD1, HRH1; maybe low, not absent |
| [[ID1]] | B | PGM5P2-1 activity lowers ID1's level | lines that do not express PGM5P2-1 (12) vs lines expressing it (38) | 1.70× higher at baseline in the lines without PGM5P2-1 | 0.0999 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MAMLD1, HRH1; maybe low, not absent |
| [[PGM5P2]] | C | PGM5P2-1 activity raises PGM5P2's level | lines that do not express PGM5P2-1 (12) vs lines expressing it (38) | 2.06× lower at baseline in the lines without PGM5P2-1 | 0.006 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MAMLD1, HRH1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 202]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.4, 13.6); signed map (27.1, 10.1). **Vector** length 71.8, 14.6% of its response variance represented; |z| ≥ 3 in 817 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.2 | +8.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.7 | +7.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.7 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +2.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.9 | +4.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.6 | -6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.4 | -8.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.3 | -12.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -4.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.9 | -3.3 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.5 | -2.6 |
|  | [[EX229 (drug)]] 0.5 µM |  | -1.2 | -3.0 |

## What is on record

> [!warning] No registry record
> PGM5P2-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16529: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16529); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16529, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16529]; `tensor/DDL_lfc|DDL_z.npy` [16529]; `embed/gene_vectors.npy` [16529]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16529 or target_col == 16529). Every well: [[PGM5P2-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGM5P2-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
