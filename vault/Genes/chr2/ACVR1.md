---
symbol: "ACVR1"
type: "gene"
col: 3630
ensembl_id: "ENSG00000115170"
name: "activin A receptor type 1"
location: "2q24.1"
module: 81
arm: "+"
pooled_cpm: 111.78
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# ACVR1

*activin A receptor type 1* — 2q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.05 µM: 1.36× (z +4.6, q 0.003, up in 30 of 49 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.27× (z +3.6, q 0.032, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.304× (z -17.8, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.727× (z -6.7, q 2e-09, down in 29 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UPP1]] (+0.59, fdr 1e-05), [[GRB10]] (+0.55, fdr 3e-05), [[OCIAD2]] (+0.54, fdr 1e-05); moves opposite to [[CPSF7]] (-0.50, fdr 4e-05), [[SRSF10]] (-0.48, fdr 1e-04), [[ZNF608]] (-0.47, fdr 1e-04).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MMP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3630.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.36×** | +4.6 | 0.003 | 30/49 (HepG2/C3A, RPMI-7951, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +3.9 | 0.022 | 27/47 (H4, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.28×** | +3.7 | 0.032 | 27/48 (HEC-1-A, NCI-H2030, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.27×** | +3.6 | 0.032 | 26/48 (COLO 205, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.032 | 25/47 (H4, RKO, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.032 | 23/48 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.052 | 21/48 (C32, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.23× | +3.2 | 0.10 | 19/48 (AN3 CA, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.10 | 17/49 (COLO 205, MIA PaCa-2, …) | top dose only |  |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 1.24× | +3.0 | 0.14 | 17/48 (A498, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3630.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.304×** | -17.8 | 0e+00 | 47/49 (SW 900, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.321×** | -16.3 | 0e+00 | 39/44 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.587×** | -7.3 | 4e-11 | 33/45 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.727×** | -6.7 | 2e-09 | 29/49 (NCI-H2347, HT-29, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.688×** | -5.6 | 3e-06 | 37/48 (HT-29, NCI-H2347, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.692×** | -5.5 | 4e-06 | 32/48 (hTERT-HPNE, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.729×** | -4.7 | 2e-04 | 30/48 (HT-29, NCI-H2347, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.760×** | -4.1 | 0.003 | 24/48 (HT-29, RPMI-7951, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.825×** | -4.0 | 0.003 | 22/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.760×** | -3.9 | 0.005 | 26/47 (NCI-H2347, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[DT-061 (drug)]] 5 µM |  | **0.666×** | -3.2 | 0.078 | 20/47 (SK-MEL-2, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **0.812×** | -3.1 | 0.094 | 21/48 (HOP62, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3630. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 175 | 9 (8 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +13.4) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.65× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.293× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 146 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -17.8) |
| [[H4 (line)]] | wt | 158 | 3 (2 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.15× (z +8.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.88× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -18.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 163 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.388× (z -8.5) |
| [[HT-29 (line)]] | alt | 185 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -13.9) |
| [[PANC-1 (line)]] | alt | 103 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -23.2) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -11.0) |
| [[SW1417 (line)]] | alt | 127 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -17.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 98.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 188 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -14.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 195 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 164 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -12.1) |
| [[A549 (line)]] | wt | 121 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -11.8) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 89.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -15.3) ⚠ cell-cycle shift, explains ~86% of this change |
| [[NCI-H2030 (line)]] | alt | 105 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -21.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 153 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -16.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 114 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -8.8) |
| [[A498 (line)]] | wt | 147 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -12.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 244 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0957× (z -20.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 124 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -12.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 151 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -14.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 80.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 61.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -12.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 71.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -13.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 86.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -12.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -10.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 70.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -16.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 47.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -15.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 65.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0430× (z -31.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -16.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 80.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.413× (z -8.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 51.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.6) ⚠ cell-cycle shift, explains ~86% of this change | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.110× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -10.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -14.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 95.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -19.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 57.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.366× (z -10.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 152 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 77.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 79.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 110 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3630), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UPP1]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[GRB10]] | +0.55 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[OCIAD2]] | +0.54 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[CLDN12]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[KHDRBS3]] | +0.53 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[PKIA]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[USP3]] | +0.52 | +0.68 / +0.34 | both halves | 1e-04 |  |
| [[ITGA2-AS1]] | +0.51 | +0.36 / +0.61 | both halves | 9e-05 |  |
| [[SPSB1]] | +0.51 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[CIB1]] | +0.50 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[GAB2]] | +0.50 | +0.57 / +0.30 | both halves | 2e-04 |  |
| [[RASA2]] | +0.50 | +0.59 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF7]] | -0.50 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[SRSF10]] | -0.48 | -0.52 / -0.32 | both halves | 1e-04 |  |
| [[ZNF608]] | -0.47 | -0.56 / -0.36 | both halves | 1e-04 |  |
| [[HNRNPUL1]] | -0.46 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[ZFX]] | -0.46 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[SRRM2]] | -0.45 | -0.47 / -0.25 | both halves | 4e-04 |  |
| [[MLLT6]] | -0.45 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[HNRNPL]] | -0.45 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[ZC3H7A]] | -0.44 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[PPWD1]] | -0.44 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[JPH2]] | -0.43 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[TNPO2]] | -0.43 | -0.53 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP1]] | B | MMP1 activity raises ACVR1's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 1.56× lower at baseline in the lines without MMP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[FAM107B]] | B | FAM107B activity raises ACVR1's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 1.34× lower at baseline in the lines without FAM107B | 0.026 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[ANTXR2]] | B | ANTXR2 activity raises ACVR1's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 1.54× lower at baseline in the lines without ANTXR2 | 0.068 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.561). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.0, -5.8); signed map (-5.8, 50.5). **Vector** length 108, 35.1% of its response variance represented; |z| ≥ 3 in 1,217 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.7 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.0 | +2.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.0 | -0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -0.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | +0.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | -4.2 | -4.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.1 | -2.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -2.9 | -3.1 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -2.9 | -2.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.8 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | +3.4 |

## What is on record

|  |  |
|---|---|
| Name | activin A receptor type 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.1 — chr2:157,736,251-157,876,330 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SKR1, ALK2, ACVR1A; previously ACVRLK2 |
| Gene groups (HGNC) | Type 1 receptor serine/threonine kinases; BMP receptors |
| Hallmark sets | TGF_BETA_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04771](https://www.uniprot.org/uniprotkb/Q04771) (Activin receptor type-1):

> Bone morphogenetic protein (BMP) type I receptor that is involved in a wide variety of biological processes, including bone, heart, cartilage, nervous, and reproductive system development and regulation. As a type I receptor, forms heterotetrameric receptor complexes with the type II receptors AMHR2, ACVR2A or ACVR2B. Upon binding of ligands such as BMP7 or GDF2/BMP9 to the heteromeric complexes, type II receptors transphosphorylate ACVR1 intracellular domain. In turn, ACVR1 kinase domain is …

**Summary**, from NCBI Gene [90](https://www.ncbi.nlm.nih.gov/gene/90):

> Activins are dimeric growth and differentiation factors which belong to the transforming growth factor-beta (TGF-beta) superfamily of structurally related signaling proteins. Activins signal through a heteromeric complex of receptor serine kinases which include at least two type I ( I and IB) and two type II (II and IIB) receptors. These receptors are all transmembrane proteins, composed of a ligand-binding extracellular domain with cysteine-rich region, a transmembrane domain, and a …

**Accessions** — [HGNC:171](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:171) · Entrez [90](https://www.ncbi.nlm.nih.gov/gene/90) · UniProt [Q04771](https://www.uniprot.org/uniprotkb/Q04771) · Ensembl [ENSG00000115170](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115170)

## Data

Gene col 3630: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3630); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3630, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3630]; `tensor/DDL_lfc|DDL_z.npy` [3630]; `embed/gene_vectors.npy` [3630]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3630 or target_col == 3630). Every well: [[ACVR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACVR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
