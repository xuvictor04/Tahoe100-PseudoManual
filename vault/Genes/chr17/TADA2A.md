---
symbol: "TADA2A"
type: "gene"
col: 15870
ensembl_id: "ENSG00000276234"
name: "transcriptional adaptor 2A"
location: "17q12"
module: 1
arm: "+"
pooled_cpm: 26.56
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TADA2A

*transcriptional adaptor 2A* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 1.34× (z +5.5, q 2e-05, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.527× (z -12.0, q 3e-30, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCAF17]] (+0.68, fdr 7e-06), [[RNASEH2B]] (+0.67, fdr 7e-06), [[ZNF236]] (+0.63, fdr 1e-05); moves opposite to [[WDR26]] (-0.60, fdr 7e-06), [[KCNQ1OT1]] (-0.58, fdr 1e-05), [[CRELD1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RAD51D]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15870.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +5.5 | 2e-05 | 24/48 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +5.3 | 3e-05 | 1/48 (NCI-H2030) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +4.7 | 5e-04 | 21/47 (HT-29, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.008 | 13/47 (PANC-1, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.13× | +3.3 | 0.093 | 6/48 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.20× | +3.3 | 0.095 | 12/47 (SW480, RKO, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.11 | 6/47 (BT-474, NCI-H2030, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.0 | 0.17 | 6/48 (LoVo, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15870.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.527×** | -12.0 | 3e-30 | 37/47 (SK-MEL-2, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.741×** | -7.9 | 8e-13 | 26/47 (NCI-H460, A498, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.678×** | -7.3 | 8e-11 | 30/48 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.693×** | -6.8 | 9e-10 | 25/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.683×** | -6.8 | 9e-10 | 26/47 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.777×** | -6.7 | 2e-09 | 26/47 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.705×** | -6.5 | 5e-09 | 29/47 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.709×** | -6.4 | 9e-09 | 28/46 (BT-474, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.734×** | -5.8 | 5e-07 | 24/48 (NCI-H2030, J82, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.811×** | -5.5 | 2e-06 | 23/48 (NCI-H1573, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.786×** | -4.5 | 4e-04 | 23/47 (SNU-1, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.817×** | -3.8 | 0.008 | 15/48 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.823×** | -3.6 | 0.012 | 20/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.824×** | -3.6 | 0.013 | 17/47 (HEC-1-A, HS-578T, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.829×** | -3.5 | 0.017 | 16/47 (HOP62, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.845× | -3.1 | 0.055 | 9/47 (PANC-1, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15870. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 56.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -11.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.443× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 28.3 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -14.8) ⚠ cell-cycle shift, explains ~34% of this change |
| [[BT-474 (line)]] | alt | 129 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.317× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 46.1 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.320× (z -12.0) |
| [[HOP62 (line)]] | alt | 27.1 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.243× (z -12.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 39.6 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.180× (z -14.0) |
| [[J82 (line)]] | alt | 29.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.249× (z -11.6) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 30.3 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.112× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 22.4 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0889× (z -11.1) ⚠ cell-cycle shift, explains ~97% of this change |
| [[SW480 (line)]] | alt | 24.3 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.358× (z -10.1) |
| [[A-427 (line)]] | wt | 46.1 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.533× (z -8.8) |
| [[A498 (line)]] | wt | 22.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -13.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[AsPC-1 (line)]] | alt | 9.81 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.159× (z -9.4) ⚠ transcription drop |
| [[C-33 A (line)]] | alt | 41.1 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.296× (z -8.8) |
| [[HS-578T (line)]] | alt | 22.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -8.5) |
| [[LoVo (line)]] | wt | 20.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.364× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 36.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -8.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[RKO (line)]] | wt | 21.3 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.107× (z -13.5) |
| [[A-172 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15870), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCAF17]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[RNASEH2B]] | +0.67 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[ZNF236]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[ANAPC7]] | +0.63 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[NSMCE4A]] | +0.63 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[ZNF239]] | +0.62 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[TXNRD3]] | +0.62 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[RIOX2]] | +0.62 | +0.67 / +0.54 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[TMEM209]] | +0.62 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[PPIL1]] | +0.61 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[CSE1L]] | +0.61 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[DHX30]] | +0.61 | +0.49 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR26]] | -0.60 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[KCNQ1OT1]] | -0.58 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[CRELD1]] | -0.57 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[RASA4B]] | -0.56 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[ASMTL]] | -0.56 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[PPARA]] | -0.56 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[MXD1]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[GP6]] | -0.54 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[BNIP3L]] | -0.53 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[HLA-F-AS1]] | -0.53 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[QSOX1]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[POFUT2]] | -0.52 | -0.48 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAD51D]] | C | RAD51D's natural level strengthens TADA2A's drug response | RAD51D's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.29; direction not clear | 0.070 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.609). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-22.6, -38.2); signed map (-3.6, -39.7). **Vector** length 84.8, 16.8% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.6 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.3 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +4.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +1.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +3.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.2 | -12.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.3 | -6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -6.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.8 | -2.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.7 | -5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | transcriptional adaptor 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:37,406,886-37,479,725 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ADA2, hADA2, ADA2A; previously TADA2L |
| Gene groups (HGNC) | Zinc fingers ZZ-type; Myb/SANT domain containing; ATAC complex |
| Reactome | 6 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; HATs acetylate histones; Epigenetic regulation by WDR5-containing histone modifying complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [O75478](https://www.uniprot.org/uniprotkb/O75478) (Transcriptional adapter 2-alpha):

> Component of the ATAC complex, a complex with histone acetyltransferase activity on histones H3 and H4. Required for the function of some acidic activation domains, which activate transcription from a distant site (By similarity). Binds double-stranded DNA. Binds dinucleosomes, probably at the linker region between neighboring nucleosomes. Plays a role in chromatin remodeling. May promote TP53/p53 'Lys-321' acetylation, leading to reduced TP53 stability and transcriptional activity. May also …

**Summary**, from NCBI Gene [6871](https://www.ncbi.nlm.nih.gov/gene/6871):

> Many DNA-binding transcriptional activator proteins enhance the initiation rate of RNA polymerase II-mediated gene transcription by interacting functionally with the general transcription machinery bound at the basal promoter. Adaptor proteins are usually required for this activation, possibly to acetylate and destabilize nucleosomes, thereby relieving chromatin constraints at the promoter. The protein encoded by this gene is a transcriptional activator adaptor and has been found to be part of …

**Accessions** — [HGNC:11531](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11531) · Entrez [6871](https://www.ncbi.nlm.nih.gov/gene/6871) · UniProt [O75478](https://www.uniprot.org/uniprotkb/O75478) · Ensembl [ENSG00000276234](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000276234)

## Data

Gene col 15870: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15870); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15870, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15870]; `tensor/DDL_lfc|DDL_z.npy` [15870]; `embed/gene_vectors.npy` [15870]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15870 or target_col == 15870). Every well: [[TADA2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TADA2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
