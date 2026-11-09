---
symbol: "ATAD3A"
type: "gene"
col: 12465
ensembl_id: "ENSG00000197785"
name: "ATPase family AAA domain containing 3A"
location: "1p36.33"
module: 36
arm: "+"
pooled_cpm: 13.38
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 20
n_dd_up_clean: 16
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# ATAD3A

*ATPase family AAA domain containing 3A* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (21 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.57× (z +19.0, q 0e+00, up in 34 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.56× (z +6.6, q 2e-09, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.654× (z -9.0, q 9e-17, down in 30 of 47 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.581× (z -8.2, q 9e-14, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATAD3B]] (+0.88, fdr 7e-06, ⚠ same locus), [[TREX2]] (+0.81, fdr 7e-06), [[TOMM40]] (+0.80, fdr 7e-06), [[TRAP1]] (+0.75, fdr 7e-06); moves opposite to [[ZNF821]] (-0.63, fdr 1e-05), [[CHMP2B]] (-0.62, fdr 1e-05), [[HHLA3]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 22 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12465.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.57×** | +19.0 | 0e+00 | 34/38 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.24×** | +16.9 | 0e+00 | 23/23 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.76×** | +14.0 | 2e-42 | 25/28 (NCI-H2030, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **2.16×** | +11.5 | 2e-28 | 41/48 (SW480, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **2.04×** | +10.6 | 3e-24 | 38/48 (SW480, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.89×** | +9.5 | 2e-19 | 38/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.84×** | +8.7 | 2e-16 | 30/42 (A-427, NCI-H460, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.77×** | +8.5 | 1e-15 | 31/47 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.74×** | +8.0 | 1e-13 | 25/42 (CFPAC-1, MIA PaCa-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +6.6 | 2e-09 | 28/46 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **1.46×** | +5.6 | 1e-06 | 24/44 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.02×** | +5.2 | 9e-06 | 20/44 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.35×** | +4.5 | 4e-04 | 16/46 (PANC-1, SW480, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.35×** | +4.4 | 4e-04 | 15/45 (SK-MEL-2, AsPC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.35×** | +4.4 | 4e-04 | 17/46 (NCI-H460, HS-578T, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.78×** | +4.3 | 6e-04 | 9/46 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.77×** | +4.2 | 7e-04 | 12/45 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.77×** | +4.2 | 7e-04 | 13/45 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +4.2 | 8e-04 | 13/48 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.48×** | +4.2 | 8e-04 | 10/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.002 | 10/47 (NCI-H460, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.009 | 14/45 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.010 | 5/48 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.037 | 10/47 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.51×** | +3.0 | 0.039 | 7/43 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.039 | 4/48 (J82, C32, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.039 | 8/46 (SW480, MIA PaCa-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12465.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.654×** | -9.0 | 9e-17 | 30/47 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.581×** | -8.2 | 9e-14 | 30/45 (SNU-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.684×** | -8.1 | 1e-13 | 31/48 (A498, SW1417, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.636×** | -6.8 | 1e-09 | 27/46 (RPMI-7951, LS 180, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | **0.797×** | -4.9 | 1e-04 | 16/48 (PANC-1, AsPC-1, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.735×** | -4.5 | 7e-04 | 18/45 (C-33 A, Hs 766T, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.745×** | -4.3 | 0.001 | 16/46 (A-427, J82, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.751×** | -3.9 | 0.008 | 12/48 (SW480, Hs 766T, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.783×** | -3.7 | 0.013 | 9/48 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.799×** | -3.4 | 0.036 | 16/48 (NCI-H661, SW480, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.637×** | -3.4 | 0.036 | 5/47 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.812×** | -3.4 | 0.036 | 8/47 (NCI-H23, LoVo, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.802×** | -3.3 | 0.037 | 13/48 (LoVo, J82, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.856× | -3.3 | 0.037 | 10/48 (NCI-H661, C-33 A, …) | all doses, flat | position effect removed |
| [[Afatinib (drug)]] 0.5 µM |  | 0.838× | -3.3 | 0.037 | 8/48 (CHP-212, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.796×** | -3.3 | 0.038 | 13/48 (LoVo, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.809×** | -3.2 | 0.044 | 6/48 (A-427, LS 180, …) | rises with dose |  |
| [[AZD-8055 (drug)]] 5 µM |  | **0.672×** | -3.0 | 0.083 | 8/46 (HCT15, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.823×** | -3.0 | 0.083 | 6/47 (KATO III, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.61 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12465. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.21 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.84× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-427 (line)]] | wt | 18.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Selinexor (drug)]] 5 µM 0.361× (z -9.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A498 (line)]] | wt | 24.0 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.367× (z -11.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.405× (z -10.6) |
| [[HOP62 (line)]] | alt | 12.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.18× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[LS 180 (line)]] | wt | 12.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Selinexor (drug)]] 5 µM 0.297× (z -9.3) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW480 (line)]] | alt | 13.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[AsPC-1 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 1 | — | [[Hesperidin (drug)]] 0.05 µM 0.127× (z -8.8) |
| [[HCT15 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.161× (z -9.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HS-578T (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.228× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 7.19 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.1× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[RPMI-7951 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.141× (z -9.0) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SNU-1 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0886× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12465), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATAD3B]] | +0.88 | +0.83 / +0.87 | both halves | 7e-06 | same gene group; STRING 640; ⚠ same locus (14.3 kb, same strand: neighbours can correlate without regulation) |
| [[TREX2]] | +0.81 | +0.76 / +0.82 | both halves | 7e-06 |  |
| [[TOMM40]] | +0.80 | +0.75 / +0.79 | both halves | 7e-06 | STRING 521 |
| [[TRAP1]] | +0.75 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[E2F4]] | +0.75 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[PGAM5]] | +0.75 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[CPSF1]] | +0.73 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[CTU2]] | +0.73 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.71 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[SRM]] | +0.71 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[GCN1]] | +0.69 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.69 | +0.74 / +0.62 | both halves | 7e-06 | STRING 431 |
| [[CHID1]] | +0.69 | +0.61 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF821]] | -0.63 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[CHMP2B]] | -0.62 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[HHLA3]] | -0.61 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[BTN2A2]] | -0.60 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[PNRC1]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.60 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[PIGP]] | -0.59 | -0.58 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity raises ATAD3A's level | compounds that target MTOR: 4 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Temsirolimus) | 50% of the class's compounds vs 4.2% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds |
| [[MAP2K1]] | B | MAP2K1 activity raises ATAD3A's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CHMP4C]] | B | CHMP4C activity lowers ATAD3A's level | lines that do not express CHMP4C (16) vs lines expressing it (34) | 1.14× higher at baseline in the lines without CHMP4C | 0.099 | ⚠ within organs, on part of the lines; also absent: TSTD1, BTC, TNK1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.694). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-5.6, -28.2); signed map (-45.8, -17.5). **Vector** length 89.5, 19.6% of its response variance represented; |z| ≥ 3 in 1,022 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +5.7 | +16.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +5.7 | +19.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.6 | +9.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +4.6 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +4.4 | +14.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +5.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +6.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +3.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -6.8 | -9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.2 | -8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -1.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -4.2 | -6.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.4 | -3.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -4.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ATPase family AAA domain containing 3A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,512,162-1,534,685 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10709 |
| Gene groups (HGNC) | AAA ATPases; Mitochondrial nucleoid associated proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVI7](https://www.uniprot.org/uniprotkb/Q9NVI7) (ATPase family AAA domain-containing protein 3A):

> Essential for mitochondrial network organization, mitochondrial metabolism and cell growth at organism and cellular level. May play an important role in mitochondrial protein synthesis. May also participate in mitochondrial DNA replication. May bind to mitochondrial DNA D-loops and contribute to nucleoid stability. Required for enhanced channeling of cholesterol for hormone-dependent steroidogenesis. Involved in mitochondrial-mediated antiviral innate immunity. Required to protect mitochondria …

**Summary**, from NCBI Gene [55210](https://www.ncbi.nlm.nih.gov/gene/55210):

> This gene encodes a ubiquitously expressed mitochondrial membrane protein that contributes to mitochondrial dynamics, nucleoid organization, protein translation, cell growth, and cholesterol metabolism. This gene is a member of the ATPase family AAA-domain containing 3 gene family which, in humans, includes two other paralogs. Naturally occurring mutations in this gene are associated with distinct neurological syndromes including Harel-Yoon syndrome. High-level expression of this gene is …

**Accessions** — [HGNC:25567](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25567) · Entrez [55210](https://www.ncbi.nlm.nih.gov/gene/55210) · UniProt [Q9NVI7](https://www.uniprot.org/uniprotkb/Q9NVI7) · Ensembl [ENSG00000197785](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197785)

## Data

Gene col 12465: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12465); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12465, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12465]; `tensor/DDL_lfc|DDL_z.npy` [12465]; `embed/gene_vectors.npy` [12465]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12465 or target_col == 12465). Every well: [[ATAD3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATAD3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
