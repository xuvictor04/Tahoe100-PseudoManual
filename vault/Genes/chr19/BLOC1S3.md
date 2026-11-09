---
symbol: "BLOC1S3"
type: "gene"
col: 12092
ensembl_id: "ENSG00000189114"
name: "biogenesis of lysosomal organelles complex 1 subunit 3"
location: "19q13.32"
module: 7
arm: "+"
pooled_cpm: 2.88
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# BLOC1S3

*biogenesis of lysosomal organelles complex 1 subunit 3* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.15× (z +10.1, q 3e-21, up in 26 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW480 0.0681×; ⚠ toxic; cell-cycle shift, explains ~38% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A498 0.0906×); [[Verteporfin (drug)]] 5 µM in 1 line (HOP62 0.0785×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMCR8]] (+0.66, fdr 7e-06), [[PPP1R37]] (+0.63, fdr 7e-06, ⚠ same locus), [[ZNF468]] (+0.61, fdr 1e-05), [[CACTIN]] (+0.60, fdr 3e-05); moves opposite to [[SPOPL]] (-0.52, fdr 4e-05), [[USP3]] (-0.51, fdr 3e-05), [[SMAD5]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12092.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.15×** | +10.1 | 3e-21 | 26/34 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.13×** | +7.1 | 4e-10 | 29/45 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.01×** | +6.5 | 1e-08 | 21/43 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.0 | 3e-07 | 12/31 (BT-474, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.76×** | +5.3 | 1e-05 | 2/14 (HEC-1-A, A549) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.77×** | +5.1 | 3e-05 | 12/39 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.6 | 3e-04 | 6/47 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +4.3 | 1e-03 | 0/9 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +4.2 | 0.001 | 8/46 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +4.0 | 0.003 | 13/44 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +4.0 | 0.004 | 14/33 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.022 | 5/42 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.45×** | +3.5 | 0.022 | 4/45 (A498, HOP62, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.022 | 9/40 (NCI-H2030, HOP62, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.025 | 5/44 (BT-474, C-33 A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.041 | 7/43 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +3.1 | 0.052 | 5/40 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12092.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW480 0.0681×; ⚠ toxic; cell-cycle shift, explains ~38% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A498 0.0906×); [[Verteporfin (drug)]] 5 µM in 1 line (HOP62 0.0785×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | 0.763× | -3.7 | 0.13 | 9/42 (AN3 CA, SNU-423, …) | top dose only |  |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | 0.646× | -3.4 | 0.13 | 7/45 (A498, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | 0.779× | -3.4 | 0.13 | 7/44 (Hs 766T, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12092. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.38 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0906× (z -10.4) |
| [[HOP62 (line)]] | alt | 4.85 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0785× (z -10.3) |
| [[SW480 (line)]] | alt | 3.51 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0681× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12092), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMCR8]] | +0.66 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[PPP1R37]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 | ⚠ same locus (30.7 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF468]] | +0.61 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[CACTIN]] | +0.60 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[EXOC8]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SLC66A1]] | +0.59 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[PTPN23]] | +0.59 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ZNF574]] | +0.59 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[CD2BP2]] | +0.57 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[CC2D1B]] | +0.56 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[PHF23]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[ZSCAN22]] | +0.55 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[VPS18]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPOPL]] | -0.52 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[USP3]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[SMAD5]] | -0.50 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[EED]] | -0.48 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[SNRPA1]] | -0.47 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[PDE7A]] | -0.47 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[FGFR1OP2]] | -0.47 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[MTF2]] | -0.46 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[ACVR2A]] | -0.46 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[ZDHHC20]] | -0.45 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[PPP2R5E]] | -0.45 | -0.48 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.538). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-38.4, -1.7); signed map (1.8, -9.2). **Vector** length 41.6, 4.43% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.9 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.7 | +4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +1.7 | +3.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +1.6 | +5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.4 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.2 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | +2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +0.9 | +0.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +0.9 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -0.7 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.0 | -1.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.0 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | biogenesis of lysosomal organelles complex 1 subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,178,784-45,216,933 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BLOS3, HPS8 |
| Gene groups (HGNC) | Biogenesis of lysosomal organelles complex 1 subunits |
| Reactome | 4 pathways, smallest: Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6QNY0](https://www.uniprot.org/uniprotkb/Q6QNY0) (Biogenesis of lysosome-related organelles complex 1 subunit 3):

> Component of the BLOC-1 complex, a complex that is required for normal biogenesis of lysosome-related organelles (LRO), such as platelet dense granules and melanosomes. In concert with the AP-3 complex, the BLOC-1 complex is required to target membrane protein cargos into vesicles assembled at cell bodies for delivery into neurites and nerve terminals. The BLOC-1 complex, in association with SNARE proteins, is also proposed to be involved in neurite extension. Plays a role in intracellular …

**Summary**, from NCBI Gene [388552](https://www.ncbi.nlm.nih.gov/gene/388552):

> This gene encodes a protein that is a component of the BLOC1 multi-subunit protein complex. This complex is necessary for the biogenesis of specialized organelles of the endosomal-lysosomal system, including platelet dense granules and melanosomes. Mutations in this gene cause Hermansky-Pudlak syndrome 8, a disease characterized by lysosomal storage defects, bleeding due to platelet storage pool deficiency, and oculocutaneous albinism. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20914](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20914) · Entrez [388552](https://www.ncbi.nlm.nih.gov/gene/388552) · UniProt [Q6QNY0](https://www.uniprot.org/uniprotkb/Q6QNY0) · Ensembl [ENSG00000189114](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189114)

## Data

Gene col 12092: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12092); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12092, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12092]; `tensor/DDL_lfc|DDL_z.npy` [12092]; `embed/gene_vectors.npy` [12092]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12092 or target_col == 12092). Every well: [[BLOC1S3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BLOC1S3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
