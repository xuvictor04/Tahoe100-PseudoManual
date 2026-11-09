---
symbol: "SOD2"
type: "gene"
col: 16635
ensembl_id: "ENSG00000291237"
name: "superoxide dismutase 2"
location: "6q25.3"
module: 139
arm: "+"
pooled_cpm: 311.36
n_lines_expressing: 47
n_dd_up: 30
n_dd_down: 12
n_dd_up_clean: 27
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 19
direction_downstream: 5
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# SOD2

*superoxide dismutase 2* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.10× (z +14.2, q 7e-43, up in 35 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.660× (z -5.6, q 1e-05, down in 28 of 45 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Tofacitinib (drug)]] 5 µM: 0.765× (z -5.1, q 8e-05, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1RL]] (+0.71, fdr 7e-06), [[WTAP]] (+0.69, fdr 7e-06, ⚠ same locus), [[TNFAIP3]] (+0.65, fdr 7e-06), [[ZC3H12A]] (+0.64, fdr 7e-06); moves opposite to [[HHIP]] (-0.50, fdr 3e-05), [[AP3M2]] (-0.49, fdr 4e-05), [[EPN2]] (-0.48, fdr 8e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[RHCG]] → it (grade B ⚠); 5 go from it, the strongest it → [[THBS3-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16635.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.10×** | +14.2 | 7e-43 | 35/45 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **6.29×** | +13.0 | 4e-36 | 43/46 (LoVo, BT-474, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.14×** | +9.9 | 1e-20 | 33/45 (HOP62, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +7.4 | 2e-11 | 35/45 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +6.7 | 2e-09 | 27/45 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.65×** | +6.6 | 5e-09 | 32/47 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +5.6 | 2e-06 | 31/45 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.49×** | +5.4 | 5e-06 | 30/45 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +5.4 | 5e-06 | 31/45 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.11×** | +5.3 | 7e-06 | 31/45 (HEC-1-A, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **2.06×** | +5.1 | 2e-05 | 35/47 (PANC-1, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.45×** | +5.1 | 2e-05 | 35/46 (PANC-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.47×** | +5.0 | 3e-05 | 27/45 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +4.9 | 4e-05 | 24/45 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +4.6 | 1e-04 | 26/45 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.33×** | +4.4 | 4e-04 | 26/45 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.85×** | +4.3 | 5e-04 | 28/46 (LoVo, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16635.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.660×** | -5.6 | 1e-05 | 28/45 (NCI-H1792, A549, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.765×** | -5.1 | 8e-05 | 26/46 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.699×** | -4.9 | 2e-04 | 33/46 (MIA PaCa-2, SW 900, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.702×** | -4.8 | 2e-04 | 31/45 (SNU-423, A549, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.709×** | -4.7 | 4e-04 | 25/45 (BT-474, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.705×** | -4.6 | 5e-04 | 26/44 (SNU-423, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.722×** | -4.4 | 8e-04 | 29/45 (A-172, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.802×** | -4.2 | 0.002 | 23/46 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.751×** | -3.9 | 0.006 | 25/45 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.765×** | -3.6 | 0.016 | 23/45 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.773×** | -3.5 | 0.025 | 22/46 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.682×** | -3.3 | 0.048 | 20/45 (CFPAC-1, SW 900, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16635. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 433 | 11 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.58× (z +13.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 305 | 9 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 1.87× (z +16.0) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 3.14× (z +9.6) | [[Tofacitinib (drug)]] 5 µM 0.384× (z -9.9) |
| [[HOP62 (line)]] | alt | 157 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.0× (z +25.3) | — |
| [[LOX-IMVI (line)]] | wt | 91.3 | 9 | 0 | [[Trametinib (drug)]] 5 µM 6.87× (z +14.4) | — |
| [[SNU-423 (line)]] | alt | 2,150 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 152 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +15.2) | — |
| [[HS-578T (line)]] | alt | 486 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +11.1) | — |
| [[LoVo (line)]] | wt | 119 | 6 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 23.3× (z +17.7) | — |
| [[PANC-1 (line)]] | alt | 206 | 6 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.19× (z +10.6) | — |
| [[A549 (line)]] | wt | 632 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.268× (z -11.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -9.6) |
| [[BT-474 (line)]] | alt | 180 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 30.8× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.246× (z -11.4) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H1573 (line)]] | alt | 611 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 14.0× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 896 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.221× (z -11.7) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -9.9) |
| [[SW48 (line)]] | wt | 118 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +17.9) | — |
| [[A-172 (line)]] | wt | 336 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.84× (z +12.8) | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -10.1) ⚠ cell-cycle shift, explains ~53% of this change |
| [[CFPAC-1 (line)]] | alt | 236 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +17.1) | [[Tofacitinib (drug)]] 5 µM 0.491× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 362 | 3 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.46× (z +14.2) | [[Bortezomib (drug)]] 0.05 µM 0.349× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 725 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +13.1) | — |
| [[AsPC-1 (line)]] | alt | 204 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +18.6) | — |
| [[HT-29 (line)]] | alt | 141 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +13.1) | — |
| [[Panc 03.27 (line)]] | alt | 212 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +16.7) | — |
| [[RPMI-7951 (line)]] | alt | 436 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 5.86× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 89.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 119 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +12.0) | — |
| [[H4 (line)]] | wt | 148 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.29× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 398 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 694 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +13.2) | — |
| [[J82 (line)]] | alt | 430 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +14.1) | — |
| [[Hs 766T (line)]] | wt | 214 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.35× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 105 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 178 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.29× (z +10.3) | — |
| [[SW1417 (line)]] | alt | 110 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.83× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 63.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 177 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 160 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 340 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 72.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 93.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 70.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 656 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 340 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 375 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 99.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16635), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1RL]] | +0.71 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[WTAP]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[TNFAIP3]] | +0.65 | +0.62 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 480 |
| [[ZC3H12A]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TNFAIP6]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 412 |
| [[BCL6]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NFKBIA]] | +0.63 | +0.64 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 705 |
| [[IL1R1]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[OGFRL1]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[KYNU]] | +0.61 | +0.56 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[FTH1]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 | STRING 501 |
| [[CEBPD]] | +0.60 | +0.65 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CFH]] | +0.60 | +0.57 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HHIP]] | -0.50 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[AP3M2]] | -0.49 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[EPN2]] | -0.48 | -0.48 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 19, C 0. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHCG]] | B | RHCG activity raises SOD2's level | lines that do not express RHCG (33) vs lines expressing it (17) | 2.35× lower at baseline in the lines without RHCG | 0.008 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[GBP1]] | B | GBP1 activity raises SOD2's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.27× lower at baseline in the lines without GBP1 | 0.011 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[ROS1]] | B | ROS1 activity raises SOD2's level | lines that do not express ROS1 (30) vs lines expressing it (20) | 2.36× lower at baseline in the lines without ROS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: COL1A1, APCDD1L, GYPC; maybe low, not absent |
| [[TNFAIP2]] | B | TNFAIP2 activity raises SOD2's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 2.48× lower at baseline in the lines without TNFAIP2 | 0.019 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[CP]] | B | CP activity raises SOD2's level | lines that do not express CP (39) vs lines expressing it (11) | 3.15× lower at baseline in the lines without CP | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[NOD2]] | B | NOD2 activity raises SOD2's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 2.05× lower at baseline in the lines without NOD2 | 0.023 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[SAA2]] | B | SAA2 activity raises SOD2's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 2.48× lower at baseline in the lines without SAA2 | 0.026 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3 |
| [[TNFAIP6]] | B | TNFAIP6 activity raises SOD2's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 2.10× lower at baseline in the lines without TNFAIP6 | 0.033 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF |
| [[KYNU]] | B | KYNU activity raises SOD2's level | lines that do not express KYNU (29) vs lines expressing it (21) | 2.39× lower at baseline in the lines without KYNU | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[IL1R1]] | B | IL1R1 activity raises SOD2's level | lines that do not express IL1R1 (17) vs lines expressing it (33) | 2.69× lower at baseline in the lines without IL1R1 | 0.040 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, CXCL8, NR3C1 |
| [[STAT5A]] | B | STAT5A activity raises SOD2's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.73× lower at baseline in the lines without STAT5A | 0.040 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[PTGES]] | B | PTGES activity raises SOD2's level | lines that do not express PTGES (17) vs lines expressing it (33) | 2.52× lower at baseline in the lines without PTGES | 0.045 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THBS3-AS1]] | C | SOD2 activity lowers THBS3-AS1's level | lines that do not express SOD2 (3) vs lines expressing it (47) | 2.97× higher at baseline in the lines without SOD2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC9A3, SMOX, NDRG1; maybe low, not absent; its own permutation p |
| [[TGIF1]] | C | SOD2 activity lowers TGIF1's level | lines that do not express SOD2 (3) vs lines expressing it (47) | 2.57× higher at baseline in the lines without SOD2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC9A3, SMOX, NDRG1; maybe low, not absent; its own permutation p |
| [[B2M]] | C | SOD2 activity raises B2M's level | lines that do not express SOD2 (3) vs lines expressing it (47) | 2.22× lower at baseline in the lines without SOD2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC9A3, SMOX, NDRG1; maybe low, not absent; its own permutation p |
| [[WTAP]] | C | SOD2 activity raises WTAP's level | lines that do not express SOD2 (3) vs lines expressing it (47) | 1.46× lower at baseline in the lines without SOD2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC9A3, SMOX, NDRG1; maybe low, not absent; its own permutation p |
| [[RAB27A]] | C | SOD2 activity raises RAB27A's level | lines that do not express SOD2 (3) vs lines expressing it (47) | 2.32× lower at baseline in the lines without SOD2 | 0.093 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC9A3, SMOX, NDRG1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.699). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.9, 16.4); signed map (41.7, 5.3). **Vector** length 157, 57.1% of its response variance represented; |z| ≥ 3 in 1,671 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-4 and Interleukin-13 signaling* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (drug)]] 5 µM |  | +7.0 | +6.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.7 | +13.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +9.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +6.1 | +5.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.1 | +4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +6.0 | +4.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +5.7 | +5.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.6 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +5.5 | +4.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -2.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.4 | -4.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.2 | -1.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -6.1 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.0 | -3.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -5.3 | -3.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.9 | -4.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.9 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | superoxide dismutase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:159,669,069-159,762,529 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GC1, IPOB, MnSOD, GClnc1, lncRNA-GC1 |
| Gene groups (HGNC) | Superoxide dismutases |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, PEROXISOME, APOPTOSIS, UV_RESPONSE_UP, INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 19 pathways, smallest: Mitochondrial unfolded protein response (UPRmt); Deregulated CDK5 triggers multiple neurodegenerative pathways in Alzheimer's disease models; Neurodegenerative Diseases |
| Matched by | ensembl_id |

**Function**, from UniProt [P04179](https://www.uniprot.org/uniprotkb/P04179) (Superoxide dismutase):

> Destroys superoxide anion radicals which are normally produced within the cells and which are toxic to biological systems.

**Summary**, from NCBI Gene [6648](https://www.ncbi.nlm.nih.gov/gene/6648):

> This gene is a member of the iron/manganese superoxide dismutase family. It encodes a mitochondrial protein that forms a homotetramer and binds one manganese ion per subunit. This protein binds to the superoxide byproducts of oxidative phosphorylation and converts them to hydrogen peroxide and diatomic oxygen. Mutations in this gene have been associated with idiopathic cardiomyopathy (IDC), premature aging, sporadic motor neuron disease, and cancer. Alternative splicing of this gene results in …

**Accessions** — [HGNC:11180](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11180) · Entrez [6648](https://www.ncbi.nlm.nih.gov/gene/6648) · UniProt [P04179](https://www.uniprot.org/uniprotkb/P04179) · Ensembl [ENSG00000291237](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000291237)

## Data

Gene col 16635: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16635); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16635, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16635]; `tensor/DDL_lfc|DDL_z.npy` [16635]; `embed/gene_vectors.npy` [16635]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16635 or target_col == 16635). Every well: [[SOD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
