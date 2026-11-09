---
symbol: "GPRC5D-AS1"
type: "gene"
col: 14496
ensembl_id: "ENSG00000247498"
name: "GPRC5D and HEBP1 antisense RNA 1"
location: "12p13.1"
module: 39
arm: "+"
pooled_cpm: 81.55
n_lines_expressing: 45
n_dd_up: 10
n_dd_down: 27
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 14
direction_downstream: 15
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# GPRC5D-AS1

*GPRC5D and HEBP1 antisense RNA 1* — 12p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 0.05 µM: 1.46× (z +5.2, q 1e-04, up in 23 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (15 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.513× (z -9.3, q 7e-18, down in 32 of 43 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.613× (z -7.1, q 2e-10, down in 30 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMO7DN]] (+0.68, fdr 1e-05), [[LSMEM2]] (+0.66, fdr 1e-05), [[SLC22A13]] (+0.66, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[LAMA3]] → it (grade B ⚠); 15 go from it, the strongest it → [[GPRC5A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14496.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | **1.46×** | +5.2 | 1e-04 | 23/43 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.35×** | +4.4 | 0.003 | 23/42 (H4, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.36×** | +4.3 | 0.003 | 23/42 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +4.3 | 0.003 | 19/43 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.92×** | +4.2 | 0.004 | 21/44 (PANC-1, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.007 | 21/43 (A-172, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.007 | 20/44 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.010 | 19/43 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.010 | 20/43 (LoVo, COLO 205, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.25×** | +3.2 | 0.075 | 14/44 (PANC-1, CHP-212, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.24× | +3.1 | 0.10 | 16/43 (A-172, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14496.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.513×** | -9.3 | 7e-18 | 32/43 (KATO III, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.560×** | -8.1 | 2e-13 | 28/42 (Hs 766T, KATO III, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.608×** | -7.2 | 1e-10 | 29/42 (BT-474, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.613×** | -7.1 | 2e-10 | 30/42 (HEC-1-A, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.606×** | -7.0 | 3e-10 | 25/37 (BT-474, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.650×** | -6.3 | 4e-08 | 29/42 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.664×** | -5.9 | 2e-07 | 25/43 (KATO III, A498, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.749×** | -5.9 | 2e-07 | 30/43 (BT-474, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.671×** | -5.8 | 5e-07 | 26/43 (BT-474, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.673×** | -5.8 | 5e-07 | 24/43 (BT-474, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.675×** | -5.7 | 6e-07 | 25/43 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.760×** | -5.6 | 9e-07 | 21/43 (KATO III, BT-474, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.795×** | -4.7 | 1e-04 | 22/44 (BT-474, KATO III, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **0.734×** | -4.5 | 3e-04 | 23/42 (KATO III, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **0.497×** | -4.5 | 3e-04 | 19/42 (KATO III, A498, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.853× | -3.3 | 0.035 | 18/43 (BT-474, A-172, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.603×** | -3.2 | 0.035 | 19/43 (KATO III, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 5 µM |  | **0.793×** | -3.2 | 0.035 | 20/42 (BT-474, NCI-H2030, …) | top dose only |  |
| [[Brivudine (drug)]] 0.5 µM |  | **0.720×** | -3.1 | 0.046 | 8/45 (KATO III, Hs 766T, …) | two highest doses | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **0.826×** | -3.1 | 0.046 | 13/44 (BT-474, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.05 µM |  | **0.803×** | -3.0 | 0.057 | 13/43 (Panc 03.27, SW 900, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.639×** | -2.9 | 0.087 | 14/43 (KATO III, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.644×** | -2.8 | 0.097 | 12/43 (KATO III, A498, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14496. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 214 | 0 | 27 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -17.7) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -12.6) |
| [[KATO III (line)]] | alt | 470 | 0 | 18 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0980× (z -21.4) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -11.8) |
| [[Hs 766T (line)]] | wt | 146 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -13.4) ⚠ cell-cycle shift, explains ~86% of this change |
| [[AsPC-1 (line)]] | alt | 109 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -11.2) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.143× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 152 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.205× (z -12.3) |
| [[NCI-H1573 (line)]] | alt | 344 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0692× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[A549 (line)]] | wt | 86.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -13.0) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.173× (z -11.5) |
| [[SW480 (line)]] | alt | 27.3 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.135× (z -11.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.267× (z -9.3) |
| [[A498 (line)]] | wt | 53.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +11.3) ⚠ cell-cycle shift, explains ~86% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.243× (z -10.4) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 67.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -10.9) ⚠ cell-cycle shift, explains ~86% of this change |
| [[H4 (line)]] | wt | 31.8 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0794× (z -9.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LS 180 (line)]] | wt | 105 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 51.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.08× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 77.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 51.4 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.347× (z -9.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.369× (z -8.9) |
| [[SW48 (line)]] | wt | 215 | 0 | 2 | — | [[Ponatinib (drug)]] 5 µM 0.153× (z -10.1) |
| [[A-172 (line)]] | wt | 32.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.40× (z +9.8) | — |
| [[A-427 (line)]] | wt | 46.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.339× (z -9.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HCT15 (line)]] | alt | 53.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HS-578T (line)]] | alt | 54.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 32.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.1000× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[NCI-H1792 (line)]] | alt | 186 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +9.2) ⚠ cell-cycle shift, explains ~86% of this change | — |
| [[NCI-H596 (line)]] | alt | 69.4 | 1 (1 ⚠) | 0 | [[Pentoxifylline (drug)]] 0.05 µM 3.15× (z +8.8) ⚠ transcription drop | — |
| [[PANC-1 (line)]] | alt | 44.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.329× (z -10.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW 1271 (line)]] | alt | 79.6 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0795× (z -9.3) |
| [[AN3 CA (line)]] | alt | 19.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 176 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.98 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.07 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.2 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14496), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMO7DN]] | +0.68 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[LSMEM2]] | +0.66 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[SLC22A13]] | +0.66 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.64 | +0.58 / +0.64 | both halves | 8e-06 | same gene group |
| [[SLC22A14]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[GRAMD2A]] | +0.61 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[GPRC5A]] | +0.61 | +0.53 / +0.65 | both halves | 1e-05 | ⚠ same locus (9.8 kb, same strand: neighbours can correlate without regulation) |
| [[LINC01619]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[OIT3]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[SEMA4A]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ADAM32]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RBM44]] | +0.58 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[UCKL1-AS1]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMA3]] | B | LAMA3 activity raises GPRC5D-AS1's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.70× lower at baseline in the lines without LAMA3 | 0.004 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[GPRC5A]] | B | GPRC5A activity raises GPRC5D-AS1's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 3.00× lower at baseline in the lines without GPRC5A | 0.004 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[C1orf116]] | B | C1orf116 activity raises GPRC5D-AS1's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 2.75× lower at baseline in the lines without C1orf116 | 0.013 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises GPRC5D-AS1's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 2.81× lower at baseline in the lines without TMPRSS4 | 0.018 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[CATSPERB]] | B | CATSPERB activity raises GPRC5D-AS1's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 2.65× lower at baseline in the lines without CATSPERB | 0.021 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[MROH3P]] | B | MROH3P activity raises GPRC5D-AS1's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 2.02× lower at baseline in the lines without MROH3P | 0.035 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[FGFBP1]] | B | FGFBP1 activity raises GPRC5D-AS1's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 2.82× lower at baseline in the lines without FGFBP1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5 |
| [[TFF1]] | B | TFF1 activity raises GPRC5D-AS1's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 2.45× lower at baseline in the lines without TFF1 | 0.050 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[LINC02582]] | B | LINC02582 activity raises GPRC5D-AS1's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 3.02× lower at baseline in the lines without LINC02582 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975 |
| [[KIAA0040]] | B | KIAA0040 activity raises GPRC5D-AS1's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 2.00× lower at baseline in the lines without KIAA0040 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1 |
| [[CEACAM6]] | B | CEACAM6 activity raises GPRC5D-AS1's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 2.71× lower at baseline in the lines without CEACAM6 | 0.075 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[KRT16]] | B | KRT16 activity raises GPRC5D-AS1's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 2.00× lower at baseline in the lines without KRT16 | 0.087 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRC5A]] | B | GPRC5D-AS1 activity raises GPRC5A's level | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (45) | 6.47× lower at baseline in the lines without GPRC5D-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |
| [[LAMA3]] | B | GPRC5D-AS1 activity raises LAMA3's level | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (45) | 4.35× lower at baseline in the lines without GPRC5D-AS1 | 0.040 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |
| [[SH2D4B]] | B | GPRC5D-AS1 activity raises SH2D4B's level | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without GPRC5D-AS1 | 0.040 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |
| cells under [[MK-3903 (drug)]] 0.05 µM | B | GPRC5D-AS1 activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (43) | the lines without GPRC5D-AS1: 0.73× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |
| [[OXSR1]] | B | GPRC5D-AS1 activity raises OXSR1's level | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (45) | 1.48× lower at baseline in the lines without GPRC5D-AS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |
| [[SLC22A13]] | B | GPRC5D-AS1 activity raises SLC22A13's level | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (45) | 1.62× lower at baseline in the lines without GPRC5D-AS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |
| [[SLC22A14]] | B | GPRC5D-AS1 activity raises SLC22A14's level | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (45) | 1.74× lower at baseline in the lines without GPRC5D-AS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |
| [[IL20RB]] | B | GPRC5D-AS1 activity raises IL20RB's level | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (45) | 1.46× lower at baseline in the lines without GPRC5D-AS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |
| [[STPG4]] | B | GPRC5D-AS1 activity raises STPG4's level | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (45) | 1.85× lower at baseline in the lines without GPRC5D-AS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | B | GPRC5D-AS1 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (43) | the lines without GPRC5D-AS1: 0.75× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |
| cells under [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM | B | GPRC5D-AS1 activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 5 µM (protects the cells) | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (43) | the lines without GPRC5D-AS1: 0.80× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |
| [[MET]] | B | GPRC5D-AS1 activity raises MET's level | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (45) | 2.93× lower at baseline in the lines without GPRC5D-AS1 | 0.088 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.515). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.5, -18.0); signed map (14.2, 13.8). **Vector** length 118, 33.4% of its response variance represented; |z| ≥ 3 in 1,222 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.4 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +5.0 | -3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.3 | +2.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +4.3 | +0.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.0 | +5.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.8 | +3.8 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -5.3 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.0 | -5.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -5.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.5 | -4.0 |
|  | [[Afatinib (drug)]] 5 µM |  | -3.4 | -3.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.2 | -1.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | GPRC5D and HEBP1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12p13.1 — chr12:12,927,712-12,984,645 (+) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-392P7.6 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53599](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53599) · Entrez [100506314](https://www.ncbi.nlm.nih.gov/gene/100506314) · Ensembl [ENSG00000247498](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247498)

## Data

Gene col 14496: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14496); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14496, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14496]; `tensor/DDL_lfc|DDL_z.npy` [14496]; `embed/gene_vectors.npy` [14496]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14496 or target_col == 14496). Every well: [[GPRC5D-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPRC5D-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
