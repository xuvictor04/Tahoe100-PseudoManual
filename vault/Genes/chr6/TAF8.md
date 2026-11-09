---
symbol: "TAF8"
type: "gene"
col: 6011
ensembl_id: "ENSG00000137413"
name: "TATA-box binding protein associated factor 8"
location: "6p21.1"
module: 154
arm: "+"
pooled_cpm: 24.28
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 9
n_dd_up_clean: 19
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# TAF8

*TATA-box binding protein associated factor 8* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.32× (z +6.0, q 8e-07, up in 21 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.491× (z -8.1, q 4e-13, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFIC]] (+0.56, fdr 1e-05), [[ZBTB40]] (+0.53, fdr 2e-05), [[CCND3]] (+0.52, fdr 2e-05, ⚠ same locus), [[MRFAP1]] (+0.51, fdr 1e-05); moves opposite to [[TTYH2]] (-0.53, fdr 4e-05), [[KHDRBS3]] (-0.53, fdr 2e-05), [[NOTCH2]] (-0.52, fdr 1e-05).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GRB10]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6011.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +6.0 | 8e-07 | 21/47 (LoVo, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.31×** | +5.9 | 8e-07 | 20/47 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.31×** | +5.9 | 8e-07 | 21/47 (LOX-IMVI, RPMI-7951, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.30×** | +5.2 | 2e-05 | 18/47 (SNU-423, PANC-1, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.26×** | +5.1 | 4e-05 | 18/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +5.0 | 4e-05 | 20/48 (COLO 205, HCT15, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.25×** | +4.9 | 7e-05 | 20/47 (H4, A-172, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.25×** | +4.8 | 9e-05 | 16/47 (PANC-1, Hs 766T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.23×** | +4.6 | 3e-04 | 17/47 (PANC-1, LOX-IMVI, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +4.5 | 4e-04 | 9/47 (LoVo, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +4.5 | 4e-04 | 17/47 (COLO 205, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.23×** | +4.4 | 4e-04 | 17/47 (PANC-1, RPMI-7951, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.22×** | +4.4 | 5e-04 | 17/47 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +4.4 | 5e-04 | 17/47 (A-427, SNU-423, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.15× | +4.3 | 7e-04 | 15/48 (Hs 766T, PANC-1, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.21×** | +4.1 | 0.001 | 14/48 (Hs 766T, HS-578T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6011.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.491×** | -8.1 | 4e-13 | 29/48 (SNU-1, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.792×** | -7.2 | 2e-10 | 26/47 (A498, COLO 205, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.719×** | -6.9 | 1e-09 | 27/48 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -6.3 | 5e-08 | 23/47 (RKO, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.752×** | -6.2 | 7e-08 | 26/47 (SW480, A498, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.690×** | -4.2 | 0.002 | 14/47 (HEC-1-A, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.716×** | -3.8 | 0.012 | 13/48 (SW480, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.738×** | -3.4 | 0.041 | 11/46 (RPMI-7951, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.742×** | -3.4 | 0.045 | 13/47 (Hs 766T, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | 0.862× | -3.2 | 0.070 | 19/44 (A-427, COLO 205, …) | two highest doses | composition shift |
| [[Silodosin (drug)]] 5 µM |  | 0.860× | -3.1 | 0.085 | 9/47 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.767× | -3.0 | 0.12 | 12/46 (NCI-H2030, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6011. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 179 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -10.0) |
| [[A498 (line)]] | wt | 16.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 18.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 33.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AN3 CA (line)]] | alt | 31.3 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0938× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 32.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.173× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~15% of this change |
| [[Hs 766T (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.134× (z -8.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -23.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 38.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -17.8) |
| [[NCI-H460 (line)]] | wt | 17.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.2) |
| [[RKO (line)]] | wt | 26.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -10.4) |
| [[SW 1271 (line)]] | alt | 43.5 | 0 | 1 | — | [[Talc (drug)]] 0.05 µM 0.0697× (z -8.5) |
| [[SW48 (line)]] | wt | 17.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -9.8) |
| [[A-172 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 34.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6011), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFIC]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[ZBTB40]] | +0.53 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[CCND3]] | +0.52 | +0.47 / +0.55 | both halves | 2e-05 | ⚠ same locus (0.2 kb: neighbours can correlate without regulation) |
| [[MRFAP1]] | +0.51 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[COA5]] | +0.51 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[NCBP3]] | +0.51 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[JPX]] | +0.48 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[MAU2]] | +0.48 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[SDHAF2]] | +0.48 | +0.43 / +0.46 | both halves | 4e-05 |  |
| [[USP19]] | +0.48 | +0.51 / +0.38 | both halves | 6e-05 |  |
| [[NMT1]] | +0.48 | +0.41 / +0.53 | both halves | 4e-05 | pathway: HIV Infection |
| [[HDAC8]] | +0.48 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[RBM15]] | +0.48 | +0.56 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTYH2]] | -0.53 | -0.50 / -0.43 | both halves | 4e-05 |  |
| [[KHDRBS3]] | -0.53 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[NOTCH2]] | -0.52 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[FAM107B]] | -0.52 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[TNFRSF11A]] | -0.51 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[FNBP1]] | -0.50 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[MGAT5]] | -0.48 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[LRRC49]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[FGFR1]] | -0.48 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[OLA1]] | -0.48 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[PTHLH]] | -0.47 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[KALRN]] | -0.47 | -0.38 / -0.47 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRB10]] | B | GRB10 activity lowers TAF8's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 1.59× higher at baseline in the lines without GRB10 | 0.009 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |
| [[NR3C1]] | B | NR3C1 activity raises TAF8's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[FAM107B]] | B | FAM107B activity lowers TAF8's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 1.28× higher at baseline in the lines without FAM107B | 0.058 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[TOP2A]] | B | TOP2A activity raises TAF8's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF649]] | B | ZNF649 activity raises TAF8's level | lines that do not express ZNF649 (13) vs lines expressing it (37) | 1.37× lower at baseline in the lines without ZNF649 | 0.094 | ⚠ within organs, on part of the lines; also absent: ZNF577, ZNF681, RPSAP58 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction -0.554). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.7, 8.4); signed map (-6.6, -15.8). **Vector** length 89.2, 17.4% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.9 | +6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.4 | +5.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.2 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +4.0 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +4.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.5 | +5.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.3 | +4.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.2 | +5.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.0 | +4.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -7.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -6.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -6.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -6.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.1 | -8.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.3 | -4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:42,050,513-42,087,461 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32821, TAF(II)43; previously TBN |
| Gene groups (HGNC) | General transcription factor IID complex subunits |
| Reactome | 20 pathways, smallest: HIV Transcription Initiation; RNA Polymerase II HIV Promoter Escape; RNA Polymerase II Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z7C8](https://www.uniprot.org/uniprotkb/Q7Z7C8) (Transcription initiation factor TFIID subunit 8):

> The TFIID basal transcription factor complex plays a major role in the initiation of RNA polymerase II (Pol II)-dependent transcription. TFIID recognizes and binds promoters with or without a TATA box via its subunit TBP, a TATA-box-binding protein, and promotes assembly of the pre-initiation complex (PIC). The TFIID complex consists of TBP and TBP-associated factors (TAFs), including TAF1, TAF2, TAF3, TAF4, TAF5, TAF6, TAF7, TAF8, TAF9, TAF10, TAF11, TAF12 and TAF13. The TFIID complex …

**Summary**, from NCBI Gene [129685](https://www.ncbi.nlm.nih.gov/gene/129685):

> This gene encodes one of several TATA-binding protein (TBP)-associated factors (TAFs), which are integral subunits of the general transcription factor complex TFIID. TFIID recognizes the core promoter of many genes and nucleates the assembly of a transcription preinitiation complex containing RNA polymerase II and other initiation factors. The protein encoded by this gene contains an H4-like histone fold domain, and interacts with several subunits of TFIID including TBP and the histone-fold …

**Accessions** — [HGNC:17300](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17300) · Entrez [129685](https://www.ncbi.nlm.nih.gov/gene/129685) · UniProt [Q7Z7C8](https://www.uniprot.org/uniprotkb/Q7Z7C8) · Ensembl [ENSG00000137413](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137413)

## Data

Gene col 6011: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6011); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6011, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6011]; `tensor/DDL_lfc|DDL_z.npy` [6011]; `embed/gene_vectors.npy` [6011]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6011 or target_col == 6011). Every well: [[TAF8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
