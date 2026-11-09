---
symbol: "LMNB1-DT"
type: "gene"
col: 14734
ensembl_id: "ENSG00000251072"
name: "LMNB1 divergent transcript"
location: "5q23.2"
module: 35
arm: "+"
pooled_cpm: 2.06
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# LMNB1-DT

*LMNB1 divergent transcript* — 5q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 22.7× (z +25.9, q 0e+00, up in 10 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.34× (z +23.4, q 0e+00, up in 30 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.856× (z -4.5, q 0.003, down in 17 of 46 measured lines) ⚠ position not correctable. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.606× (z -3.8, q 0.045, down in 7 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (A-427 0.0964×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPAG5-AS1]] (+0.73, fdr 7e-06), [[SPEN-AS1]] (+0.71, fdr 7e-06), [[HEATR4]] (+0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14734.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **22.7×** | +25.9 | 0e+00 | 10/10 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **24.5×** | +24.1 | 0e+00 | 3/3 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.34×** | +23.4 | 0e+00 | 30/30 (A498, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.76×** | +18.3 | 0e+00 | 27/32 (HOP62, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **10.8×** | +18.3 | 0e+00 | 4/4 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.72×** | +9.9 | 4e-21 | 15/24 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.90×** | +8.8 | 8e-17 | 15/27 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.43×** | +7.4 | 1e-11 | 17/33 (HEC-1-A, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.63×** | +7.3 | 2e-11 | 21/37 (HS-578T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.32×** | +6.3 | 1e-08 | 17/30 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.50×** | +5.4 | 3e-06 | 1/4 (PANC-1) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +5.2 | 1e-05 | 7/43 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +4.7 | 1e-04 | 3/11 (NCI-H2347, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.75×** | +4.6 | 1e-04 | 7/41 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.56×** | +3.7 | 0.009 | 4/20 (HS-578T, NCI-H460, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.046 | 5/34 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +3.1 | 0.046 | 6/37 (CFPAC-1, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14734.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (A-427 0.0964×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.856× | -4.5 | 0.003 | 17/46 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.606×** | -3.8 | 0.045 | 7/31 (SK-MEL-2, NCI-H2347, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.662× | -3.4 | 0.11 | 6/41 (SW 900, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14734. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 2.60 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 63.3× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 8.84× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 2.37 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 24.6× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.58× (z +9.8) | — |
| [[A498 (line)]] | wt | 1.64 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.4× (z +12.2) | — |
| [[A-172 (line)]] | wt | 2.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +10.2) | — |
| [[A-427 (line)]] | wt | 6.01 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0964× (z -8.6) |
| [[A549 (line)]] | wt | 1.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.0× (z +8.8) | — |
| [[C32 (line)]] | wt | 2.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 3.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.26× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 1.51 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 56.0× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 2.83 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.1× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 2.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 1.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.0× (z +8.6) | — |
| [[SW480 (line)]] | alt | 1.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.12× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.828 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.797 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.645 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.916 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.647 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.999 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.829 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.983 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14734), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG5-AS1]] | +0.73 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[SPEN-AS1]] | +0.71 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[HEATR4]] | +0.71 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[RAD9B]] | +0.70 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[FBXO43]] | +0.70 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[PJVK]] | +0.69 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[MALINC1]] | +0.68 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[PPP1R15B-AS1]] | +0.67 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[LINC00863]] | +0.67 | +0.69 / +0.42 | both halves | 4e-05 |  |
| [[RELA-DT]] | +0.67 | +0.61 / +0.58 | both halves | 8e-06 | same gene group |
| [[DEPDC4]] | +0.66 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[MEIOC]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LMNB1-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GNG4]] | B | GNG4 activity raises LMNB1-DT's level | lines that do not express GNG4 (20) vs lines expressing it (30) | 1.35× lower at baseline in the lines without GNG4 | 0.048 | ⚠ within organs, on part of the lines; also absent: OLFM1, JPH3, LRRC4B |
| [[ZPLD1]] | B | ZPLD1 activity lowers LMNB1-DT's level | lines that do not express ZPLD1 (7) vs lines expressing it (43) | 1.00× higher at baseline in the lines without ZPLD1 | 0.072 | ⚠ within organs, on part of the lines; also absent: STAT4, ABCA12, ANKRD7; maybe low, not absent |
| [[AP3B2]] | B | AP3B2 activity raises LMNB1-DT's level | lines that do not express AP3B2 (15) vs lines expressing it (35) | 1.39× lower at baseline in the lines without AP3B2 | 0.081 | ⚠ within organs, on part of the lines; also absent: MAPK8IP2, MED12L, HRK; maybe low, not absent |
| [[SLC37A2]] | B | SLC37A2 activity strengthens LMNB1-DT's drug response | lines that do not express SLC37A2 (9) vs lines expressing it (30) | the lines without SLC37A2 respond 0.64× as strongly (z diff +1.16); strongest at Homoharringtonine 5 µM: 3.23x vs 5.17x (z diff +1.9) | 0.097 | ⚠ within organs, on part of the lines; also absent: FAM111B; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.678). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (13.8, 23.3); signed map (30.5, 1.8). **Vector** length 48.4, 6.73% of its response variance represented; |z| ≥ 3 in 884 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +23.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +18.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +24.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +18.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +25.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +5.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +1.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +3.1 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -0.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +1.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -4.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | LMNB1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q23.2 — chr5:126,751,963-126,776,486 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53089](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53089) · Entrez [102723557](https://www.ncbi.nlm.nih.gov/gene/102723557) · Ensembl [ENSG00000251072](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251072)

## Data

Gene col 14734: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14734); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14734, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14734]; `tensor/DDL_lfc|DDL_z.npy` [14734]; `embed/gene_vectors.npy` [14734]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14734 or target_col == 14734). Every well: [[LMNB1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMNB1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
