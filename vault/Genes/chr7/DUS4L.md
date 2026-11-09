---
symbol: "DUS4L"
type: "gene"
col: 2679
ensembl_id: "ENSG00000105865"
name: "dihydrouridine synthase 4 like"
location: "7q22.3"
module: 135
arm: "+"
pooled_cpm: 13.84
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# DUS4L

*dihydrouridine synthase 4 like* — 7q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.54× (z +10.6, q 2e-23, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.446× (z -7.4, q 1e-10, down in 25 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRMT13]] (+0.71, fdr 7e-06), [[C17orf75]] (+0.66, fdr 1e-05), [[ARL14EP]] (+0.66, fdr 1e-05); moves opposite to [[SLC66A2]] (-0.63, fdr 1e-05), [[GNB2]] (-0.61, fdr 6e-05), [[PEDS1]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NNT-AS1]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2679.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +10.6 | 2e-23 | 30/48 (CFPAC-1, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +7.8 | 2e-12 | 17/25 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +7.1 | 2e-10 | 24/45 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +7.1 | 2e-10 | 20/35 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +6.5 | 1e-08 | 22/47 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +6.4 | 2e-08 | 21/47 (NCI-H23, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.2 | 6e-08 | 20/45 (NCI-H1792, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +5.3 | 8e-06 | 17/48 (A498, A-172, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.32×** | +4.9 | 7e-05 | 19/47 (RKO, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +4.7 | 1e-04 | 9/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.1 | 0.002 | 14/46 (A-172, HS-578T, …) | all doses, flat | composition shift |
| [[Belzutifan (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.017 | 6/42 (RPMI-7951, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.030 | 8/47 (KATO III, BT-474, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.082 | 2/48 (LS 180, PANC-1) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.088 | 6/43 (A-427, SW48, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2679.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.446×** | -7.4 | 1e-10 | 25/43 (MIA PaCa-2, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.740×** | -5.3 | 4e-05 | 19/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.571×** | -5.1 | 5e-05 | 17/48 (SW480, SW1417, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.747×** | -5.1 | 5e-05 | 14/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.605×** | -4.6 | 4e-04 | 14/43 (PANC-1, A549, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.770×** | -4.6 | 4e-04 | 16/47 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.785×** | -4.2 | 0.002 | 16/46 (Hs 766T, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.868× | -3.5 | 0.030 | 13/48 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.820×** | -3.5 | 0.031 | 13/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 0.838× | -3.1 | 0.10 | 10/45 (C-33 A, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | 0.839× | -3.1 | 0.10 | 18/46 (NCI-H460, PANC-1, …) | two highest doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.833× | -3.0 | 0.11 | 15/47 (SW48, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2679. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 8.91 | 0 | 2 | — | [[Trimetrexate (drug)]] 0.05 µM 0.0858× (z -10.6) |
| [[A-172 (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 13.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 13.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[PANC-1 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.309× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[SK-MEL-2 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.217× (z -9.5) ⚠ cell-cycle shift, explains ~9% of this change |
| [[SW48 (line)]] | wt | 11.9 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0886× (z -8.6) |
| [[A-427 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2679), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT13]] | +0.71 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[C17orf75]] | +0.66 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[ARL14EP]] | +0.66 | +0.75 / +0.50 | both halves | 1e-05 |  |
| [[TRMT5]] | +0.66 | +0.72 / +0.48 | both halves | 2e-05 | STRING 545 |
| [[RIMOC1]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[KICS2]] | +0.66 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[MTHFSD]] | +0.65 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[ZXDA]] | +0.64 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[ZNF507]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[SBF2-AS1]] | +0.63 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ZNF621]] | +0.63 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[RWDD2B]] | +0.62 | +0.66 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC66A2]] | -0.63 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[GNB2]] | -0.61 | -0.62 / -0.38 | both halves | 6e-05 |  |
| [[PEDS1]] | -0.60 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[ABCA7]] | -0.58 | -0.38 / -0.60 | both halves | 7e-05 |  |
| [[DNM2]] | -0.57 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[COX6A1]] | -0.56 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[CALR]] | -0.56 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[ADIPOR1]] | -0.55 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[SDF2L1]] | -0.55 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[ABHD12]] | -0.55 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[CSNK1G2]] | -0.55 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[CD81]] | -0.55 | -0.60 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NNT-AS1]] | B | NNT-AS1 activity lowers DUS4L's level | lines that do not express NNT-AS1 (6) vs lines expressing it (44) | 1.46× higher at baseline in the lines without NNT-AS1 | 0.057 | ⚠ within organs, on part of the lines; co-absent genes |
| [[HDAC6]] | B | HDAC6 activity raises DUS4L's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | DUS4L's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | DUS4L's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.57 | 0.500 over the table, 0.085 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **+** arm (projection on the module's main direction 0.587). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-18.6, 7.2); signed map (9.6, -29.5). **Vector** length 74.9, 12.7% of its response variance represented; |z| ≥ 3 in 892 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.5 | +10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +7.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +6.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.4 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +5.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +2.7 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -2.8 | -3.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.5 | -5.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -7.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | dihydrouridine synthase 4 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.3 — chr7:107,563,484-107,578,523 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PP35, DUS4 |
| Gene groups (HGNC) | Dihydrouridine synthase family |
| Matched by | ensembl_id |

**Function**, from UniProt [O95620](https://www.uniprot.org/uniprotkb/O95620) (tRNA-dihydrouridine(20a/20b) synthase):

> Catalyzes the synthesis of dihydrouridine, a modified base found in the D-loop of most tRNAs.

**Summary**, from NCBI Gene [11062](https://www.ncbi.nlm.nih.gov/gene/11062):

> Predicted to enable tRNA dihydrouridine synthase activity. Involved in tRNA dihydrouridine synthesis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21517](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21517) · Entrez [11062](https://www.ncbi.nlm.nih.gov/gene/11062) · UniProt [O95620](https://www.uniprot.org/uniprotkb/O95620) · Ensembl [ENSG00000105865](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105865)

## Data

Gene col 2679: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2679); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2679, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2679]; `tensor/DDL_lfc|DDL_z.npy` [2679]; `embed/gene_vectors.npy` [2679]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2679 or target_col == 2679). Every well: [[DUS4L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUS4L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
