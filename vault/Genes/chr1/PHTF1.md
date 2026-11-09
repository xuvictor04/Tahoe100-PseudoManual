---
symbol: "PHTF1"
type: "gene"
col: 3841
ensembl_id: "ENSG00000116793"
name: "putative homeodomain transcription factor 1"
location: "1p13.2"
module: 60
arm: "+"
pooled_cpm: 44.56
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# PHTF1

*putative homeodomain transcription factor 1* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.82× (z +22.4, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.642× (z -9.2, q 2e-17, down in 29 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.669× (z -8.7, q 1e-15, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SFXN5]] (+0.72, fdr 7e-06), [[PSMC1]] (+0.64, fdr 1e-05), [[ANKUB1]] (+0.63, fdr 8e-06); moves opposite to [[WASHC4]] (-0.55, fdr 1e-05), [[RNF141]] (-0.52, fdr 4e-05), [[C6orf89]] (-0.50, fdr 9e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[B4GALNT1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3841.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.82×** | +22.4 | 0e+00 | 46/47 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.77×** | +22.0 | 0e+00 | 45/47 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.66×** | +20.0 | 0e+00 | 47/47 (LoVo, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.85×** | +9.5 | 4e-19 | 38/47 (SW480, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +9.4 | 5e-19 | 27/46 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +8.4 | 5e-15 | 36/47 (SW480, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +7.0 | 2e-10 | 31/47 (C32, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +6.1 | 7e-08 | 26/42 (SHP-77, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.47×** | +4.3 | 1e-03 | 19/47 (RKO, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 1.12× | +3.5 | 0.029 | 15/47 (NCI-H2347, J82, …) | top dose only | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.12 | 10/46 (LoVo, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3841.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.642×** | -9.2 | 2e-17 | 29/46 (HepG2/C3A, A-427, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.669×** | -8.7 | 1e-15 | 36/47 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.677×** | -8.4 | 5e-15 | 28/46 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.678×** | -8.4 | 5e-15 | 29/47 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.679×** | -8.4 | 6e-15 | 26/47 (SHP-77, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.724×** | -7.0 | 3e-10 | 26/47 (SHP-77, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.739×** | -6.3 | 2e-08 | 22/47 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.748×** | -6.3 | 2e-08 | 26/47 (PANC-1, SW48, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.781×** | -5.2 | 2e-05 | 23/47 (PANC-1, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.800×** | -4.8 | 7e-05 | 22/47 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.798×** | -4.7 | 1e-04 | 20/46 (A-172, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.798×** | -4.5 | 3e-04 | 22/46 (A549, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **0.830×** | -4.1 | 0.002 | 19/47 (SHP-77, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.835× | -3.9 | 0.004 | 18/47 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.847× | -3.6 | 0.012 | 6/47 (NCI-H2030, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3841. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 54.3 | 3 | 6 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.23× (z +11.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.392× (z -13.7) |
| [[HepG2_C3A (line)]] | wt | 93.6 | 3 | 5 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.38× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.352× (z -9.2) |
| [[SW480 (line)]] | alt | 67.8 | 4 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.77× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.516× (z -9.2) |
| [[LoVo (line)]] | wt | 44.2 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.08× (z +18.2) | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 53.5 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.70× (z +8.8) | [[Harringtonine (drug)]] 0.5 µM 0.286× (z -11.0) |
| [[C32 (line)]] | wt | 58.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.14× (z +14.3) | — |
| [[HOP62 (line)]] | alt | 29.5 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.37× (z +13.3) | — |
| [[hTERT-HPNE (line)]] | wt | 39.9 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 4.23× (z +10.3) | [[vincristine (drug)]] 5 µM 0.0867× (z -9.2) |
| [[J82 (line)]] | alt | 64.5 | 2 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.12× (z +8.6) | [[Harringtonine (drug)]] 5 µM 0.463× (z -8.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 50.8 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.89× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 75.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.379× (z -9.6) |
| [[SW1417 (line)]] | alt | 36.0 | 3 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.27× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 18.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +10.4) | — |
| [[COLO 205 (line)]] | alt | 30.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 8.84× (z +13.2) | — |
| [[Hs 766T (line)]] | wt | 43.9 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.45× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 36.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.75× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 23.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.43× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 44.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.56× (z +14.2) | — |
| [[NCI-H2030 (line)]] | alt | 32.7 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.236× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 79.3 | 1 | 2 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.38× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -23.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.446× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 31.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.11× (z +14.5) | — |
| [[NCI-H460 (line)]] | wt | 26.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.72× (z +13.4) | — |
| [[SNU-423 (line)]] | alt | 44.1 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.25× (z +10.4) | — |
| [[A-427 (line)]] | wt | 66.7 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.323× (z -11.3) ⚠ toxic |
| [[A498 (line)]] | wt | 33.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.77× (z +9.4) | — |
| [[H4 (line)]] | wt | 44.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.94× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 51.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +10.1) | — |
| [[RKO (line)]] | wt | 70.1 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.353× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 65.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.11× (z +10.2) | — |
| [[SK-MEL-2 (line)]] | alt | 112 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.346× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 32.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.307× (z -10.4) ⚠ toxic |
| [[KATO III (line)]] | alt | 28.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.87× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 39.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +10.8) | — |
| [[SW 1271 (line)]] | alt | 44.7 | 0 | 1 | — | [[Bicalutamide (drug)]] 0.5 µM 0.0482× (z -9.6) |
| [[AN3 CA (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 95.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3841), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFXN5]] | +0.72 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[PSMC1]] | +0.64 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[ANKUB1]] | +0.63 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[PSMB5]] | +0.61 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[FERMT3]] | +0.59 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[HSP90AA2P]] | +0.59 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[SERPINH1]] | +0.59 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[PSMA1]] | +0.59 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[TIRAP]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[HSPE1]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SMIM10L1]] | +0.58 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[VCP]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASHC4]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[RNF141]] | -0.52 | -0.52 / -0.40 | both halves | 4e-05 |  |
| [[C6orf89]] | -0.50 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[YY1AP1]] | -0.47 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[ZMIZ2]] | -0.47 | -0.42 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B4GALNT1]] | B | B4GALNT1 activity raises PHTF1's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 1.59× lower at baseline in the lines without B4GALNT1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1 |
| [[PSMB5]] | B | PSMB5 activity lowers PHTF1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.616). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-12.5, 19.6); signed map (-24.6, -24.0). **Vector** length 128, 35.4% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +13.4 | +22.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +13.0 | +20.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +11.9 | +22.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +8.2 | +6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +7.3 | +8.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +6.8 | +9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +7.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.3 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +2.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.4 | -8.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.4 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -6.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.6 | -7.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | -8.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.6 | -5.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -4.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.8 | -4.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | putative homeodomain transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:113,696,831-113,759,489 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PHTF |
| Matched by | ensembl_id |

UniProt [Q9UMS5](https://www.uniprot.org/uniprotkb/Q9UMS5) carries no function annotation.

**Summary**, from NCBI Gene [10745](https://www.ncbi.nlm.nih.gov/gene/10745):

> Predicted to be located in cis-Golgi network membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:8939](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8939) · Entrez [10745](https://www.ncbi.nlm.nih.gov/gene/10745) · UniProt [Q9UMS5](https://www.uniprot.org/uniprotkb/Q9UMS5) · Ensembl [ENSG00000116793](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116793)

## Data

Gene col 3841: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3841); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3841, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3841]; `tensor/DDL_lfc|DDL_z.npy` [3841]; `embed/gene_vectors.npy` [3841]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3841 or target_col == 3841). Every well: [[PHTF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHTF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
