---
symbol: "TMEM243"
type: "gene"
col: 5663
ensembl_id: "ENSG00000135185"
name: "transmembrane protein 243"
location: "7q21.12"
module: 49
arm: "+"
pooled_cpm: 32.01
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 30
n_dd_up_clean: 1
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# TMEM243

*transmembrane protein 243* — 7q21.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.28× (z +4.5, q 0.005, up in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 3.42×).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.436× (z -21.0, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COG6]] (+0.72, fdr 7e-06), [[PDIA5]] (+0.71, fdr 7e-06), [[TMED3]] (+0.70, fdr 7e-06); moves opposite to [[BAZ2B]] (-0.62, fdr 1e-05), [[VPS35L]] (-0.59, fdr 1e-05), [[NCOA4]] (-0.59, fdr 1e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FAM98A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5663.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 3.42×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +4.5 | 0.005 | 22/48 (HepG2/C3A, LOX-IMVI, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | 1.29× | +3.2 | 0.23 | 10/47 (Hs 766T, H4, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | 1.14× | +3.2 | 0.23 | 8/48 (SW1417, LoVo, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.24 | 9/48 (NCI-H2347, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5663.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.436×** | -21.0 | 0e+00 | 43/47 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.362×** | -17.4 | 0e+00 | 42/47 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.419×** | -15.5 | 0e+00 | 43/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.420×** | -15.5 | 0e+00 | 45/48 (H4, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.481×** | -13.1 | 6e-37 | 40/48 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.486×** | -12.9 | 7e-36 | 39/45 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.540×** | -11.0 | 4e-26 | 41/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.591×** | -9.4 | 5e-19 | 31/48 (hTERT-HPNE, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.591×** | -9.4 | 5e-19 | 33/48 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.381×** | -9.0 | 1e-17 | 34/48 (HS-578T, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.617×** | -8.6 | 4e-16 | 32/48 (H4, A498, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -7.6 | 1e-12 | 28/45 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -6.9 | 2e-10 | 28/48 (AsPC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.669×** | -6.9 | 3e-10 | 30/48 (hTERT-HPNE, AsPC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.716×** | -6.0 | 1e-07 | 27/47 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.720×** | -5.8 | 2e-07 | 26/48 (H4, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5663. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 78.1 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -14.6) |
| [[HS-578T (line)]] | alt | 38.4 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -18.2) |
| [[AsPC-1 (line)]] | alt | 40.0 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -21.1) |
| [[KATO III (line)]] | alt | 42.4 | 0 | 8 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0376× (z -33.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.396× (z -13.1) |
| [[A498 (line)]] | wt | 114 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -37.4) |
| [[hTERT-HPNE (line)]] | wt | 47.2 | 0 | 7 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -11.7) |
| [[A-172 (line)]] | wt | 26.5 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.122× (z -16.8) |
| [[HOP62 (line)]] | alt | 25.0 | 0 | 5 | — | [[Harringtonine (drug)]] 0.5 µM 0.128× (z -15.3) |
| [[HT-29 (line)]] | alt | 45.3 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.251× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.387× (z -11.7) |
| [[PANC-1 (line)]] | alt | 14.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -19.9) |
| [[Hs 766T (line)]] | wt | 45.2 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 32.0 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.174× (z -13.0) |
| [[SW1417 (line)]] | alt | 36.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.348× (z -13.2) |
| [[SW480 (line)]] | alt | 31.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 32.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -14.2) |
| [[LoVo (line)]] | wt | 44.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -9.6) |
| [[J82 (line)]] | alt | 33.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 31.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 38.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.329× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.345× (z -9.0) |
| [[RKO (line)]] | wt | 31.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 36.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.200× (z -10.0) |
| [[SNU-1 (line)]] | wt | 43.5 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.129× (z -12.1) |
| [[SW 900 (line)]] | alt | 36.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -11.8) |
| [[A549 (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[BT-474 (line)]] | alt | 24.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -8.7) |
| [[COLO 205 (line)]] | alt | 32.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -8.8) |
| [[HCT15 (line)]] | alt | 27.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LOX-IMVI (line)]] | wt | 20.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.210× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 17.1 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.306× (z -8.9) |
| [[SHP-77 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -10.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 28.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +12.4) | — |
| [[SW48 (line)]] | wt | 63.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5663), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG6]] | +0.72 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[PDIA5]] | +0.71 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[TMED3]] | +0.70 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[PDXDC2P]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[PDXDC1]] | +0.69 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[ISOC2]] | +0.69 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[AKR1A1]] | +0.68 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[NAA35]] | +0.67 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[ERLEC1]] | +0.67 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[PRRC1]] | +0.67 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[BET1L]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2B]] | -0.62 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[VPS35L]] | -0.59 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[NCOA4]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.58 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[MED1]] | -0.57 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[DDX6]] | -0.57 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[ATRX]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[CUX1]] | -0.56 | -0.51 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TMEM243's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SNHG18]] | B | SNHG18 activity raises TMEM243's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.46× lower at baseline in the lines without SNHG18 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM98A]] | C | TMEM243's natural level weakens FAM98A's drug response | TMEM243's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.27; direction not clear | 0.062 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.8, -33.8); signed map (-50.3, 8.4). **Vector** length 119, 33.4% of its response variance represented; |z| ≥ 3 in 1,275 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +4.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.7 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.2 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.0 | -0.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.4 | -15.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.6 | -11.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -17.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.5 | -3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.3 | -5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.1 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 243 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.12 — chr7:87,196,160-87,220,587 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4175, MM-TRAG; previously C7orf23 |
| Matched by | ensembl_id |

UniProt [Q9BU79](https://www.uniprot.org/uniprotkb/Q9BU79) carries no function annotation.

**Summary**, from NCBI Gene [79161](https://www.ncbi.nlm.nih.gov/gene/79161):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21707](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21707) · Entrez [79161](https://www.ncbi.nlm.nih.gov/gene/79161) · UniProt [Q9BU79](https://www.uniprot.org/uniprotkb/Q9BU79) · Ensembl [ENSG00000135185](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135185)

## Data

Gene col 5663: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5663); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5663, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5663]; `tensor/DDL_lfc|DDL_z.npy` [5663]; `embed/gene_vectors.npy` [5663]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5663 or target_col == 5663). Every well: [[TMEM243 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM243.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
