---
symbol: "RPF1"
type: "gene"
col: 3876
ensembl_id: "ENSG00000117133"
name: "ribosome production factor 1 homolog"
location: "1p22.3"
module: 11
arm: "+"
pooled_cpm: 38.92
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# RPF1

*ribosome production factor 1 homolog* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (13 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.50× (z +13.3, q 2e-37, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.386×; ⚠ cell-cycle shift, explains ~65% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (AN3 CA 0.108×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHAX]] (+0.72, fdr 7e-06), [[REXO4]] (+0.68, fdr 7e-06), [[PDRG1]] (+0.67, fdr 7e-06); moves opposite to [[HDAC6]] (-0.60, fdr 1e-05), [[AP2A1]] (-0.58, fdr 2e-05), [[PRKACA]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3876.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.50×** | +13.3 | 2e-37 | 47/48 (SW480, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.10×** | +10.7 | 3e-24 | 43/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.88×** | +9.2 | 1e-17 | 45/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.51×** | +8.5 | 3e-15 | 39/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.78×** | +7.6 | 3e-12 | 40/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.64×** | +7.2 | 8e-11 | 39/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +6.4 | 1e-08 | 39/47 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +6.2 | 4e-08 | 36/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +6.1 | 8e-08 | 35/46 (NCI-H1573, RKO, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.1 | 2e-05 | 27/48 (HOP62, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.42×** | +5.0 | 2e-05 | 26/48 (HEC-1-A, NCI-H2347, …) | two highest doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +4.9 | 4e-05 | 31/48 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.8 | 6e-05 | 31/47 (PANC-1, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | **1.39×** | +4.8 | 8e-05 | 26/45 (NCI-H23, HCT15, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.83×** | +4.6 | 2e-04 | 26/48 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +4.3 | 5e-04 | 24/48 (Hs 766T, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.039 | 18/48 (NCI-H1573, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.080 | 15/48 (LoVo, SNU-423, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.24×** | +2.9 | 0.094 | 16/48 (HS-578T, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3876.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.386×; ⚠ cell-cycle shift, explains ~65% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (AN3 CA 0.108×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.892× | -5.5 | 2e-05 | 7/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3876. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 90.0 | 4 | 0 | [[Auranofin (drug)]] 5 µM 2.37× (z +11.0) | — |
| [[A-427 (line)]] | wt | 41.4 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.53× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -12.2) ⚠ cell-cycle shift, explains ~65% of this change |
| [[CFPAC-1 (line)]] | alt | 29.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.28× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 33.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 33.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.42× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 29.2 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.29× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 59.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.68× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 50.6 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.108× (z -9.8) |
| [[C-33 A (line)]] | alt | 42.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.08× (z +9.3) | — |
| [[C32 (line)]] | wt | 28.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.04× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 53.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.48× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 31.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.31× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 26.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +10.0) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[NCI-H460 (line)]] | wt | 28.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.76× (z +9.1) | — |
| [[RKO (line)]] | wt | 53.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.61× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 45.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.10× (z +8.5) | — |
| [[SW480 (line)]] | alt | 48.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.30× (z +12.5) | — |
| [[A-172 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3876), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHAX]] | +0.72 | +0.80 / +0.64 | both halves | 7e-06 |  |
| [[REXO4]] | +0.68 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[PDRG1]] | +0.67 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[GSPT2]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[TRMT10C]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 | STRING 938 |
| [[DNTTIP2]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 | STRING 781 |
| [[NSUN5]] | +0.65 | +0.74 / +0.64 | both halves | 7e-06 | STRING 694 |
| [[EIF6]] | +0.65 | +0.69 / +0.52 | both halves | 1e-05 | same gene group; STRING 983 |
| [[AGGF1]] | +0.64 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[LLPH]] | +0.64 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[GLRX2]] | +0.64 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[MRPL58]] | +0.63 | +0.73 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC6]] | -0.60 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[AP2A1]] | -0.58 | -0.71 / -0.48 | both halves | 2e-05 |  |
| [[PRKACA]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CEP43]] | -0.57 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[SEPTIN2]] | -0.57 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[SUGP2]] | -0.56 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[GANAB]] | -0.56 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[ODF2]] | -0.55 | -0.54 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.609). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.9, 1.9); signed map (-1.3, -22.9). **Vector** length 79.2, 19.1% of its response variance represented; |z| ≥ 3 in 828 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.6 | +13.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.4 | +10.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.6 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +7.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.8 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +6.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +1.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +0.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.3 | +2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -0.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | +0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | +0.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -0.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ribosome production factor 1 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:84,479,259-84,498,352 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously BXDC5 |
| Gene groups (HGNC) | Brix domain containing; Ribosome biogenesis factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9Y2](https://www.uniprot.org/uniprotkb/Q9H9Y2) (Ribosome production factor 1):

> May be required for ribosome biogenesis.

**Summary**, from NCBI Gene [80135](https://www.ncbi.nlm.nih.gov/gene/80135):

> Enables RNA binding activity. Predicted to be involved in maturation of 5.8S rRNA and maturation of LSU-rRNA. Located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30350](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30350) · Entrez [80135](https://www.ncbi.nlm.nih.gov/gene/80135) · UniProt [Q9H9Y2](https://www.uniprot.org/uniprotkb/Q9H9Y2) · Ensembl [ENSG00000117133](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117133)

## Data

Gene col 3876: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3876); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3876, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3876]; `tensor/DDL_lfc|DDL_z.npy` [3876]; `embed/gene_vectors.npy` [3876]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3876 or target_col == 3876). Every well: [[RPF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
