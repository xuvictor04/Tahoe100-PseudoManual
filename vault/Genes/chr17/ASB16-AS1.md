---
symbol: "ASB16-AS1"
type: "gene"
col: 15520
ensembl_id: "ENSG00000267080"
name: "ASB16 antisense RNA 1"
location: "17q21.31"
module: 142
arm: "+"
pooled_cpm: 8.83
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# ASB16-AS1

*ASB16 antisense RNA 1* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.02× (z +15.4, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.541× (z -6.8, q 5e-09, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STARD3]] (+0.72, fdr 7e-06), [[ADIPOR1]] (+0.66, fdr 2e-05), [[SS18L1]] (+0.65, fdr 8e-06); moves opposite to [[THOC7]] (-0.64, fdr 2e-05), [[TIGD2]] (-0.63, fdr 2e-05), [[DZIP3]] (-0.62, fdr 1e-05).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DSP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15520.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.02×** | +15.4 | 0e+00 | 46/47 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.68×** | +14.4 | 1e-44 | 44/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.39×** | +13.5 | 2e-39 | 45/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.21×** | +8.4 | 4e-15 | 34/44 (SK-MEL-2, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **2.11×** | +7.9 | 3e-13 | 28/38 (CFPAC-1, NCI-H460, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.63×** | +7.6 | 2e-12 | 33/46 (A549, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.88×** | +6.7 | 2e-09 | 6/13 (SW480, CFPAC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +5.4 | 5e-06 | 24/44 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.57×** | +5.0 | 4e-05 | 16/34 (CFPAC-1, SW 900, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.84×** | +4.8 | 8e-05 | 19/40 (SW480, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +4.8 | 8e-05 | 22/47 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.53×** | +4.7 | 1e-04 | 19/47 (NCI-H23, A-427, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.53×** | +4.5 | 3e-04 | 21/44 (NCI-H460, A549, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.74×** | +4.4 | 5e-04 | 16/44 (A498, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.45×** | +4.1 | 0.001 | 17/47 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.48×** | +4.1 | 0.002 | 12/42 (LS 180, Panc 03.27, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.66×** | +4.0 | 0.002 | 13/46 (A498, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.006 | 15/46 (HOP62, COLO 205, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.009 | 15/47 (CFPAC-1, HCT15, …) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.51×** | +3.2 | 0.033 | 12/37 (SW1417, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.85×** | +3.0 | 0.058 | 4/41 (CFPAC-1, PANC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15520.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.541×** | -6.8 | 5e-09 | 30/46 (NCI-H1573, SW480, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.550×** | -6.3 | 1e-07 | 26/44 (A-427, NCI-H23, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.570×** | -6.0 | 3e-07 | 25/46 (A-427, LoVo, …) | two highest doses | cell-cycle shift (explains ~25% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.390×** | -4.7 | 4e-04 | 22/47 (Panc 03.27, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.730×** | -3.5 | 0.051 | 14/47 (A-172, A498, …) | all doses, flat | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.812×** | -3.3 | 0.092 | 15/43 (A-427, PANC-1, …) | all doses, flat | composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.525× | -3.2 | 0.11 | 13/43 (Panc 03.27, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.762× | -3.0 | 0.18 | 16/47 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15520. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 18.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -12.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.139× (z -11.7) |
| [[SW480 (line)]] | alt | 9.51 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.39× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 7.59 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.73× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 6.60 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.67× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 8.02 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.87× (z +9.4) | — |
| [[C32 (line)]] | wt | 5.44 | 0 | 1 | — | [[Hesperidin (drug)]] 0.5 µM 0.0805× (z -8.8) |
| [[HCT15 (line)]] | alt | 9.97 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0981× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -9.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 5.80 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15520), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STARD3]] | +0.72 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ADIPOR1]] | +0.66 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[SS18L1]] | +0.65 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[POLR2F]] | +0.63 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[DIP2A]] | +0.63 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ZMYND19]] | +0.62 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[DHRS1]] | +0.62 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[CERS5]] | +0.62 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[UNC45A]] | +0.62 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[IFI27L1]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[CSNK1G2]] | +0.62 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[TANGO2]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC7]] | -0.64 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[TIGD2]] | -0.63 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[DZIP3]] | -0.62 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[RAD50]] | -0.62 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[BMI1]] | -0.62 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[ZNF620]] | -0.61 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ZXDB]] | -0.60 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[BBS10]] | -0.59 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.59 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[ZNF462]] | -0.59 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[DARS1]] | -0.59 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[AASDHPPT]] | -0.58 | -0.52 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSP]] | B | DSP activity raises ASB16-AS1's level | lines that do not express DSP (17) vs lines expressing it (33) | 1.26× lower at baseline in the lines without DSP | 0.016 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, GRB7, SFN; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.740). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.3, -2.8); signed map (-44.0, 2.6). **Vector** length 74.9, 14.3% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +4.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.1 | +4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | +14.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +2.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.5 | +15.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.2 | +2.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +3.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.1 | +4.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.5 | -6.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.4 | -6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.9 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.8 | -6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -0.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | ASB16 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q21.31 — chr17:44,175,968-44,186,723 (-) |
| Ensembl biotype | lncRNA |
| Also known as | DKFZp762C2414; previously C17orf65 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q495Z4](https://www.uniprot.org/uniprotkb/Q495Z4) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25442](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25442) · Entrez [339201](https://www.ncbi.nlm.nih.gov/gene/339201) · UniProt [Q495Z4](https://www.uniprot.org/uniprotkb/Q495Z4) · Ensembl [ENSG00000267080](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267080)

## Data

Gene col 15520: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15520); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15520, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15520]; `tensor/DDL_lfc|DDL_z.npy` [15520]; `embed/gene_vectors.npy` [15520]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15520 or target_col == 15520). Every well: [[ASB16-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASB16-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
