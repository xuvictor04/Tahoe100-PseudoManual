---
symbol: "TACO1"
type: "gene"
col: 5867
ensembl_id: "ENSG00000136463"
name: "translational activator of cytochrome c oxidase I"
location: "17q23.3"
module: 7
arm: "+"
pooled_cpm: 8.29
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TACO1

*translational activator of cytochrome c oxidase I* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.41× (z +9.6, q 3e-19, up in 11 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.38× (z +5.1, q 3e-05, up in 21 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.571× (z -6.4, q 8e-08, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FUNDC1]] (+0.77, fdr 7e-06), [[FBXO38]] (+0.75, fdr 1e-05), [[CBLL1]] (+0.75, fdr 1e-05); moves opposite to [[RPS6KA5]] (-0.65, fdr 1e-05), [[SLC25A5]] (-0.63, fdr 4e-05), [[FAM118A]] (-0.62, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5867.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +9.6 | 3e-19 | 11/16 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +8.6 | 2e-15 | 25/33 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +6.7 | 5e-09 | 13/24 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.43×** | +5.7 | 1e-06 | 20/43 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.1 | 3e-05 | 21/43 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +5.0 | 5e-05 | 25/42 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +5.0 | 5e-05 | 22/46 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +4.9 | 6e-05 | 19/47 (CFPAC-1, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.9 | 6e-05 | 20/37 (SW1417, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.53×** | +4.7 | 1e-04 | 20/46 (NCI-H1573, SW480, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +4.5 | 4e-04 | 17/37 (HOP62, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +4.0 | 0.003 | 13/47 (HS-578T, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +3.5 | 0.018 | 10/46 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.77×** | +3.4 | 0.026 | 8/43 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.22×** | +3.2 | 0.045 | 10/48 (NCI-H460, HepG2/C3A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.051 | 14/47 (RPMI-7951, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.094 | 8/43 (AsPC-1, COLO 205, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5867.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.571×** | -6.4 | 8e-08 | 28/47 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.738×** | -4.9 | 2e-04 | 24/48 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.652×** | -4.9 | 2e-04 | 22/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.669×** | -4.6 | 6e-04 | 21/45 (LOX-IMVI, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.680×** | -4.4 | 0.001 | 18/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.726×** | -3.7 | 0.023 | 15/46 (CHP-212, NCI-H661, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.751×** | -3.3 | 0.084 | 12/47 (AN3 CA, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5867. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 14.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.96× (z +11.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 4.90 | 0 | 2 | — | [[XRK3F2 (drug)]] 0.05 µM 0.0725× (z -9.2) |
| [[LoVo (line)]] | wt | 7.24 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 17.4× (z +13.2) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 9.75 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.32× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.151× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 6.51 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0938× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 9.33 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -9.5) |
| [[A-172 (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5867), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUNDC1]] | +0.77 | +0.85 / +0.61 | both halves | 7e-06 |  |
| [[FBXO38]] | +0.75 | +0.81 / +0.55 | both halves | 1e-05 |  |
| [[CBLL1]] | +0.75 | +0.79 / +0.51 | both halves | 1e-05 |  |
| [[PSMD7]] | +0.75 | +0.82 / +0.57 | both halves | 1e-05 |  |
| [[MRPL38]] | +0.74 | +0.79 / +0.60 | both halves | 7e-06 |  |
| [[ZNF189]] | +0.74 | +0.76 / +0.54 | both halves | 1e-05 |  |
| [[ZNF407-AS1]] | +0.74 | +0.78 / +0.54 | both halves | 1e-05 |  |
| [[ZNF268]] | +0.73 | +0.79 / +0.60 | both halves | 7e-06 |  |
| [[ZSCAN29]] | +0.73 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[HIKESHI]] | +0.72 | +0.78 / +0.42 | both halves | 4e-05 |  |
| [[ZNF629]] | +0.72 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[GTF3C4]] | +0.72 | +0.75 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS6KA5]] | -0.65 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[SLC25A5]] | -0.63 | -0.60 / -0.40 | both halves | 4e-05 |  |
| [[FAM118A]] | -0.62 | -0.68 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TACO1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.805). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-37.2, 9.3); signed map (-1.9, -24.9). **Vector** length 62.3, 9.71% of its response variance represented; |z| ≥ 3 in 786 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.6 | +5.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.5 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +5.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +0.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | -4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.4 | -6.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.9 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -0.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | translational activator of cytochrome c oxidase I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:63,600,882-63,608,365 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CCDC44 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex IV assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSH4](https://www.uniprot.org/uniprotkb/Q9BSH4) (Translational activator of cytochrome c oxidase 1):

> Acts as a translational activator of mitochondrially-encoded cytochrome c oxidase 1.

**Summary**, from NCBI Gene [51204](https://www.ncbi.nlm.nih.gov/gene/51204):

> This gene encodes a mitochondrial protein that function as a translational activator of mitochondrially-encoded cytochrome c oxidase 1. Mutations in this gene are associated with Leigh syndrome.[provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:24316](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24316) · Entrez [51204](https://www.ncbi.nlm.nih.gov/gene/51204) · UniProt [Q9BSH4](https://www.uniprot.org/uniprotkb/Q9BSH4) · Ensembl [ENSG00000136463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136463)

## Data

Gene col 5867: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5867); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5867, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5867]; `tensor/DDL_lfc|DDL_z.npy` [5867]; `embed/gene_vectors.npy` [5867]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5867 or target_col == 5867). Every well: [[TACO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TACO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
