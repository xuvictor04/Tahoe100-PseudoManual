---
symbol: "HEIH"
type: "gene"
col: 15925
ensembl_id: "ENSG00000278970"
name: "hepatocellular carcinoma up-regulated EZH2-associated long non-coding RNA"
location: "5q35.3"
module: 12
arm: "+"
pooled_cpm: 7.62
n_lines_expressing: 43
n_dd_up: 1
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# HEIH

*hepatocellular carcinoma up-regulated EZH2-associated long non-coding RNA* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.55× (z +3.9, q 0.034, up in 17 of 31 measured lines) ⚠ transcription drop.
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.446× (z -7.2, q 3e-10, down in 30 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFKBIL1]] (+0.72, fdr 7e-06), [[RRAGC]] (+0.67, fdr 7e-06), [[RNF7]] (+0.65, fdr 1e-05); moves opposite to [[SPCS3]] (-0.63, fdr 1e-05), [[EIF5A]] (-0.61, fdr 1e-05), [[PRPS2]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 3 go from it, the strongest it → [[MID1IP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15925.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +3.9 | 0.034 | 17/31 (Panc 03.27, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +3.8 | 0.034 | 7/41 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.71× | +3.3 | 0.21 | 6/36 (Panc 03.27, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.66× | +3.1 | 0.25 | 10/34 (COLO 205, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.27× | +3.1 | 0.25 | 8/41 (NCI-H460, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15925.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.446×** | -7.2 | 3e-10 | 30/40 (SW 900, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.507×** | -6.1 | 3e-07 | 23/36 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.545×** | -5.4 | 1e-05 | 26/40 (J82, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.551×** | -5.3 | 1e-05 | 25/40 (PANC-1, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.585×** | -4.8 | 2e-04 | 23/39 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.588×** | -4.8 | 2e-04 | 20/39 (PANC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.603×** | -4.5 | 5e-04 | 24/40 (NCI-H460, SW480, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.623×** | -4.2 | 0.002 | 17/39 (C32, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.648×** | -3.9 | 0.007 | 16/39 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.669×** | -3.4 | 0.039 | 14/39 (AN3 CA, MIA PaCa-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.699×** | -3.2 | 0.071 | 19/40 (SW 900, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.48 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15925. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 12.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 8.61 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0809× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 3.32 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0576× (z -8.6) |
| [[HS-578T (line)]] | alt | 8.88 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 9.44 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 5.98 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0849× (z -13.5) |
| [[SNU-423 (line)]] | alt | 5.64 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.0620× (z -9.2) |
| [[A-172 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.699 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.757 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.756 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15925), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKBIL1]] | +0.72 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[RRAGC]] | +0.67 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[RNF7]] | +0.65 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[RP9]] | +0.65 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[GFER]] | +0.65 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[SPACA9]] | +0.65 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[MPHOSPH8]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[DSTYK]] | +0.63 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[MTIF3]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[NSMCE3]] | +0.62 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[CCDC174]] | +0.62 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[SNHG11]] | +0.62 | +0.51 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPCS3]] | -0.63 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[EIF5A]] | -0.61 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[PRPS2]] | -0.59 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[FAM91A1]] | -0.59 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[LRP8]] | -0.58 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[MACROH2A1]] | -0.57 | -0.39 / -0.62 | both halves | 6e-05 |  |
| [[ASPH]] | -0.57 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[CHID1]] | -0.57 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[SDC1]] | -0.57 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[TFDP1]] | -0.56 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[EIF4EBP2]] | -0.56 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[ARHGAP4]] | -0.56 | -0.39 / -0.57 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises HEIH's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC00847]] | C | LINC00847 activity raises HEIH's level | lines that do not express LINC00847 (4) vs lines expressing it (46) | 3.95× lower at baseline in the lines without LINC00847 | 0.009 | ⚠ few lines (4 vs 46); across organs; also absent: DDR1, FTH1, HEIH; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MID1IP1]] | B | HEIH activity raises MID1IP1's level | lines that do not express HEIH (7) vs lines expressing it (43) | 1.63× lower at baseline in the lines without HEIH | 0.064 | ⚠ within organs, on part of the lines; also absent: HYI, LINC00847; maybe low, not absent |
| [[EAPP]] | B | HEIH activity raises EAPP's level | lines that do not express HEIH (7) vs lines expressing it (43) | 1.28× lower at baseline in the lines without HEIH | 0.071 | ⚠ within organs, on part of the lines; also absent: HYI, LINC00847; maybe low, not absent |
| [[LINC00847]] | C | HEIH activity raises LINC00847's level | lines that do not express HEIH (7) vs lines expressing it (43) | 2.42× lower at baseline in the lines without HEIH | 0.060 | ⚠ within organs, on part of the lines; also absent: HYI, LINC00847; maybe low, not absent; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.678). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-46.3, -5.5); signed map (-8.3, 0.1). **Vector** length 62.8, 11.7% of its response variance represented; |z| ≥ 3 in 716 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +1.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +2.0 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.9 | +3.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +1.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.6 | +1.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.1 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.8 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | hepatocellular carcinoma up-regulated EZH2-associated long non-coding RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q35.3 — chr5:180,826,871-180,831,621 (-) |
| Ensembl biotype | lncRNA |
| Also known as | LINC-HEIH, lncRNA-HEIH, LINC00848, HCCAT2 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100859930](https://www.ncbi.nlm.nih.gov/gene/100859930):

> Biomarker of esophagus squamous cell carcinoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:45049](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:45049) · Entrez [100859930](https://www.ncbi.nlm.nih.gov/gene/100859930) · Ensembl [ENSG00000278970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000278970)

## Data

Gene col 15925: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15925); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15925, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15925]; `tensor/DDL_lfc|DDL_z.npy` [15925]; `embed/gene_vectors.npy` [15925]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15925 or target_col == 15925). Every well: [[HEIH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEIH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
