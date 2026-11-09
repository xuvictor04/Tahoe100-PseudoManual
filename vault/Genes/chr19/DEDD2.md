---
symbol: "DEDD2"
type: "gene"
col: 8357
ensembl_id: "ENSG00000160570"
name: "death effector domain containing 2"
location: "19q13.2"
module: 60
arm: "+"
pooled_cpm: 20.17
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# DEDD2

*death effector domain containing 2* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 4.20× (z +16.4, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.421× (z -9.9, q 3e-20, down in 32 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.5 µM: 0.711× (z -3.9, q 0.015, down in 21 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H2347 0.0960×, HT-29 0.123×, HOP62 0.155×, COLO 205 0.153×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (AsPC-1 0.108×, HT-29 0.204×, NCI-H2347 0.183×, HEC-1-A 0.160×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2347 0.147×, KATO III 0.129×, RPMI-7951 0.104×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.377×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFAND2A]] (+0.74, fdr 7e-06), [[MACO1]] (+0.65, fdr 7e-06), [[BAG3]] (+0.65, fdr 7e-06); moves opposite to [[NHLRC2]] (-0.65, fdr 9e-06), [[GFM1]] (-0.61, fdr 3e-05), [[IPO9]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GCKR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8357.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **4.20×** | +16.4 | 0e+00 | 46/47 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.18×** | +13.2 | 2e-37 | 46/47 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.94×** | +12.3 | 1e-32 | 45/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.82×** | +11.2 | 7e-27 | 44/46 (HEC-1-A, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +9.0 | 2e-17 | 32/44 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +8.5 | 1e-15 | 36/42 (SHP-77, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.31×** | +6.8 | 7e-10 | 39/48 (HT-29, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.83×** | +6.2 | 4e-08 | 32/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.65×** | +5.8 | 3e-07 | 31/39 (HEC-1-A, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **2.08×** | +4.4 | 7e-04 | 26/47 (SW480, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 0.002 | 21/46 (NCI-H23, A549, …) | two highest doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.005 | 18/44 (HOP62, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.91×** | +3.9 | 0.005 | 20/43 (SW48, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[crizotinib (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.033 | 15/48 (SW1417, A498, …) | top dose only |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.043 | 8/47 (A-172, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[Vilanterol (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.057 | 8/48 (SW480, HEC-1-A, …) | two highest doses | position effect removed |
| [[Terfenadine (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.076 | 9/48 (A-427, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8357.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H2347 0.0960×, HT-29 0.123×, HOP62 0.155×, COLO 205 0.153×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (AsPC-1 0.108×, HT-29 0.204×, NCI-H2347 0.183×, HEC-1-A 0.160×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2347 0.147×, KATO III 0.129×, RPMI-7951 0.104×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.377×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.421×** | -9.9 | 3e-20 | 32/39 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.524×** | -7.1 | 4e-10 | 28/33 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.596×** | -5.5 | 9e-06 | 24/35 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.711×** | -3.9 | 0.015 | 21/47 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.719×** | -3.7 | 0.020 | 21/47 (A549, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | 0.578× | -3.3 | 0.11 | 17/45 (NCI-H1792, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8357. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 17.8 | 5 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 7.60× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.160× (z -11.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 41.0 | 4 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 5.47× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -15.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 33.0 | 2 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.09× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -10.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 58.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 4.15× (z +8.5) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -8.7) |
| [[KATO III (line)]] | alt | 24.8 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.35× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -11.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 11.4 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.63× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 29.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0960× (z -16.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 28.4 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.19× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -10.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 27.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.64× (z +9.6) | — |
| [[A549 (line)]] | wt | 33.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -9.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 26.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +8.8) ⚠ cell-cycle shift, explains ~88% of this change | [[Dinaciclib (drug)]] 5 µM 0.108× (z -14.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 16.4 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 8.46× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.138× (z -9.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 23.4 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.00× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -12.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 18.5 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.64× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -9.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 19.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.29× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 22.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -10.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 40.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -9.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 17.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.44× (z +12.4) | — |
| [[A-172 (line)]] | wt | 21.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.21× (z +11.6) | — |
| [[A-427 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -11.0) ⚠ cell-cycle shift, explains ~88% of this change |
| [[C32 (line)]] | wt | 12.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.7× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -9.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 27.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.28× (z +11.3) | — |
| [[LS 180 (line)]] | wt | 22.0 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.55× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -10.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 12.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.96× (z +11.7) | — |
| [[SHP-77 (line)]] | alt | 14.1 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 11.8× (z +10.6) ⚠ toxic | — |
| [[SNU-423 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -9.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8357), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFAND2A]] | +0.74 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[MACO1]] | +0.65 | +0.63 / +0.68 | both halves | 7e-06 | STRING 440 |
| [[BAG3]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 | pathway: Cellular response to heat stress |
| [[ZNF581]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[BSDC1]] | +0.63 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[PANX2]] | +0.62 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[TVP23C]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[MXD1]] | +0.62 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[ABHD17B]] | +0.62 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[HLA-F-AS1]] | +0.61 | +0.42 / +0.70 | both halves | 4e-05 |  |
| [[UBB]] | +0.61 | +0.42 / +0.64 | both halves | 4e-05 | pathway: Attenuation phase |
| [[SUGT1]] | +0.61 | +0.69 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHLRC2]] | -0.65 | -0.57 / -0.64 | both halves | 9e-06 |  |
| [[GFM1]] | -0.61 | -0.46 / -0.66 | both halves | 3e-05 |  |
| [[IPO9]] | -0.60 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[YEATS4]] | -0.59 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[ANAPC7]] | -0.59 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[SRFBP1]] | -0.58 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[EFR3A]] | -0.58 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[FARSB]] | -0.58 | -0.37 / -0.71 | both halves | 8e-05 |  |
| [[GUF1]] | -0.56 | -0.42 / -0.65 | both halves | 4e-05 |  |
| [[ABCE1]] | -0.54 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[MIOS]] | -0.54 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[SF3B3]] | -0.54 | -0.41 / -0.64 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GCKR]] | B | GCKR activity raises DEDD2's level | lines that do not express GCKR (24) vs lines expressing it (26) | 1.43× lower at baseline in the lines without GCKR | 0.006 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent |
| [[NDRG1]] | B | NDRG1 activity raises DEDD2's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without NDRG1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[KCNK6]] | B | KCNK6 activity raises DEDD2's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 1.54× lower at baseline in the lines without KCNK6 | 0.063 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[PRAME]] | B | PRAME activity lowers DEDD2's level | lines that do not express PRAME (25) vs lines expressing it (25) | 1.41× higher at baseline in the lines without PRAME | 0.082 | ⚠ within organs, on part of the lines; also absent: GLDC, NR0B1, PAX2 |
| [[WHRN]] | C | WHRN activity lowers DEDD2's level | lines that do not express WHRN (4) vs lines expressing it (46) | 2.06× higher at baseline in the lines without WHRN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, NKAIN1, KIAA1549; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.463). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-17.0, -7.0); signed map (-23.6, 11.5). **Vector** length 114, 31.4% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.6 | +16.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.0 | +11.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.5 | +13.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.2 | +12.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.7 | +5.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.2 | +6.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.6 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +2.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.0 | +0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.9 | +0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | +2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -2.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.8 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.6 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.2 | -2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | death effector domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:42,198,598-42,220,140 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLAME-3 |
| Gene groups (HGNC) | Death effector domain containing |
| Reactome | 7 pathways, smallest: Attenuation phase; HSF1 activation; HSF1-dependent transactivation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXF8](https://www.uniprot.org/uniprotkb/Q8WXF8) (DNA-binding death effector domain-containing protein 2):

> May play a critical role in death receptor-induced apoptosis and may target CASP8 and CASP10 to the nucleus. May regulate degradation of intermediate filaments during apoptosis. May play a role in the general transcription machinery in the nucleus and might be an important regulator of the activity of GTF3C3.

**Summary**, from NCBI Gene [162989](https://www.ncbi.nlm.nih.gov/gene/162989):

> This gene encodes a nuclear-localized protein containing a death effector domain (DED). The encoded protein may regulate the trafficking of caspases and other proteins into the nucleus during death receptor-induced apoptosis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:24450](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24450) · Entrez [162989](https://www.ncbi.nlm.nih.gov/gene/162989) · UniProt [Q8WXF8](https://www.uniprot.org/uniprotkb/Q8WXF8) · Ensembl [ENSG00000160570](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160570)

## Data

Gene col 8357: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8357); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8357, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8357]; `tensor/DDL_lfc|DDL_z.npy` [8357]; `embed/gene_vectors.npy` [8357]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8357 or target_col == 8357). Every well: [[DEDD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DEDD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
