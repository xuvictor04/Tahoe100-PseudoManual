---
symbol: "MRPL50"
type: "gene"
col: 5935
ensembl_id: "ENSG00000136897"
name: "mitochondrial ribosomal protein L50"
location: "9q31.1"
module: 7
arm: "+"
pooled_cpm: 8.17
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# MRPL50

*mitochondrial ribosomal protein L50* — 9q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (16 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.36× (z +9.4, q 3e-18, up in 29 of 36 measured lines) ⚠ toxic. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.50× (z +6.5, q 1e-08, up in 24 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.0737×; ⚠ cell-cycle shift, explains ~86% of this change); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (COLO 205 0.0700×); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (HT-29 0.139×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NIP7]] (+0.72, fdr 7e-06), [[MRM3]] (+0.71, fdr 7e-06), [[FEM1A]] (+0.71, fdr 7e-06); moves opposite to [[SPAG9]] (-0.58, fdr 3e-05), [[AKTIP]] (-0.57, fdr 2e-05), [[ARL3]] (-0.56, fdr 2e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[MRPL15]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 17 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5935.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.36×** | +9.4 | 3e-18 | 29/36 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.65×** | +8.0 | 3e-13 | 24/42 (AsPC-1, A-172, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.95×** | +7.3 | 5e-11 | 12/18 (SW1417, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.80×** | +6.7 | 3e-09 | 30/45 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +6.5 | 1e-08 | 24/47 (A-172, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.80×** | +6.4 | 1e-08 | 27/46 (A-172, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.71×** | +6.1 | 9e-08 | 27/47 (SW480, LoVo, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.65×** | +5.7 | 8e-07 | 24/31 (A549, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +5.5 | 2e-06 | 4/48 (RKO, SNU-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +5.3 | 7e-06 | 23/46 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.64×** | +5.2 | 1e-05 | 11/24 (HT-29, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +5.0 | 2e-05 | 20/46 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.6 | 2e-04 | 22/44 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.5 | 3e-04 | 18/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +4.4 | 4e-04 | 21/45 (NCI-H460, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.001 | 17/47 (RPMI-7951, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.72×** | +3.2 | 0.029 | 8/42 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.68×** | +3.1 | 0.045 | 3/38 (LS 180, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5935.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.0737×; ⚠ cell-cycle shift, explains ~86% of this change); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (COLO 205 0.0700×); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (HT-29 0.139×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.824× | -3.1 | 0.97 | 9/47 (PANC-1, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5935. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0700× (z -10.2) |
| [[HT-29 (line)]] | alt | 6.27 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.139× (z -8.5) |
| [[RKO (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0737× (z -14.6) ⚠ cell-cycle shift, explains ~86% of this change |
| [[A-172 (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5935), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIP7]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[MRM3]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 | STRING 889 |
| [[FEM1A]] | +0.71 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[NOL11]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.70 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[TRMT10C]] | +0.70 | +0.68 / +0.76 | both halves | 7e-06 | STRING 440 |
| [[YTHDF2]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[JAGN1]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[TRMT5]] | +0.64 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[DDX28]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 | STRING 816 |
| [[MRPS7]] | +0.64 | +0.64 / +0.53 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 894 |
| [[COA4]] | +0.64 | +0.63 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG9]] | -0.58 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[AKTIP]] | -0.57 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ARL3]] | -0.56 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[TMEM50B]] | -0.56 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[LINC01881]] | -0.56 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[GFPT1]] | -0.55 | -0.59 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MRPL15]] | C | MRPL50's natural level strengthens MRPL15's drug response | MRPL50's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67, reverse -0.13; direction not clear | 0.031 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-38.5, 10.2); signed map (-2.8, -26.1). **Vector** length 50.8, 6.93% of its response variance represented; |z| ≥ 3 in 755 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.5 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +5.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +1.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.5 | +1.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.5 | +1.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -1.7 | -3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -0.5 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L50 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.1 — chr9:101,387,633-101,398,618 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20493, MRP-L50, mL50 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q8N5N7](https://www.uniprot.org/uniprotkb/Q8N5N7) carries no function annotation.

**Summary**, from NCBI Gene [54534](https://www.ncbi.nlm.nih.gov/gene/54534):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:16654](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16654) · Entrez [54534](https://www.ncbi.nlm.nih.gov/gene/54534) · UniProt [Q8N5N7](https://www.uniprot.org/uniprotkb/Q8N5N7) · Ensembl [ENSG00000136897](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136897)

## Data

Gene col 5935: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5935); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5935, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5935]; `tensor/DDL_lfc|DDL_z.npy` [5935]; `embed/gene_vectors.npy` [5935]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5935 or target_col == 5935). Every well: [[MRPL50 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL50.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
