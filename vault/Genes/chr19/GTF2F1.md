---
symbol: "GTF2F1"
type: "gene"
col: 4638
ensembl_id: "ENSG00000125651"
name: "general transcription factor IIF subunit 1"
location: "19p13.3"
module: 7
arm: "+"
pooled_cpm: 44.71
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# GTF2F1

*general transcription factor IIF subunit 1* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.87× (z +9.4, q 2e-18, up in 37 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.30× (z +6.6, q 1e-08, up in 37 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.749× (z -5.7, q 7e-06, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUPT6H]] (+0.69, fdr 7e-06), [[INO80B]] (+0.60, fdr 1e-05), [[RTF2]] (+0.58, fdr 1e-05); moves opposite to [[FDX1]] (-0.50, fdr 4e-05), [[ATP1B3]] (-0.50, fdr 6e-05), [[C2orf69]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4638.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.87×** | +9.4 | 2e-18 | 37/47 (SW480, RKO, …) | all doses, flat | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.30×** | +6.6 | 1e-08 | 37/49 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.3 | 6e-08 | 32/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.35×** | +6.1 | 1e-07 | 31/48 (PANC-1, A498, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +6.1 | 2e-07 | 36/48 (PANC-1, LOX-IMVI, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.51×** | +6.0 | 2e-07 | 27/41 (KATO III, SW480, …) | all doses, flat | composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +5.7 | 1e-06 | 37/48 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +5.6 | 1e-06 | 33/48 (HS-578T, A-172, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.46×** | +5.3 | 9e-06 | 28/45 (C-33 A, HEC-1-A, …) | all doses, flat | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +5.2 | 9e-06 | 37/48 (PANC-1, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +4.8 | 9e-05 | 30/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.39×** | +4.8 | 9e-05 | 29/48 (PANC-1, NCI-H2030, …) | rises with dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.34×** | +4.4 | 5e-04 | 27/46 (HCT15, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.28×** | +3.6 | 0.015 | 21/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.024 | 19/48 (LoVo, NCI-H2030, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.032 | 15/48 (NCI-H2030, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.049 | 17/48 (SW1417, Hs 766T, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.24×** | +3.0 | 0.067 | 14/48 (NCI-H23, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +3.0 | 0.073 | 20/48 (NCI-H2030, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4638.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.749×** | -5.7 | 7e-06 | 39/48 (A498, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.723×** | -4.9 | 2e-04 | 28/48 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.857× | -3.1 | 0.29 | 14/48 (COLO 205, MIA PaCa-2, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4638. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 32.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +11.6) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.74× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 51.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H23 (line)]] | alt | 41.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[RKO (line)]] | wt | 45.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW480 (line)]] | alt | 57.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 69.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4638), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUPT6H]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins; STRING 414 |
| [[INO80B]] | +0.60 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[RTF2]] | +0.58 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[ZNF408]] | +0.58 | +0.63 / +0.39 | both halves | 6e-05 |  |
| [[GOLGB1]] | +0.58 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[SDE2]] | +0.57 | +0.70 / +0.48 | both halves | 2e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[EIF3G]] | +0.57 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[GCC1]] | +0.57 | +0.67 / +0.38 | both halves | 7e-05 |  |
| [[NELFE]] | +0.57 | +0.62 / +0.55 | both halves | 1e-05 | same gene group; pathway: HALLMARK_DNA_REPAIR; STRING 740 |
| [[ZNF543]] | +0.55 | +0.66 / +0.34 | both halves | 1e-04 |  |
| [[DHX38]] | +0.55 | +0.61 / +0.56 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions |
| [[SF3A3]] | +0.55 | +0.63 / +0.42 | both halves | 4e-05 | pathway: HALLMARK_DNA_REPAIR; STRING 410 |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FDX1]] | -0.50 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[ATP1B3]] | -0.50 | -0.58 / -0.39 | both halves | 6e-05 |  |
| [[C2orf69]] | -0.49 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[FAM241A]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ZFAND6]] | -0.47 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[NDUFB2]] | -0.47 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[ASB13]] | -0.47 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[SGPP1]] | -0.46 | -0.55 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.432). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-37.0, -2.5); signed map (-0.9, -10.8). **Vector** length 93.3, 23.6% of its response variance represented; |z| ≥ 3 in 764 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.9 | +6.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.3 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +6.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +5.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | -0.5 |
|  | [[Malotilate (drug)]] 0.05 µM |  | +1.8 | +1.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.8 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.0 | -4.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.2 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIF subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:6,379,572-6,393,981 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TFIIF, BTF4, RAP74, TF2F1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; General transcription factor IIF complex subunits |
| Hallmark sets | DNA_REPAIR, APICAL_JUNCTION |
| Reactome | 59 pathways, smallest: Signaling by FGFR2 IIIa TM; Abortive elongation of HIV-1 transcript in the absence of Tat; FGFR2 mutant receptor activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P35269](https://www.uniprot.org/uniprotkb/P35269) (General transcription factor IIF subunit 1):

> TFIIF is a general transcription initiation factor that binds to RNA polymerase II and helps to recruit it to the initiation complex in collaboration with TFIIB. It promotes transcription elongation.

**Summary**, from NCBI Gene [2962](https://www.ncbi.nlm.nih.gov/gene/2962):

> Enables several functions, including RNA polymerase II general transcription initiation factor activity; enzyme binding activity; and promoter-specific chromatin binding activity. Involved in positive regulation of transcription by RNA polymerase II; response to virus; and transcription by RNA polymerase II. Located in nucleoplasm. Part of transcription factor TFIID complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:4652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4652) · Entrez [2962](https://www.ncbi.nlm.nih.gov/gene/2962) · UniProt [P35269](https://www.uniprot.org/uniprotkb/P35269) · Ensembl [ENSG00000125651](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125651)

## Data

Gene col 4638: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4638); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4638, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4638]; `tensor/DDL_lfc|DDL_z.npy` [4638]; `embed/gene_vectors.npy` [4638]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4638 or target_col == 4638). Every well: [[GTF2F1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2F1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
