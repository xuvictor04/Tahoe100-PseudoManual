---
symbol: "MAPKAPK2"
type: "gene"
col: 8594
ensembl_id: "ENSG00000162889"
name: "MAPK activated protein kinase 2"
location: "1q32.1"
module: 160
arm: "+"
pooled_cpm: 103.01
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# MAPKAPK2

*MAPK activated protein kinase 2* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.73× (z +12.5, q 4e-33, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.687× (z -12.1, q 9e-31, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLF13]] (+0.70, fdr 7e-06), [[LRRC8A]] (+0.68, fdr 7e-06), [[NECTIN2]] (+0.68, fdr 7e-06); moves opposite to [[PHC3]] (-0.66, fdr 1e-05), [[TRUB1]] (-0.64, fdr 7e-06), [[CHIC1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8594.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.73×** | +12.5 | 4e-33 | 40/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +12.2 | 5e-32 | 34/49 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +10.1 | 7e-22 | 39/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +9.3 | 2e-18 | 34/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.87×** | +6.8 | 8e-10 | 37/49 (C32, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +6.8 | 9e-10 | 34/48 (NCI-H460, SNU-423, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.32×** | +6.4 | 1e-08 | 29/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.29×** | +5.8 | 6e-07 | 26/48 (NCI-H460, SW480, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +5.6 | 1e-06 | 30/48 (A-172, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.27×** | +5.5 | 2e-06 | 28/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.28×** | +5.4 | 4e-06 | 27/47 (NCI-H460, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.26×** | +5.2 | 9e-06 | 23/48 (NCI-H460, SNU-423, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +5.0 | 2e-05 | 27/48 (SW48, C32, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.22×** | +4.6 | 2e-04 | 23/48 (PANC-1, RKO, …) | inconsistent across doses | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.10× | +3.2 | 0.052 | 9/48 (NCI-H460, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8594.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.687×** | -12.1 | 9e-31 | 40/48 (AsPC-1, C32, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.651×** | -9.8 | 4e-20 | 41/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.695×** | -8.3 | 2e-14 | 34/48 (HT-29, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.725×** | -7.3 | 4e-11 | 35/48 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.729×** | -6.9 | 6e-10 | 35/47 (RKO, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.763×** | -6.1 | 8e-08 | 29/49 (SW480, Hs 766T, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.766×** | -6.1 | 1e-07 | 28/48 (LoVo, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.774×** | -5.8 | 4e-07 | 31/49 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.758×** | -5.8 | 4e-07 | 34/48 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.804×** | -4.9 | 4e-05 | 25/48 (hTERT-HPNE, NCI-H2347, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.860× | -4.9 | 6e-05 | 18/48 (AsPC-1, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.808×** | -4.7 | 1e-04 | 26/50 (RKO, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.806×** | -4.7 | 1e-04 | 26/48 (SW480, RKO, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.826×** | -4.3 | 5e-04 | 22/48 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.826×** | -4.3 | 5e-04 | 20/47 (AsPC-1, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.877× | -4.2 | 0.001 | 11/48 (SW480, Hs 766T, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.829×** | -4.1 | 0.001 | 19/49 (SNU-423, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8594. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 82.8 | 12 (9 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.11× (z +17.0) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +16.5) | — |
| [[C32 (line)]] | wt | 99.2 | 6 (4 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 3.71× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.81× (z +9.8) | [[Selinexor (drug)]] 5 µM 0.453× (z -10.7) |
| [[HT-29 (line)]] | alt | 121 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.396× (z -11.6) |
| [[A-172 (line)]] | wt | 98.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.42× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 184 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.484× (z -13.3) |
| [[LoVo (line)]] | wt | 109 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.436× (z -12.2) |
| [[PANC-1 (line)]] | alt | 63.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 1.96× (z +9.4) | — |
| [[RKO (line)]] | wt | 122 | 0 | 3 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.452× (z -9.9) |
| [[A498 (line)]] | wt | 221 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 111 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.494× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 79.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +12.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.293× (z -11.3) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 56.3 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.383× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.561× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 144 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 1.99× (z +11.1) | — |
| [[SW480 (line)]] | alt | 81.2 | 0 | 2 | — | [[Selinexor (drug)]] 0.5 µM 0.455× (z -10.5) |
| [[A-427 (line)]] | wt | 54.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 59.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.418× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 90.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.147× (z -17.5) ⚠ toxic |
| [[HS-578T (line)]] | alt | 106 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.624× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 80.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 98.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.536× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 102 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.15× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.416× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 102 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +10.7) | — |
| [[SW 1088 (line)]] | alt | 105 | 0 | 1 | — | [[Sulfatinib (drug)]] 0.5 µM 0.0895× (z -10.1) |
| [[SW 900 (line)]] | alt | 300 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.390× (z -9.6) |
| [[SW48 (line)]] | wt | 92.9 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 7.66× (z +8.6) | — |
| [[A549 (line)]] | wt | 80.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 91.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 189 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 82.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 104 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8594), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF13]] | +0.70 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[LRRC8A]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[NECTIN2]] | +0.68 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[INPP5K]] | +0.66 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[RALY]] | +0.65 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[PITPNA]] | +0.64 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[GATAD2A]] | +0.63 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[FBRSL1]] | +0.63 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[EHBP1L1]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[GRK6]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[RCOR1]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[DUSP5]] | +0.62 | +0.64 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHC3]] | -0.66 | -0.62 / -0.53 | both halves | 1e-05 | pathway: Cellular Senescence; STRING 507 |
| [[TRUB1]] | -0.64 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[CHIC1]] | -0.63 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[RAD52]] | -0.62 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[MIX23]] | -0.60 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[ZNF280D]] | -0.60 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[MTX3]] | -0.59 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[THUMPD2]] | -0.59 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[RRAGB]] | -0.58 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[ZFR]] | -0.58 | -0.62 / -0.38 | both halves | 6e-05 |  |
| [[XPO1]] | -0.58 | -0.47 / -0.54 | both halves | 2e-05 | pathway: Regulation of mRNA stability by proteins that bind AU-rich elements |
| [[ARMCX5-GPRASP2]] | -0.57 | -0.52 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises MAPKAPK2's level | compounds that target MAP2K1: 3 of 4 lower it (Cobimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **+** arm (projection on the module's main direction 0.783). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (12.7, 0.3); signed map (-13.0, 39.3). **Vector** length 136, 42.1% of its response variance represented; |z| ≥ 3 in 1,344 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +12.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.7 | +10.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.7 | +9.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.6 | +12.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +5.4 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +5.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.7 | +1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +1.0 |
|  | [[Rimonabant (drug)]] 5 µM |  | +2.2 | +1.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -12.4 | -12.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -8.2 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.2 | -8.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.7 | -6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.0 | -7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.9 | -4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.0 | -6.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.1 | -5.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.0 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | MAPK activated protein kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:206,684,905-206,734,281 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MK2 |
| Gene groups (HGNC) | MAPK activated protein kinases; MAPKAPK family |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 50 pathways, smallest: CREB phosphorylation; Synthesis of Leukotrienes (LT) and Eoxins (EX); p38MAPK events |
| Matched by | ensembl_id |

**Function**, from UniProt [P49137](https://www.uniprot.org/uniprotkb/P49137) (MAP kinase-activated protein kinase 2):

> Stress-activated serine/threonine-protein kinase involved in cytokine production, endocytosis, reorganization of the cytoskeleton, cell migration, cell cycle control, chromatin remodeling, DNA damage response and transcriptional regulation. Following stress, it is phosphorylated and activated by MAP kinase p38-alpha/MAPK14, leading to phosphorylation of substrates. Phosphorylates serine in the peptide sequence, Hyd-X-R-X(2)-S, where Hyd is a large hydrophobic residue. Phosphorylates ALOX5, …

**Summary**, from NCBI Gene [9261](https://www.ncbi.nlm.nih.gov/gene/9261):

> This gene encodes a member of the Ser/Thr protein kinase family. This kinase is regulated through direct phosphorylation by p38 MAP kinase. In conjunction with p38 MAP kinase, this kinase is known to be involved in many cellular processes including stress and inflammatory responses, nuclear export, gene expression regulation and cell proliferation. Heat shock protein HSP27 was shown to be one of the substrates of this kinase in vivo. Two transcript variants encoding two different isoforms have …

**Accessions** — [HGNC:6887](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6887) · Entrez [9261](https://www.ncbi.nlm.nih.gov/gene/9261) · UniProt [P49137](https://www.uniprot.org/uniprotkb/P49137) · Ensembl [ENSG00000162889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162889)

## Data

Gene col 8594: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8594); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8594, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8594]; `tensor/DDL_lfc|DDL_z.npy` [8594]; `embed/gene_vectors.npy` [8594]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8594 or target_col == 8594). Every well: [[MAPKAPK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPKAPK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
