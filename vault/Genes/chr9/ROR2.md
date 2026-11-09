---
symbol: "ROR2"
type: "gene"
col: 9747
ensembl_id: "ENSG00000169071"
name: "ROR family WNT receptor 2"
location: "9q22.31"
module: 115
arm: "+"
pooled_cpm: 20.08
n_lines_expressing: 25
n_dd_up: 36
n_dd_down: 3
n_dd_up_clean: 26
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 3
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# ROR2

*ROR family WNT receptor 2* — 9q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.61× (z +23.7, q 0e+00, up in 11 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.744× (z -5.2, q 1e-04, down in 12 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (PANC-1 0.219×, J82 0.272×, HOP62 0.197×, Panc 03.27 0.330×, …); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SNU-423 0.0775×, J82 0.161×, SW480 0.198×, NCI-H23 0.154×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-423 0.0795×, Panc 03.27 0.105×, PANC-1 0.158×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-423 0.222×, SW480 0.367×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-423 0.379×, J82 0.529×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENTREP2]] (+0.58, fdr 1e-05), [[KCNG3]] (+0.55, fdr 1e-05), [[TSPAN33]] (+0.53, fdr 2e-05); moves opposite to [[EDEM3]] (-0.46, fdr 4e-05), [[ESM1]] (-0.46, fdr 1e-04), [[SERPIND1]] (-0.43, fdr 2e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[C14orf132]] → it (grade B ⚠); 3 go from it, the strongest it → [[CDON]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9747.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +23.7 | 0e+00 | 11/21 (A549, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.54×** | +23.0 | 0e+00 | 17/23 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.20×** | +13.8 | 5e-41 | 3/20 (A-172, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.16×** | +13.5 | 4e-39 | 17/22 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +10.5 | 9e-24 | 17/22 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +10.4 | 2e-23 | 1/16 (NCI-H460) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +10.0 | 8e-22 | 7/22 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +9.2 | 3e-18 | 7/22 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +9.1 | 8e-18 | 2/21 (HCT15, NCI-H460) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +8.3 | 6e-15 | 2/11 (NCI-H460, SHP-77) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +7.9 | 1e-13 | 8/22 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +7.3 | 1e-11 | 6/22 (A-172, HOP62, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.93×** | +6.0 | 9e-08 | 10/23 (NCI-H1573, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.59×** | +5.8 | 3e-07 | 1/19 (NCI-H1573) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +5.6 | 7e-07 | 3/22 (A549, LS 180, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.49×** | +5.0 | 2e-05 | 4/22 (SW480, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +4.7 | 1e-04 | 11/22 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.29×** | +4.4 | 3e-04 | 3/22 (C-33 A, Panc 03.27, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9747.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (PANC-1 0.219×, J82 0.272×, HOP62 0.197×, Panc 03.27 0.330×, …); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SNU-423 0.0775×, J82 0.161×, SW480 0.198×, NCI-H23 0.154×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-423 0.0795×, Panc 03.27 0.105×, PANC-1 0.158×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-423 0.222×, SW480 0.367×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-423 0.379×, J82 0.529×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.744×** | -5.2 | 1e-04 | 12/22 (NCI-H1573, HOP62, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.775×** | -4.5 | 0.002 | 10/22 (LoVo, SHP-77, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.785×** | -4.3 | 0.004 | 8/22 (A549, A-172, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.826× | -3.4 | 0.11 | 4/22 (Panc 03.27, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.832× | -3.1 | 0.20 | 11/21 (HOP62, LoVo, …) | two highest doses | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | 0.834× | -3.1 | 0.20 | 2/22 (LoVo, C-33 A) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.954× | -3.0 | 0.20 | 2/23 (NCI-H661, HCT15) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9747. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.46 | 9 (2 ⚠) | 0 | [[Trametinib (drug)]] 0.05 µM 8.70× (z +12.8) | — |
| [[J82 (line)]] | alt | 110 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -18.0) |
| [[SNU-423 (line)]] | alt | 85.9 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0795× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -10.8) |
| [[LoVo (line)]] | wt | 42.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -12.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 45.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -18.0) |
| [[A-427 (line)]] | wt | 46.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 42.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Pralsetinib (drug)]] 5 µM 0.0379× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 47.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.330× (z -12.9) |
| [[SW480 (line)]] | alt | 32.0 | 0 | 3 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.210× (z -14.0) ⚠ transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -8.7) |
| [[A549 (line)]] | wt | 10.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 27.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -14.7) |
| [[LS 180 (line)]] | wt | 12.8 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.10× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 140 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0198× (z -35.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 6.19 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0726× (z -9.0) ⚠ cell-cycle shift, explains ~80% of this change |
| [[SW48 (line)]] | wt | 28.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -9.0) |
| [[A-172 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.94 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.94 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.77 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.68 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9747), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENTREP2]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[KCNG3]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[TSPAN33]] | +0.53 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[REEP1]] | +0.52 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[SNAP91]] | +0.52 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[HES2]] | +0.51 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[CELF4]] | +0.51 | +0.38 / +0.54 | both halves | 7e-05 |  |
| [[APBA1]] | +0.51 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[EPB41L4A]] | +0.50 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[GRID1]] | +0.50 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[MIAT]] | +0.50 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[PDE5A]] | +0.49 | +0.48 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDEM3]] | -0.46 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[ESM1]] | -0.46 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[SERPIND1]] | -0.43 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[BMS1P4-1]] | -0.42 | -0.42 / -0.29 | both halves | 2e-04 |  |
| [[MIRLET7IHG]] | -0.42 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[SLC30A9]] | -0.41 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[RC3H2]] | -0.41 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[LINC01257]] | -0.41 | -0.49 / -0.15 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C14orf132]] | B | C14orf132 activity raises ROR2's level | lines that do not express C14orf132 (19) vs lines expressing it (31) | 2.49× lower at baseline in the lines without C14orf132 | 0.037 | ⚠ within organs, on part of the lines; also absent: SLC22A17, ZFP28, ADAMTS7 |
| [[SERPIND1]] | B | SERPIND1 activity lowers ROR2's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 2.20× higher at baseline in the lines without SERPIND1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[KCNK13]] | B | KCNK13 activity raises ROR2's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 2.84× lower at baseline in the lines without KCNK13 | 0.063 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[ENTREP2]] | C | ENTREP2 activity raises ROR2's level | lines that do not express ENTREP2 (22) vs lines expressing it (28) | 3.03× lower at baseline in the lines without ENTREP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: TBX1, JPH3, MAPK4; maybe low, not absent; co-absent with the target |
| [[CELF4]] | C | CELF4 activity raises ROR2's level | lines that do not express CELF4 (24) vs lines expressing it (26) | 1.97× lower at baseline in the lines without CELF4 | 0.071 | ⚠ within organs, on part of the lines; also absent: CHST8, ASXL3, SULT4A1; maybe low, not absent; co-absent with the target |
| [[JAKMIP2]] | C | JAKMIP2 activity raises ROR2's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 1.78× lower at baseline in the lines without JAKMIP2 | 0.089 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDON]] | B | ROR2 activity raises CDON's level | lines that do not express ROR2 (25) vs lines expressing it (25) | 1.51× lower at baseline in the lines without ROR2 | 0.069 | ⚠ within organs, on part of the lines; also absent: BEGAIN, OLFM1, HOXD11 |
| [[GLS2]] | B | ROR2 activity raises GLS2's level | lines that do not express ROR2 (25) vs lines expressing it (25) | 1.54× lower at baseline in the lines without ROR2 | 0.071 | ⚠ within organs, on part of the lines; also absent: BEGAIN, OLFM1, HOXD11 |
| [[RETREG1]] | B | ROR2 activity raises RETREG1's level | lines that do not express ROR2 (25) vs lines expressing it (25) | 1.83× lower at baseline in the lines without ROR2 | 0.099 | ⚠ within organs, on part of the lines; also absent: BEGAIN, OLFM1, HOXD11 |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.1, 36.3); signed map (28.6, 23.9). **Vector** length 58.7, 13.1% of its response variance represented; |z| ≥ 3 in 638 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +23.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +13.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +23.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +8.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.0 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +7.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +6.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -2.5 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -5.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.0 | -4.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.1 | -2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ROR family WNT receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.31 — chr9:91,563,091-91,950,228 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously NTRKR2, BDB, BDB1 |
| Gene groups (HGNC) | I-set domain containing; Pseudokinases; Kringle domain containing; ROR family WNT receptors |
| Reactome | 4 pathways, smallest: WNT5A-dependent internalization of FZD2, FZD5 and ROR2; PCP/CE pathway; Beta-catenin independent WNT signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01974](https://www.uniprot.org/uniprotkb/Q01974) (Tyrosine-protein kinase transmembrane receptor ROR2):

> Tyrosine-protein kinase receptor which may be involved in the early formation of the chondrocytes. It seems to be required for cartilage and growth plate development (By similarity). Phosphorylates YWHAB, leading to induction of osteogenesis and bone formation. In contrast, has also been shown to have very little tyrosine kinase activity in vitro. May act as a receptor for wnt ligand WNT5A which may result in the inhibition of WNT3A-mediated signaling.

**Summary**, from NCBI Gene [4920](https://www.ncbi.nlm.nih.gov/gene/4920):

> The protein encoded by this gene is a receptor protein tyrosine kinase and type I transmembrane protein that belongs to the ROR subfamily of cell surface receptors. The protein may be involved in the early formation of the chondrocytes and may be required for cartilage and growth plate development. Mutations in this gene can cause brachydactyly type B, a skeletal disorder characterized by hypoplasia/aplasia of distal phalanges and nails. In addition, mutations in this gene can cause the …

**Accessions** — [HGNC:10257](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10257) · Entrez [4920](https://www.ncbi.nlm.nih.gov/gene/4920) · UniProt [Q01974](https://www.uniprot.org/uniprotkb/Q01974) · Ensembl [ENSG00000169071](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169071)

## Data

Gene col 9747: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9747); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9747, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9747]; `tensor/DDL_lfc|DDL_z.npy` [9747]; `embed/gene_vectors.npy` [9747]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9747 or target_col == 9747). Every well: [[ROR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ROR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
