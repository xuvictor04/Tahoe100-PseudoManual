---
symbol: "BCL7B"
type: "gene"
col: 2788
ensembl_id: "ENSG00000106635"
name: "BAF chromatin remodeling complex subunit BCL7B"
location: "7q11.23"
module: 96
arm: "+"
pooled_cpm: 23.48
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# BCL7B

*BAF chromatin remodeling complex subunit BCL7B* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.76× (z +16.8, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.688× (z -11.3, q 1e-26, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARAF]] (+0.68, fdr 1e-05), [[PIGO]] (+0.67, fdr 1e-05), [[TEX261]] (+0.65, fdr 1e-05); moves opposite to [[PRDX4]] (-0.64, fdr 1e-05), [[TMEM68]] (-0.60, fdr 2e-05), [[NDUFAF7]] (-0.59, fdr 2e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2788.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +16.8 | 0e+00 | 43/47 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.12×** | +15.3 | 0e+00 | 42/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +14.2 | 2e-43 | 33/41 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +11.6 | 6e-29 | 26/33 (Panc 03.27, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +10.0 | 1e-21 | 25/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +9.9 | 6e-21 | 33/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +8.1 | 3e-14 | 26/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +6.9 | 3e-10 | 24/45 (LoVo, SHP-77, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +6.8 | 7e-10 | 21/37 (KATO III, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +5.8 | 3e-07 | 23/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~19% of this change | **1.31×** | +5.7 | 7e-07 | 24/45 (H4, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +4.9 | 5e-05 | 15/48 (PANC-1, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +4.6 | 2e-04 | 18/47 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.0 | 0.003 | 2/48 (HCT15, SW 1088) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.005 | 12/48 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 0.05 µM |  | **1.21×** | +3.8 | 0.006 | 10/48 (HepG2/C3A, Hs 766T, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.012 | 8/46 (MIA PaCa-2, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.1 | 0.047 | 9/48 (SNU-423, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.055 | 6/48 (LOX-IMVI, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.15× | +2.9 | 0.082 | 9/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2788.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.688×** | -11.3 | 1e-26 | 32/47 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -8.6 | 2e-15 | 30/47 (NCI-H460, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.731×** | -6.4 | 2e-08 | 26/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.822×** | -5.9 | 4e-07 | 24/48 (SNU-1, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.769×** | -5.6 | 2e-06 | 22/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.775×** | -5.4 | 5e-06 | 20/47 (SW48, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.776×** | -5.4 | 5e-06 | 20/48 (A-172, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.841× | -5.2 | 1e-05 | 18/48 (NCI-H2347, NCI-H1573, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.866× | -4.4 | 8e-04 | 17/48 (A498, LS 180, …) | rises with dose | low cells (technical?) |
| [[Clotrimazole (drug)]] 5 µM |  | 0.881× | -3.9 | 0.007 | 10/48 (BT-474, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.844× | -3.6 | 0.014 | 6/48 (SK-MEL-2, J82, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.860× | -3.2 | 0.055 | 13/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.867× | -3.1 | 0.096 | 11/47 (A498, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2788. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +15.8) | — |
| [[A498 (line)]] | wt | 39.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +14.7) | [[Selinexor (drug)]] 5 µM 0.495× (z -11.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A549 (line)]] | wt | 16.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 25.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +10.1) ⚠ toxic; transcription drop | [[Lonafarnib (drug)]] 5 µM 0.0907× (z -10.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -10.0) |
| [[PANC-1 (line)]] | alt | 23.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 28.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -14.2) |
| [[NCI-H1792 (line)]] | alt | 24.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -11.8) |
| [[SW48 (line)]] | wt | 30.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.166× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 43.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -10.4) |
| [[C32 (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.167× (z -9.0) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 18.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 19.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -9.3) |
| [[J82 (line)]] | alt | 20.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +8.7) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 36.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.01× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.380× (z -9.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H23 (line)]] | alt | 18.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 30.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 22.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +9.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 23.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -11.8) |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 13.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +12.5) | — |
| [[SW1417 (line)]] | alt | 26.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.3) | — |
| [[SW480 (line)]] | alt | 24.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.4) | — |
| [[A-172 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2788), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARAF]] | +0.68 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[PIGO]] | +0.67 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[TEX261]] | +0.65 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[FAAP100]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[PUF60]] | +0.60 | +0.56 / +0.62 | both halves | 1e-05 | pathway: ATP-dependent chromatin remodelers |
| [[CCDC113]] | +0.60 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[CELSR3]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ZNF512B]] | +0.59 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[SMARCB1]] | +0.59 | +0.57 / +0.64 | both halves | 1e-05 | same gene group; pathway: ATP-dependent chromatin remodelers; STRING 989 |
| [[RNF123]] | +0.58 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[SAYSD1]] | +0.57 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[CSRP1]] | +0.57 | +0.44 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDX4]] | -0.64 | -0.55 / -0.72 | both halves | 1e-05 |  |
| [[TMEM68]] | -0.60 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[NDUFAF7]] | -0.59 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[FASTKD1]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[ASB7]] | -0.58 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[HOXB5]] | -0.58 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | -0.57 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[POM121]] | -0.56 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[SMAD5]] | -0.56 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ANKRD16]] | -0.55 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[MIR4458HG]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[EEF1AKMT4]] | -0.55 | -0.43 / -0.66 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises BCL7B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KHDC1]] | B | KHDC1 activity lowers BCL7B's level | lines that do not express KHDC1 (15) vs lines expressing it (35) | 1.08× higher at baseline in the lines without KHDC1 | 0.093 | ⚠ within organs, on part of the lines; also absent: KHDC1-AS1, MAP9, C15orf48 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises BCL7B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises BCL7B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity raises BCL7B's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.616). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-18.6, -2.6); signed map (0.2, -33.9). **Vector** length 88.1, 17.8% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +16.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.1 | +15.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +14.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.2 | +9.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +4.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +2.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.8 | +1.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.7 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -11.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -8.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.3 | -5.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.2 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -5.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -0.8 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | BAF chromatin remodeling complex subunit BCL7B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:73,536,356-73,557,690 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SMARCJ2 |
| Gene groups (HGNC) | BAF complex subunits |
| Reactome | 18 pathways, smallest: Formation of the non-canonical BAF (ncBAF) complex; Formation of the canonical BAF (cBAF) complex; Formation of the polybromo-BAF (pBAF) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQE9](https://www.uniprot.org/uniprotkb/Q9BQE9) (B-cell CLL/lymphoma 7 protein family member B):

> Positive regulator of apoptosis. Plays a role in the Wnt signaling pathway, negatively regulating the expression of Wnt signaling components CTNNB1 and HMGA1. Involved in cell cycle progression, maintenance of the nuclear structure and stem cell differentiation. May play a role in lung tumor development or progression (By similarity).

**Summary**, from NCBI Gene [9275](https://www.ncbi.nlm.nih.gov/gene/9275):

> This gene encodes a member of the BCL7 family including BCL7A, BCL7B and BCL7C proteins. This member is BCL7B, which contains a region that is highly similar to the N-terminal segment of BCL7A or BCL7C proteins. The BCL7A protein is encoded by the gene known to be directly involved in a three-way gene translocation in a Burkitt lymphoma cell line. This gene is located at a chromosomal region commonly deleted in Williams syndrome. This gene is highly conserved from C. elegans to human. Multiple …

**Accessions** — [HGNC:1005](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1005) · Entrez [9275](https://www.ncbi.nlm.nih.gov/gene/9275) · UniProt [Q9BQE9](https://www.uniprot.org/uniprotkb/Q9BQE9) · Ensembl [ENSG00000106635](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106635)

## Data

Gene col 2788: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2788); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2788, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2788]; `tensor/DDL_lfc|DDL_z.npy` [2788]; `embed/gene_vectors.npy` [2788]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2788 or target_col == 2788). Every well: [[BCL7B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL7B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
