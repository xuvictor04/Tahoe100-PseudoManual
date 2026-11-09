---
symbol: "DLEU7"
type: "gene"
col: 11770
ensembl_id: "ENSG00000186047"
name: "deleted in lymphocytic leukemia 7"
location: "13q14.3"
module: 75
arm: "+"
pooled_cpm: 5.21
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# DLEU7

*deleted in lymphocytic leukemia 7* — 13q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.81× (z +16.9, q 0e+00, up in 36 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.699× (z -4.1, q 0.012, down in 14 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Temsirolimus (drug)]] 0.5 µM in 1 line (PANC-1 0.0735×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.184×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (COLO 205 0.125×; ⚠ cell-cycle shift, explains ~31% of this change); [[Dihydroartemisinin (drug)]] 0.5 µM in 1 line (KATO III 0.0726×); [[Dexamethasone (drug)]] 0.5 µM in 1 line (HS-578T 0.0521×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R9A-AS1]] (+0.80, fdr 7e-06), [[SLC3A1]] (+0.78, fdr 7e-06), [[DPP6]] (+0.77, fdr 7e-06); moves opposite to [[FBXW2]] (-0.64, fdr 1e-05).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11770.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.81×** | +16.9 | 0e+00 | 36/41 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +11.3 | 2e-27 | 20/26 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +9.8 | 2e-20 | 25/36 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +8.4 | 7e-15 | 6/9 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +6.5 | 8e-09 | 4/14 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +5.8 | 7e-07 | 12/31 (HOP62, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +5.1 | 2e-05 | 16/44 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.9 | 8e-05 | 11/46 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.7 | 2e-04 | 12/38 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +4.0 | 0.004 | 11/38 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.068 | 4/45 (AsPC-1, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.068 | 10/44 (PANC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.30×** | +3.1 | 0.095 | 11/37 (HEC-1-A, LOX-IMVI, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.095 | 4/43 (KATO III, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11770.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Temsirolimus (drug)]] 0.5 µM in 1 line (PANC-1 0.0735×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.184×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (COLO 205 0.125×; ⚠ cell-cycle shift, explains ~31% of this change); [[Dihydroartemisinin (drug)]] 0.5 µM in 1 line (KATO III 0.0726×); [[Dexamethasone (drug)]] 0.5 µM in 1 line (HS-578T 0.0521×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.699×** | -4.1 | 0.012 | 14/47 (COLO 205, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.901× | -4.1 | 0.012 | 14/48 (HT-29, SW 900, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.708×** | -4.0 | 0.014 | 18/46 (COLO 205, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.748× | -3.3 | 0.12 | 12/44 (COLO 205, LS 180, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.757× | -3.2 | 0.16 | 11/46 (COLO 205, LS 180, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11770. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.35 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -10.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 3.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.27× (z +9.1) | — |
| [[C32 (line)]] | wt | 4.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -10.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HEC-1-A (line)]] | alt | 9.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 4.43 | 0 | 1 | — | [[Gallic acid (drug)]] 0.05 µM 0.0936× (z -9.0) |
| [[HS-578T (line)]] | alt | 3.33 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.5 µM 0.0521× (z -9.2) |
| [[KATO III (line)]] | alt | 5.18 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0726× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 3.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.43× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 3.92 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0735× (z -13.3) |
| [[A-172 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11770), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R9A-AS1]] | +0.80 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[SLC3A1]] | +0.78 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[DPP6]] | +0.77 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.76 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.76 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[GRM7]] | +0.76 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[G2E3-AS1]] | +0.76 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[MALRD1]] | +0.76 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[TTN]] | +0.76 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[RBMS3-AS3]] | +0.75 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[LINC02694]] | +0.75 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.75 | +0.64 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW2]] | -0.64 | -0.61 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DLEU7's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC01170]] | B | LINC01170 activity raises DLEU7's level | lines that do not express LINC01170 (13) vs lines expressing it (37) | 1.35× lower at baseline in the lines without LINC01170 | 0.079 | ⚠ within organs, on part of the lines; also absent: ZNF608, ENSG00000249526; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.798). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.1, 27.0); signed map (34.5, 12.3). **Vector** length 62.1, 8.86% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +16.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +11.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -2.6 | -4.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.2 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -1.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -4.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | deleted in lymphocytic leukemia 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.3 — chr13:50,519,364-50,843,939 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ44882 |
| Matched by | ensembl_id |

UniProt [Q6UYE1](https://www.uniprot.org/uniprotkb/Q6UYE1) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:17567](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17567) · Entrez [220107](https://www.ncbi.nlm.nih.gov/gene/220107) · UniProt [Q6UYE1](https://www.uniprot.org/uniprotkb/Q6UYE1) · Ensembl [ENSG00000186047](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186047)

## Data

Gene col 11770: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11770); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11770, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11770]; `tensor/DDL_lfc|DDL_z.npy` [11770]; `embed/gene_vectors.npy` [11770]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11770 or target_col == 11770). Every well: [[DLEU7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLEU7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
