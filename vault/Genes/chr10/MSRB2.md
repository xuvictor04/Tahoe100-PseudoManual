---
symbol: "MSRB2"
type: "gene"
col: 7285
ensembl_id: "ENSG00000148450"
name: "methionine sulfoxide reductase B2"
location: "10p12.2"
module: 12
arm: "+"
pooled_cpm: 5.74
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MSRB2

*methionine sulfoxide reductase B2* — 10p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.87× (z +9.4, q 2e-18, up in 25 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.45× (z +4.7, q 4e-04, up in 16 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.333× (z -9.9, q 3e-20, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS33]] (+0.68, fdr 7e-06), [[DECR2]] (+0.66, fdr 7e-06), [[PNPLA4]] (+0.65, fdr 7e-06); moves opposite to [[RBM14-RBM4]] (-0.57, fdr 1e-05), [[BCAP31]] (-0.56, fdr 1e-05), [[ODF2]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7285.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.87×** | +9.4 | 2e-18 | 25/28 (HEC-1-A, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +4.8 | 4e-04 | 8/18 (A-172, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +4.7 | 4e-04 | 16/47 (AsPC-1, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +4.7 | 4e-04 | 7/11 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.97×** | +4.3 | 0.002 | 11/30 (HEC-1-A, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.005 | 12/46 (A498, A-172, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.4 | 0.050 | 11/41 (SW 900, A-172, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.66×** | +3.2 | 0.084 | 8/40 (LS 180, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.42× | +3.2 | 0.10 | 12/31 (HOP62, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7285.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.333×** | -9.9 | 3e-20 | 37/46 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.373×** | -8.8 | 3e-16 | 41/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.418×** | -7.8 | 1e-12 | 27/42 (LS 180, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.430×** | -7.6 | 5e-12 | 33/45 (LS 180, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.527×** | -5.8 | 1e-06 | 26/47 (KATO III, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.588×** | -4.5 | 7e-04 | 16/43 (HepG2/C3A, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.383×** | -4.3 | 0.001 | 19/40 (LS 180, HepG2/C3A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.390×** | -4.2 | 0.002 | 12/42 (LS 180, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.701×** | -3.2 | 0.084 | 16/46 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.779×** | -3.2 | 0.084 | 16/41 (LS 180, LoVo, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.706×** | -3.1 | 0.090 | 11/46 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.714× | -3.0 | 0.12 | 13/46 (RPMI-7951, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7285. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 16.0 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.116× (z -11.7) |
| [[A549 (line)]] | wt | 4.48 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0764× (z -9.6) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.5 µM 0.103× (z -8.5) |
| [[A-172 (line)]] | wt | 10.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.167× (z -9.2) |
| [[HT-29 (line)]] | alt | 7.12 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0506× (z -12.0) |
| [[KATO III (line)]] | alt | 14.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.176× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 4.38 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0684× (z -9.3) |
| [[SW480 (line)]] | alt | 5.64 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.159× (z -9.4) |
| [[A-427 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7285), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS33]] | +0.68 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[DECR2]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[PNPLA4]] | +0.65 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[PPP4R2]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[REPIN1]] | +0.62 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[FUNDC1]] | +0.61 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[ZNF428]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[SNAPIN]] | +0.60 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[SDSL]] | +0.59 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.58 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[COMMD3]] | +0.58 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[TAB2]] | +0.58 | +0.42 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM14-RBM4]] | -0.57 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[BCAP31]] | -0.56 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[ODF2]] | -0.56 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[NFATC2IP]] | -0.56 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[TPD52L2]] | -0.54 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[NPIPB11]] | -0.54 | -0.23 / -0.67 | both halves | 5e-04 |  |
| [[CORO7]] | -0.54 | -0.63 / -0.40 | both halves | 5e-05 |  |
| [[SMG1P6]] | -0.53 | -0.34 / -0.71 | both halves | 1e-04 |  |
| [[PMPCA]] | -0.53 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[RECQL]] | -0.53 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[NTAQ1]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ZNF731P]] | -0.52 | -0.53 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.508). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-31.4, 2.7); signed map (5.6, -21.3). **Vector** length 48.4, 6.37% of its response variance represented; |z| ≥ 3 in 835 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.9 | +4.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +0.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +9.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +3.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -8.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.1 | -7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -1.9 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -9.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.7 | -3.2 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | -2.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Tirabrutinib (drug)]] 0.05 µM |  | -0.9 | -1.3 |
|  | [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | -0.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | methionine sulfoxide reductase B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.2 — chr10:23,095,579-23,122,013 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PILB, CGI-131, CBS1, CBS-1; previously MSRB |
| Gene groups (HGNC) | Methionine sulfoxide reductases |
| Hallmark sets | COAGULATION |
| Reactome | 1 pathways, smallest: Protein repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3D2](https://www.uniprot.org/uniprotkb/Q9Y3D2) (Methionine-R-sulfoxide reductase B2, mitochondrial):

> Methionine-sulfoxide reductase that specifically reduces methionine (R)-sulfoxide back to methionine. While in many cases, methionine oxidation is the result of random oxidation following oxidative stress, methionine oxidation is also a post-translational modification that takes place on specific residue. Upon oxidative stress, may play a role in the preservation of mitochondrial integrity by decreasing the intracellular reactive oxygen species build-up through its scavenging role, hence …

**Summary**, from NCBI Gene [22921](https://www.ncbi.nlm.nih.gov/gene/22921):

> Predicted to enable actin binding activity; peptide-methionine (R)-S-oxide reductase activity; and zinc ion binding activity. Predicted to be involved in actin filament polymerization and protein repair. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17061](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17061) · Entrez [22921](https://www.ncbi.nlm.nih.gov/gene/22921) · UniProt [Q9Y3D2](https://www.uniprot.org/uniprotkb/Q9Y3D2) · Ensembl [ENSG00000148450](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148450)

## Data

Gene col 7285: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7285); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7285, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7285]; `tensor/DDL_lfc|DDL_z.npy` [7285]; `embed/gene_vectors.npy` [7285]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7285 or target_col == 7285). Every well: [[MSRB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSRB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
