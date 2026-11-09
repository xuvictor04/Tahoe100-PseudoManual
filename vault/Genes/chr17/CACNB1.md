---
symbol: "CACNB1"
type: "gene"
col: 855
ensembl_id: "ENSG00000067191"
name: "calcium voltage-gated channel auxiliary subunit beta 1"
location: "17q12"
module: 2
arm: "+"
pooled_cpm: 6.78
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CACNB1

*calcium voltage-gated channel auxiliary subunit beta 1* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.71× (z +5.6, q 1e-05, up in 4 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cepharanthine (drug)]] 5 µM: 1.27× (z +3.7, q 0.045, up in 15 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.584× (z -5.9, q 3e-06, down in 23 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.613× (z -5.1, q 8e-05, down in 19 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL17]] (+0.58, fdr 1e-05), [[ZDHHC8]] (+0.57, fdr 2e-05), [[RTN4R]] (+0.57, fdr 3e-05); moves opposite to [[NIPBL]] (-0.55, fdr 3e-05), [[ITFG1]] (-0.51, fdr 2e-05), [[ASH1L]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 855.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +5.6 | 1e-05 | 4/14 (NCI-H2030, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.045 | 15/46 (NCI-H2030, COLO 205, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.045 | 9/46 (BT-474, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.045 | 7/41 (BT-474, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.5 | 0.045 | 1/47 (C32) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.38×** | +3.4 | 0.071 | 9/43 (A498, HOP62, …) | rises with dose |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | 1.34× | +3.1 | 0.16 | 5/43 (hTERT-HPNE, SNU-423, …) | top dose only | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 1.32× | +3.1 | 0.16 | 5/40 (RPMI-7951, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 855.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.584×** | -5.9 | 3e-06 | 23/40 (C32, RKO, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.613×** | -5.1 | 8e-05 | 19/41 (A-172, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.642×** | -4.6 | 7e-04 | 21/39 (HS-578T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.672×** | -4.3 | 0.002 | 17/45 (CFPAC-1, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.685×** | -4.1 | 0.004 | 12/45 (BT-474, CFPAC-1, …) | two highest doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.695×** | -4.0 | 0.007 | 18/41 (NCI-H2030, RKO, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.726×** | -3.5 | 0.039 | 17/45 (LoVo, A-427, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.739×** | -3.3 | 0.068 | 17/44 (SNU-1, HCT15, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.745×** | -3.2 | 0.083 | 11/26 (SW1417, A549, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.749×** | -3.1 | 0.089 | 14/46 (BT-474, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Arbutin (drug)]] 5 µM |  | **0.741×** | -3.1 | 0.089 | 7/43 (A-427, A498, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.822× | -3.0 | 0.12 | 16/42 (A-427, CFPAC-1, …) | two highest doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 855. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -8.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 14.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 25.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.131× (z -10.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 7.32 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0766× (z -8.5) ⚠ cell-cycle shift, explains ~23% of this change |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 7.68 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.129× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 6.89 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -12.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H2030 (line)]] | alt | 9.39 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0338× (z -17.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 7.07 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0678× (z -11.3) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 4.01 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.132× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 6.55 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0745× (z -8.9) |
| [[A498 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 855), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL17]] | +0.58 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ZDHHC8]] | +0.57 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[RTN4R]] | +0.57 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[USP35]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PLD2]] | +0.56 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[EEF1A2]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[NBEAL2]] | +0.55 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[ST6GALNAC6]] | +0.55 | +0.60 / +0.39 | both halves | 6e-05 |  |
| [[PPP1R12C]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ITPR3]] | +0.54 | +0.57 / +0.44 | both halves | 3e-05 | pathway: Cardiac conduction |
| [[PLCB3]] | +0.54 | +0.57 / +0.46 | both halves | 3e-05 | pathway: Neuronal System |
| [[FCHSD1]] | +0.54 | +0.46 / +0.55 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIPBL]] | -0.55 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[ITFG1]] | -0.51 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[ASH1L]] | -0.51 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[MAP2K5]] | -0.51 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[ELP4]] | -0.51 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[SON]] | -0.50 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[MED13]] | -0.50 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[ATXN7L1]] | -0.47 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[RFX3]] | -0.47 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[XRN1]] | -0.46 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[GIGYF2]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[CEP350]] | -0.46 | -0.37 / -0.47 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CACNB1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[KIF3C]] | B | KIF3C activity raises CACNB1's level | lines that do not express KIF3C (5) vs lines expressing it (45) | 1.73× lower at baseline in the lines without KIF3C | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC00888, WNT3, TBKBP1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.582). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (1.7, -1.2); signed map (-44.1, -9.3). **Vector** length 60.4, 8.59% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +2.8 | +2.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.7 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.4 | -0.2 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.7 | -5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.2 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.5 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.3 | -0.5 |
|  | [[Thymol (drug)]] 5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | calcium voltage-gated channel auxiliary subunit beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:39,173,453-39,197,702 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CACNLB1 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; Calcium voltage-gated channel auxiliary beta subunits; SH3 domain containing |
| Reactome | 14 pathways, smallest: Phase 2 - plateau phase; Presynaptic depolarization and calcium channel opening; Mechanical load activates signaling by PIEZO1 and integrins in osteocytes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02641](https://www.uniprot.org/uniprotkb/Q02641) (Voltage-dependent L-type calcium channel subunit beta-1):

> Regulatory subunit of L-type calcium channels. Regulates the activity of L-type calcium channels that contain CACNA1A as pore-forming subunit (By similarity). Regulates the activity of L-type calcium channels that contain CACNA1C as pore-forming subunit and increases the presence of the channel complex at the cell membrane. Required for functional expression L-type calcium channels that contain CACNA1D as pore-forming subunit. Regulates the activity of L-type calcium channels that contain …

**Summary**, from NCBI Gene [782](https://www.ncbi.nlm.nih.gov/gene/782):

> The protein encoded by this gene belongs to the calcium channel beta subunit family. It plays an important role in the calcium channel by modulating G protein inhibition, increasing peak calcium current, controlling the alpha-1 subunit membrane targeting and shifting the voltage dependence of activation and inactivation. Alternative splicing occurs at this locus and three transcript variants encoding three distinct isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1401](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1401) · Entrez [782](https://www.ncbi.nlm.nih.gov/gene/782) · UniProt [Q02641](https://www.uniprot.org/uniprotkb/Q02641) · Ensembl [ENSG00000067191](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067191)

## Data

Gene col 855: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 855); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 855, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 855]; `tensor/DDL_lfc|DDL_z.npy` [855]; `embed/gene_vectors.npy` [855]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 855 or target_col == 855). Every well: [[CACNB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACNB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
