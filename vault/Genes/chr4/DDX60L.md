---
symbol: "DDX60L"
type: "gene"
col: 11183
ensembl_id: "ENSG00000181381"
name: "DExD/H-box 60 like"
location: "4q32.3"
module: 32
arm: "+"
pooled_cpm: 133.53
n_lines_expressing: 43
n_dd_up: 18
n_dd_down: 49
n_dd_up_clean: 16
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 56
direction_downstream: 44
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# DDX60L

*DExD/H-box 60 like* — 4q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.07× (z +7.0, q 2e-09, up in 28 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 49 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.176× (z -16.5, q 0e+00, down in 41 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARP14]] (+0.92, fdr 7e-06), [[DDX60]] (+0.92, fdr 7e-06, ⚠ same locus), [[HERC6]] (+0.91, fdr 7e-06), [[PARP9]] (+0.91, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 56 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); 44 go from it, the strongest it → [[DDX60]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11183.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.07×** | +7.0 | 2e-09 | 28/41 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **2.00×** | +6.4 | 5e-08 | 36/40 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.6 | 4e-06 | 33/41 (SW1417, SW 900, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.87×** | +5.5 | 4e-06 | 28/41 (NCI-H2347, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.63×** | +4.3 | 0.002 | 32/40 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.52×** | +4.2 | 0.002 | 30/43 (NCI-H460, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.38×** | +3.8 | 0.009 | 26/41 (NCI-H460, CFPAC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.009 | 31/42 (NCI-H460, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.009 | 27/41 (NCI-H460, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.014 | 27/41 (NCI-H460, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.014 | 27/41 (NCI-H460, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.030 | 21/41 (LOX-IMVI, SNU-1, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.45×** | +3.4 | 0.030 | 26/41 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.043 | 23/41 (HS-578T, A-172, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.043 | 26/42 (CFPAC-1, RKO, …) | all doses, flat |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.48×** | +3.2 | 0.057 | 28/42 (SHP-77, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 49 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11183.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.176×** | -16.5 | 0e+00 | 41/41 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.235×** | -13.8 | 6e-41 | 40/41 (LoVo, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.246×** | -13.4 | 2e-38 | 39/41 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.458×** | -10.5 | 1e-23 | 33/42 (MIA PaCa-2, COLO 205, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.371×** | -9.4 | 4e-19 | 41/41 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.373×** | -9.4 | 6e-19 | 38/42 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.361×** | -9.3 | 9e-19 | 36/40 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.515×** | -8.9 | 3e-17 | 33/42 (MIA PaCa-2, A549, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.431×** | -8.0 | 7e-14 | 34/41 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.432×** | -8.0 | 8e-14 | 32/42 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.442×** | -7.8 | 4e-13 | 33/41 (LoVo, RKO, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.466×** | -7.3 | 2e-11 | 31/41 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.593×** | -7.0 | 1e-10 | 31/41 (COLO 205, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.517×** | -6.3 | 2e-08 | 30/41 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.527×** | -6.1 | 4e-08 | 31/41 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.310×** | -5.8 | 2e-07 | 33/42 (A549, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.530×** | -5.7 | 4e-07 | 28/41 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 5 µM |  | **0.332×** | -5.5 | 1e-06 | 31/41 (COLO 205, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11183. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 264 | 0 | 19 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0629× (z -21.6) |
| [[MIA PaCa-2 (line)]] | alt | 265 | 1 | 18 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.82× (z +9.4) | [[Tofacitinib (drug)]] 5 µM 0.114× (z -18.5) |
| [[A549 (line)]] | wt | 359 | 0 | 18 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0636× (z -17.1) |
| [[NCI-H1573 (line)]] | alt | 109 | 1 | 16 (7 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.08× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -15.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.125× (z -14.8) |
| [[BT-474 (line)]] | alt | 183 | 0 | 16 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0866× (z -13.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.0992× (z -12.9) |
| [[RPMI-7951 (line)]] | alt | 233 | 0 | 16 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -15.4) |
| [[NCI-H23 (line)]] | alt | 77.4 | 0 | 15 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0857× (z -14.2) |
| [[A-172 (line)]] | wt | 216 | 2 | 12 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.37× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.0756× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.126× (z -15.0) |
| [[RKO (line)]] | wt | 154 | 0 | 12 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0618× (z -17.4) |
| [[AsPC-1 (line)]] | alt | 449 | 0 | 11 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.142× (z -13.9) |
| [[SNU-423 (line)]] | alt | 166 | 0 | 11 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.117× (z -14.7) |
| [[NCI-H2347 (line)]] | alt | 233 | 4 (2 ⚠) | 6 | [[Homoharringtonine (drug)]] 0.5 µM 6.32× (z +13.9) | [[Tofacitinib (drug)]] 5 µM 0.280× (z -13.7) |
| [[A498 (line)]] | wt | 179 | 0 | 9 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.130× (z -14.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.234× (z -10.4) |
| [[COLO 205 (line)]] | alt | 277 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0834× (z -15.3) |
| [[PANC-1 (line)]] | alt | 43.3 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.270× (z -10.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.331× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 272 | 0 | 7 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.231× (z -14.2) |
| [[CHP-212 (line)]] | wt | 131 | 0 | 7 (1 ⚠) | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.0786× (z -12.1) |
| [[Hs 766T (line)]] | wt | 535 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.117× (z -15.9) |
| [[NCI-H1792 (line)]] | alt | 212 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.104× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 90.4 | 1 | 5 (2 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.76× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.182× (z -15.0) |
| [[Panc 03.27 (line)]] | alt | 155 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.22× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0916× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.236× (z -9.7) |
| [[HS-578T (line)]] | alt | 89.6 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.45× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.153× (z -11.6) |
| [[KATO III (line)]] | alt | 108 | 0 | 4 | — | [[Tofacitinib (drug)]] 5 µM 0.332× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 89.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0978× (z -16.9) |
| [[LS 180 (line)]] | wt | 71.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.222× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 55.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.252× (z -13.0) |
| [[H4 (line)]] | wt | 89.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -10.1) |
| [[HCT15 (line)]] | alt | 67.4 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +14.0) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.169× (z -11.6) |
| [[SHP-77 (line)]] | alt | 56.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -10.8) |
| [[SW 900 (line)]] | alt | 67.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -9.0) |
| [[C-33 A (line)]] | alt | 47.9 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.247× (z -8.6) |
| [[NCI-H661 (line)]] | alt | 45.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0325× (z -8.7) ⚠ cell-cycle shift, explains ~78% of this change |
| [[A-427 (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 29.9 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.1 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.8 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 11.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11183), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARP14]] | +0.92 | +0.88 / +0.92 | both halves | 7e-06 | STRING 582 |
| [[DDX60]] | +0.92 | +0.90 / +0.93 | both halves | 7e-06 | same gene group; STRING 773; ⚠ same locus (37.9 kb, same strand: neighbours can correlate without regulation) |
| [[HERC6]] | +0.91 | +0.86 / +0.92 | both halves | 7e-06 | STRING 466 |
| [[PARP9]] | +0.91 | +0.84 / +0.94 | both halves | 7e-06 | STRING 807 |
| [[SAMD9L]] | +0.90 | +0.86 / +0.92 | both halves | 7e-06 | STRING 843 |
| [[OAS2]] | +0.90 | +0.81 / +0.94 | both halves | 7e-06 | STRING 578 |
| [[SAMD9]] | +0.89 | +0.86 / +0.91 | both halves | 7e-06 | STRING 815 |
| [[OAS3]] | +0.89 | +0.82 / +0.93 | both halves | 7e-06 | STRING 533 |
| [[XAF1]] | +0.89 | +0.81 / +0.91 | both halves | 7e-06 | STRING 589 |
| [[RSAD2]] | +0.88 | +0.82 / +0.91 | both halves | 7e-06 | STRING 616 |
| [[DTX3L]] | +0.88 | +0.82 / +0.89 | both halves | 7e-06 | STRING 512 |
| [[MX1]] | +0.88 | +0.80 / +0.92 | both halves | 7e-06 | STRING 446 |
| [[RIGI]] | +0.88 | +0.80 / +0.90 | both halves | 7e-06 | STRING 844 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*56 arrows, 56 of them with an alert ⚠; grade A 0, B 45, C 11. Shown: the 12 strongest; 44 more arrows (44 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity raises DDX60L's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 3.96× lower at baseline in the lines without OAS2 | 1e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[SAMD9L]] | B | SAMD9L activity raises DDX60L's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 3.40× lower at baseline in the lines without SAMD9L | 4e-04 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[MX1]] | B | MX1 activity raises DDX60L's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.89× lower at baseline in the lines without MX1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[GBP4]] | B | GBP4 activity raises DDX60L's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 3.58× lower at baseline in the lines without GBP4 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[TRIM22]] | B | TRIM22 activity raises DDX60L's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 3.09× lower at baseline in the lines without TRIM22 | 0.001 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[RSAD2]] | B | RSAD2 activity raises DDX60L's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 3.03× lower at baseline in the lines without RSAD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[IFI6]] | B | IFI6 activity raises DDX60L's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 3.30× lower at baseline in the lines without IFI6 | 0.002 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity raises DDX60L's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 3.07× lower at baseline in the lines without OAS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[IFI44]] | B | IFI44 activity raises DDX60L's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 3.34× lower at baseline in the lines without IFI44 | 0.003 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[SAMD9]] | B | SAMD9 activity raises DDX60L's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 3.87× lower at baseline in the lines without SAMD9 | 0.006 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[GBP1]] | B | GBP1 activity raises DDX60L's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 3.32× lower at baseline in the lines without GBP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[OASL]] | B | OASL activity raises DDX60L's level | lines that do not express OASL (10) vs lines expressing it (40) | 3.03× lower at baseline in the lines without OASL | 0.009 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |

### Downstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 40, C 4. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDX60]] | B | DDX60L activity raises DDX60's level | lines that do not express DDX60L (7) vs lines expressing it (43) | 4.19× lower at baseline in the lines without DDX60L | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent |
| [[HERC6]] | B | DDX60L activity strengthens HERC6's drug response | lines that do not express DDX60L (5) vs lines expressing it (39) | the lines without DDX60L respond 0.36× as strongly (z diff +3.88); strongest at Panobinostat 0.05 µM: 0.64x vs 0.25x (z diff +5.0) | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[IFIT1]] | B | DDX60L activity raises IFIT1's level | lines that do not express DDX60L (7) vs lines expressing it (43) | 3.49× lower at baseline in the lines without DDX60L | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent |
| [[RIGI]] | B | DDX60L activity raises RIGI's level | lines that do not express DDX60L (7) vs lines expressing it (43) | 2.69× lower at baseline in the lines without DDX60L | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent |
| [[HERC6]] | B | DDX60L activity raises HERC6's level | lines that do not express DDX60L (7) vs lines expressing it (43) | 2.87× lower at baseline in the lines without DDX60L | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent |
| [[TDRD7]] | B | DDX60L activity raises TDRD7's level | lines that do not express DDX60L (7) vs lines expressing it (43) | 1.81× lower at baseline in the lines without DDX60L | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent |
| [[IFI44]] | B | DDX60L activity raises IFI44's level | lines that do not express DDX60L (7) vs lines expressing it (43) | 4.50× lower at baseline in the lines without DDX60L | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent |
| [[PML]] | B | DDX60L activity raises PML's level | lines that do not express DDX60L (7) vs lines expressing it (43) | 2.19× lower at baseline in the lines without DDX60L | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent |
| [[IFIT3]] | B | DDX60L activity raises IFIT3's level | lines that do not express DDX60L (7) vs lines expressing it (43) | 3.79× lower at baseline in the lines without DDX60L | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent |
| [[TRANK1]] | B | DDX60L activity raises TRANK1's level | lines that do not express DDX60L (7) vs lines expressing it (43) | 2.51× lower at baseline in the lines without DDX60L | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent |
| [[RSAD2]] | B | DDX60L activity raises RSAD2's level | lines that do not express DDX60L (7) vs lines expressing it (43) | 3.40× lower at baseline in the lines without DDX60L | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent |
| [[STX17]] | B | DDX60L activity raises STX17's level | lines that do not express DDX60L (7) vs lines expressing it (43) | 1.20× lower at baseline in the lines without DDX60L | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.921). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.5, 54.0); signed map (63.8, 32.1). **Vector** length 156, 64.7% of its response variance represented; |z| ≥ 3 in 1,796 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.76 to 56); *interferon gamma response* (hallmark, mean cos +0.77 to 60); *interferon* (control, mean cos +0.84 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +14.2 | +7.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +13.1 | +5.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.3 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.2 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.6 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.4 | +6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.4 | +3.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.1 | +3.8 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -10.5 | -10.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -9.4 | -8.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -8.9 | -8.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -8.6 | -7.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -7.6 | -9.4 |

## What is on record

|  |  |
|---|---|
| Name | DExD/H-box 60 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.3 — chr4:168,356,735-168,537,786 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31033 |
| Gene groups (HGNC) | Ski2 like RNA helicases |
| Matched by | ensembl_id |

UniProt [Q5H9U9](https://www.uniprot.org/uniprotkb/Q5H9U9) carries no function annotation.

**Summary**, from NCBI Gene [91351](https://www.ncbi.nlm.nih.gov/gene/91351):

> This gene encodes a member of the DExD/H-box helicase family of proteins, a subset of the super family 2 helicases. Members of the DExD/H-box helicase family share a conserved functional core comprised of two RecA-like globular domains. These domains contain conserved motifs that mediate ATP binding, ATP hydrolysis, nucleic acid binding, and RNA unwinding. In addition to functions in RNA metabolism, members of this family are involved in anti-viral immunity and act as cytosolic sensors of viral …

**Accessions** — [HGNC:26429](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26429) · Entrez [91351](https://www.ncbi.nlm.nih.gov/gene/91351) · UniProt [Q5H9U9](https://www.uniprot.org/uniprotkb/Q5H9U9) · Ensembl [ENSG00000181381](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181381)

## Data

Gene col 11183: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11183); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11183, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11183]; `tensor/DDL_lfc|DDL_z.npy` [11183]; `embed/gene_vectors.npy` [11183]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11183 or target_col == 11183). Every well: [[DDX60L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX60L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
