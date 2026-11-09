---
symbol: "MAP3K2-DT"
type: "gene"
col: 14090
ensembl_id: "ENSG00000236682"
name: "MAP3K2 divergent transcript"
location: "2q14.3"
module: 35
arm: "+"
pooled_cpm: 3.22
n_lines_expressing: 48
n_dd_up: 22
n_dd_down: 5
n_dd_up_clean: 17
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# MAP3K2-DT

*MAP3K2 divergent transcript* — 2q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.61× (z +12.1, q 1e-30, up in 25 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.622× (z -4.2, q 0.013, down in 13 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPK8IP2]] (+0.68, fdr 9e-06), [[LINC00240]] (+0.68, fdr 7e-06), [[ZFHX2]] (+0.68, fdr 1e-05); moves opposite to [[TREX2]] (-0.61, fdr 1e-05), [[ERI3]] (-0.61, fdr 4e-05), [[BCAP31]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ID2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14090.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.61×** | +12.1 | 1e-30 | 25/31 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.32×** | +10.6 | 1e-23 | 25/31 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.98×** | +9.7 | 6e-20 | 10/16 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.59×** | +8.1 | 6e-14 | 4/5 (HOP62, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +7.6 | 4e-12 | 24/42 (NCI-H460, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.44×** | +7.3 | 2e-11 | 5/6 (A498, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.63×** | +6.2 | 6e-08 | 12/43 (NCI-H2030, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.91×** | +5.7 | 6e-07 | 18/34 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.95×** | +5.7 | 6e-07 | 17/38 (KATO III, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +5.6 | 1e-06 | 13/27 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.67×** | +4.6 | 3e-04 | 10/28 (RPMI-7951, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +3.8 | 0.007 | 8/17 (NCI-H1573, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.010 | 9/40 (NCI-H460, A-172, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.74×** | +3.5 | 0.019 | 3/17 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.73×** | +3.5 | 0.020 | 6/26 (J82, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.022 | 6/42 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.028 | 7/41 (KATO III, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +3.3 | 0.028 | 10/43 (NCI-H1573, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.033 | 6/40 (NCI-H2030, HOP62, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14090.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.622×** | -4.2 | 0.013 | 13/40 (C-33 A, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.649×** | -3.9 | 0.032 | 16/38 (LoVo, A549, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.452×** | -3.7 | 0.040 | 13/36 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.685×** | -3.4 | 0.089 | 13/39 (SW1417, HT-29, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.687×** | -3.4 | 0.089 | 16/38 (A-427, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14090. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 6.31 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0725× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[NCI-H23 (line)]] | alt | 5.51 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0946× (z -8.5) ⚠ toxic |
| [[SW480 (line)]] | alt | 3.36 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0477× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.753 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.973 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.872 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14090), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK8IP2]] | +0.68 | +0.72 / +0.57 | both halves | 9e-06 |  |
| [[LINC00240]] | +0.68 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[ZFHX2]] | +0.68 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[ZC2HC1C]] | +0.66 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[PIGP]] | +0.66 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[GLIS2]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[C11orf71]] | +0.66 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[NDUFV2-AS1]] | +0.65 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[UPK2]] | +0.65 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[LINC01569]] | +0.65 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[NDRG2]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[TCEANC]] | +0.64 | +0.71 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TREX2]] | -0.61 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[ERI3]] | -0.61 | -0.67 / -0.41 | both halves | 4e-05 |  |
| [[BCAP31]] | -0.60 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[CHID1]] | -0.60 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[NTAQ1]] | -0.60 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[DROSHA]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.59 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[URB1]] | -0.59 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[HERC2P9]] | -0.59 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[HERC2]] | -0.58 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[PRIM2]] | -0.58 | -0.60 / -0.39 | both halves | 6e-05 |  |
| [[BLTP2]] | -0.57 | -0.54 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ID2-AS1]] | B | ID2-AS1 activity raises MAP3K2-DT's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.60× lower at baseline in the lines without ID2-AS1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[KLRC2]] | B | KLRC2 activity raises MAP3K2-DT's level | lines that do not express KLRC2 (27) vs lines expressing it (23) | 1.32× lower at baseline in the lines without KLRC2 | 0.088 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRK1, TRPM2-AS |
| [[MAP2K1]] | B | MAP2K1 activity lowers MAP3K2-DT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.559). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (20.4, 7.5); signed map (40.2, -0.9). **Vector** length 50.0, 6.92% of its response variance represented; |z| ≥ 3 in 908 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +7.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +3.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.8 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -4.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -3.4 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.2 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -2.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | MAP3K2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q14.3 — chr2:127,388,173-127,406,228 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ENST00000433673 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54088](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54088) · Entrez [100506922](https://www.ncbi.nlm.nih.gov/gene/100506922) · Ensembl [ENSG00000236682](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236682)

## Data

Gene col 14090: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14090); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14090, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14090]; `tensor/DDL_lfc|DDL_z.npy` [14090]; `embed/gene_vectors.npy` [14090]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14090 or target_col == 14090). Every well: [[MAP3K2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
