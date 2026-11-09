---
symbol: "SLC30A9"
type: "gene"
col: 288
ensembl_id: "ENSG00000014824"
name: "solute carrier family 30 member 9"
location: "4p13"
module: 148
arm: "+"
pooled_cpm: 93.16
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# SLC30A9

*solute carrier family 30 member 9* — 4p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +12.4, q 3e-32, up in 34 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.588× (z -12.9, q 3e-35, down in 37 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.665× (z -9.9, q 9e-21, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCNP]] (+0.64, fdr 1e-05), [[ALG13]] (+0.64, fdr 1e-05), [[MCTS1]] (+0.63, fdr 1e-05); moves opposite to [[NR2F6]] (-0.67, fdr 7e-06), [[MRPL34]] (-0.62, fdr 1e-05), [[ST3GAL4]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 288.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +12.4 | 3e-32 | 34/49 (AsPC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +10.5 | 2e-23 | 33/49 (NCI-H2347, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +10.0 | 3e-21 | 38/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +9.5 | 2e-19 | 30/43 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +8.4 | 6e-15 | 27/48 (RKO, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +7.5 | 7e-12 | 30/50 (SW480, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +7.1 | 1e-10 | 32/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +7.0 | 1e-10 | 30/45 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +6.9 | 3e-10 | 27/48 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +6.7 | 1e-09 | 30/48 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.30×** | +6.4 | 7e-09 | 29/48 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.057 | 13/49 (RKO, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.057 | 14/48 (A-427, RKO, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.14× | +3.1 | 0.068 | 16/48 (A498, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 288.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.588×** | -12.9 | 3e-35 | 37/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.650×** | -10.1 | 2e-21 | 39/47 (SK-MEL-2, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.665×** | -9.9 | 9e-21 | 36/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.754×** | -6.8 | 1e-09 | 31/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.755×** | -6.8 | 1e-09 | 32/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.774×** | -6.2 | 5e-08 | 27/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.821×** | -4.8 | 1e-04 | 23/48 (PANC-1, J82, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.832×** | -4.5 | 6e-04 | 22/47 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.858× | -3.7 | 0.015 | 18/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -3.6 | 0.015 | 20/48 (PANC-1, C32, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | 0.861× | -3.6 | 0.015 | 20/48 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 0.899× | -3.6 | 0.015 | 8/48 (AsPC-1, NCI-H1792, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.778×** | -3.1 | 0.085 | 20/45 (H4, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.961× | -3.1 | 0.085 | 0/50 | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | 0.839× | -3.0 | 0.093 | 17/48 (LoVo, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 288. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 104 | 4 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +11.1) | [[Digitoxin (drug)]] 5 µM 0.426× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.509× (z -11.4) |
| [[PANC-1 (line)]] | alt | 85.2 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.386× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.450× (z -12.6) |
| [[NCI-H2347 (line)]] | alt | 73.1 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +9.0) | — |
| [[RKO (line)]] | wt | 102 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +14.1) | [[Dinaciclib (drug)]] 0.05 µM 0.376× (z -10.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 102 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.97× (z +9.3) ⚠ toxic; transcription drop | [[Niclosamide (olamine) (drug)]] 5 µM 0.455× (z -10.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.494× (z -10.0) |
| [[H4 (line)]] | wt | 177 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.371× (z -10.0) |
| [[J82 (line)]] | alt | 80.0 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.270× (z -15.8) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.456× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 80.8 | 1 | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +9.1) | [[Ixazomib citrate (drug)]] 5 µM 0.465× (z -11.0) |
| [[A498 (line)]] | wt | 81.6 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.08× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 82.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 101 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.349× (z -10.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 168 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.346× (z -10.7) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.391× (z -9.9) |
| [[HOP62 (line)]] | alt | 135 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.396× (z -13.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 121 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +11.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.447× (z -11.2) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 78.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +12.1) | [[Lonafarnib (drug)]] 5 µM 0.179× (z -10.4) ⚠ toxic |
| [[SW1417 (line)]] | alt | 60.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +9.2) | — |
| [[A-172 (line)]] | wt | 98.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.07× (z +8.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 60.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +12.6) | — |
| [[C32 (line)]] | wt | 100 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.414× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 101 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 78.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +13.2) | — |
| [[HEC-1-A (line)]] | alt | 123 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 1.94× (z +9.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 82.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +11.4) | — |
| [[KATO III (line)]] | alt | 94.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.469× (z -9.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 50.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.57× (z +9.2) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 100 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +11.9) | — |
| [[NCI-H1792 (line)]] | alt | 94.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.20× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.226× (z -18.9) ⚠ toxic |
| [[A549 (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 132 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 107 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 142 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 84.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 62.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 288), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNP]] | +0.64 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ALG13]] | +0.64 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[MCTS1]] | +0.63 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[TSTD2]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[USO1]] | +0.62 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[LMBRD2]] | +0.61 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[MRPL30]] | +0.61 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[UBE3B]] | +0.61 | +0.75 / +0.42 | both halves | 4e-05 |  |
| [[UEVLD]] | +0.60 | +0.61 / +0.51 | both halves | 1e-05 | STRING 609 |
| [[MCPH1-AS1]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[TLN1]] | +0.59 | +0.34 / +0.63 | both halves | 1e-04 |  |
| [[PSME3IP1]] | +0.58 | +0.53 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR2F6]] | -0.67 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[MRPL34]] | -0.62 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[ST3GAL4]] | -0.62 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[TSPAN33]] | -0.60 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[C15orf61]] ⚠ | -0.59 | -0.30 / -0.60 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CDC14B]] | -0.58 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[ARHGEF10L]] | -0.57 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[CMTM8]] | -0.56 | -0.63 / -0.36 | both halves | 1e-04 |  |
| [[LSM2]] | -0.56 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[SNN]] | -0.56 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[MRPL14]] | -0.55 | -0.27 / -0.58 | both halves | 3e-04 |  |
| [[ARHGAP44]] | -0.54 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[BRF1]] | -0.54 | -0.64 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC30A9's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises SLC30A9's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers SLC30A9's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.757). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-7.4, 2.2); signed map (16.2, -28.7). **Vector** length 115, 33.0% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +7.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +10.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +10.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +3.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.8 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +6.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +2.0 | +1.9 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.6 | -10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -0.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.7 | -12.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.3 | -9.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -4.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 30 member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p13 — chr4:41,990,502-42,090,461 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HUEL, ZNT9, GAC63; previously C4orf1 |
| Gene groups (HGNC) | Solute carrier family 30 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PML9](https://www.uniprot.org/uniprotkb/Q6PML9) (Proton-coupled zinc antiporter SLC30A9, mitochondrial):

> Mitochondrial proton-coupled zinc ion antiporter mediating the export of zinc from the mitochondria and involved in zinc homeostasis, zinc mobilization as well as mitochondrial morphology and health. In nucleus, functions as a secondary coactivator for nuclear receptors by cooperating with p160 coactivators subtypes. Plays a role in transcriptional activation of Wnt-responsive genes (By similarity).

**Summary**, from NCBI Gene [10463](https://www.ncbi.nlm.nih.gov/gene/10463):

> Enables zinc ion transmembrane transporter activity. Involved in intracellular zinc ion homeostasis; regulation of mitochondrion organization; and zinc ion transport. Located in several cellular components, including cytoplasmic vesicle; endoplasmic reticulum; and mitochondrial membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1329](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1329) · Entrez [10463](https://www.ncbi.nlm.nih.gov/gene/10463) · UniProt [Q6PML9](https://www.uniprot.org/uniprotkb/Q6PML9) · Ensembl [ENSG00000014824](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000014824)

## Data

Gene col 288: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 288); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 288, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 288]; `tensor/DDL_lfc|DDL_z.npy` [288]; `embed/gene_vectors.npy` [288]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 288 or target_col == 288). Every well: [[SLC30A9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC30A9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
