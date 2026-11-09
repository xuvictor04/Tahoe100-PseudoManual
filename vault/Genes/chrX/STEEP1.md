---
symbol: "STEEP1"
type: "gene"
col: 308
ensembl_id: "ENSG00000018610"
name: "STING1 ER exit protein 1"
location: "Xq24"
module: 209
arm: "+"
pooled_cpm: 17.97
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/209"]
generated_by: "tahoemap"
---

# STEEP1

*STING1 ER exit protein 1* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.44× (z +17.1, q 0e+00, up in 45 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (COLO 205 0.0856×); [[Roxadustat (drug)]] 0.05 µM in 1 line (SNU-1 0.0556×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.220×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRPF31]] (+0.64, fdr 1e-05), [[TBC1D13]] (+0.63, fdr 2e-05), [[SKIC2]] (+0.61, fdr 1e-05); moves opposite to [[CLOCK]] (-0.53, fdr 8e-05), [[HIVEP1]] (-0.52, fdr 7e-05), [[SATB2]] (-0.50, fdr 1e-04).
> It is in [[Module 209]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 308.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.44×** | +17.1 | 0e+00 | 45/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.08×** | +14.0 | 3e-42 | 46/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.82×** | +11.4 | 5e-28 | 43/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +9.4 | 8e-19 | 28/42 (NCI-H1573, A498, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +8.8 | 2e-16 | 34/47 (SW480, BT-474, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.34×** | +8.5 | 2e-15 | 32/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +7.1 | 1e-10 | 25/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.9 | 3e-10 | 26/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +6.4 | 1e-08 | 22/48 (HOP62, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **1.38×** | +5.9 | 2e-07 | 15/30 (SW480, PANC-1, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.24×** | +5.8 | 3e-07 | 20/47 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +5.7 | 6e-07 | 17/36 (SW480, J82, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.27×** | +4.6 | 2e-04 | 17/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.25×** | +4.2 | 0.001 | 9/46 (LOX-IMVI, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.002 | 19/47 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.005 | 15/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.006 | 13/46 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.058 | 9/48 (SW1417, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 308.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (COLO 205 0.0856×); [[Roxadustat (drug)]] 0.05 µM in 1 line (SNU-1 0.0556×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.220×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.866× | -3.9 | 0.056 | 14/48 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.835× | -3.0 | 0.68 | 11/47 (CHP-212, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 308. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 26.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.86× (z +12.9) | — |
| [[A-427 (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.111× (z -9.4) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 18.3 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0856× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 21.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.56× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 26.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.19× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 23.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.48× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 15.9 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0556× (z -12.0) |
| [[A-172 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 308), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF31]] | +0.64 | +0.50 / +0.60 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[TBC1D13]] | +0.63 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[SKIC2]] | +0.61 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[EIF2B1]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[VAMP7]] | +0.60 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[EXOC3]] | +0.57 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[SENP2]] | +0.57 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[MED23]] | +0.56 | +0.67 / +0.39 | both halves | 5e-05 |  |
| [[GNPTG]] | +0.56 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[ALDH6A1]] | +0.55 | +0.51 / +0.38 | both halves | 6e-05 |  |
| [[RMDN3]] | +0.55 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[CALCOCO1]] | +0.54 | +0.46 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLOCK]] | -0.53 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[HIVEP1]] | -0.52 | -0.44 / -0.37 | both halves | 7e-05 |  |
| [[SATB2]] | -0.50 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[PKP4]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[RAN]] | -0.48 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[TRAF3]] | -0.48 | -0.48 / -0.24 | both halves | 4e-04 |  |
| [[NETO2]] | -0.47 | -0.47 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 209]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.749). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-5.3, -11.2); signed map (-31.7, -11.4). **Vector** length 63.4, 10.00% of its response variance represented; |z| ≥ 3 in 834 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | +4.1 | +5.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.2 | +17.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.2 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +8.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.8 |
|  | [[MK-3903 (drug)]] 5 µM |  | +1.3 | +0.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +0.8 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.2 | +1.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | -0.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -2.8 | -3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | STING1 ER exit protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:119,538,149-119,565,409 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22965; previously CXorf56 |
| Gene groups (HGNC) | Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H5V9](https://www.uniprot.org/uniprotkb/Q9H5V9) (STING ER exit protein):

> Molecular adapter that stimulates membrane curvature formation and subsequent endoplasmic reticulum exit site (ERES) establishment by recruiting PI3K complex I, leading to COPII vesicle-mediated transport. Promotes endoplasmic reticulum (ER) exit of cGAMP-activated STING1 oligomers.

**Summary**, from NCBI Gene [63932](https://www.ncbi.nlm.nih.gov/gene/63932):

> While this gene is well-supported by transcript data, no functional information on its protein products is currently available. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2009]

**Accessions** — [HGNC:26239](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26239) · Entrez [63932](https://www.ncbi.nlm.nih.gov/gene/63932) · UniProt [Q9H5V9](https://www.uniprot.org/uniprotkb/Q9H5V9) · Ensembl [ENSG00000018610](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000018610)

## Data

Gene col 308: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 308); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 308, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 308]; `tensor/DDL_lfc|DDL_z.npy` [308]; `embed/gene_vectors.npy` [308]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 308 or target_col == 308). Every well: [[STEEP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STEEP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
