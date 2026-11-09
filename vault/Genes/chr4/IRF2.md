---
symbol: "IRF2"
type: "gene"
col: 9635
ensembl_id: "ENSG00000168310"
name: "interferon regulatory factor 2"
location: "4q35.1"
module: 14
arm: "+"
pooled_cpm: 34.5
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 28
n_dd_up_clean: 14
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# IRF2

*interferon regulatory factor 2* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 1.71× (z +9.3, q 1e-17, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.444× (z -13.4, q 2e-38, down in 28 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.502× (z -12.3, q 1e-32, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HIVEP1]] (+0.74, fdr 7e-06), [[SIX4]] (+0.66, fdr 1e-05), [[TAP1]] (+0.64, fdr 1e-05); moves opposite to [[NAPG]] (-0.64, fdr 1e-05), [[PPIL2]] (-0.58, fdr 5e-05), [[TBCE]] (-0.58, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[GBP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, none with an alert; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9635.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.71×** | +9.3 | 1e-17 | 30/48 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +8.0 | 3e-13 | 29/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +7.8 | 1e-12 | 31/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +7.6 | 4e-12 | 27/47 (SW48, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +7.6 | 4e-12 | 31/48 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +6.3 | 3e-08 | 28/47 (NCI-H1792, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.7 | 1e-06 | 23/48 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +5.7 | 1e-06 | 23/47 (NCI-H2347, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 2e-04 | 19/48 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.65×** | +4.3 | 1e-03 | 22/49 (RPMI-7951, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.004 | 18/48 (MIA PaCa-2, A549, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +3.9 | 0.005 | 14/48 (MIA PaCa-2, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.008 | 14/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.021 | 17/48 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.023 | 12/48 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9635.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.444×** | -13.4 | 2e-38 | 28/40 (A-172, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.472×** | -12.9 | 1e-35 | 30/36 (A-172, KATO III, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.502×** | -12.3 | 1e-32 | 40/48 (A-427, SW480, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.519×** | -11.7 | 1e-29 | 40/45 (NCI-H1573, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.531×** | -11.3 | 9e-28 | 38/48 (SW480, KATO III, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.584×** | -9.6 | 6e-20 | 36/48 (SW480, RKO, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.620×** | -8.5 | 1e-15 | 35/48 (SNU-423, HT-29, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.630×** | -8.3 | 1e-14 | 30/48 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.629×** | -8.0 | 9e-14 | 30/46 (NCI-H1573, SW 900, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.477×** | -6.4 | 1e-08 | 28/48 (PANC-1, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.712×** | -6.1 | 6e-08 | 29/48 (SW480, A-427, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.720×** | -5.9 | 2e-07 | 28/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.509×** | -5.8 | 3e-07 | 31/47 (PANC-1, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.527×** | -5.5 | 2e-06 | 24/47 (PANC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.745×** | -5.0 | 3e-05 | 21/48 (KATO III, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.574×** | -4.8 | 7e-05 | 24/47 (NCI-H460, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.585×** | -4.6 | 1e-04 | 19/47 (NCI-H1792, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.721×** | -4.2 | 9e-04 | 15/47 (HCT15, KATO III, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.729×** | -4.0 | 0.002 | 16/48 (NCI-H1792, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.751×** | -3.6 | 0.007 | 11/48 (NCI-H460, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9635. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 48.7 | 2 | 3 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.25× (z +13.5) | [[Dinaciclib (drug)]] 0.05 µM 0.0583× (z -24.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 38.2 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.234× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 30.1 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 62.4 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0974× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.287× (z -14.4) |
| [[SK-MEL-2 (line)]] | alt | 59.6 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0963× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.278× (z -10.4) |
| [[SW480 (line)]] | alt | 23.0 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -15.0) |
| [[KATO III (line)]] | alt | 49.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0889× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.213× (z -13.7) |
| [[A-427 (line)]] | wt | 27.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -15.0) |
| [[HS-578T (line)]] | alt | 30.8 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.85× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -10.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 24.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.274× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 27.1 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.03× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.114× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 29.2 | 0 | 3 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0486× (z -11.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.280× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 28.4 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.236× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 29.0 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.98× (z +10.6) | — |
| [[NCI-H460 (line)]] | wt | 28.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -9.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 46.5 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.65× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -13.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 40.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.231× (z -11.5) |
| [[SNU-423 (line)]] | alt | 52.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.311× (z -10.0) |
| [[C32 (line)]] | wt | 53.9 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.40× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -9.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 43.1 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.334× (z -9.2) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 38.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -13.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 29.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -11.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 27.4 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0984× (z -8.6) |
| [[H4 (line)]] | wt | 26.4 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0941× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 33.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.322× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 26.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.190× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[Hs 766T (line)]] | wt | 24.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.233× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 36.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -12.7) |
| [[RPMI-7951 (line)]] | alt | 32.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 16.0× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.117× (z -9.6) ⚠ toxic |
| [[SW1417 (line)]] | alt | 31.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0681× (z -19.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9635), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP1]] | +0.74 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[SIX4]] | +0.66 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[TAP1]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[LINC02362]] | +0.64 | +0.62 / +0.58 | both halves | 8e-06 | ⚠ same locus (3.3 kb, same strand: neighbours can correlate without regulation) |
| [[HIVEP2]] | +0.63 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[TRIM69]] | +0.63 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[NKX3-1]] | +0.62 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[PSMB8]] | +0.61 | +0.50 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[LINC02605]] | +0.61 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[PSME2]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 542 |
| [[TNFAIP2]] | +0.61 | +0.58 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[STAT5A]] | +0.61 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[IRF1]] | +0.60 | +0.58 / +0.57 | both halves | 9e-06 | same gene group; pathway: HALLMARK_COMPLEMENT; STRING 982 |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAPG]] | -0.64 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[PPIL2]] | -0.58 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[TBCE]] | -0.58 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ARPC1A]] | -0.57 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[OPA1]] | -0.55 | -0.39 / -0.54 | both halves | 6e-05 | pathway: Programmed Cell Death |
| [[RNF216P1]] | -0.54 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[KCTD21]] | -0.54 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[TCF3]] | -0.54 | -0.48 / -0.43 | both halves | 4e-05 |  |
| [[TMEM41B]] | -0.54 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[SMC5]] | -0.53 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[ZNF875]] | -0.53 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ELP1]] | -0.52 | -0.46 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP3]] | B | GBP3 activity raises IRF2's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 1.38× lower at baseline in the lines without GBP3 | 0.031 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[GBP4]] | B | GBP4 activity raises IRF2's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.28× lower at baseline in the lines without GBP4 | 0.034 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[NKX3-1]] | B | NKX3-1 activity raises IRF2's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 1.22× lower at baseline in the lines without NKX3-1 | 0.035 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers IRF2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SERTAD4]] | B | SERTAD4 activity raises IRF2's level | lines that do not express SERTAD4 (14) vs lines expressing it (36) | 1.26× lower at baseline in the lines without SERTAD4 | 0.060 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC |
| [[IL15]] | B | IL15 activity raises IRF2's level | lines that do not express IL15 (10) vs lines expressing it (40) | 1.30× lower at baseline in the lines without IL15 | 0.069 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers IRF2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[NMI]] | C | NMI activity raises IRF2's level | lines that do not express NMI (4) vs lines expressing it (46) | 1.42× lower at baseline in the lines without NMI | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NABP1, LGI4, C21orf91; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.3, 4.8); signed map (40.6, 8.1). **Vector** length 121, 33.4% of its response variance represented; |z| ≥ 3 in 1,210 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.6 | +8.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.5 | +9.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +7.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.6 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +0.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.0 | +3.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.7 | +2.7 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.9 | -11.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.8 | -12.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.3 | -9.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.2 | -8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.5 | -13.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -8.5 |
|  | [[EX229 (drug)]] 5 µM |  | -5.0 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -5.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.8 | -5.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | interferon regulatory factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:184,385,702-184,474,558 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Interferon regulatory factors |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, COMPLEMENT, INTERFERON_GAMMA_RESPONSE |
| Reactome | 9 pathways, smallest: Pyroptosis; Regulated Necrosis; Interferon alpha/beta signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P14316](https://www.uniprot.org/uniprotkb/P14316) (Interferon regulatory factor 2):

> DNA-binding transcription factor that specifically binds to the upstream regulatory region of type I interferon (IFN) and IFN-inducible genes and regulates their expression. Mainly acts as a transcription repressor, repressing expression. Also acts as an activator for several genes including H4 and IL7. Constitutively binds to the ISRE promoter to activate IL7. Involved in cell cycle regulation through binding the site II (HiNF-M) promoter region of H4 and activating transcription during cell …

**Summary**, from NCBI Gene [3660](https://www.ncbi.nlm.nih.gov/gene/3660):

> IRF2 encodes interferon regulatory factor 2, a member of the interferon regulatory transcription factor (IRF) family. IRF2 competitively inhibits the IRF1-mediated transcriptional activation of interferons alpha and beta, and presumably other genes that employ IRF1 for transcription activation. However, IRF2 also functions as a transcriptional activator of histone H4. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6117](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6117) · Entrez [3660](https://www.ncbi.nlm.nih.gov/gene/3660) · UniProt [P14316](https://www.uniprot.org/uniprotkb/P14316) · Ensembl [ENSG00000168310](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168310)

## Data

Gene col 9635: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9635); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9635, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9635]; `tensor/DDL_lfc|DDL_z.npy` [9635]; `embed/gene_vectors.npy` [9635]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9635 or target_col == 9635). Every well: [[IRF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
