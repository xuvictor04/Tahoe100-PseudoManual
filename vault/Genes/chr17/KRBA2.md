---
symbol: "KRBA2"
type: "gene"
col: 11559
ensembl_id: "ENSG00000184619"
name: "KRAB domain containing 2"
location: "17p13.1"
module: 10
arm: "+"
pooled_cpm: 7.71
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 9
n_dd_up_clean: 23
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# KRBA2

*KRAB domain containing 2* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 3.54× (z +15.3, q 0e+00, up in 31 of 35 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.36× (z +15.3, q 0e+00, up in 31 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.545× (z -7.6, q 1e-11, down in 26 of 47 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.555× (z -7.4, q 4e-11, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (75 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 25 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCNX4-DT]] (+0.77, fdr 1e-04), [[ERCC6L2-AS1]] (+0.77, fdr 7e-06), [[TMEM202-AS1]] (+0.77, fdr 1e-04); moves opposite to [[NPHP4]] (-0.65, fdr 3e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[OTUD7A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11559.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.54×** | +15.3 | 0e+00 | 31/35 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +15.3 | 0e+00 | 31/46 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.24×** | +14.4 | 2e-44 | 33/43 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.07×** | +12.9 | 4e-36 | 41/48 (A-427, A549, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.50×** | +10.7 | 2e-24 | 16/22 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.39×** | +8.0 | 9e-14 | 8/16 (SW480, A498, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +8.0 | 1e-13 | 23/44 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +7.4 | 1e-11 | 21/43 (HS-578T, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.5 | 3e-06 | 19/48 (A-172, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +5.2 | 1e-05 | 17/46 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.51×** | +5.2 | 1e-05 | 18/47 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +5.0 | 2e-05 | 19/44 (HS-578T, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.41×** | +4.3 | 7e-04 | 5/48 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.29×** | +4.2 | 9e-04 | 11/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.004 | 12/47 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.006 | 6/48 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.006 | 7/48 (NCI-H2030, HCT15, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.012 | 10/48 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.030 | 4/47 (A549, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11559.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.545×** | -7.6 | 1e-11 | 26/47 (A-427, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.555×** | -7.4 | 4e-11 | 26/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.637×** | -5.7 | 3e-06 | 22/43 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.657×** | -5.3 | 2e-05 | 23/47 (NCI-H1573, A-427, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.663×** | -5.2 | 3e-05 | 20/47 (A-427, SW480, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.667×** | -4.7 | 2e-04 | 16/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.701×** | -4.5 | 6e-04 | 17/47 (NCI-H460, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.825×** | -3.4 | 0.045 | 9/48 (J82, H4, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.751×** | -3.3 | 0.069 | 8/47 (PANC-1, A-427, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11559. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 3.49 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.69× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 8.01 | 1 (1 ⚠) | 2 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 10.2× (z +11.0) ⚠ toxic | [[Digitoxin (drug)]] 5 µM 0.0654× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.144× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 9.47 | 3 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.07× (z +9.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.00× (z +8.6) | — |
| [[A-172 (line)]] | wt | 3.51 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.51× (z +10.3) | — |
| [[A-427 (line)]] | wt | 17.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.276× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.279× (z -8.5) |
| [[A498 (line)]] | wt | 7.98 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 7.06 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 8.33× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.149× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[LOX-IMVI (line)]] | wt | 8.54 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 14.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +9.4) | [[Digitoxin (drug)]] 0.05 µM 0.0947× (z -11.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[PANC-1 (line)]] | alt | 6.95 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.199× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 1.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.8× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 7.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.82× (z +11.5) | — |
| [[C-33 A (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 4.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 4.35 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 12.4× (z +9.1) ⚠ toxic | — |
| [[LoVo (line)]] | wt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.54 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 14.6× (z +11.2) ⚠ toxic | — |
| [[NCI-H2347 (line)]] | alt | 2.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.60× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 20.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +9.0) | — |
| [[SW480 (line)]] | alt | 11.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.0) | — |
| [[A549 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11559), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 25 of them with an alert (⚠; 25 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX4-DT]] | +0.77 | +0.83 / +0.33 | both halves | 1e-04 |  |
| [[ERCC6L2-AS1]] | +0.77 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.77 | +0.82 / +0.33 | both halves | 1e-04 |  |
| [[LRRC37A3]] | +0.74 | +0.77 / +0.32 | both halves | 2e-04 |  |
| [[ZNF407-AS1]] | +0.74 | +0.76 / +0.49 | both halves | 2e-05 |  |
| [[PBLD]] | +0.73 | +0.76 / +0.32 | both halves | 2e-04 |  |
| [[DDX19A-DT]] | +0.73 | +0.80 / +0.40 | both halves | 5e-05 |  |
| [[TRAM2-AS1]] | +0.72 | +0.73 / +0.45 | both halves | 3e-05 |  |
| [[NUTM2E]] | +0.72 | +0.77 / +0.35 | both halves | 1e-04 |  |
| [[ZNF610]] | +0.72 | +0.69 / +0.42 | both halves | 4e-05 | same gene group |
| [[SEPTIN7-DT]] | +0.72 | +0.78 / +0.26 | both halves | 4e-04 |  |
| [[AHI1-DT]] | +0.71 | +0.69 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHP4]] | -0.65 | -0.67 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OTUD7A]] | B | OTUD7A activity raises KRBA2's level | lines that do not express OTUD7A (6) vs lines expressing it (44) | 1.96× lower at baseline in the lines without OTUD7A | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000256673, WWOX, RUNDC3A-AS1; maybe low, not absent |
| [[LNC-LBCS]] | B | LNC-LBCS activity raises KRBA2's level | lines that do not express LNC-LBCS (13) vs lines expressing it (37) | 1.62× lower at baseline in the lines without LNC-LBCS | 0.019 | ⚠ within organs, on part of the lines; also absent: ANKS1B, TERT, SAMD11; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers KRBA2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LRRIQ3]] | C | LRRIQ3 activity raises KRBA2's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.85× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.802). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (4.1, 14.8); signed map (26.2, -10.3). **Vector** length 76.5, 13.7% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.0 | +12.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +14.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +10.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.3 | +15.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +5.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +3.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | +1.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.8 | -0.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -5.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | KRAB domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:8,356,902-8,376,704 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KRBA2 |
| Gene groups (HGNC) | Integrase like retrotransposon derived; KRAB domain containing |
| Matched by | ensembl_id |

UniProt [Q6ZNG9](https://www.uniprot.org/uniprotkb/Q6ZNG9) carries no function annotation.

**Summary**, from NCBI Gene [124751](https://www.ncbi.nlm.nih.gov/gene/124751):

> Predicted to enable nucleic acid binding activity. Predicted to be involved in DNA integration and regulation of DNA-templated transcription. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26989) · Entrez [124751](https://www.ncbi.nlm.nih.gov/gene/124751) · UniProt [Q6ZNG9](https://www.uniprot.org/uniprotkb/Q6ZNG9) · Ensembl [ENSG00000184619](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184619)

## Data

Gene col 11559: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11559); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11559, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11559]; `tensor/DDL_lfc|DDL_z.npy` [11559]; `embed/gene_vectors.npy` [11559]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11559 or target_col == 11559). Every well: [[KRBA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRBA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
