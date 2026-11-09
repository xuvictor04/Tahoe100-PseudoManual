---
symbol: "SNHG17"
type: "gene"
col: 12279
ensembl_id: "ENSG00000196756"
name: "small nucleolar RNA host gene 17"
location: "20q11.23"
module: 33
arm: "+"
pooled_cpm: 29.43
n_lines_expressing: 50
n_dd_up: 55
n_dd_down: 12
n_dd_up_clean: 39
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# SNHG17

*small nucleolar RNA host gene 17* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 55 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 3.13× (z +15.2, q 0e+00, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.602× (z -6.6, q 3e-08, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG15]] (+0.81, fdr 7e-06), [[NLE1]] (+0.79, fdr 7e-06), [[NOP16]] (+0.74, fdr 7e-06); moves opposite to [[ITM2B]] (-0.60, fdr 1e-05), [[PSENEN]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 55 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12279.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.13×** | +15.2 | 0e+00 | 38/47 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.59×** | +12.7 | 2e-34 | 47/47 (A498, NCI-H460, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.37×** | +11.1 | 3e-26 | 40/45 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **5.17×** | +10.0 | 2e-21 | 38/45 (SW480, A-427, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.02×** | +9.4 | 7e-19 | 41/47 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.65×** | +9.4 | 7e-19 | 44/48 (SW480, SW1417, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +8.3 | 7e-15 | 32/47 (HOP62, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.69×** | +7.0 | 2e-10 | 35/47 (KATO III, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +6.3 | 2e-08 | 30/48 (Hs 766T, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +6.1 | 5e-08 | 28/48 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.44×** | +5.4 | 3e-06 | 28/47 (A498, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.41×** | +5.4 | 4e-06 | 28/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **2.40×** | +5.3 | 4e-06 | 31/45 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.75×** | +5.3 | 4e-06 | 31/48 (NCI-H460, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.48×** | +5.2 | 7e-06 | 24/46 (H4, LoVo, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **2.31×** | +5.1 | 1e-05 | 23/47 (A498, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.68×** | +5.0 | 2e-05 | 27/46 (NCI-H460, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.67×** | +4.9 | 4e-05 | 26/44 (A-172, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12279.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.602×** | -6.6 | 3e-08 | 34/47 (MIA PaCa-2, C-33 A, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.715×** | -6.4 | 4e-08 | 28/47 (RKO, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.801×** | -4.2 | 0.006 | 21/48 (MIA PaCa-2, LoVo, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.739×** | -4.1 | 0.006 | 18/47 (RKO, SW48, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.785×** | -3.9 | 0.009 | 17/48 (LoVo, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.731×** | -3.9 | 0.009 | 18/48 (LoVo, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.758×** | -3.8 | 0.014 | 16/47 (MIA PaCa-2, SW480, …) | rises with dose | position effect removed |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.782×** | -3.3 | 0.058 | 13/47 (SNU-423, A549, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.811×** | -3.3 | 0.058 | 15/48 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.780×** | -3.2 | 0.068 | 15/35 (NCI-H23, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.792×** | -3.2 | 0.079 | 14/48 (PANC-1, SNU-423, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.797×** | -3.1 | 0.095 | 13/47 (RKO, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12279. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 36.0 | 0 | 3 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.639× (z -9.9) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 68.3 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -9.5) |
| [[RKO (line)]] | wt | 102 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -14.8) |
| [[AsPC-1 (line)]] | alt | 17.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.82× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 10.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +11.2) | — |
| [[Hs 766T (line)]] | wt | 18.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.97× (z +11.1) | — |
| [[HT-29 (line)]] | alt | 20.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.62× (z +9.7) | — |
| [[KATO III (line)]] | alt | 27.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +9.6) | — |
| [[LoVo (line)]] | wt | 20.6 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 3.52× (z +8.7) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 10.4 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.43× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 25.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.79× (z +10.9) | — |
| [[NCI-H460 (line)]] | wt | 33.3 | 2 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.81× (z +10.1) ⚠ unreliable plate only | — |
| [[SHP-77 (line)]] | alt | 29.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.37× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 53.4 | 1 | 1 | [[TAK-901 (drug)]] 0.05 µM 4.97× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -10.1) |
| [[A498 (line)]] | wt | 32.3 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.34× (z +10.2) ⚠ unreliable plate only | — |
| [[A549 (line)]] | wt | 27.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -10.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 38.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.60× (z +9.6) | — |
| [[CHP-212 (line)]] | wt | 24.7 | 0 | 1 | — | [[Clotrimazole (drug)]] 0.5 µM 0.0703× (z -9.2) |
| [[COLO 205 (line)]] | alt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 27.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -10.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 37.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.26× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 61.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -9.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 21.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.07× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 30.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.65× (z +8.8) ⚠ unreliable plate only | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.82× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[SNU-1 (line)]] | wt | 38.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 62.1 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.17× (z +10.0) ⚠ unreliable plate only | — |
| [[SW480 (line)]] | alt | 41.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.18× (z +10.2) | — |
| [[A-172 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12279), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG15]] | +0.81 | +0.80 / +0.79 | both halves | 7e-06 | same gene group |
| [[NLE1]] | +0.79 | +0.72 / +0.83 | both halves | 7e-06 |  |
| [[NOP16]] | +0.74 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.73 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[DDX31]] | +0.73 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[CLUH]] | +0.72 | +0.77 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[WDR43]] | +0.72 | +0.70 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[IMP4]] | +0.72 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[RRP1]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[PDCD11]] | +0.71 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[RIOK1]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[CTU1]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITM2B]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[PSENEN]] | -0.58 | -0.58 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises SNHG17's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[CENPV]] | B | CENPV activity raises SNHG17's level | lines that do not express CENPV (9) vs lines expressing it (41) | 1.46× lower at baseline in the lines without CENPV | 0.088 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TERT]] | B | TERT activity raises SNHG17's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.24× lower at baseline in the lines without TERT | 0.097 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.768). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.1, -41.0); signed map (-7.5, -51.3). **Vector** length 109, 32.1% of its response variance represented; |z| ≥ 3 in 1,113 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.51 to 8); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.55 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.55 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.2 | +12.7 |
|  | [[EX229 (drug)]] 5 µM |  | +4.4 | +5.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.0 | +5.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +5.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.5 | +5.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -6.0 | +4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | +2.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -4.8 | +5.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.6 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -1.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.2 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 17 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20q11.23 — chr20:38,419,638-38,435,409 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [388796](https://www.ncbi.nlm.nih.gov/gene/388796):

> Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:48600](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48600) · Entrez [388796](https://www.ncbi.nlm.nih.gov/gene/388796) · Ensembl [ENSG00000196756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196756)

## Data

Gene col 12279: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12279); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12279, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12279]; `tensor/DDL_lfc|DDL_z.npy` [12279]; `embed/gene_vectors.npy` [12279]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12279 or target_col == 12279). Every well: [[SNHG17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
