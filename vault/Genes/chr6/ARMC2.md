---
symbol: "ARMC2"
type: "gene"
col: 4013
ensembl_id: "ENSG00000118690"
name: "armadillo repeat containing 2"
location: "6q21"
module: 17
arm: "+"
pooled_cpm: 17.51
n_lines_expressing: 48
n_dd_up: 29
n_dd_down: 38
n_dd_up_clean: 24
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ARMC2

*armadillo repeat containing 2* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.63× (z +15.7, q 0e+00, up in 36 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.261× (z -21.7, q 0e+00, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTLL1]] (+0.66, fdr 7e-06), [[ZNF559-ZNF177]] (+0.58, fdr 2e-05), [[SDHB]] (+0.57, fdr 2e-04); moves opposite to [[KIF26B]] (-0.52, fdr 2e-04), [[GCNT4]] (-0.50, fdr 9e-04, ⚠ not reproduced), [[RNF6]] (-0.50, fdr 6e-04), [[CARD6]] (-0.49, fdr 3e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CARD6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4013.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.63×** | +15.7 | 0e+00 | 36/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.26×** | +13.2 | 2e-37 | 35/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +9.9 | 8e-21 | 32/46 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +8.5 | 4e-15 | 32/46 (LoVo, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +6.2 | 7e-08 | 23/46 (PANC-1, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.37×** | +5.1 | 3e-05 | 20/46 (KATO III, NCI-H1792, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +4.9 | 6e-05 | 21/45 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +4.6 | 3e-04 | 14/46 (SW480, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.24×** | +4.5 | 5e-04 | 13/46 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +4.4 | 6e-04 | 16/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.002 | 15/45 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.31×** | +4.0 | 0.002 | 10/45 (NCI-H2347, RPMI-7951, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.005 | 9/46 (PANC-1, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.9 | 0.005 | 12/38 (SW480, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.006 | 8/46 (KATO III, PANC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.006 | 8/46 (MIA PaCa-2, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4013.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.261×** | -21.7 | 0e+00 | 43/46 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.272×** | -21.0 | 0e+00 | 38/45 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.358×** | -16.6 | 0e+00 | 43/46 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.356×** | -15.8 | 0e+00 | 38/45 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.397×** | -14.9 | 0e+00 | 40/46 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.435×** | -13.4 | 3e-39 | 33/45 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.597×** | -11.8 | 4e-30 | 27/45 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.495×** | -11.4 | 5e-28 | 35/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.542×** | -9.9 | 3e-21 | 27/46 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.569×** | -9.1 | 5e-18 | 30/46 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.554×** | -9.0 | 1e-17 | 27/44 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.594×** | -8.4 | 2e-15 | 31/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.611×** | -7.5 | 2e-12 | 30/46 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.698×** | -5.8 | 3e-07 | 23/46 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.700×** | -5.2 | 6e-06 | 20/45 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.705×** | -5.1 | 1e-05 | 21/46 (NCI-H460, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.570×** | -4.7 | 7e-05 | 14/46 (SHP-77, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.782×** | -4.0 | 0.002 | 10/46 (PANC-1, BT-474, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.842× | -3.9 | 0.003 | 19/46 (A-427, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4013. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 43.2 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -27.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -23.1) |
| [[LOX-IMVI (line)]] | wt | 28.9 | 0 | 9 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 14.7 | 0 | 7 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.102× (z -16.7) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.193× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 22.9 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.105× (z -12.3) |
| [[A549 (line)]] | wt | 17.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -19.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.164× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 21.9 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0959× (z -17.0) |
| [[NCI-H23 (line)]] | alt | 46.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -13.4) |
| [[SNU-1 (line)]] | wt | 23.4 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0375× (z -15.6) |
| [[SW480 (line)]] | alt | 10.9 | 2 | 3 | [[Panobinostat (drug)]] 5 µM 4.31× (z +9.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -9.7) |
| [[A-427 (line)]] | wt | 40.1 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0748× (z -21.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.295× (z -14.6) |
| [[BT-474 (line)]] | alt | 21.2 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.54× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -15.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -9.0) |
| [[C32 (line)]] | wt | 12.9 | 0 | 4 (2 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0570× (z -13.1) ⚠ toxic; unreliable plate only · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.146× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 18.7 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.157× (z -13.6) |
| [[HS-578T (line)]] | alt | 31.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.221× (z -9.6) |
| [[LoVo (line)]] | wt | 14.9 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +11.2) ⚠ cell-cycle shift, explains ~35% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.130× (z -14.1) |
| [[HCT15 (line)]] | alt | 11.9 | 0 | 3 (1 ⚠) | — | [[Pemigatinib (drug)]] 0.05 µM 0.0599× (z -11.1) |
| [[HOP62 (line)]] | alt | 14.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.202× (z -9.5) |
| [[HT-29 (line)]] | alt | 11.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -9.6) |
| [[A-172 (line)]] | wt | 14.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -8.9) |
| [[C-33 A (line)]] | alt | 59.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -9.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 15.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0452× (z -12.6) |
| [[KATO III (line)]] | alt | 10.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.92× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 16.1 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.208× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 15.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.78× (z +15.5) ⚠ cell-cycle shift, explains ~35% of this change | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.150× (z -10.1) |
| [[SNU-423 (line)]] | alt | 21.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.162× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -10.5) |
| [[Hs 766T (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -8.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[J82 (line)]] | alt | 11.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.188× (z -8.8) |
| [[LS 180 (line)]] | wt | 8.51 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0851× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.236× (z -8.7) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 21.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.147× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 9.76 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0403× (z -13.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 7.86 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -9.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.21 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4013), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTLL1]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ZNF559-ZNF177]] | +0.58 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[SDHB]] | +0.57 | +0.31 / +0.53 | both halves | 2e-04 |  |
| [[ELP1]] | +0.56 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[SMIM8]] | +0.56 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[ZNF559]] | +0.55 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[EHMT2]] | +0.55 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[ARL3]] | +0.54 | +0.33 / +0.52 | both halves | 1e-04 |  |
| [[FAM13B]] | +0.53 | +0.35 / +0.36 | both halves | 1e-04 |  |
| [[ZNF177]] | +0.53 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[SKIC3]] | +0.53 | +0.26 / +0.46 | both halves | 3e-04 |  |
| [[POT1]] | +0.53 | +0.33 / +0.41 | both halves | 1e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF26B]] | -0.52 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[GCNT4]] | -0.50 | -0.19 / -0.37 | ⚠ not reproduced | 9e-04 |  |
| [[RNF6]] | -0.50 | -0.22 / -0.42 | both halves | 6e-04 |  |
| [[CARD6]] | -0.49 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[ZNF700]] | -0.48 | -0.34 / -0.32 | both halves | 2e-04 |  |
| [[ZNF124]] | -0.47 | -0.25 / -0.20 | ⚠ not reproduced | 7e-04 |  |
| [[SLC22A3]] | -0.46 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[MSRA]] | -0.46 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[ZHX2]] | -0.46 | -0.08 / -0.52 | ⚠ one half (not replicated) | 0.004 |  |
| [[SPHK1]] | -0.45 | -0.12 / -0.41 | ⚠ not reproduced | 0.002 |  |
| [[ZNF100]] | -0.44 | -0.26 / -0.35 | both halves | 3e-04 |  |
| [[DGKH]] | -0.44 | -0.21 / -0.41 | both halves | 7e-04 |  |
| [[ZNF672]] | -0.44 | -0.29 / -0.36 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD6]] | B | CARD6 activity lowers ARMC2's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 1.83× higher at baseline in the lines without CARD6 | 0.007 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.454). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-38.5, 27.1); signed map (-26.9, -12.9). **Vector** length 70.5, 14.3% of its response variance represented; |z| ≥ 3 in 1,230 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +0.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +15.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +13.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | -2.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.1 | +9.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +8.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +3.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.0 | -9.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -8.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -4.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | armadillo repeat containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:108,848,416-108,974,476 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434P0714, bA787I22.1 |
| Gene groups (HGNC) | Armadillo repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEN0](https://www.uniprot.org/uniprotkb/Q8NEN0) (Armadillo repeat-containing protein 2):

> Required for sperm flagellum axoneme organization and function (By similarity). Involved in axonemal central pair complex assembly and/or stability (By similarity).

**Summary**, from NCBI Gene [84071](https://www.ncbi.nlm.nih.gov/gene/84071):

> Involved in sperm axoneme assembly. Implicated in spermatogenic failure 38. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23045](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23045) · Entrez [84071](https://www.ncbi.nlm.nih.gov/gene/84071) · UniProt [Q8NEN0](https://www.uniprot.org/uniprotkb/Q8NEN0) · Ensembl [ENSG00000118690](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118690)

## Data

Gene col 4013: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4013); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4013, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4013]; `tensor/DDL_lfc|DDL_z.npy` [4013]; `embed/gene_vectors.npy` [4013]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4013 or target_col == 4013). Every well: [[ARMC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARMC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
