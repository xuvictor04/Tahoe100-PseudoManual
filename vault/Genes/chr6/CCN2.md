---
symbol: "CCN2"
type: "gene"
col: 4002
ensembl_id: "ENSG00000118523"
name: "cellular communication network factor 2"
location: "6q23.2"
module: 120
arm: "+"
pooled_cpm: 31.86
n_lines_expressing: 33
n_dd_up: 22
n_dd_down: 38
n_dd_up_clean: 8
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# CCN2

*cellular communication network factor 2* — 6q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.43× (z +19.4, q 0e+00, up in 21 of 30 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.67× (z +9.0, q 4e-17, up in 16 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (5 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.244× (z -12.4, q 8e-33, down in 25 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCN1]] (+0.78, fdr 7e-06), [[DDAH1]] (+0.77, fdr 7e-06), [[ENC1]] (+0.65, fdr 7e-06); moves opposite to [[LRRC37B]] (-0.51, fdr 4e-05), [[KCTD7]] (-0.50, fdr 1e-05), [[BLVRB]] (-0.49, fdr 2e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ARHGAP18]] → it (grade B ⚠); 6 go from it, the strongest it → [[CRIM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4002.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **4.43×** | +19.4 | 0e+00 | 21/30 (CFPAC-1, RPMI-7951, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.67×** | +9.0 | 4e-17 | 16/30 (RPMI-7951, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.37×** | +7.9 | 4e-13 | 20/31 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.35×** | +7.6 | 6e-12 | 16/30 (CFPAC-1, SW1417, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.15×** | +7.0 | 2e-10 | 18/31 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **2.43×** | +7.0 | 2e-10 | 12/27 (SK-MEL-2, CFPAC-1, …) | all doses, flat | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.76×** | +6.4 | 2e-08 | 22/31 (A-427, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +6.2 | 5e-08 | 17/31 (A-172, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.93×** | +6.1 | 8e-08 | 18/31 (SK-MEL-2, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.00×** | +5.9 | 2e-07 | 9/26 (SK-MEL-2, CFPAC-1, …) | all doses, flat | composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.66×** | +4.7 | 1e-04 | 11/29 (SK-MEL-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.60×** | +4.3 | 7e-04 | 17/31 (HT-29, J82, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.61×** | +3.8 | 0.007 | 12/31 (LOX-IMVI, SNU-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +3.7 | 0.009 | 13/31 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.45×** | +3.4 | 0.022 | 10/31 (hTERT-HPNE, A549, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.033 | 4/31 (HepG2/C3A, J82, …) | inconsistent across doses |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.063 | 3/31 (C-33 A, RKO, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4002.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.244×** | -12.4 | 8e-33 | 25/29 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.313×** | -9.2 | 2e-17 | 23/30 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.417×** | -8.0 | 2e-13 | 20/31 (A-427, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.430×** | -7.7 | 1e-12 | 23/30 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.437×** | -7.3 | 3e-11 | 23/30 (A-427, HepG2/C3A, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.512×** | -6.1 | 8e-08 | 20/31 (LOX-IMVI, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.513×** | -5.9 | 3e-07 | 20/29 (A-427, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.534×** | -5.5 | 2e-06 | 15/30 (A-427, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.584×** | -5.4 | 5e-06 | 17/31 (A-427, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.567×** | -5.2 | 1e-05 | 14/31 (A-427, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | **0.567×** | -4.8 | 8e-05 | 16/30 (C-33 A, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.595×** | -4.8 | 9e-05 | 19/31 (A-427, HepG2/C3A, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.375×** | -4.7 | 1e-04 | 10/29 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.511×** | -4.4 | 5e-04 | 18/31 (H4, A-427, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 0.05 µM |  | **0.605×** | -4.3 | 5e-04 | 16/31 (NCI-H2030, A-172, …) | all doses, flat | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.421×** | -4.1 | 0.001 | 15/29 (LOX-IMVI, A-427, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Terfenadine (drug)]] 5 µM |  | **0.727×** | -4.1 | 0.001 | 8/31 (J82, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4002. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 344 | 1 | 18 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 8.03× (z +8.5) | [[Ponatinib (drug)]] 5 µM 0.134× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 40.9 | 0 | 10 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0528× (z -14.9) |
| [[LOX-IMVI (line)]] | wt | 163 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.179× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 109 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.103× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 31.9 | 4 (4 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 15.5× (z +9.5) ⚠ cell-cycle shift, explains ~28% of this change | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0258× (z -10.9) |
| [[HOP62 (line)]] | alt | 26.8 | 0 | 3 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0450× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 70.5 | 0 | 3 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.124× (z -9.9) |
| [[SNU-1 (line)]] | wt | 56.0 | 0 | 3 (1 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.177× (z -9.6) |
| [[J82 (line)]] | alt | 41.0 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.111× (z -14.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 19.5 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.08× (z +11.1) ⚠ cell-cycle shift, explains ~31% of this change | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0928× (z -8.5) |
| [[PANC-1 (line)]] | alt | 51.2 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 6.87× (z +9.4) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[RPMI-7951 (line)]] | alt | 18.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +14.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 11.0× (z +8.8) | — |
| [[A-172 (line)]] | wt | 57.6 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0414× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 13.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.45× (z +11.1) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[CFPAC-1 (line)]] | alt | 8.84 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.5× (z +17.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HT-29 (line)]] | alt | 30.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.129× (z -9.2) |
| [[SW 900 (line)]] | alt | 10.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.58× (z +9.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW1417 (line)]] | alt | 29.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +13.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A498 (line)]] | wt | 5.49 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.43 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.13 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.47 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.73 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.28 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.45 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.89 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.20 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4002), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCN1]] | +0.78 | +0.76 / +0.80 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 816 |
| [[DDAH1]] | +0.77 | +0.74 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[ENC1]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[CRIM1]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[DLC1]] | +0.63 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[SRGAP1]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[DNMBP]] | +0.60 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[VCL]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[THBS1]] | +0.58 | +0.61 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 749 |
| [[CYTOR]] | +0.57 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[RBMS2]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[COTL1]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC37B]] | -0.51 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[KCTD7]] | -0.50 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[BLVRB]] | -0.49 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[NRSN2-AS1]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[RAB6A]] | -0.47 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[BCL2L2-PABPN1]] | -0.46 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[MORN4]] | -0.46 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[TOM1]] | -0.46 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[NADSYN1]] | -0.44 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[PGLS-DT]] | -0.44 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[ARL8A]] | -0.43 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[PPP3CC]] | -0.43 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP18]] | B | ARHGAP18 activity lowers CCN2's level | lines that do not express ARHGAP18 (6) vs lines expressing it (44) | 4.76× higher at baseline in the lines without ARHGAP18 | 0.042 | ⚠ within organs, on part of the lines; also absent: IER3, SLC2A1, SHB |
| [[RAB3B]] | B | RAB3B activity raises CCN2's level | lines that do not express RAB3B (17) vs lines expressing it (33) | 2.54× lower at baseline in the lines without RAB3B | 0.069 | ⚠ within organs, on part of the lines; also absent: C1QL1, CYS1, ACTN2 |
| [[FHL2]] | C | FHL2 activity lowers CCN2's level | lines that do not express FHL2 (4) vs lines expressing it (46) | 6.15× higher at baseline in the lines without FHL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EPS8, MYO1E, RUNX1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRIM1]] | B | CCN2 activity raises CRIM1's level | lines that do not express CCN2 (17) vs lines expressing it (33) | 1.85× lower at baseline in the lines without CCN2 | 0.003 | ⚠ within organs, on part of the lines; also absent: GDNF-AS1, CPEB1, TRIML2 |
| [[ITGB1]] | B | CCN2 activity raises ITGB1's level | lines that do not express CCN2 (17) vs lines expressing it (33) | 1.63× lower at baseline in the lines without CCN2 | 0.016 | ⚠ within organs, on part of the lines; also absent: GDNF-AS1, CPEB1, TRIML2 |
| [[RAB3B]] | B | CCN2 activity raises RAB3B's level | lines that do not express CCN2 (17) vs lines expressing it (33) | 2.70× lower at baseline in the lines without CCN2 | 0.017 | ⚠ within organs, on part of the lines; also absent: GDNF-AS1, CPEB1, TRIML2 |
| [[TEAD1]] | B | CCN2 activity strengthens TEAD1's drug response | lines that do not express CCN2 (17) vs lines expressing it (32) | the lines without CCN2 respond 0.77× as strongly (z diff +1.32); strongest at Homoharringtonine 0.5 µM: 1.23x vs 1.73x (z diff +3.9) | 0.033 | ⚠ within organs, on part of the lines; also absent: GDNF-AS1, CPEB1, TRIML2; target measured in part of the lines; artifact flags |
| [[CCN1]] | B | CCN2 activity raises CCN1's level | lines that do not express CCN2 (17) vs lines expressing it (33) | 2.36× lower at baseline in the lines without CCN2 | 0.068 | ⚠ within organs, on part of the lines; also absent: GDNF-AS1, CPEB1, TRIML2 |
| [[DNMBP]] | B | CCN2 activity raises DNMBP's level | lines that do not express CCN2 (17) vs lines expressing it (33) | 1.29× lower at baseline in the lines without CCN2 | 0.072 | ⚠ within organs, on part of the lines; also absent: GDNF-AS1, CPEB1, TRIML2 |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.765). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.5, 13.1); signed map (14.5, 40.8). **Vector** length 115, 33.2% of its response variance represented; |z| ≥ 3 in 1,051 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.8 | +19.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +4.1 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +4.1 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.5 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.4 | +1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.2 | +2.5 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -6.1 | -12.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.8 | -9.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.7 | -7.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -4.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.0 | -4.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.5 | -4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -8.0 |

## What is on record

|  |  |
|---|---|
| Name | cellular communication network factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.2 — chr6:131,948,176-131,951,372 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IGFBP8; previously CTGF |
| Gene groups (HGNC) | Cellular communication network factors |
| Hallmark sets | HYPOXIA, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 3 pathways, smallest: RUNX3 regulates YAP1-mediated transcription; YAP1- and WWTR1 (TAZ)-stimulated gene expression; Transcriptional regulation by RUNX3 |
| Matched by | ensembl_id |

**Function**, from UniProt [P29279](https://www.uniprot.org/uniprotkb/P29279) (CCN family member 2):

> Major connective tissue mitoattractant secreted by vascular endothelial cells. Promotes proliferation and differentiation of chondrocytes. Is involved in the stimulation of osteoblast differentiation and has a critical role in osteogenesis. Mediates heparin- and divalent cation-dependent cell adhesion in many cell types including fibroblasts, myofibroblasts, endothelial and epithelial cells. Enhances fibroblast growth factor-induced DNA synthesis.

**Summary**, from NCBI Gene [1490](https://www.ncbi.nlm.nih.gov/gene/1490):

> The protein encoded by this gene is a mitogen that is secreted by vascular endothelial cells. The encoded protein plays a role in chondrocyte proliferation and differentiation, cell adhesion in many cell types, and is related to platelet-derived growth factor. Certain polymorphisms in this gene have been linked with a higher incidence of systemic sclerosis. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:2500](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2500) · Entrez [1490](https://www.ncbi.nlm.nih.gov/gene/1490) · UniProt [P29279](https://www.uniprot.org/uniprotkb/P29279) · Ensembl [ENSG00000118523](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118523)

## Data

Gene col 4002: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4002); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4002, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4002]; `tensor/DDL_lfc|DDL_z.npy` [4002]; `embed/gene_vectors.npy` [4002]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4002 or target_col == 4002). Every well: [[CCN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
