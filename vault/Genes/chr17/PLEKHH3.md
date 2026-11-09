---
symbol: "PLEKHH3"
type: "gene"
col: 883
ensembl_id: "ENSG00000068137"
name: "pleckstrin homology, MyTH4 and FERM domain containing H3"
location: "17q21.2"
module: 45
arm: "+"
pooled_cpm: 11.67
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# PLEKHH3

*pleckstrin homology, MyTH4 and FERM domain containing H3* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.40× (z +8.3, q 4e-14, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.419× (z -8.3, q 4e-14, down in 28 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL3]] (+0.76, fdr 7e-06), [[GMCL1]] (+0.76, fdr 7e-06), [[EFNA4]] (+0.73, fdr 7e-06); moves opposite to [[AVEN]] (-0.73, fdr 7e-06), [[SNAPC5]] (-0.73, fdr 1e-05), [[GPATCH4]] (-0.72, fdr 7e-06).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CXXC5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 883.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.40×** | +8.3 | 4e-14 | 42/47 (KATO III, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.38×** | +8.2 | 6e-14 | 42/47 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +6.9 | 1e-09 | 40/47 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +5.7 | 2e-06 | 34/47 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +5.1 | 4e-05 | 22/39 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +4.7 | 2e-04 | 25/48 (Hs 766T, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +3.7 | 0.019 | 18/45 (LS 180, A-427, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.024 | 20/48 (PANC-1, A-427, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.58× | +3.1 | 0.11 | 9/44 (Panc 03.27, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | 1.39× | +3.1 | 0.11 | 18/46 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | 1.83× | +3.0 | 0.14 | 11/48 (RKO, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 883.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.419×** | -8.3 | 4e-14 | 28/44 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.458×** | -7.5 | 2e-11 | 33/46 (NCI-H2347, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.639×** | -6.1 | 2e-07 | 28/44 (AsPC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.534×** | -6.0 | 2e-07 | 29/47 (NCI-H460, SW1417, …) | all doses, flat | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.626×** | -4.5 | 7e-04 | 20/39 (HOP62, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.720×** | -4.5 | 7e-04 | 22/48 (A-172, A549, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.646×** | -4.2 | 0.002 | 23/47 (hTERT-HPNE, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.661×** | -3.8 | 0.009 | 21/42 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.700×** | -3.4 | 0.035 | 17/47 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.691×** | -3.4 | 0.035 | 13/23 (SW480, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.714×** | -3.1 | 0.088 | 16/47 (COLO 205, NCI-H661, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | 0.720× | -3.1 | 0.11 | 19/45 (NCI-H2347, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.733× | -3.0 | 0.12 | 13/48 (LOX-IMVI, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 883. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 16.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0708× (z -16.1) |
| [[NCI-H2030 (line)]] | alt | 15.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 12.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 6.95 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0610× (z -15.4) |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0817× (z -11.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -8.5) |
| [[KATO III (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -10.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 9.06 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 9.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 6.29 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0501× (z -11.4) |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0988× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -8.9) |
| [[SW48 (line)]] | wt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0902× (z -8.5) |
| [[A-172 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 883), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL3]] | +0.76 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.76 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[EFNA4]] | +0.73 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[RAB40C]] | +0.72 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[AHDC1]] | +0.71 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[KMT5C]] | +0.71 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.71 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[SLC9A6]] | +0.70 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[KBTBD3]] | +0.70 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[TNNI3]] | +0.70 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SUFU]] | +0.69 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[NFRKB]] | +0.69 | +0.64 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVEN]] | -0.73 | -0.62 / -0.70 | both halves | 7e-06 |  |
| [[SNAPC5]] | -0.73 | -0.70 / -0.52 | both halves | 1e-05 |  |
| [[GPATCH4]] | -0.72 | -0.72 / -0.62 | both halves | 7e-06 |  |
| [[ALG8]] | -0.71 | -0.70 / -0.58 | both halves | 7e-06 |  |
| [[ST7L]] | -0.71 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[UTP20]] | -0.71 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[ZNF655]] | -0.70 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[DNAJC11]] | -0.69 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[DPH5-DT]] | -0.68 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[RNASEH1]] | -0.67 | -0.68 / -0.57 | both halves | 1e-05 |  |
| [[PCBD2]] | -0.66 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[MAPKAP1]] | -0.66 | -0.62 / -0.65 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXXC5]] | B | CXXC5 activity raises PLEKHH3's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 1.45× lower at baseline in the lines without CXXC5 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PLEKHH3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers PLEKHH3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.735). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (6.2, -8.3); signed map (-31.1, 18.7). **Vector** length 116, 29.0% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.5 | +8.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +6.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.8 | +8.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.3 | +5.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.8 | +5.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.5 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.9 | -8.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.9 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.1 | -6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.1 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.3 | -6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology, MyTH4 and FERM domain containing H3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,667,914-42,676,994 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21019 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; FERM domain containing |
| Matched by | ensembl_id |

UniProt [Q7Z736](https://www.uniprot.org/uniprotkb/Q7Z736) carries no function annotation.

**Summary**, from NCBI Gene [79990](https://www.ncbi.nlm.nih.gov/gene/79990):

> Located in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26105](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26105) · Entrez [79990](https://www.ncbi.nlm.nih.gov/gene/79990) · UniProt [Q7Z736](https://www.uniprot.org/uniprotkb/Q7Z736) · Ensembl [ENSG00000068137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068137)

## Data

Gene col 883: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 883); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 883, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 883]; `tensor/DDL_lfc|DDL_z.npy` [883]; `embed/gene_vectors.npy` [883]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 883 or target_col == 883). Every well: [[PLEKHH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
