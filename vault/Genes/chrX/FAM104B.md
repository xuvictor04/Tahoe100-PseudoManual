---
symbol: "FAM104B"
type: "gene"
col: 11295
ensembl_id: "ENSG00000182518"
name: "VCP nuclear cofactor family member 2"
location: "Xp11.21"
module: 58
arm: "+"
pooled_cpm: 4.82
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# FAM104B

*VCP nuclear cofactor family member 2* — Xp11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.73× (z +12.7, q 3e-34, up in 8 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.39× (z +4.7, q 2e-04, up in 7 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SHP-77 4.85×, PANC-1 5.29×, HOP62 5.37×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.515× (z -6.6, q 2e-08, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKN2AIPNL]] (+0.66, fdr 7e-06), [[FLVCR1-DT]] (+0.63, fdr 4e-05), [[MFSD3]] (+0.61, fdr 1e-05); moves opposite to [[ATXN1L]] (-0.50, fdr 1e-04), [[TRPV1]] (-0.49, fdr 1e-04), [[LINC02936]] (-0.48, fdr 3e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GAMT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11295.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SHP-77 4.85×, PANC-1 5.29×, HOP62 5.37×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.73×** | +12.7 | 3e-34 | 8/8 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.29×** | +12.0 | 1e-30 | 24/25 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.52×** | +8.6 | 2e-15 | 9/12 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.69×** | +5.3 | 2e-05 | 20/45 (HOP62, NCI-H460, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +4.7 | 2e-04 | 7/45 (C-33 A, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +4.7 | 3e-04 | 10/26 (HOP62, SHP-77, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.6 | 3e-04 | 12/27 (NCI-H1573, A-427, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.55×** | +4.4 | 7e-04 | 14/46 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.41×** | +3.5 | 0.029 | 10/46 (HEC-1-A, NCI-H1573, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.55×** | +3.1 | 0.099 | 5/26 (A498, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Proglumide (drug)]] 0.05 µM |  | 1.35× | +3.1 | 0.11 | 2/44 (A-427, RKO) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11295.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.515×** | -6.6 | 2e-08 | 25/46 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.693×** | -5.2 | 6e-05 | 17/37 (SHP-77, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.664×** | -4.1 | 0.008 | 13/46 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.669×** | -4.0 | 0.008 | 17/46 (Hs 766T, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.671×** | -4.0 | 0.008 | 11/36 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.675×** | -3.9 | 0.008 | 14/34 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.695×** | -3.6 | 0.023 | 15/44 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.733× | -3.1 | 0.14 | 15/46 (SW48, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11295. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.76 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +9.4) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.180× (z -9.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 27.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -9.1) |
| [[HOP62 (line)]] | alt | 6.38 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +8.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 5.29 | 0 | 1 | — | [[Thymopentin (drug)]] 0.05 µM 0.0486× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 4.53 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0680× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 6.37 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0708× (z -8.9) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 6.90 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.106× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 6.56 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -8.9) |
| [[A-172 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11295), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN2AIPNL]] | +0.66 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[FLVCR1-DT]] | +0.63 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[MFSD3]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[COMMD8]] | +0.61 | +0.39 / +0.66 | both halves | 6e-05 |  |
| [[ATP6V0E2]] | +0.60 | +0.39 / +0.61 | both halves | 6e-05 |  |
| [[ARL2]] | +0.60 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[GVQW3]] | +0.59 | +0.65 / +0.39 | both halves | 6e-05 |  |
| [[CDK5]] | +0.58 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[SLC25A11]] | +0.58 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[SMIM10]] | +0.58 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[MRPL40]] | +0.57 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[BOLA3]] | +0.57 | +0.46 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN1L]] | -0.50 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[TRPV1]] | -0.49 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[LINC02936]] | -0.48 | -0.44 / -0.29 | both halves | 3e-04 |  |
| [[MC1R]] | -0.46 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[SPON1-AS1]] | -0.46 | -0.20 / -0.38 | ⚠ not reproduced | 8e-04 |  |
| [[MCF2]] | -0.45 | -0.35 / -0.27 | both halves | 3e-04 |  |
| [[NPIPA1]] | -0.45 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[CCDC17]] | -0.45 | -0.28 / -0.25 | both halves | 4e-04 |  |
| [[MUC20-OT1]] | -0.45 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[UNKL]] | -0.45 | -0.39 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAMT]] | B | GAMT activity raises FAM104B's level | lines that do not express GAMT (11) vs lines expressing it (39) | 1.45× lower at baseline in the lines without GAMT | 0.035 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: HDGFL3, HLTF, EHD3 |
| [[EID2B]] | B | EID2B activity raises FAM104B's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.55× lower at baseline in the lines without EID2B | 0.040 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[FAM229B]] | B | FAM229B activity raises FAM104B's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 1.59× lower at baseline in the lines without FAM229B | 0.086 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |
| [[HDAC6]] | B | HDAC6 activity lowers FAM104B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.518). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.0, -13.0); signed map (-22.3, -3.8). **Vector** length 35.8, 3.42% of its response variance represented; |z| ≥ 3 in 795 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.9 | +4.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +0.3 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | +1.0 | +1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.0 | +1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +0.9 | +2.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -1.8 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -6.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -3.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | VCP nuclear cofactor family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.21 — chrX:55,143,102-55,161,310 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20434; previously CXorf44, FAM104B |
| Matched by | ensembl_id |

UniProt [Q5XKR9](https://www.uniprot.org/uniprotkb/Q5XKR9) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25085](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25085) · Entrez [90736](https://www.ncbi.nlm.nih.gov/gene/90736) · UniProt [Q5XKR9](https://www.uniprot.org/uniprotkb/Q5XKR9) · Ensembl [ENSG00000182518](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182518)

## Data

Gene col 11295: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11295); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11295, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11295]; `tensor/DDL_lfc|DDL_z.npy` [11295]; `embed/gene_vectors.npy` [11295]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11295 or target_col == 11295). Every well: [[FAM104B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM104B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
