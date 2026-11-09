---
symbol: "NDUFB9"
type: "gene"
col: 7216
ensembl_id: "ENSG00000147684"
name: "NADH:ubiquinone oxidoreductase subunit B9"
location: "8q24.13"
module: 12
arm: "+"
pooled_cpm: 77.22
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# NDUFB9

*NADH:ubiquinone oxidoreductase subunit B9* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.83× (z +9.8, q 6e-20, up in 47 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.71× (z +5.1, q 5e-05, up in 42 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.285×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL21]] (+0.73, fdr 7e-06), [[NOL7]] (+0.71, fdr 7e-06, ⚠ NOL7 in the vector space only through flagged drug-doses), [[PUS3]] (+0.66, fdr 7e-06), [[EPB41L4A-AS1]] (+0.65, fdr 1e-05); moves opposite to [[CD164]] (-0.68, fdr 7e-06), [[GPAA1]] (-0.67, fdr 4e-05), [[NAGA]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7216.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.83×** | +9.8 | 6e-20 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.15×** | +6.9 | 1e-09 | 38/44 (KATO III, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.94×** | +5.8 | 1e-06 | 41/45 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +5.1 | 5e-05 | 42/48 (HOP62, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +5.0 | 5e-05 | 38/46 (HepG2/C3A, J82, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.69×** | +5.0 | 6e-05 | 44/48 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.68×** | +4.9 | 8e-05 | 41/48 (C32, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.66×** | +4.8 | 1e-04 | 40/47 (SW 900, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +4.5 | 5e-04 | 41/48 (HT-29, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.61×** | +4.3 | 1e-03 | 38/48 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +4.2 | 0.001 | 36/48 (NCI-H1573, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.2 | 0.001 | 36/48 (C32, NCI-H23, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +3.7 | 0.010 | 35/48 (LOX-IMVI, NCI-H1573, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.26×** | +3.1 | 0.073 | 23/48 (COLO 205, NCI-H1573, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.40×** | +3.1 | 0.081 | 28/47 (LoVo, C32, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.285×; ⚠ cell-cycle shift, would explain all of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7216. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 84.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.89× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H460 (line)]] | wt | 51.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[PANC-1 (line)]] | alt | 88.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SNU-1 (line)]] | wt | 68.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -11.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A549 (line)]] | wt | 67.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HepG2_C3A (line)]] | wt | 61.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.91× (z +8.5) ⚠ toxic | — |
| [[HT-29 (line)]] | alt | 178 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LoVo (line)]] | wt | 60.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LS 180 (line)]] | wt | 70.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 41.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1792 (line)]] | alt | 50.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H23 (line)]] | alt | 65.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SW480 (line)]] | alt | 69.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 69.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 117 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 120 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 109 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 152 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 67.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7216), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL21]] | +0.73 | +0.67 / +0.72 | both halves | 7e-06 | STRING 685 |
| [[NOL7]] ⚠ | +0.71 | +0.68 / +0.68 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[PUS3]] | +0.66 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[EPB41L4A-AS1]] | +0.65 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[MPHOSPH10]] | +0.65 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[ADPRM]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[SNHG8]] | +0.64 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[CINP]] | +0.63 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[RBMX2]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[DNAJC2]] | +0.62 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[PSMA7]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ZNF329]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[NSUN5]] | +0.59 | +0.65 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD164]] | -0.68 | -0.62 / -0.67 | both halves | 7e-06 |  |
| [[GPAA1]] | -0.67 | -0.41 / -0.68 | both halves | 4e-05 |  |
| [[NAGA]] | -0.63 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[TMEM123]] | -0.61 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[RBBP7]] | -0.61 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[CDK2]] | -0.60 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[FOXM1]] | -0.59 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[ADAM10]] | -0.58 | -0.71 / -0.53 | both halves | 1e-05 |  |
| [[SELENON]] | -0.58 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[NEMP1]] | -0.56 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[LRP11]] | -0.56 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[STMN1]] | -0.56 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.637). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-38.3, -9.8); signed map (-16.7, -7.6). **Vector** length 66.9, 22.1% of its response variance represented; |z| ≥ 3 in 651 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.5 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.8 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.5 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | -0.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.2 | +0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -0.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | -3.7 | +3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.5 | +0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -0.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -0.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.2 | +0.7 |
|  | [[Thymol (drug)]] 5 µM |  | -1.1 | +0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit B9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:124,539,101-124,580,648 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B22, UQOR22, LYRM3 |
| Gene groups (HGNC) | LYR motif containing; NADH:ubiquinone oxidoreductase supernumerary subunits |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6M9](https://www.uniprot.org/uniprotkb/Q9Y6M9) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed to be not involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4715](https://www.ncbi.nlm.nih.gov/gene/4715):

> The protein encoded by this gene is a subunit of the mitochondrial oxidative phosphorylation complex I (nicotinamide adenine dinucleotide: ubiquinone oxidoreductase). Complex I is localized to the inner mitochondrial membrane and functions to dehydrogenate nicotinamide adenine dinucleotide and to shuttle electrons to coenzyme Q. Complex I deficiency is the most common defect found in oxidative phosphorylation disorders and results in a range of conditions, including lethal neonatal disease, …

**Accessions** — [HGNC:7704](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7704) · Entrez [4715](https://www.ncbi.nlm.nih.gov/gene/4715) · UniProt [Q9Y6M9](https://www.uniprot.org/uniprotkb/Q9Y6M9) · Ensembl [ENSG00000147684](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147684)

## Data

Gene col 7216: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7216); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7216, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7216]; `tensor/DDL_lfc|DDL_z.npy` [7216]; `embed/gene_vectors.npy` [7216]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7216 or target_col == 7216). Every well: [[NDUFB9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFB9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
