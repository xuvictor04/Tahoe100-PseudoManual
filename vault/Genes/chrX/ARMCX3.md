---
symbol: "ARMCX3"
type: "gene"
col: 2246
ensembl_id: "ENSG00000102401"
name: "armadillo repeat containing X-linked 3"
location: "Xq22.1"
module: 59
arm: "+"
pooled_cpm: 39.38
n_lines_expressing: 47
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# ARMCX3

*armadillo repeat containing X-linked 3* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.14× (z +12.1, q 8e-31, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 0.05 µM: 0.731× (z -4.8, q 1e-03, down in 23 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.203×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 0.05 µM in 1 line (NCI-H2347 0.373×); [[Panobinostat (drug)]] 5 µM in 1 line (A498 0.493×; ⚠ cell-cycle shift, explains ~65% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCEAL3]] (+0.75, fdr 7e-06), [[TCEAL9]] (+0.69, fdr 7e-06), [[GOLGA4]] (+0.61, fdr 7e-06); moves opposite to [[NUP93]] (-0.63, fdr 7e-06), [[URB2]] (-0.59, fdr 1e-05), [[CPSF3]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[CHRNA7]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2246.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.14×** | +12.1 | 8e-31 | 43/45 (HT-29, RKO, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +7.2 | 1e-10 | 7/45 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +7.2 | 1e-10 | 25/45 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +7.1 | 2e-10 | 28/43 (SK-MEL-2, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +6.9 | 7e-10 | 29/45 (A-427, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.38×** | +5.1 | 3e-05 | 23/45 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +5.0 | 6e-05 | 27/44 (HOP62, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +4.7 | 2e-04 | 23/38 (NCI-H460, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +4.5 | 4e-04 | 20/45 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **1.70×** | +4.4 | 6e-04 | 25/44 (A498, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +3.9 | 0.005 | 18/40 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.015 | 14/45 (MIA PaCa-2, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.016 | 17/45 (Hs 766T, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.24×** | +3.4 | 0.029 | 22/44 (NCI-H460, NCI-H1573, …) | rises with dose | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.047 | 12/45 (RKO, HT-29, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.055 | 14/45 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.055 | 7/45 (NCI-H1792, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.060 | 12/45 (KATO III, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +2.9 | 0.092 | 13/45 (MIA PaCa-2, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2246.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.203×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 0.05 µM in 1 line (NCI-H2347 0.373×); [[Panobinostat (drug)]] 5 µM in 1 line (A498 0.493×; ⚠ cell-cycle shift, explains ~65% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | **0.731×** | -4.8 | 1e-03 | 23/44 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.585×** | -4.5 | 0.002 | 25/44 (Hs 766T, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.824× | -3.0 | 0.39 | 10/45 (LOX-IMVI, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2246. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 44.0 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +18.5) | — |
| [[NCI-H1573 (line)]] | alt | 42.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.34× (z +10.2) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.2) | — |
| [[A-172 (line)]] | wt | 25.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +13.1) | — |
| [[HOP62 (line)]] | alt | 42.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 36.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -10.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 83.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.493× (z -9.1) ⚠ cell-cycle shift, explains ~65% of this change |
| [[HEC-1-A (line)]] | alt | 34.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.03× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 59.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.24× (z +11.3) | — |
| [[J82 (line)]] | alt | 55.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +13.8) | — |
| [[LOX-IMVI (line)]] | wt | 36.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.86× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 43.7 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.51× (z +11.8) ⚠ position not correctable | — |
| [[NCI-H2347 (line)]] | alt | 45.9 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.373× (z -10.6) |
| [[PANC-1 (line)]] | alt | 15.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.0) | — |
| [[RKO (line)]] | wt | 34.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.15× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 92.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.94× (z +10.3) | — |
| [[SW480 (line)]] | alt | 47.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.38× (z +9.0) | — |
| [[A-427 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 77.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.53 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.32 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2246), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCEAL3]] | +0.75 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[TCEAL9]] | +0.69 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[GOLGA4]] | +0.61 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[SAT2]] | +0.59 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[ATP6V1G1]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ZRANB2]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[TMEM167B]] | +0.58 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[APBA3]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ABCA5]] | +0.57 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[HLA-V-1]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[NEU1]] | +0.57 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[TMF1]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP93]] | -0.63 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[URB2]] | -0.59 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[CPSF3]] | -0.58 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[PRKDC]] | -0.58 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[TCF20]] | -0.57 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[SRPK1]] | -0.56 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[RANBP1]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[NCAPD3]] | -0.55 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[RFWD3]] | -0.54 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[POLA1]] | -0.54 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[NSD2]] | -0.54 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[CTPS1]] | -0.54 | -0.53 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHRNA7]] | C | ARMCX3 activity lowers CHRNA7's level | lines that do not express ARMCX3 (3) vs lines expressing it (47) | 7.53× higher at baseline in the lines without ARMCX3 | 0.035 | ⚠ few lines (3 vs 47); across organs; also absent: ARMCX6, TRAF3IP2, SFXN3 |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | ARMCX3 activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express ARMCX3 (3) vs lines expressing it (45) | the lines without ARMCX3: 1.36× the cells of the other lines | 0.076 | ⚠ few lines (3 vs 47); across organs; also absent: ARMCX6, TRAF3IP2, SFXN3 |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-35.0, -31.3); signed map (-10.7, -0.7). **Vector** length 111, 30.5% of its response variance represented; |z| ≥ 3 in 790 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.5 | +12.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.1 | +6.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.6 | +5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.2 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.1 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.6 | +3.1 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -5.0 | -4.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.1 | -4.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -3.7 | -2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.1 | -1.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | armadillo repeat containing X-linked 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:101,622,797-101,627,843 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ALEX3, GASP6 |
| Gene groups (HGNC) | Armadillo repeat containing |
| Reactome | 4 pathways, smallest: RAC2 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UH62](https://www.uniprot.org/uniprotkb/Q9UH62) (Armadillo repeat-containing X-linked protein 3):

> Regulates mitochondrial aggregation and transport in axons in living neurons. May link mitochondria to the TRAK2-kinesin motor complex via its interaction with Miro and TRAK2. Mitochondrial distribution and dynamics is regulated through ARMCX3 protein degradation, which is promoted by PCK and negatively regulated by WNT1. Enhances the SOX10-mediated transactivation of the neuronal acetylcholine receptor subunit alpha-3 and beta-4 subunit gene promoters.

**Summary**, from NCBI Gene [51566](https://www.ncbi.nlm.nih.gov/gene/51566):

> This gene encodes a member of the ALEX family of proteins which may play a role in tumor suppression. The encoded protein contains a potential N-terminal transmembrane domain and a single Armadillo (arm) repeat. Other proteins containing the arm repeat are involved in development, maintenance of tissue integrity, and tumorigenesis. This gene is closely localized with other family members on the X chromosome. Three transcript variants encoding the same protein have been identified for this gene. …

**Accessions** — [HGNC:24065](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24065) · Entrez [51566](https://www.ncbi.nlm.nih.gov/gene/51566) · UniProt [Q9UH62](https://www.uniprot.org/uniprotkb/Q9UH62) · Ensembl [ENSG00000102401](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102401)

## Data

Gene col 2246: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2246); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2246, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2246]; `tensor/DDL_lfc|DDL_z.npy` [2246]; `embed/gene_vectors.npy` [2246]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2246 or target_col == 2246). Every well: [[ARMCX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARMCX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
