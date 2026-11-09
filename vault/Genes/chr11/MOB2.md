---
symbol: "MOB2"
type: "gene"
col: 11260
ensembl_id: "ENSG00000182208"
name: "MOB kinase activator 2"
location: "11p15.5"
module: 145
arm: "+"
pooled_cpm: 22.5
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 19
n_dd_up_clean: 12
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# MOB2

*MOB kinase activator 2* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.24× (z +14.6, q 3e-45, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.384× (z -15.3, q 0e+00, down in 44 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[venetoclax (drug)]] 5 µM: 0.356× (z -9.8, q 2e-20, down in 34 of 44 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABTB1]] (+0.76, fdr 7e-06), [[SPSB3]] (+0.70, fdr 3e-05), [[WIPI2]] (+0.69, fdr 2e-05); moves opposite to [[AGL]] (-0.55, fdr 4e-05), [[ZNF280D]] (-0.53, fdr 1e-04), [[RBM26]] (-0.52, fdr 2e-04).
> It is in [[Module 145]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11260.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.24×** | +14.6 | 3e-45 | 44/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.92×** | +11.8 | 1e-29 | 42/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +10.7 | 1e-24 | 42/47 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +6.2 | 8e-08 | 25/48 (J82, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +5.8 | 6e-07 | 23/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.6 | 2e-06 | 20/47 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.37×** | +5.5 | 3e-06 | 22/47 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.002 | 18/47 (RPMI-7951, NCI-H2030, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.7 | 0.011 | 0/48 | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.021 | 11/47 (LoVo, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.062 | 11/48 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.20×** | +3.1 | 0.082 | 3/48 (Panc 03.27, KATO III, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.082 | 8/46 (LoVo, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.19× | +3.1 | 0.089 | 6/47 (NCI-H2347, A549, …) | two highest doses |  |
| [[crizotinib (drug)]] 5 µM |  | 1.19× | +3.0 | 0.089 | 8/48 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.091 | 3/48 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11260.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.384×** | -15.3 | 0e+00 | 44/47 (AsPC-1, HT-29, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.479×** | -12.8 | 3e-35 | 25/31 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.533×** | -11.4 | 8e-28 | 29/41 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.356×** | -9.8 | 2e-20 | 34/44 (NCI-H1792, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.361×** | -9.6 | 6e-20 | 37/45 (A549, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.575×** | -9.3 | 2e-18 | 24/36 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.378×** | -9.2 | 3e-18 | 36/47 (LOX-IMVI, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.381×** | -9.1 | 5e-18 | 36/45 (PANC-1, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.433×** | -7.9 | 2e-13 | 31/46 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.543×** | -7.9 | 2e-13 | 34/48 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.589×** | -6.8 | 4e-10 | 31/48 (SW480, HT-29, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.699×** | -6.1 | 4e-08 | 27/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.637×** | -5.8 | 2e-07 | 25/48 (HT-29, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.806×** | -5.5 | 1e-06 | 21/48 (A-427, Hs 766T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.783×** | -4.3 | 8e-04 | 16/47 (SNU-1, A-427, …) | top dose only | composition shift |
| [[Decitabine (drug)]] 0.5 µM |  | **0.800×** | -4.1 | 0.002 | 13/47 (SW 1271, LoVo, …) | inconsistent across doses | position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **0.652×** | -4.0 | 0.002 | 18/44 (A498, SNU-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.680×** | -3.7 | 0.008 | 17/48 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.883× | -3.2 | 0.040 | 8/48 (SW 900, SW 1088, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | 0.842× | -2.9 | 0.087 | 10/48 (SHP-77, J82, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11260. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.2 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.02× (z +13.8) | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -15.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 42.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -13.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 32.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -13.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 32.5 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.268× (z -10.1) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 37.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0870× (z -18.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 22.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.12× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -10.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 25.0 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0881× (z -9.8) ⚠ toxic |
| [[A-427 (line)]] | wt | 22.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.450× (z -8.8) |
| [[A498 (line)]] | wt | 18.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -8.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 27.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -13.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 27.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.83× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.338× (z -9.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 23.8 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.158× (z -12.1) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 21.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.196× (z -10.5) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 19.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -9.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 23.0 | 0 | 1 | — | [[Mifepristone (drug)]] 5 µM 0.0643× (z -8.9) |
| [[C32 (line)]] | wt | 20.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -10.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0654× (z -15.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.257× (z -9.6) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 20.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0854× (z -13.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 16.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 27.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -9.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.196× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -12.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -11.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 29.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0939× (z -10.8) |
| [[SW48 (line)]] | wt | 24.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -10.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11260), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABTB1]] | +0.76 | +0.59 / +0.79 | both halves | 7e-06 |  |
| [[SPSB3]] | +0.70 | +0.43 / +0.75 | both halves | 3e-05 |  |
| [[WIPI2]] | +0.69 | +0.48 / +0.73 | both halves | 2e-05 |  |
| [[INPP5K]] | +0.68 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[HECA]] | +0.66 | +0.48 / +0.74 | both halves | 2e-05 |  |
| [[ULK1]] | +0.64 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[MXD4]] | +0.62 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[UBALD1]] | +0.62 | +0.34 / +0.69 | both halves | 1e-04 |  |
| [[RB1CC1]] | +0.61 | +0.36 / +0.70 | both halves | 1e-04 |  |
| [[OTUD5]] | +0.60 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[WASF2]] | +0.60 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[MAP3K3]] | +0.60 | +0.32 / +0.64 | both halves | 2e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGL]] | -0.55 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[ZNF280D]] | -0.53 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[RBM26]] | -0.52 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[CC2D2A]] | -0.52 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[ECHDC1]] | -0.51 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[PRTFDC1]] | -0.51 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[GUF1]] | -0.51 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[PUS7L]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[MTMR2]] | -0.50 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[ARHGEF9]] | -0.49 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[STEAP2]] | -0.49 | -0.15 / -0.59 | ⚠ one half (not replicated) | 0.001 |  |
| [[SLC16A9]] | -0.49 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[NAPEPLD]] | -0.49 | -0.46 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.760). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.5, -43.7); signed map (-19.5, 11.7). **Vector** length 90.1, 19.4% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.3 | +11.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +14.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.1 | +6.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.9 | +10.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +1.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.2 | -15.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.1 | -9.1 |
|  | [[EX229 (drug)]] 5 µM |  | -6.2 | -7.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.1 | -9.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.1 | -9.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.9 | -9.2 |

## What is on record

|  |  |
|---|---|
| Name | MOB kinase activator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:1,469,457-1,501,247 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HCCA2 |
| Gene groups (HGNC) | MOB kinase activators |
| Matched by | ensembl_id |

**Function**, from UniProt [Q70IA6](https://www.uniprot.org/uniprotkb/Q70IA6) (MOB kinase activator 2):

> Stimulates the autophosphorylation and kinase activity of STK38 and STK38L.

**Summary**, from NCBI Gene [81532](https://www.ncbi.nlm.nih.gov/gene/81532):

> Predicted to enable protein kinase activator activity. Predicted to be involved in signal transduction. Predicted to act upstream of or within actin cytoskeleton organization; positive regulation of neuron projection development; and positive regulation of protein phosphorylation. Located in cytosol; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24904](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24904) · Entrez [81532](https://www.ncbi.nlm.nih.gov/gene/81532) · UniProt [Q70IA6](https://www.uniprot.org/uniprotkb/Q70IA6) · Ensembl [ENSG00000182208](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182208)

## Data

Gene col 11260: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11260); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11260, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11260]; `tensor/DDL_lfc|DDL_z.npy` [11260]; `embed/gene_vectors.npy` [11260]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11260 or target_col == 11260). Every well: [[MOB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
