---
symbol: "NUS1"
type: "gene"
col: 7759
ensembl_id: "ENSG00000153989"
name: "NUS1 dehydrodolichyl diphosphate synthase subunit"
location: "6q22.1"
module: 56
arm: "+"
pooled_cpm: 85.41
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# NUS1

*NUS1 dehydrodolichyl diphosphate synthase subunit* — 6q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 3.35× (z +8.1, q 2e-13, up in 46 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (CFPAC-1 7.29×, NCI-H2347 4.68×, Panc 03.27 6.06×, PANC-1 5.49×, …; ⚠ cell-cycle shift, explains ~32% of this change); [[TAK-901 (drug)]] 5 µM in 4 lines (NCI-H2347 5.81×, CFPAC-1 5.94×, SK-MEL-2 6.87×, PANC-1 6.42×); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 2.97×, PANC-1 2.94×; ⚠ cell-cycle shift, explains ~30% of this change); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 5.25×); [[PH-797804 (drug)]] 5 µM in 1 line (PANC-1 7.09×).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.629× (z -8.3, q 5e-14, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM39A]] (+0.83, fdr 7e-06), [[GORASP2]] (+0.81, fdr 7e-06), [[PRRC1]] (+0.81, fdr 7e-06); moves opposite to [[BAZ2B]] (-0.62, fdr 5e-05), [[TSC22D1]] (-0.60, fdr 2e-05), [[CUX1]] (-0.58, fdr 4e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7759.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (CFPAC-1 7.29×, NCI-H2347 4.68×, Panc 03.27 6.06×, PANC-1 5.49×, …; ⚠ cell-cycle shift, explains ~32% of this change); [[TAK-901 (drug)]] 5 µM in 4 lines (NCI-H2347 5.81×, CFPAC-1 5.94×, SK-MEL-2 6.87×, PANC-1 6.42×); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 2.97×, PANC-1 2.94×; ⚠ cell-cycle shift, explains ~30% of this change); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 5.25×); [[PH-797804 (drug)]] 5 µM in 1 line (PANC-1 7.09×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **3.35×** | +8.1 | 2e-13 | 46/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **3.34×** | +8.0 | 2e-13 | 47/49 (NCI-H2347, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +4.1 | 0.009 | 35/48 (NCI-H460, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7759.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.629×** | -8.3 | 5e-14 | 39/49 (NCI-H1573, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.691×** | -6.6 | 9e-09 | 33/48 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.607×** | -6.4 | 4e-08 | 39/49 (AsPC-1, SW 900, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.597×** | -6.3 | 4e-08 | 35/44 (NCI-H2030, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.624×** | -6.0 | 2e-07 | 37/48 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.659×** | -5.1 | 3e-05 | 32/48 (SW48, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.700×** | -4.4 | 0.001 | 27/48 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.718×** | -4.0 | 0.004 | 33/50 (LS 180, HT-29, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.745×** | -3.7 | 0.012 | 33/48 (LoVo, A-172, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.751×** | -3.5 | 0.027 | 24/48 (NCI-H2030, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.766×** | -3.4 | 0.038 | 25/48 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.776×** | -3.2 | 0.062 | 24/48 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.780×** | -3.1 | 0.072 | 23/48 (AsPC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.772×** | -3.0 | 0.097 | 22/45 (NCI-H1573, RPMI-7951, …) | all doses, stronger at high dose | composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7759. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 118 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +21.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 7.09× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 66.7 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.29× (z +26.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.94× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -9.8) |
| [[HOP62 (line)]] | alt | 81.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -10.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.425× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 65.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +22.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.81× (z +9.6) | — |
| [[A498 (line)]] | wt | 90.4 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +13.4) ⚠ cell-cycle shift, explains ~32% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -9.8) |
| [[HT-29 (line)]] | alt | 94.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -11.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 70.9 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.87× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW48 (line)]] | wt | 88.0 | 1 | 1 | [[TAK-901 (drug)]] 0.05 µM 5.25× (z +10.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -8.6) |
| [[SW480 (line)]] | alt | 104 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -10.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 53.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -10.7) |
| [[A549 (line)]] | wt | 75.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[AsPC-1 (line)]] | alt | 98.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[BT-474 (line)]] | alt | 56.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.352× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 61.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[CHP-212 (line)]] | wt | 92.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -9.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 83.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -13.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1573 (line)]] | alt | 87.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -14.1) |
| [[NCI-H1792 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 97.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 62.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +21.3) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[RKO (line)]] | wt | 82.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -11.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-1 (line)]] | wt | 95.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -9.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-423 (line)]] | alt | 96.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +19.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 106 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 85.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 103 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 104 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 122 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 86.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 69.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 97.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 97.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 80.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7759), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM39A]] | +0.83 | +0.86 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[GORASP2]] | +0.81 | +0.84 / +0.68 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.81 | +0.88 / +0.61 | both halves | 7e-06 |  |
| [[SEC13]] | +0.77 | +0.80 / +0.65 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC23A]] | +0.75 | +0.79 / +0.66 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC61A1]] | +0.75 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[CLINT1]] | +0.73 | +0.79 / +0.57 | both halves | 1e-05 |  |
| [[PDIA5]] | +0.73 | +0.78 / +0.53 | both halves | 1e-05 |  |
| [[COG6]] | +0.72 | +0.76 / +0.57 | both halves | 9e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC24D]] | +0.72 | +0.78 / +0.55 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[DDB1]] | +0.72 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[COPA]] | +0.71 | +0.78 / +0.57 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2B]] | -0.62 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[TSC22D1]] | -0.60 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[CUX1]] | -0.58 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[PNRC2]] | -0.57 | -0.61 / -0.38 | both halves | 7e-05 |  |
| [[ZBED5]] | -0.57 | -0.64 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NUS1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.1, -32.6); signed map (-51.4, 9.3). **Vector** length 107, 33.4% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ER to Golgi Anterograde Transport* (reactome, mean cos +0.60 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.60 to 16); *protein secretion* (hallmark, mean cos +0.52 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.2 | +8.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +8.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | -1.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | -0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | -0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +0.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.2 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +0.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | +1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.1 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -0.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | NUS1 dehydrodolichyl diphosphate synthase subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.1 — chr6:117,675,469-117,710,727 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC7199, NgBR, TANGO14; previously C6orf68 |
| Gene groups (HGNC) | Dehydrodolichyl diphosphate synthase |
| Reactome | 7 pathways, smallest: Synthesis of dolichyl-phosphate; Diseases associated with glycosylation precursor biosynthesis; Synthesis of substrates in N-glycan biosythesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96E22](https://www.uniprot.org/uniprotkb/Q96E22) (Dehydrodolichyl diphosphate synthase complex subunit NUS1):

> With DHDDS, forms the dehydrodolichyl diphosphate synthase (DDS) complex, an essential component of the dolichol monophosphate (Dol-P) biosynthetic machinery. Both subunits contribute to enzymatic activity, i.e. condensation of multiple copies of isopentenyl pyrophosphate (IPP) to farnesyl pyrophosphate (FPP) to produce dehydrodolichyl diphosphate (Dedol-PP), a precursor of dolichol phosphate which is utilized as a sugar carrier in protein glycosylation in the endoplasmic reticulum (ER). …

**Summary**, from NCBI Gene [116150](https://www.ncbi.nlm.nih.gov/gene/116150):

> This gene encodes a type I single transmembrane domain receptor, which is a subunit of cis-prenyltransferase, and serves as a specific receptor for the neural and cardiovascular regulator Nogo-B. The encoded protein is essential for dolichol synthesis and protein glycosylation. This gene is highly expressed in non-small cell lung carcinomas as well as estrogen receptor-alpha positive breast cancer cells where it promotes epithelial mesenchymal transition. This gene is associated with the poor …

**Accessions** — [HGNC:21042](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21042) · Entrez [116150](https://www.ncbi.nlm.nih.gov/gene/116150) · UniProt [Q96E22](https://www.uniprot.org/uniprotkb/Q96E22) · Ensembl [ENSG00000153989](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153989)

## Data

Gene col 7759: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7759); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7759, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7759]; `tensor/DDL_lfc|DDL_z.npy` [7759]; `embed/gene_vectors.npy` [7759]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7759 or target_col == 7759). Every well: [[NUS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
