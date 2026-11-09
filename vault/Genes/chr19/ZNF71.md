---
symbol: "ZNF71"
type: "gene"
col: 12495
ensembl_id: "ENSG00000197951"
name: "zinc finger protein 71"
location: "19q13.4"
module: 129
arm: "+"
pooled_cpm: 5.63
n_lines_expressing: 35
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 15
direction_downstream: 24
tags: ["gene", "module/129"]
generated_by: "tahoemap"
---

# ZNF71

*zinc finger protein 71* — 19q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.50× (z +6.5, q 5e-08, up in 15 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.499× (z -13.2, q 3e-37, down in 20 of 31 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.408× (z -11.6, q 1e-28, down in 20 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZIM2-AS1]] (+0.71, fdr 7e-06, ⚠ same locus), [[ZFP28]] (+0.70, fdr 7e-06, ⚠ same locus), [[LRFN3]] (+0.69, fdr 7e-06), [[RNF216P1]] (+0.68, fdr 1e-05), [[ZNF559]] (+0.68, fdr 7e-06); moves opposite to [[BAZ2B]] (-0.59, fdr 3e-05), [[HIVEP2-DT]] (-0.58, fdr 1e-05), [[SGO1-AS1]] (-0.55, fdr 4e-05).
> It is in [[Module 129]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[THRB]] → it (grade B ⚠); 24 go from it, the strongest it → [[ZNF891]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12495.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.50×** | +6.5 | 5e-08 | 15/31 (PANC-1, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +5.4 | 2e-05 | 13/32 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.27×** | +4.6 | 8e-04 | 9/33 (MIA PaCa-2, NCI-H460, …) | top dose only | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.88×** | +4.5 | 0.001 | 8/28 (A-427, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.4 | 0.001 | 7/33 (SW1417, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.32×** | +3.6 | 0.029 | 8/30 (PANC-1, BT-474, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.092 | 4/33 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.55× | +3.1 | 0.11 | 3/12 (PANC-1, SNU-423, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.27× | +3.1 | 0.11 | 6/29 (SW 900, HOP62, …) | top dose only |  |
| [[Vismodegib (drug)]] 0.05 µM |  | 1.25× | +3.0 | 0.14 | 5/31 (NCI-H460, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12495.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.499×** | -13.2 | 3e-37 | 20/31 (HS-578T, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.408×** | -11.6 | 1e-28 | 20/31 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.489×** | -9.6 | 1e-19 | 17/20 (SW1417, SNU-423, …) | two highest doses | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.647×** | -8.3 | 2e-14 | 19/29 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.568×** | -7.3 | 3e-11 | 18/28 (HS-578T, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.586×** | -7.2 | 6e-11 | 16/30 (NCI-H460, HS-578T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.629×** | -6.2 | 4e-08 | 15/31 (HepG2/C3A, SW1417, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.679×** | -5.2 | 1e-05 | 13/33 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.712×** | -4.4 | 7e-04 | 13/30 (A-172, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **0.727×** | -4.1 | 0.002 | 11/12 (PANC-1, MIA PaCa-2, …) | two highest doses | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.815×** | -3.9 | 0.006 | 8/33 (A-172, HOP62, …) | top dose only |  |
| [[palbociclib (drug)]] 0.05 µM |  | **0.755×** | -3.6 | 0.018 | 8/31 (SHP-77, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.767×** | -3.4 | 0.027 | 6/31 (NCI-H2347, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.780×** | -3.3 | 0.035 | 14/29 (hTERT-HPNE, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12495. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 24.0 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -11.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.404× (z -9.2) |
| [[HS-578T (line)]] | alt | 7.85 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0773× (z -16.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0675× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 9.02 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0804× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.144× (z -11.9) |
| [[C-33 A (line)]] | alt | 26.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[HOP62 (line)]] | alt | 6.43 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -13.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.137× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 6.06 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0911× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 7.18 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0701× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SW480 (line)]] | alt | 5.14 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A-427 (line)]] | wt | 7.78 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -9.5) |
| [[A549 (line)]] | wt | 13.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -9.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 9.96 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.104× (z -9.9) ⚠ cell-cycle shift, explains ~73% of this change |
| [[MIA PaCa-2 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H1792 (line)]] | alt | 7.74 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0851× (z -10.3) |
| [[PANC-1 (line)]] | alt | 4.93 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[RKO (line)]] | wt | 8.50 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 11.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -9.5) |
| [[SW1417 (line)]] | alt | 8.39 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0859× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A498 (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.355 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.522 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.334 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.457 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12495), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZIM2-AS1]] | +0.71 | +0.66 / +0.63 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ZFP28]] | +0.70 | +0.76 / +0.59 | both halves | 7e-06 | same gene group; ⚠ same locus (38.5 kb, same strand: neighbours can correlate without regulation) |
| [[LRFN3]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[RNF216P1]] | +0.68 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[ZNF559]] | +0.68 | +0.59 / +0.68 | both halves | 7e-06 | same gene group |
| [[ZNF329]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 | same gene group |
| [[ZNF549]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 | same gene group |
| [[USP35]] | +0.63 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | +0.62 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[ZNF420]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 | same gene group |
| [[NUDCD3]] | +0.61 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[POMGNT2]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ZNF692]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 | same gene group |
| [[ZNF567]] | +0.61 | +0.44 / +0.65 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2B]] | -0.59 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[HIVEP2-DT]] | -0.58 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | -0.55 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[RFX3]] | -0.54 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[USP11]] | -0.53 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[CACNA2D1]] | -0.51 | -0.50 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 8, C 7. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THRB]] | B | THRB activity lowers ZNF71's level | lines that do not express THRB (21) vs lines expressing it (29) | 2.48× higher at baseline in the lines without THRB | 0.003 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[TOP2A]] | B | TOP2A activity raises ZNF71's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF420]] | B | ZNF420 activity raises ZNF71's level | lines that do not express ZNF420 (7) vs lines expressing it (43) | 4.46× lower at baseline in the lines without ZNF420 | 0.040 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF850, ZNF540 |
| [[ZNF329]] | B | ZNF329 activity raises ZNF71's level | lines that do not express ZNF329 (7) vs lines expressing it (43) | 1.87× lower at baseline in the lines without ZNF329 | 0.045 | ⚠ within organs, on part of the lines; also absent: C2orf27A |
| [[ZNF567-DT]] | B | ZNF567-DT activity raises ZNF71's level | lines that do not express ZNF567-DT (6) vs lines expressing it (44) | 4.27× lower at baseline in the lines without ZNF567-DT | 0.065 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540 |
| [[ZNF891]] | B | ZNF891 activity raises ZNF71's level | lines that do not express ZNF891 (7) vs lines expressing it (43) | 3.07× lower at baseline in the lines without ZNF891 | 0.079 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KMT2D; also absent: ENSG00000256825, ZNF140, CEP126 |
| [[PSMB5]] | B | PSMB5 activity lowers ZNF71's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF569]] | B | ZNF569 activity raises ZNF71's level | lines that do not express ZNF569 (14) vs lines expressing it (36) | 2.36× lower at baseline in the lines without ZNF569 | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF570, PEG10, DNAAF9 |
| [[ZIM2-AS1]] | C | ZIM2-AS1 activity raises ZNF71's level | lines that do not express ZIM2-AS1 (13) vs lines expressing it (37) | 5.83× lower at baseline in the lines without ZIM2-AS1 | 4e-05 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZFP28; co-absent with the target |
| [[ZFP28]] | C | ZFP28 activity raises ZNF71's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 4.29× lower at baseline in the lines without ZFP28 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6; co-absent with the target |
| [[ZNF470]] | C | ZNF470 activity raises ZNF71's level | lines that do not express ZNF470 (18) vs lines expressing it (32) | 4.54× lower at baseline in the lines without ZNF470 | 5e-04 | ⚠ within organs, on part of the lines; also absent: ZFP28, ZNF71, ZIM2-AS1; co-absent with the target |
| [[ZNF471]] | C | ZNF471 activity raises ZNF71's level | lines that do not express ZNF471 (28) vs lines expressing it (22) | 3.30× lower at baseline in the lines without ZNF471 | 0.004 | ⚠ within organs, on part of the lines; also absent: TRIML2, ZNF667, ZNF667-AS1; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 19, C 5. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF891]] | B | ZNF71 activity raises ZNF891's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 2.55× lower at baseline in the lines without ZNF71 | 6e-04 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28 |
| [[ZNF84]] | B | ZNF71 activity raises ZNF84's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 1.91× lower at baseline in the lines without ZNF71 | 0.004 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28 |
| [[ZNF420]] | B | ZNF71 activity raises ZNF420's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 3.05× lower at baseline in the lines without ZNF71 | 0.004 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28 |
| [[ZNF329]] | B | ZNF71 activity raises ZNF329's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 2.10× lower at baseline in the lines without ZNF71 | 0.006 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28 |
| [[ZNF527]] | B | ZNF71 activity raises ZNF527's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 1.86× lower at baseline in the lines without ZNF71 | 0.011 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28 |
| [[THRB]] | B | ZNF71 activity lowers THRB's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 2.86× higher at baseline in the lines without ZNF71 | 0.015 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28 |
| [[ZNF496]] | B | ZNF71 activity raises ZNF496's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 1.63× lower at baseline in the lines without ZNF71 | 0.016 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28 |
| [[ZNF567-DT]] | B | ZNF71 activity raises ZNF567-DT's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 1.79× lower at baseline in the lines without ZNF71 | 0.022 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28 |
| [[ZNF461]] | B | ZNF71 activity raises ZNF461's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 2.92× lower at baseline in the lines without ZNF71 | 0.024 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28 |
| [[ZNF790-AS1]] | B | ZNF71 activity raises ZNF790-AS1's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 2.59× lower at baseline in the lines without ZNF71 | 0.024 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28 |
| [[ZNF875]] | B | ZNF71 activity raises ZNF875's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 2.05× lower at baseline in the lines without ZNF71 | 0.033 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28 |
| [[ZNF567]] | B | ZNF71 activity raises ZNF567's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 2.26× lower at baseline in the lines without ZNF71 | 0.038 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28 |

## Where it sits

- **Module**: [[Module 129]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.8, 28.3); signed map (-17.7, -16.0). **Vector** length 57.6, 10.3% of its response variance represented; |z| ≥ 3 in 739 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.3 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.7 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.7 | +5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | +2.5 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.9 | -11.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.0 | -13.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.7 | -7.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.7 | -4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -3.9 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -0.8 | -0.4 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -0.8 | -1.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.7 | -1.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -0.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 71 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.4 — chr19:56,595,300-56,626,481 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Cos26, EZFIT |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQZ8](https://www.uniprot.org/uniprotkb/Q9NQZ8) (Endothelial zinc finger protein induced by tumor necrosis factor alpha):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [58491](https://www.ncbi.nlm.nih.gov/gene/58491):

> Predicted to enable DNA-binding transcription activator activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13141](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13141) · Entrez [58491](https://www.ncbi.nlm.nih.gov/gene/58491) · UniProt [Q9NQZ8](https://www.uniprot.org/uniprotkb/Q9NQZ8) · Ensembl [ENSG00000197951](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197951)

## Data

Gene col 12495: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12495); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12495, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12495]; `tensor/DDL_lfc|DDL_z.npy` [12495]; `embed/gene_vectors.npy` [12495]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12495 or target_col == 12495). Every well: [[ZNF71 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF71.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
