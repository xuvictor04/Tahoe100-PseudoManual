---
symbol: "NTMT1"
type: "gene"
col: 7266
ensembl_id: "ENSG00000148335"
name: "N-terminal Xaa-Pro-Lys N-methyltransferase 1"
location: "9q34.11"
module: 162
arm: "+"
pooled_cpm: 16.84
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# NTMT1

*N-terminal Xaa-Pro-Lys N-methyltransferase 1* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.24× (z +11.5, q 5e-28, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Anethole trithione (drug)]] 5 µM: 0.800× (z -4.5, q 0.004, down in 16 of 48 measured lines) ⚠ cell-cycle shift, explains ~22% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (COLO 205 0.180×, LoVo 0.193×, SHP-77 0.183×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-1 0.101×, A-427 0.188×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.150×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP2]] (+0.66, fdr 7e-06), [[TRIM15]] (+0.64, fdr 1e-05), [[MIDN]] (+0.61, fdr 1e-05); moves opposite to [[CSDE1]] (-0.61, fdr 3e-05), [[STRADB]] (-0.55, fdr 1e-05), [[AP2B1]] (-0.54, fdr 3e-05).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7266.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.24×** | +11.5 | 5e-28 | 43/47 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.08×** | +10.0 | 3e-21 | 36/47 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.93×** | +9.4 | 1e-18 | 36/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.87×** | +8.9 | 5e-17 | 38/48 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.65×** | +7.2 | 8e-11 | 30/47 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +7.0 | 3e-10 | 29/46 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.40×** | +6.8 | 9e-10 | 27/46 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +5.0 | 4e-05 | 21/47 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.36×** | +4.4 | 6e-04 | 20/46 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.34×** | +4.1 | 0.002 | 17/42 (C32, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.003 | 16/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.31×** | +3.8 | 0.007 | 17/47 (NCI-H460, A549, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7266.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (COLO 205 0.180×, LoVo 0.193×, SHP-77 0.183×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-1 0.101×, A-427 0.188×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.150×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.800×** | -4.5 | 0.004 | 16/48 (COLO 205, SW 1088, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.795×** | -3.6 | 0.099 | 13/48 (SW480, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | 0.790× | -3.4 | 0.15 | 13/47 (SNU-1, J82, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.800× | -3.1 | 0.31 | 12/47 (LoVo, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7266. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 61.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 25.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 21.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 11.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +11.8) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[SHP-77 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 31.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 15.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +8.6) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[A-172 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7266), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP2]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[TRIM15]] | +0.64 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[MIDN]] | +0.61 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ASTL]] | +0.60 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[SHH]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[LINC00659]] | +0.59 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[MAP3K14]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[EPOP]] | +0.58 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[SPATA2L]] | +0.56 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[EGR2]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ABHD11]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[EGR3]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSDE1]] | -0.61 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[STRADB]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[AP2B1]] | -0.54 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[GHITM]] | -0.54 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[ARPP19]] | -0.54 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[ADD1]] | -0.53 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[NCKAP1]] | -0.52 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[GNAS]] | -0.52 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[DNAJC13]] | -0.51 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[CIZ1]] | -0.51 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[ATL3]] | -0.51 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[KATNAL1]] | -0.50 | -0.57 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers NTMT1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers NTMT1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.677). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.5, 46.7); signed map (7.5, 31.2). **Vector** length 82.1, 16.0% of its response variance represented; |z| ≥ 3 in 871 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.2 | +10.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +3.8 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +0.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -2.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -2.7 | -3.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.3 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | N-terminal Xaa-Pro-Lys N-methyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:129,608,884-129,636,135 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AD-003, HOMT1A, NRMT1, NRMT; previously C9orf32, METTL11A |
| Gene groups (HGNC) | 7BS protein methyltransferases; N- and C-terminal methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BV86](https://www.uniprot.org/uniprotkb/Q9BV86) (N-terminal Xaa-Pro-Lys N-methyltransferase 1):

> Distributive alpha-N-methyltransferase that methylates the N-terminus of target proteins containing the N-terminal motif [Ala/Gly/Pro/Ser]-Pro-Lys when the initiator Met is cleaved. Specifically catalyzes mono-, di- or tri-methylation of the exposed alpha-amino group of the Ala, Gly or Ser residue in the [Ala/Gly/Ser]-Pro-Lys motif and mono- or di-methylation of Pro in the Pro-Pro-Lys motif. Some of the substrates may be primed by NTMT2-mediated monomethylation. Catalyzes the trimethylation of …

**Summary**, from NCBI Gene [28989](https://www.ncbi.nlm.nih.gov/gene/28989):

> The METTL11A gene encodes an N-terminal methyltransferase for the RAN (MIM 601179) guanine nucleotide exchange factor regulator of chromosome condensation 1 (RCC1; MIM 179710). METTL11A enzyme alpha-N-methylates other protein targets such as SET (MIM 600960) and RB (MIM 180200).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:23373](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23373) · Entrez [28989](https://www.ncbi.nlm.nih.gov/gene/28989) · UniProt [Q9BV86](https://www.uniprot.org/uniprotkb/Q9BV86) · Ensembl [ENSG00000148335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148335)

## Data

Gene col 7266: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7266); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7266, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7266]; `tensor/DDL_lfc|DDL_z.npy` [7266]; `embed/gene_vectors.npy` [7266]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7266 or target_col == 7266). Every well: [[NTMT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NTMT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
