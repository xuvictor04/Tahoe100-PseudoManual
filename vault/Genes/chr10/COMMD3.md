---
symbol: "COMMD3"
type: "gene"
col: 7284
ensembl_id: "ENSG00000148444"
name: "COMM domain containing 3"
location: "10p12.2"
module: 12
arm: "+"
pooled_cpm: 12.22
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# COMMD3

*COMM domain containing 3* — 10p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.01× (z +7.7, q 1e-11, up in 32 of 37 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.72× (z +6.2, q 2e-07, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.302× (z -6.3, q 2e-07, down in 31 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLK4]] (+0.69, fdr 7e-06), [[TCEANC]] (+0.68, fdr 7e-06), [[PPP4R2]] (+0.67, fdr 7e-06); moves opposite to [[BCAP31]] (-0.65, fdr 7e-06), [[ZNF731P]] (-0.64, fdr 7e-06), [[ATP2A2]] (-0.62, fdr 8e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7284.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +7.7 | 1e-11 | 32/37 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.72×** | +6.2 | 2e-07 | 27/46 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.71×** | +5.9 | 9e-07 | 26/46 (A-427, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.37×** | +5.1 | 4e-05 | 20/45 (A-172, HCT15, …) | all doses, flat | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +5.1 | 4e-05 | 9/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.54×** | +4.9 | 8e-05 | 23/41 (HOP62, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.53×** | +4.9 | 8e-05 | 20/35 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.52×** | +4.8 | 1e-04 | 24/47 (SW48, HEC-1-A, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.47×** | +4.4 | 8e-04 | 20/42 (A-172, PANC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.003 | 14/48 (A498, SNU-423, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.005 | 20/48 (A-172, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.38×** | +3.5 | 0.019 | 11/25 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7284.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.302×** | -6.3 | 2e-07 | 31/42 (LS 180, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.635×** | -5.2 | 6e-05 | 24/47 (SHP-77, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.657×** | -4.8 | 3e-04 | 24/47 (RPMI-7951, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.442×** | -4.3 | 0.002 | 23/46 (NCI-H1573, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.687×** | -4.3 | 0.002 | 19/47 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.692×** | -4.2 | 0.003 | 20/45 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.719×** | -3.7 | 0.014 | 18/47 (RKO, SW48, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.718×** | -3.6 | 0.027 | 17/44 (SW 900, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.763× | -3.1 | 0.13 | 12/46 (NCI-H2030, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.766× | -3.0 | 0.14 | 11/46 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7284. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 13.2 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0881× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.192× (z -11.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -11.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SK-MEL-2 (line)]] | alt | 9.33 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.122× (z -9.8) |
| [[SNU-423 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -10.1) ⚠ cell-cycle shift, explains ~15% of this change |
| [[A-172 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7284), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLK4]] | +0.69 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[TCEANC]] | +0.68 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[PPP4R2]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[SEPSECS]] | +0.66 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[TMEM42]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[MED18]] | +0.64 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[TRMT10B]] | +0.63 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[SNHG11]] | +0.63 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[MRPS31]] | +0.63 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[PIM3]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[RAB30]] | +0.62 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[GORAB]] | +0.62 | +0.62 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAP31]] | -0.65 | -0.67 / -0.65 | both halves | 7e-06 |  |
| [[ZNF731P]] | -0.64 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[ATP2A2]] | -0.62 | -0.57 / -0.64 | both halves | 8e-06 |  |
| [[AHSA1]] | -0.62 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[RNPS1]] | -0.61 | -0.64 / -0.58 | both halves | 8e-06 |  |
| [[ELAVL1]] | -0.61 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[SNRPA]] | -0.60 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[LARP4B]] | -0.60 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[TOMM40]] | -0.60 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[KCNIP2]] | -0.59 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[CHID1]] | -0.59 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[SMG1P6]] | -0.59 | -0.42 / -0.67 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises COMMD3's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-31.2, 3.7); signed map (6.4, -20.8). **Vector** length 70.8, 14.3% of its response variance represented; |z| ≥ 3 in 669 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +6.0 | +5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.3 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.7 | +4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +4.2 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.7 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.4 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.7 | -4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -6.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.3 | -1.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.3 | -3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | COMM domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.2 — chr10:22,316,386-22,320,306 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BUP; previously C10orf8 |
| Gene groups (HGNC) | COMM domain containing; CCC complex |
| Reactome | 3 pathways, smallest: Neddylation; Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBI1](https://www.uniprot.org/uniprotkb/Q9UBI1) (COMM domain-containing protein 3):

> Scaffold protein in the commander complex that is essential for endosomal recycling of transmembrane cargos; the commander complex is composed of the CCC subcomplex and the retriever subcomplex. May modulate activity of cullin-RING E3 ubiquitin ligase (CRL) complexes. May down-regulate activation of NF-kappa-B. Modulates Na(+) transport in epithelial cells by regulation of apical cell surface expression of amiloride-sensitive sodium channel (ENaC) subunits.

**Summary**, from NCBI Gene [23412](https://www.ncbi.nlm.nih.gov/gene/23412):

> Predicted to be involved in endocytic recycling. Predicted to act upstream of or within intracellular copper ion homeostasis. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23332](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23332) · Entrez [23412](https://www.ncbi.nlm.nih.gov/gene/23412) · UniProt [Q9UBI1](https://www.uniprot.org/uniprotkb/Q9UBI1) · Ensembl [ENSG00000148444](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148444)

## Data

Gene col 7284: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7284); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7284, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7284]; `tensor/DDL_lfc|DDL_z.npy` [7284]; `embed/gene_vectors.npy` [7284]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7284 or target_col == 7284). Every well: [[COMMD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COMMD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
