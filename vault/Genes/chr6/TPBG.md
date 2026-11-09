---
symbol: "TPBG"
type: "gene"
col: 7076
ensembl_id: "ENSG00000146242"
name: "trophoblast glycoprotein"
location: "6q14.1"
module: 81
arm: "+"
pooled_cpm: 26.15
n_lines_expressing: 40
n_dd_up: 4
n_dd_down: 26
n_dd_up_clean: 2
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 12
direction_downstream: 9
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# TPBG

*trophoblast glycoprotein* — 6q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +5.7, q 9e-06, up in 15 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 3.54×, HEC-1-A 5.06×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 2.91×, HEC-1-A 2.88×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HEC-1-A 2.87×).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.428× (z -12.8, q 1e-34, down in 31 of 38 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM158]] (+0.59, fdr 7e-06), [[ERN1]] (+0.59, fdr 1e-05), [[CCNYL1]] (+0.57, fdr 1e-05); moves opposite to [[CCDC6]] (-0.55, fdr 4e-05), [[MRRF]] (-0.52, fdr 1e-05), [[MRPL42]] (-0.51, fdr 2e-04).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[PTGS2]] → it (grade B ⚠); 9 go from it, the strongest it → [[SNAI1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7076.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 3.54×, HEC-1-A 5.06×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 2.91×, HEC-1-A 2.88×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HEC-1-A 2.87×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.7 | 9e-06 | 15/37 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Artesunate (drug)]] 5 µM |  | **1.23×** | +4.4 | 0.003 | 20/38 (COLO 205, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.9 | 0.021 | 16/36 (HT-29, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **1.27×** | +3.6 | 0.046 | 16/38 (SNU-1, BT-474, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | 1.24× | +3.3 | 0.11 | 10/38 (RPMI-7951, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | 1.24× | +3.2 | 0.11 | 12/38 (NCI-H2030, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 5 µM |  | 1.16× | +3.2 | 0.11 | 11/38 (Panc 03.27, HOP62, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7076.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.428×** | -12.8 | 1e-34 | 31/38 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.436×** | -12.5 | 2e-33 | 30/38 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.589×** | -11.3 | 3e-27 | 22/37 (H4, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.483×** | -11.0 | 9e-26 | 31/38 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.475×** | -5.9 | 5e-07 | 20/38 (LOX-IMVI, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.690×** | -5.4 | 7e-06 | 21/38 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.703×** | -5.3 | 9e-06 | 20/38 (H4, HS-578T, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.711×** | -4.9 | 5e-05 | 22/38 (H4, HOP62, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.542×** | -4.8 | 9e-05 | 18/38 (RPMI-7951, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.733×** | -4.7 | 2e-04 | 21/36 (H4, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.734×** | -4.5 | 4e-04 | 19/27 (H4, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.746×** | -4.4 | 5e-04 | 17/38 (HOP62, NCI-H1573, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **0.724×** | -4.2 | 0.001 | 18/38 (NCI-H23, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **0.766×** | -4.0 | 0.002 | 16/38 (H4, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.774×** | -3.9 | 0.004 | 17/38 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.624×** | -3.7 | 0.007 | 14/36 (RKO, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.784×** | -3.7 | 0.007 | 17/38 (H4, HS-578T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7076. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 74.4 | 0 | 17 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -20.3) |
| [[HS-578T (line)]] | alt | 91.8 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 35.4 | 0 | 7 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.331× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.249× (z -11.1) |
| [[HOP62 (line)]] | alt | 76.5 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 68.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.123× (z -18.1) |
| [[NCI-H23 (line)]] | alt | 32.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -15.1) |
| [[SW 900 (line)]] | alt | 55.1 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.262× (z -9.9) |
| [[A549 (line)]] | wt | 31.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.218× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 13.2 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.06× (z +9.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 34.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -15.6) |
| [[J82 (line)]] | alt | 38.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -12.2) |
| [[SNU-423 (line)]] | alt | 63.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.279× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 56.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -18.3) |
| [[A-172 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 27.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.320× (z -9.2) |
| [[AN3 CA (line)]] | alt | 18.7 | 0 | 1 | — | [[Methyl aminolevulinate (hydrochloride) (drug)]] 0.05 µM 0.0682× (z -8.7) |
| [[COLO 205 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0948× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -8.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 26.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 48.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -12.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 26.1 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.54× (z +11.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 1271 (line)]] | alt | 71.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0757× (z -9.3) |
| [[SW480 (line)]] | alt | 9.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +10.1) | — |
| [[A-427 (line)]] | wt | 5.06 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.44 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.01 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.81 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7076), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM158]] | +0.59 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ERN1]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[CCNYL1]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[HBEGF]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[FAM107B]] | +0.55 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[EHD1]] | +0.54 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[LRRC49]] | +0.54 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[SMOX]] | +0.54 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[PTHLH]] | +0.53 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[C15orf48]] | +0.53 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[RGS16]] | +0.52 | +0.30 / +0.47 | both halves | 2e-04 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[LUCAT1]] | +0.52 | +0.45 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC6]] | -0.55 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[MRRF]] | -0.52 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[MRPL42]] | -0.51 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[NELFCD]] | -0.50 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[HEATR1]] | -0.49 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[LAS1L]] | -0.48 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[API5]] | -0.48 | -0.23 / -0.56 | both halves | 5e-04 |  |
| [[MAP2]] | -0.48 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[VPS50]] | -0.48 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[COPS8]] | -0.48 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[CNBP]] | -0.48 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[TCERG1]] | -0.47 | -0.42 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTGS2]] | B | PTGS2 activity raises TPBG's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.73× lower at baseline in the lines without PTGS2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[ANTXR2]] | B | ANTXR2 activity raises TPBG's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 3.19× lower at baseline in the lines without ANTXR2 | 0.018 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[KCNMA1]] | B | KCNMA1 activity raises TPBG's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 2.86× lower at baseline in the lines without KCNMA1 | 0.024 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[TMEM158]] | B | TMEM158 activity raises TPBG's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 2.38× lower at baseline in the lines without TMEM158 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[VEGFC]] | B | VEGFC activity raises TPBG's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 2.95× lower at baseline in the lines without VEGFC | 0.042 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1 |
| [[STC1]] | B | STC1 activity raises TPBG's level | lines that do not express STC1 (24) vs lines expressing it (26) | 2.72× lower at baseline in the lines without STC1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[LRRC8C]] | B | LRRC8C activity raises TPBG's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 2.59× lower at baseline in the lines without LRRC8C | 0.054 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[PTHLH]] | B | PTHLH activity raises TPBG's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 2.49× lower at baseline in the lines without PTHLH | 0.056 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |
| [[C15orf48]] | B | C15orf48 activity raises TPBG's level | lines that do not express C15orf48 (25) vs lines expressing it (25) | 2.48× lower at baseline in the lines without C15orf48 | 0.061 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG |
| [[GABRE]] | B | GABRE activity raises TPBG's level | lines that do not express GABRE (20) vs lines expressing it (30) | 2.05× lower at baseline in the lines without GABRE | 0.096 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |
| [[HMGN2P46]] | B | HMGN2P46 activity raises TPBG's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 2.43× lower at baseline in the lines without HMGN2P46 | 0.099 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |
| [[SYNJ2]] | C | SYNJ2 activity raises TPBG's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 3.40× lower at baseline in the lines without SYNJ2 | 0.059 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNAI1]] | B | TPBG activity lowers SNAI1's level | lines that do not express TPBG (10) vs lines expressing it (40) | 1.51× higher at baseline in the lines without TPBG | 0.028 | ⚠ within organs, on part of the lines |
| [[STC1]] | B | TPBG activity raises STC1's level | lines that do not express TPBG (10) vs lines expressing it (40) | 3.85× lower at baseline in the lines without TPBG | 0.030 | ⚠ within organs, on part of the lines |
| [[FAM110A]] | B | TPBG activity raises FAM110A's level | lines that do not express TPBG (10) vs lines expressing it (40) | 1.69× lower at baseline in the lines without TPBG | 0.037 | ⚠ within organs, on part of the lines |
| [[ANTXR2]] | B | TPBG activity raises ANTXR2's level | lines that do not express TPBG (10) vs lines expressing it (40) | 2.60× lower at baseline in the lines without TPBG | 0.058 | ⚠ within organs, on part of the lines |
| [[ULBP2]] | B | TPBG activity raises ULBP2's level | lines that do not express TPBG (10) vs lines expressing it (40) | 2.37× lower at baseline in the lines without TPBG | 0.060 | ⚠ within organs, on part of the lines |
| [[RPE]] | B | TPBG activity strengthens RPE's drug response | lines that do not express TPBG (10) vs lines expressing it (38) | the lines without TPBG respond 0.60× as strongly (z diff +0.72); strongest at Belinostat 5 µM: 1.28x vs 1.65x (z diff +1.8) | 0.068 | ⚠ within organs, on part of the lines; target measured in part of the lines; artifact flags |
| [[LUCAT1]] | B | TPBG activity raises LUCAT1's level | lines that do not express TPBG (10) vs lines expressing it (40) | 2.09× lower at baseline in the lines without TPBG | 0.078 | ⚠ within organs, on part of the lines |
| [[ISG20]] | B | TPBG activity raises ISG20's level | lines that do not express TPBG (10) vs lines expressing it (40) | 1.69× lower at baseline in the lines without TPBG | 0.083 | ⚠ within organs, on part of the lines |
| [[KCNMA1]] | B | TPBG activity raises KCNMA1's level | lines that do not express TPBG (10) vs lines expressing it (40) | 2.92× lower at baseline in the lines without TPBG | 0.091 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.1, -6.7); signed map (-1.6, 30.1). **Vector** length 102, 25.0% of its response variance represented; |z| ≥ 3 in 1,032 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +0.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +0.6 |
|  | [[Artesunate (drug)]] 5 µM |  | +2.8 | +4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.9 | +3.2 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.1 | -4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.7 | -2.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.6 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -3.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.5 | -2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.3 | -5.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.2 | -2.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -3.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | trophoblast glycoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:82,363,206-82,367,420 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 5T4-AG, 5T4 |
| Hallmark sets | INFLAMMATORY_RESPONSE, ESTROGEN_RESPONSE_LATE, GLYCOLYSIS, HYPOXIA, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13641](https://www.uniprot.org/uniprotkb/Q13641) (Trophoblast glycoprotein):

> May function as an inhibitor of Wnt/beta-catenin signaling by indirectly interacting with LRP6 and blocking Wnt3a-dependent LRP6 internalization.

**Summary**, from NCBI Gene [7162](https://www.ncbi.nlm.nih.gov/gene/7162):

> This gene encodes a leucine-rich transmembrane glycoprotein that may be involved in cell adhesion. The encoded protein is an oncofetal antigen that is specific to trophoblast cells. In adults this protein is highly expressed in many tumor cells and is associated with poor clinical outcome in numerous cancers. Alternate splicing in the 5' UTR results in multiple transcript variants that encode the same protein. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:12004](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12004) · Entrez [7162](https://www.ncbi.nlm.nih.gov/gene/7162) · UniProt [Q13641](https://www.uniprot.org/uniprotkb/Q13641) · Ensembl [ENSG00000146242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146242)

## Data

Gene col 7076: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7076); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7076, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7076]; `tensor/DDL_lfc|DDL_z.npy` [7076]; `embed/gene_vectors.npy` [7076]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7076 or target_col == 7076). Every well: [[TPBG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPBG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
