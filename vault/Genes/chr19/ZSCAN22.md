---
symbol: "ZSCAN22"
type: "gene"
col: 11273
ensembl_id: "ENSG00000182318"
name: "zinc finger and SCAN domain containing 22"
location: "19q13.43"
module: 16
arm: "+"
pooled_cpm: 3.09
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZSCAN22

*zinc finger and SCAN domain containing 22* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.00× (z +7.1, q 5e-10, up in 17 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.687× (z -5.5, q 3e-05, down in 15 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.0741×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Arbutin (drug)]] 5 µM in 1 line (SW1417 0.0579×); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0853×; ⚠ cell-cycle shift, explains ~31% of this change); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (A498 0.0947×); [[Azithromycin (hydrate) (drug)]] 0.5 µM in 1 line (KATO III 0.0837×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZSCAN20]] (+0.75, fdr 7e-06), [[DNAJC14]] (+0.71, fdr 7e-06), [[RNF25]] (+0.67, fdr 7e-06); moves opposite to [[HIGD2A]] (-0.54, fdr 7e-05), [[CDK19]] (-0.53, fdr 2e-05), [[ZMYM2]] (-0.53, fdr 5e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11273.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.00×** | +7.1 | 5e-10 | 17/35 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +6.7 | 6e-09 | 22/42 (SK-MEL-2, BT-474, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +5.9 | 6e-07 | 13/37 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +5.8 | 1e-06 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +5.7 | 1e-06 | 2/5 (HS-578T, NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +5.4 | 6e-06 | 13/44 (PANC-1, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.34×** | +4.3 | 0.001 | 6/44 (A-172, RKO, …) | top dose only | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.003 | 9/36 (RKO, SK-MEL-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +4.1 | 0.003 | 9/45 (LoVo, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.10×** | +4.0 | 0.004 | 7/38 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.91×** | +3.5 | 0.025 | 2/33 (SW480, RKO) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11273.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.0741×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Arbutin (drug)]] 5 µM in 1 line (SW1417 0.0579×); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0853×; ⚠ cell-cycle shift, explains ~31% of this change); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (A498 0.0947×); [[Azithromycin (hydrate) (drug)]] 0.5 µM in 1 line (KATO III 0.0837×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -5.5 | 3e-05 | 15/35 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.595×** | -5.1 | 7e-05 | 15/36 (A-172, SW 900, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.712× | -3.4 | 0.14 | 8/25 (PANC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.741× | -3.1 | 0.29 | 10/34 (J82, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11273. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.76 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0947× (z -8.6) |
| [[KATO III (line)]] | alt | 4.01 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0837× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 2.54 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0853× (z -9.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[PANC-1 (line)]] | alt | 4.02 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0741× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 3.75 | 0 | 1 | — | [[Arbutin (drug)]] 5 µM 0.0579× (z -9.6) |
| [[A-172 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11273), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN20]] | +0.75 | +0.64 / +0.75 | both halves | 7e-06 | same gene group; STRING 797 |
| [[DNAJC14]] | +0.71 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[RNF25]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[TOP3B]] | +0.65 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[ZNF613]] | +0.65 | +0.67 / +0.55 | both halves | 1e-05 | same gene group |
| [[CDK9]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[ABCF3]] | +0.64 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[MIER2]] | +0.62 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[ZNF211]] | +0.62 | +0.66 / +0.54 | both halves | 1e-05 | same gene group |
| [[ASB6]] | +0.62 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[ZNF527]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 | same gene group |
| [[ZKSCAN2]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIGD2A]] | -0.54 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[CDK19]] | -0.53 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[ZMYM2]] | -0.53 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[ABHD18]] | -0.52 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[TRIM52-AS1]] | -0.52 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[NDUFA2]] | -0.51 | -0.30 / -0.57 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ZSCAN22's level | compounds that target TOP2A: 2 of 5 lower it (Epirubicin, Idarubicin) | 40% of the class's compounds vs 0.6% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.585). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-34.3, -2.0); signed map (-12.4, -29.2). **Vector** length 43.1, 4.32% of its response variance represented; |z| ≥ 3 in 1,085 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.2 | +6.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.4 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.3 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.0 | +1.0 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.7 | -5.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.5 | -0.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.2 | -1.8 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.0 | -0.9 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -0.9 | -2.1 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -0.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and SCAN domain containing 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.43 — chr19:58,326,994-58,342,332 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ZNF50, HKR2 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P10073](https://www.uniprot.org/uniprotkb/P10073) (Zinc finger and SCAN domain-containing protein 22):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [342945](https://www.ncbi.nlm.nih.gov/gene/342945):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:4929](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4929) · Entrez [342945](https://www.ncbi.nlm.nih.gov/gene/342945) · UniProt [P10073](https://www.uniprot.org/uniprotkb/P10073) · Ensembl [ENSG00000182318](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182318)

## Data

Gene col 11273: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11273); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11273, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11273]; `tensor/DDL_lfc|DDL_z.npy` [11273]; `embed/gene_vectors.npy` [11273]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11273 or target_col == 11273). Every well: [[ZSCAN22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSCAN22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
