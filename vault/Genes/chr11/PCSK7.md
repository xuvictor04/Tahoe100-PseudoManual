---
symbol: "PCSK7"
type: "gene"
col: 8362
ensembl_id: "ENSG00000160613"
name: "proprotein convertase subtilisin/kexin type 7"
location: "11q23.3"
module: 36
arm: "+"
pooled_cpm: 33.46
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# PCSK7

*proprotein convertase subtilisin/kexin type 7* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.21× (z +18.5, q 0e+00, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +17.5, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.693× (z -12.2, q 3e-31, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PITPNA]] (+0.69, fdr 1e-05), [[FAM118B]] (+0.68, fdr 7e-06), [[EMC8]] (+0.65, fdr 7e-06); moves opposite to [[CISD2]] (-0.57, fdr 3e-05), [[SLC25A30]] (-0.56, fdr 1e-05), [[CDC73]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KLKP1-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8362.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.21×** | +18.5 | 0e+00 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.18×** | +18.2 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.17×** | +18.1 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +17.5 | 0e+00 | 42/48 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +12.0 | 4e-31 | 40/47 (HEC-1-A, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.44×** | +10.7 | 1e-24 | 33/48 (SW480, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.55×** | +9.9 | 3e-21 | 30/47 (NCI-H2030, SW 900, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.13×** | +9.0 | 1e-17 | 32/47 (SW480, LoVo, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.46×** | +8.5 | 1e-15 | 29/48 (SW 900, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.41×** | +8.1 | 4e-14 | 27/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.33×** | +6.6 | 2e-09 | 24/48 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +6.5 | 3e-09 | 23/48 (PANC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.33×** | +6.4 | 5e-09 | 26/48 (PANC-1, Hs 766T, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +6.4 | 6e-09 | 18/48 (NCI-H2030, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.32×** | +6.2 | 2e-08 | 25/46 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.002 | 4/48 (MIA PaCa-2, HCT15, …) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.004 | 8/48 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.007 | 7/46 (HT-29, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 1.17× | +3.6 | 0.009 | 11/48 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.034 | 5/48 (SW480, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.058 | 10/46 (H4, NCI-H460, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.10× | +3.0 | 0.059 | 4/48 (PANC-1, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8362.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.693×** | -12.2 | 3e-31 | 39/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.739×** | -7.1 | 3e-10 | 25/48 (HS-578T, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.818×** | -6.7 | 5e-09 | 20/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.784×** | -5.7 | 2e-06 | 20/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.811×** | -4.9 | 1e-04 | 16/48 (PANC-1, SW 1088, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.741×** | -3.6 | 0.031 | 8/47 (KATO III, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.870× | -3.3 | 0.081 | 6/48 (SNU-423, CHP-212, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.871× | -3.3 | 0.081 | 11/48 (C32, SW480, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.874× | -3.2 | 0.097 | 3/48 (NCI-H2030, SNU-423, …) | inconsistent across doses | position effect removed |
| [[AZD-8055 (drug)]] 0.5 µM |  | 0.832× | -3.1 | 0.11 | 4/48 (AsPC-1, HS-578T, …) | two highest doses | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.878× | -3.1 | 0.11 | 8/48 (KATO III, RPMI-7951, …) | top dose only |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | 0.836× | -3.0 | 0.13 | 0/48 | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8362. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 59.3 | 5 (3 ⚠) | 4 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.16× (z +10.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.609× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 18.1 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +9.4) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 20.7 | 4 (4 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.72× (z +9.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 42.3 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 35.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +9.4) | — |
| [[LoVo (line)]] | wt | 31.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.43× (z +9.2) ⚠ cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.412× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 60.5 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.405× (z -9.6) |
| [[HT-29 (line)]] | alt | 52.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 32.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +9.1) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[Panc 03.27 (line)]] | alt | 32.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.6) | [[Selinexor (drug)]] 5 µM 0.431× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 22.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +9.7) | — |
| [[H4 (line)]] | wt | 23.4 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.156× (z -8.7) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 19.6 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0854× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 28.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +14.1) | — |
| [[NCI-H23 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0738× (z -19.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 37.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.4) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[SW 900 (line)]] | alt | 34.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.3) | — |
| [[A-172 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8362), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PITPNA]] | +0.69 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[FAM118B]] | +0.68 | +0.66 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[EMC8]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[HIRA]] | +0.59 | +0.49 / +0.56 | both halves | 2e-05 |  |
| [[FBXL18]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[PIK3R4]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[AREL1]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[TBC1D10B]] | +0.56 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[TRAPPC10]] | +0.54 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[MEF2B]] | +0.54 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[USP20]] | +0.54 | +0.30 / +0.56 | both halves | 2e-04 |  |
| [[ZNF324]] | +0.53 | +0.30 / +0.59 | both halves | 2e-04 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CISD2]] | -0.57 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[SLC25A30]] | -0.56 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[CDC73]] | -0.53 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[OGFRL1]] | -0.52 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ATP6V1B2]] | -0.50 | -0.28 / -0.63 | both halves | 3e-04 |  |
| [[SDCBP]] | -0.49 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[MATR3]] | -0.49 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[SUGT1P3]] | -0.48 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[NPM1]] | -0.48 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[SNX27]] | -0.48 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[LSMEM1]] | -0.47 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[NT5DC1]] | -0.47 | -0.36 / -0.41 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLKP1-1]] | B | KLKP1-1 activity raises PCSK7's level | lines that do not express KLKP1-1 (11) vs lines expressing it (39) | 1.22× lower at baseline in the lines without KLKP1-1 | 0.020 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PCSK7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.484). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-11.2, -17.3); signed map (-47.2, -23.7). **Vector** length 99.1, 23.3% of its response variance represented; |z| ≥ 3 in 1,063 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.2 | +10.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.5 | +9.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.9 | +12.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +17.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +3.7 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +2.1 | +3.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +3.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.9 | +2.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -10.1 | -12.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.6 | -6.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -6.0 | -7.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -5.8 | -5.7 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.1 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -1.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.6 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.4 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | proprotein convertase subtilisin/kexin type 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:117,204,337-117,232,525 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PC7, PC8, LPC, SPC7 |
| Gene groups (HGNC) | Proprotein convertase subtilisin/kexin family |
| Reactome | 8 pathways, smallest: Regulation of CDH1 posttranslational processing and trafficking to plasma membrane; Regulation of CDH1 Expression and Function; Regulation of Expression and Function of Type I Classical Cadherins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16549](https://www.uniprot.org/uniprotkb/Q16549) (Proprotein convertase subtilisin/kexin type 7):

> Serine endoprotease that processes various proproteins by cleavage at paired basic amino acids, recognizing the RXXX[KR]R consensus motif. Likely functions in the constitutive secretory pathway.

**Summary**, from NCBI Gene [9159](https://www.ncbi.nlm.nih.gov/gene/9159):

> This gene encodes a member of the subtilisin-like proprotein convertase family, which includes proteases that process protein and peptide precursors trafficking through regulated or constitutive branches of the secretory pathway. It encodes a type 1 membrane bound protease that is expressed in many tissues, including neuroendocrine, liver, gut, and brain. The encoded protein undergoes an initial autocatalytic processing event in the ER and then sorts to the trans-Golgi network through endosomes …

**Accessions** — [HGNC:8748](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8748) · Entrez [9159](https://www.ncbi.nlm.nih.gov/gene/9159) · UniProt [Q16549](https://www.uniprot.org/uniprotkb/Q16549) · Ensembl [ENSG00000160613](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160613)

## Data

Gene col 8362: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8362); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8362, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8362]; `tensor/DDL_lfc|DDL_z.npy` [8362]; `embed/gene_vectors.npy` [8362]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8362 or target_col == 8362). Every well: [[PCSK7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCSK7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
