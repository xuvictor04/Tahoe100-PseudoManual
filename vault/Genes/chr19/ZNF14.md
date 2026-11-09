---
symbol: "ZNF14"
type: "gene"
col: 2651
ensembl_id: "ENSG00000105708"
name: "zinc finger protein 14"
location: "19p13.11"
module: 17
arm: "+"
pooled_cpm: 15.0
n_lines_expressing: 47
n_dd_up: 20
n_dd_down: 15
n_dd_up_clean: 19
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ZNF14

*zinc finger protein 14* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.55× (z +15.0, q 0e+00, up in 39 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.308× (z -14.8, q 0e+00, down in 32 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.683× (z -4.8, q 2e-04, down in 20 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL14]] (+0.73, fdr 7e-06), [[RP9]] (+0.73, fdr 7e-06), [[ZNF230]] (+0.73, fdr 7e-06); moves opposite to [[HCFC1]] (-0.67, fdr 7e-06), [[RNF32-AS1]] (-0.64, fdr 1e-05), [[DDX5]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RRAGD]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2651.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.55×** | +15.0 | 0e+00 | 39/44 (RKO, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **9.54×** | +14.8 | 0e+00 | 45/45 (MIA PaCa-2, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.95×** | +10.5 | 1e-23 | 39/44 (LS 180, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +8.8 | 1e-16 | 35/44 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +5.9 | 5e-07 | 24/45 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.51×** | +5.2 | 2e-05 | 23/45 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +5.0 | 6e-05 | 29/45 (NCI-H460, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.7 | 2e-04 | 20/44 (LS 180, J82, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +4.6 | 2e-04 | 19/45 (NCI-H2347, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +4.6 | 3e-04 | 18/45 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +4.1 | 0.002 | 17/45 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +4.0 | 0.003 | 16/45 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.006 | 12/44 (NCI-H23, SNU-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.010 | 19/44 (C32, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.010 | 15/45 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +3.6 | 0.010 | 8/45 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2651.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.308×** | -14.8 | 0e+00 | 32/37 (A549, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.304×** | -14.4 | 8e-45 | 24/26 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.445×** | -9.4 | 7e-19 | 19/30 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.683×** | -4.8 | 2e-04 | 20/44 (HOP62, SHP-77, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.755×** | -4.8 | 2e-04 | 23/45 (A-172, CHP-212, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.690×** | -4.7 | 3e-04 | 21/45 (AsPC-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.702×** | -4.5 | 6e-04 | 16/45 (Panc 03.27, HEC-1-A, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.732×** | -3.9 | 0.006 | 16/45 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.735×** | -3.9 | 0.007 | 14/45 (CFPAC-1, HOP62, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.742×** | -3.8 | 0.009 | 9/45 (PANC-1, LS 180, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.754×** | -3.6 | 0.019 | 17/45 (SHP-77, HOP62, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.764×** | -3.4 | 0.032 | 10/45 (Panc 03.27, SHP-77, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.822×** | -3.2 | 0.057 | 17/45 (NCI-H2347, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.783×** | -3.1 | 0.079 | 12/45 (KATO III, NCI-H661, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.784×** | -3.1 | 0.079 | 7/45 (HEC-1-A, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2651. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 23.2 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 25.4× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.0796× (z -15.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 22.5 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 17.6× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.0539× (z -17.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 21.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0521× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -12.4) |
| [[PANC-1 (line)]] | alt | 14.8 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 18.2× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.192× (z -11.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 14.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0583× (z -15.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 14.5 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.7× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -14.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 15.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -11.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 18.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -11.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 15.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -13.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 18.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.0763× (z -14.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 16.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -8.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 19.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 19.3× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -12.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 23.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 22.7× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -10.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 23.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +11.6) | — |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 21.6× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 26.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0911× (z -13.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +8.8) | — |
| [[C-33 A (line)]] | alt | 27.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -11.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 16.5 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0537× (z -12.1) |
| [[HOP62 (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -8.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 13.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 17.9× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -10.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -9.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2651), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL14]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[RP9]] | +0.73 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[ZNF230]] | +0.73 | +0.71 / +0.68 | both halves | 7e-06 | same gene group |
| [[KBTBD3]] | +0.71 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[PRPF39]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ORC4]] | +0.69 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[SNX2]] | +0.69 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[RIOK2]] | +0.68 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[CGRRF1]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[PRMT9]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[FAM229B]] | +0.67 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[RCHY1]] | +0.66 | +0.70 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCFC1]] | -0.67 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[RNF32-AS1]] | -0.64 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[DDX5]] | -0.64 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.64 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[HNRNPAB]] | -0.63 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.62 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[PEPD]] | -0.62 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[DOCK1]] | -0.62 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[MFSD14CP-1]] | -0.61 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[AVEN]] | -0.61 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[SLC20A2]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[ATP2A2]] | -0.59 | -0.52 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RRAGD]] | B | RRAGD activity raises ZNF14's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 2.26× lower at baseline in the lines without RRAGD | 0.025 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |
| [[ZNF461]] | B | ZNF461 activity raises ZNF14's level | lines that do not express ZNF461 (7) vs lines expressing it (43) | 2.93× lower at baseline in the lines without ZNF461 | 0.079 | ⚠ within organs, on part of the lines; also absent: ZNF567, ZNF529-AS1, ZNF571 |
| [[ZNF571]] | B | ZNF571 activity raises ZNF14's level | lines that do not express ZNF571 (6) vs lines expressing it (44) | 3.05× lower at baseline in the lines without ZNF571 | 0.091 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.714). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-23.9, -4.3); signed map (-25.2, -8.6). **Vector** length 75.3, 14.8% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.6 | +14.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +10.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +0.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.7 | -14.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.6 | -14.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -4.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | +1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:19,710,472-19,733,112 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KOX6, GIOT-4 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P17017](https://www.uniprot.org/uniprotkb/P17017) (Zinc finger protein 14):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7561](https://www.ncbi.nlm.nih.gov/gene/7561):

> The protein encoded by this gene contains a zinc finger and a Kruppel-associated box (KRAB) domain. KRAB domain is known to be involved in the transcriptional repression of a number of zinc finger proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12924](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12924) · Entrez [7561](https://www.ncbi.nlm.nih.gov/gene/7561) · UniProt [P17017](https://www.uniprot.org/uniprotkb/P17017) · Ensembl [ENSG00000105708](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105708)

## Data

Gene col 2651: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2651); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2651, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2651]; `tensor/DDL_lfc|DDL_z.npy` [2651]; `embed/gene_vectors.npy` [2651]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2651 or target_col == 2651). Every well: [[ZNF14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
