---
symbol: "MAX"
type: "gene"
col: 4695
ensembl_id: "ENSG00000125952"
name: "MYC associated transcriptional regulator X"
location: "14q23.3"
module: 40
arm: "+"
pooled_cpm: 90.06
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 21
n_dd_up_clean: 18
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# MAX

*MYC associated transcriptional regulator X* — 14q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.77× (z +9.7, q 2e-19, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.632× (z -7.5, q 5e-11, down in 32 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Gallic acid (hydrate) (drug)]] 0.05 µM: 0.770× (z -4.4, q 0.001, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELP2]] (+0.82, fdr 7e-06), [[SRP54-AS1]] (+0.80, fdr 7e-06), [[IFT20]] (+0.75, fdr 7e-06); moves opposite to [[TASOR]] (-0.68, fdr 7e-06), [[ZKSCAN2]] (-0.67, fdr 7e-06), [[TMEM185B]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4695.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +9.7 | 2e-19 | 39/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.76×** | +9.6 | 3e-19 | 44/48 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.72×** | +9.2 | 8e-18 | 44/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +8.6 | 9e-16 | 33/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +7.3 | 3e-11 | 39/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +6.4 | 1e-08 | 35/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +6.3 | 2e-08 | 37/48 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +6.1 | 7e-08 | 31/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.82×** | +5.3 | 6e-06 | 31/48 (RKO, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +5.3 | 7e-06 | 27/48 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.0 | 2e-05 | 27/49 (SHP-77, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +4.9 | 5e-05 | 26/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.66×** | +4.5 | 3e-04 | 29/49 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +4.0 | 0.003 | 25/47 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +3.9 | 0.004 | 24/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.005 | 23/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.7 | 0.008 | 16/49 (NCI-H1573, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4695.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.632×** | -7.5 | 5e-11 | 32/44 (CHP-212, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.695×** | -5.9 | 1e-06 | 28/49 (COLO 205, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.725×** | -5.0 | 9e-05 | 26/45 (RKO, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.770×** | -4.4 | 0.001 | 33/48 (Panc 03.27, SK-MEL-2, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.779×** | -4.2 | 0.003 | 28/48 (A-172, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.792×** | -3.9 | 0.007 | 26/48 (A498, SW 900, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.783×** | -3.9 | 0.007 | 29/48 (NCI-H1573, RPMI-7951, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.806×** | -3.6 | 0.017 | 24/48 (RPMI-7951, PANC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.806×** | -3.6 | 0.017 | 25/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.807×** | -3.6 | 0.017 | 23/49 (SW1417, HEC-1-A, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | **0.811×** | -3.5 | 0.020 | 22/48 (A-172, NCI-H1573, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.813×** | -3.5 | 0.021 | 26/49 (A549, A-172, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.813×** | -3.5 | 0.021 | 23/48 (A-172, NCI-H1792, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.814×** | -3.5 | 0.021 | 23/48 (RPMI-7951, LS 180, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.815×** | -3.4 | 0.022 | 20/48 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.805×** | -3.4 | 0.025 | 20/47 (RKO, COLO 205, …) | all doses, flat | low cells (technical?) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.820×** | -3.3 | 0.028 | 24/49 (A498, SW 900, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.815×** | -3.3 | 0.030 | 21/48 (RPMI-7951, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4695. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 93.6 | 8 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +12.7) | — |
| [[NCI-H460 (line)]] | wt | 68.7 | 7 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.92× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.88× (z +13.3) | — |
| [[NCI-H1792 (line)]] | alt | 129 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.57× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +13.8) | — |
| [[NCI-H23 (line)]] | alt | 124 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.12× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 60.2 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +12.0) | — |
| [[COLO 205 (line)]] | alt | 88.9 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.90× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0955× (z -19.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 82.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 49.5 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.86× (z +13.2) | — |
| [[SHP-77 (line)]] | alt | 72.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.72× (z +10.0) | — |
| [[LoVo (line)]] | wt | 78.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.7) | — |
| [[Panc 03.27 (line)]] | alt | 113 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.67× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 127 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -9.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 111 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0827× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.242× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 82.8 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.36× (z +9.7) | — |
| [[KATO III (line)]] | alt | 62.1 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.51× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 107 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 1.89× (z +8.8) | — |
| [[RKO (line)]] | wt | 104 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -13.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 106 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -14.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 85.9 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.89× (z +9.4) | — |
| [[C-33 A (line)]] | alt | 57.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.03× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 89.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -11.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 57.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.303× (z -8.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 70.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -10.6) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 110 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.100× (z -8.9) |
| [[A-172 (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 97.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 107 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 101 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 86.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 70.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 115 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4695), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELP2]] | +0.82 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.80 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[IFT20]] | +0.75 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[KCTD7]] | +0.73 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[RAB6A]] | +0.73 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[SDHAP1]] | +0.72 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.72 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[GPR107]] | +0.71 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.71 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[RAB40C]] | +0.71 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[PPOX]] | +0.70 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[CBFA2T2]] | +0.70 | +0.67 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TASOR]] | -0.68 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[ZKSCAN2]] | -0.67 | -0.66 / -0.73 | both halves | 7e-06 |  |
| [[TMEM185B]] | -0.66 | -0.64 / -0.67 | both halves | 7e-06 |  |
| [[ZC3H4]] | -0.65 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[CEP41]] | -0.65 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[SRCAP]] | -0.64 | -0.59 / -0.57 | both halves | 9e-06 |  |
| [[CHTOP]] | -0.64 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[ZBTB38]] | -0.64 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.64 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[CSTF2T]] | -0.64 | -0.58 / -0.63 | both halves | 8e-06 |  |
| [[COMMD10]] | -0.63 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[MED1]] | -0.63 | -0.64 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.831). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (4.5, -18.4); signed map (-42.5, 13.2). **Vector** length 100, 31.2% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +3.3 | +9.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.8 | +3.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.5 | +1.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.5 | +9.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.3 | +7.3 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +3.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -8.9 | -2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.9 | -2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.0 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -3.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.9 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | MYC associated transcriptional regulator X |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.3 — chr14:65,006,174-65,102,695 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bHLHd4, bHLHd5, bHLHd6, bHLHd7, bHLHd8 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Reactome | 10 pathways, smallest: Transcription of E2F targets under negative control by DREAM complex; G0 and Early G1; Transcriptional Regulation by E2F6 |
| Matched by | ensembl_id |

**Function**, from UniProt [P61244](https://www.uniprot.org/uniprotkb/P61244) (Protein max):

> Transcription regulator. Forms a sequence-specific DNA-binding protein complex with MYC or MAD which recognizes the core sequence 5'-CAC[GA]TG-3'. The MYC:MAX complex is a transcriptional activator, whereas the MAD:MAX complex is a repressor. May repress transcription via the recruitment of a chromatin remodeling complex containing H3 'Lys-9' histone methyltransferase activity. Represses MYC transcriptional activity from E-box elements.

**Summary**, from NCBI Gene [4149](https://www.ncbi.nlm.nih.gov/gene/4149):

> The protein encoded by this gene is a member of the basic helix-loop-helix leucine zipper (bHLHZ) family of transcription factors. It is able to form homodimers and heterodimers with other family members, which include Mad, Mxi1 and Myc. Myc is an oncoprotein implicated in cell proliferation, differentiation and apoptosis. The homodimers and heterodimers compete for a common DNA target site (the E box) and rearrangement among these dimer forms provides a complex system of transcriptional …

**Accessions** — [HGNC:6913](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6913) · Entrez [4149](https://www.ncbi.nlm.nih.gov/gene/4149) · UniProt [P61244](https://www.uniprot.org/uniprotkb/P61244) · Ensembl [ENSG00000125952](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125952)

## Data

Gene col 4695: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4695); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4695, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4695]; `tensor/DDL_lfc|DDL_z.npy` [4695]; `embed/gene_vectors.npy` [4695]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4695 or target_col == 4695). Every well: [[MAX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
