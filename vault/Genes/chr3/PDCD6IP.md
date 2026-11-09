---
symbol: "PDCD6IP"
type: "gene"
col: 9920
ensembl_id: "ENSG00000170248"
name: "programmed cell death 6 interacting protein"
location: "3p22.3"
module: 5
arm: "-"
pooled_cpm: 167.78
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PDCD6IP

*programmed cell death 6 interacting protein* — 3p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +7.6, q 2e-11, up in 31 of 50 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.712× (z -10.0, q 7e-21, down in 44 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SNU-1 0.349×, HEC-1-A 0.538×, RPMI-7951 0.459×, Panc 03.27 0.533×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change); [[Belinostat (drug)]] 0.5 µM in 4 lines (AsPC-1 0.541×, A-172 0.584×, RPMI-7951 0.522×, PANC-1 0.659×); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 0.460×, A-427 0.461×, HCT15 0.433×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SW 1088 0.158×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCTA]] (+0.64, fdr 1e-05), [[CCDC90B]] (+0.58, fdr 1e-05), [[EXOC1]] (+0.56, fdr 2e-05); moves opposite to [[RRP7BP]] (-0.53, fdr 4e-05), [[CHERP]] (-0.52, fdr 3e-05), [[UNC13A]] (-0.47, fdr 9e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9920.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +7.6 | 2e-11 | 31/50 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +7.4 | 4e-11 | 33/48 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +6.2 | 9e-08 | 24/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.48×** | +6.0 | 2e-07 | 29/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.44×** | +5.6 | 2e-06 | 35/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +4.8 | 1e-04 | 14/49 (COLO 205, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.17× | +4.8 | 1e-04 | 23/48 (PANC-1, NCI-H2030, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.12× | +4.8 | 1e-04 | 8/48 (SW1417, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +4.3 | 0.001 | 12/48 (SW1417, A-427, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +4.0 | 0.004 | 4/48 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | 1.14× | +3.9 | 0.005 | 5/48 (C-33 A, A-427, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.15× | +3.9 | 0.005 | 16/47 (NCI-H460, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.10× | +3.9 | 0.005 | 19/48 (A-427, PANC-1, …) | all doses, flat | composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.007 | 23/50 (NCI-H460, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.13× | +3.7 | 0.007 | 13/48 (COLO 205, LS 180, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.14× | +3.7 | 0.008 | 8/48 (SNU-423, HOP62, …) | rises with dose | plate-row cell shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.12× | +3.2 | 0.040 | 10/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.11× | +3.2 | 0.040 | 12/48 (COLO 205, LS 180, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.12× | +3.2 | 0.040 | 2/49 (HEC-1-A, SNU-423) | top dose only | plate-row cell shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.11× | +3.2 | 0.040 | 13/48 (A-427, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9920.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SNU-1 0.349×, HEC-1-A 0.538×, RPMI-7951 0.459×, Panc 03.27 0.533×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change); [[Belinostat (drug)]] 0.5 µM in 4 lines (AsPC-1 0.541×, A-172 0.584×, RPMI-7951 0.522×, PANC-1 0.659×); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 0.460×, A-427 0.461×, HCT15 0.433×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SW 1088 0.158×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.712×** | -10.0 | 7e-21 | 44/48 (AsPC-1, A-172, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.759×** | -8.1 | 1e-13 | 30/48 (AsPC-1, SNU-1, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.744×** | -8.1 | 1e-13 | 25/45 (SK-MEL-2, RKO, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.783×** | -7.1 | 2e-10 | 29/48 (A-172, J82, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.798×** | -6.7 | 3e-09 | 27/48 (A-172, HOP62, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | 0.837× | -5.0 | 6e-05 | 23/47 (NCI-H2030, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | 0.855× | -4.6 | 3e-04 | 22/48 (A-172, HOP62, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | 0.856× | -4.6 | 3e-04 | 22/49 (SK-MEL-2, A-427, …) | all doses, flat | composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.866× | -4.2 | 0.001 | 17/48 (SW 1088, SHP-77, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | 0.877× | -3.7 | 0.014 | 18/44 (SNU-1, HEC-1-A, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~16% of this change | 0.884× | -3.6 | 0.015 | 13/48 (H4, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 0.887× | -3.5 | 0.021 | 15/48 (HOP62, H4, …) | top dose only |  |
| [[OTS514 (drug)]] 5 µM |  | **0.801×** | -3.4 | 0.027 | 16/46 (H4, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9920. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 145 | 6 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 1.93× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[A-172 (line)]] | wt | 229 | 0 | 4 (3 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.584× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 91.2 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +12.4) | — |
| [[NCI-H2030 (line)]] | alt | 126 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.531× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[PANC-1 (line)]] | alt | 123 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.67× (z +10.6) | [[Belinostat (drug)]] 0.5 µM 0.659× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 240 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[AsPC-1 (line)]] | alt | 187 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Belinostat (drug)]] 5 µM 0.527× (z -10.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.541× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 153 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +10.8) | — |
| [[RKO (line)]] | wt | 182 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.458× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SNU-1 (line)]] | wt | 248 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[COLO 205 (line)]] | alt | 119 | 2 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.89× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 181 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.533× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[RPMI-7951 (line)]] | alt | 206 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.459× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.522× (z -8.9) |
| [[SW480 (line)]] | alt | 212 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.61× (z +11.0) | — |
| [[A549 (line)]] | wt | 252 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -15.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 191 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[HEC-1-A (line)]] | alt | 230 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.538× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[KATO III (line)]] | alt | 190 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.74× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 178 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.608× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 177 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 243 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.645× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[SW 1088 (line)]] | alt | 168 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.158× (z -8.5) |
| [[A498 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 147 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 131 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 159 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 149 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 199 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 171 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 158 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 161 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 176 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 319 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 188 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9920), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCTA]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[CCDC90B]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[EXOC1]] | +0.56 | +0.62 / +0.48 | both halves | 2e-05 | pathway: Dengue Virus-Host Interactions |
| [[TRAPPC6B]] | +0.55 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ANXA4]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[FKBP3]] | +0.53 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[WASHC3]] | +0.53 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[DERA]] | +0.53 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[DNAJC13]] | +0.53 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[SH3BGR]] | +0.52 | +0.53 / +0.38 | both halves | 7e-05 |  |
| [[RMDN1]] | +0.52 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[VPS37A]] | +0.52 | +0.57 / +0.45 | both halves | 3e-05 | pathway: Budding and maturation of HIV virion; STRING 696 |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP7BP]] | -0.53 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[CHERP]] | -0.52 | -0.44 / -0.56 | both halves | 3e-05 | pathway: Dengue Virus-Host Interactions |
| [[UNC13A]] | -0.47 | -0.37 / -0.46 | both halves | 9e-05 |  |
| [[SNRPA]] | -0.47 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[TMEM201]] | -0.47 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[ARMC9]] | -0.46 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[CCDC138]] | -0.46 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[NOP2]] | -0.45 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[MAP3K5]] | -0.45 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[GNB1L]] | -0.45 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[SLC27A5]] | -0.44 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[ZNF787]] | -0.44 | -0.40 / -0.41 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PDCD6IP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[UNC13A]] | B | UNC13A activity raises PDCD6IP's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 1.19× lower at baseline in the lines without UNC13A | 0.075 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.255). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-20.5, 20.4); signed map (19.3, -17.2). **Vector** length 121, 36.1% of its response variance represented; |z| ≥ 3 in 1,174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +10.2 | +7.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.1 | +7.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +7.6 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.6 | +4.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.3 | +3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.9 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.9 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.9 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +3.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -7.3 | -10.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | -4.1 | -7.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +0.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.8 | -0.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.7 | -1.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.3 | -2.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | programmed cell death 6 interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.3 — chr3:33,798,571-33,869,707 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Alix, AIP1, Hp95 |
| Reactome | 14 pathways, smallest: Uptake and function of anthrax toxins; Uptake and actions of bacterial toxins; Budding and maturation of HIV virion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUM4](https://www.uniprot.org/uniprotkb/Q8WUM4) (Programmed cell death 6-interacting protein):

> Multifunctional protein involved in endocytosis, multivesicular body biogenesis, membrane repair, cytokinesis, apoptosis and maintenance of tight junction integrity. Class E VPS protein involved in concentration and sorting of cargo proteins of the multivesicular body (MVB) for incorporation into intralumenal vesicles (ILVs) that are generated by invagination and scission from the limiting membrane of the endosome. Binds to the phospholipid lysobisphosphatidic acid (LBPA) which is abundant in …

**Summary**, from NCBI Gene [10015](https://www.ncbi.nlm.nih.gov/gene/10015):

> This gene encodes a protein that functions within the ESCRT pathway in the abscission stage of cytokinesis, in intralumenal endosomal vesicle formation, and in enveloped virus budding. Studies using mouse cells have shown that overexpression of this protein can block apoptosis. In addition, the product of this gene binds to the product of the PDCD6 gene, a protein required for apoptosis, in a calcium-dependent manner. This gene product also binds to endophilins, proteins that regulate membrane …

**Accessions** — [HGNC:8766](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8766) · Entrez [10015](https://www.ncbi.nlm.nih.gov/gene/10015) · UniProt [Q8WUM4](https://www.uniprot.org/uniprotkb/Q8WUM4) · Ensembl [ENSG00000170248](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170248)

## Data

Gene col 9920: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9920); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9920, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9920]; `tensor/DDL_lfc|DDL_z.npy` [9920]; `embed/gene_vectors.npy` [9920]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9920 or target_col == 9920). Every well: [[PDCD6IP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDCD6IP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
