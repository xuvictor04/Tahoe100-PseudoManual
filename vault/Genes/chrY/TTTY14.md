---
symbol: "TTTY14"
type: "gene"
col: 10746
ensembl_id: "ENSG00000176728"
name: "testis expressed transcript, Y-linked 14"
location: "Yq11.222"
module: 133
arm: "+"
pooled_cpm: 9.77
n_lines_expressing: 24
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 8
direction_downstream: 12
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# TTTY14

*testis expressed transcript, Y-linked 14* — Yq11.222

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.67× (z +11.2, q 2e-26, up in 3 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.40× (z +10.0, q 3e-21, up in 17 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.580× (z -6.2, q 3e-07, down in 15 of 21 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.621× (z -5.2, q 5e-05, down in 11 of 21 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COP1-DT]] (+0.68, fdr 7e-06), [[PAPPA2]] (+0.65, fdr 7e-06), [[ANKFN1]] (+0.53, fdr 2e-04); moves opposite to [[FAM3C]] (-0.40, fdr 2e-04).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[UTY]] → it (grade C ⚠); 12 go from it, the strongest it → [[AUTS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10746.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +11.2 | 2e-26 | 3/15 (HT-29, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.40×** | +10.0 | 3e-21 | 17/21 (SNU-423, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +9.0 | 4e-17 | 1/10 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +4.5 | 0.001 | 1/16 (C32) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.49×** | +4.4 | 0.001 | 0/20 | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +3.9 | 0.008 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.032 | 1/19 (LoVo) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.040 | 7/21 (SNU-423, A-172, …) | rises with dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.52×** | +3.4 | 0.042 | 0/21 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.064 | 3/21 (SNU-423, NCI-H460, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.090 | 5/21 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.090 | 2/19 (BT-474, H4) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.31×** | +3.1 | 0.090 | 8/21 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.091 | 6/21 (NCI-H460, A-427, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | 1.30× | +3.0 | 0.10 | 4/18 (hTERT-HPNE, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10746.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.580×** | -6.2 | 3e-07 | 15/21 (SNU-1, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.621×** | -5.2 | 5e-05 | 11/21 (A-427, SNU-423, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.592×** | -5.0 | 1e-04 | 11/21 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.648×** | -4.9 | 1e-04 | 14/21 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.462×** | -4.6 | 5e-04 | 11/21 (A-427, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.652×** | -4.1 | 0.004 | 12/21 (SNU-1, SNU-423, …) | rises with dose |  |
| [[Asciminib (drug)]] 0.05 µM |  | **0.729×** | -3.6 | 0.026 | 4/21 (A549, H4, …) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.720×** | -3.5 | 0.037 | 1/21 (J82) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.740×** | -3.4 | 0.037 | 12/21 (LoVo, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.753×** | -3.2 | 0.068 | 11/21 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.763× | -3.1 | 0.10 | 7/21 (H4, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10746. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 248 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -14.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 14.0 | 1 | 6 (5 ⚠) | [[Auranofin (drug)]] 5 µM 4.14× (z +8.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.120× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 40.3 | 1 | 6 (4 ⚠) | [[Auranofin (drug)]] 5 µM 3.75× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -11.1) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -10.6) |
| [[H4 (line)]] | wt | 20.7 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0313× (z -14.9) |
| [[SNU-423 (line)]] | alt | 24.8 | 1 | 5 (3 ⚠) | [[Auranofin (drug)]] 5 µM 5.26× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -16.8) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0599× (z -9.9) |
| [[A-427 (line)]] | wt | 41.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0933× (z -17.3) |
| [[CHP-212 (line)]] | wt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -10.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 20.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0507× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.105× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 67.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -14.5) ⚠ cell-cycle shift, explains ~66% of this change |
| [[A-172 (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -10.2) ⚠ cell-cycle shift, explains ~66% of this change |
| [[C32 (line)]] | wt | 2.79 | 1 | 0 | [[Auranofin (drug)]] 5 µM 51.3× (z +10.3) | — |
| [[A498 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.994 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.810 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.853 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.992 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.928 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.20 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10746), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COP1-DT]] | +0.68 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[PAPPA2]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[ANKFN1]] | +0.53 | +0.30 / +0.59 | both halves | 2e-04 |  |
| [[MIR99AHG]] | +0.51 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[TTTY10]] | +0.51 | +0.60 / +0.42 | both halves | 4e-05 | same gene group |
| [[PGLS-DT]] | +0.51 | +0.32 / +0.57 | both halves | 2e-04 |  |
| [[PDE8B]] | +0.51 | +0.55 / +0.30 | both halves | 2e-04 |  |
| [[ASNSP1]] | +0.50 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[VLDLR-AS1]] | +0.50 | +0.28 / +0.52 | both halves | 3e-04 |  |
| [[AUTS2]] | +0.50 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[NMRAL2P]] | +0.49 | +0.37 / +0.45 | both halves | 8e-05 |  |
| [[EIF2S2]] | +0.49 | +0.36 / +0.56 | both halves | 9e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM3C]] | -0.40 | -0.30 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UTY]] | C | UTY activity raises TTTY14's level | lines that do not express UTY (31) vs lines expressing it (19) | 6.76× lower at baseline in the lines without UTY | 6e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[USP9Y]] | C | USP9Y activity raises TTTY14's level | lines that do not express USP9Y (30) vs lines expressing it (20) | 6.18× lower at baseline in the lines without USP9Y | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1; co-absent with the target |
| [[TTTY10]] | C | TTTY10 activity raises TTTY14's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 5.88× lower at baseline in the lines without TTTY10 | 4e-04 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |
| [[MIR99AHG]] | C | MIR99AHG activity raises TTTY14's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 4.47× lower at baseline in the lines without MIR99AHG | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[NLGN4Y]] | C | NLGN4Y activity raises TTTY14's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 5.76× lower at baseline in the lines without NLGN4Y | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[LINC00470]] | C | LINC00470 activity raises TTTY14's level | lines that do not express LINC00470 (38) vs lines expressing it (12) | 1.73× lower at baseline in the lines without LINC00470 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, ENSG00000287474, FCRLA; co-absent with the target |
| [[CDH7]] | C | CDH7 activity raises TTTY14's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 2.12× lower at baseline in the lines without CDH7 | 0.084 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9; co-absent with the target |
| [[WNK3]] | C | WNK3 activity raises TTTY14's level | lines that do not express WNK3 (28) vs lines expressing it (22) | 1.96× lower at baseline in the lines without WNK3 | 0.085 | ⚠ within organs, on part of the lines; also absent: PCDH17, ZNF667, PTPRN; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 5, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AUTS2]] | B | TTTY14 activity raises AUTS2's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 3.26× lower at baseline in the lines without TTTY14 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY |
| [[KCNK2]] | B | TTTY14 activity raises KCNK2's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 1.74× lower at baseline in the lines without TTTY14 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY |
| [[GABBR2]] | B | TTTY14 activity raises GABBR2's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 1.51× lower at baseline in the lines without TTTY14 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY |
| [[NBR2]] | B | TTTY14 activity raises NBR2's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 1.44× lower at baseline in the lines without TTTY14 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY |
| [[FAM3C]] | B | TTTY14 activity lowers FAM3C's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 1.89× higher at baseline in the lines without TTTY14 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY |
| [[UTY]] | C | TTTY14 activity raises UTY's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 14.49× lower at baseline in the lines without TTTY14 | 5e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY; co-absent with the target |
| [[TTTY10]] | C | TTTY14 activity raises TTTY10's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 4.41× lower at baseline in the lines without TTTY14 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY; co-absent with the target |
| [[USP9Y]] | C | TTTY14 activity raises USP9Y's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 11.86× lower at baseline in the lines without TTTY14 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY; co-absent with the target |
| [[NLGN4Y]] | C | TTTY14 activity raises NLGN4Y's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 5.21× lower at baseline in the lines without TTTY14 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY; co-absent with the target |
| [[GREM2]] | C | TTTY14 activity raises GREM2's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 2.24× lower at baseline in the lines without TTTY14 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY; co-absent with the target |
| [[MIR99AHG]] | C | TTTY14 activity raises MIR99AHG's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 2.40× lower at baseline in the lines without TTTY14 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY; co-absent with the target |
| [[CDH7]] | C | TTTY14 activity raises CDH7's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 2.32× lower at baseline in the lines without TTTY14 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY; co-absent with the target |

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.588). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.7, 36.6); signed map (41.2, 41.5). **Vector** length 49.2, 10.3% of its response variance represented; |z| ≥ 3 in 542 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.3 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +9.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.4 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +0.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +0.5 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -5.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -3.5 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | -2.7 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | testis expressed transcript, Y-linked 14 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Yq11.222 — chrY:18,772,706-19,077,416 (-) |
| Ensembl biotype | lncRNA |
| Also known as | TTY14, NCRNA00137, PRO2834; previously NCRNA00185, CYorf14 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [83869](https://www.ncbi.nlm.nih.gov/gene/83869):

> Predicted to enable pre-mRNA 5'-splice site binding activity. Predicted to be involved in mRNA 5'-splice site recognition. Predicted to be part of U1 snRNP. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18495](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18495) · Entrez [83869](https://www.ncbi.nlm.nih.gov/gene/83869) · Ensembl [ENSG00000176728](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176728)

## Data

Gene col 10746: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10746); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10746, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10746]; `tensor/DDL_lfc|DDL_z.npy` [10746]; `embed/gene_vectors.npy` [10746]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10746 or target_col == 10746). Every well: [[TTTY14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTTY14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
