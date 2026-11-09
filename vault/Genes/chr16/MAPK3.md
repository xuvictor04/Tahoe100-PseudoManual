---
symbol: "MAPK3"
type: "gene"
col: 2281
ensembl_id: "ENSG00000102882"
name: "mitogen-activated protein kinase 3"
location: "16p11.2"
module: 30
arm: "+"
pooled_cpm: 9.85
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 30
n_dd_up_clean: 1
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# MAPK3

*mitogen-activated protein kinase 3* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.12× (z +9.5, q 8e-19, up in 19 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 1.33× (z +3.6, q 0.028, up in 10 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 3.68×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.467× (z -14.2, q 5e-43, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A23]] (+0.71, fdr 1e-05), [[PLD2]] (+0.69, fdr 7e-06), [[USP30]] (+0.69, fdr 7e-06); moves opposite to [[SLFNL1-AS1]] (-0.62, fdr 7e-06), [[SPOPL-DT]] (-0.61, fdr 1e-05), [[SIPA1L1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2281.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 3.68×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +9.5 | 8e-19 | 19/22 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +9.1 | 2e-17 | 28/34 (Panc 03.27, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +6.1 | 3e-07 | 17/28 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.29×** | +4.7 | 3e-04 | 18/48 (CFPAC-1, HOP62, …) | rises with dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +4.0 | 0.007 | 16/41 (LS 180, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.028 | 10/47 (PANC-1, A498, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.28× | +3.1 | 0.18 | 7/46 (LOX-IMVI, SHP-77, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2281.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.467×** | -14.2 | 5e-43 | 34/45 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.420×** | -11.4 | 7e-28 | 34/45 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.582×** | -10.1 | 1e-21 | 31/44 (KATO III, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.489×** | -9.4 | 6e-19 | 31/45 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.493×** | -9.3 | 1e-18 | 39/47 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.515×** | -8.7 | 2e-16 | 36/48 (LS 180, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.510×** | -8.5 | 1e-15 | 31/47 (HCT15, H4, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.574×** | -7.0 | 1e-10 | 24/45 (LS 180, C-33 A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.635×** | -6.0 | 1e-07 | 27/46 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.640×** | -5.9 | 2e-07 | 24/47 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.743×** | -5.5 | 2e-06 | 20/48 (COLO 205, A498, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.680×** | -4.9 | 5e-05 | 16/39 (NCI-H23, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.686×** | -4.8 | 8e-05 | 20/46 (LS 180, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.697×** | -4.8 | 8e-05 | 20/47 (Hs 766T, A549, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.707×** | -4.5 | 2e-04 | 20/46 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.715×** | -4.4 | 4e-04 | 12/47 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.735×** | -3.8 | 0.004 | 18/47 (PANC-1, SW480, …) | inconsistent across doses | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.604×** | -3.5 | 0.014 | 12/42 (hTERT-HPNE, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.761×** | -3.4 | 0.018 | 10/45 (HT-29, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.784×** | -3.2 | 0.033 | 8/47 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.635×** | -3.1 | 0.038 | 8/43 (LOX-IMVI, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.802×** | -2.9 | 0.078 | 9/47 (HT-29, LoVo, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.51 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2281. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 15.9 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -13.9) |
| [[LOX-IMVI (line)]] | wt | 8.52 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0314× (z -16.2) |
| [[CFPAC-1 (line)]] | alt | 12.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.290× (z -10.0) |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -11.2) |
| [[HT-29 (line)]] | alt | 11.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -14.9) |
| [[MIA PaCa-2 (line)]] | alt | 16.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -9.5) |
| [[A-172 (line)]] | wt | 19.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -8.7) |
| [[A549 (line)]] | wt | 8.02 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[AsPC-1 (line)]] | alt | 8.93 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -11.1) |
| [[C-33 A (line)]] | alt | 7.72 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -9.0) |
| [[HCT15 (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 7.62 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0831× (z -9.1) |
| [[HOP62 (line)]] | alt | 6.55 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0615× (z -13.9) |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -12.8) |
| [[KATO III (line)]] | alt | 9.37 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 8.54 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.153× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 7.59 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -10.1) |
| [[PANC-1 (line)]] | alt | 9.57 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +8.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 9.81 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.125× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0759× (z -10.2) |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -8.8) |
| [[SW480 (line)]] | alt | 8.67 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -13.4) |
| [[A-427 (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2281), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A23]] | +0.71 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[PLD2]] | +0.69 | +0.69 / +0.60 | both halves | 7e-06 | pathway: Fcgamma receptor (FCGR) dependent phagocytosis |
| [[USP30]] | +0.69 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[VAT1]] | +0.66 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[FKBP8]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[C20orf96]] | +0.64 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[TMEM9]] | +0.63 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[CAT]] | +0.63 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[BAD]] | +0.63 | +0.71 / +0.47 | both halves | 2e-05 | pathway: Apoptosis; STRING 932 |
| [[UBAC1]] | +0.62 | +0.68 / +0.40 | both halves | 4e-05 |  |
| [[PNKD]] | +0.62 | +0.60 / +0.47 | both halves | 2e-05 | STRING 401 |
| [[ABCA2]] | +0.61 | +0.65 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLFNL1-AS1]] | -0.62 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[SPOPL-DT]] | -0.61 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[SIPA1L1]] | -0.61 | -0.52 / -0.52 | both halves | 1e-05 | pathway: Neuronal System |
| [[ENOX2]] | -0.59 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[NOP56]] | -0.59 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[TASOR2]] | -0.59 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[KCNJ14]] | -0.58 | -0.49 / -0.57 | both halves | 1e-05 | pathway: Neuronal System |
| [[SATB2]] | -0.58 | -0.56 / -0.44 | both halves | 3e-05 | pathway: RUNX2 regulates bone development |
| [[SNRPB]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.55 | -0.60 / -0.37 | both halves | 7e-05 |  |
| [[NHSL1]] | -0.55 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[PPIEL-1]] | -0.55 | -0.52 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MAPK3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EPS8L2]] | B | EPS8L2 activity strengthens MAPK3's drug response | lines that do not express EPS8L2 (19) vs lines expressing it (29) | the lines without EPS8L2 respond 0.57× as strongly (z diff +1.39); strongest at Homoharringtonine 5 µM: 0.55x vs 0.37x (z diff +2.8) | 0.059 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[YPEL2]] | C | YPEL2 activity raises MAPK3's level | lines that do not express YPEL2 (3) vs lines expressing it (47) | 1.26× lower at baseline in the lines without YPEL2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MAGI1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.614). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.5, -7.9); signed map (-30.0, -4.1). **Vector** length 68.8, 11.5% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +9.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.3 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.7 | -3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -11.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -9.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.8 | -7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.7 | -4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.5 | +0.1 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,114,105-30,123,506 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ERK1, p44mapk, p44erk1, ERK-1; previously PRKM3 |
| Gene groups (HGNC) | Mitogen-activated protein kinase 3 and 1 (ERK1/2) family |
| Reactome | 166 pathways, smallest: Signaling by MAP2K mutants; Negative feedback regulation of MAPK pathway; Suppression of apoptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P27361](https://www.uniprot.org/uniprotkb/P27361) (Mitogen-activated protein kinase 3):

> Serine/threonine kinase which acts as an essential component of the MAP kinase signal transduction pathway. MAPK1/ERK2 and MAPK3/ERK1 are the 2 MAPKs which play an important role in the MAPK/ERK cascade. They participate also in a signaling cascade initiated by activated KIT and KITLG/SCF. Depending on the cellular context, the MAPK/ERK cascade mediates diverse biological functions such as cell growth, adhesion, survival and differentiation through the regulation of transcription, translation, …

**Summary**, from NCBI Gene [5595](https://www.ncbi.nlm.nih.gov/gene/5595):

> The protein encoded by this gene is a member of the MAP kinase family. MAP kinases, also known as extracellular signal-regulated kinases (ERKs), act in a signaling cascade that regulates various cellular processes such as proliferation, differentiation, and cell cycle progression in response to a variety of extracellular signals. This kinase is activated by upstream kinases, resulting in its translocation to the nucleus where it phosphorylates nuclear targets. Alternatively spliced transcript …

**Accessions** — [HGNC:6877](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6877) · Entrez [5595](https://www.ncbi.nlm.nih.gov/gene/5595) · UniProt [P27361](https://www.uniprot.org/uniprotkb/P27361) · Ensembl [ENSG00000102882](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102882)

## Data

Gene col 2281: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2281); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2281, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2281]; `tensor/DDL_lfc|DDL_z.npy` [2281]; `embed/gene_vectors.npy` [2281]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2281 or target_col == 2281). Every well: [[MAPK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
