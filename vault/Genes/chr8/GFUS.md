---
symbol: "GFUS"
type: "gene"
col: 2470
ensembl_id: "ENSG00000104522"
name: "GDP-L-fucose synthase"
location: "8q24.3"
module: 12
arm: "+"
pooled_cpm: 10.01
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# GFUS

*GDP-L-fucose synthase* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.35× (z +14.4, q 4e-44, up in 31 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.24× (z +7.9, q 4e-13, up in 33 of 39 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXL6]] (+0.65, fdr 1e-05), [[CREB3]] (+0.63, fdr 4e-05), [[NOC4L]] (+0.61, fdr 1e-05); moves opposite to [[INTS9]] (-0.49, fdr 0.003, ⚠ one half only (not replicated)), [[NDUFA4]] (-0.47, fdr 3e-04), [[UBL5]] (-0.46, fdr 7e-04), [[HINT1]] (-0.45, fdr 6e-04).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2470.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.35×** | +14.4 | 4e-44 | 31/31 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.77×** | +12.5 | 4e-33 | 15/16 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.85×** | +8.5 | 4e-15 | 30/42 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.24×** | +7.9 | 4e-13 | 33/39 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.75×** | +7.4 | 2e-11 | 21/24 (LS 180, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **2.06×** | +7.1 | 1e-10 | 32/39 (A549, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.94×** | +6.4 | 9e-09 | 36/46 (SW480, HCT15, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.90×** | +6.0 | 1e-07 | 26/45 (PANC-1, Panc 03.27, …) | rises with dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +5.4 | 4e-06 | 19/35 (SW1417, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.46×** | +3.7 | 0.012 | 17/46 (SW480, PANC-1, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.47×** | +3.6 | 0.015 | 17/35 (J82, LS 180, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **2.11×** | +3.6 | 0.015 | 12/38 (LOX-IMVI, RKO, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.72×** | +3.2 | 0.052 | 7/44 (KATO III, C32, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.052 | 10/44 (hTERT-HPNE, NCI-H2030, …) | all doses, flat |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.39×** | +3.2 | 0.052 | 12/44 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.67×** | +3.1 | 0.077 | 7/37 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.084 | 9/43 (HS-578T, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2470.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.685× | -3.7 | 0.12 | 17/47 (HT-29, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.732× | -3.1 | 0.41 | 6/48 (LOX-IMVI, HS-578T, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.733× | -3.0 | 0.41 | 5/47 (C-33 A, A-172, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2470. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.06 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.09× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 9.53 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.77× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 27.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 9.90 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.70× (z +10.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 9.14 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +8.6) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[LS 180 (line)]] | wt | 13.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.04× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 3.34 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.75× (z +8.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 13.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +8.9) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[SW480 (line)]] | alt | 6.43 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.73× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2470), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXL6]] | +0.65 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[CREB3]] | +0.63 | +0.71 / +0.41 | both halves | 4e-05 |  |
| [[NOC4L]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[IMP4]] | +0.59 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[STK16]] | +0.57 | +0.67 / +0.36 | both halves | 9e-05 |  |
| [[GLRX2]] | +0.57 | +0.64 / +0.39 | both halves | 6e-05 |  |
| [[DXO]] | +0.56 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[NOL6]] | +0.55 | +0.60 / +0.39 | both halves | 5e-05 |  |
| [[GFER]] | +0.54 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[ACTR8]] | +0.54 | +0.62 / +0.33 | both halves | 1e-04 |  |
| [[SURF2]] | +0.54 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[NCDN]] | +0.54 | +0.57 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS9]] | -0.49 | -0.68 / -0.09 | ⚠ one half (not replicated) | 0.003 |  |
| [[NDUFA4]] | -0.47 | -0.53 / -0.26 | both halves | 3e-04 |  |
| [[UBL5]] | -0.46 | -0.63 / -0.20 | both halves | 7e-04 |  |
| [[MIF]] | -0.45 | -0.60 / -0.12 | ⚠ one half (not replicated) | 0.002 | pathway: HALLMARK_GLYCOLYSIS |
| [[HINT1]] | -0.45 | -0.53 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.425). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-32.5, 0.9); signed map (-6.7, -21.9). **Vector** length 57.6, 10.3% of its response variance represented; |z| ≥ 3 in 632 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +5.3 | +8.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +4.0 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +14.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +12.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +6.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +3.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +2.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +2.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.6 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -3.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.3 | -1.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | GDP-L-fucose synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,612,618-143,618,048 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FX, P35B, SDR4E1; previously TSTA3 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, GLYCOLYSIS |
| Reactome | 4 pathways, smallest: GDP-fucose biosynthesis; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13630](https://www.uniprot.org/uniprotkb/Q13630) (GDP-L-fucose synthase):

> Catalyzes the two-step NADP-dependent conversion of GDP-4-dehydro-6-deoxy-D-mannose to GDP-fucose, involving an epimerase and a reductase reaction.

**Summary**, from NCBI Gene [7264](https://www.ncbi.nlm.nih.gov/gene/7264):

> Tissue specific transplantation antigen P35B is a NADP(H)-binding protein. It catalyze the two-step epimerase and the reductase reactions in GDP-D-mannose metabolism, converting GDP-4-keto-6-D-deoxymannose to GDP-L-fucose. GDP-L-fucose is the substrate of several fucosyltransferases involved in the expression of many glycoconjugates, including blood group ABH antigens and developmental adhesion antigens. Mutations in this gene may cause leukocyte adhesion deficiency, type II. [provided by …

**Accessions** — [HGNC:12390](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12390) · Entrez [7264](https://www.ncbi.nlm.nih.gov/gene/7264) · UniProt [Q13630](https://www.uniprot.org/uniprotkb/Q13630) · Ensembl [ENSG00000104522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104522)

## Data

Gene col 2470: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2470); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2470, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2470]; `tensor/DDL_lfc|DDL_z.npy` [2470]; `embed/gene_vectors.npy` [2470]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2470 or target_col == 2470). Every well: [[GFUS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GFUS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
