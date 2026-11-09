---
symbol: "PAFAH2"
type: "gene"
col: 8122
ensembl_id: "ENSG00000158006"
name: "platelet activating factor acetylhydrolase 2"
location: "1p36.11"
module: 16
arm: "+"
pooled_cpm: 7.36
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# PAFAH2

*platelet activating factor acetylhydrolase 2* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.36× (z +10.1, q 3e-21, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.548× (z -7.6, q 1e-11, down in 24 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF780A]] (+0.61, fdr 9e-06), [[ZNF776]] (+0.60, fdr 1e-05), [[HNRNPH2]] (+0.59, fdr 1e-05); moves opposite to [[GDI2]] (-0.57, fdr 1e-04), [[DONSON]] (-0.53, fdr 3e-05), [[CCDC168]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8122.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.36×** | +10.1 | 3e-21 | 37/46 (SW480, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.97×** | +8.9 | 1e-16 | 26/48 (LS 180, A-427, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.79×** | +7.0 | 3e-10 | 21/42 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +6.8 | 1e-09 | 23/41 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +6.3 | 3e-08 | 21/43 (RKO, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +6.2 | 4e-08 | 18/47 (LS 180, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 2e-04 | 16/45 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.002 | 9/47 (AsPC-1, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.058 | 3/43 (A549, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **1.28×** | +3.2 | 0.071 | 7/38 (LS 180, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.19× | +3.2 | 0.075 | 3/46 (hTERT-HPNE, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.26× | +3.1 | 0.11 | 9/41 (NCI-H2030, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8122.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.548×** | -7.6 | 1e-11 | 24/43 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.735×** | -5.7 | 3e-06 | 20/42 (NCI-H2347, PANC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -5.5 | 6e-06 | 18/40 (SK-MEL-2, LS 180, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.676×** | -5.0 | 1e-04 | 18/38 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.786× | -3.1 | 0.25 | 5/47 (J82, BT-474, …) | rises with dose | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8122. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 4.25 | 0 | 2 | — | [[Neratinib (drug)]] 0.05 µM 0.0533× (z -8.8) |
| [[A-427 (line)]] | wt | 12.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -11.7) |
| [[BT-474 (line)]] | alt | 6.48 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0943× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +20.1) | — |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0969× (z -8.5) |
| [[HOP62 (line)]] | alt | 6.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +16.4) | — |
| [[Hs 766T (line)]] | wt | 8.56 | 0 | 1 | — | [[ULK-101 (drug)]] 0.5 µM 0.0693× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 8.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +12.8) | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 5.11 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -10.8) |
| [[SW480 (line)]] | alt | 7.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +9.8) | — |
| [[A-172 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8122), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF780A]] | +0.61 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[ZNF776]] | +0.60 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[HNRNPH2]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[ATXN7L3B]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[TMEM254]] | +0.58 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[VPS11]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[ZNF268]] | +0.55 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[ZNF155]] | +0.55 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[MRFAP1L1]] | +0.55 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ZBTB40]] | +0.54 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[SETD2]] | +0.54 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[GOPC]] | +0.54 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDI2]] | -0.57 | -0.71 / -0.33 | both halves | 1e-04 |  |
| [[DONSON]] | -0.53 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[CCDC168]] | -0.51 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[HEATR5A]] | -0.49 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[GLS]] | -0.48 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[METTL21A]] | -0.46 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[NDEL1]] | -0.46 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[SELENOI]] | -0.45 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[CCNYL1]] | -0.45 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[FBXO34]] | -0.45 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[RARS2]] | -0.45 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[TPTEP2-CSNK1E]] | -0.45 | -0.33 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PAFAH2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-35.5, 16.3); signed map (3.2, -28.4). **Vector** length 74.7, 12.8% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.1 | +10.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +6.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +6.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.9 | +6.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +1.2 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -7.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -5.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.3 | -5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Pimozide (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | platelet activating factor acetylhydrolase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:25,959,767-25,998,117 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSD-PLA2 |
| Gene groups (HGNC) | Acyltransferases |
| Reactome | 2 pathways, smallest: Platelet homeostasis; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99487](https://www.uniprot.org/uniprotkb/Q99487) (Platelet-activating factor acetylhydrolase 2, cytoplasmic):

> Catalyzes the hydrolyze of the acetyl group at the sn-2 position of platelet-activating factor (PAF) and its analogs, leading to their inactivation. Hydrolyzes propionyl and butyroyl moieties approximately half as effectively as PAF (By similarity). Also catalyzes transacetylation of the acetyl group from platelet-activating factor (PAF) to lysoplasmalogen and to sphingosine, producing plasmalogen analogs of PAF and N-acetylsphingosine (C2-ceramide) respectively. Has a marked selectivity for …

**Summary**, from NCBI Gene [5051](https://www.ncbi.nlm.nih.gov/gene/5051):

> This gene encodes platelet-activating factor acetylhydrolase isoform 2, a single-subunit intracellular enzyme that catalyzes the removal of the acetyl group at the SN-2 position of platelet-activating factor (identified as 1-O-alkyl-2-acetyl-sn-glyceryl-3-phosphorylcholine). However, this lipase exhibits a broader substrate specificity than simply platelet activating factor. Two other isoforms of intracellular platelet-activating factor acetylhydrolase exist, and both are multi-subunit enzymes. …

**Accessions** — [HGNC:8579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8579) · Entrez [5051](https://www.ncbi.nlm.nih.gov/gene/5051) · UniProt [Q99487](https://www.uniprot.org/uniprotkb/Q99487) · Ensembl [ENSG00000158006](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158006)

## Data

Gene col 8122: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8122); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8122, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8122]; `tensor/DDL_lfc|DDL_z.npy` [8122]; `embed/gene_vectors.npy` [8122]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8122 or target_col == 8122). Every well: [[PAFAH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAFAH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
