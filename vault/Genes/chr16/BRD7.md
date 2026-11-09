---
symbol: "BRD7"
type: "gene"
col: 9248
ensembl_id: "ENSG00000166164"
name: "bromodomain containing 7"
location: "16q12.1"
module: 37
arm: "+"
pooled_cpm: 74.84
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# BRD7

*bromodomain containing 7* — 16q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.55× (z +9.6, q 4e-19, up in 33 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.57× (z +5.2, q 4e-05, up in 26 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.730× (z -9.7, q 1e-19, down in 36 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (SW480 0.507×, RKO 0.491×, HOP62 0.515×, NCI-H2030 0.590×, …); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.126×, NCI-H1573 0.469×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (SW 1271 0.0797×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAAL1]] (+0.63, fdr 1e-05), [[TERF1]] (+0.61, fdr 1e-05), [[COG2]] (+0.60, fdr 3e-05); moves opposite to [[SMIM4]] (-0.66, fdr 2e-05), [[LSMEM1]] (-0.66, fdr 1e-05), [[TICAM2]] (-0.65, fdr 1e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLSCR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9248.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.55×** | +9.6 | 4e-19 | 33/49 (Hs 766T, HOP62, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.35×** | +6.1 | 3e-07 | 28/45 (SNU-1, KATO III, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.57×** | +5.2 | 4e-05 | 26/49 (A498, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.26×** | +5.0 | 9e-05 | 22/44 (NCI-H460, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.25×** | +4.9 | 1e-04 | 24/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.24×** | +4.8 | 2e-04 | 23/48 (RPMI-7951, SNU-423, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +4.4 | 6e-04 | 22/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.22×** | +4.4 | 6e-04 | 24/48 (RPMI-7951, hTERT-HPNE, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +4.4 | 6e-04 | 24/48 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.45×** | +4.3 | 0.001 | 23/48 (A498, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.44×** | +4.2 | 0.001 | 24/47 (NCI-H2030, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.0 | 0.003 | 22/44 (HOP62, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | 1.20× | +3.8 | 0.006 | 20/47 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.023 | 17/48 (HCT15, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.026 | 13/48 (SW 900, C-33 A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.066 | 14/47 (NCI-H460, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.066 | 12/48 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.14× | +2.9 | 0.098 | 9/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9248.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (SW480 0.507×, RKO 0.491×, HOP62 0.515×, NCI-H2030 0.590×, …); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.126×, NCI-H1573 0.469×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (SW 1271 0.0797×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.730×** | -9.7 | 1e-19 | 36/49 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.842× | -5.3 | 3e-05 | 23/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | 0.861× | -4.6 | 8e-04 | 19/48 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.954× | -3.3 | 0.16 | 1/50 (NCI-H2122) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.871× | -3.0 | 0.30 | 9/48 (SW 1271, HOP62, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9248. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 56.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 86.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.24× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.469× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[BT-474 (line)]] | alt | 76.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -8.5) |
| [[C-33 A (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -21.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[HepG2_C3A (line)]] | wt | 97.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -10.7) |
| [[Hs 766T (line)]] | wt | 61.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[J82 (line)]] | alt | 63.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 63.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 101 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 41.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H2030 (line)]] | alt | 151 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 78.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 71.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.92× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | — |
| [[Panc 03.27 (line)]] | alt | 60.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[PANC-1 (line)]] | alt | 53.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -8.7) |
| [[RKO (line)]] | wt | 106 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 55.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | — |
| [[SNU-1 (line)]] | wt | 85.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.81× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW 1271 (line)]] | alt | 52.9 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0797× (z -8.7) |
| [[SW480 (line)]] | alt | 127 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -12.8) |
| [[A-172 (line)]] | wt | 69.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 94.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 77.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 75.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 102 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 56.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 77.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 83.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 88.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 112 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9248), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAAL1]] | +0.63 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[TERF1]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[COG2]] | +0.60 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[RBM17]] | +0.60 | +0.60 / +0.65 | both halves | 7e-06 | pathway: ATP-dependent chromatin remodelers |
| [[COMMD2]] | +0.59 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[FAM98B]] | +0.58 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[WDR70]] | +0.57 | +0.30 / +0.52 | both halves | 2e-04 |  |
| [[REPS1]] | +0.57 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[WDR7]] | +0.57 | +0.36 / +0.50 | both halves | 1e-04 |  |
| [[EHMT2]] | +0.57 | +0.45 / +0.39 | both halves | 5e-05 | pathway: Regulation of TP53 Activity |
| [[COPG2]] | +0.57 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[VPS50]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM4]] | -0.66 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[LSMEM1]] | -0.66 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[TICAM2]] | -0.65 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[SNX31]] | -0.62 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[LINC02936]] | -0.62 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[LRP2BP]] | -0.60 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[ADCY10]] | -0.58 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[CASS4]] | -0.58 | -0.44 / -0.32 | both halves | 1e-04 |  |
| [[SIAH2-AS1]] | -0.58 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[EPHX1]] | -0.58 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[CORIN]] | -0.57 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[LINC00880]] | -0.57 | -0.31 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLSCR2]] | B | PLSCR2 activity lowers BRD7's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 1.46× higher at baseline in the lines without PLSCR2 | 0.077 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction -0.597). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.3, -14.2); signed map (-22.9, -17.2). **Vector** length 88.7, 21.3% of its response variance represented; |z| ≥ 3 in 701 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.3 | +4.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.2 | +4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +4.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.7 | +4.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.1 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -5.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.4 | -0.7 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | bromodomain containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.1 — chr16:50,313,487-50,368,988 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CELTIX1, BP75, SMARCI1 |
| Gene groups (HGNC) | Bromodomain containing; PBAF complex subunits |
| Reactome | 7 pathways, smallest: Formation of the polybromo-BAF (pBAF) complex; Regulation of TP53 Activity through Acetylation; SWI/SNF chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPI1](https://www.uniprot.org/uniprotkb/Q9NPI1) (Bromodomain-containing protein 7):

> Acts both as coactivator and as corepressor. May play a role in chromatin remodeling. Activator of the Wnt signaling pathway in a DVL1-dependent manner by negatively regulating the GSK3B phosphotransferase activity. Induces dephosphorylation of GSK3B at 'Tyr-216'. Down-regulates TRIM24-mediated activation of transcriptional activation by AR (By similarity). Transcriptional corepressor that down-regulates the expression of target genes. Binds to target promoters, leading to increased histone H3 …

**Summary**, from NCBI Gene [29117](https://www.ncbi.nlm.nih.gov/gene/29117):

> This gene encodes a protein which is a member of the bromodomain-containing protein family. The product of this gene has been identified as a component of one form of the SWI/SNF chromatin remodeling complex, and as a protein which interacts with p53 and is required for p53-dependent oncogene-induced senescence which prevents tumor growth. Pseudogenes have been described on chromosomes 2, 3, 6, 13 and 14. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul …

**Accessions** — [HGNC:14310](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14310) · Entrez [29117](https://www.ncbi.nlm.nih.gov/gene/29117) · UniProt [Q9NPI1](https://www.uniprot.org/uniprotkb/Q9NPI1) · Ensembl [ENSG00000166164](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166164)

## Data

Gene col 9248: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9248); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9248, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9248]; `tensor/DDL_lfc|DDL_z.npy` [9248]; `embed/gene_vectors.npy` [9248]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9248 or target_col == 9248). Every well: [[BRD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
