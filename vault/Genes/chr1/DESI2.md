---
symbol: "DESI2"
type: "gene"
col: 4283
ensembl_id: "ENSG00000121644"
name: "desumoylating isopeptidase 2"
location: "1q44"
module: 63
arm: "+"
pooled_cpm: 86.45
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# DESI2

*desumoylating isopeptidase 2* — 1q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.51× (z +7.2, q 4e-10, up in 42 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.47× (z +6.7, q 4e-09, up in 34 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW 900 0.255×, A-427 0.494×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.386×, SK-MEL-2 0.368×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.504×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.5 µM in 1 line (SW 1088 0.0719×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTHFD2]] (+0.66, fdr 7e-06), [[TUBE1]] (+0.60, fdr 7e-06), [[PCK2]] (+0.59, fdr 1e-05); moves opposite to [[GPATCH8]] (-0.57, fdr 9e-06), [[SURF6]] (-0.53, fdr 1e-05), [[CSTF2T]] (-0.51, fdr 1e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSAT1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4283.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +7.2 | 4e-10 | 42/48 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +6.7 | 4e-09 | 34/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +4.9 | 2e-04 | 35/48 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.7 | 3e-04 | 30/48 (SW48, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +4.6 | 6e-04 | 27/47 (COLO 205, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.20× | +4.4 | 8e-04 | 25/48 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +4.1 | 0.003 | 27/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.012 | 23/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.012 | 24/48 (HEC-1-A, SW48, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.014 | 23/47 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.16× | +3.6 | 0.014 | 16/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.014 | 26/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.015 | 20/48 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.059 | 16/49 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.059 | 16/48 (NCI-H2347, A-427, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4283.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW 900 0.255×, A-427 0.494×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.386×, SK-MEL-2 0.368×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.504×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.5 µM in 1 line (SW 1088 0.0719×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.725× | -3.6 | 0.12 | 22/48 (SNU-1, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.818× | -3.5 | 0.12 | 24/48 (A498, H4, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4283. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 57.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +8.5) | — |
| [[A-427 (line)]] | wt | 89.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 65.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 85.4 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.263× (z -8.8) ⚠ transcription drop |
| [[AsPC-1 (line)]] | alt | 83.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 58.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 121 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.155× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~43% of this change |
| [[LoVo (line)]] | wt | 98.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.386× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[PANC-1 (line)]] | alt | 121 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 74.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.368× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[SW 1088 (line)]] | alt | 70.0 | 0 | 1 | — | [[Adagrasib (drug)]] 0.5 µM 0.0719× (z -9.0) |
| [[SW 900 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 73.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 87.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 67.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 86.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 84.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 97.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 108 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 76.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 87.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 79.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4283), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTHFD2]] | +0.66 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[TUBE1]] | +0.60 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[PCK2]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[TXNDC12]] | +0.56 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[ASNS]] | +0.56 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[TCEA1]] | +0.55 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[SLC1A4]] | +0.55 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[PSAT1]] | +0.55 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[CCNG1]] | +0.55 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[STRADB]] | +0.54 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[XPOT]] | +0.54 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[AARS1]] | +0.54 | +0.54 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH8]] | -0.57 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[SURF6]] | -0.53 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[CSTF2T]] | -0.51 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[ABCF1]] | -0.49 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[RASAL2]] | -0.48 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[USP43]] | -0.48 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[CHMP1A]] | -0.48 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[COA3]] | -0.47 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[ZBTB4]] | -0.47 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[PRPF38B]] | -0.47 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[CENPB]] | -0.46 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[TOMM40L]] | -0.46 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSAT1]] | B | PSAT1 activity raises DESI2's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.24× lower at baseline in the lines without PSAT1 | 0.086 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.6, 47.8); signed map (-15.6, 24.7). **Vector** length 107, 28.5% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +6.8 | +4.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.9 | +3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.8 | +3.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.7 | +3.6 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.9 | +0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -4.9 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -1.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | desumoylating isopeptidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q44 — chr1:244,653,103-244,709,033 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-146, FLJ21998, PNAS-4, DESI-2; previously C1orf121, FAM152A, PPPDE1 |
| Gene groups (HGNC) | Desumoylating isopeptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSY9](https://www.uniprot.org/uniprotkb/Q9BSY9) (Deubiquitinase DESI2):

> Has deubiquitinating activity towards 'Lys-48'- and 'Lys-63'-linked polyubiquitin chains. Deubiquitinates 'Lys-48'-linked polyubiquitination of RPS7 leading to its stabilization. Exhibits palmitoyl protein thioesterase (S-depalmitoylation) activity towards synthetic substrates 4-methylumbelliferyl-6-S-palmitoyl-beta-D-glucopyranoside and S-depalmitoylation probe 5 (DPP-5).

**Summary**, from NCBI Gene [51029](https://www.ncbi.nlm.nih.gov/gene/51029):

> Enables deubiquitinase activity and long-chain fatty acyl-CoA hydrolase activity. Predicted to be involved in macromolecule depalmitoylation and proteolysis. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24264](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24264) · Entrez [51029](https://www.ncbi.nlm.nih.gov/gene/51029) · UniProt [Q9BSY9](https://www.uniprot.org/uniprotkb/Q9BSY9) · Ensembl [ENSG00000121644](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121644)

## Data

Gene col 4283: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4283); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4283, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4283]; `tensor/DDL_lfc|DDL_z.npy` [4283]; `embed/gene_vectors.npy` [4283]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4283 or target_col == 4283). Every well: [[DESI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DESI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
