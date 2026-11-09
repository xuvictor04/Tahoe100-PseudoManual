---
symbol: "LSM6"
type: "gene"
col: 8888
ensembl_id: "ENSG00000164167"
name: "LSM6 homolog, U6 small nuclear RNA and mRNA degradation associated"
location: "4q31.22"
module: 46
arm: "+"
pooled_cpm: 13.91
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# LSM6

*LSM6 homolog, U6 small nuclear RNA and mRNA degradation associated* — 4q31.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.97× (z +9.5, q 8e-19, up in 34 of 42 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +8.8, q 5e-16, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.536× (z -4.8, q 9e-04, down in 20 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GGA3]] (+0.64, fdr 1e-05), [[LATS1]] (+0.63, fdr 1e-05), [[WDR75]] (+0.62, fdr 7e-06); moves opposite to [[NUCB1]] (-0.56, fdr 2e-05), [[KHDRBS1]] (-0.52, fdr 4e-05), [[IDS]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8888.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +9.5 | 8e-19 | 34/42 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +8.8 | 5e-16 | 32/46 (BT-474, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +6.5 | 2e-08 | 25/46 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.48×** | +5.7 | 1e-06 | 18/41 (A549, CFPAC-1, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +5.2 | 3e-05 | 20/46 (MIA PaCa-2, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.36×** | +4.4 | 1e-03 | 18/48 (A-427, HS-578T, …) | top dose only |  |
| [[Cysteamine (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +4.4 | 1e-03 | 17/46 (NCI-H2347, RPMI-7951, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.33×** | +4.1 | 0.002 | 16/47 (HEC-1-A, H4, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +4.0 | 0.004 | 15/48 (LS 180, A498, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.20×** | +3.8 | 0.009 | 13/47 (NCI-H1792, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.29×** | +3.7 | 0.010 | 18/43 (NCI-H2347, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Esmolol (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.021 | 13/47 (HepG2/C3A, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.27×** | +3.5 | 0.021 | 15/48 (PANC-1, hTERT-HPNE, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | **1.26×** | +3.3 | 0.046 | 11/25 (KATO III, NCI-H2347, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.061 | 11/48 (NCI-H2347, SK-MEL-2, …) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8888.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.536×** | -4.8 | 9e-04 | 20/48 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.728×** | -4.7 | 9e-04 | 22/47 (BT-474, LoVo, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.589×** | -4.1 | 0.009 | 18/44 (HOP62, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -3.5 | 0.055 | 5/48 (A-172, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8888. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 9.99 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0871× (z -10.6) |
| [[Hs 766T (line)]] | wt | 8.13 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0952× (z -10.3) |
| [[SW48 (line)]] | wt | 13.1 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0787× (z -9.3) |
| [[A-172 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8888), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGA3]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[LATS1]] | +0.63 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[WDR75]] | +0.62 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[PKD2]] | +0.61 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[RNF146]] | +0.60 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[RBX1]] | +0.59 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[ATAD2B]] | +0.59 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[ACTR3B]] | +0.59 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[MTFMT]] | +0.58 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[OBI1]] | +0.58 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[UNK]] | +0.57 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[TRIM13]] | +0.57 | +0.39 / +0.54 | both halves | 5e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUCB1]] | -0.56 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[KHDRBS1]] | -0.52 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[IDS]] | -0.52 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[GNAI3]] | -0.52 | -0.68 / -0.31 | both halves | 2e-04 |  |
| [[CALU]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[RALY]] | -0.52 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[AZIN1]] | -0.52 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[MLF2]] | -0.51 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[TUBB3]] | -0.51 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[MYO7A]] | -0.50 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[NCKAP5L]] | -0.50 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[CAST]] | -0.49 | -0.47 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LSM6's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.447). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-8.0, 13.9); signed map (6.6, -5.4). **Vector** length 57.0, 8.62% of its response variance represented; |z| ≥ 3 in 648 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +9.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.1 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.4 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +4.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.4 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.2 | +1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.8 | -4.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.9 | -4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +2.7 |
|  | [[Auranofin (drug)]] 0.5 µM |  | -1.0 | -1.2 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.0 | -1.6 |
|  | [[Malotilate (drug)]] 0.05 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | LSM6 homolog, U6 small nuclear RNA and mRNA degradation associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.22 — chr4:146,175,703-146,200,000 (+) |
| Ensembl biotype | protein_coding |
| Also known as | YDR378C |
| Gene groups (HGNC) | LSm proteins |
| Reactome | 6 pathways, smallest: mRNA decay by 5' to 3' exoribonuclease; Deadenylation-dependent mRNA decay; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P62312](https://www.uniprot.org/uniprotkb/P62312) (U6 snRNA-associated Sm-like protein LSm6):

> Plays a role in pre-mRNA splicing as component of the U4/U6-U5 tri-snRNP complex that is involved in spliceosome assembly, and as component of the precatalytic spliceosome (spliceosome B complex). The heptameric LSM2-8 complex binds specifically to the 3'-terminal U-tract of U6 snRNA. Component of LSm protein complexes, which are involved in RNA processing and may function in a chaperone-like manner, facilitating the efficient association of RNA processing factors with their substrates. …

**Summary**, from NCBI Gene [11157](https://www.ncbi.nlm.nih.gov/gene/11157):

> Sm-like proteins were identified in a variety of organisms based on sequence homology with the Sm protein family (see SNRPD2; MIM 601061). Sm-like proteins contain the Sm sequence motif, which consists of 2 regions separated by a linker of variable length that folds as a loop. The Sm-like proteins are thought to form a stable heteromer present in tri-snRNP particles, which are important for pre-mRNA splicing.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:17017](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17017) · Entrez [11157](https://www.ncbi.nlm.nih.gov/gene/11157) · UniProt [P62312](https://www.uniprot.org/uniprotkb/P62312) · Ensembl [ENSG00000164167](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164167)

## Data

Gene col 8888: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8888); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8888, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8888]; `tensor/DDL_lfc|DDL_z.npy` [8888]; `embed/gene_vectors.npy` [8888]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8888 or target_col == 8888). Every well: [[LSM6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSM6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
