---
symbol: "RAMAC"
type: "gene"
col: 9827
ensembl_id: "ENSG00000169612"
name: "RNA guanine-7 methyltransferase activating subunit"
location: "15q25.2"
module: 119
arm: "+"
pooled_cpm: 5.48
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# RAMAC

*RNA guanine-7 methyltransferase activating subunit* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (14 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.56× (z +10.2, q 2e-21, up in 37 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.878× (z -5.0, q 4e-04, down in 13 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.794× (z -3.7, q 0.061, down in 11 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Silodosin (drug)]] 0.05 µM in 1 line (A-172 0.0573×); [[Harringtonine (drug)]] 0.05 µM in 1 line (HT-29 0.0928×); [[Docetaxel (drug)]] 0.05 µM in 1 line (NCI-H2347 0.228×; ⚠ transcription drop; cell-cycle shift, explains ~41% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (J82 0.122×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFIP11]] (+0.62, fdr 1e-05), [[RNF139]] (+0.61, fdr 1e-05), [[C2orf49]] (+0.61, fdr 1e-05); moves opposite to [[R3HDM1]] (-0.47, fdr 4e-05), [[WWC2]] (-0.43, fdr 1e-04).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9827.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.56×** | +10.2 | 2e-21 | 37/42 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.58×** | +7.3 | 6e-11 | 23/41 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +7.1 | 3e-10 | 9/16 (SW480, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +6.9 | 6e-10 | 23/46 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.82×** | +6.8 | 1e-09 | 25/47 (PANC-1, SW480, …) | rises with dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +6.5 | 6e-09 | 17/31 (NCI-H2030, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +6.4 | 2e-08 | 19/37 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.69×** | +5.9 | 3e-07 | 18/37 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.64×** | +5.6 | 1e-06 | 25/47 (LOX-IMVI, MIA PaCa-2, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.3 | 7e-06 | 20/40 (NCI-H2347, BT-474, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.56×** | +5.1 | 2e-05 | 18/47 (SW480, C-33 A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.51×** | +4.7 | 1e-04 | 20/47 (SW480, HEC-1-A, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +4.4 | 5e-04 | 14/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.48×** | +4.3 | 8e-04 | 14/45 (NCI-H460, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.04×** | +4.2 | 9e-04 | 3/11 (NCI-H2030, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.003 | 7/43 (SW1417, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.011 | 12/47 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +3.5 | 0.011 | 7/42 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.2 | 0.032 | 7/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.035 | 9/44 (HT-29, KATO III, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9827.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Silodosin (drug)]] 0.05 µM in 1 line (A-172 0.0573×); [[Harringtonine (drug)]] 0.05 µM in 1 line (HT-29 0.0928×); [[Docetaxel (drug)]] 0.05 µM in 1 line (NCI-H2347 0.228×; ⚠ transcription drop; cell-cycle shift, explains ~41% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (J82 0.122×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.878× | -5.0 | 4e-04 | 13/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.794×** | -3.7 | 0.061 | 11/46 (NCI-H460, H4, …) | rises with dose | position effect removed |
| [[Cilostazol (drug)]] 5 µM |  | 0.729× | -3.4 | 0.11 | 6/47 (NCI-H460, SW480, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9827. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.63 | 0 | 1 | — | [[Silodosin (drug)]] 0.05 µM 0.0573× (z -9.7) |
| [[HT-29 (line)]] | alt | 5.71 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0928× (z -9.2) |
| [[J82 (line)]] | alt | 4.99 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.122× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.228× (z -8.9) ⚠ transcription drop; cell-cycle shift, explains ~41% of this change |
| [[A-427 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9827), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFIP11]] | +0.62 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[RNF139]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[C2orf49]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[VPS33B]] | +0.59 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[ZNF576]] | +0.58 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[RNF25]] | +0.58 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[KCTD10]] | +0.57 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[MRPS14]] | +0.56 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[ABT1]] | +0.55 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[RBM8A]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[EAF1]] | +0.55 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[TMEM184C]] | +0.55 | +0.50 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[R3HDM1]] | -0.47 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[WWC2]] | -0.43 | -0.36 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.520). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.6, 4.8); signed map (-11.1, -12.7). **Vector** length 41.2, 4.37% of its response variance represented; |z| ≥ 3 in 831 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.3 | +6.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.2 | +10.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +2.4 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +5.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | +3.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | +0.8 | +0.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.1 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.4 | -0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | -1.2 | +4.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.9 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.7 | -0.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.7 | +0.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.7 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | RNA guanine-7 methyltransferase activating subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.2 — chr15:82,986,210-82,991,057 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HsT19360, C15orf18, MGC2560, RAM; previously FAM103A1, RAMMET |
| Reactome | 3 pathways, smallest: RNA Pol II CTD phosphorylation and interaction with CE; mRNA Capping; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTL3](https://www.uniprot.org/uniprotkb/Q9BTL3) (RNA guanine-N7 methyltransferase activating subunit):

> Regulatory subunit of the mRNA-capping methyltransferase RNMT:RAMAC complex that methylates the N7 position of the added guanosine to the 5'-cap structure of mRNAs. Promotes the recruitment of the methyl donor, S-adenosyl-L-methionine, to RNMT. Regulates RNMT expression by a post-transcriptional stabilizing mechanism. Binds RNA.

**Summary**, from NCBI Gene [83640](https://www.ncbi.nlm.nih.gov/gene/83640):

> Enables RNA binding activity and enzyme activator activity. Involved in 7-methylguanosine mRNA capping. Located in nucleoplasm. Part of mRNA cap methyltransferase RNMT:RAMAC complex and mRNA capping enzyme complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:31022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31022) · Entrez [83640](https://www.ncbi.nlm.nih.gov/gene/83640) · UniProt [Q9BTL3](https://www.uniprot.org/uniprotkb/Q9BTL3) · Ensembl [ENSG00000169612](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169612)

## Data

Gene col 9827: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9827); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9827, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9827]; `tensor/DDL_lfc|DDL_z.npy` [9827]; `embed/gene_vectors.npy` [9827]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9827 or target_col == 9827). Every well: [[RAMAC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAMAC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
