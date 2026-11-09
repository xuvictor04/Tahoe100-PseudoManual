---
symbol: "CCDC43"
type: "gene"
col: 11097
ensembl_id: "ENSG00000180329"
name: "coiled-coil domain containing 43"
location: "17q21.31"
module: 12
arm: "+"
pooled_cpm: 43.4
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CCDC43

*coiled-coil domain containing 43* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.60× (z +6.1, q 8e-07, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.701× (z -6.4, q 1e-07, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COIL]] (+0.76, fdr 7e-06), [[SLC4A1AP]] (+0.74, fdr 7e-06), [[PHAX]] (+0.71, fdr 7e-06); moves opposite to [[AKT1]] (-0.61, fdr 1e-05), [[ADAM10]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11097.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +6.1 | 8e-07 | 38/48 (SK-MEL-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.5 | 9e-06 | 36/47 (A-172, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.55×** | +5.3 | 2e-05 | 36/48 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.49×** | +4.9 | 9e-05 | 34/48 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.47×** | +4.9 | 9e-05 | 30/47 (NCI-H1792, KATO III, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +4.8 | 1e-04 | 34/48 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.29×** | +4.7 | 2e-04 | 27/48 (A-172, NCI-H1573, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.6 | 3e-04 | 36/48 (LoVo, A549, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +3.9 | 0.007 | 31/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.38×** | +3.8 | 0.007 | 29/47 (SW480, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.36×** | +3.8 | 0.008 | 20/40 (KATO III, A-427, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.010 | 26/48 (KATO III, SNU-423, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.012 | 22/48 (SK-MEL-2, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.40×** | +3.5 | 0.019 | 26/47 (SK-MEL-2, LS 180, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **1.30×** | +3.4 | 0.024 | 23/46 (HOP62, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.030 | 24/48 (A-172, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.094 | 22/48 (SNU-423, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11097.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.701×** | -6.4 | 1e-07 | 37/48 (HOP62, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.899× | -4.2 | 0.009 | 3/49 (Hs 766T, SW48, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.819×** | -3.5 | 0.061 | 23/48 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.757×** | -3.5 | 0.061 | 23/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.766×** | -3.4 | 0.085 | 22/48 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.771×** | -3.3 | 0.095 | 23/48 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11097. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 44.7 | 0 | 1 | — | [[MK-3903 (drug)]] 5 µM 0.0464× (z -10.7) |
| [[H4 (line)]] | wt | 44.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -9.9) |
| [[HOP62 (line)]] | alt | 37.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[RKO (line)]] | wt | 50.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -10.0) |
| [[A-172 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 93.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 52.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11097), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COIL]] | +0.76 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[SLC4A1AP]] | +0.74 | +0.84 / +0.68 | both halves | 7e-06 |  |
| [[PHAX]] | +0.71 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[SNW1]] | +0.71 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.70 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[SEC62]] | +0.69 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[PDRG1]] | +0.69 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[DCTN6]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[CWC22]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.68 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.67 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[DHX36]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT1]] | -0.61 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[ADAM10]] | -0.59 | -0.61 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CCDC43's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises CCDC43's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF573]] | C | ZNF573 activity raises CCDC43's level | lines that do not express ZNF573 (4) vs lines expressing it (46) | 1.52× lower at baseline in the lines without ZNF573 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with FBXW7; also absent: ZNF540, ZNF675, ZNF571; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.731). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.0, 3.1); signed map (-0.5, -17.3). **Vector** length 94.2, 27.6% of its response variance represented; |z| ≥ 3 in 687 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA Splicing - Major Pathway* (reactome, mean cos +0.50 to 17); *mRNA Splicing* (reactome, mean cos +0.50 to 17).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.3 | +3.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.5 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.1 | +6.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.8 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.4 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +1.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +3.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.8 | +1.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.6 | +0.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -2.1 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 43 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:44,673,069-44,689,779 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31795 |
| Matched by | ensembl_id |

UniProt [Q96MW1](https://www.uniprot.org/uniprotkb/Q96MW1) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26472](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26472) · Entrez [124808](https://www.ncbi.nlm.nih.gov/gene/124808) · UniProt [Q96MW1](https://www.uniprot.org/uniprotkb/Q96MW1) · Ensembl [ENSG00000180329](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180329)

## Data

Gene col 11097: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11097); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11097, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11097]; `tensor/DDL_lfc|DDL_z.npy` [11097]; `embed/gene_vectors.npy` [11097]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11097 or target_col == 11097). Every well: [[CCDC43 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC43.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
