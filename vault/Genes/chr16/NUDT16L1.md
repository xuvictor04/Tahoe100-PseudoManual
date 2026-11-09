---
symbol: "NUDT16L1"
type: "gene"
col: 9600
ensembl_id: "ENSG00000168101"
name: "nudix hydrolase 16 like 1"
location: "16p13.3"
module: 24
arm: "+"
pooled_cpm: 3.93
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# NUDT16L1

*nudix hydrolase 16 like 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.17× (z +8.7, q 2e-15, up in 13 of 20 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.68× (z +5.5, q 4e-06, up in 21 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 5.14×; ⚠ cell-cycle shift, explains ~83% of this change).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.564× (z -4.3, q 0.008, down in 20 of 42 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAL4]] (+0.72, fdr 7e-06), [[DCTN3]] (+0.69, fdr 1e-05), [[MED19]] (+0.66, fdr 7e-06); moves opposite to [[RPL6]] (-0.65, fdr 1e-05), [[RPSA]] (-0.63, fdr 7e-06), [[RPS3A]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 11 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9600.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 5.14×; ⚠ cell-cycle shift, explains ~83% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.17×** | +8.7 | 2e-15 | 13/20 (LS 180, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.23×** | +8.5 | 7e-15 | 6/8 (J82, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.13×** | +5.7 | 3e-06 | 28/47 (SW480, AsPC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.5 | 4e-06 | 21/35 (A549, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.09×** | +5.5 | 4e-06 | 27/45 (SW480, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.64×** | +5.3 | 1e-05 | 21/36 (NCI-H2030, CFPAC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.13×** | +5.2 | 1e-05 | 4/10 (PANC-1, HT-29, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.88×** | +4.7 | 2e-04 | 8/22 (LS 180, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.88×** | +4.5 | 4e-04 | 19/41 (HEC-1-A, LS 180, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.0 | 0.004 | 10/24 (SW1417, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.63×** | +3.7 | 0.012 | 11/46 (SW480, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.53×** | +3.2 | 0.072 | 12/36 (HEC-1-A, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9600.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.564×** | -4.3 | 0.008 | 20/42 (KATO III, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.372×** | -3.9 | 0.027 | 17/35 (NCI-H1792, HT-29, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.723×** | -3.5 | 0.080 | 14/44 (NCI-H2347, SW1417, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.635×** | -3.4 | 0.080 | 13/46 (A-172, A498, …) | inconsistent across doses |  |
| [[Ivermectin (drug)]] 5 µM |  | 0.651× | -3.3 | 0.13 | 11/47 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.450× | -3.2 | 0.15 | 13/40 (RKO, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9600. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 4.59 | 0 | 1 | — | [[Ligustrazine (drug)]] 5 µM 0.0675× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 5.88 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +9.3) ⚠ cell-cycle shift, explains ~83% of this change | — |
| [[A-172 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9600), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 10 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAL4]] | +0.72 | +0.61 / +0.79 | both halves | 7e-06 |  |
| [[DCTN3]] | +0.69 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[MED19]] | +0.66 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[MORN2]] | +0.64 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[TIMM17B]] ⚠ | +0.64 | +0.51 / +0.72 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM205]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ZNF324]] | +0.64 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[KRTCAP2]] | +0.63 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[GGNBP2]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[POLR2J]] ⚠ | +0.62 | +0.36 / +0.73 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CEP350]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[PDCD7]] | +0.60 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[IFT22]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[ING2]] | +0.60 | +0.48 / +0.67 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL6]] | -0.65 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[RPSA]] | -0.63 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[RPS3A]] | -0.61 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[MAT2A]] | -0.61 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[NAA50]] | -0.58 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[HNRNPA3]] | -0.58 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[IPO5]] | -0.58 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[GLO1]] | -0.58 | -0.36 / -0.65 | both halves | 1e-04 |  |
| [[APP]] | -0.57 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[EIF2S3]] | -0.56 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[DHFR]] | -0.55 | -0.43 / -0.62 | both halves | 4e-05 |  |
| [[LINC03009]] | -0.53 | -0.48 / -0.57 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-37.0, -13.9); signed map (-11.2, -2.3). **Vector** length 52.3, 7.78% of its response variance represented; |z| ≥ 3 in 763 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +3.3 | +4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +3.2 | +5.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +1.9 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +1.9 | +3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +1.9 | +5.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +2.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.1 | +1.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.3 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.1 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | nudix hydrolase 16 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:4,693,562-4,695,859 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SDOS, TIRR |
| Gene groups (HGNC) | Nudix hydrolase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRJ7](https://www.uniprot.org/uniprotkb/Q9BRJ7) (Tudor-interacting repair regulator protein):

> Key regulator of TP53BP1 required to stabilize TP53BP1 and regulate its recruitment to chromatin. In absence of DNA damage, interacts with the tandem Tudor-like domain of TP53BP1, masking the region that binds histone H4 dimethylated at 'Lys-20' (H4K20me2), thereby preventing TP53BP1 recruitment to chromatin and maintaining TP53BP1 localization to the nucleus. Following DNA damage, ATM-induced phosphorylation of TP53BP1 and subsequent recruitment of RIF1 leads to dissociate NUDT16L1/TIRR from …

**Summary**, from NCBI Gene [84309](https://www.ncbi.nlm.nih.gov/gene/84309):

> Enables snoRNA binding activity. Involved in negative regulation of double-strand break repair via nonhomologous end joining. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28154](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28154) · Entrez [84309](https://www.ncbi.nlm.nih.gov/gene/84309) · UniProt [Q9BRJ7](https://www.uniprot.org/uniprotkb/Q9BRJ7) · Ensembl [ENSG00000168101](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168101)

## Data

Gene col 9600: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9600); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9600, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9600]; `tensor/DDL_lfc|DDL_z.npy` [9600]; `embed/gene_vectors.npy` [9600]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9600 or target_col == 9600). Every well: [[NUDT16L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT16L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
