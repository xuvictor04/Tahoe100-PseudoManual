---
symbol: "KIF3C"
type: "gene"
col: 1409
ensembl_id: "ENSG00000084731"
name: "kinesin family member 3C"
location: "2p23.3"
module: 82
arm: "+"
pooled_cpm: 21.76
n_lines_expressing: 45
n_dd_up: 15
n_dd_down: 23
n_dd_up_clean: 10
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 15
direction_downstream: 8
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# KIF3C

*kinesin family member 3C* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.46× (z +9.4, q 2e-18, up in 25 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.365× (z -17.7, q 0e+00, down in 38 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMOD1]] (+0.58, fdr 1e-05), [[DPYSL5]] (+0.58, fdr 2e-05), [[GALNT12]] (+0.57, fdr 1e-05); moves opposite to [[ANKRD17-DT]] (-0.51, fdr 1e-04), [[BDNF-AS]] (-0.48, fdr 1e-04), [[GIGYF2]] (-0.46, fdr 6e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[BOLA3-DT]] → it (grade B ⚠); 8 go from it, the strongest it → [[ANXA6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1409.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +9.4 | 2e-18 | 25/43 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +6.8 | 4e-09 | 22/43 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.48×** | +6.6 | 7e-09 | 21/42 (NCI-H2030, C32, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.76×** | +5.2 | 3e-05 | 14/43 (CFPAC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +4.8 | 2e-04 | 15/43 (SW480, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 0.002 | 12/43 (CFPAC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.26×** | +4.1 | 0.004 | 12/43 (HepG2/C3A, BT-474, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.26×** | +4.0 | 0.004 | 11/43 (RKO, CFPAC-1, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.53×** | +3.9 | 0.005 | 8/35 (C32, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.17× | +3.9 | 0.005 | 15/43 (A498, NCI-H2030, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.005 | 11/42 (NCI-H2030, C32, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +3.9 | 0.005 | 11/43 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.24×** | +3.8 | 0.006 | 5/43 (J82, PANC-1, …) | all doses, flat |  |
| [[Berbamine (drug)]] 5 µM |  | 1.16× | +3.7 | 0.007 | 12/43 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.008 | 6/42 (A-427, HS-578T, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.015 | 9/42 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.027 | 9/43 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Posaconazole (drug)]] 5 µM |  | 1.19× | +2.9 | 0.093 | 8/43 (HEC-1-A, HS-578T, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1409.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.365×** | -17.7 | 0e+00 | 38/43 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.400×** | -16.1 | 0e+00 | 37/42 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.524×** | -16.1 | 0e+00 | 29/42 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.435×** | -14.6 | 0e+00 | 32/42 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.464×** | -13.5 | 2e-39 | 34/41 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.470×** | -13.3 | 3e-38 | 33/42 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.544×** | -10.3 | 4e-23 | 28/43 (MIA PaCa-2, PANC-1, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.622×** | -8.0 | 8e-14 | 24/42 (A-427, PANC-1, …) | two highest doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.438×** | -7.6 | 2e-12 | 22/43 (A-427, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.653×** | -7.5 | 4e-12 | 25/42 (A-427, SK-MEL-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.679×** | -6.8 | 6e-10 | 21/42 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.689×** | -6.5 | 3e-09 | 22/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.756×** | -4.9 | 4e-05 | 20/43 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -4.9 | 4e-05 | 22/43 (MIA PaCa-2, A-172, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.759×** | -4.8 | 5e-05 | 19/43 (MIA PaCa-2, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.833× | -4.5 | 2e-04 | 18/43 (A-427, A-172, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.622×** | -4.4 | 4e-04 | 9/43 (MIA PaCa-2, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.781×** | -4.2 | 9e-04 | 9/42 (A-172, Panc 03.27, …) | rises with dose | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | 0.852× | -4.0 | 0.002 | 15/43 (Hs 766T, HS-578T, …) | top dose only | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **0.822×** | -3.4 | 0.015 | 14/43 (Hs 766T, HOP62, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | **0.818×** | -3.4 | 0.017 | 7/42 (C-33 A, NCI-H23, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1409. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 32.9 | 0 | 10 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0730× (z -19.8) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.157× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 36.8 | 0 | 10 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.123× (z -14.2) |
| [[PANC-1 (line)]] | alt | 32.8 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -27.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -20.7) |
| [[NCI-H2030 (line)]] | alt | 35.5 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -17.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.191× (z -12.0) |
| [[A-172 (line)]] | wt | 90.8 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.334× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.349× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 21.1 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0336× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0710× (z -16.1) |
| [[Hs 766T (line)]] | wt | 18.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -16.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 14.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0754× (z -19.1) |
| [[SW480 (line)]] | alt | 22.5 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.284× (z -11.0) |
| [[A549 (line)]] | wt | 35.0 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -9.9) |
| [[AN3 CA (line)]] | alt | 24.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0696× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 27.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.287× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 13.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 30.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0955× (z -12.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 17.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -10.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.201× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 17.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -12.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 12.1 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.167× (z -10.1) |
| [[C32 (line)]] | wt | 22.3 | 1 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.70× (z +10.0) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[H4 (line)]] | wt | 13.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0682× (z -10.5) |
| [[HCT15 (line)]] | alt | 9.24 | 0 | 1 | — | [[Terfenadine (drug)]] 0.5 µM 0.0870× (z -8.5) |
| [[HS-578T (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -13.1) ⚠ cell-cycle shift, explains ~4% of this change |
| [[NCI-H661 (line)]] | alt | 28.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0570× (z -8.7) |
| [[RKO (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0747× (z -11.4) ⚠ toxic; unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 23.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.159× (z -10.7) |
| [[SW 900 (line)]] | alt | 17.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.186× (z -9.2) |
| [[SW1417 (line)]] | alt | 11.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.01× (z +8.6) | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.107× (z -8.8) |
| [[A498 (line)]] | wt | 67.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.91 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.04 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1409), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMOD1]] | +0.58 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[DPYSL5]] | +0.58 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[GALNT12]] | +0.57 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[USP35]] | +0.55 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[CPNE2]] | +0.54 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[RCAN3]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[KIF1A]] | +0.54 | +0.51 / +0.44 | both halves | 3e-05 | same gene group; pathway: COPI-dependent Golgi-to-ER retrograde traffic; STRING 648 |
| [[MAP6]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[KIF26A]] | +0.54 | +0.48 / +0.44 | both halves | 3e-05 | same gene group; pathway: Affinity selection of immunoglobulins; STRING 584 |
| [[FSD1L]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[L1CAM]] | +0.54 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[RASSF2]] | +0.54 | +0.48 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD17-DT]] | -0.51 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[BDNF-AS]] | -0.48 | -0.47 / -0.32 | both halves | 1e-04 |  |
| [[GIGYF2]] | -0.46 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[UFL1-AS1]] | -0.46 | -0.41 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 13, C 2. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BOLA3-DT]] | B | BOLA3-DT activity raises KIF3C's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 2.78× lower at baseline in the lines without BOLA3-DT | 0.002 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[PDZD4]] | B | PDZD4 activity raises KIF3C's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 2.11× lower at baseline in the lines without PDZD4 | 0.005 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[ANXA6]] | B | ANXA6 activity raises KIF3C's level | lines that do not express ANXA6 (8) vs lines expressing it (42) | 2.35× lower at baseline in the lines without ANXA6 | 0.006 | ⚠ within organs, on part of the lines; also absent: KATNAL1, PHC1, FAM171A1 |
| [[FSD1]] | B | FSD1 activity raises KIF3C's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 2.32× lower at baseline in the lines without FSD1 | 0.008 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[KIF26A]] | B | KIF26A activity raises KIF3C's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 1.70× lower at baseline in the lines without KIF26A | 0.010 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[BRSK2]] | B | BRSK2 activity raises KIF3C's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.51× lower at baseline in the lines without BRSK2 | 0.031 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[MYT1]] | B | MYT1 activity raises KIF3C's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 1.89× lower at baseline in the lines without MYT1 | 0.037 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[L1CAM]] | B | L1CAM activity raises KIF3C's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 1.91× lower at baseline in the lines without L1CAM | 0.042 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[SPEG]] | B | SPEG activity raises KIF3C's level | lines that do not express SPEG (16) vs lines expressing it (34) | 2.17× lower at baseline in the lines without SPEG | 0.053 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1 |
| [[RNF182]] | B | RNF182 activity raises KIF3C's level | lines that do not express RNF182 (22) vs lines expressing it (28) | 2.17× lower at baseline in the lines without RNF182 | 0.054 | ⚠ within organs, on part of the lines; also absent: PTX3, FZD8, ENSG00000230615 |
| [[SEPTIN5]] | B | SEPTIN5 activity raises KIF3C's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.97× lower at baseline in the lines without SEPTIN5 | 0.065 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[TUBA1A]] | B | TUBA1A activity raises KIF3C's level | lines that do not express TUBA1A (10) vs lines expressing it (40) | 3.02× lower at baseline in the lines without TUBA1A | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, GABBR1, CHST10 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA6]] | B | KIF3C activity raises ANXA6's level | lines that do not express KIF3C (5) vs lines expressing it (45) | 3.60× lower at baseline in the lines without KIF3C | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC00888, WNT3, TBKBP1; its own permutation p |
| [[STARD3NL]] | B | KIF3C activity raises STARD3NL's level | lines that do not express KIF3C (5) vs lines expressing it (45) | 3.34× lower at baseline in the lines without KIF3C | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC00888, WNT3, TBKBP1; its own permutation p |
| [[NXPE3]] | B | KIF3C activity raises NXPE3's level | lines that do not express KIF3C (5) vs lines expressing it (45) | 2.59× lower at baseline in the lines without KIF3C | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC00888, WNT3, TBKBP1; its own permutation p |
| [[FCHSD1]] | B | KIF3C activity raises FCHSD1's level | lines that do not express KIF3C (5) vs lines expressing it (45) | 1.95× lower at baseline in the lines without KIF3C | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC00888, WNT3, TBKBP1; its own permutation p |
| [[GPR161]] | B | KIF3C activity raises GPR161's level | lines that do not express KIF3C (5) vs lines expressing it (45) | 3.17× lower at baseline in the lines without KIF3C | 0.069 | ⚠ within organs, on part of the lines; also absent: LINC00888, WNT3, TBKBP1 |
| [[FAM161A]] | B | KIF3C activity raises FAM161A's level | lines that do not express KIF3C (5) vs lines expressing it (45) | 2.71× lower at baseline in the lines without KIF3C | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC00888, WNT3, TBKBP1; its own permutation p |
| [[CACNB1]] | B | KIF3C activity raises CACNB1's level | lines that do not express KIF3C (5) vs lines expressing it (45) | 1.73× lower at baseline in the lines without KIF3C | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC00888, WNT3, TBKBP1; its own permutation p |
| [[KATNAL1]] | C | KIF3C activity raises KATNAL1's level | lines that do not express KIF3C (5) vs lines expressing it (45) | 4.61× lower at baseline in the lines without KIF3C | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC00888, WNT3, TBKBP1; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.9, 39.8); signed map (-7.6, 23.3). **Vector** length 95.3, 22.1% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +5.4 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.3 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +6.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~80% of this change | +4.6 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.4 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +5.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.3 | -14.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.3 | -16.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.9 | -17.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.9 | -13.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -10.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -4.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.0 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -7.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.8 | -1.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 3C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:25,926,598-25,982,749 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Kinesins |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 17 pathways, smallest: Intraflagellar transport; Kinesins; Processing of antigen in germinal center B cells |
| Matched by | ensembl_id |

**Function**, from UniProt [O14782](https://www.uniprot.org/uniprotkb/O14782) (Kinesin-like protein KIF3C):

> Microtubule-based anterograde translocator for membranous organelles.

**Summary**, from NCBI Gene [3797](https://www.ncbi.nlm.nih.gov/gene/3797):

> Predicted to enable ATP hydrolysis activity; microtubule binding activity; and microtubule motor activity. Predicted to be involved in microtubule-based movement. Predicted to be located in microtubule cytoskeleton; neuronal cell body; and neuronal ribonucleoprotein granule. Predicted to be part of kinesin complex. Predicted to be active in cytoplasm and microtubule. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:6321](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6321) · Entrez [3797](https://www.ncbi.nlm.nih.gov/gene/3797) · UniProt [O14782](https://www.uniprot.org/uniprotkb/O14782) · Ensembl [ENSG00000084731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084731)

## Data

Gene col 1409: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1409); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1409, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1409]; `tensor/DDL_lfc|DDL_z.npy` [1409]; `embed/gene_vectors.npy` [1409]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1409 or target_col == 1409). Every well: [[KIF3C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF3C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
