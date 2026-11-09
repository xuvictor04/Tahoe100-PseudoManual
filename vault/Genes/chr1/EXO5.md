---
symbol: "EXO5"
type: "gene"
col: 8830
ensembl_id: "ENSG00000164002"
name: "exonuclease 5"
location: "1p34.2"
module: 1
arm: "+"
pooled_cpm: 2.62
n_lines_expressing: 45
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# EXO5

*exonuclease 5* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.11× (z +6.2, q 2e-07, up in 6 of 17 measured lines) ⚠ toxic; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.53× (z +5.2, q 3e-05, up in 10 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.535× (z -5.4, q 3e-05, down in 15 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.0281×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.0679×); [[Roxadustat (drug)]] 0.05 µM in 1 line (A-427 0.0572×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETMAR]] (+0.61, fdr 2e-05), [[ZFP69]] (+0.61, fdr 7e-06, ⚠ same locus), [[PGBD2]] (+0.60, fdr 1e-05), [[ZNF239]] (+0.57, fdr 3e-05); moves opposite to [[SIRT2]] (-0.58, fdr 3e-05), [[HADHB]] (-0.55, fdr 1e-04), [[GABARAP]] (-0.54, fdr 3e-05, ⚠ GABARAP in the vector space only through flagged drug-doses), [[VEGFB]] (-0.51, fdr 7e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF681]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8830.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **2.11×** | +6.2 | 2e-07 | 6/17 (J82, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +5.4 | 2e-05 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +5.2 | 3e-05 | 10/39 (J82, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.78×** | +5.0 | 7e-05 | 14/40 (J82, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.50×** | +5.0 | 8e-05 | 7/30 (SW480, RKO, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.64×** | +4.3 | 0.002 | 5/12 (J82, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.3 | 0.002 | 10/39 (A498, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.57×** | +3.9 | 0.007 | 10/40 (J82, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.56×** | +3.9 | 0.007 | 11/37 (J82, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +3.8 | 0.010 | 8/28 (SNU-423, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.54×** | +3.5 | 0.028 | 2/6 (NCI-H2347, A498) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | 1.42× | +3.0 | 0.11 | 1/10 (CFPAC-1) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8830.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.0281×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.0679×); [[Roxadustat (drug)]] 0.05 µM in 1 line (A-427 0.0572×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.535×** | -5.4 | 3e-05 | 15/39 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.639×** | -3.9 | 0.027 | 13/24 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Furosemide (drug)]] 0.05 µM |  | 0.698× | -3.1 | 0.33 | 8/36 (Hs 766T, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8830. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.31 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0281× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0679× (z -14.8) |
| [[A-427 (line)]] | wt | 6.18 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0572× (z -11.3) |
| [[A-172 (line)]] | wt | 0.898 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.783 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.668 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.255 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.193 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.390 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.997 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.243 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8830), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETMAR]] | +0.61 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[ZFP69]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 | ⚠ same locus (12.4 kb, same strand: neighbours can correlate without regulation) |
| [[PGBD2]] | +0.60 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ZNF239]] | +0.57 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[TMEM147-AS1]] | +0.56 | +0.63 / +0.38 | both halves | 6e-05 |  |
| [[HENMT1]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ZNF746]] | +0.56 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[PIGW]] | +0.56 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[CENPBD1P]] | +0.55 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[HPS6]] | +0.55 | +0.68 / +0.33 | both halves | 1e-04 |  |
| [[SPRYD4]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[CHST14]] | +0.55 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[POLR2D]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT2]] | -0.58 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[HADHB]] | -0.55 | -0.32 / -0.48 | both halves | 1e-04 |  |
| [[GABARAP]] ⚠ | -0.54 | -0.48 / -0.45 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[VEGFB]] | -0.51 | -0.53 / -0.37 | both halves | 7e-05 |  |
| [[MLF1]] | -0.51 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[SLC17A5]] | -0.51 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[TMEM205]] | -0.50 | -0.23 / -0.39 | both halves | 5e-04 |  |
| [[PPP1R12B]] | -0.50 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[RFX2]] | -0.49 | -0.57 / -0.32 | both halves | 2e-04 |  |
| [[EFHC1]] | -0.49 | -0.56 / -0.28 | both halves | 3e-04 |  |
| [[HIP1]] | -0.49 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[MAK]] | -0.49 | -0.23 / -0.41 | both halves | 5e-04 |  |
| [[WDR19]] | -0.49 | -0.32 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF681]] | B | ZNF681 activity raises EXO5's level | lines that do not express ZNF681 (16) vs lines expressing it (34) | 1.53× lower at baseline in the lines without ZNF681 | 0.088 | ⚠ within organs, on part of the lines; also absent: RPSAP58, ZNF649, ZNF793 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.383). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-38.3, 22.9); signed map (-7.5, -24.3). **Vector** length 34.7, 3.55% of its response variance represented; |z| ≥ 3 in 831 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.6 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +2.5 | +6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.1 | +3.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.0 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +1.9 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +4.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.0 | +1.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.2 | -3.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | +1.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.9 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | +0.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | exonuclease 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:40,508,741-40,516,038 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21144; previously C1orf176, DEM1 |
| Gene groups (HGNC) | Exonucleases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H790](https://www.uniprot.org/uniprotkb/Q9H790) (Exonuclease V):

> Single-stranded DNA (ssDNA) bidirectional exonuclease involved in DNA repair. Probably involved in DNA repair following ultraviolet (UV) irradiation and interstrand cross-links (ICLs) damage. Has both 5'-3' and 3'-5' exonuclease activities with a strong preference for 5'-ends. Acts as a sliding exonuclease that loads at ssDNA ends and then slides along the ssDNA prior to cutting; however the sliding and the 3'-5' exonuclease activities are abolished upon binding to the replication protein A …

**Summary**, from NCBI Gene [64789](https://www.ncbi.nlm.nih.gov/gene/64789):

> The protein encoded by this gene is a single-stranded DNA (ssDNA)-specific exonuclease that can slide along the DNA before cutting it. However, human replication protein A binds ssDNA and restricts sliding of the encoded protein, providing a 5'-directionality to the enzyme. This protein localizes to nuclear repair loci after DNA damage. [provided by RefSeq, Nov 2016]

**Accessions** — [HGNC:26115](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26115) · Entrez [64789](https://www.ncbi.nlm.nih.gov/gene/64789) · UniProt [Q9H790](https://www.uniprot.org/uniprotkb/Q9H790) · Ensembl [ENSG00000164002](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164002)

## Data

Gene col 8830: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8830); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8830, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8830]; `tensor/DDL_lfc|DDL_z.npy` [8830]; `embed/gene_vectors.npy` [8830]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8830 or target_col == 8830). Every well: [[EXO5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXO5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
