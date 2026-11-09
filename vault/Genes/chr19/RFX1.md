---
symbol: "RFX1"
type: "gene"
col: 5268
ensembl_id: "ENSG00000132005"
name: "regulatory factor X1"
location: "19p13.12"
module: 95
arm: "+"
pooled_cpm: 23.05
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# RFX1

*regulatory factor X1* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 3.08× (z +16.5, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.409× (z -13.1, q 1e-36, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF335]] (+0.77, fdr 7e-06), [[RBM5]] (+0.71, fdr 7e-06), [[DRC3]] (+0.70, fdr 7e-06); moves opposite to [[WASF3]] (-0.65, fdr 1e-05), [[PAFAH1B2]] (-0.61, fdr 1e-05), [[FAR1]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HLA-B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5268.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.08×** | +16.5 | 0e+00 | 46/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +14.8 | 0e+00 | 45/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.97×** | +14.1 | 1e-42 | 40/47 (BT-474, NCI-H1573, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.26×** | +11.9 | 9e-31 | 45/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.91×** | +9.5 | 3e-19 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +8.4 | 3e-15 | 32/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.55×** | +6.4 | 9e-09 | 23/47 (NCI-H460, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.50×** | +5.9 | 3e-07 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +5.1 | 3e-05 | 22/43 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sodium Salicylate (drug)]] 5 µM |  | 1.17× | +3.2 | 0.090 | 6/48 (HT-29, NCI-H1573, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5268.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.409×** | -13.1 | 1e-36 | 42/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.414×** | -13.0 | 7e-36 | 44/48 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.487×** | -10.5 | 1e-23 | 38/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.521×** | -9.6 | 1e-19 | 43/48 (SK-MEL-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.638×** | -9.3 | 1e-18 | 42/48 (NCI-H460, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.421×** | -6.6 | 3e-09 | 37/48 (SK-MEL-2, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.681×** | -5.6 | 1e-06 | 31/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.690×** | -5.5 | 3e-06 | 27/48 (NCI-H460, HS-578T, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.705×** | -5.1 | 2e-05 | 29/47 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.866× | -3.0 | 0.15 | 19/48 (HOP62, A498, …) | top dose only | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5268. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 23.7 | 5 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.88× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.182× (z -13.6) |
| [[NCI-H460 (line)]] | wt | 19.0 | 5 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.70× (z +12.7) | [[Belinostat (drug)]] 5 µM 0.356× (z -8.5) |
| [[PANC-1 (line)]] | alt | 19.7 | 5 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.55× (z +13.1) | [[Belinostat (drug)]] 5 µM 0.371× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 31.2 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.238× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.296× (z -9.4) |
| [[A498 (line)]] | wt | 26.8 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.4) ⚠ cell-cycle shift, explains ~28% of this change | [[Belinostat (drug)]] 5 µM 0.269× (z -11.6) |
| [[HOP62 (line)]] | alt | 22.3 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +9.3) | [[Selinexor (drug)]] 5 µM 0.394× (z -9.8) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.269× (z -9.8) |
| [[BT-474 (line)]] | alt | 104 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +15.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.37× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 21.2 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +9.1) ⚠ cell-cycle shift, explains ~28% of this change | [[Panobinostat (drug)]] 5 µM 0.257× (z -9.0) |
| [[SW480 (line)]] | alt | 21.6 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.32× (z +13.6) | — |
| [[COLO 205 (line)]] | alt | 18.3 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.51× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.82× (z +9.0) | — |
| [[LoVo (line)]] | wt | 14.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.37× (z +14.0) | — |
| [[NCI-H1792 (line)]] | alt | 20.4 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.27× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -9.8) |
| [[RKO (line)]] | wt | 14.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +10.7) ⚠ cell-cycle shift, explains ~28% of this change | [[Nimesulide (drug)]] 5 µM 0.135× (z -10.3) ⚠ toxic; unreliable plate only |
| [[SNU-1 (line)]] | wt | 20.8 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.89× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 24.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.244× (z -8.6) |
| [[A-172 (line)]] | wt | 20.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[A-427 (line)]] | wt | 21.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +8.5) | — |
| [[A549 (line)]] | wt | 20.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +8.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[AsPC-1 (line)]] | alt | 19.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.60× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 19.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[LS 180 (line)]] | wt | 14.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.58× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 29.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +9.2) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2347 (line)]] | alt | 27.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.317× (z -10.1) |
| [[SNU-423 (line)]] | alt | 22.0 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.207× (z -9.4) |
| [[SW1417 (line)]] | alt | 23.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.65× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5268), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF335]] | +0.77 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[RBM5]] | +0.71 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[DRC3]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[DYRK1B]] | +0.69 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[CREBBP]] | +0.67 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[FAM193A]] | +0.65 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SIRT1]] | +0.65 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[GTF2IRD2B]] | +0.64 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[CHKB]] | +0.64 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[UNK]] | +0.64 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[EP300]] | +0.63 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[FBRS]] | +0.62 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASF3]] | -0.65 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[PAFAH1B2]] | -0.61 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[FAR1]] | -0.61 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[CORO1C]] | -0.59 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[CCT8]] | -0.58 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[METAP1]] | -0.58 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ADH5]] | -0.57 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[NEIL2]] | -0.57 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[PLEKHB2]] | -0.56 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[OTULIN]] | -0.55 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[EEF1E1]] | -0.55 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[SDHAF3]] | -0.55 | -0.52 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-B]] | B | HLA-B activity raises RFX1's level | lines that do not express HLA-B (9) vs lines expressing it (41) | 1.29× lower at baseline in the lines without HLA-B | 0.067 | ⚠ within organs, on part of the lines; also absent: HLA-F, UBE2L6 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises RFX1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises RFX1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-42.1, 19.4); signed map (-2.2, 6.5). **Vector** length 101, 25.4% of its response variance represented; |z| ≥ 3 in 1,060 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Activation of HOX genes during differentiation* (reactome, mean cos +0.60 to 4); *Activation of anterior HOX genes in hindbrain development during early embryogenesis* (reactome, mean cos +0.60 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +8.2 | +14.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.9 | +16.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +14.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.6 | +5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.0 | +11.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | -1.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.7 | +1.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.6 | +0.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.5 | +1.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.4 | +1.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.6 | -9.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.3 | -13.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -6.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | regulatory factor X1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:13,961,530-14,007,039 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EF-C |
| Gene groups (HGNC) | Regulatory factor X family |
| Matched by | ensembl_id |

**Function**, from UniProt [P22670](https://www.uniprot.org/uniprotkb/P22670) (MHC class II regulatory factor RFX1):

> Regulatory factor essential for MHC class II genes expression. Binds to the X boxes of MHC class II genes. Also binds to an inverted repeat (ENH1) required for hepatitis B virus genes expression and to the most upstream element (alpha) of the RPL30 promoter.

**Summary**, from NCBI Gene [5989](https://www.ncbi.nlm.nih.gov/gene/5989):

> This gene encodes a member of the regulatory factor X (RFX) family of transcription factors, which are characterized by a winged-helix DNA-binding domain. The encoded transcription factor contains an N-terminal activation domain and a C-terminal repression domain, and may activate or repress target gene expression depending on cellular context. This transcription factor has been shown to regulate a wide variety of genes involved in immunity and cancer, including the MHC class II genes and genes …

**Accessions** — [HGNC:9982](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9982) · Entrez [5989](https://www.ncbi.nlm.nih.gov/gene/5989) · UniProt [P22670](https://www.uniprot.org/uniprotkb/P22670) · Ensembl [ENSG00000132005](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132005)

## Data

Gene col 5268: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5268); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5268, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5268]; `tensor/DDL_lfc|DDL_z.npy` [5268]; `embed/gene_vectors.npy` [5268]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5268 or target_col == 5268). Every well: [[RFX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
