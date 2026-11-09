---
symbol: "CIAPIN1"
type: "gene"
col: 73
ensembl_id: "ENSG00000005194"
name: "cytokine induced apoptosis inhibitor 1"
location: "16q21"
module: 11
arm: "+"
pooled_cpm: 16.95
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# CIAPIN1

*cytokine induced apoptosis inhibitor 1* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.03× (z +12.1, q 7e-31, up in 43 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C32 0.123×, A-427 0.270×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.262×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C32 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHX30]] (+0.74, fdr 7e-06), [[SCO1]] (+0.74, fdr 7e-06), [[ZNF746]] (+0.68, fdr 7e-06); moves opposite to [[APLP2]] (-0.59, fdr 1e-05), [[RPS6KA5]] (-0.57, fdr 1e-05), [[PHF1]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 21 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 73.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.03×** | +12.1 | 7e-31 | 43/47 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.76×** | +9.3 | 6e-18 | 34/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +8.6 | 2e-15 | 26/43 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.62×** | +8.3 | 2e-14 | 31/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.38×** | +7.8 | 6e-13 | 27/47 (HT-29, A549, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.33×** | +7.6 | 4e-12 | 31/48 (SW480, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.53×** | +7.3 | 2e-11 | 30/48 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.48×** | +6.7 | 1e-09 | 23/43 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **2.04×** | +6.4 | 1e-08 | 26/44 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +6.1 | 7e-08 | 24/47 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.28×** | +5.9 | 2e-07 | 20/47 (NCI-H2030, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.34×** | +5.0 | 2e-05 | 18/48 (SW480, Hs 766T, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.7 | 1e-04 | 15/48 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +4.6 | 1e-04 | 18/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.31×** | +4.6 | 1e-04 | 15/47 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.67×** | +4.6 | 2e-04 | 14/45 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.57×** | +4.0 | 0.002 | 7/42 (J82, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.55×** | +3.9 | 0.002 | 11/44 (SNU-423, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.003 | 16/47 (SW480, Panc 03.27, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.003 | 11/46 (SNU-1, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.005 | 5/46 (NCI-H460, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.005 | 4/46 (SW480, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.027 | 9/43 (NCI-H460, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.031 | 10/47 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 73.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C32 0.123×, A-427 0.270×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.262×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C32 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.676× | -3.5 | 0.24 | 8/46 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.701× | -3.2 | 0.39 | 4/48 (A498, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 73. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 15.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 73), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX30]] | +0.74 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[SCO1]] | +0.74 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[ZNF746]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[COA4]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[UQCRFS1]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[UMPS]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[MRPL20]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[MRPL38]] | +0.64 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[YTHDF2]] | +0.64 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[FLAD1]] | +0.64 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[RPP38]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[RDH14]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APLP2]] | -0.59 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[RPS6KA5]] | -0.57 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[PHF1]] | -0.56 | -0.64 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.596). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-47.0, 3.7); signed map (-7.7, -25.4). **Vector** length 64.1, 10.5% of its response variance represented; |z| ≥ 3 in 808 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +8.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.6 | +8.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +4.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +12.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.3 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +6.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +2.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.7 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -1.6 | -0.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -3.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -0.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | cytokine induced apoptosis inhibitor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:57,428,187-57,447,420 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CIAE2 |
| Gene groups (HGNC) | Cytosolic iron-sulfur assembly components; 7BS orphan methyltransferases |
| Reactome | 1 pathways, smallest: Cytosolic iron-sulfur cluster assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6FI81](https://www.uniprot.org/uniprotkb/Q6FI81) (Anamorsin):

> Component of the cytosolic iron-sulfur (Fe-S) protein assembly (CIA) machinery required for the maturation of extramitochondrial Fe-S proteins. Part of an electron transfer chain functioning in an early step of cytosolic Fe-S biogenesis, facilitating the de novo assembly of a [4Fe-4S] cluster on the scaffold complex NUBP1-NUBP2. Electrons are transferred to CIAPIN1 from NADPH via the FAD- and FMN-containing protein NDOR1. NDOR1-CIAPIN1 are also required for the assembly of the diferric tyrosyl …

**Summary**, from NCBI Gene [57019](https://www.ncbi.nlm.nih.gov/gene/57019):

> CIAPIN1 is a cytokine-induced inhibitor of apoptosis with no relation to apoptosis regulatory molecules of the BCL2 (MIM 151430) or CASP (see MIM 147678) families. Expression of CIAPIN1 is dependent on growth factor stimulation (Shibayama et al., 2004 [PubMed 14970183]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:28050](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28050) · Entrez [57019](https://www.ncbi.nlm.nih.gov/gene/57019) · UniProt [Q6FI81](https://www.uniprot.org/uniprotkb/Q6FI81) · Ensembl [ENSG00000005194](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005194)

## Data

Gene col 73: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 73); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 73, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 73]; `tensor/DDL_lfc|DDL_z.npy` [73]; `embed/gene_vectors.npy` [73]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 73 or target_col == 73). Every well: [[CIAPIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CIAPIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
