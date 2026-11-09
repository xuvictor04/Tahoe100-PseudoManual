---
symbol: "EIF1AY"
type: "gene"
col: 12644
ensembl_id: "ENSG00000198692"
name: "eukaryotic translation initiation factor 1A Y-linked"
location: "Yq11.223"
module: 199
arm: "+"
pooled_cpm: 7.07
n_lines_expressing: 19
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/199"]
generated_by: "tahoemap"
---

# EIF1AY

*eukaryotic translation initiation factor 1A Y-linked* — Yq11.223

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.30× (z +12.7, q 5e-34, up in 14 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +6.4, q 3e-08, up in 13 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM133A]] (+0.56, fdr 5e-05), [[SNRNP27]] (+0.54, fdr 3e-05), [[PEX5L]] (+0.53, fdr 4e-05); moves opposite to [[WRNIP1]] (-0.48, fdr 4e-05), [[LRFN3]] (-0.46, fdr 3e-05), [[PTK2]] (-0.45, fdr 9e-05).
> It is in [[Module 199]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[EFR3B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12644.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.30×** | +12.7 | 5e-34 | 14/14 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.07×** | +10.2 | 3e-22 | 8/10 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.71×** | +7.0 | 5e-10 | 9/12 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +6.4 | 3e-08 | 13/16 (A-172, COLO 205, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.77×** | +6.1 | 1e-07 | 14/17 (A549, NCI-H460, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +4.0 | 0.005 | 9/17 (C32, SK-MEL-2, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.69×** | +4.0 | 0.005 | 3/16 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +3.9 | 0.007 | 7/17 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +3.4 | 0.038 | 10/16 (SK-MEL-2, J82, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.4 | 0.039 | 6/15 (J82, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.58×** | +3.3 | 0.055 | 6/17 (C32, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +3.2 | 0.056 | 12/17 (COLO 205, A-427, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.062 | 4/17 (J82, HCT15, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12644.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.661× | -3.1 | 0.94 | 2/17 (A549, COLO 205) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12644. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.80× (z +12.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 15.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.658 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.824 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.675 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.763 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.919 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.953 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.688 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.820 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.648 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.857 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.977 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.921 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.677 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12644), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM133A]] | +0.56 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[SNRNP27]] | +0.54 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[PEX5L]] | +0.53 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[MITD1]] | +0.47 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[NR1H4]] | +0.45 | +0.49 / +0.24 | both halves | 4e-04 |  |
| [[AKAP9]] | +0.45 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[UBXN4]] | +0.45 | +0.64 / +0.23 | both halves | 5e-04 |  |
| [[ATOSA]] | +0.44 | +0.34 / +0.39 | both halves | 1e-04 |  |
| [[ZIC1]] | +0.44 | +0.33 / +0.34 | both halves | 1e-04 |  |
| [[MR1]] | +0.44 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[EPB41]] | +0.44 | +0.34 / +0.45 | both halves | 1e-04 |  |
| [[AIMP1]] | +0.43 | +0.57 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRNIP1]] | -0.48 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[LRFN3]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[PTK2]] | -0.45 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[LSM12]] | -0.45 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[SMG1P2]] | -0.44 | -0.56 / -0.32 | both halves | 2e-04 |  |
| [[GNAZ]] | -0.44 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[SHANK3]] | -0.44 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[SRPX]] | -0.44 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[PCYOX1L]] | -0.43 | -0.27 / -0.27 | both halves | 3e-04 |  |
| [[ICMT]] | -0.43 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[WASF3]] | -0.43 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[TATDN2]] | -0.43 | -0.50 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EIF1AY's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ANOS2P]] | C | ANOS2P activity raises EIF1AY's level | lines that do not express ANOS2P (32) vs lines expressing it (18) | 11.24× lower at baseline in the lines without ANOS2P | 5e-07 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, KDM5D; co-absent with the target |
| [[NR1H4]] | C | NR1H4 activity raises EIF1AY's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 2.78× lower at baseline in the lines without NR1H4 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent; co-absent with the target |
| [[TNFRSF19]] | C | TNFRSF19 activity raises EIF1AY's level | lines that do not express TNFRSF19 (21) vs lines expressing it (29) | 2.67× lower at baseline in the lines without TNFRSF19 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, PCDH9, LOXL3; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFR3B]] | B | EIF1AY activity raises EFR3B's level | lines that do not express EIF1AY (31) vs lines expressing it (19) | 1.72× lower at baseline in the lines without EIF1AY | 0.084 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY |
| [[ANOS2P]] | C | EIF1AY activity raises ANOS2P's level | lines that do not express EIF1AY (31) vs lines expressing it (19) | 3.37× lower at baseline in the lines without EIF1AY | 1e-04 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |
| [[TNFRSF19]] | C | EIF1AY, [[TTTY10]] activity raises TNFRSF19's level | lines that do not express EIF1AY, TTTY10 (31) vs lines expressing them (19) | 3.14× lower at baseline in the lines without EIF1AY, TTTY10 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target; co-absent genes |
| [[NR1H4]] | C | EIF1AY activity raises NR1H4's level | lines that do not express EIF1AY (31) vs lines expressing it (19) | 1.27× lower at baseline in the lines without EIF1AY | 0.084 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |

## Where it sits

- **Module**: [[Module 199]]; 16 genes; every member is in the + arm (projection on the module's main direction -0.496). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.7, 2.3); signed map (1.2, -15.7). **Vector** length 27.4, 5.58% of its response variance represented; |z| ≥ 3 in 224 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +1.9 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +2.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.8 | +2.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +0.8 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.7 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.6 | -0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.6 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.5 | +0.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.4 | +1.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.0 | +2.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | +0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -0.9 | +7.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -0.8 | -0.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.5 | +1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -0.5 | +0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.5 | +0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 1A Y-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Yq11.223 — chrY:20,575,776-20,593,154 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [O14602](https://www.uniprot.org/uniprotkb/O14602) (Eukaryotic translation initiation factor 1A, Y-chromosomal):

> Component of the 43S pre-initiation complex (43S PIC), which binds to the mRNA cap-proximal region, scans mRNA 5'-untranslated region, and locates the initiation codon. This protein enhances formation of the cap-proximal complex. Together with EIF1, facilitates scanning, start codon recognition, promotion of the assembly of 48S complex at the initiation codon (43S PIC becomes 48S PIC after the start codon is reached), and dissociation of aberrant complexes. After start codon location, together …

**Summary**, from NCBI Gene [9086](https://www.ncbi.nlm.nih.gov/gene/9086):

> This gene is located on the non-recombining region of the Y chromosome. It encodes a protein related to eukaryotic translation initiation factor 1A (EIF1A), which may function in stabilizing the binding of the initiator Met-tRNA to 40S ribosomal subunits. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:3252](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3252) · Entrez [9086](https://www.ncbi.nlm.nih.gov/gene/9086) · UniProt [O14602](https://www.uniprot.org/uniprotkb/O14602) · Ensembl [ENSG00000198692](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198692)

## Data

Gene col 12644: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12644); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12644, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12644]; `tensor/DDL_lfc|DDL_z.npy` [12644]; `embed/gene_vectors.npy` [12644]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12644 or target_col == 12644). Every well: [[EIF1AY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF1AY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
