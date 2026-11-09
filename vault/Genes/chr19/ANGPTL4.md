---
symbol: "ANGPTL4"
type: "gene"
col: 9537
ensembl_id: "ENSG00000167772"
name: "angiopoietin like 4"
location: "19p13.2"
module: 113
arm: "+"
pooled_cpm: 128.77
n_lines_expressing: 37
n_dd_up: 17
n_dd_down: 37
n_dd_up_clean: 17
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 9
direction_downstream: 5
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# ANGPTL4

*angiopoietin like 4* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (none with an alert); the strongest is [[Betamethasone dipropionate (drug)]] 5 µM: 1.94× (z +4.9, q 5e-04, up in 25 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.128× (z -22.2, q 0e+00, down in 33 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MT1X]] (+0.80, fdr 7e-06), [[MT2A]] (+0.79, fdr 7e-06), [[TANC2]] (+0.69, fdr 7e-06); moves opposite to [[MATN2]] (-0.58, fdr 3e-05), [[PSG9]] (-0.53, fdr 2e-04), [[NNT]] (-0.50, fdr 5e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[SERPINE1]] → it (grade B ⚠); 5 go from it, the strongest it → [[NNT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, none with an alert; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9537.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.94×** | +4.9 | 5e-04 | 25/36 (SNU-423, HS-578T, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.76×** | +4.4 | 0.002 | 24/35 (SNU-423, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +4.3 | 0.002 | 23/35 (A-172, A498, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +4.3 | 0.002 | 25/35 (SNU-423, HS-578T, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.70×** | +4.1 | 0.003 | 22/35 (SNU-423, HS-578T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.70×** | +4.1 | 0.003 | 23/35 (SNU-423, HS-578T, …) | all doses, flat |  |
| [[Econazole (drug)]] 5 µM |  | **1.70×** | +4.1 | 0.003 | 23/35 (SNU-423, HS-578T, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +3.9 | 0.006 | 24/36 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.63×** | +3.8 | 0.009 | 19/35 (SNU-423, A498, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.62×** | +3.8 | 0.010 | 22/35 (SNU-423, HS-578T, …) | all doses, flat |  |
| [[Bexarotene (drug)]] 5 µM |  | **1.60×** | +3.7 | 0.013 | 20/35 (HS-578T, SNU-423, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.59×** | +3.6 | 0.015 | 21/35 (SNU-423, A-172, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.59×** | +3.6 | 0.015 | 21/35 (SNU-423, HS-578T, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.56×** | +3.5 | 0.022 | 21/35 (SNU-423, HS-578T, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.51×** | +3.2 | 0.049 | 21/37 (SNU-423, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9537.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.128×** | -22.2 | 0e+00 | 33/35 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.275×** | -13.9 | 2e-41 | 33/36 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.161×** | -13.4 | 2e-38 | 32/35 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.221×** | -11.5 | 2e-28 | 30/35 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.222×** | -11.0 | 4e-26 | 30/34 (CHP-212, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.413×** | -9.5 | 2e-19 | 32/35 (SK-MEL-2, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.334×** | -8.0 | 9e-14 | 29/35 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.375×** | -7.5 | 6e-12 | 30/35 (HOP62, SW 900, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.393×** | -7.1 | 8e-11 | 31/35 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.360×** | -6.7 | 2e-09 | 29/35 (HOP62, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.434×** | -6.3 | 1e-08 | 30/35 (PANC-1, J82, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.439×** | -6.3 | 2e-08 | 23/35 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.426×** | -6.2 | 2e-08 | 27/34 (PANC-1, SW 1271, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.513×** | -5.1 | 2e-05 | 25/35 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.510×** | -4.9 | 4e-05 | 27/37 (SW 1271, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.460×** | -4.8 | 4e-05 | 23/37 (SK-MEL-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.637×** | -4.8 | 5e-05 | 25/35 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.520×** | -4.6 | 1e-04 | 26/35 (PANC-1, SK-MEL-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9537. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 381 | 0 | 18 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0444× (z -37.6) |
| [[SNU-423 (line)]] | alt | 78.5 | 11 | 5 (1 ⚠) | [[Betamethasone dipropionate (drug)]] 0.5 µM 6.14× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -15.1) |
| [[J82 (line)]] | alt | 114 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0719× (z -21.1) |
| [[SK-MEL-2 (line)]] | alt | 418 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0405× (z -28.4) |
| [[SW 900 (line)]] | alt | 162 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0676× (z -21.9) |
| [[HEC-1-A (line)]] | alt | 116 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -19.2) |
| [[MIA PaCa-2 (line)]] | alt | 408 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0336× (z -31.3) |
| [[RPMI-7951 (line)]] | alt | 399 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0350× (z -28.8) |
| [[A549 (line)]] | wt | 261 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0481× (z -28.2) |
| [[Hs 766T (line)]] | wt | 223 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0883× (z -23.3) |
| [[A-172 (line)]] | wt | 79.7 | 1 | 7 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.10× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.0973× (z -19.6) |
| [[HOP62 (line)]] | alt | 274 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0750× (z -23.7) |
| [[NCI-H460 (line)]] | wt | 125 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -18.1) |
| [[HS-578T (line)]] | alt | 154 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0721× (z -20.7) |
| [[NCI-H1792 (line)]] | alt | 354 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0662× (z -23.3) |
| [[RKO (line)]] | wt | 103 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -19.1) |
| [[SW 1271 (line)]] | alt | 412 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0482× (z -20.0) |
| [[C32 (line)]] | wt | 48.7 | 0 | 5 | — | [[Harringtonine (drug)]] 5 µM 0.111× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 159 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -17.9) |
| [[NCI-H1573 (line)]] | alt | 160 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0836× (z -23.8) |
| [[CHP-212 (line)]] | wt | 169 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0426× (z -21.5) |
| [[HCT15 (line)]] | alt | 129 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0743× (z -11.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.175× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 114 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -12.4) |
| [[hTERT-HPNE (line)]] | wt | 139 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -15.4) |
| [[NCI-H2030 (line)]] | alt | 242 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -12.1) |
| [[SW 1088 (line)]] | alt | 138 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -10.4) |
| [[A-427 (line)]] | wt | 43.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.123× (z -12.5) ⚠ toxic |
| [[BT-474 (line)]] | alt | 35.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -11.4) |
| [[HepG2_C3A (line)]] | wt | 46.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -13.2) |
| [[A498 (line)]] | wt | 33.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.64× (z +11.0) | — |
| [[KATO III (line)]] | alt | 37.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 63.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.143× (z -9.4) |
| [[AN3 CA (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.18 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 16.6 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 26.1 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 25.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.73 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.69 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.81 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.82 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 11.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9537), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1X]] | +0.80 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[MT2A]] | +0.79 | +0.71 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[TANC2]] | +0.69 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[ERRFI1]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[SERPINE1]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 496 |
| [[GLRX]] | +0.64 | +0.61 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[PHC2]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[ZMYND8]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[HS3ST3B1]] | +0.61 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[SLC45A1]] | +0.60 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[AKAP12]] | +0.59 | +0.60 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[MT1A]] | +0.58 | +0.43 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MATN2]] | -0.58 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[PSG9]] | -0.53 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[NNT]] | -0.50 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[ANKRD30B]] | -0.50 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ADI1]] | -0.48 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[BBOX1-AS1]] | -0.48 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ANKRD18B]] | -0.48 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[TRIML2]] | -0.47 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[PTPRK]] | -0.47 | -0.49 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINE1]] | B | SERPINE1 activity raises ANGPTL4's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 2.94× lower at baseline in the lines without SERPINE1 | 0.031 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[NR3C1]] | B | NR3C1 activity raises ANGPTL4's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |
| [[ITPRIP]] | B | ITPRIP activity raises ANGPTL4's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 2.93× lower at baseline in the lines without ITPRIP | 0.032 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[BIRC3]] | B | BIRC3 activity raises ANGPTL4's level | lines that do not express BIRC3 (5) vs lines expressing it (45) | 3.72× lower at baseline in the lines without BIRC3 | 0.042 | ⚠ within organs, on part of the lines; also absent: LRRC8E, TRIM34, IFI35 |
| [[GAB3]] | B | GAB3 activity raises ANGPTL4's level | lines that do not express GAB3 (17) vs lines expressing it (33) | 3.54× lower at baseline in the lines without GAB3 | 0.054 | ⚠ within organs, on part of the lines; also absent: CACNG6, GNG11, SOGA3 |
| [[GALNT18]] | B | GALNT18 activity strengthens ANGPTL4's drug response | lines that do not express GALNT18 (6) vs lines expressing it (30) | the lines without GALNT18 respond 0.62× as strongly (z diff +1.86); strongest at Homoharringtonine 5 µM: 0.39x vs 0.11x (z diff +3.0) | 0.057 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises ANGPTL4's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ITGA10]] | B | ITGA10 activity raises ANGPTL4's level | lines that do not express ITGA10 (9) vs lines expressing it (41) | 2.99× lower at baseline in the lines without ITGA10 | 0.073 | ⚠ within organs, on part of the lines; also absent: SLC17A7, ZEB1, BOLA3-DT; maybe low, not absent |
| [[FOXC2]] | B | FOXC2 activity raises ANGPTL4's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 2.52× lower at baseline in the lines without FOXC2 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NNT]] | B | ANGPTL4 activity lowers NNT's level | lines that do not express ANGPTL4 (13) vs lines expressing it (37) | 2.16× higher at baseline in the lines without ANGPTL4 | 0.021 | ⚠ within organs, on part of the lines; also absent: CLDN14-AS1, LGALS1, EBI3 |
| [[SDCCAG8]] | B | ANGPTL4 activity raises SDCCAG8's level | lines that do not express ANGPTL4 (13) vs lines expressing it (37) | 1.60× lower at baseline in the lines without ANGPTL4 | 0.067 | ⚠ within organs, on part of the lines; also absent: CLDN14-AS1, LGALS1, EBI3 |
| [[ADAMTS9]] | B | ANGPTL4 activity lowers ADAMTS9's level | lines that do not express ANGPTL4 (13) vs lines expressing it (37) | 1.32× higher at baseline in the lines without ANGPTL4 | 0.074 | ⚠ within organs, on part of the lines; also absent: CLDN14-AS1, LGALS1, EBI3 |
| cells under [[Torkinib (drug)]] 5 µM | B | ANGPTL4 activity lowers the cells' numbers under Torkinib 5 µM (makes them more sensitive) | lines that do not express ANGPTL4 (13) vs lines expressing it (35) | the lines without ANGPTL4: 1.35× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: CLDN14-AS1, LGALS1, EBI3 |
| [[AKAP12]] | B | ANGPTL4 activity raises AKAP12's level | lines that do not express ANGPTL4 (13) vs lines expressing it (37) | 3.64× lower at baseline in the lines without ANGPTL4 | 0.085 | ⚠ within organs, on part of the lines; also absent: CLDN14-AS1, LGALS1, EBI3 |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.5, 11.4); signed map (14.4, 35.4). **Vector** length 138, 48.5% of its response variance represented; |z| ≥ 3 in 1,627 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Metallothioneins bind metals* (reactome, mean cos +0.64 to 5); *metallothionein* (control, mean cos +0.64 to 5); *Response to metal ions* (reactome, mean cos +0.64 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.9 | -3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.6 | -4.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.1 | -6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.9 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +4.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +5.0 | +4.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +5.0 | +4.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +4.9 | +3.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +4.9 | +4.1 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.6 | -2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.6 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -9.0 | -11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.0 | -4.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -7.9 | -9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.7 | -7.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.2 | -6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.6 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.3 | -3.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.7 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | angiopoietin like 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:8,363,289-8,374,370 (+) |
| Ensembl biotype | protein_coding |
| Also known as | pp1158, PGAR, ARP4, HFARP, FIAF, NL2 |
| Gene groups (HGNC) | Fibrinogen C domain containing; Angiopoietin like family |
| Hallmark sets | KRAS_SIGNALING_UP, GLYCOLYSIS, HYPOXIA, ADIPOGENESIS |
| Reactome | 22 pathways, smallest: Assembly of active LPL and LIPC lipase complexes; Regulation of CDH11 function; Plasma lipoprotein remodeling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BY76](https://www.uniprot.org/uniprotkb/Q9BY76) (Angiopoietin-related protein 4):

> Mediates inactivation of the lipoprotein lipase LPL, and thereby plays a role in the regulation of triglyceride clearance from the blood serum and in lipid metabolism. May also play a role in regulating glucose homeostasis and insulin sensitivity (Probable). Inhibits proliferation, migration, and tubule formation of endothelial cells and reduces vascular leakage. Upon heterologous expression, inhibits the adhesion of endothelial cell to the extracellular matrix (ECM), and inhibits the …

**Summary**, from NCBI Gene [51129](https://www.ncbi.nlm.nih.gov/gene/51129):

> This gene encodes a glycosylated, secreted protein containing a C-terminal fibrinogen domain. The encoded protein is induced by peroxisome proliferation activators and functions as a serum hormone that regulates glucose homeostasis, lipid metabolism, and insulin sensitivity. This protein can also act as an apoptosis survival factor for vascular endothelial cells and can prevent metastasis by inhibiting vascular growth and tumor cell invasion. The C-terminal domain may be proteolytically-cleaved …

**Accessions** — [HGNC:16039](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16039) · Entrez [51129](https://www.ncbi.nlm.nih.gov/gene/51129) · UniProt [Q9BY76](https://www.uniprot.org/uniprotkb/Q9BY76) · Ensembl [ENSG00000167772](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167772)

## Data

Gene col 9537: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9537); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9537, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9537]; `tensor/DDL_lfc|DDL_z.npy` [9537]; `embed/gene_vectors.npy` [9537]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9537 or target_col == 9537). Every well: [[ANGPTL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANGPTL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
