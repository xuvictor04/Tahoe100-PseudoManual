---
symbol: "MLXIP"
type: "gene"
col: 10642
ensembl_id: "ENSG00000175727"
name: "MLX interacting protein"
location: "12q21.31"
module: 218
arm: "+"
pooled_cpm: 91.53
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/218"]
generated_by: "tahoemap"
---

# MLXIP

*MLX interacting protein* — 12q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.85× (z +16.5, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.690× (z -14.0, q 7e-42, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUMBL]] (+0.65, fdr 1e-05), [[FARP2]] (+0.64, fdr 7e-06), [[ASL]] (+0.63, fdr 2e-05); moves opposite to [[FAM111A-DT]] (-0.60, fdr 5e-05), [[RAB11FIP2]] (-0.58, fdr 6e-05), [[OSGIN2]] (-0.58, fdr 1e-05).
> It is in [[Module 218]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10642.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +16.5 | 0e+00 | 39/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.75×** | +15.0 | 0e+00 | 40/48 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +13.3 | 3e-38 | 33/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +8.1 | 8e-14 | 31/48 (NCI-H1792, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +6.3 | 3e-08 | 24/48 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +4.6 | 3e-04 | 0/50 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.17× | +4.3 | 0.002 | 21/48 (LoVo, SW48, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.17× | +4.2 | 0.002 | 22/48 (SW480, NCI-H2030, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.16× | +4.0 | 0.004 | 18/48 (NCI-H1573, HT-29, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | 1.15× | +3.7 | 0.013 | 13/48 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 1.14× | +3.5 | 0.023 | 11/48 (Panc 03.27, SNU-1, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.13× | +3.3 | 0.038 | 16/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.13× | +3.2 | 0.059 | 8/48 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | 1.12× | +3.0 | 0.099 | 7/48 (Hs 766T, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10642.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.690×** | -14.0 | 7e-42 | 36/48 (HOP62, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.722×** | -8.7 | 1e-15 | 35/48 (AsPC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.756×** | -6.9 | 1e-09 | 28/45 (J82, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.768×** | -6.8 | 2e-09 | 25/42 (LOX-IMVI, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.783×** | -6.5 | 8e-09 | 25/48 (A-172, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.851× | -6.1 | 1e-07 | 18/48 (HOP62, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.797×** | -6.1 | 1e-07 | 26/48 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.802×** | -5.9 | 3e-07 | 23/49 (COLO 205, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.797×** | -5.8 | 4e-07 | 23/50 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.860× | -5.7 | 8e-07 | 22/49 (A-172, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.878× | -4.9 | 5e-05 | 14/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.823×** | -4.8 | 8e-05 | 21/47 (A-172, C-33 A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.749×** | -4.0 | 0.003 | 18/47 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.862× | -4.0 | 0.003 | 15/48 (A-172, C32, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.872× | -3.9 | 0.004 | 15/50 (NCI-H596, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.879× | -3.4 | 0.019 | 15/48 (H4, HepG2/C3A, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.879× | -3.2 | 0.045 | 11/48 (RKO, PANC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.903× | -3.1 | 0.058 | 13/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.907× | -3.0 | 0.067 | 11/48 (RKO, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10642. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 189 | 0 | 16 (12 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.393× (z -14.3) |
| [[A-172 (line)]] | wt | 195 | 0 | 15 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -23.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.168× (z -19.8) |
| [[LOX-IMVI (line)]] | wt | 140 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 117 | 3 (1 ⚠) | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.19× (z +10.0) | [[Selinexor (drug)]] 5 µM 0.539× (z -11.2) |
| [[J82 (line)]] | alt | 95.8 | 2 | 3 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.07× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.266× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.606× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 53.8 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.35× (z +9.8) | [[Selinexor (drug)]] 5 µM 0.589× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 133 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -13.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 60.2 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.30× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.366× (z -10.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 161 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 114 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.561× (z -10.4) |
| [[RKO (line)]] | wt | 144 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -15.1) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.399× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 143 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -10.5) |
| [[SW1417 (line)]] | alt | 66.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.38× (z +10.4) | — |
| [[SW480 (line)]] | alt | 68.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.36× (z +12.3) | — |
| [[A-427 (line)]] | wt | 55.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -17.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 138 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.05× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.425× (z -10.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 59.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.89× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 44.2 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.101× (z -11.1) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 59.7 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.52× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 75.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.417× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 28.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 65.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.01× (z +8.5) | — |
| [[NCI-H596 (line)]] | alt | 94.6 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.344× (z -9.2) |
| [[PANC-1 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 55.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.509× (z -8.5) |
| [[SNU-423 (line)]] | alt | 72.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.24× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 75.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.293× (z -11.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 70.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 93.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 88.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10642), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUMBL]] | +0.65 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[FARP2]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ASL]] | +0.63 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[SH2B2]] | +0.63 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[CCNQ]] | +0.62 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[NPHP4]] | +0.61 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[CLTCL1]] | +0.60 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[SLC66A2]] | +0.60 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[MYO9B]] | +0.59 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[OGG1]] | +0.59 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[TBC1D16]] | +0.57 | +0.40 / +0.44 | both halves | 4e-05 |  |
| [[RHBDF2]] | +0.57 | +0.48 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM111A-DT]] | -0.60 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[RAB11FIP2]] | -0.58 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[OSGIN2]] | -0.58 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[CISD2]] | -0.58 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[MR1]] | -0.58 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[RWDD2B]] | -0.57 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[DECR1]] | -0.53 | -0.47 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[OGFRL1]] | -0.53 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[TLR1]] | -0.53 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[CASC9]] | -0.52 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[PAXIP1-AS2]] | -0.52 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[VBP1]] | -0.52 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[TBCEL]] | -0.52 | -0.44 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MLXIP's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CPNE8]] | B | CPNE8 activity lowers MLXIP's level | lines that do not express CPNE8 (17) vs lines expressing it (33) | 1.33× higher at baseline in the lines without CPNE8 | 0.099 | ⚠ within organs, on part of the lines; also absent: NALCN, NT5E, MAP9 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 218]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.761). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (4.6, 2.9); signed map (-26.9, 17.1). **Vector** length 124, 33.3% of its response variance represented; |z| ≥ 3 in 1,297 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.9 | +15.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.6 | +16.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.7 | +8.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.6 | +13.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.1 | +2.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.9 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +2.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.7 | +2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +2.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -11.0 | -14.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -7.6 | -8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.3 | -6.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -5.7 | -5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.4 | -6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.7 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | MLX interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.31 — chr12:122,078,756-122,147,344 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MONDOA, KIAA0867, MIR, bHLHe36 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAP2](https://www.uniprot.org/uniprotkb/Q9HAP2) (MLX-interacting protein):

> Binds DNA as a heterodimer with MLX and activates transcription. Binds to the canonical E box sequence 5'-CACGTG-3'. Plays a role in transcriptional activation of glycolytic target genes. Involved in glucose-responsive gene regulation.

**Summary**, from NCBI Gene [22877](https://www.ncbi.nlm.nih.gov/gene/22877):

> This gene encodes a protein that functions as part of a heterodimer to activate transcription. The encoded protein forms a heterodimer with Max-like protein X (MLX) and is involved in the regulation of genes in response to cellular glucose levels. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:17055](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17055) · Entrez [22877](https://www.ncbi.nlm.nih.gov/gene/22877) · UniProt [Q9HAP2](https://www.uniprot.org/uniprotkb/Q9HAP2) · Ensembl [ENSG00000175727](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175727)

## Data

Gene col 10642: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10642); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10642, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10642]; `tensor/DDL_lfc|DDL_z.npy` [10642]; `embed/gene_vectors.npy` [10642]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10642 or target_col == 10642). Every well: [[MLXIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MLXIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
