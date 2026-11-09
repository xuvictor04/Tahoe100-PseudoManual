---
symbol: "SLIRP"
type: "gene"
col: 4105
ensembl_id: "ENSG00000119705"
name: "SRA stem-loop interacting RNA binding protein"
location: "14q24.3"
module: 54
arm: "+"
pooled_cpm: 39.87
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# SLIRP

*SRA stem-loop interacting RNA binding protein* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.34× (z +9.3, q 1e-17, up in 45 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 26 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS26]] (+0.66, fdr 1e-05), [[MRPS21]] (+0.64, fdr 4e-05), [[COMMD6]] (+0.63, fdr 4e-04); moves opposite to [[HP1BP3]] (-0.58, fdr 2e-04), [[CHRAC1]] (-0.57, fdr 9e-05), [[PCNT]] (-0.57, fdr 8e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4105.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +9.3 | 1e-17 | 45/48 (BT-474, HOP62, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **2.58×** | +7.1 | 4e-10 | 40/46 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **2.44×** | +6.6 | 8e-09 | 35/40 (A549, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **2.12×** | +5.8 | 1e-06 | 46/48 (BT-474, NCI-H1573, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.09×** | +5.7 | 2e-06 | 46/48 (BT-474, NCI-H1573, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +5.6 | 2e-06 | 44/47 (NCI-H1573, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **2.01×** | +5.4 | 7e-06 | 44/48 (BT-474, A549, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.84×** | +4.5 | 5e-04 | 35/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.89×** | +4.5 | 5e-04 | 33/44 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +4.4 | 7e-04 | 38/48 (HOP62, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **1.63×** | +3.8 | 0.008 | 32/46 (SW 900, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.65×** | +3.8 | 0.008 | 36/48 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.027 | 33/48 (HT-29, SW480, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~68% of this change | **1.53×** | +3.2 | 0.062 | 29/47 (NCI-H1792, SW 900, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.53×** | +3.1 | 0.062 | 30/47 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.074 | 23/48 (BT-474, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4105.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.640× | -3.4 | 0.36 | 34/48 (HT-29, RKO, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.61 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4105. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 41.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +12.8) | — |
| [[NCI-H1792 (line)]] | alt | 27.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +9.4) | — |
| [[A549 (line)]] | wt | 36.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | — |
| [[AsPC-1 (line)]] | alt | 22.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 48.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 43.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 27.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 52.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 39.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | — |
| [[Panc 03.27 (line)]] | alt | 52.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 41.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | — |
| [[SHP-77 (line)]] | alt | 45.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 25.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 43.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +9.0) | — |
| [[A-172 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 77.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 53.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4105), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 20 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS26]] | +0.66 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[MRPS21]] | +0.64 | +0.41 / +0.67 | both halves | 4e-05 | STRING 418 |
| [[COMMD6]] | +0.63 | +0.25 / +0.74 | both halves | 4e-04 |  |
| [[SF3B6]] | +0.63 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[ATP5MK]] | +0.62 | +0.29 / +0.72 | both halves | 2e-04 | STRING 454 |
| [[COX6B1]] | +0.61 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[SNHG19]] | +0.61 | +0.31 / +0.68 | both halves | 2e-04 |  |
| [[DCUN1D5]] | +0.61 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[NDUFAF7]] | +0.60 | +0.26 / +0.62 | both halves | 4e-04 |  |
| [[RPL35]] ⚠ | +0.60 | +0.43 / +0.66 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MIR4458HG]] | +0.60 | +0.30 / +0.61 | both halves | 2e-04 |  |
| [[ATP5MJ]] | +0.60 | +0.32 / +0.71 | both halves | 1e-04 | STRING 534 |
| [[DDN-AS1]] | +0.60 | +0.34 / +0.57 | both halves | 1e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HP1BP3]] | -0.58 | -0.32 / -0.62 | both halves | 2e-04 |  |
| [[CHRAC1]] | -0.57 | -0.37 / -0.63 | both halves | 9e-05 |  |
| [[PCNT]] | -0.57 | -0.37 / -0.58 | both halves | 8e-05 |  |
| [[FLII]] | -0.56 | -0.28 / -0.63 | both halves | 3e-04 |  |
| [[RAB1B]] | -0.55 | -0.27 / -0.65 | both halves | 3e-04 |  |
| [[PBRM1]] | -0.55 | -0.11 / -0.64 | ⚠ one half (not replicated) | 0.002 |  |
| [[BAG6]] | -0.54 | -0.36 / -0.62 | both halves | 1e-04 |  |
| [[FGD5-AS1]] | -0.54 | -0.25 / -0.59 | both halves | 4e-04 |  |
| [[CBX5]] | -0.52 | -0.19 / -0.55 | ⚠ one half (not replicated) | 8e-04 |  |
| [[SRRM2]] | -0.52 | -0.17 / -0.58 | ⚠ one half (not replicated) | 0.001 |  |
| [[CNOT3]] | -0.51 | -0.18 / -0.56 | ⚠ one half (not replicated) | 1e-03 |  |
| [[HNRNPUL1]] | -0.51 | -0.17 / -0.62 | ⚠ one half (not replicated) | 0.001 |  |
| [[VEZF1]] | -0.51 | -0.31 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLIRP's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.563). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-43.6, -23.9); signed map (-35.2, 6.4). **Vector** length 57.0, 16.8% of its response variance represented; |z| ≥ 3 in 663 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +1.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | -2.9 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | -2.8 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | -2.5 | +7.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -2.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | SRA stem-loop interacting RNA binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:77,708,071-77,761,104 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DC50; previously C14orf156 |
| Gene groups (HGNC) | RNA binding motif containing; LRPPRC:SLIRP complex subunits |
| Reactome | 3 pathways, smallest: Mitochondrial mRNA modification; Mitochondrial RNA degradation; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZT3](https://www.uniprot.org/uniprotkb/Q9GZT3) (SRA stem-loop-interacting RNA-binding protein, mitochondrial):

> RNA-binding protein that acts as a nuclear receptor corepressor. Probably acts by binding the SRA RNA, and repressing the SRA-mediated nuclear receptor coactivation. Binds the STR7 loop of SRA RNA. Also able to repress glucocorticoid (GR), androgen (AR), thyroid (TR) and VDR-mediated transactivation.

**Summary**, from NCBI Gene [81892](https://www.ncbi.nlm.nih.gov/gene/81892):

> Steroid receptor RNA activator (SRA, or SRA1; MIM 603819) is a complex RNA molecule containing multiple stable stem-loop structures that functions in coactivation of nuclear receptors. SLIRP interacts with stem-loop structure-7 of SRA (STR7) and modulates nuclear receptor transactivation (Hatchell et al., 2006 [PubMed 16762838]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:20495](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20495) · Entrez [81892](https://www.ncbi.nlm.nih.gov/gene/81892) · UniProt [Q9GZT3](https://www.uniprot.org/uniprotkb/Q9GZT3) · Ensembl [ENSG00000119705](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119705)

## Data

Gene col 4105: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4105); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4105, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4105]; `tensor/DDL_lfc|DDL_z.npy` [4105]; `embed/gene_vectors.npy` [4105]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4105 or target_col == 4105). Every well: [[SLIRP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLIRP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
