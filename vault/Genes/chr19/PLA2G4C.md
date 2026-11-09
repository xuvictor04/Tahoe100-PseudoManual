---
symbol: "PLA2G4C"
type: "gene"
col: 2612
ensembl_id: "ENSG00000105499"
name: "phospholipase A2 group IVC"
location: "19q13.33"
module: 68
arm: "+"
pooled_cpm: 16.92
n_lines_expressing: 48
n_dd_up: 45
n_dd_down: 24
n_dd_up_clean: 32
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# PLA2G4C

*phospholipase A2 group IVC* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 17.0× (z +61.3, q 0e+00, up in 45 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.527× (z -9.8, q 6e-20, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00944]] (+0.79, fdr 7e-06), [[HDAC9]] (+0.77, fdr 7e-06), [[RIPK2-DT]] (+0.71, fdr 7e-06); moves opposite to [[TAF5L]] (-0.73, fdr 7e-06), [[WASF3]] (-0.67, fdr 6e-05), [[SKP2]] (-0.67, fdr 2e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2612.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **17.0×** | +61.3 | 0e+00 | 45/45 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **8.43×** | +32.6 | 0e+00 | 43/44 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **9.03×** | +32.4 | 0e+00 | 44/45 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +14.3 | 3e-44 | 33/43 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.50×** | +14.0 | 2e-42 | 34/46 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.26×** | +12.4 | 1e-33 | 34/45 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.70×** | +11.5 | 8e-29 | 30/46 (J82, SW1417, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +11.2 | 2e-27 | 26/44 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.97×** | +10.4 | 2e-23 | 29/45 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +9.7 | 1e-20 | 29/46 (MIA PaCa-2, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +9.1 | 6e-18 | 12/25 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +9.0 | 2e-17 | 28/38 (J82, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.69×** | +8.0 | 4e-14 | 28/45 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.38×** | +7.0 | 8e-11 | 23/46 (SW 900, SW1417, …) | all doses, flat | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +7.0 | 9e-11 | 24/45 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +6.6 | 1e-09 | 23/45 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.4 | 5e-09 | 18/43 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.50×** | +6.2 | 1e-08 | 23/46 (HEC-1-A, SW1417, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +6.0 | 4e-08 | 19/44 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2612.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.527×** | -9.8 | 6e-20 | 29/45 (SNU-423, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.571×** | -8.6 | 2e-15 | 26/43 (SK-MEL-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.645×** | -6.4 | 2e-08 | 22/45 (SNU-423, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.670×** | -6.1 | 1e-07 | 22/45 (SNU-423, LOX-IMVI, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **0.476×** | -5.9 | 3e-07 | 19/42 (NCI-H460, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.684×** | -5.8 | 6e-07 | 18/45 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.685×** | -5.8 | 6e-07 | 20/45 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.691×** | -5.7 | 1e-06 | 21/45 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.701×** | -5.4 | 3e-06 | 17/45 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.702×** | -5.4 | 3e-06 | 20/46 (SNU-423, RPMI-7951, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -5.2 | 9e-06 | 15/45 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.726×** | -4.9 | 4e-05 | 14/44 (Panc 03.27, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.736×** | -4.7 | 1e-04 | 20/45 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.747×** | -4.5 | 3e-04 | 19/46 (SNU-423, RPMI-7951, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.750×** | -4.4 | 4e-04 | 15/45 (SNU-423, NCI-H460, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.745×** | -4.2 | 0.001 | 17/43 (SW 900, SHP-77, …) | all doses, stronger at high dose |  |
| [[Econazole (drug)]] 5 µM |  | **0.769×** | -4.0 | 0.002 | 10/45 (H4, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2612. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 27.7 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 26.0× (z +30.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 33.3 | 3 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +27.1) | [[Dinaciclib (drug)]] 0.05 µM 0.0449× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 13.1 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 31.7× (z +31.6) | — |
| [[SNU-423 (line)]] | alt | 67.4 | 2 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.13× (z +22.6) | [[Belinostat (drug)]] 5 µM 0.211× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 65.6 | 4 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +17.1) | [[Ixazomib citrate (drug)]] 5 µM 0.214× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.262× (z -10.2) |
| [[SNU-1 (line)]] | wt | 69.6 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +21.0) | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -12.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 14.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 32.0× (z +17.6) | — |
| [[A-172 (line)]] | wt | 16.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.1× (z +28.7) | — |
| [[HOP62 (line)]] | alt | 18.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 28.3× (z +29.5) | — |
| [[hTERT-HPNE (line)]] | wt | 18.1 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 20.8× (z +19.8) | [[Belinostat (drug)]] 5 µM 0.125× (z -9.6) |
| [[PANC-1 (line)]] | alt | 13.1 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +23.4) | [[Bortezomib (drug)]] 5 µM 0.0654× (z -10.2) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +18.4) | [[Belinostat (drug)]] 0.5 µM 0.115× (z -12.2) |
| [[SW 900 (line)]] | alt | 15.2 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +20.0) | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.114× (z -10.0) |
| [[A549 (line)]] | wt | 18.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +21.7) | — |
| [[AsPC-1 (line)]] | alt | 8.76 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +15.5) | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0959× (z -8.7) |
| [[C32 (line)]] | wt | 7.49 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.1× (z +16.3) | — |
| [[HEC-1-A (line)]] | alt | 24.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.3× (z +25.8) | — |
| [[HepG2_C3A (line)]] | wt | 15.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 32.7× (z +18.1) | — |
| [[HS-578T (line)]] | alt | 17.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.8× (z +22.1) | — |
| [[HT-29 (line)]] | alt | 9.59 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 65.8× (z +23.8) | — |
| [[NCI-H1573 (line)]] | alt | 8.69 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.8× (z +22.1) | — |
| [[NCI-H2347 (line)]] | alt | 9.22 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.0× (z +23.3) | — |
| [[Panc 03.27 (line)]] | alt | 19.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +20.7) | — |
| [[SW1417 (line)]] | alt | 13.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +19.5) | — |
| [[A498 (line)]] | wt | 35.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +21.6) | — |
| [[LoVo (line)]] | wt | 7.07 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.4× (z +21.8) | — |
| [[LOX-IMVI (line)]] | wt | 21.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +26.0) | — |
| [[RKO (line)]] | wt | 7.70 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 25.5× (z +10.9) | — |
| [[SW480 (line)]] | alt | 5.24 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.5× (z +22.4) | — |
| [[A-427 (line)]] | wt | 9.23 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 15.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +22.5) | — |
| [[COLO 205 (line)]] | alt | 10.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 56.5× (z +20.9) | — |
| [[H4 (line)]] | wt | 35.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.03× (z +14.1) | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -8.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 8.79 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.5× (z +21.1) | — |
| [[NCI-H1792 (line)]] | alt | 9.91 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.05× (z +9.5) | [[Belinostat (drug)]] 0.5 µM 0.143× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 17.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.4× (z +23.1) | — |
| [[HCT15 (line)]] | alt | 16.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +13.6) | — |
| [[NCI-H23 (line)]] | alt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.48× (z +16.0) | — |
| [[SHP-77 (line)]] | alt | 5.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.89× (z +9.9) | — |
| [[SW 1271 (line)]] | alt | 31.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.5× (z +9.6) | — |
| [[SW48 (line)]] | wt | 6.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.1× (z +11.6) | — |
| [[AN3 CA (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2612), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00944]] | +0.79 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[HDAC9]] | +0.77 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[RIPK2-DT]] | +0.71 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[APLF]] | +0.71 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[PATL2]] | +0.71 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[NPHS1]] | +0.70 | +0.74 / +0.57 | both halves | 8e-06 |  |
| [[PPP1R12A-AS2]] | +0.70 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[SLC9A8]] | +0.70 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[NFKBIB]] | +0.69 | +0.75 / +0.57 | both halves | 1e-05 |  |
| [[SOCS2-AS1]] | +0.69 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[HHLA3]] | +0.69 | +0.68 / +0.40 | both halves | 4e-05 |  |
| [[ZNF341-AS1]] | +0.69 | +0.60 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF5L]] | -0.73 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[WASF3]] | -0.67 | -0.66 / -0.38 | both halves | 6e-05 |  |
| [[SKP2]] | -0.67 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[GRB2]] | -0.66 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[ATRN]] | -0.65 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[CCNY]] | -0.64 | -0.71 / -0.39 | both halves | 6e-05 |  |
| [[ELP1]] | -0.63 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[PHKA2]] | -0.63 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[SLC35A3]] | -0.62 | -0.64 / -0.37 | both halves | 8e-05 |  |
| [[SAP130]] | -0.62 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[RNF4]] | -0.62 | -0.71 / -0.61 | both halves | 7e-06 |  |
| [[FAR1]] | -0.61 | -0.67 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PLA2G4C's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.6% of all compounds | 0.011 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TRIML2]] | B | TRIML2 activity raises PLA2G4C's level | lines that do not express TRIML2 (30) vs lines expressing it (20) | 1.72× lower at baseline in the lines without TRIML2 | 0.023 | ⚠ within organs, on part of the lines; also absent: ZNF471, LINC01010, ENSG00000222032 |
| [[APH1B]] | B | APH1B activity raises PLA2G4C's level | lines that do not express APH1B (6) vs lines expressing it (44) | 1.84× lower at baseline in the lines without APH1B | 0.031 | ⚠ within organs, on part of the lines; also absent: PER3, DLG4, CCDC3 |
| [[MYPN]] | B | MYPN activity raises PLA2G4C's level | lines that do not express MYPN (29) vs lines expressing it (21) | 1.37× lower at baseline in the lines without MYPN | 0.038 | ⚠ within organs, on part of the lines; also absent: COL4A6, EPGN, FLRT2 |
| [[NR3C1]] | B | NR3C1 activity lowers PLA2G4C's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[IL23A]] | B | IL23A activity raises PLA2G4C's level | lines that do not express IL23A (6) vs lines expressing it (44) | 1.48× lower at baseline in the lines without IL23A | 0.068 | ⚠ within organs, on part of the lines; also absent: MYRF; maybe low, not absent |
| [[JAM2]] | B | JAM2 activity raises PLA2G4C's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 1.69× lower at baseline in the lines without JAM2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[LINC00504]] | B | LINC00504 activity raises PLA2G4C's level | lines that do not express LINC00504 (31) vs lines expressing it (19) | 1.58× lower at baseline in the lines without LINC00504 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC02930, ENSG00000287474 |
| [[FMNL1-DT]] | B | FMNL1-DT activity raises PLA2G4C's level | lines that do not express FMNL1-DT (23) vs lines expressing it (27) | 1.41× lower at baseline in the lines without FMNL1-DT | 0.099 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.802). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (17.4, 9.7); signed map (26.5, 7.6). **Vector** length 124, 34.4% of its response variance represented; |z| ≥ 3 in 1,424 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.2 | +61.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.4 | +32.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.1 | +32.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +9.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.7 | +12.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.4 | +11.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +9.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.8 | +5.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -7.6 | -8.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.5 | -9.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -5.5 | -3.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -5.1 | -3.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | -4.6 | -4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.5 | -3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.1 | -5.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -4.0 | -5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.7 | -2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.2 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase A2 group IVC |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,047,843-48,110,817 (-) |
| Ensembl biotype | protein_coding |
| Also known as | cPLA2-gamma |
| Gene groups (HGNC) | Phospholipases |
| Reactome | 7 pathways, smallest: Hydrolysis of LPC; Acyl chain remodelling of PI; Acyl chain remodelling of PC |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UP65](https://www.uniprot.org/uniprotkb/Q9UP65) (Cytosolic phospholipase A2 gamma):

> Calcium-independent phospholipase, lysophospholipase and O-acyltransferase involved in phospholipid remodeling with implications in endoplasmic reticulum membrane homeostasis and lipid droplet biogenesis. Preferentially hydrolyzes the ester bond of the fatty acyl group attached at the sn-2 position of phospholipids with choline and ethanolamine head groups, producing lysophospholipids that are used in deacylation-reacylation cycles. Transfers the sn-1 fatty acyl from one lysophospholipid …

**Summary**, from NCBI Gene [8605](https://www.ncbi.nlm.nih.gov/gene/8605):

> This gene encodes a protein which is a member of the phospholipase A2 enzyme family which hydrolyzes glycerophospholipids to produce free fatty acids and lysophospholipids, both of which serve as precursors in the production of signaling molecules. The encoded protein has been shown to be a calcium-independent and membrane bound enzyme. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:9037](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9037) · Entrez [8605](https://www.ncbi.nlm.nih.gov/gene/8605) · UniProt [Q9UP65](https://www.uniprot.org/uniprotkb/Q9UP65) · Ensembl [ENSG00000105499](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105499)

## Data

Gene col 2612: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2612); `tables/drug_effects.parquet` (78 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2612, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2612]; `tensor/DDL_lfc|DDL_z.npy` [2612]; `embed/gene_vectors.npy` [2612]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2612 or target_col == 2612). Every well: [[PLA2G4C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLA2G4C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
