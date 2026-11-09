---
symbol: "MED18"
type: "gene"
col: 5124
ensembl_id: "ENSG00000130772"
name: "mediator complex subunit 18"
location: "1p35.3"
module: 11
arm: "+"
pooled_cpm: 6.48
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# MED18

*mediator complex subunit 18* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.06× (z +12.4, q 2e-32, up in 29 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.693× (z -4.5, q 0.002, down in 17 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC174]] (+0.80, fdr 7e-06), [[ZNF226]] (+0.79, fdr 7e-06), [[FAM200A]] (+0.78, fdr 7e-06); moves opposite to [[ADAM15]] (-0.72, fdr 7e-06), [[MAPK9]] (-0.69, fdr 7e-06), [[CRTAP]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TCEAL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5124.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.06×** | +12.4 | 2e-32 | 29/40 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.48×** | +10.9 | 3e-25 | 33/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.38×** | +10.1 | 1e-21 | 30/34 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.03×** | +8.6 | 1e-15 | 35/46 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.08×** | +8.5 | 2e-15 | 30/45 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +7.3 | 2e-11 | 21/46 (PANC-1, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.71×** | +6.5 | 8e-09 | 24/44 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.66×** | +6.1 | 8e-08 | 19/36 (SNU-423, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +5.0 | 4e-05 | 1/10 (CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.39×** | +3.9 | 0.005 | 11/45 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +3.8 | 0.009 | 3/17 (CFPAC-1, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.7 | 0.011 | 9/43 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.5 | 0.019 | 13/43 (HT-29, COLO 205, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.055 | 7/44 (LOX-IMVI, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.063 | 6/45 (NCI-H460, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.067 | 4/43 (A-172, C32, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.094 | 3/47 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5124.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.693×** | -4.5 | 0.002 | 17/47 (LOX-IMVI, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.694×** | -4.5 | 0.002 | 18/47 (NCI-H1573, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.698×** | -4.4 | 0.002 | 10/47 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | **0.738×** | -3.5 | 0.074 | 7/46 (NCI-H2030, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.753×** | -3.4 | 0.086 | 8/41 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.763×** | -3.3 | 0.088 | 2/47 (COLO 205, BT-474) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5124. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 10.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +16.1) | — |
| [[A498 (line)]] | wt | 5.75 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.123× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 8.98 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0900× (z -8.5) |
| [[LoVo (line)]] | wt | 8.41 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.193× (z -8.8) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 8.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 5.66 | 0 | 1 | — | [[Acetohexamide (drug)]] 0.5 µM 0.0900× (z -8.5) |
| [[A-172 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5124), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC174]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[ZNF226]] | +0.79 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.78 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[ZNF585A]] | +0.75 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[NAIF1]] | +0.74 | +0.81 / +0.57 | both halves | 1e-05 |  |
| [[COIL]] | +0.73 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[TJAP1]] | +0.73 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[PEX12]] | +0.73 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[WASHC1]] | +0.72 | +0.78 / +0.61 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.72 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[C14orf119]] | +0.72 | +0.73 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM15]] | -0.72 | -0.68 / -0.66 | both halves | 7e-06 |  |
| [[MAPK9]] | -0.69 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[CRTAP]] | -0.69 | -0.72 / -0.68 | both halves | 7e-06 |  |
| [[TBCD]] | -0.67 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[STT3B]] | -0.66 | -0.64 / -0.69 | both halves | 7e-06 |  |
| [[NUTF2]] | -0.65 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[HACD3]] | -0.65 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.64 | -0.57 / -0.63 | both halves | 9e-06 | pathway: Adipogenesis |
| [[SETD3]] | -0.64 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[PARP1]] | -0.64 | -0.46 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCEAL3]] | B | TCEAL3 activity lowers MED18's level | lines that do not express TCEAL3 (7) vs lines expressing it (43) | 1.32× higher at baseline in the lines without TCEAL3 | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, TTLL7, ENSG00000234405 |
| [[HDAC6]] | B | HDAC6 activity raises MED18's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.831). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.8, 5.6); signed map (4.2, -19.2). **Vector** length 69.0, 11.4% of its response variance represented; |z| ≥ 3 in 820 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +12.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.0 | +10.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.0 | +7.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.0 | +8.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +10.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +6.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +0.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.4 | +0.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.7 | -2.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.5 | -4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.3 | -1.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.3 | -4.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.0 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -1.0 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:28,329,002-28,335,965 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20045, p28b, SRB5 |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 8 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Adipogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUE0](https://www.uniprot.org/uniprotkb/Q9BUE0) (Mediator of RNA polymerase II transcription subunit 18):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [54797](https://www.ncbi.nlm.nih.gov/gene/54797):

> MED18 is a component of the Mediator complex, which is a coactivator for DNA-binding factors that activate transcription via RNA polymerase II (Sato et al., 2003 [PubMed 12584197]).[supplied by OMIM, Oct 2008]

**Accessions** — [HGNC:25944](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25944) · Entrez [54797](https://www.ncbi.nlm.nih.gov/gene/54797) · UniProt [Q9BUE0](https://www.uniprot.org/uniprotkb/Q9BUE0) · Ensembl [ENSG00000130772](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130772)

## Data

Gene col 5124: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5124); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5124, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5124]; `tensor/DDL_lfc|DDL_z.npy` [5124]; `embed/gene_vectors.npy` [5124]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5124 or target_col == 5124). Every well: [[MED18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
