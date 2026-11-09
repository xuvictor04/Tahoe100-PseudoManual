---
symbol: "MYOM1"
type: "gene"
col: 2157
ensembl_id: "ENSG00000101605"
name: "myomesin 1"
location: "18p11.31"
module: 47
arm: "+"
pooled_cpm: 15.8
n_lines_expressing: 41
n_dd_up: 16
n_dd_down: 23
n_dd_up_clean: 13
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# MYOM1

*myomesin 1* — 18p11.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.05× (z +14.0, q 9e-42, up in 28 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.370× (z -13.6, q 1e-39, down in 32 of 38 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYADM-AS1]] (+0.64, fdr 1e-05), [[ERRFI1-DT]] (+0.55, fdr 3e-05), [[FBXO27]] (+0.54, fdr 2e-05); moves opposite to [[NEK4]] (-0.44, fdr 4e-04), [[GFM1]] (-0.43, fdr 5e-04), [[RUFY1]] (-0.42, fdr 2e-04).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ERRFI1-DT]] → it (grade B ⚠); 6 go from it, the strongest it → [[PYGM]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2157.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +14.0 | 9e-42 | 28/36 (HOP62, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.90×** | +12.5 | 2e-33 | 27/37 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +7.3 | 6e-11 | 19/38 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +6.3 | 5e-08 | 13/35 (HOP62, Hs 766T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +6.2 | 8e-08 | 14/37 (BT-474, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.48×** | +5.4 | 5e-06 | 22/36 (NCI-H1573, A-427, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.7 | 2e-04 | 13/34 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +4.3 | 0.001 | 14/38 (HOP62, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.003 | 14/36 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.004 | 13/38 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +3.9 | 0.004 | 12/38 (KATO III, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.38×** | +3.8 | 0.006 | 6/36 (HS-578T, CFPAC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.011 | 12/38 (HOP62, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +3.6 | 0.013 | 4/18 (HEC-1-A, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.28×** | +3.4 | 0.024 | 6/38 (HT-29, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +3.2 | 0.042 | 3/37 (HOP62, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2157.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.370×** | -13.6 | 1e-39 | 32/38 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.378×** | -13.4 | 2e-38 | 31/38 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.402×** | -12.5 | 1e-33 | 30/35 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.407×** | -12.3 | 8e-33 | 29/37 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.505×** | -9.4 | 6e-19 | 24/36 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.499×** | -9.2 | 4e-18 | 23/38 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.633×** | -8.9 | 5e-17 | 20/37 (A-427, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.525×** | -8.5 | 1e-15 | 24/31 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.612×** | -6.7 | 1e-09 | 25/38 (SW 900, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.462×** | -5.5 | 2e-06 | 16/34 (A-427, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.671×** | -5.5 | 2e-06 | 10/38 (A-427, NCI-H23, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.663×** | -5.4 | 3e-06 | 17/32 (NCI-H23, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.642×** | -5.3 | 5e-06 | 17/37 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.690×** | -5.1 | 1e-05 | 19/37 (A-427, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.719×** | -4.3 | 7e-04 | 15/35 (HepG2/C3A, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.702×** | -4.2 | 8e-04 | 15/38 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.735×** | -4.2 | 8e-04 | 18/38 (SNU-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.664×** | -4.0 | 0.002 | 5/38 (NCI-H23, HT-29, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.583×** | -3.9 | 0.003 | 18/37 (A-427, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.765×** | -3.7 | 0.007 | 12/38 (SW480, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2157. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 103 | 0 | 14 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.00831× (z -38.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0837× (z -20.0) |
| [[A-427 (line)]] | wt | 112 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -19.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.158× (z -16.5) |
| [[NCI-H1573 (line)]] | alt | 42.5 | 1 | 8 (3 ⚠) | [[Selinexor (drug)]] 5 µM 3.11× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0861× (z -15.3) |
| [[SHP-77 (line)]] | alt | 27.2 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -13.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.157× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 28.2 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.192× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.210× (z -10.8) |
| [[PANC-1 (line)]] | alt | 14.0 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 24.2 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0972× (z -13.2) |
| [[HOP62 (line)]] | alt | 16.0 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.235× (z -9.0) |
| [[HT-29 (line)]] | alt | 15.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0932× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.149× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 16.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.164× (z -9.7) |
| [[SW480 (line)]] | alt | 9.92 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.0922× (z -15.1) |
| [[A549 (line)]] | wt | 7.55 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -9.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[AsPC-1 (line)]] | alt | 19.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -15.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.236× (z -8.7) |
| [[Hs 766T (line)]] | wt | 9.21 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.41× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.132× (z -8.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 48.7 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.18× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 3.96 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.107× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 25.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0968× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 12.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 9.99× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0735× (z -9.3) |
| [[A-172 (line)]] | wt | 3.56 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.44 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2157), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYADM-AS1]] | +0.64 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[ERRFI1-DT]] | +0.55 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[FBXO27]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[NOS1]] | +0.52 | +0.50 / +0.42 | both halves | 4e-05 | pathway: HALLMARK_MYOGENESIS |
| [[SDAD1P1]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[RERE]] | +0.51 | +0.36 / +0.59 | both halves | 9e-05 |  |
| [[ATP13A3-DT]] | +0.51 | +0.36 / +0.47 | both halves | 9e-05 |  |
| [[ITGA2-AS1]] | +0.51 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[TM4SF1-AS1]] | +0.50 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[XG]] | +0.50 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[BLZF2P]] | +0.50 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[HPN]] | +0.49 | +0.45 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEK4]] | -0.44 | -0.24 / -0.49 | both halves | 4e-04 |  |
| [[GFM1]] | -0.43 | -0.23 / -0.53 | both halves | 5e-04 |  |
| [[RUFY1]] | -0.42 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[TADA2A]] | -0.42 | -0.29 / -0.51 | both halves | 3e-04 |  |
| [[PDIK1L]] | -0.42 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[C12orf4]] | -0.42 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[CIAO3]] | -0.42 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[NSL1]] | -0.41 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[NDUFA9]] | -0.41 | -0.39 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERRFI1-DT]] | B | ERRFI1-DT activity raises MYOM1's level | lines that do not express ERRFI1-DT (13) vs lines expressing it (37) | 2.03× lower at baseline in the lines without ERRFI1-DT | 0.066 | ⚠ within organs, on part of the lines; also absent: GCAWKR; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MYOM1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAGEA4]], [[MAGEA4-AS1]] | B | MAGEA4, MAGEA4-AS1 activity raises MYOM1's level | lines that do not express MAGEA4, MAGEA4-AS1 (41) vs lines expressing them (9) | 2.69× lower at baseline in the lines without MAGEA4, MAGEA4-AS1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, GCG; co-absent genes |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PYGM]] | B | MYOM1 activity raises PYGM's level | lines that do not express MYOM1 (9) vs lines expressing it (41) | 1.50× lower at baseline in the lines without MYOM1 | 0.005 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TRIM72]] | B | MYOM1 activity raises TRIM72's level | lines that do not express MYOM1 (9) vs lines expressing it (41) | 1.63× lower at baseline in the lines without MYOM1 | 0.022 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SAXO1]] | B | MYOM1 activity raises SAXO1's level | lines that do not express MYOM1 (9) vs lines expressing it (41) | 1.21× lower at baseline in the lines without MYOM1 | 0.042 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[USP50]] | B | MYOM1 activity raises USP50's level | lines that do not express MYOM1 (9) vs lines expressing it (41) | 1.29× lower at baseline in the lines without MYOM1 | 0.055 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FNDC7]] | B | MYOM1 activity raises FNDC7's level | lines that do not express MYOM1 (9) vs lines expressing it (41) | 1.48× lower at baseline in the lines without MYOM1 | 0.066 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ASGR1]] | B | MYOM1 activity raises ASGR1's level | lines that do not express MYOM1 (9) vs lines expressing it (41) | 1.65× lower at baseline in the lines without MYOM1 | 0.067 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.418). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.7, -6.4); signed map (16.6, 19.8). **Vector** length 74.6, 14.5% of its response variance represented; |z| ≥ 3 in 974 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +14.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.0 | +12.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +6.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.2 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | -0.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +7.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.6 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -13.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.4 | -8.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -13.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.4 | -12.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -5.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | +1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -1.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | myomesin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.31 — chr18:3,066,807-3,219,968 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | I-set domain containing; Myosin binding proteins |
| Hallmark sets | MYOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [P52179](https://www.uniprot.org/uniprotkb/P52179) (Myomesin-1):

> Major component of the vertebrate myofibrillar M band. Binds myosin, titin, and light meromyosin. This binding is dose dependent.

**Summary**, from NCBI Gene [8736](https://www.ncbi.nlm.nih.gov/gene/8736):

> The giant protein titin, together with its associated proteins, interconnects the major structure of sarcomeres, the M bands and Z discs. The C-terminal end of the titin string extends into the M line, where it binds tightly to M-band constituents of apparent molecular masses of 190 kD (myomesin 1) and 165 kD (myomesin 2). This protein, myomesin 1, like myomesin 2, titin, and other myofibrillar proteins contains structural modules with strong homology to either fibronectin type III (motif I) or …

**Accessions** — [HGNC:7613](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7613) · Entrez [8736](https://www.ncbi.nlm.nih.gov/gene/8736) · UniProt [P52179](https://www.uniprot.org/uniprotkb/P52179) · Ensembl [ENSG00000101605](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101605)

## Data

Gene col 2157: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2157); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2157, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2157]; `tensor/DDL_lfc|DDL_z.npy` [2157]; `embed/gene_vectors.npy` [2157]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2157 or target_col == 2157). Every well: [[MYOM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYOM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
