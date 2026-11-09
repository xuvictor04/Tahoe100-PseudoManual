---
symbol: "RC3H2"
type: "gene"
col: 639
ensembl_id: "ENSG00000056586"
name: "ring finger and CCCH-type domains 2"
location: "9q33.2"
module: 68
arm: "+"
pooled_cpm: 101.19
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# RC3H2

*ring finger and CCCH-type domains 2* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.58× (z +17.3, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.746× (z -7.9, q 2e-12, down in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.771× (z -7.0, q 7e-10, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF146]] (+0.74, fdr 1e-05), [[DDX6]] (+0.73, fdr 1e-05), [[PBLD]] (+0.73, fdr 1e-04); moves opposite to [[ST6GALNAC4]] (-0.72, fdr 3e-05), [[LPCAT4]] (-0.67, fdr 4e-05), [[SMG1P2]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[OGFRL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 639.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +17.3 | 0e+00 | 43/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +11.9 | 2e-30 | 40/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +10.9 | 3e-25 | 42/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +8.9 | 6e-17 | 36/48 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.20×** | +7.0 | 2e-10 | 22/48 (J82, HT-29, …) | rises with dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.8 | 7e-07 | 32/50 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.24×** | +5.7 | 8e-07 | 26/48 (BT-474, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.20×** | +5.0 | 4e-05 | 23/48 (A498, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +5.0 | 4e-05 | 15/48 (SW1417, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +4.0 | 0.003 | 19/44 (NCI-H23, NCI-H1573, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +4.0 | 0.004 | 16/49 (SW1417, Panc 03.27, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.15× | +3.4 | 0.032 | 9/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.13× | +3.4 | 0.032 | 8/49 (J82, LOX-IMVI, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.053 | 12/50 (SW480, BT-474, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.13× | +3.1 | 0.066 | 14/47 (Panc 03.27, HepG2/C3A, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.09× | +3.0 | 0.080 | 5/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 639.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.746×** | -7.9 | 2e-12 | 36/48 (CFPAC-1, KATO III, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.771×** | -7.0 | 7e-10 | 35/48 (SW480, J82, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.772×** | -6.9 | 7e-10 | 31/48 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.779×** | -6.7 | 3e-09 | 32/48 (NCI-H1792, A-427, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.780×** | -6.6 | 3e-09 | 27/48 (SK-MEL-2, CFPAC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.784×** | -6.5 | 7e-09 | 31/48 (SNU-423, LoVo, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.793×** | -6.2 | 5e-08 | 26/48 (MIA PaCa-2, H4, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.798×** | -6.1 | 1e-07 | 32/48 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | 0.839× | -4.5 | 4e-04 | 23/47 (NCI-H460, AN3 CA, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.898× | -4.1 | 0.003 | 9/48 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.861× | -3.8 | 0.008 | 17/48 (C-33 A, SW480, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.772×** | -3.6 | 0.013 | 20/45 (SW48, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.831×** | -3.5 | 0.018 | 14/49 (HS-578T, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.967× | -3.1 | 0.089 | 0/50 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 639. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 115 | 4 | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.8) | [[Auranofin (drug)]] 5 µM 0.494× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 118 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +20.0) | [[Digitoxin (drug)]] 5 µM 0.533× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[RKO (line)]] | wt | 134 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.0934× (z -28.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 120 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +11.0) | [[Digitoxin (drug)]] 5 µM 0.501× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[BT-474 (line)]] | alt | 188 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.527× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 89.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.9) | [[Belinostat (drug)]] 0.5 µM 0.549× (z -8.6) ⚠ cell-cycle shift, explains ~17% of this change |
| [[NCI-H23 (line)]] | alt | 88.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +19.8) | — |
| [[PANC-1 (line)]] | alt | 83.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +22.4) | — |
| [[H4 (line)]] | wt | 117 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.378× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 133 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.479× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 127 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.57× (z +9.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 104 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +13.5) | — |
| [[NCI-H1573 (line)]] | alt | 54.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +17.7) | — |
| [[SW1417 (line)]] | alt | 91.9 | 2 (1 ⚠) | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.74× (z +10.4) | — |
| [[SW48 (line)]] | wt | 75.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +12.6) | — |
| [[A-427 (line)]] | wt | 84.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.27× (z +11.2) | — |
| [[A549 (line)]] | wt | 102 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.9) | — |
| [[CHP-212 (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 99.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +11.8) | — |
| [[HT-29 (line)]] | alt | 81.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +15.7) | — |
| [[KATO III (line)]] | alt | 92.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.522× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 71.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +14.5) | — |
| [[Panc 03.27 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.59× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 93.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 96.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.2) | — |
| [[A-172 (line)]] | wt | 178 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 105 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 117 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 76.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 128 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 73.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 131 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 90.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 94.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 91.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 89.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 175 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 639), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF146]] | +0.74 | +0.73 / +0.53 | both halves | 1e-05 | same gene group |
| [[DDX6]] | +0.73 | +0.62 / +0.53 | both halves | 1e-05 | STRING 404 |
| [[PBLD]] | +0.73 | +0.77 / +0.35 | both halves | 1e-04 |  |
| [[LATS1]] | +0.73 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[KRBOX5]] | +0.71 | +0.78 / +0.35 | both halves | 1e-04 |  |
| [[TRAPPC6B]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[ERCC6L2-AS1]] | +0.71 | +0.78 / +0.23 | both halves | 5e-04 |  |
| [[WAC-AS1]] | +0.70 | +0.69 / +0.38 | both halves | 7e-05 |  |
| [[METTL6]] | +0.70 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[PPP3CB-AS1]] | +0.70 | +0.60 / +0.39 | both halves | 5e-05 |  |
| [[CCAR1]] | +0.69 | +0.68 / +0.48 | both halves | 2e-05 | same gene group |
| [[FBXW4]] | +0.68 | +0.56 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC4]] | -0.72 | -0.70 / -0.44 | both halves | 3e-05 |  |
| [[LPCAT4]] | -0.67 | -0.68 / -0.42 | both halves | 4e-05 |  |
| [[SMG1P2]] | -0.67 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[PACC1]] | -0.65 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[WASF3]] | -0.64 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[MAST3]] | -0.63 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[HK1]] | -0.63 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[CAMK2G]] | -0.63 | -0.60 / -0.31 | both halves | 2e-04 |  |
| [[ANKRD27]] | -0.62 | -0.61 / -0.27 | both halves | 3e-04 | same gene group |
| [[LPCAT1]] | -0.62 | -0.60 / -0.40 | both halves | 4e-05 |  |
| [[TSEN54]] | -0.62 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[GARNL3]] | -0.62 | -0.56 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OGFRL1]] | B | OGFRL1 activity raises RC3H2's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 1.17× lower at baseline in the lines without OGFRL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1 |
| [[HDAC6]] | B | HDAC6 activity raises RC3H2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises RC3H2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MR1]] | B | MR1 activity raises RC3H2's level | lines that do not express MR1 (5) vs lines expressing it (45) | 1.29× lower at baseline in the lines without MR1 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: GGT7, AGK, TCTN1 |
| [[PLXND1]] | B | PLXND1 activity raises RC3H2's level | lines that do not express PLXND1 (7) vs lines expressing it (43) | 1.27× lower at baseline in the lines without PLXND1 | 0.093 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (1.0, 10.4); signed map (21.0, -19.0). **Vector** length 123, 34.1% of its response variance represented; |z| ≥ 3 in 1,009 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.8 | +10.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.9 | +11.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.1 | +17.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.4 | +5.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +6.3 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.5 | +3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.7 | +3.2 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | -7.8 | -6.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -7.3 | -6.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -7.2 | -6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -6.9 | -7.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -6.9 | -6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.4 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.0 | -7.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.0 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ring finger and CCCH-type domains 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:122,844,556-122,905,359 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20301, FLJ20713, RNF164; previously MNAB |
| Gene groups (HGNC) | Ring finger proteins; Zinc fingers CCCH-type; Small nucleolar RNA protein coding host genes; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBD1](https://www.uniprot.org/uniprotkb/Q9HBD1) (Roquin-2):

> Post-transcriptional repressor of mRNAs containing a conserved stem loop motif, called constitutive decay element (CDE), which is often located in the 3'-UTR, as in HMGXB3, ICOS, IER3, NFKBID, NFKBIZ, PPP1R10, TNF and in many more mRNAs. Binds to CDE and promotes mRNA deadenylation and degradation. This process does not involve miRNAs. In follicular helper T (Tfh) cells, represses of ICOS and TNFRSF4 expression, thus preventing spontaneous Tfh cell differentiation, germinal center B-cell …

**Summary**, from NCBI Gene [54542](https://www.ncbi.nlm.nih.gov/gene/54542):

> Enables DNA binding activity; RNA binding activity; and ubiquitin protein ligase activity. Involved in protein polyubiquitination. Located in cell surface and membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21461](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21461) · Entrez [54542](https://www.ncbi.nlm.nih.gov/gene/54542) · UniProt [Q9HBD1](https://www.uniprot.org/uniprotkb/Q9HBD1) · Ensembl [ENSG00000056586](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000056586)

## Data

Gene col 639: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 639); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 639, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 639]; `tensor/DDL_lfc|DDL_z.npy` [639]; `embed/gene_vectors.npy` [639]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 639 or target_col == 639). Every well: [[RC3H2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RC3H2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
