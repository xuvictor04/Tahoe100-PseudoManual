---
symbol: "PQBP1"
type: "gene"
col: 2215
ensembl_id: "ENSG00000102103"
name: "polyglutamine binding protein 1"
location: "Xp11.23"
module: 20
arm: "-"
pooled_cpm: 18.9
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# PQBP1

*polyglutamine binding protein 1* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.00× (z +8.4, q 3e-14, up in 38 of 47 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.07× (z +6.2, q 7e-08, up in 43 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (J82 0.316×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG8]] (+0.69, fdr 7e-06), [[WASHC1]] (+0.68, fdr 7e-06), [[EIF4EBP3]] (+0.67, fdr 7e-06); moves opposite to [[PGAM1]] (-0.63, fdr 1e-05), [[TPM3]] (-0.62, fdr 7e-06), [[BLTP2]] (-0.61, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2215.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.00×** | +8.4 | 3e-14 | 38/47 (PANC-1, J82, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.40×** | +7.5 | 2e-11 | 36/40 (SNU-423, H4, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.26×** | +6.7 | 4e-09 | 37/46 (PANC-1, A549, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.07×** | +6.2 | 7e-08 | 43/47 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +6.2 | 7e-08 | 35/47 (NCI-H2347, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.00×** | +5.7 | 1e-06 | 20/30 (PANC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.77×** | +4.7 | 2e-04 | 31/42 (A-172, PANC-1, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +4.7 | 2e-04 | 14/48 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.67×** | +4.4 | 7e-04 | 28/47 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.67×** | +4.4 | 7e-04 | 29/43 (SW 900, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.65×** | +4.3 | 9e-04 | 29/46 (BT-474, PANC-1, …) | top dose only | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.15×** | +4.0 | 0.003 | 32/45 (A498, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.05×** | +3.8 | 0.006 | 27/44 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.6 | 0.015 | 23/43 (MIA PaCa-2, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.68×** | +3.4 | 0.027 | 18/33 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.77×** | +3.0 | 0.089 | 19/45 (KATO III, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.42×** | +3.0 | 0.089 | 19/44 (SNU-423, AsPC-1, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.0 | 0.092 | 22/48 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2215.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (J82 0.316×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | 0.436× | -3.3 | 0.48 | 21/48 (NCI-H460, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2215. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 18.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +10.5) ⚠ cell-cycle shift, explains ~47% of this change | [[Selinexor (drug)]] 5 µM 0.316× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 10.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +8.8) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[A549 (line)]] | wt | 22.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +9.4) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[LoVo (line)]] | wt | 17.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +8.7) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[PANC-1 (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +10.8) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[SNU-423 (line)]] | alt | 26.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +9.4) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[A-427 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 30.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2215), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG8]] | +0.69 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[WASHC1]] | +0.68 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[EIF4EBP3]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[CIRBP]] | +0.67 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[EIF1]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[RNF7]] | +0.66 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[SMDT1]] | +0.65 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[RSF1]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[CDK3]] | +0.64 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[DCXR]] | +0.64 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[SNHG12]] | +0.64 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[FBXL15]] | +0.63 | +0.61 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGAM1]] | -0.63 | -0.70 / -0.57 | both halves | 1e-05 |  |
| [[TPM3]] | -0.62 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[BLTP2]] | -0.61 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[NUP155]] | -0.61 | -0.52 / -0.62 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[TMED7]] | -0.60 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[HNRNPA3]] | -0.60 | -0.56 / -0.69 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions |
| [[RPE]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[RNPS1]] | -0.59 | -0.60 / -0.57 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions |
| [[CHID1]] | -0.58 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[FAM91A1]] | -0.58 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.57 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[OPA1]] | -0.57 | -0.54 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.639). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-38.4, -21.2); signed map (-12.7, -0.4). **Vector** length 71.3, 17.9% of its response variance represented; |z| ≥ 3 in 596 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +6.7 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +6.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.9 | +6.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +6.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.5 | +3.8 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.3 | +2.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +3.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.2 | +4.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.9 | +0.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.9 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -2.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +0.3 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -1.8 | +0.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.3 | +0.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -2.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | polyglutamine binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:48,890,197-48,903,402 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RENS1, MRXS8, SHS, MRX55, MRX2 |
| Gene groups (HGNC) | Spliceosomal B complex |
| Reactome | 7 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Dengue Virus-Host Interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [O60828](https://www.uniprot.org/uniprotkb/O60828) (Polyglutamine-binding protein 1):

> Intrinsically disordered protein that acts as a scaffold, and which is involved in different processes, such as pre-mRNA splicing, transcription regulation, innate immunity and neuron development. Interacts with splicing-related factors via the intrinsically disordered region and regulates alternative splicing of target pre-mRNA species. May suppress the ability of POU3F2 to transactivate the DRD1 gene in a POU3F2 dependent manner. Can activate transcription directly or via association with the …

**Summary**, from NCBI Gene [10084](https://www.ncbi.nlm.nih.gov/gene/10084):

> This gene encodes a nuclear polyglutamine-binding protein that is involved with transcription activation. The encoded protein contains a WW domain. Mutations in this gene have been found in patients with Renpenning syndrome 1 and other syndromes with X-linked cognitive disability. Multiple alternatively spliced transcript variants that encode different protein isoforms have been described for this gene.[provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:9330](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9330) · Entrez [10084](https://www.ncbi.nlm.nih.gov/gene/10084) · UniProt [O60828](https://www.uniprot.org/uniprotkb/O60828) · Ensembl [ENSG00000102103](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102103)

## Data

Gene col 2215: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2215); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2215, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2215]; `tensor/DDL_lfc|DDL_z.npy` [2215]; `embed/gene_vectors.npy` [2215]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2215 or target_col == 2215). Every well: [[PQBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PQBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
