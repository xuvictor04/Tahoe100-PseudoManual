---
symbol: "RBSN"
type: "gene"
col: 5202
ensembl_id: "ENSG00000131381"
name: "rabenosyn, RAB effector"
location: "3p25.1"
module: 64
arm: "+"
pooled_cpm: 37.02
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# RBSN

*rabenosyn, RAB effector* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.72× (z +14.0, q 6e-42, up in 42 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.507× (z -25.7, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CINP]] (+0.73, fdr 7e-06), [[C19orf44]] (+0.72, fdr 7e-06), [[ZNF329]] (+0.71, fdr 7e-06); moves opposite to [[EPB41L2]] (-0.68, fdr 7e-06), [[GLS]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5202.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.72×** | +14.0 | 6e-42 | 42/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +9.7 | 1e-19 | 28/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +9.2 | 8e-18 | 30/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +7.9 | 4e-13 | 30/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +7.9 | 4e-13 | 29/48 (NCI-H2030, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.28×** | +6.3 | 3e-08 | 21/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +6.0 | 2e-07 | 27/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.16× | +5.8 | 5e-07 | 15/48 (Hs 766T, RPMI-7951, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.49×** | +5.6 | 1e-06 | 17/48 (NCI-H2030, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +5.0 | 3e-05 | 17/48 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.4 | 6e-04 | 18/48 (SHP-77, NCI-H1573, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.6 | 0.016 | 12/48 (SW1417, SW48, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.067 | 4/47 (HCT15, H4, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.08× | +3.1 | 0.080 | 0/48 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5202.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.507×** | -25.7 | 0e+00 | 42/48 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.561×** | -15.5 | 0e+00 | 40/47 (SW480, C32, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.566×** | -14.7 | 0e+00 | 41/48 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.580×** | -14.0 | 2e-42 | 36/48 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.587×** | -13.7 | 7e-41 | 26/39 (LS 180, HCT15, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.589×** | -13.1 | 2e-37 | 31/45 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.782×** | -9.3 | 1e-18 | 31/48 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.809×** | -8.0 | 8e-14 | 23/48 (HOP62, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 0.840× | -4.6 | 2e-04 | 22/48 (KATO III, A-172, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | 0.845× | -4.5 | 4e-04 | 18/48 (A-172, SW1417, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.849× | -4.4 | 6e-04 | 17/48 (SW 1088, HOP62, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.850× | -4.2 | 0.001 | 15/48 (COLO 205, LS 180, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 0.860× | -4.0 | 0.002 | 16/48 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | 0.888× | -3.0 | 0.091 | 16/47 (A-172, HOP62, …) | top dose only |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.893× | -3.0 | 0.091 | 4/48 (COLO 205, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5202. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 51.8 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -19.6) |
| [[HOP62 (line)]] | alt | 51.4 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 34.4 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -24.0) |
| [[SW480 (line)]] | alt | 40.3 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.442× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 47.7 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -13.4) |
| [[C32 (line)]] | wt | 33.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -11.7) |
| [[HCT15 (line)]] | alt | 49.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Alpelisib (drug)]] 5 µM 0.106× (z -8.5) |
| [[Hs 766T (line)]] | wt | 32.8 | 1 (1 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.94× (z +8.5) ⚠ cell-cycle shift, explains ~14% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -14.2) |
| [[HS-578T (line)]] | alt | 40.8 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -13.9) |
| [[LoVo (line)]] | wt | 27.2 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.25× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -9.4) |
| [[LS 180 (line)]] | wt | 31.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -10.1) |
| [[RKO (line)]] | wt | 45.4 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -11.9) |
| [[SNU-423 (line)]] | alt | 44.8 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -17.2) |
| [[SW 900 (line)]] | alt | 31.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.8) |
| [[SW1417 (line)]] | alt | 49.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -14.5) |
| [[A498 (line)]] | wt | 28.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -15.7) |
| [[A549 (line)]] | wt | 37.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 23.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -11.6) |
| [[H4 (line)]] | wt | 46.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -12.9) |
| [[hTERT-HPNE (line)]] | wt | 38.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 57.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -13.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 30.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 49.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -13.6) |
| [[SHP-77 (line)]] | alt | 36.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -10.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 38.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -12.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 23.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 51.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -10.9) |
| [[J82 (line)]] | alt | 41.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -8.9) |
| [[KATO III (line)]] | alt | 38.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -10.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 34.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -19.5) |
| [[Panc 03.27 (line)]] | alt | 40.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -14.6) |
| [[SNU-1 (line)]] | wt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -9.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -9.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 75.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5202), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CINP]] | +0.73 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[C19orf44]] | +0.72 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[ZNF329]] | +0.71 | +0.74 / +0.60 | both halves | 7e-06 | same gene group |
| [[VIRMA]] | +0.70 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[BRF2]] | +0.70 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[NMT1]] | +0.69 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[TTF1]] | +0.68 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[ZNF205]] | +0.67 | +0.60 / +0.68 | both halves | 7e-06 | same gene group |
| [[CCDC43]] | +0.67 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[ZFP37]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 | same gene group |
| [[ZNF426]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 | same gene group |
| [[ASB8]] | +0.66 | +0.64 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L2]] | -0.68 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[GLS]] | -0.62 | -0.60 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RBSN's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 1.7% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity raises RBSN's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-39.4, -4.7); signed map (-15.0, -16.3). **Vector** length 89.9, 18.9% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.4 | +14.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.2 | +1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.7 | +7.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +4.3 | +5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +9.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +5.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +2.1 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -14.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.3 | -14.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -25.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -9.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | -3.6 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -8.0 |
|  | [[Auranofin (drug)]] 0.5 µM |  | -1.4 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -0.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | rabenosyn, RAB effector |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:15,070,073-15,099,163 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ZFYVE20 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Zinc fingers FYVE-type |
| Hallmark sets | COMPLEMENT |
| Reactome | 5 pathways, smallest: Toll Like Receptor 9 (TLR9) Cascade; Factors involved in megakaryocyte development and platelet production; Toll-like Receptor Cascades |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1K0](https://www.uniprot.org/uniprotkb/Q9H1K0) (Rabenosyn-5):

> Rab4/Rab5 effector protein acting in early endocytic membrane fusion and membrane trafficking of recycling endosomes. Required for endosome fusion either homotypically or with clathrin coated vesicles. Plays a role in the lysosomal trafficking of CTSD/cathepsin D from the Golgi to lysosomes. Also promotes the recycling of transferrin directly from early endosomes to the plasma membrane. Binds phospholipid vesicles containing phosphatidylinositol 3-phosphate (PtdInsP3). Plays a role in the …

**Summary**, from NCBI Gene [64145](https://www.ncbi.nlm.nih.gov/gene/64145):

> This gene encodes a protein that belongs to the FYVE zinc finger family of proteins. The encoded protein interacts with Ras-related proteins that regulate membrane trafficking. A missense mutation in this gene is associated with a defect in the early endocytic pathway. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2014]

**Accessions** — [HGNC:20759](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20759) · Entrez [64145](https://www.ncbi.nlm.nih.gov/gene/64145) · UniProt [Q9H1K0](https://www.uniprot.org/uniprotkb/Q9H1K0) · Ensembl [ENSG00000131381](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131381)

## Data

Gene col 5202: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5202); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5202, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5202]; `tensor/DDL_lfc|DDL_z.npy` [5202]; `embed/gene_vectors.npy` [5202]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5202 or target_col == 5202). Every well: [[RBSN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBSN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
