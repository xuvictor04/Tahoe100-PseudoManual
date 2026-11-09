---
symbol: "ABCA10"
type: "gene"
col: 7791
ensembl_id: "ENSG00000154263"
name: "ATP binding cassette subfamily A member 10"
location: "17q24.3"
module: 39
arm: "+"
pooled_cpm: 12.79
n_lines_expressing: 44
n_dd_up: 20
n_dd_down: 19
n_dd_up_clean: 15
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 15
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# ABCA10

*ATP binding cassette subfamily A member 10* — 17q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.79× (z +20.7, q 0e+00, up in 37 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.385× (z -8.0, q 9e-13, down in 29 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.520× (z -5.5, q 6e-06, down in 29 of 41 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM151B]] (+0.76, fdr 7e-06), [[N4BP2L1]] (+0.75, fdr 1e-05), [[SLC22A1]] (+0.73, fdr 7e-06); moves opposite to [[SLC9A6]] (-0.67, fdr 4e-05), [[STIMATE]] (-0.66, fdr 3e-05), [[PACC1]] (-0.66, fdr 2e-04).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ABCA6]] → it (grade B ⚠); 15 go from it, the strongest it → [[CCT6B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7791.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.79×** | +20.7 | 0e+00 | 37/40 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +8.3 | 4e-14 | 34/39 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.10×** | +6.2 | 1e-07 | 27/39 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.10×** | +5.9 | 4e-07 | 24/41 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +5.3 | 1e-05 | 26/38 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +5.0 | 4e-05 | 22/41 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.48×** | +4.7 | 3e-04 | 17/42 (A498, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.64×** | +4.1 | 0.003 | 18/41 (A498, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **2.50×** | +4.0 | 0.004 | 17/42 (HEC-1-A, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +3.9 | 0.005 | 22/40 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +3.6 | 0.015 | 14/36 (RKO, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.54×** | +3.6 | 0.015 | 16/40 (HepG2/C3A, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.55×** | +3.5 | 0.018 | 17/39 (NCI-H460, C32, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.50×** | +3.4 | 0.032 | 16/42 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.50×** | +3.3 | 0.042 | 10/42 (HepG2/C3A, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.02×** | +3.1 | 0.073 | 15/42 (HepG2/C3A, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.97×** | +3.0 | 0.088 | 7/42 (HEC-1-A, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7791.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.385×** | -8.0 | 9e-13 | 29/38 (Panc 03.27, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.406×** | -7.5 | 2e-11 | 30/41 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.415×** | -7.3 | 4e-11 | 29/40 (NCI-H23, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.437×** | -6.9 | 7e-10 | 27/40 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.520×** | -5.5 | 6e-06 | 29/41 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.547×** | -5.0 | 5e-05 | 25/39 (SNU-423, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.341×** | -4.7 | 2e-04 | 18/32 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.357×** | -4.5 | 5e-04 | 23/37 (HOP62, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.633×** | -3.8 | 0.008 | 21/40 (RPMI-7951, Hs 766T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **0.623×** | -3.8 | 0.008 | 20/37 (HepG2/C3A, SW480, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.730×** | -3.7 | 0.010 | 19/41 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.661×** | -3.5 | 0.024 | 19/40 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.662×** | -3.4 | 0.024 | 16/40 (SW 900, SW48, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.662×** | -3.4 | 0.024 | 15/38 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~97% of this change | **0.678×** | -3.2 | 0.045 | 18/37 (HepG2/C3A, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **0.596×** | -3.1 | 0.068 | 13/38 (SW 900, NCI-H460, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.689×** | -3.0 | 0.088 | 10/41 (Hs 766T, A-427, …) | top dose only | plate-row cell shift |
| [[Auranofin (drug)]] 5 µM |  | **0.701×** | -3.0 | 0.091 | 14/40 (HepG2/C3A, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.76 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7791. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 48.8 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0411× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.142× (z -9.4) |
| [[SW480 (line)]] | alt | 9.34 | 0 | 6 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -10.6) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SNU-423 (line)]] | alt | 33.7 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.0751× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 11.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.4× (z +15.2) | — |
| [[hTERT-HPNE (line)]] | wt | 41.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.48× (z +14.2) | [[Digitoxin (drug)]] 5 µM 0.0831× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H460 (line)]] | wt | 20.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.2× (z +25.1) | — |
| [[A498 (line)]] | wt | 9.04 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 6.25 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +8.6) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0581× (z -10.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HS-578T (line)]] | alt | 7.35 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.2× (z +16.7) | — |
| [[LoVo (line)]] | wt | 6.56 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +14.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 38.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +11.9) | [[Digitoxin (drug)]] 5 µM 0.183× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A549 (line)]] | wt | 11.1 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0895× (z -9.2) |
| [[BT-474 (line)]] | alt | 5.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.7× (z +11.9) | — |
| [[CHP-212 (line)]] | wt | 36.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +12.1) | — |
| [[COLO 205 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0859× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[H4 (line)]] | wt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 49.6× (z +18.4) | — |
| [[HEC-1-A (line)]] | alt | 17.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +12.6) | — |
| [[HOP62 (line)]] | alt | 9.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +14.5) | — |
| [[HT-29 (line)]] | alt | 9.91 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.26× (z +10.9) | — |
| [[J82 (line)]] | alt | 16.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +15.6) | — |
| [[KATO III (line)]] | alt | 13.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H2030 (line)]] | alt | 12.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 9.47 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0412× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[PANC-1 (line)]] | alt | 4.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.81× (z +12.6) | — |
| [[RKO (line)]] | wt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 21.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +14.1) | — |
| [[SK-MEL-2 (line)]] | alt | 7.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +14.4) | — |
| [[SW 1088 (line)]] | alt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.5× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 29.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +13.1) | — |
| [[A-172 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7791), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM151B]] | +0.76 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[N4BP2L1]] | +0.75 | +0.82 / +0.49 | both halves | 1e-05 |  |
| [[SLC22A1]] | +0.73 | +0.83 / +0.59 | both halves | 7e-06 |  |
| [[USP50]] | +0.72 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[NLGN3]] | +0.71 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[LINC01191]] | +0.70 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[C3orf20]] | +0.69 | +0.74 / +0.48 | both halves | 2e-05 |  |
| [[TXK]] | +0.69 | +0.76 / +0.55 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | +0.69 | +0.74 / +0.42 | both halves | 4e-05 |  |
| [[DNAH12]] | +0.68 | +0.76 / +0.38 | both halves | 6e-05 |  |
| [[CCT6B]] | +0.68 | +0.74 / +0.31 | both halves | 2e-04 |  |
| [[AK9]] | +0.68 | +0.75 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A6]] | -0.67 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[STIMATE]] | -0.66 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[PACC1]] | -0.66 | -0.63 / -0.32 | both halves | 2e-04 |  |
| [[GNA12]] | -0.64 | -0.65 / -0.31 | both halves | 2e-04 |  |
| [[COPG2]] | -0.64 | -0.66 / -0.39 | both halves | 5e-05 |  |
| [[LPCAT4]] | -0.63 | -0.68 / -0.31 | both halves | 2e-04 |  |
| [[CPSF4]] | -0.63 | -0.70 / -0.41 | both halves | 4e-05 |  |
| [[ANKS6]] | -0.63 | -0.65 / -0.35 | both halves | 1e-04 |  |
| [[CDK5RAP1]] | -0.63 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[PIGF]] | -0.63 | -0.66 / -0.35 | both halves | 1e-04 |  |
| [[TBC1D24]] | -0.62 | -0.63 / -0.36 | both halves | 1e-04 |  |
| [[ATRN]] | -0.62 | -0.58 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA6]] | B | ABCA6 activity raises ABCA10's level | lines that do not express ABCA6 (26) vs lines expressing it (24) | 3.04× lower at baseline in the lines without ABCA6 | 2e-04 | ⚠ within organs, on part of the lines; also absent: LINC02154, IGF2, LYPLAL1-DT |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity raises ABCA10's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 2.35× lower at baseline in the lines without ZNF341-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[ZHX2]] | B | ZHX2 activity raises ABCA10's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without ZHX2 | 0.080 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[YBX3]] | C | YBX3 activity raises ABCA10's level | lines that do not express YBX3 (4) vs lines expressing it (46) | 2.87× lower at baseline in the lines without YBX3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPATA13, RNF103-CHMP3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCT6B]] | B | ABCA10 activity raises CCT6B's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.49× lower at baseline in the lines without ABCA10 | 0.011 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[GARIN1A]] | B | ABCA10 activity raises GARIN1A's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.15× lower at baseline in the lines without ABCA10 | 0.021 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[RCBTB2]] | B | ABCA10 activity raises RCBTB2's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.35× lower at baseline in the lines without ABCA10 | 0.022 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[RIPK2-DT]] | B | ABCA10 activity raises RIPK2-DT's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.45× lower at baseline in the lines without ABCA10 | 0.030 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[TMEM202-AS1]] | B | ABCA10 activity raises TMEM202-AS1's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.25× lower at baseline in the lines without ABCA10 | 0.035 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[LINC02362]] | B | ABCA10 activity raises LINC02362's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.35× lower at baseline in the lines without ABCA10 | 0.035 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[MEPCE]] | B | ABCA10 activity raises MEPCE's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.54× lower at baseline in the lines without ABCA10 | 0.038 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[ACTR3-AS1]] | B | ABCA10 activity raises ACTR3-AS1's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.74× lower at baseline in the lines without ABCA10 | 0.049 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[LACC1]] | B | ABCA10 activity raises LACC1's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 2.52× lower at baseline in the lines without ABCA10 | 0.058 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[LINC01191]] | B | ABCA10 activity raises LINC01191's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.58× lower at baseline in the lines without ABCA10 | 0.064 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[LINC01004]] | B | ABCA10 activity raises LINC01004's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.62× lower at baseline in the lines without ABCA10 | 0.067 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[WDR5]] | B | ABCA10 activity lowers WDR5's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.41× higher at baseline in the lines without ABCA10 | 0.070 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.672). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.8, -11.8); signed map (19.5, 5.4). **Vector** length 98.0, 23.8% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.6 | +20.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.0 | +0.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.9 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +5.0 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.8 | +0.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +1.7 | +4.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.9 | -5.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.8 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily A member 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.3 — chr17:69,147,214-69,244,846 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EST698739 |
| Gene groups (HGNC) | ATP binding cassette subfamily A |
| Reactome | 3 pathways, smallest: ABC transporters in lipid homeostasis; ABC-family protein mediated transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWZ4](https://www.uniprot.org/uniprotkb/Q8WWZ4) (ATP-binding cassette sub-family A member 10):

> Probable transporter which may play a role in macrophage lipid transport and homeostasis.

**Summary**, from NCBI Gene [10349](https://www.ncbi.nlm.nih.gov/gene/10349):

> The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intracellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, and White). This encoded protein is a member of the ABC1 subfamily. Members of the ABC1 subfamily comprise the only major ABC subfamily found exclusively in multicellular eukaryotes. This gene …

**Accessions** — [HGNC:30](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30) · Entrez [10349](https://www.ncbi.nlm.nih.gov/gene/10349) · UniProt [Q8WWZ4](https://www.uniprot.org/uniprotkb/Q8WWZ4) · Ensembl [ENSG00000154263](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154263)

## Data

Gene col 7791: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7791); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7791, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7791]; `tensor/DDL_lfc|DDL_z.npy` [7791]; `embed/gene_vectors.npy` [7791]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7791 or target_col == 7791). Every well: [[ABCA10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCA10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
