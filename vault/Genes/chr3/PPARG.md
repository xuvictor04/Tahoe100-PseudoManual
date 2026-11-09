---
symbol: "PPARG"
type: "gene"
col: 5281
ensembl_id: "ENSG00000132170"
name: "peroxisome proliferator activated receptor gamma"
location: "3p25.2"
module: 31
arm: "+"
pooled_cpm: 118.03
n_lines_expressing: 30
n_dd_up: 2
n_dd_down: 28
n_dd_up_clean: 1
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 38
direction_downstream: 35
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# PPARG

*peroxisome proliferator activated receptor gamma* — 3p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.20× (z +5.4, q 3e-05, up in 12 of 28 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (CFPAC-1 2.65×, SNU-423 2.98×, A498 1.90×, AsPC-1 2.25×, …; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A498 2.75×); [[Auranofin (drug)]] 5 µM in 1 line (A-427 3.15×).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.615× (z -14.3, q 2e-43, down in 26 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNS4]] (+0.63, fdr 1e-05), [[KIF13B]] (+0.60, fdr 2e-05), [[BAIAP2L1]] (+0.59, fdr 1e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 38 arrows point to it, the strongest [[LINC00511]] → it (grade B ⚠); 35 go from it, the strongest it → [[TCF7L2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5281.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (CFPAC-1 2.65×, SNU-423 2.98×, A498 1.90×, AsPC-1 2.25×, …; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A498 2.75×); [[Auranofin (drug)]] 5 µM in 1 line (A-427 3.15×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +5.4 | 3e-05 | 12/28 (CFPAC-1, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +5.3 | 3e-05 | 15/28 (A498, A549, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.22×** | +4.2 | 0.005 | 13/29 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +3.5 | 0.059 | 9/29 (A498, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5281.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.615×** | -14.3 | 2e-43 | 26/29 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.546×** | -12.1 | 4e-31 | 25/28 (LoVo, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.584×** | -10.7 | 1e-24 | 23/28 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.589×** | -10.6 | 7e-24 | 22/27 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.622×** | -9.8 | 9e-21 | 20/29 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.674×** | -7.9 | 4e-13 | 25/30 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.673×** | -7.6 | 3e-12 | 22/27 (Panc 03.27, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.780×** | -7.3 | 3e-11 | 18/28 (J82, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.710×** | -7.1 | 8e-11 | 15/28 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.726×** | -6.6 | 2e-09 | 21/28 (KATO III, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.736×** | -6.3 | 1e-08 | 19/28 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.752×** | -5.9 | 2e-07 | 14/28 (LS 180, SW480, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.770×** | -5.4 | 3e-06 | 20/28 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.770×** | -5.4 | 3e-06 | 14/28 (NCI-H1573, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.791×** | -4.8 | 5e-05 | 15/28 (SW480, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.794×** | -4.6 | 1e-04 | 11/28 (AsPC-1, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.806×** | -4.5 | 3e-04 | 15/28 (CFPAC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.812×** | -4.1 | 0.001 | 12/28 (Hs 766T, HepG2/C3A, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.822×** | -4.0 | 0.001 | 10/29 (HepG2/C3A, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.826×** | -3.8 | 0.004 | 13/28 (Hs 766T, LoVo, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.712×** | -3.7 | 0.006 | 11/29 (Panc 03.27, Hs 766T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5281. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 614 | 0 | 17 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -23.5) |
| [[Hs 766T (line)]] | wt | 267 | 0 | 15 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -14.6) |
| [[LoVo (line)]] | wt | 439 | 0 | 14 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -22.5) |
| [[KATO III (line)]] | alt | 257 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -15.1) |
| [[SW480 (line)]] | alt | 150 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -11.7) |
| [[A498 (line)]] | wt | 102 | 2 (1 ⚠) | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.75× (z +12.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -14.6) |
| [[NCI-H1573 (line)]] | alt | 50.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.234× (z -12.4) |
| [[HepG2_C3A (line)]] | wt | 128 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 119 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.503× (z -8.9) |
| [[PANC-1 (line)]] | alt | 184 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.360× (z -10.8) |
| [[SW1417 (line)]] | alt | 223 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.571× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 276 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.299× (z -11.2) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 161 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -12.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 60.0 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -14.1) |
| [[A549 (line)]] | wt | 154 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -14.8) |
| [[HOP62 (line)]] | alt | 62.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -9.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.284× (z -8.5) |
| [[HT-29 (line)]] | alt | 236 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -12.0) |
| [[J82 (line)]] | alt | 76.3 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.42× (z +8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Selinexor (drug)]] 5 µM 0.521× (z -9.3) |
| [[SNU-423 (line)]] | alt | 66.5 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +14.3) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.500× (z -9.1) |
| [[A-427 (line)]] | wt | 39.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.15× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 89.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +14.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CHP-212 (line)]] | wt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -8.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 201 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -12.6) |
| [[NCI-H2347 (line)]] | alt | 161 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -8.9) |
| [[SW 900 (line)]] | alt | 91.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -8.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 18.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 17.5 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 22.9 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.89 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 21.4 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.52 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 20.1 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.16 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.25 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 15.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5281), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNS4]] | +0.63 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[KIF13B]] | +0.60 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[BAIAP2L1]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[ONECUT3]] | +0.59 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[PKP2]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[PPP3CA]] | +0.57 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[FOXO1]] | +0.56 | +0.50 / +0.49 | both halves | 1e-05 | pathway: Intracellular signaling by second messengers; STRING 856 |
| [[PDE9A]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[CALB1]] | +0.54 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[EFNB2]] | +0.54 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[MMP28]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[B3GNT3]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 23, C 15. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00511]] | B | LINC00511 activity raises PPARG's level | lines that do not express LINC00511 (12) vs lines expressing it (38) | 4.50× lower at baseline in the lines without LINC00511 | 0.007 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18 |
| [[FA2H]] | B | FA2H activity raises PPARG's level | lines that do not express FA2H (27) vs lines expressing it (23) | 3.45× lower at baseline in the lines without FA2H | 0.015 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[MAML2]] | B | MAML2 activity raises PPARG's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 4.10× lower at baseline in the lines without MAML2 | 0.018 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[SYNE3]] | B | SYNE3 activity raises PPARG's level | lines that do not express SYNE3 (11) vs lines expressing it (39) | 2.51× lower at baseline in the lines without SYNE3 | 0.018 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC01819]] | B | LINC01819 activity raises PPARG's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 2.38× lower at baseline in the lines without LINC01819 | 0.030 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent |
| [[SLC52A3]] | B | SLC52A3 activity raises PPARG's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 3.40× lower at baseline in the lines without SLC52A3 | 0.030 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[TBC1D8]] | B | TBC1D8 activity raises PPARG's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 3.92× lower at baseline in the lines without TBC1D8 | 0.035 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[NPSR1]] | B | NPSR1 activity raises PPARG's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 6.00× lower at baseline in the lines without NPSR1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |
| [[CAPN8]] | B | CAPN8 activity raises PPARG's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 3.81× lower at baseline in the lines without CAPN8 | 0.041 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38 |
| [[MYO7B]] | B | MYO7B activity raises PPARG's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 2.47× lower at baseline in the lines without MYO7B | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[CYP3A5]] | B | CYP3A5 activity raises PPARG's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 3.67× lower at baseline in the lines without CYP3A5 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[IGSF9]] | B | IGSF9 activity raises PPARG's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 2.12× lower at baseline in the lines without IGSF9 | 0.054 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 23, C 12. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF7L2]] | B | PPARG activity raises TCF7L2's level | lines that do not express PPARG (20) vs lines expressing it (30) | 1.80× lower at baseline in the lines without PPARG | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[TBC1D8]] | B | PPARG activity raises TBC1D8's level | lines that do not express PPARG (20) vs lines expressing it (30) | 2.30× lower at baseline in the lines without PPARG | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[EPS8]] | B | PPARG activity raises EPS8's level | lines that do not express PPARG (20) vs lines expressing it (30) | 2.20× lower at baseline in the lines without PPARG | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[ITGA6]] | B | PPARG activity raises ITGA6's level | lines that do not express PPARG (20) vs lines expressing it (30) | 1.97× lower at baseline in the lines without PPARG | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[MAML2]] | B | PPARG activity raises MAML2's level | lines that do not express PPARG (20) vs lines expressing it (30) | 2.39× lower at baseline in the lines without PPARG | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[LINC00511]] | B | PPARG activity raises LINC00511's level | lines that do not express PPARG (20) vs lines expressing it (30) | 2.58× lower at baseline in the lines without PPARG | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[ARHGAP26]] | B | PPARG activity raises ARHGAP26's level | lines that do not express PPARG (20) vs lines expressing it (30) | 2.20× lower at baseline in the lines without PPARG | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[HS3ST1]] | B | PPARG activity raises HS3ST1's level | lines that do not express PPARG (20) vs lines expressing it (30) | 2.79× lower at baseline in the lines without PPARG | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[STK17B]] | B | PPARG activity raises STK17B's level | lines that do not express PPARG (20) vs lines expressing it (30) | 1.43× lower at baseline in the lines without PPARG | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[SH3TC1]] | B | PPARG activity raises SH3TC1's level | lines that do not express PPARG (20) vs lines expressing it (30) | 2.07× lower at baseline in the lines without PPARG | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[CYP3A5]] | B | PPARG activity raises CYP3A5's level | lines that do not express PPARG (20) vs lines expressing it (30) | 2.59× lower at baseline in the lines without PPARG | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[SYNE3]] | B | PPARG activity raises SYNE3's level | lines that do not express PPARG (20) vs lines expressing it (30) | 1.67× lower at baseline in the lines without PPARG | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.7, 48.4); signed map (10.8, 33.3). **Vector** length 103, 29.2% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +5.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.1 | +5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.8 | +0.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | -1.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +2.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +1.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -3.7 | -3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.0 | -12.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.0 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.6 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.5 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | peroxisome proliferator activated receptor gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.2 — chr3:12,287,368-12,434,356 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PPARG1, PPARG2, NR1C3, PPARgamma |
| Gene groups (HGNC) | Peroxisome proliferator activated receptors |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, UV_RESPONSE_DN, ADIPOGENESIS |
| Reactome | 22 pathways, smallest: MECP2 regulates transcription factors; Transcriptional regulation of brown and beige adipocyte differentiation; Transcriptional regulation of brown and beige adipocyte differentiation by EBF2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P37231](https://www.uniprot.org/uniprotkb/P37231) (Peroxisome proliferator-activated receptor gamma):

> Ligand-activated transcription factor that forms obligate heterodimers with the retinoic acid receptor and acts as a key regulator of biological processes, such as adipocyte differentiation, lipid metabolism, glucose homeostasis and beta-oxidation of fatty acids. Activated by lipid ligands: binds peroxisome proliferators, such as hypolipidemic drugs, and fatty acids, such as prostaglandin J2 metabolites. Ligand-binding results in a conformational change in the receptor, promoting dissociation …

**Summary**, from NCBI Gene [5468](https://www.ncbi.nlm.nih.gov/gene/5468):

> This gene encodes a member of the peroxisome proliferator-activated receptor (PPAR) subfamily of nuclear receptors. PPARs form heterodimers with retinoid X receptors (RXRs) and these heterodimers regulate transcription of various genes. Three subtypes of PPARs are known: PPAR-alpha, PPAR-delta, and PPAR-gamma. The protein encoded by this gene is PPAR-gamma and is a regulator of adipocyte differentiation. Additionally, PPAR-gamma has been implicated in the pathology of numerous diseases …

**Accessions** — [HGNC:9236](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9236) · Entrez [5468](https://www.ncbi.nlm.nih.gov/gene/5468) · UniProt [P37231](https://www.uniprot.org/uniprotkb/P37231) · Ensembl [ENSG00000132170](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132170)

## Data

Gene col 5281: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5281); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5281, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5281]; `tensor/DDL_lfc|DDL_z.npy` [5281]; `embed/gene_vectors.npy` [5281]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5281 or target_col == 5281). Every well: [[PPARG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPARG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
