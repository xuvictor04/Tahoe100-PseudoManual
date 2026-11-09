---
symbol: "KLHL21"
type: "gene"
col: 8513
ensembl_id: "ENSG00000162413"
name: "kelch like family member 21"
location: "1p36.31"
module: 101
arm: "+"
pooled_cpm: 18.17
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 28
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# KLHL21

*kelch like family member 21* — 1p36.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.27× (z +19.2, q 0e+00, up in 42 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 0.5 µM in 1 line (LoVo 0.182×); [[Tucidinostat (drug)]] 0.5 µM in 1 line (COLO 205 0.0645×; ⚠ cell-cycle shift, explains ~0% of this change); [[Elagolix sodium (drug)]] 0.5 µM in 1 line (H4 0.0695×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR45]] (+0.64, fdr 1e-05), [[JOSD1]] (+0.63, fdr 7e-06), [[FAM83G]] (+0.57, fdr 1e-05); moves opposite to [[POT1]] (-0.57, fdr 1e-05), [[ATG4C]] (-0.57, fdr 3e-05), [[ATP5MC3]] (-0.55, fdr 2e-05, ⚠ ATP5MC3 in the vector space only through flagged drug-doses), [[SPATA6]] (-0.55, fdr 1e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PPP1R18]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8513.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.27×** | +19.2 | 0e+00 | 42/46 (AsPC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.00×** | +15.9 | 0e+00 | 42/45 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +11.3 | 3e-27 | 40/45 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.67×** | +11.3 | 3e-27 | 43/47 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.73×** | +11.1 | 2e-26 | 31/47 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.06×** | +8.3 | 1e-14 | 32/48 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.92×** | +7.5 | 5e-12 | 35/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.87×** | +7.2 | 4e-11 | 35/47 (HCT15, SW480, …) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +7.1 | 1e-10 | 32/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.79×** | +6.7 | 1e-09 | 31/47 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.85×** | +6.7 | 1e-09 | 33/46 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +6.3 | 1e-08 | 29/44 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +6.2 | 3e-08 | 31/47 (SW480, HCT15, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.70×** | +6.1 | 5e-08 | 30/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.65×** | +5.7 | 4e-07 | 32/48 (HS-578T, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.79×** | +4.7 | 7e-05 | 26/44 (Hs 766T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.45×** | +4.3 | 7e-04 | 20/45 (hTERT-HPNE, SNU-423, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8513.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 0.5 µM in 1 line (LoVo 0.182×); [[Tucidinostat (drug)]] 0.5 µM in 1 line (COLO 205 0.0645×; ⚠ cell-cycle shift, explains ~0% of this change); [[Elagolix sodium (drug)]] 0.5 µM in 1 line (H4 0.0695×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | 0.553× | -3.6 | 0.21 | 16/47 (HOP62, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | 0.597× | -3.1 | 0.55 | 12/45 (H4, HEC-1-A, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8513. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.7 | 10 (3 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 8.74× (z +11.5) | — |
| [[HS-578T (line)]] | alt | 29.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.98× (z +19.6) | — |
| [[COLO 205 (line)]] | alt | 11.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 30.3× (z +17.7) | [[Tucidinostat (drug)]] 0.5 µM 0.0645× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 18.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.53× (z +14.5) | — |
| [[PANC-1 (line)]] | alt | 14.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +16.1) | — |
| [[A498 (line)]] | wt | 9.86 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.64× (z +16.7) | — |
| [[HOP62 (line)]] | alt | 20.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +14.6) | — |
| [[hTERT-HPNE (line)]] | wt | 20.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.06× (z +14.4) | — |
| [[NCI-H2347 (line)]] | alt | 16.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +14.0) | — |
| [[SNU-423 (line)]] | alt | 26.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +15.4) | — |
| [[AsPC-1 (line)]] | alt | 33.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.45× (z +20.3) | — |
| [[C32 (line)]] | wt | 15.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.76× (z +14.2) | — |
| [[CFPAC-1 (line)]] | alt | 25.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.92× (z +17.0) | — |
| [[HepG2_C3A (line)]] | wt | 63.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +12.2) | — |
| [[HT-29 (line)]] | alt | 15.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +11.4) | — |
| [[LoVo (line)]] | wt | 33.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +8.6) | [[Cobimetinib (drug)]] 0.5 µM 0.182× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 29.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 16.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 17.3× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 11.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 40.2 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.82× (z +13.1) | — |
| [[SW 900 (line)]] | alt | 13.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +11.0) | — |
| [[H4 (line)]] | wt | 10.3 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0695× (z -9.1) |
| [[Hs 766T (line)]] | wt | 35.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +11.1) | — |
| [[J82 (line)]] | alt | 15.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +13.1) | — |
| [[KATO III (line)]] | alt | 21.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.22× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 8.16 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.11× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +8.6) | — |
| [[SW480 (line)]] | alt | 15.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.87× (z +11.5) | — |
| [[A-172 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8513), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR45]] | +0.64 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[JOSD1]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[FAM83G]] | +0.57 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[TRIM8]] | +0.57 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[YOD1]] | +0.56 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[CLCF1]] | +0.55 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[MAFK]] | +0.54 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[MDGA1]] | +0.53 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[SNX9]] | +0.53 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[HOMER3]] | +0.53 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[MOB3C]] | +0.53 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[CLCN7]] | +0.53 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POT1]] | -0.57 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[ATG4C]] | -0.57 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[ATP5MC3]] ⚠ | -0.55 | -0.46 / -0.52 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SPATA6]] | -0.55 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[RAD54B]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[FSBP]] | -0.52 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[CTDSPL2]] | -0.51 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[AP2S1]] | -0.51 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[GCHFR]] | -0.51 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[SMAP2]] | -0.51 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[TTC23]] | -0.50 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[MTF2]] | -0.50 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[IMMT]] | -0.50 | -0.43 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R18]] | B | PPP1R18 activity raises KLHL21's level | lines that do not express PPP1R18 (5) vs lines expressing it (45) | 1.75× lower at baseline in the lines without PPP1R18 | 0.017 | ⚠ within organs, on part of the lines; also absent: PER3, VIM-AS1, UPP1; maybe low, not absent |
| [[LINC00520]] | B | LINC00520 activity raises KLHL21's level | lines that do not express LINC00520 (31) vs lines expressing it (19) | 1.31× lower at baseline in the lines without LINC00520 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, LINC00589, LINC02930 |
| [[SPHK1]] | B | SPHK1 activity raises KLHL21's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 1.41× lower at baseline in the lines without SPHK1 | 0.096 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.542). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.7, -4.0); signed map (3.8, 33.5). **Vector** length 107, 28.4% of its response variance represented; |z| ≥ 3 in 1,214 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.9 | +15.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +11.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +19.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.8 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.8 | +4.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.5 | +3.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.5 | -3.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | +0.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -3.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.9 | -1.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.9 | -2.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.31 — chr1:6,590,724-6,614,607 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0469 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJP4](https://www.uniprot.org/uniprotkb/Q9UJP4) (Kelch-like protein 21):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complex required for efficient chromosome alignment and cytokinesis. The BCR(KLHL21) E3 ubiquitin ligase complex regulates localization of the chromosomal passenger complex (CPC) from chromosomes to the spindle midzone in anaphase and mediates the ubiquitination of AURKB. Ubiquitination of AURKB by BCR(KLHL21) E3 ubiquitin ligase complex may not lead to its degradation by the proteasome.

**Summary**, from NCBI Gene [9903](https://www.ncbi.nlm.nih.gov/gene/9903):

> Enables cullin family protein binding activity. Contributes to ubiquitin-protein transferase activity. Involved in chromosome passenger complex localization to spindle midzone; protein ubiquitination; and regulation of cytokinesis. Located in centrosome and polar microtubule. Part of Cul3-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29041](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29041) · Entrez [9903](https://www.ncbi.nlm.nih.gov/gene/9903) · UniProt [Q9UJP4](https://www.uniprot.org/uniprotkb/Q9UJP4) · Ensembl [ENSG00000162413](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162413)

## Data

Gene col 8513: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8513); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8513, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8513]; `tensor/DDL_lfc|DDL_z.npy` [8513]; `embed/gene_vectors.npy` [8513]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8513 or target_col == 8513). Every well: [[KLHL21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
