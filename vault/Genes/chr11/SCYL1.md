---
symbol: "SCYL1"
type: "gene"
col: 6603
ensembl_id: "ENSG00000142186"
name: "SCY1 like pseudokinase 1"
location: "11q13.1"
module: 3
arm: "+"
pooled_cpm: 31.67
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SCYL1

*SCY1 like pseudokinase 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.14× (z +14.5, q 1e-44, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.629× (z -8.5, q 1e-14, down in 23 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.664× (z -7.5, q 2e-11, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATG4B]] (+0.64, fdr 2e-05), [[YTHDF1]] (+0.63, fdr 1e-05), [[PKD1]] (+0.60, fdr 1e-05); moves opposite to [[SLC12A2-DT]] (-0.52, fdr 5e-05), [[VBP1]] (-0.50, fdr 2e-04), [[ACADM]] (-0.50, fdr 6e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6603.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.14×** | +14.5 | 1e-44 | 44/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.68×** | +9.9 | 1e-20 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +6.0 | 4e-07 | 28/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **1.35×** | +5.7 | 2e-06 | 25/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +5.1 | 5e-05 | 23/48 (HOP62, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.64×** | +4.9 | 9e-05 | 24/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +4.9 | 9e-05 | 23/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | **1.30×** | +4.8 | 1e-04 | 24/47 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.2 | 0.001 | 20/43 (PANC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.25×** | +4.2 | 0.001 | 19/48 (SW480, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.24×** | +4.1 | 0.002 | 18/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +4.0 | 0.003 | 14/48 (SW480, NCI-H1792, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.16× | +3.8 | 0.007 | 17/47 (A498, A549, …) | top dose only | composition shift; position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.015 | 12/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.019 | 14/48 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.020 | 10/48 (Hs 766T, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.031 | 15/48 (J82, CFPAC-1, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.070 | 10/48 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.077 | 5/48 (PANC-1, KATO III, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6603.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.629×** | -8.5 | 1e-14 | 23/36 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.664×** | -7.5 | 2e-11 | 32/47 (HOP62, SW 900, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.760×** | -7.2 | 2e-10 | 29/48 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.721×** | -6.0 | 3e-07 | 25/48 (HOP62, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.746×** | -5.6 | 2e-06 | 22/48 (HOP62, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.808×** | -5.5 | 3e-06 | 24/47 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -4.4 | 9e-04 | 1/48 (AsPC-1) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.849× | -4.3 | 0.001 | 16/48 (RPMI-7951, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.854× | -4.2 | 0.002 | 18/48 (HS-578T, SW1417, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.803×** | -4.0 | 0.003 | 17/47 (HCT15, KATO III, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.820×** | -3.8 | 0.008 | 17/42 (HCT15, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6603. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 50.1 | 2 | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 18.9 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.33× (z +12.2) | — |
| [[HS-578T (line)]] | alt | 47.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0757× (z -23.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 24.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.44× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -10.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -12.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 25.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +8.5) | — |
| [[LoVo (line)]] | wt | 31.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.57× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 25.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -10.1) ⚠ cell-cycle shift, explains ~12% of this change |
| [[PANC-1 (line)]] | alt | 24.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 40.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.432× (z -9.0) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SW 900 (line)]] | alt | 33.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6603), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG4B]] | +0.64 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[YTHDF1]] | +0.63 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[PKD1]] | +0.60 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[ENO2]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[EIF1AD]] | +0.58 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[PIP5K1C]] | +0.58 | +0.45 / +0.39 | both halves | 5e-05 |  |
| [[PLPPR2]] | +0.58 | +0.71 / +0.25 | both halves | 4e-04 |  |
| [[POFUT2]] | +0.58 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[MAP3K9]] | +0.58 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[BRPF1]] | +0.57 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[CDC34]] | +0.57 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[PHRF1]] | +0.56 | +0.42 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC12A2-DT]] | -0.52 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[VBP1]] | -0.50 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[ACADM]] | -0.50 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[OGFRL1]] | -0.49 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[OXCT1]] | -0.49 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[MCCC2]] | -0.49 | -0.45 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SCYL1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.512). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-7.6, -55.0); signed map (-28.1, 3.4). **Vector** length 87.5, 18.4% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.8 | +14.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.8 | +4.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +2.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +5.1 | +2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +1.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +3.4 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.0 | -5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -4.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | +0.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | SCY1 like pseudokinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,525,077-65,538,704 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HT019, P105, GKLP, NKTL, TAPK, TRAP, TEIF, MGC78454; previously NTKL |
| Gene groups (HGNC) | SCY1 like pseudokinases; Armadillo like helical domain containing; Pseudokinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96KG9](https://www.uniprot.org/uniprotkb/Q96KG9) (N-terminal kinase-like protein):

> Regulates COPI-mediated retrograde protein traffic at the interface between the Golgi apparatus and the endoplasmic reticulum. Involved in the maintenance of the Golgi apparatus morphology.; [Isoform 6]: Acts as a transcriptional activator. It binds to three different types of GC-rich DNA binding sites (box-A, -B and -C) in the beta-polymerase promoter region. It also binds to the TERT promoter region.

**Summary**, from NCBI Gene [57410](https://www.ncbi.nlm.nih.gov/gene/57410):

> This gene encodes a transcriptional regulator belonging to the SCY1-like family of kinase-like proteins. The protein has a divergent N-terminal kinase domain that is thought to be catalytically inactive, and can bind specific DNA sequences through its C-terminal domain. It activates transcription of the telomerase reverse transcriptase and DNA polymerase beta genes. The protein has been localized to the nucleus, and also to the cytoplasm and centrosomes during mitosis. Multiple transcript …

**Accessions** — [HGNC:14372](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14372) · Entrez [57410](https://www.ncbi.nlm.nih.gov/gene/57410) · UniProt [Q96KG9](https://www.uniprot.org/uniprotkb/Q96KG9) · Ensembl [ENSG00000142186](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142186)

## Data

Gene col 6603: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6603); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6603, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6603]; `tensor/DDL_lfc|DDL_z.npy` [6603]; `embed/gene_vectors.npy` [6603]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6603 or target_col == 6603). Every well: [[SCYL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCYL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
