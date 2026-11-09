---
symbol: "RGPD8"
type: "gene"
col: 9829
ensembl_id: "ENSG00000169629"
name: "RANBP2 like and GRIP domain containing 8"
location: "2q14.1"
module: 30
arm: "+"
pooled_cpm: 5.82
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# RGPD8

*RANBP2 like and GRIP domain containing 8* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.74× (z +9.4, q 3e-18, up in 30 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Megestrol (drug)]] 0.05 µM: 0.698× (z -4.3, q 0.009, down in 11 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1792 0.0892×, SW1417 0.0819×, HS-578T 0.0835×, NCI-H2030 0.219×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (HOP62 0.0986×, NCI-H2030 0.151×, NCI-H2347 0.157×, NCI-H1792 0.168×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0729×; ⚠ transcription drop); [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM in 1 line (A-172 0.0895×); [[Naproxen (drug)]] 0.05 µM in 1 line (LoVo 0.0806×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCAS4]] (+0.58, fdr 1e-05), [[LINC00674]] (+0.57, fdr 1e-05), [[UBE2Q2P1]] (+0.55, fdr 2e-05); moves opposite to [[ZNF407]] (-0.53, fdr 5e-05), [[LARP4B]] (-0.49, fdr 8e-05), [[GPAA1]] (-0.48, fdr 5e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PIK3CD]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9829.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +9.4 | 3e-18 | 30/41 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +5.1 | 8e-05 | 16/46 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +4.2 | 0.005 | 9/37 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +4.1 | 0.005 | 10/42 (MIA PaCa-2, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.009 | 12/46 (LoVo, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.54×** | +3.4 | 0.070 | 3/47 (A-427, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.30× | +3.2 | 0.11 | 12/34 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.29× | +3.1 | 0.14 | 2/43 (LoVo, SW1417) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9829.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1792 0.0892×, SW1417 0.0819×, HS-578T 0.0835×, NCI-H2030 0.219×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (HOP62 0.0986×, NCI-H2030 0.151×, NCI-H2347 0.157×, NCI-H1792 0.168×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0729×; ⚠ transcription drop); [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM in 1 line (A-172 0.0895×); [[Naproxen (drug)]] 0.05 µM in 1 line (LoVo 0.0806×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Megestrol (drug)]] 0.05 µM |  | **0.698×** | -4.3 | 0.009 | 11/47 (HepG2/C3A, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.707×** | -4.0 | 0.014 | 12/37 (A-172, SK-MEL-2, …) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.600×** | -4.0 | 0.014 | 16/31 (NCI-H1573, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.834× | -3.1 | 0.26 | 10/47 (COLO 205, PANC-1, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.776× | -3.0 | 0.26 | 4/46 (SW 1271, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9829. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 13.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 12.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0892× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[SW1417 (line)]] | alt | 9.36 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0819× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[A-172 (line)]] | wt | 4.52 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0895× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 6.93 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0729× (z -11.5) ⚠ transcription drop |
| [[HOP62 (line)]] | alt | 8.24 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0986× (z -11.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 6.03 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0835× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[LoVo (line)]] | wt | 3.29 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0806× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -10.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9829), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 9 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAS4]] | +0.58 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[LINC00674]] | +0.57 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[UBE2Q2P1]] | +0.55 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[PRKAB2]] | +0.54 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[C3orf33]] | +0.53 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[CGRRF1]] | +0.53 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[ZNF815P]] | +0.52 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[SNHG32]] | +0.51 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[SUGT1P4-STRA6LP]] | +0.51 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[SNHG6]] | +0.51 | +0.48 / +0.38 | both halves | 6e-05 |  |
| [[RCAN3]] | +0.49 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[RUFY2]] | +0.49 | +0.52 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF407]] | -0.53 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[LARP4B]] | -0.49 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[GPAA1]] | -0.48 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[M6PR]] | -0.48 | -0.56 / -0.32 | both halves | 2e-04 |  |
| [[C2CD3]] | -0.47 | -0.52 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[SNRPB]] | -0.47 | -0.56 / -0.27 | both halves | 3e-04 |  |
| [[ASXL2]] | -0.46 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[XRCC5]] | -0.43 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[ATXN7L3B]] | -0.43 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[EIF5A]] | -0.42 | -0.51 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[VMA21]] | -0.42 | -0.51 / -0.21 | both halves | 7e-04 |  |
| [[C1GALT1C1]] | -0.42 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[TGOLN2]] | -0.42 | -0.47 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIK3CD]] | B | PIK3CD activity raises RGPD8's level | lines that do not express PIK3CD (8) vs lines expressing it (42) | 1.76× lower at baseline in the lines without PIK3CD | 0.045 | ⚠ within organs, on part of the lines; also absent: WNT3, CCDC3, CSRP2; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity lowers RGPD8's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.384). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-3.9, -3.1); signed map (-26.6, -6.1). **Vector** length 40.1, 3.85% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.4 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +1.1 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +0.8 | +1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.8 | +1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.8 | +0.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | +3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.8 | +0.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | -0.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | -1.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | RANBP2 like and GRIP domain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:112,368,369-112,434,488 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RanBP2alpha; previously RANBP2L1 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

UniProt [O14715](https://www.uniprot.org/uniprotkb/O14715) carries no function annotation.

**Summary**, from NCBI Gene [727851](https://www.ncbi.nlm.nih.gov/gene/727851):

> Predicted to enable SUMO transferase activity. Predicted to be involved in NLS-bearing protein import into nucleus and nuclear export. Predicted to be part of nuclear pore. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9849](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9849) · Entrez [727851](https://www.ncbi.nlm.nih.gov/gene/727851) · UniProt [O14715](https://www.uniprot.org/uniprotkb/O14715) · Ensembl [ENSG00000169629](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169629)

## Data

Gene col 9829: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9829); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9829, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9829]; `tensor/DDL_lfc|DDL_z.npy` [9829]; `embed/gene_vectors.npy` [9829]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9829 or target_col == 9829). Every well: [[RGPD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGPD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
