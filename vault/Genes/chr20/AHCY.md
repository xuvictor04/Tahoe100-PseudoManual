---
symbol: "AHCY"
type: "gene"
col: 2139
ensembl_id: "ENSG00000101444"
name: "adenosylhomocysteinase"
location: "20q11.22"
module: 18
arm: "+"
pooled_cpm: 49.08
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# AHCY

*adenosylhomocysteinase* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.43× (z +18.0, q 0e+00, up in 46 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.31× (z +5.5, q 3e-06, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.695× (z -5.3, q 6e-05, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEH1L]] (+0.70, fdr 7e-06), [[GLB1L2]] (+0.69, fdr 7e-06), [[IPO7]] (+0.68, fdr 7e-06); moves opposite to [[ZMYM5]] (-0.68, fdr 7e-06), [[SLC4A1AP]] (-0.68, fdr 7e-06), [[ASB8]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LAMC3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2139.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.43×** | +18.0 | 0e+00 | 46/46 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.15×** | +16.1 | 0e+00 | 40/41 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.27×** | +11.1 | 3e-26 | 40/45 (SW480, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.59×** | +6.8 | 2e-09 | 37/48 (Hs 766T, KATO III, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.53×** | +6.0 | 2e-07 | 31/47 (NCI-H460, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.48×** | +5.8 | 8e-07 | 33/47 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +5.5 | 3e-06 | 30/48 (HepG2/C3A, LoVo, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.45×** | +5.4 | 4e-06 | 34/48 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +5.4 | 5e-06 | 32/48 (NCI-H1792, Panc 03.27, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.44×** | +5.1 | 2e-05 | 30/48 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.40×** | +4.9 | 6e-05 | 29/47 (NCI-H460, KATO III, …) | rises with dose | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.74×** | +4.2 | 0.001 | 28/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.002 | 23/47 (C32, NCI-H23, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.34×** | +4.1 | 0.002 | 23/48 (SNU-423, LOX-IMVI, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.32×** | +4.0 | 0.002 | 24/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.57×** | +3.5 | 0.020 | 24/47 (NCI-H460, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.042 | 17/48 (NCI-H460, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.069 | 15/48 (HOP62, Panc 03.27, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.48×** | +3.0 | 0.080 | 18/47 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +2.9 | 0.086 | 14/48 (A549, HOP62, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.22×** | +2.9 | 0.099 | 16/47 (MIA PaCa-2, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2139.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.695×** | -5.3 | 6e-05 | 28/47 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.781×** | -5.1 | 1e-04 | 26/48 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.703×** | -4.9 | 1e-04 | 32/47 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.713×** | -4.7 | 3e-04 | 28/48 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.792×** | -3.4 | 0.079 | 23/48 (SW480, LS 180, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.778× | -3.3 | 0.10 | 22/48 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2139. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 74.8 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.64× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.331× (z -11.9) |
| [[Hs 766T (line)]] | wt | 44.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[KATO III (line)]] | alt | 59.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.92× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 88.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0430× (z -33.1) |
| [[A498 (line)]] | wt | 40.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[CFPAC-1 (line)]] | alt | 34.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HEC-1-A (line)]] | alt | 41.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.430× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 72.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.32× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.329× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 40.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 64.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.414× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 29.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.11× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[C-33 A (line)]] | alt | 64.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -12.5) |
| [[C32 (line)]] | wt | 22.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HOP62 (line)]] | alt | 28.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[J82 (line)]] | alt | 52.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LoVo (line)]] | wt | 47.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.78× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LOX-IMVI (line)]] | wt | 41.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 41.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2030 (line)]] | alt | 82.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[Panc 03.27 (line)]] | alt | 61.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 48.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[RKO (line)]] | wt | 60.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.248× (z -12.8) |
| [[SHP-77 (line)]] | alt | 38.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.94× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SNU-1 (line)]] | wt | 58.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -9.8) |
| [[SNU-423 (line)]] | alt | 41.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW 900 (line)]] | alt | 21.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.78× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 25.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A549 (line)]] | wt | 63.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HCT15 (line)]] | alt | 39.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.19× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HepG2_C3A (line)]] | wt | 76.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HS-578T (line)]] | alt | 25.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HT-29 (line)]] | alt | 51.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LS 180 (line)]] | wt | 49.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1573 (line)]] | alt | 47.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2347 (line)]] | alt | 36.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +10.8) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[NCI-H661 (line)]] | alt | 59.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 54.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW1417 (line)]] | alt | 89.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW48 (line)]] | wt | 71.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -12.6) |
| [[AN3 CA (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2139), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEH1L]] | +0.70 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[GLB1L2]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[IPO7]] | +0.68 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[PODXL2]] | +0.67 | +0.64 / +0.59 | both halves | 7e-06 | pathway: Biological oxidations |
| [[RPSA]] | +0.67 | +0.70 / +0.59 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives; STRING 585 |
| [[RPL3]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives; STRING 476 |
| [[MAT2A]] | +0.65 | +0.72 / +0.56 | both halves | 1e-05 | pathway: Biological oxidations; STRING 848 |
| [[ARHGAP4]] | +0.64 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[SMG1P3]] | +0.64 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[URB1]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[NUTF2]] | +0.63 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[SLC19A1]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM5]] | -0.68 | -0.69 / -0.58 | both halves | 7e-06 |  |
| [[SLC4A1AP]] | -0.68 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[ASB8]] | -0.65 | -0.69 / -0.64 | both halves | 7e-06 |  |
| [[ANKRD49]] | -0.65 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[FRG1]] | -0.64 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[WHAMM]] | -0.64 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[C3orf38]] | -0.64 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[TRAFD1]] | -0.64 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[ZNF44]] | -0.64 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[DCP1A]] | -0.62 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[CIR1]] | -0.62 | -0.62 / -0.58 | both halves | 8e-06 |  |
| [[ZNF226]] | -0.61 | -0.65 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMC3]] | B | LAMC3 activity raises AHCY's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.29× lower at baseline in the lines without LAMC3 | 0.047 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.602). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-28.6, -30.0); signed map (-21.5, -44.7). **Vector** length 92.5, 24.6% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.53 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +5.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +4.1 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +3.4 | +5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +5.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[Volasertib (drug)]] 0.5 µM |  | +2.1 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -5.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | adenosylhomocysteinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:34,280,268-34,311,802 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SAHH, AdoHcyase |
| Hallmark sets | XENOBIOTIC_METABOLISM, IL2_STAT5_SIGNALING |
| Reactome | 9 pathways, smallest: Metabolism of ingested SeMet, Sec, MeSec into H2Se; Methylation; Metabolic disorders of biological oxidation enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [P23526](https://www.uniprot.org/uniprotkb/P23526) (Adenosylhomocysteinase):

> Catalyzes the hydrolysis of S-adenosyl-L-homocysteine to form adenosine and homocysteine. Binds copper ions (By similarity).

**Summary**, from NCBI Gene [191](https://www.ncbi.nlm.nih.gov/gene/191):

> S-adenosylhomocysteine hydrolase belongs to the adenosylhomocysteinase family. It catalyzes the reversible hydrolysis of S-adenosylhomocysteine (AdoHcy) to adenosine (Ado) and L-homocysteine (Hcy). Thus, it regulates the intracellular S-adenosylhomocysteine (SAH) concentration thought to be important for transmethylation reactions. Deficiency in this protein is one of the different causes of hypermethioninemia. Alternatively spliced transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:343](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:343) · Entrez [191](https://www.ncbi.nlm.nih.gov/gene/191) · UniProt [P23526](https://www.uniprot.org/uniprotkb/P23526) · Ensembl [ENSG00000101444](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101444)

## Data

Gene col 2139: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2139); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2139, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2139]; `tensor/DDL_lfc|DDL_z.npy` [2139]; `embed/gene_vectors.npy` [2139]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2139 or target_col == 2139). Every well: [[AHCY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AHCY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
