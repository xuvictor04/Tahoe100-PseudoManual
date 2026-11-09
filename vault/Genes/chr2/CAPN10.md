---
symbol: "CAPN10"
type: "gene"
col: 6617
ensembl_id: "ENSG00000142330"
name: "calpain 10"
location: "2q37.3"
module: 2
arm: "+"
pooled_cpm: 13.4
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CAPN10

*calpain 10* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.39× (z +12.4, q 2e-32, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.720× (z -4.7, q 0.001, down in 15 of 34 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HEC-1-A 0.128×, SW1417 0.325×; ⚠ toxic; transcription drop); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0834×); [[Simotinib (drug)]] 5 µM in 1 line (SNU-423 0.114×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADCK5]] (+0.69, fdr 1e-05), [[ZFYVE21]] (+0.68, fdr 7e-06), [[ZDHHC8]] (+0.67, fdr 7e-06); moves opposite to [[ZNF644]] (-0.63, fdr 1e-05), [[ATF7IP]] (-0.61, fdr 1e-05), [[SMARCA5]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CXCL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6617.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.39×** | +12.4 | 2e-32 | 41/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +10.2 | 4e-22 | 29/44 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +9.6 | 2e-19 | 39/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.88×** | +8.9 | 7e-17 | 40/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +6.7 | 3e-09 | 23/45 (SW480, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.022 | 10/48 (LoVo, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.062 | 13/47 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.27×** | +3.2 | 0.084 | 10/38 (SW480, NCI-H2347, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.084 | 12/43 (Panc 03.27, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6617.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HEC-1-A 0.128×, SW1417 0.325×; ⚠ toxic; transcription drop); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0834×); [[Simotinib (drug)]] 5 µM in 1 line (SNU-423 0.114×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.720×** | -4.7 | 0.001 | 15/34 (HEC-1-A, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.773× | -3.6 | 0.11 | 16/46 (A498, A549, …) | rises with dose | composition shift; position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 0.800× | -3.1 | 0.37 | 14/44 (CFPAC-1, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6617. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.95× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 28.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +13.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HEC-1-A (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -14.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 16.7 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0834× (z -10.7) |
| [[HS-578T (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H460 (line)]] | wt | 9.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 8.16 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.114× (z -10.1) ⚠ toxic |
| [[SW 900 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[SW1417 (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6617), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADCK5]] | +0.69 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[ZFYVE21]] | +0.68 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ZDHHC8]] | +0.67 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[SBF1]] | +0.65 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[PLCB3]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[CORO7]] | +0.64 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[TPD52L2]] | +0.64 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[ABHD17A]] | +0.63 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[AXIN1]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[GIT1]] | +0.62 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[CCT6P3-1]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[SMG1P5]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF644]] | -0.63 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[ATF7IP]] | -0.61 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[SMARCA5]] | -0.60 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[ZMYM4]] | -0.59 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[ARHGAP24]] | -0.59 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[ZC3H11A]] | -0.58 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[DZIP3]] | -0.58 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[ATRX]] | -0.58 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[AGL]] | -0.55 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[SYNE1]] | -0.55 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[ZNF280D]] | -0.55 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[SENP1]] | -0.55 | -0.54 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL2]] | B | CXCL2 activity raises CAPN10's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 1.18× lower at baseline in the lines without CXCL2 | 0.074 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[HDAC6]] | B | HDAC6 activity lowers CAPN10's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ATP10D]] | B | ATP10D activity lowers CAPN10's level | lines that do not express ATP10D (5) vs lines expressing it (45) | 1.81× higher at baseline in the lines without ATP10D | 0.086 | ⚠ within organs, on part of the lines; also absent: DUBR, CLEC2D, VPS35L |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.711). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-6.4, -21.3); signed map (-42.7, -2.0). **Vector** length 66.7, 10.5% of its response variance represented; |z| ≥ 3 in 892 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +10.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +2.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.5 | +1.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.5 | +12.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.2 | +8.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.8 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.6 | +2.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -4.5 | -3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.8 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.7 | -0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Thymol (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | calpain 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:240,586,734-240,617,705 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Calpains |
| Reactome | 2 pathways, smallest: Degradation of the extracellular matrix; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HC96](https://www.uniprot.org/uniprotkb/Q9HC96) (Calpain-10):

> Calcium-regulated non-lysosomal thiol-protease which catalyzes limited proteolysis of substrates involved in cytoskeletal remodeling and signal transduction. May play a role in insulin-stimulated glucose uptake.

**Summary**, from NCBI Gene [11132](https://www.ncbi.nlm.nih.gov/gene/11132):

> Calpains represent a ubiquitous, well-conserved family of calcium-dependent cysteine proteases. The calpain proteins are heterodimers consisting of an invariant small subunit and variable large subunits. The large catalytic subunit has four domains: domain I, the N-terminal regulatory domain that is processed upon calpain activation; domain II, the protease domain; domain III, a linker domain of unknown function; and domain IV, the calmodulin-like calcium-binding domain. This gene encodes a …

**Accessions** — [HGNC:1477](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1477) · Entrez [11132](https://www.ncbi.nlm.nih.gov/gene/11132) · UniProt [Q9HC96](https://www.uniprot.org/uniprotkb/Q9HC96) · Ensembl [ENSG00000142330](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142330)

## Data

Gene col 6617: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6617); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6617, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6617]; `tensor/DDL_lfc|DDL_z.npy` [6617]; `embed/gene_vectors.npy` [6617]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6617 or target_col == 6617). Every well: [[CAPN10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPN10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
