---
symbol: "INPP5E"
type: "gene"
col: 7276
ensembl_id: "ENSG00000148384"
name: "inositol polyphosphate-5-phosphatase E"
location: "9q34.3"
module: 2
arm: "+"
pooled_cpm: 5.89
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# INPP5E

*inositol polyphosphate-5-phosphatase E* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.57× (z +6.1, q 6e-07, up in 19 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.643× (z -5.9, q 2e-06, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED22]] (+0.65, fdr 7e-06), [[KMT2D]] (+0.62, fdr 1e-05), [[TRIM65]] (+0.62, fdr 1e-05); moves opposite to [[TMEM14C]] (-0.49, fdr 9e-05), [[SLC50A1]] (-0.48, fdr 4e-05), [[ATP7A]] (-0.47, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7276.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +6.1 | 6e-07 | 19/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +4.5 | 0.002 | 2/11 (HT-29, HOP62) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.015 | 13/46 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.035 | 9/43 (LOX-IMVI, NCI-H23, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +3.5 | 0.054 | 6/40 (NCI-H460, A549, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.4 | 0.054 | 11/30 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.080 | 9/44 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.18× | +3.1 | 0.14 | 5/46 (SHP-77, HOP62, …) | top dose only | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.29× | +3.1 | 0.14 | 10/45 (A-172, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7276.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.643×** | -5.9 | 2e-06 | 21/47 (H4, J82, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Silodosin (drug)]] 5 µM |  | **0.680×** | -5.0 | 2e-04 | 14/41 (SW1417, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.704×** | -4.7 | 4e-04 | 10/43 (SNU-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.794×** | -4.4 | 0.002 | 16/47 (BT-474, J82, …) | all doses, stronger at high dose |  |
| [[Pyridoxine (drug)]] 5 µM |  | **0.802×** | -4.2 | 0.003 | 11/47 (A498, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.742×** | -4.0 | 0.006 | 12/47 (A-172, NCI-H661, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.747×** | -3.9 | 0.007 | 15/47 (A-172, SHP-77, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Tadalafil (drug)]] 0.5 µM |  | **0.773×** | -3.5 | 0.039 | 6/47 (A549, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7276. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -10.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 4.71 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.101× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 6.87 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.104× (z -9.0) |
| [[J82 (line)]] | alt | 8.51 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0811× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 3.75 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0720× (z -8.7) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H2030 (line)]] | alt | 3.81 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.05 µM 0.0722× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 4.76 | 0 | 1 (1 ⚠) | — | [[Carbidopa (monohydrate) (drug)]] 0.5 µM 0.0527× (z -9.1) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7276), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED22]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[KMT2D]] | +0.62 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[TRIM65]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[ZNF142]] | +0.60 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[ZBTB45]] | +0.58 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[HDAC10]] | +0.56 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ZNF746]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[RAPSN]] | +0.54 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[PKN3]] | +0.53 | +0.43 / +0.52 | both halves | 4e-05 |  |
| [[LRRC14]] | +0.53 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[MAPK12]] | +0.53 | +0.53 / +0.51 | both halves | 1e-05 | pathway: Organelle biogenesis and maintenance |
| [[LZTR1]] | +0.53 | +0.53 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM14C]] | -0.49 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[SLC50A1]] | -0.48 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[ATP7A]] | -0.47 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[BABAM2]] | -0.47 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[COX7B]] | -0.46 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[LINC01473]] | -0.45 | -0.46 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises INPP5E's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises INPP5E's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SLC22A20P]] | C | SLC22A20P activity lowers INPP5E's level | lines that do not express SLC22A20P (3) vs lines expressing it (47) | 1.30× higher at baseline in the lines without SLC22A20P | 0.092 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CDC42EP1, PLEKHG5, MYH16; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.451). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-15.9, -28.6); signed map (-8.8, -28.6). **Vector** length 56.8, 7.39% of its response variance represented; |z| ≥ 3 in 847 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.0 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +4.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +2.6 | +3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +1.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.2 | -4.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +0.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | inositol polyphosphate-5-phosphatase E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,428,619-136,439,845 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PPI5PIV, CORS1, pharbin; previously JBTS1 |
| Gene groups (HGNC) | Phosphoinositide phosphatases |
| Reactome | 9 pathways, smallest: ARL13B-mediated ciliary trafficking of INPP5E; Synthesis of PIPs at the Golgi membrane; Cargo trafficking to the periciliary membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRR6](https://www.uniprot.org/uniprotkb/Q9NRR6) (Phosphatidylinositol polyphosphate 5-phosphatase type IV):

> Phosphatidylinositol (PtdIns) phosphatase that specifically hydrolyzes the 5-phosphate of phosphatidylinositol-3,4,5-trisphosphate (PtdIns(3,4,5)P3), phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2) and phosphatidylinositol 3,5-bisphosphate (PtdIns(3,5)P2) (By similarity). Specific for lipid substrates, inactive towards water soluble inositol phosphates. Can also remove the 5-phosphate from 1D-myo-inositol 1,4,5-trisphosphate (Ins(1,4,5)P3). Plays an essential role in the primary cilium by …

**Summary**, from NCBI Gene [56623](https://www.ncbi.nlm.nih.gov/gene/56623):

> The protein encoded by this gene is an inositol 1,4,5-trisphosphate (InsP3) 5-phosphatase. InsP3 5-phosphatases hydrolyze Ins(1,4,5)P3, which mobilizes intracellular calcium and acts as a second messenger mediating cell responses to various stimulation. Studies of the mouse counterpart suggest that this protein may hydrolyze phosphatidylinositol 3,4,5-trisphosphate and phosphatidylinositol 3,5-bisphosphate on the cytoplasmic Golgi membrane and thereby regulate Golgi-vesicular trafficking. …

**Accessions** — [HGNC:21474](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21474) · Entrez [56623](https://www.ncbi.nlm.nih.gov/gene/56623) · UniProt [Q9NRR6](https://www.uniprot.org/uniprotkb/Q9NRR6) · Ensembl [ENSG00000148384](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148384)

## Data

Gene col 7276: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7276); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7276, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7276]; `tensor/DDL_lfc|DDL_z.npy` [7276]; `embed/gene_vectors.npy` [7276]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7276 or target_col == 7276). Every well: [[INPP5E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INPP5E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
