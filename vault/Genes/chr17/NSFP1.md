---
symbol: "NSFP1"
type: "gene"
col: 15259
ensembl_id: "ENSG00000260075"
name: "N-ethylmaleimide-sensitive factor pseudogene 1"
location: "17q21.31"
module: 54
arm: "+"
pooled_cpm: 7.92
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# NSFP1

*N-ethylmaleimide-sensitive factor pseudogene 1* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.43× (z +5.0, q 3e-04, up in 11 of 33 measured lines) ⚠ toxic. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.37× (z +4.5, q 0.001, up in 12 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.482× (z -9.8, q 7e-20, down in 17 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.653× (z -5.9, q 4e-07, down in 19 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK5RAP1]] (+0.69, fdr 7e-06), [[KLHL20]] (+0.66, fdr 1e-05), [[CCDC107]] (+0.64, fdr 1e-05); moves opposite to [[YWHAZ]] (-0.63, fdr 2e-05), [[ADSS2]] (-0.61, fdr 1e-05), [[KRT8P12]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02930]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15259.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +5.0 | 3e-04 | 11/33 (CFPAC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +4.5 | 0.001 | 12/46 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +4.5 | 0.001 | 11/45 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +3.7 | 0.031 | 3/35 (PANC-1, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | 1.35× | +3.1 | 0.20 | 3/38 (LOX-IMVI, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.25× | +3.1 | 0.20 | 6/40 (HEC-1-A, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15259.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.482×** | -9.8 | 7e-20 | 17/20 (KATO III, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.605×** | -7.3 | 9e-11 | 21/29 (NCI-H460, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.624×** | -6.6 | 9e-09 | 15/15 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.653×** | -5.9 | 4e-07 | 19/43 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.675×** | -5.7 | 1e-06 | 10/45 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.689×** | -5.4 | 6e-06 | 15/41 (C32, HOP62, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.686×** | -5.3 | 1e-05 | 17/31 (NCI-H1792, C32, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.789×** | -3.5 | 0.039 | 13/43 (AsPC-1, HT-29, …) | inconsistent across doses |  |
| [[Simotinib (drug)]] 0.05 µM |  | **0.787×** | -3.2 | 0.078 | 6/38 (LS 180, HOP62, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.747× | -3.0 | 0.14 | 12/29 (NCI-H1573, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15259. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.7 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0536× (z -22.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 14.1 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0646× (z -14.9) |
| [[A-172 (line)]] | wt | 9.19 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -13.3) ⚠ cell-cycle shift, explains ~81% of this change |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -9.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 20.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0444× (z -18.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 16.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -13.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 14.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -11.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 24.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0613× (z -19.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 16.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -12.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 11.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -11.3) ⚠ cell-cycle shift, explains ~81% of this change |
| [[HT-29 (line)]] | alt | 9.81 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -8.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 7.93 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -8.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 7.04 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -9.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15259), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK5RAP1]] | +0.69 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[KLHL20]] | +0.66 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[CCDC107]] | +0.64 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[FBXO42]] | +0.64 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[PRKRIP1]] | +0.62 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ATP5MJ]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[CNOT8]] | +0.61 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[SDHAF1]] | +0.61 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[MALSU1]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ROMO1]] | +0.60 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[PDXP]] | +0.60 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[ANAPC11]] | +0.59 | +0.46 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAZ]] | -0.63 | -0.46 / -0.64 | both halves | 2e-05 |  |
| [[ADSS2]] | -0.61 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[KRT8P12]] | -0.61 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[TUG1]] | -0.60 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[EIF4G2]] | -0.60 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[NRAS]] | -0.58 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[SLC39A10]] | -0.58 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[NXT2]] | -0.57 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[HUWE1]] | -0.57 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.56 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[ZNF655]] | -0.56 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[HNRNPK]] | -0.56 | -0.40 / -0.54 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02930]] | B | LINC02930 activity raises NSFP1's level | lines that do not express LINC02930 (33) vs lines expressing it (17) | 1.48× lower at baseline in the lines without LINC02930 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000232053, GYPC, PLPP4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.678). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.4, -18.1); signed map (-38.9, 19.3). **Vector** length 61.8, 9.21% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.2 | +5.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.8 | +4.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +2.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.3 | +4.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.2 | +2.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.0 | +2.5 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +0.9 | +0.2 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.9 | -7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | -6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.7 | -9.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.2 | -5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | N-ethylmaleimide-sensitive factor pseudogene 1 |
| Locus type | pseudogene |
| Location | 17q21.31 — chr17:46,372,855-46,487,141 (+) |
| Ensembl biotype | unprocessed_pseudogene |
| Also known as | ; previously NSFP |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:31405](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31405) · Entrez [728806](https://www.ncbi.nlm.nih.gov/gene/728806) · Ensembl [ENSG00000260075](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000260075)

## Data

Gene col 15259: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15259); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15259, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15259]; `tensor/DDL_lfc|DDL_z.npy` [15259]; `embed/gene_vectors.npy` [15259]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15259 or target_col == 15259). Every well: [[NSFP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSFP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
