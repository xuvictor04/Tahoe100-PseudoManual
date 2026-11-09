---
symbol: "SPATA13"
type: "gene"
col: 11348
ensembl_id: "ENSG00000182957"
name: "spermatogenesis associated 13"
location: "13q12.12"
module: 23
arm: "-"
pooled_cpm: 106.83
n_lines_expressing: 46
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# SPATA13

*spermatogenesis associated 13* — 13q12.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.03× (z +28.4, q 0e+00, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.649× (z -11.1, q 7e-26, down in 30 of 44 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHPN2]] (+0.68, fdr 1e-05), [[EEPD1]] (+0.66, fdr 1e-05), [[TRAK1]] (+0.62, fdr 1e-05); moves opposite to [[METTL6]] (-0.59, fdr 4e-05), [[ZNF563]] (-0.59, fdr 5e-05), [[ZNF621]] (-0.58, fdr 4e-05).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LEMD1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RALGAPA2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11348.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.03×** | +28.4 | 0e+00 | 42/44 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.44×** | +22.8 | 0e+00 | 39/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.30×** | +21.3 | 0e+00 | 40/44 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.75×** | +14.3 | 3e-44 | 36/44 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +10.5 | 6e-24 | 25/44 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.07×** | +9.7 | 2e-20 | 31/45 (A-427, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +8.3 | 1e-14 | 30/44 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.50×** | +5.5 | 3e-06 | 17/40 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +5.0 | 4e-05 | 19/44 (Hs 766T, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.21×** | +4.9 | 5e-05 | 18/45 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.17× | +3.8 | 0.007 | 18/43 (NCI-H460, HOP62, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.7 | 0.009 | 13/43 (SW48, LoVo, …) | two highest doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.009 | 11/45 (LoVo, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.15× | +3.6 | 0.012 | 15/44 (J82, SW1417, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.058 | 16/44 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.077 | 11/44 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.081 | 6/44 (SNU-423, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11348.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.649×** | -11.1 | 7e-26 | 30/44 (SW480, SW48, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.692×** | -9.1 | 2e-17 | 26/44 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.835× | -6.6 | 9e-09 | 23/43 (PANC-1, LoVo, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.837× | -6.5 | 1e-08 | 22/45 (SW480, SW48, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.795×** | -5.9 | 4e-07 | 23/45 (HepG2/C3A, C32, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.685×** | -5.1 | 3e-05 | 15/45 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.827×** | -4.9 | 8e-05 | 17/44 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.834× | -4.3 | 0.001 | 20/41 (C32, Panc 03.27, …) | all doses, flat | composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.894× | -4.1 | 0.002 | 9/44 (SW 900, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.894× | -4.1 | 0.002 | 17/44 (SW48, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.812×** | -3.8 | 0.007 | 11/44 (SW48, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.759×** | -3.7 | 0.010 | 12/44 (C32, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.767×** | -3.6 | 0.015 | 10/44 (SW1417, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.866× | -3.6 | 0.015 | 21/43 (SW1417, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.868× | -3.5 | 0.017 | 21/37 (C32, HepG2/C3A, …) | all doses, flat | composition shift |
| [[Sulfatinib (drug)]] 5 µM |  | 0.879× | -3.2 | 0.048 | 9/45 (HCT15, RPMI-7951, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.800×** | -3.0 | 0.082 | 12/44 (SW48, C32, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | 0.853× | -2.9 | 0.097 | 5/45 (SW48, C32, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11348. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 340 | 0 | 15 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -18.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.261× (z -12.5) |
| [[SW480 (line)]] | alt | 495 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -19.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.304× (z -13.8) |
| [[C32 (line)]] | wt | 224 | 2 | 5 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 5.04× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 77.2 | 4 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.96× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -15.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.376× (z -11.0) |
| [[PANC-1 (line)]] | alt | 45.8 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.73× (z +13.3) | [[Harringtonine (drug)]] 5 µM 0.235× (z -18.5) |
| [[SW1417 (line)]] | alt | 155 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.32× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.524× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 53.5 | 4 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.95× (z +15.3) | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -13.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HT-29 (line)]] | alt | 223 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.03× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.338× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 35.2 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.71× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 63.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.343× (z -8.5) |
| [[A-427 (line)]] | wt | 34.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.30× (z +10.9) | — |
| [[A498 (line)]] | wt | 51.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.95× (z +11.1) | — |
| [[A549 (line)]] | wt | 36.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.72× (z +13.0) | — |
| [[HepG2_C3A (line)]] | wt | 190 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -14.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 33.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.90× (z +12.2) | — |
| [[J82 (line)]] | alt | 51.8 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.14× (z +11.4) | — |
| [[KATO III (line)]] | alt | 273 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 45.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.66× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 35.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.65× (z +12.0) | — |
| [[NCI-H2030 (line)]] | alt | 26.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.77× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 29.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.28× (z +13.6) | — |
| [[RKO (line)]] | wt | 66.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.23× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 48.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.85× (z +12.2) | — |
| [[AsPC-1 (line)]] | alt | 98.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.24× (z +10.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.364× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 63.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -11.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[COLO 205 (line)]] | alt | 663 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 69.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.53× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 37.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.71× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 146 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.57× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.349× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 67.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.78× (z +10.0) | — |
| [[H4 (line)]] | wt | 36.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.93× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 37.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.15× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 214 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.360× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 61.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.70× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 44.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.28× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 40.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 56.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.01× (z +9.1) | — |
| [[A-172 (line)]] | wt | 25.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.0 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.03 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11348), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHPN2]] | +0.68 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[EEPD1]] | +0.66 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[TRAK1]] | +0.62 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[RAPGEF5]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[GMDS]] | +0.60 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[ARHGAP8]] | +0.60 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[LMCD1]] | +0.59 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[PLXND1]] | +0.58 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[CLMN]] | +0.58 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[ENDOD1]] | +0.57 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[MAGI1]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[EML4]] | +0.56 | +0.49 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL6]] | -0.59 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[ZNF563]] | -0.59 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[ZNF621]] | -0.58 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[OXA1L-DT]] | -0.55 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[ACAD11]] | -0.54 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[MFF-DT]] | -0.54 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[ADAL]] | -0.54 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[MAILR]] | -0.54 | -0.38 / -0.20 | both halves | 7e-04 |  |
| [[C19orf54]] | -0.54 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[CSTF3]] | -0.53 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[RC3H2]] | -0.53 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[THBS4]] | -0.53 | -0.43 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LEMD1]] | B | LEMD1 activity raises SPATA13's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 2.42× lower at baseline in the lines without LEMD1 | 0.013 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[B4GALNT3]] | B | B4GALNT3 activity raises SPATA13's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 2.38× lower at baseline in the lines without B4GALNT3 | 0.021 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[HNF4A]] | B | HNF4A activity raises SPATA13's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 2.80× lower at baseline in the lines without HNF4A | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |
| [[CLMN]] | B | CLMN activity raises SPATA13's level | lines that do not express CLMN (7) vs lines expressing it (43) | 2.28× lower at baseline in the lines without CLMN | 0.055 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[GPRC5A]] | B | GPRC5A activity raises SPATA13's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 1.93× lower at baseline in the lines without GPRC5A | 0.056 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[COBL]] | B | COBL activity raises SPATA13's level | lines that do not express COBL (23) vs lines expressing it (27) | 2.22× lower at baseline in the lines without COBL | 0.078 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7 |
| [[RNF128]] | B | RNF128 activity raises SPATA13's level | lines that do not express RNF128 (23) vs lines expressing it (27) | 1.91× lower at baseline in the lines without RNF128 | 0.093 | ⚠ within organs, on part of the lines; also absent: AZGP1, RNF43, PROM1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RALGAPA2]] | C | SPATA13 activity lowers RALGAPA2's level | lines that do not express SPATA13 (4) vs lines expressing it (46) | 1.49× higher at baseline in the lines without SPATA13 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: YBX3, ZNF513, RNF32-DT; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.557). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-5.9, 34.7); signed map (-18.4, 35.5). **Vector** length 118, 31.6% of its response variance represented; |z| ≥ 3 in 1,292 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +6.9 | +28.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.4 | +21.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.4 | +22.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +10.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.4 | +14.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +9.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.1 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -6.2 | -6.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -2.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.9 | -9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -11.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -1.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.5 | -3.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.4 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | spermatogenesis associated 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.12 — chr13:23,979,805-24,307,074 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31208, ARHGEF29, ASEF2 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs; MicroRNA protein coding host genes; SH3 domain containing |
| Reactome | 5 pathways, smallest: CDC42 GTPase cycle; RAC1 GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96N96](https://www.uniprot.org/uniprotkb/Q96N96) (Spermatogenesis-associated protein 13):

> Acts as a guanine nucleotide exchange factor (GEF) for RHOA, RAC1 and CDC42 GTPases. Regulates cell migration and adhesion assembly and disassembly through a RAC1, PI3K, RHOA and AKT1-dependent mechanism. Increases both RAC1 and CDC42 activity, but decreases the amount of active RHOA. Required for MMP9 up-regulation via the JNK signaling pathway in colorectal tumor cells. Involved in tumor angiogenesis and may play a role in intestinal adenoma formation and tumor progression.

**Summary**, from NCBI Gene [221178](https://www.ncbi.nlm.nih.gov/gene/221178):

> Enables guanyl-nucleotide exchange factor activity and identical protein binding activity. Involved in cell migration; plasma membrane bounded cell projection assembly; and regulation of cell migration. Located in several cellular components, including filopodium; lamellipodium; and ruffle membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23222](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23222) · Entrez [221178](https://www.ncbi.nlm.nih.gov/gene/221178) · UniProt [Q96N96](https://www.uniprot.org/uniprotkb/Q96N96) · Ensembl [ENSG00000182957](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182957)

## Data

Gene col 11348: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11348); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11348, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11348]; `tensor/DDL_lfc|DDL_z.npy` [11348]; `embed/gene_vectors.npy` [11348]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11348 or target_col == 11348). Every well: [[SPATA13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPATA13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
