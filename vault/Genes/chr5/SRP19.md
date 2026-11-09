---
symbol: "SRP19"
type: "gene"
col: 7681
ensembl_id: "ENSG00000153037"
name: "signal recognition particle 19"
location: "5q22.2"
module: 156
arm: "+"
pooled_cpm: 57.81
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 1
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# SRP19

*signal recognition particle 19* — 5q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.90× (z +16.5, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Pyridoxine (hydrochloride) (drug)]] 5 µM: 0.821× (z -4.2, q 0.014, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HepG2/C3A 0.0853×, AsPC-1 0.196×, NCI-H1573 0.335×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0725×; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW48 0.267×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Diphenhydramine (drug)]] 0.5 µM in 1 line (SW 1088 0.0552×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FICD]] (+0.68, fdr 7e-06), [[ALG2]] (+0.66, fdr 7e-06), [[SDHAF2]] (+0.62, fdr 1e-05); moves opposite to [[GUSB]] (-0.58, fdr 4e-05), [[RBBP7]] (-0.58, fdr 1e-05), [[H3-3A]] (-0.55, fdr 1e-05).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7681.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.90×** | +16.5 | 0e+00 | 45/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +14.6 | 1e-45 | 45/48 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.44×** | +13.8 | 3e-41 | 45/48 (BT-474, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.84×** | +9.5 | 3e-19 | 44/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +9.4 | 5e-19 | 42/48 (COLO 205, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.61×** | +7.4 | 2e-11 | 42/48 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.56×** | +6.9 | 5e-10 | 36/48 (HOP62, H4, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.38×** | +6.9 | 5e-10 | 34/49 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.52×** | +6.5 | 4e-09 | 37/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.54×** | +6.4 | 7e-09 | 32/48 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +6.4 | 8e-09 | 37/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +6.4 | 8e-09 | 32/47 (RKO, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.46×** | +5.9 | 2e-07 | 33/48 (A-172, SNU-423, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +5.8 | 2e-07 | 33/48 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.43×** | +5.3 | 3e-06 | 31/50 (HS-578T, Panc 03.27, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.36×** | +4.7 | 6e-05 | 32/48 (HOP62, J82, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.3 | 5e-04 | 27/48 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +3.7 | 0.004 | 19/49 (MIA PaCa-2, CFPAC-1, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.013 | 19/47 (HOP62, hTERT-HPNE, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.013 | 22/47 (NCI-H460, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.014 | 23/48 (hTERT-HPNE, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7681.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HepG2/C3A 0.0853×, AsPC-1 0.196×, NCI-H1573 0.335×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0725×; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW48 0.267×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Diphenhydramine (drug)]] 0.5 µM in 1 line (SW 1088 0.0552×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.821×** | -4.2 | 0.014 | 21/48 (HT-29, NCI-H1573, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.800× | -3.5 | 0.15 | 18/48 (NCI-H661, HT-29, …) | all doses, flat |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.811× | -3.1 | 0.37 | 19/47 (J82, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.824× | -3.0 | 0.37 | 15/48 (AsPC-1, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7681. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 120 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 9.83× (z +21.8) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 58.2 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.27× (z +10.9) | — |
| [[NCI-H460 (line)]] | wt | 63.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 40.4 | 4 | 0 | [[Auranofin (drug)]] 5 µM 3.73× (z +11.9) | — |
| [[SW480 (line)]] | alt | 55.8 | 4 | 0 | [[Auranofin (drug)]] 5 µM 3.42× (z +12.7) | — |
| [[CFPAC-1 (line)]] | alt | 39.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.3) | — |
| [[COLO 205 (line)]] | alt | 65.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +14.4) | — |
| [[HEC-1-A (line)]] | alt | 48.4 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.40× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 37.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +12.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 39.6 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +11.0) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.03× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 58.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.91× (z +12.7) | — |
| [[RKO (line)]] | wt | 69.2 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.15× (z +12.3) | — |
| [[A549 (line)]] | wt | 48.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.3) | — |
| [[HCT15 (line)]] | alt | 39.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 45.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0853× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 50.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.5) | — |
| [[KATO III (line)]] | alt | 46.4 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.31× (z +9.5) | — |
| [[LoVo (line)]] | wt | 99.0 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.57× (z +12.7) | — |
| [[LS 180 (line)]] | wt | 61.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.86× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 47.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 54.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.3) | — |
| [[SK-MEL-2 (line)]] | alt | 76.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.01× (z +10.3) | — |
| [[A-172 (line)]] | wt | 52.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.36× (z +11.0) | — |
| [[A498 (line)]] | wt | 67.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.27× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 54.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 35.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.90× (z +12.8) | — |
| [[C32 (line)]] | wt | 39.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.08× (z +9.7) | — |
| [[H4 (line)]] | wt | 52.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.33× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 38.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.92× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 53.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.26× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 56.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.58× (z +11.7) | — |
| [[SNU-423 (line)]] | alt | 34.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.30× (z +10.5) | — |
| [[SW 1088 (line)]] | alt | 59.8 | 0 | 1 | — | [[Diphenhydramine (drug)]] 0.5 µM 0.0552× (z -8.7) |
| [[SW 900 (line)]] | alt | 52.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.23× (z +12.3) | — |
| [[SW48 (line)]] | wt | 67.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 65.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 62.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7681), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FICD]] | +0.68 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[ALG2]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[SDHAF2]] | +0.62 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[TSSC4]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[GOSR2]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[MIR22HG]] | +0.60 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[BMS1P4-1]] | +0.60 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[SEC23IP]] | +0.60 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[TRIP11]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[NSRP1]] | +0.58 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[DNAJC2]] | +0.58 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[CDKL4]] | +0.57 | +0.63 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUSB]] | -0.58 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[RBBP7]] | -0.58 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[H3-3A]] | -0.55 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[ERLIN1]] | -0.54 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[CLSTN1]] | -0.53 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[NUP62CL]] | -0.53 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[CREG1]] | -0.53 | -0.43 / -0.43 | both halves | 4e-05 |  |
| [[ALDH7A1]] | -0.53 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[TWSG1]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[HDAC1]] | -0.52 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[SKP2]] | -0.52 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[SHMT1]] | -0.52 | -0.49 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SRP19's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NRAS]] | C | NRAS activity raises SRP19's level | recorded gain-of-function mutation of NRAS in 7 lines vs 43 not recorded | 1.32× higher at baseline in the NRAS-altered lines | 0.311 over the table, 0.058 within its group | ⚠ within its group only (a lead); within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.414). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.1, -33.9); signed map (-10.1, -7.7). **Vector** length 91.6, 26.9% of its response variance represented; |z| ≥ 3 in 1,106 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.4 | +13.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +16.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +9.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.6 | +4.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +3.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -2.8 | +5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +2.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.5 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | +0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.3 | -4.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.0 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | signal recognition particle 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.2 — chr5:112,861,188-112,898,371 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Signal recognition particle |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [P09132](https://www.uniprot.org/uniprotkb/P09132) (Signal recognition particle 19 kDa protein):

> Component of the signal recognition particle (SRP) complex, a ribonucleoprotein complex that mediates the cotranslational targeting of secretory and membrane proteins to the endoplasmic reticulum (ER) (By similarity). Binds directly to 7SL RNA (By similarity). Mediates binding of SRP54 to the SRP complex (By similarity).

**Summary**, from NCBI Gene [6728](https://www.ncbi.nlm.nih.gov/gene/6728):

> Enables 7S RNA binding activity. Contributes to ribosome binding activity. Predicted to be involved in SRP-dependent cotranslational protein targeting to membrane, signal sequence recognition. Located in cytosol and nucleolus. Part of signal recognition particle, endoplasmic reticulum targeting. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11300](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11300) · Entrez [6728](https://www.ncbi.nlm.nih.gov/gene/6728) · UniProt [P09132](https://www.uniprot.org/uniprotkb/P09132) · Ensembl [ENSG00000153037](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153037)

## Data

Gene col 7681: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7681); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7681, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7681]; `tensor/DDL_lfc|DDL_z.npy` [7681]; `embed/gene_vectors.npy` [7681]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7681 or target_col == 7681). Every well: [[SRP19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRP19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
