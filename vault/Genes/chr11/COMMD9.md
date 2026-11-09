---
symbol: "COMMD9"
type: "gene"
col: 3141
ensembl_id: "ENSG00000110442"
name: "COMM domain containing 9"
location: "11p13"
module: 209
arm: "+"
pooled_cpm: 7.37
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 8
n_dd_up_clean: 15
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/209"]
generated_by: "tahoemap"
---

# COMMD9

*COMM domain containing 9* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.43× (z +11.4, q 3e-27, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.649× (z -7.9, q 2e-12, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAGPA]] (+0.70, fdr 1e-05), [[ATG14]] (+0.67, fdr 7e-06), [[VPS50]] (+0.65, fdr 7e-06); moves opposite to [[SATB2]] (-0.59, fdr 1e-05), [[HIVEP1]] (-0.55, fdr 4e-05), [[SMC6]] (-0.54, fdr 9e-06).
> It is in [[Module 209]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3141.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.43×** | +11.4 | 3e-27 | 41/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.40×** | +11.2 | 8e-27 | 38/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +9.0 | 4e-17 | 14/19 (A498, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.97×** | +8.7 | 4e-16 | 33/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.60×** | +8.5 | 2e-15 | 27/47 (A498, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +8.0 | 8e-14 | 18/31 (A498, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +6.9 | 5e-10 | 6/13 (A498, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +6.3 | 2e-08 | 26/47 (LS 180, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +5.9 | 2e-07 | 21/46 (SW1417, HS-578T, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +5.7 | 7e-07 | 21/45 (A-427, RKO, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +4.9 | 4e-05 | 17/44 (HS-578T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.61×** | +4.4 | 6e-04 | 11/36 (A498, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +4.3 | 6e-04 | 16/34 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.40×** | +4.3 | 7e-04 | 11/44 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.59×** | +4.3 | 7e-04 | 14/44 (LS 180, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +4.2 | 9e-04 | 16/40 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.008 | 5/47 (KATO III, HS-578T, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.009 | 10/44 (NCI-H460, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.20× | +3.3 | 0.024 | 10/48 (HCT15, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3141.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.649×** | -7.9 | 2e-12 | 34/47 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.714×** | -6.1 | 2e-07 | 22/42 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.652×** | -5.5 | 7e-06 | 21/44 (SW480, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.704×** | -4.5 | 9e-04 | 16/46 (SNU-423, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.765×** | -3.5 | 0.061 | 14/42 (HT-29, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.602×** | -3.4 | 0.061 | 15/42 (SHP-77, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.777×** | -3.2 | 0.085 | 12/47 (LoVo, SW1417, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.738×** | -3.2 | 0.085 | 7/45 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.783× | -3.2 | 0.10 | 15/46 (LS 180, SW48, …) | all doses, flat | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3141. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 6.55 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0719× (z -11.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -8.6) |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0736× (z -13.3) |
| [[A-172 (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3141), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAGPA]] | +0.70 | +0.53 / +0.78 | both halves | 1e-05 |  |
| [[ATG14]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[VPS50]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[SPNS1]] | +0.65 | +0.53 / +0.77 | both halves | 1e-05 |  |
| [[USP30]] | +0.65 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[WASHC5]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[TBC1D13]] | +0.63 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[VPS11]] | +0.62 | +0.56 / +0.80 | both halves | 1e-05 |  |
| [[GNPTG]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[CYB5R1]] | +0.61 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[RPP30]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[TENT2]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SATB2]] | -0.59 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[HIVEP1]] | -0.55 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[SMC6]] | -0.54 | -0.58 / -0.57 | both halves | 9e-06 |  |
| [[CLOCK]] | -0.54 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[RIPK1]] | -0.53 | -0.41 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 209]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.511). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.6, -15.4); signed map (-22.4, -21.4). **Vector** length 75.0, 13.5% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.6 | +8.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.0 | +6.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.0 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +5.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +3.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.9 | -5.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.1 | -6.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | COMM domain containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:36,269,284-36,289,449 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC166, FLJ31106 |
| Gene groups (HGNC) | COMM domain containing; CCC complex |
| Reactome | 3 pathways, smallest: Neddylation; Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P000](https://www.uniprot.org/uniprotkb/Q9P000) (COMM domain-containing protein 9):

> Scaffold protein in the commander complex that is essential for endosomal recycling of transmembrane cargos; the commander complex is composed of the CCC subcomplex and the retriever subcomplex. May modulate activity of cullin-RING E3 ubiquitin ligase (CRL) complexes. May down-regulate activation of NF-kappa-B. Modulates Na(+) transport in epithelial cells by regulation of apical cell surface expression of amiloride-sensitive sodium channel (ENaC) subunits.

**Summary**, from NCBI Gene [29099](https://www.ncbi.nlm.nih.gov/gene/29099):

> Predicted to be involved in endocytic recycling. Predicted to act upstream of or within cholesterol homeostasis. Located in nucleoplasm. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25014](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25014) · Entrez [29099](https://www.ncbi.nlm.nih.gov/gene/29099) · UniProt [Q9P000](https://www.uniprot.org/uniprotkb/Q9P000) · Ensembl [ENSG00000110442](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110442)

## Data

Gene col 3141: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3141); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3141, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3141]; `tensor/DDL_lfc|DDL_z.npy` [3141]; `embed/gene_vectors.npy` [3141]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3141 or target_col == 3141). Every well: [[COMMD9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COMMD9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
