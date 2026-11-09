---
symbol: "YEATS4"
type: "gene"
col: 4803
ensembl_id: "ENSG00000127337"
name: "YEATS domain containing 4"
location: "12q15"
module: 22
arm: "+"
pooled_cpm: 27.65
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# YEATS4

*YEATS domain containing 4* — 12q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.94× (z +11.5, q 1e-27, up in 38 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.34× (z +5.1, q 4e-05, up in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 1.95×, A549 2.44×, BT-474 2.75×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A549 3.86×, A498 2.80×, NCI-H23 2.45×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 3.04×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.853× (z -9.4, q 3e-18, down in 20 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.627× (z -8.1, q 2e-13, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NHLRC2]] (+0.72, fdr 7e-06), [[DEK]] (+0.68, fdr 1e-05), [[CEP135]] (+0.64, fdr 1e-05); moves opposite to [[DEDD2]] (-0.59, fdr 2e-05), [[ZNF581]] (-0.56, fdr 2e-05), [[SPSB1]] (-0.55, fdr 1e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4803.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 1.95×, A549 2.44×, BT-474 2.75×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A549 3.86×, A498 2.80×, NCI-H23 2.45×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 3.04×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.94×** | +11.5 | 1e-27 | 38/43 (A549, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.97×** | +10.6 | 1e-23 | 30/36 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +8.6 | 2e-15 | 29/40 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.52×** | +6.5 | 9e-09 | 34/48 (NCI-H1573, RKO, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.37×** | +5.4 | 6e-06 | 24/47 (A549, C32, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +5.1 | 4e-05 | 21/48 (A549, LoVo, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.31×** | +4.7 | 2e-04 | 22/46 (NCI-H460, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.16× | +3.6 | 0.019 | 18/47 (PANC-1, A549, …) | all doses, flat | composition shift |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.031 | 10/48 (A498, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **1.22×** | +3.4 | 0.033 | 13/47 (NCI-H1573, A549, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **1.23×** | +3.2 | 0.062 | 18/47 (A-427, SNU-423, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.19× | +3.0 | 0.12 | 15/48 (NCI-H1573, LoVo, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4803.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.853× | -9.4 | 3e-18 | 20/48 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.627×** | -8.1 | 2e-13 | 33/47 (SW480, NCI-H2347, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.785×** | -5.9 | 7e-07 | 29/48 (A498, RKO, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.714×** | -5.5 | 5e-06 | 25/48 (H4, KATO III, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.612×** | -4.4 | 0.001 | 22/41 (NCI-H1792, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -3.9 | 0.009 | 18/47 (NCI-H23, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.652×** | -3.9 | 0.009 | 16/48 (A-427, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | 0.857× | -3.8 | 0.012 | 11/48 (J82, HT-29, …) | inconsistent across doses | position effect removed |
| [[olaparib (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.825×** | -3.3 | 0.059 | 10/47 (HEC-1-A, KATO III, …) | inconsistent across doses | position effect removed |
| [[Sildenafil (drug)]] 0.5 µM |  | **0.827×** | -3.3 | 0.062 | 6/47 (A549, C-33 A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4803. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 22.6 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Selinexor (drug)]] 5 µM 0.354× (z -12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.472× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 48.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -12.5) |
| [[A-427 (line)]] | wt | 78.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 30.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 30.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0772× (z -8.8) |
| [[BT-474 (line)]] | alt | 23.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0555× (z -11.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0942× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 26.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H661 (line)]] | alt | 39.2 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0739× (z -8.7) |
| [[PANC-1 (line)]] | alt | 37.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW480 (line)]] | alt | 37.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.390× (z -9.8) |
| [[A-172 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4803), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHLRC2]] | +0.72 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[DEK]] | +0.68 | +0.73 / +0.57 | both halves | 1e-05 | pathway: Transcriptional regulation by the AP-2 (TFAP2) family of transcription factors |
| [[CEP135]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[SKA3]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[EXOSC9]] | +0.63 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[SMC3]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[KIF15]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[CEP295]] | +0.61 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[SGO1]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[C2CD5]] | +0.61 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[NCAPH]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[MDM1]] | +0.60 | +0.48 / +0.67 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DEDD2]] | -0.59 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[ZNF581]] | -0.56 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[SPSB1]] | -0.55 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[ZNF841]] | -0.54 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[MBOAT7]] | -0.54 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[BAG3]] | -0.53 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[PIP5KL1]] | -0.53 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[ABCB6]] | -0.53 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[SPRED3]] | -0.52 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[VPS53]] | -0.52 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[ZFC3H1]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[RAB7A]] | -0.51 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises YEATS4's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without E2F8 | 0.082 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TOP2B]] | B | TOP2B activity raises YEATS4's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 5 µM | C | YEATS4's natural level lowers the cells' numbers under ERK5-IN-2 5 µM (makes them more sensitive) | YEATS4's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.365 over the table, 0.096 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.513). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.1, -51.9); signed map (-47.5, -47.0). **Vector** length 82.6, 17.0% of its response variance represented; |z| ≥ 3 in 771 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Condensation of Prometaphase Chromosomes* (reactome, mean cos +0.51 to 8); *Kinesins* (reactome, mean cos +0.50 to 10); *COPI-dependent Golgi-to-ER retrograde traffic* (reactome, mean cos +0.50 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +4.9 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.5 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.9 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.7 | +10.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +3.7 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +0.5 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | +1.4 | +1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.0 | -8.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.1 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | -2.7 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -1.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | YEATS domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q15 — chr12:69,359,710-69,390,870 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NuBI-1, GAS41, YAF9 |
| Gene groups (HGNC) | YEATS domain containing; SRCAP complex subunits; Tip60/Nua4 histone acetyltransferase complex subunits |
| Reactome | 5 pathways, smallest: Activation of the TFAP2 (AP-2) family of transcription factors; Transcriptional regulation by the AP-2 (TFAP2) family of transcription factors; HATs acetylate histones |
| Matched by | ensembl_id |

**Function**, from UniProt [O95619](https://www.uniprot.org/uniprotkb/O95619) (YEATS domain-containing protein 4):

> Chromatin reader component of the NuA4 histone acetyltransferase (HAT) complex, a complex involved in transcriptional activation of select genes principally by acetylation of nucleosomal histones H4 and H2A. Specifically recognizes and binds acylated histone H3, with a preference for histone H3 diacetylated at 'Lys-18' and 'Lys-27' (H3K18ac and H3K27ac) or histone H3 diacetylated at 'Lys-14' and 'Lys-27' (H3K14ac and H3K27ac). Also able to recognize and bind crotonylated histone H3. May also …

**Summary**, from NCBI Gene [8089](https://www.ncbi.nlm.nih.gov/gene/8089):

> The protein encoded by this gene is found in the nucleoli. It has high sequence homology to human MLLT1, and yeast and human MLLT3 proteins. Both MLLT1 and MLLT3 proteins belong to a class of transcription factors, indicating that the encoded protein might also represent a transcription factor. This protein is thought to be required for RNA transcription. This gene has been shown to be amplified in tumors. Alternative splicing results in multiple transcript variants encoding different isoforms. …

**Accessions** — [HGNC:24859](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24859) · Entrez [8089](https://www.ncbi.nlm.nih.gov/gene/8089) · UniProt [O95619](https://www.uniprot.org/uniprotkb/O95619) · Ensembl [ENSG00000127337](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127337)

## Data

Gene col 4803: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4803); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4803, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4803]; `tensor/DDL_lfc|DDL_z.npy` [4803]; `embed/gene_vectors.npy` [4803]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4803 or target_col == 4803). Every well: [[YEATS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YEATS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
