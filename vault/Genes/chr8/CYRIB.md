---
symbol: "CYRIB"
type: "gene"
col: 7714
ensembl_id: "ENSG00000153310"
name: "CYFIP related Rac1 interactor B"
location: "8q24.21"
module: 23
arm: "-"
pooled_cpm: 210.43
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# CYRIB

*CYFIP related Rac1 interactor B* — 8q24.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.44× (z +8.4, q 2e-14, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.720× (z -10.8, q 3e-24, down in 38 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (NCI-H2347 0.454×, PANC-1 0.482×, A549 0.515×, HEC-1-A 0.564×, …); [[Dinaciclib (drug)]] 5 µM in 3 lines (BT-474 0.287×, NCI-H1573 0.402×, NCI-H2347 0.406×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.351×, RKO 0.397×; ⚠ cell-cycle shift, explains ~25% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMTK2]] (+0.66, fdr 2e-05), [[CARMIL1]] (+0.64, fdr 7e-06), [[BCR]] (+0.64, fdr 2e-05); moves opposite to [[THAP2]] (-0.61, fdr 4e-05), [[ZNF764]] (-0.57, fdr 1e-04), [[CFAP53]] (-0.57, fdr 5e-05).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[P2RY2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7714.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +8.4 | 2e-14 | 35/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +7.4 | 3e-11 | 29/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +7.2 | 1e-10 | 36/48 (HT-29, A498, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.35×** | +6.8 | 1e-09 | 33/48 (HT-29, HS-578T, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.86×** | +6.5 | 1e-08 | 39/49 (SW480, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +6.3 | 3e-08 | 27/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +6.1 | 1e-07 | 28/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.28×** | +5.7 | 8e-07 | 30/48 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +5.3 | 9e-06 | 30/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.26×** | +5.2 | 9e-06 | 29/48 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +5.1 | 2e-05 | 27/47 (LoVo, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.23×** | +4.8 | 6e-05 | 27/48 (NCI-H23, J82, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.55×** | +4.6 | 2e-04 | 28/48 (C32, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.19× | +3.8 | 0.005 | 20/48 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.023 | 18/47 (SW48, C32, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.11× | +3.4 | 0.028 | 4/48 (A498, SW48, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.051 | 19/48 (A498, RPMI-7951, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7714.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (NCI-H2347 0.454×, PANC-1 0.482×, A549 0.515×, HEC-1-A 0.564×, …); [[Dinaciclib (drug)]] 5 µM in 3 lines (BT-474 0.287×, NCI-H1573 0.402×, NCI-H2347 0.406×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.351×, RKO 0.397×; ⚠ cell-cycle shift, explains ~25% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.720×** | -10.8 | 3e-24 | 38/49 (NCI-H2347, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.670×** | -8.9 | 1e-16 | 27/44 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.732×** | -7.2 | 9e-11 | 28/49 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~20% of this change | **0.782×** | -5.7 | 2e-06 | 32/48 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.796×** | -5.3 | 1e-05 | 28/48 (A-427, RKO, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.784×** | -5.2 | 2e-05 | 25/45 (HepG2/C3A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.861× | -3.3 | 0.068 | 17/50 (NCI-H2347, BT-474, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.761×** | -3.2 | 0.085 | 19/48 (Hs 766T, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.879× | -3.0 | 0.17 | 16/49 (KATO III, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7714. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 210 | 3 (1 ⚠) | 4 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 1.97× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.80× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -14.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 234 | 5 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -17.8) |
| [[SW480 (line)]] | alt | 165 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.16× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +14.3) | — |
| [[HEC-1-A (line)]] | alt | 215 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -13.6) |
| [[SW1417 (line)]] | alt | 285 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -12.5) |
| [[HT-29 (line)]] | alt | 456 | 2 (2 ⚠) | 2 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.15× (z +10.0) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -12.2) |
| [[NCI-H2030 (line)]] | alt | 377 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 376 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -18.0) |
| [[Panc 03.27 (line)]] | alt | 266 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.455× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -10.5) |
| [[A-427 (line)]] | wt | 165 | 2 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.97× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.351× (z -14.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[AsPC-1 (line)]] | alt | 335 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -13.2) |
| [[BT-474 (line)]] | alt | 227 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -12.4) |
| [[C32 (line)]] | wt | 181 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.59× (z +10.1) | — |
| [[KATO III (line)]] | alt | 206 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -9.9) |
| [[LoVo (line)]] | wt | 237 | 1 (1 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.81× (z +8.6) ⚠ toxic | [[Homoharringtonine (drug)]] 0.5 µM 0.469× (z -11.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 294 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.436× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 164 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -14.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 271 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -9.9) |
| [[LS 180 (line)]] | wt | 210 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.637× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 342 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.397× (z -14.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[RPMI-7951 (line)]] | alt | 98.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +14.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 155 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.36× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.570× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 170 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.51× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -11.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 240 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.88× (z +8.8) ⚠ unreliable plate only | — |
| [[A549 (line)]] | wt | 231 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -14.9) |
| [[CFPAC-1 (line)]] | alt | 208 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -10.0) |
| [[COLO 205 (line)]] | alt | 213 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.577× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 181 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[J82 (line)]] | alt | 173 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 135 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.31× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 98.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.55× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.420× (z -10.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 164 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 139 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 263 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 79.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 197 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7714), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMTK2]] | +0.66 | +0.71 / +0.49 | both halves | 2e-05 |  |
| [[CARMIL1]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[BCR]] | +0.64 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[METAP1]] | +0.62 | +0.64 / +0.50 | both halves | 1e-05 | same gene group |
| [[XPR1]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[TRAK1]] | +0.61 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[MCU]] | +0.60 | +0.60 / +0.47 | both halves | 2e-05 | same gene group |
| [[CCNY]] | +0.59 | +0.66 / +0.36 | both halves | 1e-04 |  |
| [[SOAT1]] | +0.59 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[USB1]] | +0.58 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[LRRC20]] | +0.58 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[TSPAN14]] | +0.57 | +0.63 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP2]] | -0.61 | -0.66 / -0.40 | both halves | 4e-05 |  |
| [[ZNF764]] | -0.57 | -0.65 / -0.35 | both halves | 1e-04 |  |
| [[CFAP53]] | -0.57 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[TRIP11]] | -0.56 | -0.70 / -0.36 | both halves | 1e-04 |  |
| [[ZDBF2]] | -0.56 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[LINC00310]] | -0.56 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[CEP57]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ZBTB1]] | -0.55 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[KDM6B]] | -0.54 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[ZC3H6]] | -0.54 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[ERF]] | -0.54 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[ZNF563]] | -0.54 | -0.60 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P2RY2]] | B | P2RY2 activity raises CYRIB's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 1.62× lower at baseline in the lines without P2RY2 | 0.006 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[SOCS2-AS1]] | B | SOCS2-AS1 activity lowers CYRIB's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 1.45× higher at baseline in the lines without SOCS2-AS1 | 0.076 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.535). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-3.9, 35.3); signed map (-18.0, 37.6). **Vector** length 109, 33.8% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.9 | +5.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.9 | +4.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +4.6 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.3 | +0.5 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +0.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | -0.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.4 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.0 | -2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.7 | -5.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.0 | -3.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | +0.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.6 | -1.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | CYFIP related Rac1 interactor B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.21 — chr8:129,839,593-130,017,504 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BM-009, CYRI-B, CYRI; previously FAM49B |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUQ9](https://www.uniprot.org/uniprotkb/Q9NUQ9) (CYFIP-related Rac1 interactor B):

> Negatively regulates RAC1 signaling and RAC1-driven cytoskeletal remodeling. Regulates chemotaxis, cell migration and epithelial polarization by controlling the polarity, plasticity, duration and extent of protrusions. Limits Rac1 mediated activation of the Scar/WAVE complex, focuses protrusion signals and regulates pseudopod complexity by inhibiting Scar/WAVE-induced actin polymerization. Protects against Salmonella bacterial infection. Attenuates processes such as macropinocytosis, …

**Summary**, from NCBI Gene [51571](https://www.ncbi.nlm.nih.gov/gene/51571):

> Enables small GTPase binding activity. Involved in several processes, including negative regulation of actin filament polymerization; negative regulation of small GTPase mediated signal transduction; and regulation of mitochondrial fission. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25216](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25216) · Entrez [51571](https://www.ncbi.nlm.nih.gov/gene/51571) · UniProt [Q9NUQ9](https://www.uniprot.org/uniprotkb/Q9NUQ9) · Ensembl [ENSG00000153310](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153310)

## Data

Gene col 7714: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7714); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7714, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7714]; `tensor/DDL_lfc|DDL_z.npy` [7714]; `embed/gene_vectors.npy` [7714]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7714 or target_col == 7714). Every well: [[CYRIB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYRIB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
