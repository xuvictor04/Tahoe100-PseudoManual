---
symbol: "PABIR2"
type: "gene"
col: 7989
ensembl_id: "ENSG00000156504"
name: "PABIR family member 2"
location: "Xq26.3"
module: 20
arm: "+"
pooled_cpm: 31.29
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# PABIR2

*PABIR family member 2* — Xq26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.55× (z +27.0, q 0e+00, up in 38 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.82× (z +13.3, q 4e-38, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.519× (z -20.5, q 0e+00, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGO1]] (+0.74, fdr 7e-06), [[HDAC1]] (+0.66, fdr 1e-05), [[DHFR]] (+0.66, fdr 1e-05); moves opposite to [[MED19]] (-0.67, fdr 7e-06), [[FOXA2]] (-0.66, fdr 1e-05), [[AK6]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7989.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.55×** | +27.0 | 0e+00 | 38/38 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.13×** | +25.3 | 0e+00 | 42/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.50×** | +18.8 | 0e+00 | 38/42 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +13.3 | 4e-38 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.79×** | +12.9 | 5e-36 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +11.1 | 8e-27 | 36/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +9.5 | 2e-19 | 30/48 (SW480, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +7.7 | 1e-12 | 25/48 (PANC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +5.3 | 6e-06 | 20/47 (HS-578T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +5.2 | 9e-06 | 19/48 (AsPC-1, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.25×** | +4.9 | 6e-05 | 21/46 (NCI-H460, HOP62, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.20×** | +4.1 | 0.002 | 11/48 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.19× | +3.9 | 0.005 | 11/47 (SW480, A-427, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.17× | +3.4 | 0.027 | 12/48 (C32, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.3 | 0.033 | 12/47 (NCI-H2030, A-427, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.078 | 6/48 (SW480, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7989.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.519×** | -20.5 | 0e+00 | 38/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.547×** | -13.4 | 3e-38 | 37/47 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.650×** | -9.6 | 2e-19 | 30/48 (PANC-1, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.706×** | -7.4 | 1e-11 | 27/48 (NCI-H2347, PANC-1, …) | two highest doses | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.816×** | -6.4 | 2e-08 | 22/47 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.794×** | -5.1 | 3e-05 | 21/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.838× | -3.9 | 0.007 | 14/48 (SHP-77, NCI-H1573, …) | all doses, flat |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.730×** | -3.6 | 0.019 | 13/46 (NCI-H2030, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.893× | -3.5 | 0.025 | 13/48 (SK-MEL-2, RPMI-7951, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -3.4 | 0.039 | 14/48 (SW480, SW48, …) | inconsistent across doses |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.900× | -3.3 | 0.047 | 7/48 (NCI-H460, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7989. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 97.8 | 8 (5 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.05× (z +21.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -11.3) |
| [[PANC-1 (line)]] | alt | 49.3 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.75× (z +19.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -18.5) |
| [[SW1417 (line)]] | alt | 75.8 | 5 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +18.2) | [[Digitoxin (drug)]] 5 µM 0.418× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 28.4 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.62× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 28.8 | 4 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.77× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -13.1) |
| [[SW48 (line)]] | wt | 75.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -13.5) |
| [[HCT15 (line)]] | alt | 35.9 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 7.32× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -12.6) |
| [[HT-29 (line)]] | alt | 26.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +12.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -8.9) |
| [[J82 (line)]] | alt | 32.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -11.3) |
| [[KATO III (line)]] | alt | 41.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.64× (z +14.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 29.8 | 2 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 2.04× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -19.4) |
| [[A498 (line)]] | wt | 25.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +12.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 22.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.15× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -9.4) |
| [[HOP62 (line)]] | alt | 21.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.89× (z +12.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 18.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +11.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 25.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +11.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 24.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +9.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 18.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 4.02× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 25.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.00× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -9.4) |
| [[SNU-423 (line)]] | alt | 34.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +13.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 35.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -10.1) |
| [[A549 (line)]] | wt | 17.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.65× (z +10.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 36.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.59× (z +11.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 23.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 40.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 19.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -9.3) |
| [[A-172 (line)]] | wt | 13.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.48× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 17.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.90× (z +10.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 14.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.15× (z +9.6) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 26.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -16.8) |
| [[H4 (line)]] | wt | 26.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.62× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 17.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.62× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0945× (z -10.8) ⚠ transcription drop |
| [[SNU-1 (line)]] | wt | 23.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -12.6) |
| [[AN3 CA (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7989), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGO1]] | +0.74 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[HDAC1]] | +0.66 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[DHFR]] | +0.66 | +0.55 / +0.80 | both halves | 1e-05 |  |
| [[CPSF6]] | +0.65 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[DCAF16]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[CNPY3]] | +0.65 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[ARF3]] | +0.65 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[FAM91A1]] | +0.64 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[MAN2B2]] | +0.63 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[SELENON]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[RPSA]] | +0.63 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[SH3GLB2]] | +0.63 | +0.62 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED19]] | -0.67 | -0.66 / -0.69 | both halves | 7e-06 |  |
| [[FOXA2]] | -0.66 | -0.49 / -0.72 | both halves | 1e-05 |  |
| [[AK6]] | -0.66 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[ZCCHC10]] | -0.65 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[CCDC174]] | -0.64 | -0.64 / -0.57 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.64 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[C14orf119]] | -0.64 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[MPLKIP]] | -0.63 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[TOPORS]] | -0.63 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[NKAP]] | -0.63 | -0.66 / -0.63 | both halves | 7e-06 |  |
| [[IRX5]] | -0.63 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[ZKSCAN1]] | -0.62 | -0.60 / -0.66 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.722). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-27.3, -24.4); signed map (-27.3, -35.4). **Vector** length 103, 23.8% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.0 | +27.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.9 | +25.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.7 | +18.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.3 | +9.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +13.3 |
|  | [[Folic acid (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | -1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +5.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +1.7 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | +1.8 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.7 | -20.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.2 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.4 | -13.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -7.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.5 | -9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -5.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | PABIR family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.3 — chrX:134,769,566-134,797,232 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686L20116, RP11-308B5.5, SPACIA2; previously FAM122B |
| Matched by | ensembl_id |

UniProt [Q7Z309](https://www.uniprot.org/uniprotkb/Q7Z309) carries no function annotation.

**Summary**, from NCBI Gene [159090](https://www.ncbi.nlm.nih.gov/gene/159090):

> Predicted to enable protein serine/threonine phosphatase inhibitor activity. Predicted to be involved in positive regulation of proteasomal ubiquitin-dependent protein catabolic process. Predicted to be active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30490](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30490) · Entrez [159090](https://www.ncbi.nlm.nih.gov/gene/159090) · UniProt [Q7Z309](https://www.uniprot.org/uniprotkb/Q7Z309) · Ensembl [ENSG00000156504](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156504)

## Data

Gene col 7989: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7989); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7989, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7989]; `tensor/DDL_lfc|DDL_z.npy` [7989]; `embed/gene_vectors.npy` [7989]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7989 or target_col == 7989). Every well: [[PABIR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PABIR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
