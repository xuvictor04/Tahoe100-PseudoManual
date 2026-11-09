---
symbol: "GGT7"
type: "gene"
col: 5165
ensembl_id: "ENSG00000131067"
name: "gamma-glutamyltransferase 7"
location: "20q11.22"
module: 20
arm: "-"
pooled_cpm: 34.35
n_lines_expressing: 45
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# GGT7

*gamma-glutamyltransferase 7* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.33× (z +7.2, q 3e-10, up in 27 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.624× (z -12.1, q 7e-31, down in 32 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYP]] (+0.69, fdr 1e-05), [[SIRT6]] (+0.66, fdr 9e-06), [[DDX19B]] (+0.66, fdr 7e-06); moves opposite to [[MOB1A]] (-0.59, fdr 2e-05), [[CNOT1]] (-0.59, fdr 2e-05), [[ATL3]] (-0.57, fdr 3e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[DCTN6-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5165.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +7.2 | 3e-10 | 27/43 (BT-474, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +6.0 | 6e-07 | 26/43 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.21×** | +4.9 | 2e-04 | 19/43 (LoVo, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.30×** | +4.7 | 3e-04 | 22/43 (HepG2/C3A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.41×** | +4.4 | 0.001 | 20/43 (HEC-1-A, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.003 | 19/43 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.17× | +4.1 | 0.003 | 21/43 (A-172, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.029 | 13/43 (C32, HEC-1-A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.031 | 15/43 (HepG2/C3A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.043 | 12/43 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.20×** | +3.3 | 0.047 | 19/43 (PANC-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.057 | 10/43 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.1 | 0.079 | 16/43 (HepG2/C3A, SW480, …) | all doses, flat |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.097 | 7/43 (COLO 205, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.18× | +3.0 | 0.097 | 8/43 (SNU-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.097 | 7/43 (NCI-H460, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.097 | 11/43 (CHP-212, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +2.9 | 0.098 | 8/43 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5165.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.624×** | -12.1 | 7e-31 | 32/43 (SK-MEL-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.511×** | -11.7 | 5e-29 | 37/43 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.564×** | -10.4 | 6e-23 | 29/43 (SK-MEL-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.558×** | -10.2 | 4e-22 | 34/43 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.599×** | -8.9 | 5e-17 | 32/42 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.647×** | -7.6 | 3e-12 | 27/38 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.760×** | -5.0 | 5e-05 | 18/43 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.802×** | -4.0 | 0.005 | 20/43 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~8% of this change | **0.815×** | -3.7 | 0.013 | 18/43 (SW 1271, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.812×** | -3.5 | 0.027 | 19/39 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.701×** | -3.4 | 0.040 | 15/43 (BT-474, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.839× | -3.2 | 0.070 | 10/43 (PANC-1, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5165. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 44.8 | 3 (3 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.11× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.231× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 63.7 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.186× (z -15.3) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 25.7 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 59.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0858× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -16.7) |
| [[NCI-H1792 (line)]] | alt | 72.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -16.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -13.3) |
| [[PANC-1 (line)]] | alt | 28.1 | 0 | 3 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.370× (z -10.1) ⚠ transcription drop; cell-cycle shift, explains ~8% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -9.0) |
| [[A-172 (line)]] | wt | 14.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.226× (z -8.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 50.6 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.78× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 59.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -12.2) |
| [[COLO 205 (line)]] | alt | 30.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 33.6 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -9.9) |
| [[LoVo (line)]] | wt | 40.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 34.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 33.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -8.6) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 46.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -9.1) |
| [[SNU-1 (line)]] | wt | 72.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -17.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 56.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -10.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 23.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -9.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 26.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -10.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 27.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -11.4) |
| [[J82 (line)]] | alt | 26.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1573 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 74.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.457× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 73.6 | 0 | 1 | — | [[Benztropine (mesylate) (drug)]] 0.05 µM 0.0622× (z -9.0) |
| [[SW 1271 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0950× (z -12.6) ⚠ transcription drop; cell-cycle shift, explains ~8% of this change |
| [[A498 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.61 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5165), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYP]] | +0.69 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[SIRT6]] | +0.66 | +0.57 / +0.71 | both halves | 9e-06 |  |
| [[DDX19B]] | +0.66 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[MARCHF9]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | +0.63 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[PIGH]] | +0.63 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[DOCK6]] | +0.62 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[ZNF316]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[MAP2K7]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SIGIRR]] | +0.60 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[PDP2]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[KLHL26]] | +0.60 | +0.50 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | -0.59 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[CNOT1]] | -0.59 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[ATL3]] | -0.57 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[FGD5-AS1]] | -0.57 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[ATP11C]] | -0.57 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[EIF4G2]] | -0.57 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[DPAGT1]] | -0.56 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[MFN2]] | -0.56 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[PSME3]] | -0.56 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[CA5BP1-1]] | -0.56 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[SETD7]] | -0.55 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[SUMO3]] | -0.55 | -0.51 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GGT7's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SOGA1]] | C | SOGA1 activity raises GGT7's level | lines that do not express SOGA1 (3) vs lines expressing it (47) | 8.67× lower at baseline in the lines without SOGA1 | 0.001 | ⚠ few lines (3 vs 47); across organs; also absent: RDX, ODAD4, GGT7; co-absent with the target |
| [[ARL4D]] | C | ARL4D activity raises GGT7's level | lines that do not express ARL4D (5) vs lines expressing it (45) | 5.81× lower at baseline in the lines without ARL4D | 0.025 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: GGT7, SOGA1, ELOVL5; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCTN6-DT]] | B | GGT7 activity lowers DCTN6-DT's level | lines that do not express GGT7 (5) vs lines expressing it (45) | 1.64× higher at baseline in the lines without GGT7 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: BBS5, ODAD4, ALK |
| [[AKIRIN2]] | B | GGT7 activity lowers AKIRIN2's level | lines that do not express GGT7 (5) vs lines expressing it (45) | 1.16× higher at baseline in the lines without GGT7 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: BBS5, ODAD4, ALK |
| [[ARL4D]] | C | GGT7 activity raises ARL4D's level | lines that do not express GGT7 (5) vs lines expressing it (45) | 3.50× lower at baseline in the lines without GGT7 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: BBS5, ODAD4, ALK; co-absent with the target |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.560). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-31.7, -27.0); signed map (-15.9, 0.1). **Vector** length 106, 25.0% of its response variance represented; |z| ≥ 3 in 840 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +7.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +6.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.8 | +4.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +4.3 | +4.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.1 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.0 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.1 | +2.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.9 | +3.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -11.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -12.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.6 | -8.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.2 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.2 | -1.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | gamma-glutamyltransferase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:34,844,720-34,872,856 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D20S101, dJ18C9.2; previously GGTL5, GGTL3 |
| Gene groups (HGNC) | Gamma-glutamyltransferases; Acyltransferases |
| Reactome | 7 pathways, smallest: Aflatoxin activation and detoxification; Glutathione synthesis and recycling; Paracetamol ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJ14](https://www.uniprot.org/uniprotkb/Q9UJ14) (Glutathione hydrolase 7):

> Hydrolyzes and transfers gamma-glutamyl moieties from glutathione and other gamma-glutamyl compounds to acceptors.

**Summary**, from NCBI Gene [2686](https://www.ncbi.nlm.nih.gov/gene/2686):

> This gene is a member of a gene family that encodes enzymes involved in both the metabolism of glutathione and in the transpeptidation of amino acids. Changes in the activity of gamma-glutamyltransferase may signal preneoplastic or toxic conditions in the liver or kidney. The protein encoded by this gene consists of a heavy and a light chain, and it can interact with CT120, a plasma membrane-associated protein that is possibly involved in lung carcinogenesis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4259](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4259) · Entrez [2686](https://www.ncbi.nlm.nih.gov/gene/2686) · UniProt [Q9UJ14](https://www.uniprot.org/uniprotkb/Q9UJ14) · Ensembl [ENSG00000131067](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131067)

## Data

Gene col 5165: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5165); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5165, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5165]; `tensor/DDL_lfc|DDL_z.npy` [5165]; `embed/gene_vectors.npy` [5165]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5165 or target_col == 5165). Every well: [[GGT7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GGT7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
