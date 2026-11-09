---
symbol: "SNAPIN"
type: "gene"
col: 6770
ensembl_id: "ENSG00000143553"
name: "SNAP associated protein"
location: "1q21.3"
module: 12
arm: "+"
pooled_cpm: 8.3
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# SNAPIN

*SNAP associated protein* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.37× (z +7.2, q 4e-10, up in 27 of 30 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.309× (z -9.7, q 1e-19, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RP9]] (+0.73, fdr 7e-06), [[ASB8]] (+0.72, fdr 7e-06), [[MRPL40]] (+0.71, fdr 7e-06); moves opposite to [[PRDM15]] (-0.68, fdr 1e-05), [[PRDM10]] (-0.67, fdr 1e-05), [[CERS2]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6770.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +7.2 | 4e-10 | 27/30 (A498, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +5.5 | 1e-05 | 15/16 (PANC-1, A498, …) | two highest doses | cell-cycle shift (explains ~21% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.58×** | +3.8 | 0.027 | 18/38 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.47× | +3.2 | 0.16 | 13/46 (A-427, A498, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.47× | +3.2 | 0.16 | 15/45 (SNU-423, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6770.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.309×** | -9.7 | 1e-19 | 44/47 (RPMI-7951, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.321×** | -9.4 | 1e-18 | 44/46 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.373×** | -8.2 | 6e-14 | 40/46 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.388×** | -7.8 | 6e-13 | 37/44 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.509×** | -5.6 | 2e-06 | 27/46 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.329×** | -4.6 | 3e-04 | 23/45 (NCI-H1792, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.674×** | -4.6 | 3e-04 | 25/43 (RKO, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.383×** | -4.0 | 0.005 | 23/42 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.653×** | -3.5 | 0.027 | 17/47 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.686×** | -3.1 | 0.092 | 15/47 (SW 900, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.766×** | -3.1 | 0.092 | 14/43 (SW 900, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.687×** | -3.1 | 0.092 | 11/47 (KATO III, NCI-H2030, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.690×** | -3.1 | 0.096 | 15/44 (SNU-423, NCI-H23, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6770. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.127× (z -11.8) |
| [[HOP62 (line)]] | alt | 5.87 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0853× (z -10.2) |
| [[Hs 766T (line)]] | wt | 9.59 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0917× (z -9.9) |
| [[PANC-1 (line)]] | alt | 10.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.206× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.212× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 7.56 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0348× (z -11.8) |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.116× (z -9.9) |
| [[SW480 (line)]] | alt | 7.51 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.153× (z -10.0) |
| [[A549 (line)]] | wt | 8.55 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0527× (z -13.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 3.81 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0465× (z -10.1) |
| [[BT-474 (line)]] | alt | 8.12 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0936× (z -8.8) |
| [[COLO 205 (line)]] | alt | 8.07 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0481× (z -9.7) |
| [[HS-578T (line)]] | alt | 6.70 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0301× (z -14.4) |
| [[LOX-IMVI (line)]] | wt | 5.05 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0503× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 8.36 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.151× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 9.30 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -8.9) |
| [[A-172 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6770), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RP9]] | +0.73 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[ASB8]] | +0.72 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[MRPL40]] | +0.71 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[MRPS33]] | +0.70 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[NUDT12]] | +0.69 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[FIBP]] | +0.68 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[DNAL4]] | +0.68 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[ELOF1]] | +0.68 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[EBAG9]] | +0.68 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[SURF2]] | +0.68 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[CREB3]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[PITPNA-AS1]] | +0.67 | +0.53 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM15]] | -0.68 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[PRDM10]] | -0.67 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[CERS2]] | -0.66 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[TMEM11-DT]] | -0.65 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[LY6G5B]] | -0.63 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[HCFC1]] | -0.62 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[SAP30L-AS1]] | -0.62 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[NAF1]] | -0.62 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[SENP3]] | -0.61 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[RBBP4]] | -0.61 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[ZNF718]] | -0.61 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[CAPN15]] | -0.60 | -0.52 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.728). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-31.9, 1.4); signed map (-16.1, -7.6). **Vector** length 61.2, 11.5% of its response variance represented; |z| ≥ 3 in 707 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.8 | +3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | -0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +2.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +3.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +2.2 |
|  | [[Flutamide (drug)]] 5 µM |  | +0.9 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.6 | -9.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.4 | -8.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.8 | -9.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.7 | -7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -0.7 |
|  | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.8 |
|  | [[Almonertinib (mesylate) (drug)]] 0.05 µM |  | -0.8 | -1.1 |
|  | [[Ivermectin (drug)]] 5 µM |  | -0.8 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | SNAP associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:153,658,703-153,661,852 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BLOC1S7, BORCS3; previously SNAPAP |
| Gene groups (HGNC) | Biogenesis of lysosomal organelles complex 1 subunits; BLOC-1 related complex subunits |
| Reactome | 4 pathways, smallest: Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [O95295](https://www.uniprot.org/uniprotkb/O95295) (SNARE-associated protein Snapin):

> Component of the BLOC-1 complex, a complex that is required for normal biogenesis of lysosome-related organelles (LRO), such as platelet dense granules and melanosomes. In concert with the AP-3 complex, the BLOC-1 complex is required to target membrane protein cargos into vesicles assembled at cell bodies for delivery into neurites and nerve terminals. The BLOC-1 complex, in association with SNARE proteins, is also proposed to be involved in neurite extension. Plays a role in intracellular …

**Summary**, from NCBI Gene [23557](https://www.ncbi.nlm.nih.gov/gene/23557):

> The protein encoded by this gene is a coiled-coil-forming protein that associates with the SNARE (soluble N-ethylmaleimide-sensitive fusion protein attachment protein receptor) complex of proteins and the BLOC-1 (biogenesis of lysosome-related organelles) complex. Biochemical studies have identified additional binding partners. As part of the SNARE complex, it is required for vesicle docking and fusion and regulates neurotransmitter release. The BLOC-1 complex is required for the biogenesis of …

**Accessions** — [HGNC:17145](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17145) · Entrez [23557](https://www.ncbi.nlm.nih.gov/gene/23557) · UniProt [O95295](https://www.uniprot.org/uniprotkb/O95295) · Ensembl [ENSG00000143553](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143553)

## Data

Gene col 6770: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6770); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6770, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6770]; `tensor/DDL_lfc|DDL_z.npy` [6770]; `embed/gene_vectors.npy` [6770]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6770 or target_col == 6770). Every well: [[SNAPIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNAPIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
