---
symbol: "PILRB"
type: "gene"
col: 4289
ensembl_id: "ENSG00000121716"
name: "paired immunoglobin like type 2 receptor beta"
location: "7q22.1"
module: 29
arm: "-"
pooled_cpm: 56.83
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PILRB

*paired immunoglobin like type 2 receptor beta* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.63× (z +15.3, q 0e+00, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.667× (z -12.6, q 2e-33, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STAG3L5P-1]] (+0.71, fdr 7e-06, ⚠ same locus), [[NUP98]] (+0.65, fdr 1e-05), [[MAP3K14]] (+0.60, fdr 1e-05), [[DDX19A]] (+0.57, fdr 1e-05); moves opposite to [[STRADB]] (-0.63, fdr 1e-05), [[MSL3]] (-0.62, fdr 1e-05), [[DERA]] (-0.59, fdr 6e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4289.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +15.3 | 0e+00 | 37/48 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +12.6 | 5e-34 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +9.7 | 4e-20 | 37/48 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +9.1 | 2e-17 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +8.0 | 1e-13 | 33/48 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +6.5 | 7e-09 | 26/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +5.6 | 2e-06 | 23/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.55×** | +5.0 | 3e-05 | 23/48 (SK-MEL-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +4.8 | 9e-05 | 21/48 (NCI-H460, A-172, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +4.8 | 1e-04 | 20/48 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.20× | +4.0 | 0.003 | 20/48 (NCI-H460, HEC-1-A, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.20× | +4.0 | 0.003 | 18/48 (NCI-H460, A-172, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.004 | 13/48 (SW480, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.007 | 13/49 (NCI-H23, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +3.6 | 0.014 | 13/49 (KATO III, HOP62, …) | top dose only |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.086 | 8/48 (SW1417, AsPC-1, …) | rises with dose | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4289.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -12.6 | 2e-33 | 42/48 (A498, H4, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.615×** | -10.7 | 3e-24 | 32/49 (RKO, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.672×** | -8.2 | 7e-14 | 31/47 (A-427, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.675×** | -8.0 | 1e-13 | 27/42 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.647×** | -6.4 | 1e-08 | 28/45 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.854× | -4.9 | 9e-05 | 19/48 (J82, SNU-423, …) | top dose only | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.791×** | -4.8 | 1e-04 | 21/48 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.796×** | -4.7 | 2e-04 | 25/49 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.820×** | -4.3 | 9e-04 | 23/48 (NCI-H2030, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.819×** | -4.1 | 0.002 | 19/48 (PANC-1, J82, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 0.839× | -3.9 | 0.006 | 14/48 (SW1417, Hs 766T, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.839× | -3.6 | 0.016 | 21/47 (NCI-H23, RKO, …) | top dose only |  |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.850× | -3.6 | 0.017 | 16/48 (A549, AN3 CA, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.857× | -3.4 | 0.027 | 12/49 (SW 1088, CHP-212, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.847× | -3.4 | 0.027 | 12/48 (SNU-1, MIA PaCa-2, …) | rises with dose |  |
| [[Cyclosporin A (drug)]] 0.5 µM |  | 0.870× | -3.1 | 0.073 | 11/48 (AsPC-1, SNU-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4289. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 55.0 | 11 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +24.6) | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -8.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 63.5 | 4 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.17× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.465× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.661× (z -8.5) |
| [[C32 (line)]] | wt | 88.0 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +16.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.327× (z -10.0) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -8.5) |
| [[PANC-1 (line)]] | alt | 75.2 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.496× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -9.4) |
| [[RKO (line)]] | wt | 64.5 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -12.3) |
| [[A-172 (line)]] | wt | 45.4 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -9.9) |
| [[A498 (line)]] | wt | 92.1 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -16.6) |
| [[J82 (line)]] | alt | 46.9 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -12.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 56.7 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.268× (z -11.0) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -9.7) |
| [[H4 (line)]] | wt | 71.1 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -12.3) |
| [[Hs 766T (line)]] | wt | 45.9 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.77× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 90.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 99.1 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.68× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -9.1) |
| [[A549 (line)]] | wt | 52.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -10.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 45.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.41× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 49.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -17.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 51.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +20.3) | — |
| [[BT-474 (line)]] | alt | 68.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.4) | — |
| [[CFPAC-1 (line)]] | alt | 36.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.9) | — |
| [[CHP-212 (line)]] | wt | 48.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 61.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 51.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -8.7) |
| [[HT-29 (line)]] | alt | 67.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -12.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 62.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.438× (z -10.0) ⚠ toxic |
| [[LS 180 (line)]] | wt | 51.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +12.7) | — |
| [[RPMI-7951 (line)]] | alt | 48.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 44.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.273× (z -10.3) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 69.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4289), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAG3L5P-1]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 | ⚠ same locus (0.3 kb, same strand: neighbours can correlate without regulation) |
| [[NUP98]] | +0.65 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[MAP3K14]] | +0.60 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[DDX19A]] | +0.57 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[TRAF2]] | +0.56 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[GGA1]] | +0.56 | +0.36 / +0.51 | both halves | 9e-05 |  |
| [[MIDN]] | +0.56 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[POLR2J4]] | +0.55 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[MAP2K7]] | +0.55 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[OPA3]] | +0.55 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[SLC35C2]] | +0.55 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[KIF20B]] | +0.55 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[ENDOV]] | +0.54 | +0.51 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRADB]] | -0.63 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[MSL3]] | -0.62 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[DERA]] | -0.59 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[VPS26A]] | -0.55 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[PGRMC1]] | -0.55 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[USF1]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[TWF1]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[SCARB2]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[UHMK1]] | -0.53 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[ANP32A]] | -0.52 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[RAB21]] | -0.52 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[RPL6]] | -0.52 | -0.45 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PILRB's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | PILRB's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | PILRB's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.57 | 0.511 over the table, 0.096 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-45.9, -53.1); signed map (-50.8, -35.8). **Vector** length 119, 32.4% of its response variance represented; |z| ≥ 3 in 979 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +15.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.4 | +9.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.3 | +3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +9.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.6 | +4.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.3 | +5.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | +3.6 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | +2.2 | +1.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.1 | -12.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -4.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -4.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -6.1 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.7 | -6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.4 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | paired immunoglobin like type 2 receptor beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,352,176-100,367,831 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FDFACT1, FDFACT2 |
| Gene groups (HGNC) | V-set domain containing |
| Reactome | 2 pathways, smallest: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKJ0](https://www.uniprot.org/uniprotkb/Q9UKJ0) (Paired immunoglobulin-like type 2 receptor beta):

> Paired receptors consist of highly related activating and inhibitory receptors and are widely involved in the regulation of the immune system. PILRB is thought to act as a cellular signaling activating receptor that associates with ITAM-bearing adapter molecules on the cell surface.

**Summary**, from NCBI Gene [29990](https://www.ncbi.nlm.nih.gov/gene/29990):

> The paired immunoglobin-like type 2 receptors consist of highly related activating and inhibitory receptors that are involved in the regulation of many aspects of the immune system. The paired immunoglobulin-like receptor genes are located in a tandem head-to-tail orientation on chromosome 7. This gene encodes the activating member of the receptor pair and contains a truncated cytoplasmic tail relative to its inhibitory counterpart (PILRA), that has a long cytoplasmic tail with immunoreceptor …

**Accessions** — [HGNC:18297](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18297) · Entrez [29990](https://www.ncbi.nlm.nih.gov/gene/29990) · UniProt [Q9UKJ0](https://www.uniprot.org/uniprotkb/Q9UKJ0) · Ensembl [ENSG00000121716](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121716)

## Data

Gene col 4289: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4289); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4289, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4289]; `tensor/DDL_lfc|DDL_z.npy` [4289]; `embed/gene_vectors.npy` [4289]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4289 or target_col == 4289). Every well: [[PILRB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PILRB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
