---
symbol: "DPH1-AS1"
type: "gene"
col: 15403
ensembl_id: "ENSG00000263050"
name: "DPH1 antisense RNA 1"
location: "17p13.3"
module: 171
arm: "-"
pooled_cpm: 2.51
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# DPH1-AS1

*DPH1 antisense RNA 1* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.01× (z +19.3, q 0e+00, up in 25 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Radotinib (drug)]] 5 µM: 0.611× (z -5.9, q 3e-06, down in 18 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASGR1]] (+0.65, fdr 7e-06), [[ORAI2]] (+0.62, fdr 1e-05), [[GASAL1]] (+0.61, fdr 8e-06); moves opposite to [[NAPB]] (-0.65, fdr 7e-06), [[MRS2]] (-0.63, fdr 7e-06), [[ATP5F1C]] (-0.62, fdr 1e-05).
> It sits in the **-** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LONRF3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15403.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.01×** | +19.3 | 0e+00 | 25/33 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +10.1 | 1e-21 | 17/28 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.54×** | +7.9 | 5e-13 | 19/32 (NCI-H460, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.29×** | +7.0 | 3e-10 | 14/32 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.22×** | +6.5 | 1e-08 | 20/37 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.04×** | +5.8 | 6e-07 | 0/3 | inconsistent across doses | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.70×** | +4.5 | 5e-04 | 9/42 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.58×** | +3.9 | 0.007 | 8/41 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.49×** | +3.4 | 0.045 | 8/44 (NCI-H460, BT-474, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.48×** | +3.3 | 0.052 | 5/19 (A-172, NCI-H460, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.44× | +3.1 | 0.10 | 12/38 (NCI-H460, BT-474, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.43× | +3.0 | 0.11 | 13/44 (NCI-H460, SW480, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15403.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **0.611×** | -5.9 | 3e-06 | 18/40 (NCI-H23, HOP62, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.842× | -5.0 | 1e-04 | 24/44 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.624×** | -3.7 | 0.045 | 9/42 (SHP-77, AsPC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.658×** | -3.5 | 0.061 | 14/41 (NCI-H23, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.747×** | -3.5 | 0.061 | 10/39 (CFPAC-1, SW 900, …) | top dose only | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.680× | -3.2 | 0.11 | 10/43 (SW 900, LOX-IMVI, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.685× | -3.2 | 0.12 | 14/38 (NCI-H1573, A498, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.764× | -3.1 | 0.13 | 9/40 (SHP-77, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15403. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.10 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 29.5× (z +16.7) | — |
| [[SHP-77 (line)]] | alt | 24.6 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 2.42 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 7.70 | 0 | 2 (1 ⚠) | — | [[Peretinoin (drug)]] 5 µM 0.0828× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 1.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.2× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 2.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.80× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 1.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 2.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.12× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 0.794 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.0× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.98× (z +9.9) | — |
| [[SW480 (line)]] | alt | 1.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +8.7) | — |
| [[A-172 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.669 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.621 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.850 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15403), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASGR1]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ORAI2]] | +0.62 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[GASAL1]] | +0.61 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[EGR3]] | +0.61 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[HES1]] | +0.60 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[EGR2]] | +0.60 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[HIVEP2-DT]] | +0.59 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[MMP25]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ANGPT2]] | +0.59 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[EGR1]] | +0.59 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[GNG4]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAPB]] | -0.65 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[MRS2]] | -0.63 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[ATP5F1C]] | -0.62 | -0.64 / -0.57 | both halves | 1e-05 |  |
| [[RTCA]] | -0.61 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[MINDY3]] | -0.60 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[CROT]] | -0.60 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[SNX4]] | -0.59 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[SACM1L]] | -0.58 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[MBD2]] | -0.58 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[TRAPPC2]] | -0.58 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[COPS7B]] | -0.58 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[LRIG2]] | -0.57 | -0.61 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LONRF3]] | B | LONRF3 activity lowers DPH1-AS1's level | lines that do not express LONRF3 (10) vs lines expressing it (40) | 1.32× higher at baseline in the lines without LONRF3 | 0.009 | ⚠ within organs, on part of the lines; also absent: AP1G2, TNFRSF10A-DT, C9orf64 |
| [[NFATC1]] | B | NFATC1 activity raises DPH1-AS1's level | lines that do not express NFATC1 (11) vs lines expressing it (39) | 1.02× lower at baseline in the lines without NFATC1 | 0.035 | ⚠ within organs, on part of the lines; also absent: RIMKLB, HOMER2, RASGEF1C |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **-** arm (projection on the module's main direction -0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (40.2, -10.6); signed map (7.8, 26.5). **Vector** length 64.6, 10.2% of its response variance represented; |z| ≥ 3 in 1,188 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +19.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +10.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.9 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +1.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.3 | +2.0 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -5.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | -3.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.0 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | DPH1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17p13.3 — chr17:2,043,475-2,044,968 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-667K14.3 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56040](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56040) · Entrez [123706529](https://www.ncbi.nlm.nih.gov/gene/123706529) · Ensembl [ENSG00000263050](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000263050)

## Data

Gene col 15403: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15403); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15403, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15403]; `tensor/DDL_lfc|DDL_z.npy` [15403]; `embed/gene_vectors.npy` [15403]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15403 or target_col == 15403). Every well: [[DPH1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPH1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
