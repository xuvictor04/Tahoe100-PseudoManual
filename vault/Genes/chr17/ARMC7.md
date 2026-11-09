---
symbol: "ARMC7"
type: "gene"
col: 4615
ensembl_id: "ENSG00000125449"
name: "armadillo repeat containing 7"
location: "17q25.1"
module: 21
arm: "+"
pooled_cpm: 9.71
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# ARMC7

*armadillo repeat containing 7* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.69× (z +27.1, q 0e+00, up in 16 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.59× (z +7.1, q 1e-10, up in 21 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.687× (z -5.4, q 4e-05, down in 16 of 43 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAP1]] (+0.53, fdr 2e-05), [[FUT10]] (+0.52, fdr 2e-04), [[KCTD2]] (+0.52, fdr 1e-04, ⚠ same locus), [[GDPD4]] (+0.49, fdr 7e-05); moves opposite to [[FRYL]] (-0.43, fdr 1e-04), [[SYNRG]] (-0.42, fdr 3e-04), [[APOA1]] (-0.39, fdr 0.002, ⚠ not reproduced), [[SLC34A2]] (-0.38, fdr 2e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LAD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4615.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.69×** | +27.1 | 0e+00 | 16/18 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.51×** | +26.3 | 0e+00 | 29/32 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.05×** | +15.9 | 0e+00 | 18/24 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +7.4 | 2e-11 | 17/35 (CFPAC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +7.1 | 1e-10 | 21/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +6.0 | 3e-07 | 19/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +5.9 | 3e-07 | 15/47 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +5.2 | 2e-05 | 11/47 (HepG2/C3A, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +4.3 | 9e-04 | 16/42 (NCI-H2347, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.2 | 0.001 | 9/31 (SW1417, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +3.9 | 0.005 | 9/39 (CFPAC-1, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.006 | 14/43 (A-427, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.011 | 7/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.26×** | +3.6 | 0.013 | 4/47 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.015 | 7/43 (CFPAC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.033 | 3/47 (CFPAC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.051 | 4/45 (PANC-1, KATO III, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.059 | 4/46 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.065 | 11/46 (KATO III, CFPAC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4615.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -5.4 | 4e-05 | 16/43 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.746×** | -4.5 | 0.002 | 15/47 (HT-29, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Salicylic acid (drug)]] 5 µM |  | 0.841× | -3.8 | 0.027 | 6/47 (NCI-H1792, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.803×** | -3.4 | 0.092 | 9/47 (BT-474, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.806×** | -3.3 | 0.092 | 11/46 (HOP62, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.814× | -3.2 | 0.13 | 11/46 (HepG2/C3A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.817× | -3.1 | 0.14 | 10/47 (SW48, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.809× | -3.1 | 0.16 | 13/41 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4615. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 6.91 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 32.0× (z +15.2) ⚠ toxic; transcription drop | [[Bosentan (hydrate) (drug)]] 5 µM 0.118× (z -9.5) |
| [[A-427 (line)]] | wt | 13.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 8.62 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 15.2× (z +10.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 7.16 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 15.2× (z +10.5) ⚠ toxic; transcription drop | [[Radotinib (drug)]] 0.5 µM 0.110× (z -8.5) |
| [[KATO III (line)]] | alt | 13.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 44.8× (z +20.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 14.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 30.7× (z +23.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 15.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.2× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 20.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.93× (z +15.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 6.40 | 0 | 2 | — | [[Bisoprolol (hemifumarate) (drug)]] 5 µM 0.0568× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 21.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.12× (z +15.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 4.11 | 0 | 2 (1 ⚠) | — | [[Captopril (drug)]] 0.05 µM 0.0666× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 11.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.38× (z +8.8) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 9.21 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 13.0× (z +11.0) ⚠ toxic; transcription drop | [[Thymol (drug)]] 0.5 µM 0.0713× (z -11.4) |
| [[PANC-1 (line)]] | alt | 8.71 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.15× (z +14.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 8.13 | 0 | 1 | — | [[Sulfatinib (drug)]] 5 µM 0.0678× (z -9.2) |
| [[COLO 205 (line)]] | alt | 9.12 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0739× (z -9.8) |
| [[HOP62 (line)]] | alt | 7.14 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.28× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 5.49 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 9.88× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 8.26 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.171× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 8.02 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.99× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4615), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 10 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAP1]] | +0.53 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[FUT10]] | +0.52 | +0.31 / +0.60 | both halves | 2e-04 |  |
| [[KCTD2]] | +0.52 | +0.32 / +0.55 | both halves | 1e-04 | STRING 598; ⚠ same locus (44.1 kb, same strand: neighbours can correlate without regulation) |
| [[GDPD4]] | +0.49 | +0.37 / +0.49 | both halves | 7e-05 |  |
| [[RPRD1A]] | +0.49 | +0.31 / +0.49 | both halves | 2e-04 |  |
| [[TCEA2]] | +0.47 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[ZC3H3]] | +0.47 | +0.39 / +0.48 | both halves | 6e-05 |  |
| [[RCAN3]] | +0.47 | +0.30 / +0.45 | both halves | 2e-04 |  |
| [[GOLGA7B-DT]] | +0.47 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[CDA]] | +0.47 | +0.30 / +0.54 | both halves | 2e-04 |  |
| [[TMEM138]] | +0.45 | +0.19 / +0.57 | ⚠ one half (not replicated) | 8e-04 |  |
| [[KLKP1-1]] | +0.45 | +0.32 / +0.51 | both halves | 1e-04 |  |
| [[SPEG]] | +0.44 | +0.36 / +0.37 | both halves | 1e-04 |  |
| [[RPS6KA4]] | +0.44 | +0.32 / +0.41 | both halves | 2e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRYL]] | -0.43 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[SYNRG]] | -0.42 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[APOA1]] | -0.39 | -0.14 / -0.28 | ⚠ not reproduced | 0.002 |  |
| [[SLC34A2]] | -0.38 | -0.32 / -0.30 | both halves | 2e-04 |  |
| [[GSTP1]] | -0.38 | -0.21 / -0.37 | both halves | 7e-04 |  |
| [[UBE3B]] | -0.37 | -0.22 / -0.48 | both halves | 6e-04 |  |
| [[SNHG31]] | -0.37 | -0.25 / -0.34 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAD1]] | B | LAD1 activity raises ARMC7's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 1.64× lower at baseline in the lines without LAD1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[TNNT2]] | B | TNNT2 activity raises ARMC7's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 1.52× lower at baseline in the lines without TNNT2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[CAPN8]] | B | CAPN8 activity raises ARMC7's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 1.50× lower at baseline in the lines without CAPN8 | 0.032 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.101). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.6, 27.8); signed map (-14.9, -41.9). **Vector** length 69.2, 10.7% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.6 | +27.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.6 | +26.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.6 | +15.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.8 | +7.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.4 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +1.7 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -5.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | armadillo repeat containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,109,952-75,130,272 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22160 |
| Gene groups (HGNC) | Armadillo repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6L4](https://www.uniprot.org/uniprotkb/Q9H6L4) (Armadillo repeat-containing protein 7):

> As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs.

**Summary**, from NCBI Gene [79637](https://www.ncbi.nlm.nih.gov/gene/79637):

> Predicted to be involved in mRNA splicing, via spliceosome. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26168](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26168) · Entrez [79637](https://www.ncbi.nlm.nih.gov/gene/79637) · UniProt [Q9H6L4](https://www.uniprot.org/uniprotkb/Q9H6L4) · Ensembl [ENSG00000125449](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125449)

## Data

Gene col 4615: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4615); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4615, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4615]; `tensor/DDL_lfc|DDL_z.npy` [4615]; `embed/gene_vectors.npy` [4615]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4615 or target_col == 4615). Every well: [[ARMC7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARMC7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
