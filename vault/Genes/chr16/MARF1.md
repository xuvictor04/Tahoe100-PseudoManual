---
symbol: "MARF1"
type: "gene"
col: 9355
ensembl_id: "ENSG00000166783"
name: "meiosis regulator and mRNA stability factor 1"
location: "16p13.11"
module: 76
arm: "+"
pooled_cpm: 105.1
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 27
n_dd_up_clean: 4
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# MARF1

*meiosis regulator and mRNA stability factor 1* — 16p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.40× (z +7.1, q 6e-10, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.539× (z -18.5, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTMR14]] (+0.74, fdr 7e-06), [[CCDC28A]] (+0.74, fdr 7e-06), [[LINC01881]] (+0.66, fdr 1e-05); moves opposite to [[ANKRD18A]] (-0.62, fdr 3e-05), [[SNHG26]] (-0.58, fdr 3e-05), [[KIF21A]] (-0.58, fdr 2e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9355.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +7.1 | 6e-10 | 32/48 (SW480, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.80×** | +6.3 | 7e-08 | 39/49 (A498, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.26×** | +4.9 | 2e-04 | 26/48 (SW480, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **1.26×** | +4.8 | 2e-04 | 30/48 (SNU-1, HEC-1-A, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.17× | +4.7 | 3e-04 | 17/48 (SNU-1, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.017 | 21/48 (SW480, RKO, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.12× | +3.4 | 0.062 | 4/48 (H4, RPMI-7951, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9355.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.539×** | -18.5 | 0e+00 | 44/48 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.418×** | -18.4 | 0e+00 | 48/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.498×** | -14.7 | 0e+00 | 41/48 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.481×** | -14.3 | 3e-44 | 41/45 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.567×** | -12.0 | 5e-31 | 42/49 (A549, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.345×** | -11.5 | 2e-28 | 45/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.589×** | -10.7 | 5e-25 | 46/48 (AsPC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.381×** | -10.4 | 2e-23 | 45/48 (NCI-H1792, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.616×** | -9.8 | 5e-21 | 34/44 (NCI-H2030, A-427, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.410×** | -9.6 | 4e-20 | 43/48 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.430×** | -9.1 | 5e-18 | 47/48 (AsPC-1, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.474×** | -8.0 | 4e-14 | 41/48 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.683×** | -8.0 | 4e-14 | 39/48 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.743×** | -6.3 | 1e-08 | 34/48 (HOP62, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.748×** | -5.9 | 1e-07 | 28/47 (HepG2/C3A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.651×** | -5.5 | 1e-06 | 34/48 (SW 900, SW1417, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.658×** | -5.4 | 3e-06 | 37/49 (A498, LOX-IMVI, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.789×** | -5.0 | 2e-05 | 30/49 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.791×** | -5.0 | 2e-05 | 28/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.791×** | -4.7 | 8e-05 | 27/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9355. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 108 | 0 | 12 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.221× (z -19.6) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.458× (z -14.3) |
| [[SW480 (line)]] | alt | 79.5 | 3 (1 ⚠) | 8 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.49× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 119 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -22.3) |
| [[AsPC-1 (line)]] | alt | 120 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -25.9) |
| [[HOP62 (line)]] | alt | 75.4 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -17.6) |
| [[NCI-H2347 (line)]] | alt | 71.1 | 0 | 7 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.396× (z -11.9) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.431× (z -10.8) |
| [[PANC-1 (line)]] | alt | 192 | 1 (1 ⚠) | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +12.4) ⚠ cell-cycle shift, explains ~66% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.359× (z -14.5) |
| [[MIA PaCa-2 (line)]] | alt | 107 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -16.0) |
| [[NCI-H23 (line)]] | alt | 115 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.430× (z -15.5) |
| [[SW 900 (line)]] | alt | 118 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -21.7) |
| [[A-427 (line)]] | wt | 99.9 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0742× (z -28.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.418× (z -14.4) |
| [[A549 (line)]] | wt | 134 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[TAK-733 (drug)]] 5 µM 0.248× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 172 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.124× (z -17.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.324× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 111 | 0 | 5 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.336× (z -14.1) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.501× (z -12.7) |
| [[NCI-H2030 (line)]] | alt | 132 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.434× (z -10.1) |
| [[SNU-423 (line)]] | alt | 104 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -18.9) |
| [[A498 (line)]] | wt | 91.8 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.89× (z +8.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.375× (z -13.5) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.232× (z -10.3) |
| [[C32 (line)]] | wt | 92.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.260× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 218 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.377× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 81.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -11.6) |
| [[H4 (line)]] | wt | 66.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -15.9) |
| [[Hs 766T (line)]] | wt | 119 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.254× (z -15.3) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.546× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 86.3 | 0 | 3 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0730× (z -12.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.397× (z -12.1) |
| [[J82 (line)]] | alt | 86.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -13.1) |
| [[LoVo (line)]] | wt | 79.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.366× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 99.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.395× (z -9.9) |
| [[SNU-1 (line)]] | wt | 137 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -11.3) |
| [[AN3 CA (line)]] | alt | 124 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Canagliflozin (drug)]] 0.05 µM 0.235× (z -9.3) |
| [[HCT15 (line)]] | alt | 115 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.333× (z -9.3) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.140× (z -8.5) |
| [[HT-29 (line)]] | alt | 80.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.360× (z -10.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -14.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 72.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.333× (z -10.8) |
| [[SW 1088 (line)]] | alt | 113 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -9.7) |
| [[SW1417 (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.328× (z -14.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.575× (z -10.2) |
| [[A-172 (line)]] | wt | 99.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.457× (z -10.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 78.9 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.164× (z -8.8) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -9.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 79.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.342× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 69.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.346× (z -13.5) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.356× (z -8.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 84.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.286× (z -11.9) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 90.5 | 0 | 1 | — | [[Arbutin (drug)]] 5 µM 0.131× (z -8.9) |
| [[SW48 (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.278× (z -10.9) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 69.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9355), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTMR14]] | +0.74 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[CCDC28A]] | +0.74 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[LINC01881]] | +0.66 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[KLHDC3]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[WIPI2]] | +0.66 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[SPSB3]] | +0.66 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[GMCL1]] | +0.65 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[NARF]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[FBXL20]] | +0.65 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[ADIPOR1]] | +0.63 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[ABTB1]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.63 | +0.63 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD18A]] | -0.62 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[SNHG26]] | -0.58 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[KIF21A]] | -0.58 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[FBXW10B]] | -0.57 | -0.60 / -0.39 | both halves | 6e-05 |  |
| [[NCR3LG1]] | -0.56 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[GPATCH4]] | -0.56 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[TENM3]] | -0.55 | -0.59 / -0.41 | both halves | 4e-05 | same gene group |
| [[UTP20]] | -0.54 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[FNIP2]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[PHACTR2]] | -0.54 | -0.61 / -0.32 | both halves | 2e-04 |  |
| [[ZNF747]] | -0.54 | -0.69 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[LINC01186]] | -0.54 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[DHX37]] | -0.53 | -0.42 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.3, -45.0); signed map (-19.6, 10.5). **Vector** length 133, 44.4% of its response variance represented; |z| ≥ 3 in 1,535 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +10.4 | +7.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +8.8 | +4.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.3 | +3.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +3.9 | +4.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.9 | +1.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.7 | +2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.6 | +4.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.6 | +6.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | +0.1 |
|  | [[Tomivosertib (drug)]] 5 µM |  | +2.0 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -13.1 | -18.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.8 | -14.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.7 | -18.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.9 | -10.4 |
|  | [[EX229 (drug)]] 5 µM |  | -8.8 | -9.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -8.7 | -11.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.4 | -9.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.0 | -8.0 |

## What is on record

|  |  |
|---|---|
| Name | meiosis regulator and mRNA stability factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.11 — chr16:15,594,387-15,643,154 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LKAP, PPP1R34, LMKB; previously KIAA0430 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4F3](https://www.uniprot.org/uniprotkb/Q9Y4F3) (Meiosis regulator and mRNA stability factor 1):

> Essential regulator of oogenesis required for female meiotic progression to repress transposable elements and preventing their mobilization, which is essential for the germline integrity. Probably acts via some RNA metabolic process, equivalent to the piRNA system in males, which mediates the repression of transposable elements during meiosis by forming complexes composed of RNAs and governs the methylation and subsequent repression of transposons. Also required to protect from DNA …

**Summary**, from NCBI Gene [9665](https://www.ncbi.nlm.nih.gov/gene/9665):

> This gene encodes a putative peroxisomal protein that appears to be conserved across Euteleostomi. In humans, it may be autoantigenic. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:29562](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29562) · Entrez [9665](https://www.ncbi.nlm.nih.gov/gene/9665) · UniProt [Q9Y4F3](https://www.uniprot.org/uniprotkb/Q9Y4F3) · Ensembl [ENSG00000166783](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166783)

## Data

Gene col 9355: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9355); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9355, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9355]; `tensor/DDL_lfc|DDL_z.npy` [9355]; `embed/gene_vectors.npy` [9355]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9355 or target_col == 9355). Every well: [[MARF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
