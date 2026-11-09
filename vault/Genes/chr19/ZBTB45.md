---
symbol: "ZBTB45"
type: "gene"
col: 4081
ensembl_id: "ENSG00000119574"
name: "zinc finger and BTB domain containing 45"
location: "19q13.43"
module: 7
arm: "+"
pooled_cpm: 3.68
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ZBTB45

*zinc finger and BTB domain containing 45* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.68× (z +5.8, q 4e-06, up in 1 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.59× (z +3.8, q 0.025, up in 3 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.426× (z -9.8, q 4e-20, down in 28 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM15B]] (+0.75, fdr 7e-06), [[HPS6]] (+0.73, fdr 7e-06), [[FIZ1]] (+0.70, fdr 7e-06); moves opposite to [[P4HA1]] (-0.60, fdr 1e-05), [[TMEM14B]] (-0.60, fdr 1e-05), [[KIAA1958]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4081.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +5.8 | 4e-06 | 1/6 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +4.4 | 0.003 | 6/20 (HEC-1-A, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.59×** | +3.8 | 0.025 | 3/22 (LS 180, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.028 | 6/43 (Panc 03.27, HT-29, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +3.4 | 0.057 | 2/7 (A498, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.057 | 5/44 (AsPC-1, SW480, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.057 | 14/41 (LoVo, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.3 | 0.057 | 6/22 (LS 180, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.31× | +3.1 | 0.11 | 2/20 (NCI-H2347, Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.44× | +3.0 | 0.14 | 1/36 (LOX-IMVI) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4081.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.426×** | -9.8 | 4e-20 | 28/45 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.543×** | -7.0 | 5e-10 | 24/44 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.569×** | -6.5 | 2e-08 | 19/45 (COLO 205, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.577×** | -6.3 | 3e-08 | 17/33 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.586×** | -6.2 | 9e-08 | 18/45 (PANC-1, KATO III, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.624×** | -5.2 | 2e-05 | 10/32 (J82, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.662×** | -4.7 | 2e-04 | 15/43 (LOX-IMVI, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.654×** | -4.7 | 2e-04 | 13/36 (LOX-IMVI, KATO III, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.668×** | -4.6 | 2e-04 | 10/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.699×** | -4.1 | 0.002 | 13/45 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.709×** | -3.9 | 0.004 | 14/43 (RPMI-7951, HEC-1-A, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.724×** | -3.7 | 0.009 | 9/45 (AN3 CA, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.725×** | -3.7 | 0.009 | 12/43 (A-172, BT-474, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.808×** | -3.4 | 0.023 | 9/37 (BT-474, A-172, …) | top dose only | composition shift |
| [[8-Hydroxyquinoline (drug)]] 0.05 µM |  | **0.754×** | -3.2 | 0.045 | 4/43 (NCI-H2030, PANC-1, …) | inconsistent across doses | position effect removed |
| [[BAY1125976 (drug)]] 0.05 µM |  | **0.752×** | -3.1 | 0.069 | 5/44 (HCT15, H4, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.764×** | -3.1 | 0.069 | 8/44 (NCI-H23, HT-29, …) | two highest doses | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4081. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 3.74 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0828× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 3.31 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0676× (z -8.8) |
| [[HOP62 (line)]] | alt | 2.92 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0857× (z -9.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 3.86 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0857× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 2.87 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0584× (z -9.5) |
| [[A-172 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4081), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM15B]] | +0.75 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[HPS6]] | +0.73 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[FIZ1]] | +0.70 | +0.67 / +0.65 | both halves | 7e-06 | same gene group |
| [[MOCS3]] | +0.70 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[FEM1A]] | +0.69 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.69 | +0.58 / +0.64 | both halves | 8e-06 | same gene group |
| [[ZNF747]] | +0.68 | +0.59 / +0.59 | both halves | 7e-06 | same gene group |
| [[CENPBD1P]] | +0.68 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[GTF3C4]] | +0.68 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[DDX28]] | +0.67 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[TACO1]] | +0.67 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[RRN3]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P4HA1]] | -0.60 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[TMEM14B]] | -0.60 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[KIAA1958]] | -0.60 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[PIK3C2A]] | -0.59 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[NGLY1]] | -0.56 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[SNX25]] | -0.55 | -0.56 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.732). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-38.2, 11.1); signed map (-3.3, -27.2). **Vector** length 41.1, 4.09% of its response variance represented; |z| ≥ 3 in 955 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +3.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +0.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.4 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +3.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.1 | +1.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.1 | +2.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -9.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.9 | -6.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.7 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 45 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.43 — chr19:58,513,530-58,538,911 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14486; previously ZNF499 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96K62](https://www.uniprot.org/uniprotkb/Q96K62) (Zinc finger and BTB domain-containing protein 45):

> May be involved in transcriptional regulation (Probable). In the central nervous system, may play a role in glial cell differentiation (By similarity).

**Summary**, from NCBI Gene [84878](https://www.ncbi.nlm.nih.gov/gene/84878):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in negative regulation of transcription by RNA polymerase II; regulation of cytokine production; and regulation of immune system process. Predicted to be located in nucleus. Predicted to be active in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23715](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23715) · Entrez [84878](https://www.ncbi.nlm.nih.gov/gene/84878) · UniProt [Q96K62](https://www.uniprot.org/uniprotkb/Q96K62) · Ensembl [ENSG00000119574](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119574)

## Data

Gene col 4081: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4081); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4081, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4081]; `tensor/DDL_lfc|DDL_z.npy` [4081]; `embed/gene_vectors.npy` [4081]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4081 or target_col == 4081). Every well: [[ZBTB45 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB45.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
