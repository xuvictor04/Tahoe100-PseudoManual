---
symbol: "GTF2H5"
type: "gene"
col: 15707
ensembl_id: "ENSG00000272047"
name: "general transcription factor IIH subunit 5"
location: "6q25.3"
module: 12
arm: "+"
pooled_cpm: 17.94
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 9
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# GTF2H5

*general transcription factor IIH subunit 5* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.97× (z +8.2, q 1e-13, up in 31 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.38× (z +3.4, q 0.086, up in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1792 6.79×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.417× (z -6.6, q 2e-08, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL57]] (+0.72, fdr 3e-05), [[MTRES1]] (+0.71, fdr 7e-06), [[PITPNA-AS1]] (+0.67, fdr 3e-05); moves opposite to [[HCFC1]] (-0.61, fdr 5e-05), [[PGRMC1]] (-0.61, fdr 1e-05), [[IL18BP]] (-0.57, fdr 8e-04, ⚠ one half only (not replicated)), [[STX16]] (-0.54, fdr 7e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15707.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1792 6.79×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.97×** | +8.2 | 1e-13 | 31/37 (LOX-IMVI, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +7.3 | 1e-10 | 22/28 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.7 | 0.048 | 25/44 (NCI-H1573, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.086 | 26/48 (NCI-H1573, Hs 766T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 5 µM |  | 1.57× | +3.3 | 0.12 | 26/47 (CFPAC-1, LS 180, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.56× | +3.1 | 0.17 | 16/33 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15707.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.417×** | -6.6 | 2e-08 | 43/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.459×** | -5.9 | 9e-07 | 44/47 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.523×** | -4.9 | 1e-04 | 31/47 (KATO III, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.634×** | -4.9 | 1e-04 | 30/47 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.543×** | -4.6 | 4e-04 | 32/47 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.324×** | -4.5 | 8e-04 | 34/45 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.596×** | -3.9 | 0.007 | 26/46 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.420×** | -3.4 | 0.042 | 23/48 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.655×** | -3.2 | 0.081 | 20/47 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 0.670× | -3.0 | 0.11 | 23/47 (BT-474, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.671× | -3.0 | 0.11 | 22/47 (LS 180, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.655× | -3.0 | 0.11 | 20/48 (SW48, H4, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.650× | -3.0 | 0.11 | 19/47 (SK-MEL-2, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15707. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.8 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -9.2) |
| [[SW480 (line)]] | alt | 23.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -9.0) |
| [[BT-474 (line)]] | alt | 9.97 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0835× (z -9.3) |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0546× (z -9.9) |
| [[LoVo (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.176× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 13.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.79× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -8.9) |
| [[A-172 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15707), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 12 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL57]] | +0.72 | +0.45 / +0.79 | both halves | 3e-05 |  |
| [[MTRES1]] | +0.71 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[PITPNA-AS1]] | +0.67 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[DMAC1]] | +0.67 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[PPP4R2]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[MTLN]] ⚠ | +0.66 | +0.47 / +0.67 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NDUFA8]] | +0.65 | +0.39 / +0.73 | both halves | 5e-05 |  |
| [[TRAPPC5]] | +0.65 | +0.34 / +0.73 | both halves | 1e-04 |  |
| [[FAM133B]] | +0.62 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[MRPS33]] | +0.62 | +0.54 / +0.69 | both halves | 1e-05 | STRING 407 |
| [[TARS2]] | +0.62 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[EBAG9]] | +0.61 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[LLPH]] | +0.61 | +0.57 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCFC1]] | -0.61 | -0.39 / -0.66 | both halves | 5e-05 | pathway: Epigenetic regulation of gene expression |
| [[PGRMC1]] | -0.61 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[IL18BP]] | -0.57 | -0.19 / -0.63 | ⚠ one half (not replicated) | 8e-04 |  |
| [[STX16]] | -0.54 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[SERPINH1]] | -0.54 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[NUCB1]] | -0.53 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[BCL2L2]] | -0.53 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[NECAB3]] | -0.53 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[SMG1P6]] | -0.53 | -0.23 / -0.60 | both halves | 5e-04 |  |
| [[CMPK1]] | -0.52 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[RPN1]] | -0.52 | -0.38 / -0.61 | both halves | 7e-05 |  |
| [[NCSTN]] | -0.52 | -0.26 / -0.55 | both halves | 4e-04 |  |
| [[CERS2]] | -0.52 | -0.34 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.578). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-47.2, -10.5); signed map (-15.8, -10.7). **Vector** length 58.7, 12.8% of its response variance represented; |z| ≥ 3 in 639 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.8 | +3.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | -0.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.3 | -4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.2 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.1 | +0.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.3 | -3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIH subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:158,168,350-158,199,344 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30544, bA120J8.2, TTD-A, TFB5, TFIIH, TTDA; previously C6orf175, TTD |
| Gene groups (HGNC) | Nucleotide excision repair; General transcription factor IIH complex subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 42 pathways, smallest: RNA Pol II CTD phosphorylation and interaction with CE during HIV infection; RNA Pol II CTD phosphorylation and interaction with CE; mRNA Capping |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZYL4](https://www.uniprot.org/uniprotkb/Q6ZYL4) (General transcription factor IIH subunit 5):

> Component of the general transcription and DNA repair factor IIH (TFIIH) core complex, which is involved in general and transcription-coupled nucleotide excision repair (NER) of damaged DNA and, when complexed to CAK, in RNA transcription by RNA polymerase II. In NER, TFIIH acts by opening DNA around the lesion to allow the excision of the damaged oligonucleotide and its replacement by a new DNA fragment. In transcription, TFIIH has an essential role in transcription initiation. When the …

**Summary**, from NCBI Gene [404672](https://www.ncbi.nlm.nih.gov/gene/404672):

> This gene encodes a subunit of transcription/repair factor TFIIH, which functions in gene transcription and DNA repair. This protein stimulates ERCC3/XPB ATPase activity to trigger DNA opening during DNA repair, and is implicated in regulating cellular levels of TFIIH. Mutations in this gene result in trichothiodystrophy, complementation group A. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:21157](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21157) · Entrez [404672](https://www.ncbi.nlm.nih.gov/gene/404672) · UniProt [Q6ZYL4](https://www.uniprot.org/uniprotkb/Q6ZYL4) · Ensembl [ENSG00000272047](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272047)

## Data

Gene col 15707: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15707); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15707, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15707]; `tensor/DDL_lfc|DDL_z.npy` [15707]; `embed/gene_vectors.npy` [15707]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15707 or target_col == 15707). Every well: [[GTF2H5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2H5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
