---
symbol: "NRBF2"
type: "gene"
col: 7296
ensembl_id: "ENSG00000148572"
name: "nuclear receptor binding factor 2"
location: "10q21.3"
module: 12
arm: "+"
pooled_cpm: 33.63
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# NRBF2

*nuclear receptor binding factor 2* — 10q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.79× (z +13.5, q 5e-39, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.438× (z -12.6, q 2e-33, down in 31 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.738× (z -5.0, q 6e-05, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC174]] (+0.79, fdr 7e-06), [[SNRPB2]] (+0.75, fdr 7e-06), [[ZNF622]] (+0.73, fdr 7e-06); moves opposite to [[CPSF6]] (-0.70, fdr 7e-06), [[VMA21]] (-0.65, fdr 1e-05), [[NUDT3]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7296.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.79×** | +13.5 | 5e-39 | 46/49 (SW480, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +9.9 | 1e-20 | 41/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.52×** | +9.8 | 3e-20 | 35/47 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.44×** | +5.8 | 8e-07 | 28/48 (PANC-1, A549, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +4.8 | 2e-04 | 25/45 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +4.1 | 0.004 | 23/45 (NCI-H1573, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.27×** | +4.0 | 0.006 | 21/48 (A549, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.8 | 0.010 | 17/48 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.031 | 19/47 (MIA PaCa-2, Hs 766T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.039 | 18/48 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.3 | 0.049 | 16/41 (SK-MEL-2, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.092 | 8/48 (A549, HOP62, …) | top dose only | plate-row cell shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.092 | 14/45 (NCI-H460, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.20×** | +3.1 | 0.092 | 15/45 (SW480, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.0 | 0.094 | 14/48 (J82, A549, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7296.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.438×** | -12.6 | 2e-33 | 31/37 (A549, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.498×** | -11.0 | 7e-26 | 29/34 (AsPC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.522×** | -10.7 | 2e-24 | 33/44 (AsPC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.727×** | -5.2 | 2e-05 | 24/46 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.738×** | -5.0 | 6e-05 | 24/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.763×** | -4.3 | 0.002 | 26/48 (COLO 205, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.778×** | -4.1 | 0.003 | 18/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.781×** | -4.1 | 0.004 | 22/48 (SNU-423, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 5 µM |  | **0.794×** | -3.6 | 0.017 | 16/47 (HepG2/C3A, SW48, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.812×** | -3.4 | 0.036 | 14/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.865× | -3.4 | 0.041 | 10/48 (Hs 766T, J82, …) | inconsistent across doses |  |
| [[Fusidic acid (drug)]] 5 µM |  | 0.870× | -3.2 | 0.063 | 9/48 (PANC-1, SW 900, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.698×** | -3.1 | 0.086 | 13/31 (NCI-H2347, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7296. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 32.4 | 4 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +17.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.44× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.0572× (z -22.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 38.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.47× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -14.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 31.5 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +18.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.34× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 44.3 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.1) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 5 µM 0.213× (z -12.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 69.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.331× (z -12.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 34.7 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.57× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -16.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 31.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.318× (z -10.3) |
| [[SW480 (line)]] | alt | 37.7 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.57× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.415× (z -8.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 54.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0617× (z -26.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 36.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.0) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 5 µM 0.360× (z -8.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 36.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -16.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 42.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -9.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 33.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.42× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -15.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 53.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -17.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 49.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -12.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.251× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 27.4 | 0 | 1 | — | [[Bendamustine (drug)]] 0.05 µM 0.0595× (z -10.2) |
| [[BT-474 (line)]] | alt | 25.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -9.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 16.8 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.154× (z -8.7) |
| [[H4 (line)]] | wt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -11.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +8.7) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[HepG2_C3A (line)]] | wt | 51.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +11.8) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[KATO III (line)]] | alt | 37.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -17.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -14.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 19.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +8.5) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2030 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0791× (z -12.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7296), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC174]] | +0.79 | +0.80 / +0.73 | both halves | 7e-06 |  |
| [[SNRPB2]] | +0.75 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[ZNF622]] | +0.73 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[YIPF5]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[MED19]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[RNF113A]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[NFKBIL1]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[ADPRM]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[NKAP]] | +0.67 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[GCC1]] | +0.67 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[ALG2]] | +0.67 | +0.48 / +0.77 | both halves | 2e-05 |  |
| [[ADPRS]] | +0.67 | +0.56 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF6]] | -0.70 | -0.61 / -0.71 | both halves | 7e-06 |  |
| [[VMA21]] | -0.65 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[NUDT3]] | -0.64 | -0.58 / -0.69 | both halves | 7e-06 |  |
| [[RBBP7]] | -0.63 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[NUP210]] | -0.63 | -0.54 / -0.68 | both halves | 1e-05 |  |
| [[UBE2G2]] | -0.63 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[SELENON]] | -0.62 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[MAPK9]] | -0.62 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.61 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[CDK2]] | -0.59 | -0.61 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.762). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-39.3, -7.7); signed map (-10.5, -8.7). **Vector** length 116, 29.8% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +9.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.2 | +13.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +6.0 | +9.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.5 | +5.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +4.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.6 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +3.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.3 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -7.7 | -5.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.3 | -5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -7.1 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.6 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.4 | -10.7 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -2.4 | -3.2 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -2.1 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.1 | -2.5 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[Lumateperone (tosylate) (drug)]] 5 µM |  | -2.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor binding factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.3 — chr10:63,133,247-63,155,031 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp564C1664, FLJ30395, COPR1, COPR2 |
| Gene groups (HGNC) | PIK3C3 complex subunits |
| Reactome | 1 pathways, smallest: Nuclear Receptor transcription pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96F24](https://www.uniprot.org/uniprotkb/Q96F24) (Nuclear receptor-binding factor 2):

> May modulate transcriptional activation by target nuclear receptors. Can act as transcriptional activator (in vitro).; Involved in starvation-induced autophagy probably by its association with PI3K complex I (PI3KC3-C1). However, effects has been described variably. Involved in the induction of starvation-induced autophagy. Stabilizes PI3KC3-C1 assembly and enhances ATG14-linked lipid kinase activity of PIK3C3 (By similarity). Proposed to negatively regulate basal and starvation-induced …

**Summary**, from NCBI Gene [29982](https://www.ncbi.nlm.nih.gov/gene/29982):

> Involved in autophagy. Located in cytoplasm and phosphatidylinositol 3-kinase complex, class III. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19692](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19692) · Entrez [29982](https://www.ncbi.nlm.nih.gov/gene/29982) · UniProt [Q96F24](https://www.uniprot.org/uniprotkb/Q96F24) · Ensembl [ENSG00000148572](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148572)

## Data

Gene col 7296: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7296); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7296, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7296]; `tensor/DDL_lfc|DDL_z.npy` [7296]; `embed/gene_vectors.npy` [7296]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7296 or target_col == 7296). Every well: [[NRBF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRBF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
