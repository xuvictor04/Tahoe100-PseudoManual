---
symbol: "CAD"
type: "gene"
col: 1414
ensembl_id: "ENSG00000084774"
name: "carbamoyl-phosphate synthetase 2, aspartate transcarbamylase, and dihydroorotase"
location: "2p23.3"
module: 18
arm: "+"
pooled_cpm: 20.59
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CAD

*carbamoyl-phosphate synthetase 2, aspartate transcarbamylase, and dihydroorotase* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 2.04× (z +11.4, q 2e-27, up in 41 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[c-Kit-IN-1 (drug)]] 5 µM: 1.79× (z +4.9, q 7e-05, up in 17 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.752× (z -6.5, q 4e-08, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PFAS]] (+0.80, fdr 7e-06), [[MDN1]] (+0.79, fdr 7e-06), [[QSOX2]] (+0.78, fdr 7e-06); moves opposite to [[SELENOK]] (-0.72, fdr 7e-06), [[ARID4B]] (-0.64, fdr 7e-06), [[RNF181]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TERT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1414.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.04×** | +11.4 | 2e-27 | 41/47 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +9.1 | 2e-17 | 21/32 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.76×** | +9.0 | 3e-17 | 29/41 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +7.6 | 5e-12 | 22/39 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.49×** | +6.4 | 2e-08 | 24/48 (NCI-H1792, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.30×** | +6.0 | 2e-07 | 23/48 (A-172, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +5.7 | 7e-07 | 2/48 (KATO III, HCT15) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.41×** | +5.4 | 4e-06 | 23/48 (NCI-H1792, SW 900, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.79×** | +4.9 | 7e-05 | 17/47 (NCI-H460, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +4.6 | 2e-04 | 16/47 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.31×** | +4.3 | 8e-04 | 20/47 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +4.3 | 8e-04 | 20/47 (NCI-H1792, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.30×** | +4.2 | 0.001 | 11/47 (KATO III, PANC-1, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +4.1 | 0.001 | 19/46 (NCI-H1792, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.54×** | +3.6 | 0.011 | 15/44 (Hs 766T, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.014 | 7/48 (NCI-H460, A498, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.51×** | +3.4 | 0.017 | 9/47 (AsPC-1, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.51×** | +3.4 | 0.017 | 12/48 (A498, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.020 | 13/46 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.039 | 8/48 (NCI-H460, A498, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.052 | 6/47 (NCI-H460, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1414.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.752×** | -6.5 | 4e-08 | 27/47 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.701×** | -5.7 | 3e-06 | 25/47 (RKO, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.734×** | -4.8 | 3e-04 | 22/48 (SNU-1, HEC-1-A, …) | top dose only | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.745×** | -4.8 | 3e-04 | 18/47 (SK-MEL-2, LS 180, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.580×** | -4.6 | 5e-04 | 20/46 (hTERT-HPNE, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.767×** | -4.1 | 0.005 | 19/48 (A498, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.782×** | -4.0 | 0.006 | 17/47 (Panc 03.27, PANC-1, …) | two highest doses | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.845× | -3.9 | 0.007 | 15/48 (KATO III, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.802×** | -3.4 | 0.036 | 17/47 (HT-29, MIA PaCa-2, …) | top dose only |  |
| [[Ciclopirox (drug)]] 5 µM |  | 0.869× | -3.2 | 0.067 | 8/48 (CHP-212, SHP-77, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.870× | -3.2 | 0.070 | 9/48 (SNU-1, A498, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1414. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 53.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -15.3) |
| [[HEC-1-A (line)]] | alt | 30.4 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.286× (z -11.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 2 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0994× (z -8.7) |
| [[SW48 (line)]] | wt | 43.3 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 16.9 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.164× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 32.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H23 (line)]] | alt | 43.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 18.4 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.10× (z +8.5) ⚠ unreliable plate only | — |
| [[RKO (line)]] | wt | 35.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.240× (z -9.5) |
| [[SNU-1 (line)]] | wt | 36.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0755× (z -12.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 31.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1414), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PFAS]] | +0.80 | +0.74 / +0.80 | both halves | 7e-06 | same gene group; pathway: Metabolism of nucleotides; STRING 650 |
| [[MDN1]] | +0.79 | +0.75 / +0.79 | both halves | 7e-06 |  |
| [[QSOX2]] | +0.78 | +0.70 / +0.80 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.76 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[BOP1]] | +0.75 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[TFDP1]] | +0.75 | +0.68 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[POFUT1]] | +0.75 | +0.62 / +0.78 | both halves | 7e-06 |  |
| [[LETM1]] | +0.74 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[ATIC]] | +0.74 | +0.72 / +0.74 | both halves | 7e-06 | pathway: Metabolism of nucleotides; STRING 658 |
| [[TUBGCP4]] | +0.74 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[URB2]] | +0.74 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[WDR4]] | +0.74 | +0.76 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOK]] | -0.72 | -0.65 / -0.70 | both halves | 7e-06 |  |
| [[ARID4B]] | -0.64 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[RNF181]] | -0.63 | -0.63 / -0.65 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises CAD's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.67× lower at baseline in the lines without TERT | 0.008 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[NCS1]] | B | NCS1 activity raises CAD's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.03× lower at baseline in the lines without NCS1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.790). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.9, -37.0); signed map (-4.6, -51.2). **Vector** length 107, 24.8% of its response variance represented; |z| ≥ 3 in 989 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.2 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +9.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~67% of this change | +5.0 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +4.8 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +7.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.2 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.8 | +4.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.3 | +3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.2 | +3.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.7 | +3.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -3.4 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -3.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | carbamoyl-phosphate synthetase 2, aspartate transcarbamylase, and dihydroorotase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:27,217,369-27,243,943 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GATD4 |
| Gene groups (HGNC) | Glutamine amidotransferase class 1 domain containing; ATP-grasp fold containing; Carbamoyl-phosphate synthetases |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 3 pathways, smallest: Pyrimidine biosynthesis; Nucleotide biosynthesis; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [P27708](https://www.uniprot.org/uniprotkb/P27708) (Multifunctional protein CAD):

> Multifunctional protein that encodes the first 3 enzymatic activities of the de novo pyrimidine pathway: carbamoylphosphate synthetase (CPSase; EC 6.3.5.5), aspartate transcarbamylase (ATCase; EC 2.1.3.2) and dihydroorotase (DHOase; EC 3.5.2.3). The CPSase-function is accomplished in 2 steps, by a glutamine-dependent amidotransferase activity (GATase) that binds and cleaves glutamine to produce ammonia, followed by an ammonium-dependent carbamoyl phosphate synthetase, which reacts with the …

**Summary**, from NCBI Gene [790](https://www.ncbi.nlm.nih.gov/gene/790):

> The de novo synthesis of pyrimidine nucleotides is required for mammalian cells to proliferate. This gene encodes a trifunctional protein which is associated with the enzymatic activities of the first 3 enzymes in the 6-step pathway of pyrimidine biosynthesis: carbamoylphosphate synthetase (CPS II), aspartate transcarbamoylase, and dihydroorotase. This protein is regulated by the mitogen-activated protein kinase (MAPK) cascade, which indicates a direct link between activation of the MAPK …

**Accessions** — [HGNC:1424](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1424) · Entrez [790](https://www.ncbi.nlm.nih.gov/gene/790) · UniProt [P27708](https://www.uniprot.org/uniprotkb/P27708) · Ensembl [ENSG00000084774](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084774)

## Data

Gene col 1414: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1414); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1414, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1414]; `tensor/DDL_lfc|DDL_z.npy` [1414]; `embed/gene_vectors.npy` [1414]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1414 or target_col == 1414). Every well: [[CAD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
