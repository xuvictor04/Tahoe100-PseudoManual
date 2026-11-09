---
symbol: "TMEM128"
type: "gene"
col: 5315
ensembl_id: "ENSG00000132406"
name: "transmembrane protein 128"
location: "4p16.3"
module: 28
arm: "+"
pooled_cpm: 11.99
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# TMEM128

*transmembrane protein 128* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.50× (z +10.5, q 7e-23, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.728× (z -5.6, q 1e-05, down in 18 of 41 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.803× (z -4.0, q 0.007, down in 20 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERMARD]] (+0.75, fdr 7e-06), [[GIN1]] (+0.75, fdr 1e-05), [[MTHFSD]] (+0.74, fdr 7e-06); moves opposite to [[PRDX1]] (-0.59, fdr 2e-05), [[RPS6KA5]] (-0.58, fdr 5e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF391]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5315.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +10.5 | 7e-23 | 32/47 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +9.3 | 4e-18 | 28/43 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +8.4 | 1e-14 | 20/32 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.28×** | +6.3 | 4e-08 | 17/48 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +5.6 | 3e-06 | 17/46 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +5.5 | 3e-06 | 14/47 (CFPAC-1, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +5.3 | 8e-06 | 18/47 (A-427, A498, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +5.3 | 8e-06 | 22/41 (CFPAC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +5.0 | 4e-05 | 10/23 (HT-29, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.8 | 9e-05 | 18/45 (A-427, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.6 | 3e-04 | 6/22 (NCI-H1573, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.1 | 0.002 | 1/48 (SW 1088) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.21×** | +3.5 | 0.024 | 1/47 (HEC-1-A) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.029 | 6/46 (C-33 A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.073 | 6/46 (SW 900, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.075 | 3/47 (SW1417, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5315.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.728×** | -5.6 | 1e-05 | 18/41 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.761×** | -5.0 | 2e-04 | 17/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.772×** | -4.7 | 4e-04 | 17/47 (SW480, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.781×** | -4.5 | 1e-03 | 19/46 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.803×** | -4.0 | 0.007 | 20/46 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.805×** | -4.0 | 0.007 | 12/47 (RKO, Panc 03.27, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.832×** | -3.4 | 0.058 | 13/47 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.832×** | -3.3 | 0.058 | 12/47 (hTERT-HPNE, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5315. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0868× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.357× (z -9.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[AsPC-1 (line)]] | alt | 4.75 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0615× (z -10.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[BT-474 (line)]] | alt | 8.94 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0674× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HEC-1-A (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -9.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 8.48 | 0 | 1 | — | [[Nafamostat (mesylate) (drug)]] 0.5 µM 0.0723× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 4.97 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A498 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5315), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERMARD]] | +0.75 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[GIN1]] | +0.75 | +0.85 / +0.51 | both halves | 1e-05 |  |
| [[MTHFSD]] | +0.74 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[KCTD18]] | +0.74 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[ZSCAN21]] | +0.74 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[TYW5]] | +0.72 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[ELAC1]] | +0.69 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[SMARCE1]] | +0.69 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[PYM1]] | +0.69 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[C17orf75]] | +0.69 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[RAD52]] | +0.68 | +0.77 / +0.50 | both halves | 1e-05 |  |
| [[TRUB1]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDX1]] | -0.59 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[RPS6KA5]] | -0.58 | -0.62 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF391]] | B | ZNF391 activity raises TMEM128's level | lines that do not express ZNF391 (5) vs lines expressing it (45) | 1.37× lower at baseline in the lines without ZNF391 | 0.084 | ⚠ within organs, on part of the lines; also absent: LINC00159, ENSG00000283491, ASIC1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.741). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.7, 6.1); signed map (6.8, -23.8). **Vector** length 67.3, 10.5% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +9.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +10.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.3 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +5.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.5 | +2.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.5 | +3.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -2.8 | -4.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.6 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -4.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 128 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:4,235,542-4,248,223 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13159 |
| Matched by | ensembl_id |

UniProt [Q5BJH2](https://www.uniprot.org/uniprotkb/Q5BJH2) carries no function annotation.

**Summary**, from NCBI Gene [85013](https://www.ncbi.nlm.nih.gov/gene/85013):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28201](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28201) · Entrez [85013](https://www.ncbi.nlm.nih.gov/gene/85013) · UniProt [Q5BJH2](https://www.uniprot.org/uniprotkb/Q5BJH2) · Ensembl [ENSG00000132406](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132406)

## Data

Gene col 5315: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5315); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5315, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5315]; `tensor/DDL_lfc|DDL_z.npy` [5315]; `embed/gene_vectors.npy` [5315]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5315 or target_col == 5315). Every well: [[TMEM128 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM128.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
