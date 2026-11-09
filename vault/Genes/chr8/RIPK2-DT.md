---
symbol: "RIPK2-DT"
type: "gene"
col: 14739
ensembl_id: "ENSG00000251136"
name: "palmitic acid regulated anti-inflammatory lncRNA"
location: "8q21.3"
module: 68
arm: "+"
pooled_cpm: 89.9
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 13
n_dd_up_clean: 20
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 16
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# RIPK2-DT

*palmitic acid regulated anti-inflammatory lncRNA* — 8q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.61× (z +23.8, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.533× (z -7.0, q 2e-09, down in 36 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.593× (z -5.8, q 8e-07, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PATL2]] (+0.83, fdr 7e-06), [[PCNX4-DT]] (+0.77, fdr 5e-05), [[TTC6]] (+0.74, fdr 7e-06); moves opposite to [[LPCAT4]] (-0.72, fdr 1e-05), [[MPG]] (-0.72, fdr 1e-05), [[TAF5L]] (-0.72, fdr 7e-06).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[TLR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14739.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.61×** | +23.8 | 0e+00 | 46/47 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.11×** | +12.5 | 2e-33 | 44/47 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.53×** | +9.8 | 2e-20 | 41/47 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.52×** | +6.5 | 8e-09 | 41/47 (A-427, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.85×** | +6.5 | 8e-09 | 40/46 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.64×** | +5.2 | 2e-05 | 41/46 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.54×** | +4.5 | 5e-04 | 35/49 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.38×** | +4.5 | 5e-04 | 36/47 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.003 | 31/47 (J82, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.9 | 0.005 | 32/48 (NCI-H1792, KATO III, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.005 | 33/47 (C-33 A, KATO III, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.46×** | +3.8 | 0.006 | 30/47 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.006 | 26/47 (NCI-H1792, A-172, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.93×** | +3.8 | 0.006 | 33/49 (CFPAC-1, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.013 | 27/47 (CFPAC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.015 | 25/48 (CFPAC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.018 | 32/47 (Hs 766T, CFPAC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14739.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.533×** | -7.0 | 2e-09 | 36/47 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.544×** | -6.5 | 3e-08 | 35/46 (RKO, SW 1271, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.567×** | -6.3 | 6e-08 | 38/47 (COLO 205, HT-29, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.571×** | -6.2 | 8e-08 | 35/47 (COLO 205, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.593×** | -5.8 | 8e-07 | 39/47 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.597×** | -5.7 | 1e-06 | 37/47 (PANC-1, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.624×** | -5.2 | 1e-05 | 33/47 (COLO 205, SW480, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.647×** | -4.8 | 1e-04 | 35/47 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.670×** | -4.2 | 0.002 | 28/47 (CFPAC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.728×** | -3.5 | 0.024 | 28/47 (COLO 205, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~73% of this change | **0.732×** | -3.5 | 0.027 | 28/47 (RPMI-7951, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.733×** | -3.4 | 0.027 | 25/47 (COLO 205, PANC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.752×** | -3.2 | 0.066 | 22/47 (COLO 205, SW480, …) | all doses, flat | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14739. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 193 | 0 | 10 (10 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.232× (z -12.5) ⚠ cell-cycle shift, explains ~68% of this change |
| [[PANC-1 (line)]] | alt | 123 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +22.4) | [[Digitoxin (drug)]] 5 µM 0.339× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[SW480 (line)]] | alt | 45.8 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +15.1) | [[Digitoxin (drug)]] 5 µM 0.233× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 67.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +20.6) | — |
| [[LoVo (line)]] | wt | 55.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.71× (z +28.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.376× (z -8.5) ⚠ toxic |
| [[HOP62 (line)]] | alt | 63.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.15× (z +23.8) | — |
| [[J82 (line)]] | alt | 70.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +27.4) | — |
| [[LS 180 (line)]] | wt | 33.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +14.9) | — |
| [[NCI-H1573 (line)]] | alt | 117 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +23.4) | — |
| [[NCI-H2347 (line)]] | alt | 51.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.98× (z +22.8) | — |
| [[NCI-H460 (line)]] | wt | 74.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +21.2) | — |
| [[RKO (line)]] | wt | 85.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 180 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +14.0) | — |
| [[SW48 (line)]] | wt | 51.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +21.1) | — |
| [[A-427 (line)]] | wt | 73.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +13.8) | — |
| [[BT-474 (line)]] | alt | 81.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +21.6) | — |
| [[C-33 A (line)]] | alt | 82.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +15.5) | — |
| [[HEC-1-A (line)]] | alt | 75.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +17.5) | — |
| [[HepG2_C3A (line)]] | wt | 70.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.247× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 149 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +16.4) | — |
| [[HT-29 (line)]] | alt | 63.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +15.6) | [[Panobinostat (drug)]] 0.5 µM 0.348× (z -9.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[hTERT-HPNE (line)]] | wt | 102 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.83× (z +15.4) | — |
| [[LOX-IMVI (line)]] | wt | 105 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +18.8) | — |
| [[NCI-H1792 (line)]] | alt | 89.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +14.5) | [[Digitoxin (drug)]] 5 µM 0.241× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[Panc 03.27 (line)]] | alt | 64.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +16.4) | — |
| [[RPMI-7951 (line)]] | alt | 116 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +16.0) | — |
| [[SNU-423 (line)]] | alt | 122 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +15.4) | — |
| [[SW 1271 (line)]] | alt | 109 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +9.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0917× (z -9.7) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 68.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +12.1) | — |
| [[AsPC-1 (line)]] | alt | 36.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +13.2) | — |
| [[C32 (line)]] | wt | 250 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +9.8) | — |
| [[CHP-212 (line)]] | wt | 69.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.25× (z +14.1) | — |
| [[H4 (line)]] | wt | 150 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +11.3) | — |
| [[HCT15 (line)]] | alt | 53.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +16.1) | — |
| [[Hs 766T (line)]] | wt | 107 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +17.6) | — |
| [[KATO III (line)]] | alt | 49.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +11.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 37.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +16.0) | — |
| [[NCI-H2030 (line)]] | alt | 132 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +16.0) | — |
| [[NCI-H23 (line)]] | alt | 66.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +18.9) | — |
| [[SNU-1 (line)]] | wt | 55.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +15.5) | — |
| [[SW 900 (line)]] | alt | 75.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +12.2) | — |
| [[SW1417 (line)]] | alt | 33.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.9) | — |
| [[A498 (line)]] | wt | 179 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 83.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 67.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14739), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATL2]] | +0.83 | +0.87 / +0.62 | both halves | 7e-06 |  |
| [[PCNX4-DT]] | +0.77 | +0.84 / +0.40 | both halves | 5e-05 |  |
| [[TTC6]] | +0.74 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[AK9]] | +0.74 | +0.83 / +0.39 | both halves | 5e-05 |  |
| [[LINC00240]] | +0.74 | +0.78 / +0.44 | both halves | 3e-05 |  |
| [[WARS2-AS1]] | +0.74 | +0.78 / +0.38 | both halves | 6e-05 |  |
| [[ARRDC3-AS1]] | +0.73 | +0.76 / +0.49 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.73 | +0.79 / +0.37 | both halves | 8e-05 |  |
| [[DNAH12]] | +0.72 | +0.80 / +0.46 | both halves | 3e-05 |  |
| [[PDCL3P4]] | +0.72 | +0.85 / +0.37 | both halves | 9e-05 |  |
| [[KRCC1]] | +0.72 | +0.81 / +0.37 | both halves | 8e-05 |  |
| [[TMEM202-AS1]] | +0.72 | +0.77 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPCAT4]] | -0.72 | -0.74 / -0.51 | both halves | 1e-05 |  |
| [[MPG]] | -0.72 | -0.76 / -0.52 | both halves | 1e-05 |  |
| [[TAF5L]] | -0.72 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[XYLT2]] | -0.70 | -0.69 / -0.56 | both halves | 1e-05 |  |
| [[MMS19]] | -0.70 | -0.74 / -0.51 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.69 | -0.69 / -0.42 | both halves | 4e-05 |  |
| [[SDHAP1]] | -0.69 | -0.74 / -0.50 | both halves | 1e-05 |  |
| [[TSEN54]] | -0.69 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[IMPDH1]] | -0.69 | -0.74 / -0.48 | both halves | 2e-05 |  |
| [[ANKRD27]] | -0.69 | -0.72 / -0.32 | both halves | 2e-04 |  |
| [[ZDHHC9]] | -0.68 | -0.73 / -0.49 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.68 | -0.67 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLR1]] | B | TLR1 activity raises RIPK2-DT's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 1.73× lower at baseline in the lines without TLR1 | 0.009 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[TLR6]] | B | TLR6 activity raises RIPK2-DT's level | lines that do not express TLR6 (16) vs lines expressing it (34) | 1.76× lower at baseline in the lines without TLR6 | 0.017 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent |
| [[SYNPO2]] | B | SYNPO2 activity raises RIPK2-DT's level | lines that do not express SYNPO2 (5) vs lines expressing it (45) | 2.04× lower at baseline in the lines without SYNPO2 | 0.018 | ⚠ within organs, on part of the lines; also absent: RIPOR3, PER3, TESK2; maybe low, not absent |
| [[ABCA10]] | B | ABCA10 activity raises RIPK2-DT's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.45× lower at baseline in the lines without ABCA10 | 0.030 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[GNGT1]] | B | GNGT1 activity lowers RIPK2-DT's level | lines that do not express GNGT1 (30) vs lines expressing it (20) | 1.33× higher at baseline in the lines without GNGT1 | 0.038 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3 |
| [[ZNF474]] | B | ZNF474 activity raises RIPK2-DT's level | lines that do not express ZNF474 (6) vs lines expressing it (44) | 2.04× lower at baseline in the lines without ZNF474 | 0.039 | ⚠ within organs, on part of the lines; also absent: RBFOX1, NEK10, LINC01524; maybe low, not absent |
| [[CACNA2D1]] | B | CACNA2D1 activity raises RIPK2-DT's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 1.54× lower at baseline in the lines without CACNA2D1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169 |
| [[SSPN]] | B | SSPN activity raises RIPK2-DT's level | lines that do not express SSPN (15) vs lines expressing it (35) | 1.69× lower at baseline in the lines without SSPN | 0.052 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent |
| [[KYNU]] | B | KYNU activity raises RIPK2-DT's level | lines that do not express KYNU (29) vs lines expressing it (21) | 1.66× lower at baseline in the lines without KYNU | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[DPY19L2]] | B | DPY19L2 activity raises RIPK2-DT's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 1.57× lower at baseline in the lines without DPY19L2 | 0.055 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ |
| [[BMPR1B]] | B | BMPR1B activity raises RIPK2-DT's level | lines that do not express BMPR1B (28) vs lines expressing it (22) | 1.60× lower at baseline in the lines without BMPR1B | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, SLC6A17, EPHA5-AS1 |
| [[SMCO2]] | B | SMCO2 activity raises RIPK2-DT's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.21× lower at baseline in the lines without SMCO2 | 0.060 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.849). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (15.2, 12.9); signed map (24.5, -6.8). **Vector** length 145, 53.4% of its response variance represented; |z| ≥ 3 in 1,349 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +15.1 | +23.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +13.8 | +12.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +13.4 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +9.2 | +0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +8.0 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.9 | +4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.0 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +2.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +4.9 | +5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.8 | +3.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -9.1 | -6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -9.0 | -6.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -8.0 | -5.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.6 | -4.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | -0.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.7 | -1.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.7 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | +0.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -3.4 | -2.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | palmitic acid regulated anti-inflammatory lncRNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q21.3 — chr8:89,545,424-89,757,812 (-) |
| Ensembl biotype | lncRNA |
| Also known as | AF117829.1; previously RIPK2-DT |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55545](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55545) · Entrez [101929709](https://www.ncbi.nlm.nih.gov/gene/101929709) · Ensembl [ENSG00000251136](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251136)

## Data

Gene col 14739: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14739); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14739, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14739]; `tensor/DDL_lfc|DDL_z.npy` [14739]; `embed/gene_vectors.npy` [14739]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14739 or target_col == 14739). Every well: [[RIPK2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIPK2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
