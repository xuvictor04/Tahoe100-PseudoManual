---
symbol: "AATK"
type: "gene"
col: 11186
ensembl_id: "ENSG00000181409"
name: "lemur tail kinase 1"
location: "17q25.3"
module: 102
arm: "+"
pooled_cpm: 6.09
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# AATK

*lemur tail kinase 1* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.52× (z +20.2, q 0e+00, up in 6 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 3.44× (z +15.2, q 0e+00, up in 34 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.630× (z -5.7, q 6e-06, down in 19 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNQ1]] (+0.73, fdr 7e-06), [[ELAVL3]] (+0.59, fdr 1e-05), [[PAX5]] (+0.58, fdr 1e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HCN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11186.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.52×** | +20.2 | 0e+00 | 6/10 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.44×** | +15.2 | 0e+00 | 34/45 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.29×** | +14.6 | 0e+00 | 18/27 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +13.9 | 9e-42 | 25/38 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.20×** | +13.2 | 8e-38 | 11/14 (HOP62, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +10.0 | 2e-21 | 20/40 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +7.8 | 5e-13 | 26/45 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +7.7 | 1e-12 | 25/45 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.005 | 13/43 (SK-MEL-2, J82, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.040 | 1/45 (NCI-H2347) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.3 | 0.047 | 5/33 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.068 | 4/45 (HOP62, SW480, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.42× | +3.0 | 0.10 | 4/33 (A-172, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11186.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.630×** | -5.7 | 6e-06 | 19/44 (CHP-212, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.710×** | -4.3 | 0.006 | 16/45 (HT-29, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.736×** | -3.8 | 0.027 | 14/44 (MIA PaCa-2, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11186. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 5.56 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 39.0× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 9.67× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 33.9 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0950× (z -12.7) |
| [[A-427 (line)]] | wt | 16.2 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0678× (z -15.4) |
| [[AN3 CA (line)]] | alt | 28.4 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0782× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.0970× (z -8.8) |
| [[KATO III (line)]] | alt | 16.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 17.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.198× (z -8.5) |
| [[SW480 (line)]] | alt | 4.48 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 3.48 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0921× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 9.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 4.27 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 17.9× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 4.99 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.79× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 3.75 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.7× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 6.34 | 0 | 1 | — | [[LJI308 (drug)]] 0.05 µM 0.0938× (z -9.0) |
| [[SW 900 (line)]] | alt | 5.28 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0647× (z -9.4) |
| [[SW1417 (line)]] | alt | 6.72 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.9× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11186), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNQ1]] | +0.73 | +0.70 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[ELAVL3]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[PAX5]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 | same gene group |
| [[LINC02580]] | +0.58 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[KCNQ2]] | +0.58 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[CFAP92]] | +0.56 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[PPM1N]] | +0.55 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[CAPN12]] | +0.54 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[RAP1GAP]] | +0.54 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[EFNA2]] | +0.54 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[CDH23]] | +0.54 | +0.53 / +0.53 | both halves | 1e-05 | same gene group |
| [[CACNG2]] | +0.53 | +0.49 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HCN1]] | B | HCN1 activity weakens AATK's drug response | lines that do not express HCN1 (36) vs lines expressing it (9) | (z diff -2.52); strongest at Dinaciclib 0.05 µM: 2.68x vs 0.49x (z diff -7.3) | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, APOH, GCG; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CBFA2T3]] | B | CBFA2T3 activity raises AATK's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 1.73× lower at baseline in the lines without CBFA2T3 | 0.022 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[HCN1]] | B | HCN1 activity raises AATK's level | lines that do not express HCN1 (37) vs lines expressing it (13) | 1.73× lower at baseline in the lines without HCN1 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, APOH, GCG; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.421). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.7, 36.2); signed map (24.9, 18.8). **Vector** length 63.9, 9.17% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +20.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +14.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +10.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +13.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +2.0 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +0.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -1.2 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -1.4 | -1.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -1.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | lemur tail kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,110,487-81,166,221 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AATYK, KIAA0641, LMR1, AATYK1, PPP1R77; previously AATK |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; MicroRNA protein coding host genes; Lemur tail kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZMQ8](https://www.uniprot.org/uniprotkb/Q6ZMQ8) (Serine/threonine-protein kinase LMTK1):

> May be involved in neuronal differentiation.

**Summary**, from NCBI Gene [9625](https://www.ncbi.nlm.nih.gov/gene/9625):

> The protein encoded by this gene contains a tyrosine kinase domain at the N-terminus and a proline-rich domain at the C-terminus. This gene is induced during apoptosis, and expression of this gene may be a necessary pre-requisite for the induction of growth arrest and/or apoptosis of myeloid precursor cells. This gene has been shown to produce neuronal differentiation in a neuroblastoma cell line. Two transcript variants encoding different isoforms have been found for this gene. [provided by …

**Accessions** — [HGNC:21](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21) · Entrez [9625](https://www.ncbi.nlm.nih.gov/gene/9625) · UniProt [Q6ZMQ8](https://www.uniprot.org/uniprotkb/Q6ZMQ8) · Ensembl [ENSG00000181409](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181409)

## Data

Gene col 11186: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11186); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11186, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11186]; `tensor/DDL_lfc|DDL_z.npy` [11186]; `embed/gene_vectors.npy` [11186]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11186 or target_col == 11186). Every well: [[AATK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AATK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
