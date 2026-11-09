---
symbol: "TMEM11-DT"
type: "gene"
col: 14024
ensembl_id: "ENSG00000235530"
name: "TMEM11 divergent transcript"
location: "17p11.2"
module: 15
arm: "+"
pooled_cpm: 8.3
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 22
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# TMEM11-DT

*TMEM11 divergent transcript* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.54× (z +18.2, q 0e+00, up in 42 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.340× (z -14.3, q 2e-43, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRDM15]] (+0.71, fdr 7e-06), [[GLUD1P3]] (+0.70, fdr 9e-06), [[PRDM10]] (+0.70, fdr 1e-05); moves opposite to [[IFTAP]] (-0.69, fdr 2e-05), [[AMOT]] (-0.67, fdr 1e-05), [[COMMD8]] (-0.65, fdr 2e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14024.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +18.2 | 0e+00 | 42/45 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +10.8 | 1e-24 | 36/45 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.8 | 2e-12 | 25/48 (HS-578T, BT-474, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +6.7 | 3e-09 | 23/47 (SW 900, HCT15, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.6 | 2e-06 | 20/45 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.54×** | +5.6 | 2e-06 | 18/44 (KATO III, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.50×** | +5.6 | 2e-06 | 19/47 (KATO III, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.37×** | +4.3 | 0.001 | 12/47 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.33×** | +3.8 | 0.010 | 13/39 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.68×** | +3.7 | 0.010 | 5/31 (MIA PaCa-2, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.29×** | +3.5 | 0.022 | 9/45 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.022 | 5/47 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.077 | 11/46 (A-172, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.094 | 4/42 (RPMI-7951, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14024.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.340×** | -14.3 | 2e-43 | 39/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.546×** | -11.8 | 2e-29 | 32/46 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.457×** | -10.8 | 9e-25 | 20/32 (J82, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.531×** | -8.4 | 8e-15 | 24/39 (NCI-H23, LS 180, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.557×** | -8.0 | 1e-13 | 28/46 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.635×** | -6.2 | 4e-08 | 23/41 (A-172, RKO, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.736×** | -6.0 | 2e-07 | 25/48 (NCI-H460, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.669×** | -5.5 | 2e-06 | 20/47 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.687×** | -5.2 | 2e-05 | 17/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.705×** | -4.4 | 5e-04 | 17/24 (SW 900, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **0.739×** | -4.2 | 0.002 | 14/35 (NCI-H460, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.576×** | -4.0 | 0.003 | 10/46 (HT-29, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.760×** | -3.8 | 0.007 | 11/47 (SW 1271, A549, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.767×** | -3.7 | 0.011 | 13/46 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.618×** | -3.5 | 0.019 | 12/42 (LOX-IMVI, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.778×** | -3.4 | 0.019 | 11/44 (LOX-IMVI, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.792×** | -3.2 | 0.043 | 15/47 (CHP-212, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.800×** | -3.1 | 0.066 | 13/47 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Fluorouracil (drug)]] 0.5 µM |  | **0.802×** | -3.0 | 0.067 | 8/46 (C32, A549, …) | inconsistent across doses |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM |  | **0.807×** | -2.9 | 0.085 | 7/44 (NCI-H2347, RKO, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.801×** | -2.9 | 0.085 | 1/47 (SNU-1) | top dose only | plate-row cell shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.810×** | -2.9 | 0.092 | 10/47 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14024. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.76 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0618× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.144× (z -12.9) |
| [[PANC-1 (line)]] | alt | 6.88 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.127× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[A-172 (line)]] | wt | 10.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -11.9) ⚠ cell-cycle shift, explains ~51% of this change |
| [[A498 (line)]] | wt | 8.69 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -14.3) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.153× (z -10.8) |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0803× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 3.20 | 0 | 2 | — | [[Dexmedetomidine (drug)]] 0.05 µM 0.0470× (z -9.2) |
| [[KATO III (line)]] | alt | 14.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 5.59 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.109× (z -9.4) |
| [[A-427 (line)]] | wt | 13.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.170× (z -10.5) |
| [[A549 (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -9.1) ⚠ cell-cycle shift, explains ~51% of this change |
| [[C32 (line)]] | wt | 5.87 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0771× (z -8.9) |
| [[HOP62 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -9.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 6.83 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.127× (z -9.0) |
| [[J82 (line)]] | alt | 7.05 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0719× (z -12.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 10.8 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.200× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 8.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.124× (z -12.0) ⚠ toxic |
| [[RKO (line)]] | wt | 8.37 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.105× (z -8.5) |
| [[SHP-77 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -11.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 5.70 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -11.2) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SW 900 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -9.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 5.71 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -9.5) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SW48 (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -8.7) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SW480 (line)]] | alt | 6.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +12.2) | — |
| [[AN3 CA (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14024), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM15]] | +0.71 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[GLUD1P3]] | +0.70 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[PRDM10]] | +0.70 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[PSMB5]] | +0.68 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[METTL4]] | +0.67 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[SAP30L-AS1]] | +0.67 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[LRRC41]] | +0.66 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[MCM9]] | +0.66 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[APTX]] | +0.66 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[NPLOC4]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ZNF460-AS1]] | +0.65 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[MIATNB]] | +0.64 | +0.58 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFTAP]] | -0.69 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[AMOT]] | -0.67 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[COMMD8]] | -0.65 | -0.47 / -0.69 | both halves | 2e-05 |  |
| [[SNAPIN]] | -0.65 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[TPPP]] | -0.64 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[ALAD]] | -0.63 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[LIMA1]] | -0.61 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[RYBP]] | -0.61 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[TUFT1]] | -0.58 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[CSRP1]] | -0.58 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[MIDEAS]] | -0.58 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[RAB3IP]] | -0.58 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMEM11-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.679). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.5, 20.4); signed map (5.2, -1.2). **Vector** length 86.5, 16.5% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +18.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.3 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +1.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.4 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.9 | -14.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -6.1 | -11.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.6 | -10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | -4.3 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | TMEM11 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17p11.2 — chr17:21,214,322-21,230,035 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55671](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55671) · Entrez [107984969](https://www.ncbi.nlm.nih.gov/gene/107984969) · Ensembl [ENSG00000235530](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235530)

## Data

Gene col 14024: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14024); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14024, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14024]; `tensor/DDL_lfc|DDL_z.npy` [14024]; `embed/gene_vectors.npy` [14024]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14024 or target_col == 14024). Every well: [[TMEM11-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM11-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
