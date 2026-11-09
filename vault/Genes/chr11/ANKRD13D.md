---
symbol: "ANKRD13D"
type: "gene"
col: 10317
ensembl_id: "ENSG00000172932"
name: "ankyrin repeat domain 13D"
location: "11q13.2"
module: 3
arm: "+"
pooled_cpm: 22.37
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 21
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# ANKRD13D

*ankyrin repeat domain 13D* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.25× (z +5.5, q 3e-05, up in 21 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.45× (z +4.5, q 0.001, up in 17 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 3.30×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.388× (z -22.9, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSNK1G2]] (+0.76, fdr 7e-06), [[UBTD1]] (+0.72, fdr 7e-06), [[NR2F6]] (+0.72, fdr 7e-06); moves opposite to [[RIPK2-DT]] (-0.66, fdr 7e-06), [[LIG4]] (-0.65, fdr 7e-06), [[ZXDB]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10317.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 3.30×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.25×** | +5.5 | 3e-05 | 21/47 (NCI-H23, A549, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.30×** | +4.6 | 0.001 | 19/48 (KATO III, AsPC-1, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +4.5 | 0.001 | 17/45 (NCI-H460, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.27×** | +4.0 | 0.011 | 18/43 (COLO 205, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.26×** | +3.9 | 0.011 | 17/47 (SW480, KATO III, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.23×** | +3.5 | 0.043 | 14/48 (KATO III, PANC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10317.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.388×** | -22.9 | 0e+00 | 42/47 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.465×** | -12.6 | 8e-34 | 40/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.504×** | -11.7 | 3e-29 | 32/47 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.586×** | -8.8 | 3e-16 | 22/32 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.639×** | -7.1 | 2e-10 | 25/38 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.671×** | -6.8 | 9e-10 | 30/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.728×** | -5.6 | 1e-06 | 24/48 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.751×** | -4.9 | 7e-05 | 23/47 (MIA PaCa-2, HepG2/C3A, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.754×** | -4.8 | 9e-05 | 20/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.766×** | -4.4 | 7e-04 | 18/47 (SW 900, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.763×** | -4.3 | 1e-03 | 18/47 (NCI-H23, SW 900, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.778×** | -4.1 | 0.002 | 19/47 (HOP62, NCI-H1792, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.850× | -3.9 | 0.004 | 14/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.798×** | -3.9 | 0.004 | 21/42 (NCI-H1792, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.831×** | -3.9 | 0.004 | 16/48 (HOP62, C-33 A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.799×** | -3.8 | 0.004 | 18/48 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.837× | -3.7 | 0.007 | 14/48 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.815×** | -3.5 | 0.015 | 14/47 (NCI-H1573, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10317. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 37.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -14.8) |
| [[PANC-1 (line)]] | alt | 18.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -25.5) |
| [[NCI-H1792 (line)]] | alt | 49.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.428× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 34.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.230× (z -9.1) |
| [[A-172 (line)]] | wt | 21.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -17.5) |
| [[NCI-H1573 (line)]] | alt | 28.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -21.7) |
| [[SW 900 (line)]] | alt | 34.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -16.6) |
| [[A-427 (line)]] | wt | 32.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -17.8) |
| [[Hs 766T (line)]] | wt | 15.8 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0720× (z -15.4) ⚠ transcription drop; cell-cycle shift, explains ~77% of this change · without an alert: [[Sulfisoxazole (drug)]] 0.5 µM 0.216× (z -9.0) |
| [[HS-578T (line)]] | alt | 24.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -23.5) |
| [[MIA PaCa-2 (line)]] | alt | 25.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 28.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -17.5) |
| [[NCI-H23 (line)]] | alt | 49.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 15.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -17.3) |
| [[SHP-77 (line)]] | alt | 33.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.30× (z +8.6) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.102× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 17.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -9.9) |
| [[A549 (line)]] | wt | 15.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -13.5) |
| [[AsPC-1 (line)]] | alt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -8.9) |
| [[BT-474 (line)]] | alt | 30.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -11.2) |
| [[C32 (line)]] | wt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -12.3) |
| [[COLO 205 (line)]] | alt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -9.9) |
| [[H4 (line)]] | wt | 15.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -12.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 18.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 19.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -8.9) |
| [[J82 (line)]] | alt | 25.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0717× (z -17.9) |
| [[SNU-1 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.145× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~83% of this change |
| [[SNU-423 (line)]] | alt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -13.7) |
| [[SW1417 (line)]] | alt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -11.9) |
| [[AN3 CA (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10317), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSNK1G2]] | +0.76 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[UBTD1]] | +0.72 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[NR2F6]] | +0.72 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[NFATC3]] | +0.70 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[AP1S1]] | +0.69 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[FOXK2]] | +0.67 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[SDHAF1]] | +0.66 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[SH3GL1]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[RNF168]] | +0.64 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[AGAP3]] | +0.64 | +0.59 / +0.69 | both halves | 7e-06 | same gene group |
| [[SH2B2]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[SMARCD2]] | +0.64 | +0.66 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIPK2-DT]] | -0.66 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[LIG4]] | -0.65 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[ZXDB]] | -0.65 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[USP40]] | -0.64 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[CFL2]] | -0.64 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[OCIAD1]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[DZIP3]] | -0.63 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[ZXDA]] | -0.63 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[TIA1]] | -0.62 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[NCOA4]] | -0.62 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[ZNF260]] | -0.61 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[FILIP1L]] | -0.61 | -0.64 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises ANKRD13D's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-9.4, -4.0); signed map (-42.3, 2.1). **Vector** length 109, 25.9% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +3.5 | +3.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.2 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +2.0 | +2.8 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.8 | +1.7 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.8 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.8 | -22.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.4 | -11.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.3 | -12.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.0 | -6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.4 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.0 | -4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.8 | -3.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -3.6 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 13D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:67,289,300-67,302,485 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZTN6](https://www.uniprot.org/uniprotkb/Q6ZTN6) (Ankyrin repeat domain-containing protein 13D):

> Ubiquitin-binding protein that specifically recognizes and binds 'Lys-63'-linked ubiquitin. Does not bind 'Lys-48'-linked ubiquitin. Positively regulates the internalization of ligand-activated EGFR by binding to the Ub moiety of ubiquitinated EGFR at the cell membrane.

**Summary**, from NCBI Gene [338692](https://www.ncbi.nlm.nih.gov/gene/338692):

> The protein encoded by this gene is a member of the ankyrin repeat domain (ANKRD) 13 family, which currently consists of four proteins containing ubiquitin-interacting motifs. These proteins are integral membrane proteins that bind specifically to Lys-63-linked ubiquitin chains on membrane-bound proteins, targeting those proteins for rapid internalization. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:27880](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27880) · Entrez [338692](https://www.ncbi.nlm.nih.gov/gene/338692) · UniProt [Q6ZTN6](https://www.uniprot.org/uniprotkb/Q6ZTN6) · Ensembl [ENSG00000172932](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172932)

## Data

Gene col 10317: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10317); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10317, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10317]; `tensor/DDL_lfc|DDL_z.npy` [10317]; `embed/gene_vectors.npy` [10317]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10317 or target_col == 10317). Every well: [[ANKRD13D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD13D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
