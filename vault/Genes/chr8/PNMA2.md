---
symbol: "PNMA2"
type: "gene"
col: 14247
ensembl_id: "ENSG00000240694"
name: "PNMA family member 2"
location: "8p21.2"
module: 34
arm: "+"
pooled_cpm: 17.96
n_lines_expressing: 34
n_dd_up: 17
n_dd_down: 34
n_dd_up_clean: 9
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PNMA2

*PNMA family member 2* — 8p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.18× (z +8.5, q 8e-15, up in 11 of 32 measured lines) ⚠ position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.66× (z +7.6, q 7e-12, up in 25 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.188× (z -35.5, q 0e+00, down in 29 of 31 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPYSL2]] (+0.56, fdr 3e-05, ⚠ same locus), [[FAM107B]] (+0.54, fdr 2e-05), [[IL17RD]] (+0.53, fdr 3e-05), [[SLC35F3]] (+0.53, fdr 4e-05); moves opposite to [[CEBPD]] (-0.47, fdr 4e-05), [[SNX13]] (-0.47, fdr 2e-04), [[LUC7L2]] (-0.46, fdr 1e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SEPTIN3]] → it (grade B ⚠); 5 go from it, the strongest it → [[CAPN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14247.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +8.5 | 8e-15 | 11/32 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +8.3 | 2e-14 | 12/21 (A498, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +7.6 | 7e-12 | 25/31 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +6.8 | 2e-09 | 19/32 (NCI-H460, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.26×** | +5.0 | 8e-05 | 16/32 (HOP62, A498, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +4.6 | 4e-04 | 11/28 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +4.3 | 0.001 | 14/26 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +4.3 | 0.001 | 14/31 (MIA PaCa-2, NCI-H1792, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.35×** | +4.3 | 0.001 | 11/30 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.32×** | +4.1 | 0.002 | 10/31 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.31×** | +4.1 | 0.002 | 8/31 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.9 | 0.005 | 8/32 (A498, NCI-H2030, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.014 | 7/31 (AsPC-1, C-33 A, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.27×** | +3.5 | 0.016 | 6/29 (A549, MIA PaCa-2, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.018 | 8/29 (NCI-H23, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.083 | 10/31 (PANC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.090 | 6/31 (HS-578T, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14247.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.188×** | -35.5 | 0e+00 | 29/31 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.147×** | -27.7 | 0e+00 | 29/31 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.257×** | -20.4 | 0e+00 | 27/30 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.338×** | -16.3 | 0e+00 | 26/29 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.354×** | -15.6 | 0e+00 | 30/31 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.511×** | -14.2 | 4e-44 | 26/31 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.439×** | -12.4 | 3e-33 | 21/31 (AsPC-1, PANC-1, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.449×** | -12.0 | 2e-31 | 27/31 (LoVo, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.455×** | -11.8 | 2e-30 | 26/31 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.459×** | -11.7 | 8e-30 | 27/31 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.468×** | -11.4 | 2e-28 | 25/31 (AsPC-1, MIA PaCa-2, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.496×** | -10.5 | 3e-24 | 27/30 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.542×** | -9.2 | 2e-18 | 21/31 (AsPC-1, PANC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.344×** | -8.4 | 2e-15 | 24/31 (AsPC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.386×** | -7.5 | 3e-12 | 26/29 (LoVo, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.610×** | -7.4 | 4e-12 | 19/31 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.641×** | -6.3 | 1e-08 | 21/29 (A549, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.479×** | -5.8 | 2e-07 | 19/32 (LoVo, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14247. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 59.5 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0287× (z -38.2) |
| [[LoVo (line)]] | wt | 22.9 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0990× (z -24.9) |
| [[AsPC-1 (line)]] | alt | 56.4 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0187× (z -39.8) |
| [[MIA PaCa-2 (line)]] | alt | 47.3 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0780× (z -19.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -17.5) |
| [[PANC-1 (line)]] | alt | 36.2 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0546× (z -40.1) |
| [[C-33 A (line)]] | alt | 43.9 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0890× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.299× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 28.8 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0338× (z -30.3) |
| [[SW480 (line)]] | alt | 11.6 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -19.9) |
| [[A549 (line)]] | wt | 32.4 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0305× (z -36.0) |
| [[CFPAC-1 (line)]] | alt | 23.7 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0497× (z -27.1) |
| [[NCI-H460 (line)]] | wt | 4.99 | 1 | 6 (3 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 5.48× (z +8.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.0339× (z -17.1) |
| [[A-172 (line)]] | wt | 37.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0836× (z -30.1) |
| [[A-427 (line)]] | wt | 23.6 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0390× (z -19.3) |
| [[Hs 766T (line)]] | wt | 57.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0513× (z -27.1) |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0485× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.126× (z -14.6) |
| [[NCI-H2030 (line)]] | alt | 24.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0778× (z -25.9) |
| [[NCI-H2347 (line)]] | alt | 29.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0626× (z -31.8) |
| [[HCT15 (line)]] | alt | 21.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -12.9) |
| [[J82 (line)]] | alt | 15.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -19.6) |
| [[A498 (line)]] | wt | 13.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -13.9) |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 8.60 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0509× (z -12.8) |
| [[SNU-423 (line)]] | alt | 9.63 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0808× (z -17.1) |
| [[SW 900 (line)]] | alt | 8.82 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -9.9) |
| [[HOP62 (line)]] | alt | 7.18 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -8.8) |
| [[RKO (line)]] | wt | 5.22 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0672× (z -9.7) |
| [[AN3 CA (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.89 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.01 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14247), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPYSL2]] | +0.56 | +0.66 / +0.46 | both halves | 3e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[FAM107B]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[IL17RD]] | +0.53 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[SLC35F3]] | +0.53 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[ZNF185]] | +0.52 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[WNT7B]] | +0.51 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[FBXO27]] | +0.51 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[CEP295NL]] | +0.50 | +0.33 / +0.46 | both halves | 1e-04 |  |
| [[WNT7A]] | +0.50 | +0.51 / +0.39 | both halves | 6e-05 |  |
| [[PAQR5]] | +0.50 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[CDCP1]] | +0.49 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[FHL1]] | +0.49 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[OSBPL3]] | +0.49 | +0.41 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEBPD]] | -0.47 | -0.40 / -0.52 | both halves | 4e-05 |  |
| [[SNX13]] | -0.47 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[LUC7L2]] | -0.46 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[DYNC2I1]] | -0.45 | -0.32 / -0.44 | both halves | 1e-04 |  |
| [[PWWP2A]] | -0.45 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[RBM5]] | -0.45 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[SRSF4]] | -0.44 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[HMGXB4]] | -0.44 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[FBXO6]] | -0.43 | -0.16 / -0.40 | ⚠ not reproduced | 0.001 |  |
| [[ATAD2B]] | -0.43 | -0.29 / -0.53 | both halves | 2e-04 |  |
| [[GTF2IRD2B]] | -0.43 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[ASH1L]] | -0.42 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[SREK1]] | -0.41 | -0.41 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEPTIN3]] | B | SEPTIN3 activity raises PNMA2's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 2.87× lower at baseline in the lines without SEPTIN3 | 0.066 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAPN2]] | B | PNMA2 activity raises CAPN2's level | lines that do not express PNMA2 (16) vs lines expressing it (34) | 1.60× lower at baseline in the lines without PNMA2 | 0.055 | ⚠ within organs, on part of the lines; also absent: MCOLN3, CACNG6, SELENOM |
| [[ULBP3]] | B | PNMA2 activity raises ULBP3's level | lines that do not express PNMA2 (16) vs lines expressing it (34) | 1.32× lower at baseline in the lines without PNMA2 | 0.086 | ⚠ within organs, on part of the lines; also absent: MCOLN3, CACNG6, SELENOM |
| [[BCORL1]] | B | PNMA2 activity raises BCORL1's level | lines that do not express PNMA2 (16) vs lines expressing it (34) | 1.30× lower at baseline in the lines without PNMA2 | 0.087 | ⚠ within organs, on part of the lines; also absent: MCOLN3, CACNG6, SELENOM |
| [[CDCP1]] | B | PNMA2 activity raises CDCP1's level | lines that do not express PNMA2 (16) vs lines expressing it (34) | 2.67× lower at baseline in the lines without PNMA2 | 0.093 | ⚠ within organs, on part of the lines; also absent: MCOLN3, CACNG6, SELENOM |
| [[IL17RD]] | B | PNMA2 activity raises IL17RD's level | lines that do not express PNMA2 (16) vs lines expressing it (34) | 1.41× lower at baseline in the lines without PNMA2 | 0.098 | ⚠ within organs, on part of the lines; also absent: MCOLN3, CACNG6, SELENOM |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.528). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.1, -0.6); signed map (1.0, 44.8). **Vector** length 84.8, 20.9% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.6 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +6.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.4 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +7.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +0.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -27.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -14.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.9 | -11.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.8 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.6 | -10.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -7.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.0 | -4.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.9 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -2.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | PNMA family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.2 — chr8:26,504,701-26,514,092 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MA2, RGAG2 |
| Gene groups (HGNC) | Paraneoplastic Ma antigens |
| Matched by | ensembl_id |

UniProt [Q9UL42](https://www.uniprot.org/uniprotkb/Q9UL42) carries no function annotation.

**Summary**, from NCBI Gene [10687](https://www.ncbi.nlm.nih.gov/gene/10687):

> Predicted to be involved in positive regulation of apoptotic process. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9159](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9159) · Entrez [10687](https://www.ncbi.nlm.nih.gov/gene/10687) · UniProt [Q9UL42](https://www.uniprot.org/uniprotkb/Q9UL42) · Ensembl [ENSG00000240694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240694)

## Data

Gene col 14247: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14247); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14247, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14247]; `tensor/DDL_lfc|DDL_z.npy` [14247]; `embed/gene_vectors.npy` [14247]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14247 or target_col == 14247). Every well: [[PNMA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNMA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
