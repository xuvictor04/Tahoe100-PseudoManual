---
symbol: "ITFG2-AS1"
type: "gene"
col: 14979
ensembl_id: "ENSG00000256150"
name: "ITFG2 antisense RNA 1"
location: "12p13.33"
module: 23
arm: "+"
pooled_cpm: 5.46
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 15
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 11
direction_downstream: 1
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ITFG2-AS1

*ITFG2 antisense RNA 1* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.40× (z +17.2, q 0e+00, up in 36 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.401× (z -9.1, q 6e-17, down in 26 of 45 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OXA1L-DT]] (+0.85, fdr 1e-05), [[PSMD7-DT]] (+0.81, fdr 7e-06), [[INTS6-AS1]] (+0.81, fdr 7e-06).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[LINC02940]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Belzutifan (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14979.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.40×** | +17.2 | 0e+00 | 36/37 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.16×** | +7.7 | 6e-12 | 27/44 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **2.01×** | +7.0 | 6e-10 | 27/46 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.93×** | +6.5 | 9e-09 | 26/46 (KATO III, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +5.7 | 2e-06 | 13/38 (LoVo, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.75×** | +5.6 | 2e-06 | 16/43 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +5.0 | 4e-05 | 17/47 (KATO III, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +4.5 | 5e-04 | 14/36 (BT-474, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.38×** | +4.4 | 7e-04 | 12/45 (SW480, LoVo, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.54×** | +4.3 | 1e-03 | 9/47 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.002 | 13/47 (BT-474, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +4.1 | 0.002 | 0/7 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.002 | 16/38 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.017 | 8/43 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.024 | 8/45 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.43×** | +3.3 | 0.032 | 6/47 (SW480, LoVo, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14979.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.401×** | -9.1 | 6e-17 | 26/45 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.405×** | -9.0 | 7e-17 | 25/37 (SW480, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.430×** | -8.4 | 9e-15 | 28/47 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.468×** | -7.6 | 6e-12 | 28/44 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.512×** | -6.6 | 3e-09 | 23/46 (HCT15, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.534×** | -6.2 | 4e-08 | 23/44 (SW480, HCT15, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.537×** | -6.2 | 5e-08 | 25/45 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.580×** | -5.1 | 2e-05 | 18/41 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.368×** | -5.0 | 4e-05 | 15/41 (NCI-H23, HT-29, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.638×** | -4.5 | 4e-04 | 21/38 (HCT15, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.645×** | -4.4 | 7e-04 | 14/46 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.652×** | -4.2 | 0.001 | 17/46 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **0.649×** | -4.1 | 0.002 | 15/31 (HCT15, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.712×** | -3.4 | 0.031 | 11/45 (SW480, HCT15, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.545×** | -3.0 | 0.094 | 4/40 (NCI-H23, LoVo, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14979. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 15.4 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.144× (z -12.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.233× (z -9.5) |
| [[LoVo (line)]] | wt | 10.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 18.6 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0607× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~45% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.117× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 14.4 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.160× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[PANC-1 (line)]] | alt | 3.15 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +9.4) | [[Pyridoxine (drug)]] 0.5 µM 0.0714× (z -11.9) |
| [[KATO III (line)]] | alt | 10.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 2.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.0× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 7.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 6.06 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.104× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.143× (z -8.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW1417 (line)]] | alt | 2.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.02× (z +8.7) | — |
| [[A-172 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14979), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OXA1L-DT]] | +0.85 | +0.85 / +0.56 | both halves | 1e-05 |  |
| [[PSMD7-DT]] | +0.81 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.81 | +0.77 / +0.65 | both halves | 7e-06 | same gene group |
| [[MGAM]] | +0.81 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.80 | +0.80 / +0.46 | both halves | 2e-05 | same gene group |
| [[DNAH12]] | +0.79 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[MALINC1]] | +0.77 | +0.76 / +0.50 | both halves | 1e-05 |  |
| [[NSMCE1-DT]] | +0.77 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[ANKHD1-DT]] | +0.77 | +0.77 / +0.58 | both halves | 7e-06 |  |
| [[CHD1-DT]] | +0.76 | +0.78 / +0.48 | both halves | 2e-05 |  |
| [[UFL1-AS1]] | +0.76 | +0.74 / +0.61 | both halves | 7e-06 | same gene group |
| [[NEB]] | +0.76 | +0.73 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02940]] | B | LINC02940 activity raises ITFG2-AS1's level | lines that do not express LINC02940 (10) vs lines expressing it (40) | 1.84× lower at baseline in the lines without LINC02940 | 0.029 | ⚠ within organs, on part of the lines; also absent: LINC02641; maybe low, not absent |
| [[LINC02641]] | B | LINC02641 activity raises ITFG2-AS1's level | lines that do not express LINC02641 (14) vs lines expressing it (36) | 1.58× lower at baseline in the lines without LINC02641 | 0.037 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent |
| [[CXCL13]] | B | CXCL13 activity raises ITFG2-AS1's level | lines that do not express CXCL13 (8) vs lines expressing it (42) | 1.73× lower at baseline in the lines without CXCL13 | 0.039 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[CES3]] | B | CES3 activity raises ITFG2-AS1's level | lines that do not express CES3 (10) vs lines expressing it (40) | 1.69× lower at baseline in the lines without CES3 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000288075; maybe low, not absent |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises ITFG2-AS1's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.73× lower at baseline in the lines without FSIP2-AS1 | 0.062 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[LINC01748]] | B | LINC01748 activity raises ITFG2-AS1's level | lines that do not express LINC01748 (34) vs lines expressing it (16) | 1.60× lower at baseline in the lines without LINC01748 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CALB1, ATP10B, CLRN3 |
| [[MAP2K1]] | B | MAP2K1 activity lowers ITFG2-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[LINC01762]] | B | LINC01762 activity raises ITFG2-AS1's level | lines that do not express LINC01762 (5) vs lines expressing it (45) | 2.00× lower at baseline in the lines without LINC01762 | 0.076 | ⚠ within organs, on part of the lines; also absent: MPP4, LINC01429, DNAH6; maybe low, not absent |
| [[FAM66C]] | B | FAM66C activity raises ITFG2-AS1's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.28× lower at baseline in the lines without FAM66C | 0.079 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[WARS2-AS1]] | C | WARS2-AS1 activity raises ITFG2-AS1's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 2.20× lower at baseline in the lines without WARS2-AS1 | 0.068 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent |
| [[RFX3-DT]] | C | RFX3-DT activity raises ITFG2-AS1's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 2.15× lower at baseline in the lines without RFX3-DT | 0.072 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Belzutifan (drug)]] 5 µM | C | ITFG2-AS1's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | ITFG2-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.60 | 0.470 over the table, 0.076 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.811). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (8.5, 18.5); signed map (29.3, -6.4). **Vector** length 74.8, 13.3% of its response variance represented; |z| ≥ 3 in 1,133 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +17.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.3 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +2.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +5.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.0 | -4.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.9 | -6.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -3.7 | -3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.2 | -9.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -6.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -2.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.7 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ITFG2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12p13.33 — chr12:2,695,765-2,812,902 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously CACNA1C-AS1, CACNA1C-AS2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | symbol |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53128](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53128) · Entrez [283440](https://www.ncbi.nlm.nih.gov/gene/283440) · Ensembl [ENSG00000256150](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000256150)

## Data

Gene col 14979: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14979); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14979, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14979]; `tensor/DDL_lfc|DDL_z.npy` [14979]; `embed/gene_vectors.npy` [14979]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14979 or target_col == 14979). Every well: [[ITFG2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITFG2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
