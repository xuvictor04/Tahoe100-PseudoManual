---
symbol: "FJX1"
type: "gene"
col: 11033
ensembl_id: "ENSG00000179431"
name: "four-jointed box kinase 1"
location: "11p13"
module: 120
arm: "+"
pooled_cpm: 4.52
n_lines_expressing: 39
n_dd_up: 34
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 9
direction_downstream: 19
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# FJX1

*four-jointed box kinase 1* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 9.44× (z +21.5, q 0e+00, up in 23 of 24 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 7.94× (z +14.1, q 1e-42, up in 25 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.349× (z -7.1, q 6e-10, down in 19 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF462]] (+0.69, fdr 7e-06), [[SPRY2]] (+0.67, fdr 7e-06), [[ENC1]] (+0.65, fdr 7e-06); moves opposite to [[GET1]] (-0.64, fdr 7e-06), [[HSPB11]] (-0.64, fdr 7e-06), [[TM9SF2]] (-0.63, fdr 9e-06).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 19 go from it, the strongest it → [[ZC3H12C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 17 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11033.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **9.44×** | +21.5 | 0e+00 | 23/24 (A-172, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **8.71×** | +14.1 | 8e-43 | 29/31 (NCI-H460, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **7.94×** | +14.1 | 1e-42 | 25/25 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.52×** | +8.2 | 3e-14 | 2/8 (HOP62, SNU-423) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.65×** | +8.1 | 5e-14 | 6/8 (NCI-H460, J82, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **3.24×** | +8.0 | 1e-13 | 8/17 (NCI-H460, HS-578T, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.88×** | +7.2 | 5e-11 | 27/35 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.59×** | +6.5 | 7e-09 | 14/26 (A-172, HS-578T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **2.32×** | +5.5 | 3e-06 | 11/20 (A-172, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.02×** | +4.8 | 1e-04 | 13/35 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.7 | 1e-04 | 8/25 (A498, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~66% of this change | **1.97×** | +4.6 | 2e-04 | 8/16 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **3.57×** | +4.5 | 3e-04 | 13/27 (LOX-IMVI, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.94×** | +4.3 | 6e-04 | 15/30 (PANC-1, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.87×** | +4.2 | 8e-04 | 13/32 (NCI-H460, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **2.34×** | +4.0 | 0.002 | 10/23 (HOP62, SW480, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.75×** | +3.6 | 0.008 | 9/33 (NCI-H1792, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +3.5 | 0.011 | 10/31 (A-172, Hs 766T, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.025 | 6/35 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.58×** | +3.1 | 0.045 | 10/34 (HOP62, SW 900, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.37×** | +3.1 | 0.047 | 4/20 (A498, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.59×** | +3.0 | 0.049 | 5/28 (A-172, A-427, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.26×** | +2.9 | 0.071 | 1/25 (NCI-H460) | top dose only | noisy plate (z scaled); position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **2.25×** | +2.9 | 0.071 | 4/16 (SNU-423, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.53×** | +2.9 | 0.071 | 5/31 (A-427, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11033.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.349×** | -7.1 | 6e-10 | 19/36 (LOX-IMVI, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.421×** | -5.9 | 1e-06 | 21/33 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.515×** | -4.3 | 0.004 | 16/35 (LOX-IMVI, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.528×** | -4.2 | 0.005 | 14/29 (NCI-H2347, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.594×** | -3.8 | 0.017 | 14/35 (SK-MEL-2, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.600×** | -3.5 | 0.052 | 13/31 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.606×** | -3.4 | 0.057 | 9/33 (RPMI-7951, NCI-H2030, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.601× | -3.2 | 0.10 | 14/35 (HS-578T, MIA PaCa-2, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.633× | -3.1 | 0.12 | 11/33 (NCI-H460, HEC-1-A, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~82% of this change | 0.620× | -3.1 | 0.12 | 10/29 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.423× | -3.0 | 0.12 | 9/34 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.88 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11033. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 47.2 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0494× (z -18.4) |
| [[NCI-H460 (line)]] | wt | 8.26 | 5 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 27.2× (z +13.5) | — |
| [[A-172 (line)]] | wt | 6.79 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +15.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 20.2× (z +11.6) | — |
| [[A549 (line)]] | wt | 4.64 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 26.0× (z +13.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 23.0× (z +9.5) | — |
| [[J82 (line)]] | alt | 9.21 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.72× (z +13.2) ⚠ cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 5 µM 0.126× (z -9.0) |
| [[HOP62 (line)]] | alt | 3.46 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.5× (z +14.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[PANC-1 (line)]] | alt | 8.99 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 6.14× (z +9.2) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SNU-423 (line)]] | alt | 4.79 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 29.8× (z +14.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 3.04 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +11.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[CFPAC-1 (line)]] | alt | 1.77 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 31.6× (z +11.4) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[Hs 766T (line)]] | wt | 1.57 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +8.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 7.98 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.93× (z +8.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1573 (line)]] | alt | 2.01 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +9.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 4.98 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.11× (z +10.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[RKO (line)]] | wt | 9.81 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0833× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 2.40 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +8.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A-427 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.908 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.663 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.513 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.313 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.204 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.828 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.291 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.296 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11033), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF462]] | +0.69 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[SPRY2]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ENC1]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[POGLUT1]] | +0.65 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[UTP3]] | +0.64 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[RPL7L1]] | +0.63 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[TGIF2]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[TASOR]] | +0.63 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[SRGAP1]] | +0.62 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[CYREN]] | +0.62 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[ST7L]] | +0.62 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[ZC3H12C]] | +0.62 | +0.64 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GET1]] | -0.64 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[HSPB11]] | -0.64 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[TM9SF2]] | -0.63 | -0.63 / -0.57 | both halves | 9e-06 |  |
| [[SARAF]] | -0.62 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[SDHAP4]] | -0.62 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[NTAN1]] | -0.62 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[SEC11A]] | -0.62 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[SNX3]] | -0.61 | -0.67 / -0.56 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.61 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[F11R]] | -0.61 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[GNB2]] | -0.60 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[RPA1]] | -0.60 | -0.59 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises FJX1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MARCHF4]] | B | MARCHF4 activity raises FJX1's level | lines that do not express MARCHF4 (28) vs lines expressing it (22) | 2.17× lower at baseline in the lines without MARCHF4 | 0.033 | ⚠ within organs, on part of the lines; also absent: PAMR1, BASP1-AS1, ENSG00000282849 |
| [[F11R]] | B | F11R activity lowers FJX1's level | lines that do not express F11R (10) vs lines expressing it (40) | 1.79× higher at baseline in the lines without F11R | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000287306, LONRF3, TUBA4A |
| [[ZC3H12C]] | B | ZC3H12C activity raises FJX1's level | lines that do not express ZC3H12C (7) vs lines expressing it (43) | 2.08× lower at baseline in the lines without ZC3H12C | 0.067 | ⚠ within organs, on part of the lines; also absent: TMOD2, KLF12, DPF1 |
| [[DLX1]] | B | DLX1 activity raises FJX1's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 1.96× lower at baseline in the lines without DLX1 | 0.067 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |
| [[LTBP2]] | B | LTBP2 activity raises FJX1's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 2.03× lower at baseline in the lines without LTBP2 | 0.073 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[MAP2K2]] | B | MAP2K2 activity raises FJX1's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[LINC00702]] | B | LINC00702 activity raises FJX1's level | lines that do not express LINC00702 (25) vs lines expressing it (25) | 1.80× lower at baseline in the lines without LINC00702 | 0.091 | ⚠ within organs, on part of the lines; also absent: FGF5, ENSG00000253553, LNCOG |
| [[ETS1]] | B | ETS1 activity raises FJX1's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 2.05× lower at baseline in the lines without ETS1 | 0.099 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 19, C 0. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZC3H12C]] | B | FJX1 activity raises ZC3H12C's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 3.78× lower at baseline in the lines without FJX1 | 0.001 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[NEPRO-AS1]] | B | FJX1 activity raises NEPRO-AS1's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 1.90× lower at baseline in the lines without FJX1 | 0.008 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[ZBTB38]] | B | FJX1 activity raises ZBTB38's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 1.76× lower at baseline in the lines without FJX1 | 0.023 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[NAPB]] | B | FJX1 activity raises NAPB's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 1.31× lower at baseline in the lines without FJX1 | 0.029 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[FRMD6]] | B | FJX1 activity raises FRMD6's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 3.74× lower at baseline in the lines without FJX1 | 0.049 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[PTX3]] | B | FJX1 activity raises PTX3's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 4.63× lower at baseline in the lines without FJX1 | 0.057 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[ARHGAP31]] | B | FJX1 activity raises ARHGAP31's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 3.58× lower at baseline in the lines without FJX1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[CDC42EP3]] | B | FJX1 activity raises CDC42EP3's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 2.80× lower at baseline in the lines without FJX1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[LINC00702]] | B | FJX1 activity raises LINC00702's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 2.44× lower at baseline in the lines without FJX1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[TASOR]] | B | FJX1 activity raises TASOR's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 1.49× lower at baseline in the lines without FJX1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[CDK17]] | B | FJX1 activity raises CDK17's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 1.53× lower at baseline in the lines without FJX1 | 0.066 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[SMG9]] | B | FJX1 activity raises SMG9's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 1.23× lower at baseline in the lines without FJX1 | 0.067 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.703). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.6, 12.7); signed map (15.6, 40.9). **Vector** length 77.2, 18.4% of its response variance represented; |z| ≥ 3 in 778 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +7.5 | +21.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +7.1 | +14.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +14.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +4.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.8 | +4.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -3.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.5 | -4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.5 | -5.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.4 | -7.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | four-jointed box kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:35,618,460-35,620,865 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22416, FLJ25593 |
| Gene groups (HGNC) | Golgi associated kinase family |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VR8](https://www.uniprot.org/uniprotkb/Q86VR8) (Four-jointed box protein 1):

> Acts as an inhibitor of dendrite extension and branching.

**Summary**, from NCBI Gene [24147](https://www.ncbi.nlm.nih.gov/gene/24147):

> The protein encoded by this gene is the human ortholog of mouse and Drosophila four-jointed gene product. The Drosophila protein is important for growth and differentiation of legs and wings, and for proper development of the eyes. The exact function of this gene in humans is not known. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17166](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17166) · Entrez [24147](https://www.ncbi.nlm.nih.gov/gene/24147) · UniProt [Q86VR8](https://www.uniprot.org/uniprotkb/Q86VR8) · Ensembl [ENSG00000179431](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179431)

## Data

Gene col 11033: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11033); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11033, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11033]; `tensor/DDL_lfc|DDL_z.npy` [11033]; `embed/gene_vectors.npy` [11033]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11033 or target_col == 11033). Every well: [[FJX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FJX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
