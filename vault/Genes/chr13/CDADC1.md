---
symbol: "CDADC1"
type: "gene"
col: 2254
ensembl_id: "ENSG00000102543"
name: "cytidine and dCMP deaminase domain containing 1"
location: "13q14.2"
module: 30
arm: "+"
pooled_cpm: 20.94
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# CDADC1

*cytidine and dCMP deaminase domain containing 1* — 13q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.76× (z +10.0, q 6e-21, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.547× (z -10.8, q 3e-24, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 4 lines (SW480 0.387×, SNU-423 0.194×, HOP62 0.293×, SHP-77 0.220×); [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 0.114×, LS 180 0.129×, KATO III 0.143×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SW 900 0.114×, RPMI-7951 0.125×, LOX-IMVI 0.246×; ⚠ toxic; transcription drop); [[Drospirenone (drug)]] 0.5 µM in 1 line (CHP-212 0.0668×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFAF7]] (+0.74, fdr 7e-06), [[ALG9]] (+0.70, fdr 7e-06), [[MED23]] (+0.69, fdr 7e-06); moves opposite to [[SSUH2]] (-0.64, fdr 1e-05), [[MYO1C]] (-0.61, fdr 1e-05), [[CHD4]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CLSTN2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2254.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.76×** | +10.0 | 6e-21 | 41/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.66×** | +9.1 | 3e-17 | 36/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.66×** | +9.0 | 4e-17 | 34/48 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +8.9 | 7e-17 | 31/43 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.32×** | +7.0 | 3e-10 | 26/48 (RKO, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.23×** | +5.3 | 1e-05 | 21/47 (A-427, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +4.4 | 7e-04 | 16/48 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.61×** | +4.4 | 7e-04 | 15/48 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.28×** | +4.3 | 9e-04 | 13/48 (SNU-423, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.24×** | +3.7 | 0.014 | 16/48 (HepG2/C3A, LoVo, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.020 | 9/48 (SW480, A-427, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.22×** | +3.5 | 0.020 | 9/47 (J82, AsPC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.049 | 6/48 (AsPC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.20× | +3.2 | 0.052 | 4/47 (A498, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.058 | 14/47 (J82, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2254.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 4 lines (SW480 0.387×, SNU-423 0.194×, HOP62 0.293×, SHP-77 0.220×); [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 0.114×, LS 180 0.129×, KATO III 0.143×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SW 900 0.114×, RPMI-7951 0.125×, LOX-IMVI 0.246×; ⚠ toxic; transcription drop); [[Drospirenone (drug)]] 0.5 µM in 1 line (CHP-212 0.0668×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.547×** | -10.8 | 3e-24 | 35/48 (SW480, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.619×** | -8.6 | 3e-15 | 24/41 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.742×** | -5.1 | 6e-05 | 16/33 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.749×** | -4.9 | 1e-04 | 20/47 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -4.4 | 1e-03 | 5/48 (LoVo, SW48, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.788×** | -4.2 | 0.002 | 17/48 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.797×** | -3.7 | 0.015 | 18/37 (SW 900, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ritonavir (drug)]] 5 µM |  | 0.877× | -3.3 | 0.064 | 12/48 (SW 1271, NCI-H23, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.834× | -3.3 | 0.072 | 10/48 (NCI-H2347, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2254. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 23.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 21.6 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.293× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 18.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.349× (z -8.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -12.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 20.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.03× (z +11.3) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 18.6 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.0668× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -18.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -13.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -9.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -13.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[OTS514 (drug)]] 0.05 µM 0.230× (z -8.6) ⚠ transcription drop |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -9.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.387× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -10.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 19.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.220× (z -9.2) |
| [[SNU-1 (line)]] | wt | 23.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 18.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.194× (z -10.9) |
| [[SW 900 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -10.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 36.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.387× (z -10.9) |
| [[A-172 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2254), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFAF7]] | +0.74 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[ALG9]] | +0.70 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[MED23]] | +0.69 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[SNX4]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[ASB7]] | +0.68 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[KLHDC10]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[CWC15]] | +0.66 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[CDK5RAP1]] | +0.66 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[SARNP]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[INPP5B]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[TERF1]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSUH2]] | -0.64 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[MYO1C]] | -0.61 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[CHD4]] | -0.61 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[OXTR]] | -0.58 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[DDX5]] | -0.58 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[ABR]] | -0.58 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[SKIL]] | -0.58 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[AGO2]] | -0.56 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[TUG1]] | -0.55 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[PHEX]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLSTN2]] | B | CLSTN2 activity raises CDADC1's level | lines that do not express CLSTN2 (30) vs lines expressing it (20) | 1.07× lower at baseline in the lines without CLSTN2 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, CCDC144NL-AS1, ENSG00000264660 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.643). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-3.0, -12.5); signed map (-32.5, -10.2). **Vector** length 86.4, 17.1% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.9 | +8.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +4.9 | +7.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +3.2 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +1.6 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +1.6 | +1.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.8 | -10.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -6.6 | -4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.0 | -4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.8 | -2.1 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | cytidine and dCMP deaminase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.2 — chr13:49,247,925-49,293,485 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NYD-SP15 |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWV3](https://www.uniprot.org/uniprotkb/Q9BWV3) (dCTP deaminase):

> Catalyzes the deamination of dCTP to dUTP, exhibiting a strong substrate preference for dCTP over CTP. No deaminase activity toward 5-methyl-dCTP, cytidine, or deoxycytidine. May play an important role in testicular development and spermatogenesis. In addition to its role on endogenous nucleotides, it deaminates the active triphosphate forms of the cytidine analog drugs, gemcitabine (dFdCTP) and decitabine (5-aza-dCTP), rendering them susceptible to inactivation by deoxyuridine triphosphatase …

**Summary**, from NCBI Gene [81602](https://www.ncbi.nlm.nih.gov/gene/81602):

> Enables several functions, including cytidine deaminase activity; importin-alpha family protein binding activity; and protein homodimerization activity. Involved in DNA cytosine deamination. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20299](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20299) · Entrez [81602](https://www.ncbi.nlm.nih.gov/gene/81602) · UniProt [Q9BWV3](https://www.uniprot.org/uniprotkb/Q9BWV3) · Ensembl [ENSG00000102543](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102543)

## Data

Gene col 2254: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2254); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2254, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2254]; `tensor/DDL_lfc|DDL_z.npy` [2254]; `embed/gene_vectors.npy` [2254]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2254 or target_col == 2254). Every well: [[CDADC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDADC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
