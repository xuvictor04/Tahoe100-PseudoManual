---
symbol: "NPRL3"
type: "gene"
col: 2324
ensembl_id: "ENSG00000103148"
name: "NPR3 like, GATOR1 complex subunit"
location: "16p13.3"
module: 18
arm: "+"
pooled_cpm: 34.39
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 25
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# NPRL3

*NPR3 like, GATOR1 complex subunit* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM: 1.31× (z +6.0, q 1e-06, up in 23 of 48 measured lines) ⚠ cell-cycle shift, explains ~20% of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 1.13× (z +3.9, q 0.013, up in 9 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (19 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.446× (z -17.1, q 0e+00, down in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.587× (z -16.6, q 0e+00, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SFXN4]] (+0.64, fdr 7e-06), [[ZNF133]] (+0.63, fdr 7e-06), [[EARS2]] (+0.63, fdr 7e-06); moves opposite to [[YWHAZ]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NT5M]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2324.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.31×** | +6.0 | 1e-06 | 23/48 (SW480, PANC-1, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +5.2 | 6e-05 | 16/48 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.21×** | +3.9 | 0.013 | 9/48 (Hs 766T, SW480, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.9 | 0.013 | 9/48 (A-172, A498, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.13× | +3.8 | 0.017 | 9/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.029 | 15/48 (CFPAC-1, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.17× | +3.5 | 0.040 | 13/48 (HS-578T, AsPC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.17× | +3.5 | 0.040 | 13/48 (HS-578T, NCI-H1792, …) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.17× | +3.3 | 0.060 | 8/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.097 | 9/47 (NCI-H460, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.11 | 11/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.11 | 11/48 (CFPAC-1, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 21 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2324.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.446×** | -17.1 | 0e+00 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.587×** | -16.6 | 0e+00 | 39/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.623×** | -14.7 | 0e+00 | 33/47 (HEC-1-A, A498, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.581×** | -11.9 | 1e-30 | 41/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.597×** | -11.3 | 1e-27 | 37/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.618×** | -10.6 | 4e-24 | 34/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.661×** | -9.1 | 7e-18 | 28/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.705×** | -7.7 | 1e-12 | 30/48 (A-172, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.711×** | -7.5 | 4e-12 | 28/48 (NCI-H460, SW480, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.707×** | -7.0 | 1e-10 | 24/43 (H4, C-33 A, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.533×** | -7.0 | 1e-10 | 32/48 (SW 900, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.737×** | -6.7 | 1e-09 | 29/48 (LS 180, MIA PaCa-2, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **0.739×** | -6.6 | 1e-09 | 24/46 (SW 900, HOP62, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.740×** | -6.6 | 2e-09 | 26/47 (HEC-1-A, SNU-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.736×** | -6.5 | 4e-09 | 25/48 (C32, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.772×** | -5.7 | 4e-07 | 22/48 (J82, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.839× | -5.4 | 2e-06 | 22/48 (SNU-423, NCI-H460, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.683×** | -4.3 | 5e-04 | 17/47 (NCI-H1573, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.727×** | -3.6 | 0.008 | 13/48 (C-33 A, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (drug)]] 5 µM |  | 0.902× | -3.2 | 0.028 | 8/49 (A-427, CHP-212, …) | inconsistent across doses |  |
| [[Hexylresorcinol (drug)]] 0.5 µM |  | 0.876× | -2.9 | 0.072 | 10/48 (KATO III, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2324. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 38.2 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -14.7) |
| [[PANC-1 (line)]] | alt | 60.8 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -11.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[C32 (line)]] | wt | 42.3 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -15.5) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -10.5) |
| [[HOP62 (line)]] | alt | 34.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -12.3) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -8.7) |
| [[J82 (line)]] | alt | 29.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -12.4) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -8.8) |
| [[SW480 (line)]] | alt | 40.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -13.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -11.0) |
| [[A-172 (line)]] | wt | 44.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -12.0) |
| [[A549 (line)]] | wt | 29.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -14.1) ⚠ cell-cycle shift, explains ~50% of this change |
| [[AsPC-1 (line)]] | alt | 29.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -14.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[C-33 A (line)]] | alt | 60.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -10.2) |
| [[H4 (line)]] | wt | 39.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[HEC-1-A (line)]] | alt | 33.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -17.1) ⚠ cell-cycle shift, explains ~50% of this change |
| [[LS 180 (line)]] | wt | 44.0 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.403× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 31.7 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.330× (z -9.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SNU-1 (line)]] | wt | 42.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -10.7) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -10.0) |
| [[SNU-423 (line)]] | alt | 32.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.126× (z -15.7) ⚠ toxic; cell-cycle shift, explains ~52% of this change |
| [[SW 900 (line)]] | alt | 28.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -13.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A498 (line)]] | wt | 23.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -16.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[BT-474 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -10.4) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HCT15 (line)]] | alt | 52.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 30.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -10.4) ⚠ cell-cycle shift, explains ~50% of this change |
| [[KATO III (line)]] | alt | 38.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.346× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 33.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 37.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -10.4) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H1792 (line)]] | alt | 37.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -9.8) |
| [[RKO (line)]] | wt | 34.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -8.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW1417 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -15.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SW48 (line)]] | wt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2324), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFXN4]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ZNF133]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[EARS2]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[ADSL]] | +0.60 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[DDX31]] | +0.60 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[TIMM9]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[PDCD11]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[RABEPK]] | +0.59 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[MRPS5]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[RILPL1]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[MECR]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ANAPC1]] | +0.58 | +0.55 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAZ]] | -0.54 | -0.54 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity raises NPRL3's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.38× lower at baseline in the lines without NT5M | 0.028 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.546). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.7, -31.2); signed map (-13.7, -56.4). **Vector** length 86.3, 19.1% of its response variance represented; |z| ≥ 3 in 1,074 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.2 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | -0.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.7 | +1.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.4 | +0.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -16.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | -4.8 | -7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.1 | -4.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -4.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.9 | -2.1 |
|  | [[Berbamine (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | NPR3 like, GATOR1 complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:84,271-138,677 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGTHBA, RMD11, NPR3, MARE, HS-40; previously C16orf35 |
| Gene groups (HGNC) | GATOR1 subcomplex |
| Reactome | 4 pathways, smallest: Amino acids regulate mTORC1; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12980](https://www.uniprot.org/uniprotkb/Q12980) (GATOR1 complex protein NPRL3):

> As a component of the GATOR1 complex functions as an inhibitor of the amino acid-sensing branch of the mTORC1 pathway. In response to amino acid depletion, the GATOR1 complex has GTPase activating protein (GAP) activity and strongly increases GTP hydrolysis by RagA/RRAGA (or RagB/RRAGB) within heterodimeric Rag complexes, thereby turning them into their inactive GDP-bound form, releasing mTORC1 from lysosomal surface and inhibiting mTORC1 signaling. In the presence of abundant amino acids, the …

**Summary**, from NCBI Gene [8131](https://www.ncbi.nlm.nih.gov/gene/8131):

> Predicted to enable GTPase activator activity. Involved in cellular response to amino acid starvation and negative regulation of TORC1 signaling. Part of GATOR1 complex. Is active in lysosomal membrane. Implicated in familial focal epilepsy with variable foci 3. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14124](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14124) · Entrez [8131](https://www.ncbi.nlm.nih.gov/gene/8131) · UniProt [Q12980](https://www.uniprot.org/uniprotkb/Q12980) · Ensembl [ENSG00000103148](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103148)

## Data

Gene col 2324: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2324); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2324, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2324]; `tensor/DDL_lfc|DDL_z.npy` [2324]; `embed/gene_vectors.npy` [2324]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2324 or target_col == 2324). Every well: [[NPRL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPRL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
