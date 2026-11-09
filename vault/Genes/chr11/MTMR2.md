---
symbol: "MTMR2"
type: "gene"
col: 1476
ensembl_id: "ENSG00000087053"
name: "myotubularin related protein 2"
location: "11q21"
module: 25
arm: "+"
pooled_cpm: 69.6
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# MTMR2

*myotubularin related protein 2* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.33× (z +13.6, q 2e-39, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.501× (z -16.3, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM98B]] (+0.69, fdr 7e-06), [[FKTN]] (+0.65, fdr 1e-05), [[EWSR1]] (+0.65, fdr 3e-05); moves opposite to [[INAFM1]] (-0.67, fdr 7e-06), [[CDC34]] (-0.66, fdr 4e-05), [[ARID3A]] (-0.65, fdr 5e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1476.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.33×** | +13.6 | 2e-39 | 47/49 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.30×** | +9.4 | 1e-18 | 39/48 (SW480, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +6.4 | 4e-08 | 29/48 (NCI-H1573, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +5.7 | 2e-06 | 27/48 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +5.6 | 2e-06 | 25/48 (LS 180, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +5.5 | 4e-06 | 28/48 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.7 | 2e-04 | 22/48 (LoVo, COLO 205, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +4.4 | 8e-04 | 19/47 (LOX-IMVI, SW48, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.6 | 0.020 | 14/37 (SW480, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.6 | 0.021 | 21/48 (A-427, SW 900, …) | top dose only | composition shift |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.023 | 15/48 (HEC-1-A, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.11× | +3.4 | 0.035 | 3/48 (LoVo, A-172, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.041 | 8/48 (HT-29, A549, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.10× | +3.2 | 0.064 | 12/48 (KATO III, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.15× | +3.1 | 0.084 | 13/48 (HOP62, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1476.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.501×** | -16.3 | 0e+00 | 46/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.508×** | -15.9 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.546×** | -14.2 | 1e-43 | 46/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.754×** | -9.4 | 8e-19 | 33/49 (RKO, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.817×** | -6.7 | 2e-09 | 31/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.755×** | -6.6 | 4e-09 | 35/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.792×** | -5.3 | 1e-05 | 27/47 (HepG2/C3A, AN3 CA, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~10% of this change | **0.816×** | -4.8 | 1e-04 | 23/48 (RPMI-7951, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.812×** | -4.7 | 2e-04 | 26/50 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.817×** | -4.6 | 3e-04 | 23/48 (A498, LOX-IMVI, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.826×** | -4.5 | 3e-04 | 23/48 (SW1417, SK-MEL-2, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.755×** | -4.0 | 0.003 | 18/48 (Hs 766T, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.743×** | -3.4 | 0.033 | 13/48 (MIA PaCa-2, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.868× | -3.3 | 0.033 | 18/49 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | 0.767× | -3.0 | 0.10 | 7/49 (Panc 03.27, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1476. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 114 | 4 (1 ⚠) | 4 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.32× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.93× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.333× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 67.0 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 4.39× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.408× (z -11.5) |
| [[SW480 (line)]] | alt | 114 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 4.97× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.346× (z -15.9) |
| [[LOX-IMVI (line)]] | wt | 98.3 | 1 | 3 | [[TAK-901 (drug)]] 0.05 µM 2.22× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.348× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 48.7 | 3 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 9.41× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.444× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 65.7 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 7.40× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.375× (z -10.5) |
| [[PANC-1 (line)]] | alt | 96.0 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 4.25× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.488× (z -11.0) |
| [[A-427 (line)]] | wt | 80.2 | 2 (2 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 2.23× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.475× (z -8.9) |
| [[HOP62 (line)]] | alt | 53.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.426× (z -10.3) |
| [[KATO III (line)]] | alt | 70.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.430× (z -9.3) |
| [[RKO (line)]] | wt | 93.9 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.63× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -11.3) |
| [[BT-474 (line)]] | alt | 30.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.5× (z +9.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.256× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 81.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -9.1) |
| [[Hs 766T (line)]] | wt | 66.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.409× (z -9.4) |
| [[HS-578T (line)]] | alt | 92.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.376× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 43.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.358× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 66.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.435× (z -10.3) |
| [[SW1417 (line)]] | alt | 76.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.457× (z -8.5) |
| [[A-172 (line)]] | wt | 32.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 51.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.517× (z -8.6) |
| [[AN3 CA (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 63.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.14× (z +9.7) | — |
| [[CHP-212 (line)]] | wt | 89.7 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.221× (z -8.5) |
| [[LS 180 (line)]] | wt | 49.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.46× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 55.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.530× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 104 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.387× (z -9.6) |
| [[SHP-77 (line)]] | alt | 85.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.451× (z -9.1) |
| [[SW 1088 (line)]] | alt | 72.3 | 0 | 1 | — | [[Nevirapine (drug)]] 0.5 µM 0.0685× (z -9.4) |
| [[SW 900 (line)]] | alt | 86.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.416× (z -8.6) |
| [[A549 (line)]] | wt | 54.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 70.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 78.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 49.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 89.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1476), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM98B]] | +0.69 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[FKTN]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[EWSR1]] | +0.65 | +0.43 / +0.68 | both halves | 3e-05 |  |
| [[ATP5PB]] | +0.64 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[ZDHHC21]] | +0.63 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[TMX3]] | +0.63 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[IPO8]] | +0.63 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[PGGT1B]] | +0.63 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[GMFB]] | +0.62 | +0.37 / +0.71 | both halves | 7e-05 |  |
| [[ACTR3]] | +0.62 | +0.57 / +0.70 | both halves | 9e-06 |  |
| [[METAP1D]] | +0.62 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[PRTFDC1]] | +0.61 | +0.41 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INAFM1]] | -0.67 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[CDC34]] | -0.66 | -0.43 / -0.66 | both halves | 4e-05 |  |
| [[ARID3A]] | -0.65 | -0.39 / -0.67 | both halves | 5e-05 |  |
| [[PPFIA1]] | -0.64 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[TESK2]] | -0.64 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[TULP3]] | -0.63 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[ARFGAP3]] | -0.63 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[RALGDS]] | -0.62 | -0.27 / -0.65 | both halves | 3e-04 |  |
| [[RBM38]] | -0.62 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[PDXK]] | -0.61 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[CDKN2D]] | -0.61 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[ULK1]] | -0.60 | -0.35 / -0.56 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MTMR2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.655). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-33.1, -26.5); signed map (12.7, -40.5). **Vector** length 90.9, 22.4% of its response variance represented; |z| ≥ 3 in 1,063 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +7.0 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.4 | +0.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.8 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.7 | +0.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +13.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +9.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | -0.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.4 | +2.2 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.3 | -15.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -16.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -14.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.7 | +1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.4 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -1.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | myotubularin related protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:95,821,766-95,925,315 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1073; previously CMT4B |
| Gene groups (HGNC) | Myotubularins; Phosphoinositide phosphatases |
| Reactome | 7 pathways, smallest: Synthesis of PIPs at the ER membrane; Synthesis of PIPs at the late endosome membrane; Synthesis of PIPs at the early endosome membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13614](https://www.uniprot.org/uniprotkb/Q13614) (Phosphatidylinositol-3,5-bisphosphate 3-phosphatase MTMR2):

> Lipid phosphatase that specifically dephosphorylates the D-3 position of phosphatidylinositol 3-phosphate and phosphatidylinositol 3,5-bisphosphate, generating phosphatidylinositol and phosphatidylinositol 5-phosphate. Regulates the level of these phosphoinositides critical for various biological processes including autophagy initiation and autophagosome maturation.

**Summary**, from NCBI Gene [8898](https://www.ncbi.nlm.nih.gov/gene/8898):

> This gene is a member of the myotubularin family of phosphoinositide lipid phosphatases. The encoded protein possesses phosphatase activity towards phosphatidylinositol-3-phosphate and phosphatidylinositol-3,5-bisphosphate. Mutations in this gene are a cause of Charcot-Marie-Tooth disease type 4B, an autosomal recessive demyelinating neuropathy. Alternatively spliced transcript variants encoding multiple isoforms have been found for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:7450](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7450) · Entrez [8898](https://www.ncbi.nlm.nih.gov/gene/8898) · UniProt [Q13614](https://www.uniprot.org/uniprotkb/Q13614) · Ensembl [ENSG00000087053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087053)

## Data

Gene col 1476: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1476); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1476, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1476]; `tensor/DDL_lfc|DDL_z.npy` [1476]; `embed/gene_vectors.npy` [1476]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1476 or target_col == 1476). Every well: [[MTMR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTMR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
