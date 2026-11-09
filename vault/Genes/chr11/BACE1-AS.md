---
symbol: "BACE1-AS"
type: "gene"
col: 15921
ensembl_id: "ENSG00000278768"
name: "BACE1 antisense RNA"
location: "11q23.3"
module: 48
arm: "-"
pooled_cpm: 4.35
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 24
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# BACE1-AS

*BACE1 antisense RNA* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.21× (z +6.8, q 4e-09, up in 20 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 1.51× (z +4.1, q 0.004, up in 7 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.337× (z -10.8, q 3e-24, down in 28 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.349× (z -10.4, q 8e-23, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGO]] (+0.74, fdr 7e-06), [[YWHAE]] (+0.65, fdr 7e-06), [[NONO]] (+0.65, fdr 5e-05); moves opposite to [[ATOX1]] (-0.66, fdr 1e-05), [[UBL5]] (-0.66, fdr 1e-05), [[COPS9]] (-0.66, fdr 1e-05).
> It sits in the **-** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SPATA17]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15921.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.21×** | +6.8 | 4e-09 | 20/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +6.7 | 8e-09 | 6/8 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +5.5 | 8e-06 | 13/22 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +4.8 | 2e-04 | 6/13 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.51×** | +4.1 | 0.004 | 7/47 (HOP62, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15921.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.337×** | -10.8 | 3e-24 | 28/35 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.349×** | -10.4 | 8e-23 | 34/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.516×** | -9.2 | 5e-18 | 28/36 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.481×** | -7.2 | 6e-11 | 24/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.481×** | -7.2 | 6e-11 | 25/45 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.496×** | -6.9 | 5e-10 | 28/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.524×** | -6.4 | 1e-08 | 22/43 (SW480, SNU-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.345×** | -5.5 | 3e-06 | 19/41 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.574×** | -5.3 | 9e-06 | 20/34 (C-33 A, LS 180, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.597×** | -4.9 | 6e-05 | 21/43 (NCI-H23, NCI-H2030, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.607×** | -4.6 | 2e-04 | 15/42 (HT-29, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.636×** | -4.4 | 4e-04 | 11/47 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.642×** | -4.4 | 6e-04 | 17/47 (NCI-H23, SW1417, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.634×** | -4.3 | 7e-04 | 15/24 (HEC-1-A, HCT15, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.660×** | -4.1 | 0.002 | 13/43 (KATO III, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.463×** | -4.0 | 0.002 | 16/36 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.475×** | -3.8 | 0.004 | 9/34 (NCI-H1792, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.758×** | -3.8 | 0.004 | 11/46 (LS 180, KATO III, …) | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.781×** | -3.4 | 0.017 | 9/45 (MIA PaCa-2, CHP-212, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.725×** | -3.2 | 0.038 | 10/38 (PANC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15921. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.76 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.129× (z -11.3) |
| [[SW480 (line)]] | alt | 6.36 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0399× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0663× (z -14.8) |
| [[CFPAC-1 (line)]] | alt | 5.08 | 0 | 2 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0547× (z -11.9) |
| [[KATO III (line)]] | alt | 7.94 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0434× (z -14.3) |
| [[LS 180 (line)]] | wt | 3.78 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -9.7) |
| [[A-427 (line)]] | wt | 2.89 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0422× (z -8.7) ⚠ cell-cycle shift, explains ~95% of this change |
| [[C-33 A (line)]] | alt | 8.73 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0849× (z -9.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HOP62 (line)]] | alt | 3.04 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0825× (z -9.0) |
| [[Hs 766T (line)]] | wt | 5.64 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0832× (z -9.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 8.49 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -8.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[MIA PaCa-2 (line)]] | alt | 5.44 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0856× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 6.94 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.120× (z -8.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 3.97 | 0 | 1 | — | [[Vismodegib (drug)]] 0.5 µM 0.0749× (z -8.5) |
| [[A-172 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15921), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGO]] | +0.74 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[YWHAE]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[NONO]] | +0.65 | +0.40 / +0.72 | both halves | 5e-05 |  |
| [[TEX261]] | +0.65 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[OCRL]] | +0.64 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[PRRC2A]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[PRELID3B]] | +0.63 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[LIN7C]] | +0.62 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[SF3A1]] | +0.62 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[EWSR1]] | +0.62 | +0.46 / +0.69 | both halves | 2e-05 |  |
| [[SRSF3]] | +0.61 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CCDC113]] | +0.60 | +0.49 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATOX1]] | -0.66 | -0.57 / -0.65 | both halves | 1e-05 |  |
| [[UBL5]] | -0.66 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[COPS9]] | -0.66 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[ROMO1]] | -0.64 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[ATP5MK]] | -0.64 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[C1orf122]] | -0.64 | -0.37 / -0.61 | both halves | 7e-05 |  |
| [[ULBP2]] | -0.63 | -0.35 / -0.65 | both halves | 1e-04 |  |
| [[SEC61G]] | -0.63 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[DTX2P1-UPK3BP1-PMS2P11]] | -0.62 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[TMEM165]] | -0.62 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[COX6C]] | -0.62 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[OST4]] | -0.61 | -0.46 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPATA17]] | C | SPATA17 activity raises BACE1-AS's level | lines that do not express SPATA17 (3) vs lines expressing it (47) | 1.60× lower at baseline in the lines without SPATA17 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ITPR2-AS1, ITPR2, SYCP2L; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **-** arm (projection on the module's main direction -0.648). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-47.5, -23.5); signed map (0.1, -33.9). **Vector** length 49.1, 5.71% of its response variance represented; |z| ≥ 3 in 1,234 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.0 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.8 | -3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | -1.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +0.9 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +0.8 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -9.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.6 | -10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -3.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.4 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -6.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.2 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | BACE1 antisense RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q23.3 — chr11:117,288,453-117,293,578 (+) |
| Ensembl biotype | lncRNA |
| Also known as | FJ573250, NCRNA00177, BACE1-AS1; previously BACE1AS |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100379571](https://www.ncbi.nlm.nih.gov/gene/100379571):

> This gene encodes an unspliced long non-coding RNA transcribed from the opposite strand to BACE1. The encoded transcript is thought to form an RNA duplex with BACE1 mRNA thereby regulating its expression and is also thought to promote post-transcriptional feed-forward regulation of BACE1. This may lead to increased levels of beta amyloid and increased senile plaque deposition, and therefore may play a role in the pathophysiology of Alzheimer's disease. [provided by RefSeq, Jan 2015]

**Accessions** — [HGNC:37125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37125) · Entrez [100379571](https://www.ncbi.nlm.nih.gov/gene/100379571) · Ensembl [ENSG00000278768](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000278768)

## Data

Gene col 15921: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15921); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15921, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15921]; `tensor/DDL_lfc|DDL_z.npy` [15921]; `embed/gene_vectors.npy` [15921]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15921 or target_col == 15921). Every well: [[BACE1-AS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BACE1-AS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
