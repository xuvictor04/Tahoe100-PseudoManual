---
symbol: "PPP1CA"
type: "gene"
col: 10266
ensembl_id: "ENSG00000172531"
name: "protein phosphatase 1 catalytic subunit alpha"
location: "11q13.2"
module: 50
arm: "+"
pooled_cpm: 35.28
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# PPP1CA

*protein phosphatase 1 catalytic subunit alpha* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.17× (z +12.8, q 2e-34, up in 41 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.44× (z +5.7, q 2e-06, up in 32 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (SW480 4.04×, A549 6.61×, PANC-1 3.73×, HEC-1-A 4.74×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 6.33×, PANC-1 3.59×, KATO III 3.50×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 4.65×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 2.66×).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.470× (z -4.4, q 0.007, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPAA1]] (+0.69, fdr 7e-06), [[AP2M1]] (+0.62, fdr 1e-05), [[SLC25A39]] (+0.61, fdr 1e-05); moves opposite to [[DNAJC2]] (-0.62, fdr 1e-05), [[TAF1D]] (-0.61, fdr 1e-05), [[LINC01012]] (-0.60, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10266.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (SW480 4.04×, A549 6.61×, PANC-1 3.73×, HEC-1-A 4.74×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 6.33×, PANC-1 3.59×, KATO III 3.50×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 4.65×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 2.66×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.17×** | +12.8 | 2e-34 | 41/42 (SW480, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.76×** | +10.8 | 1e-24 | 37/39 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.11×** | +7.6 | 5e-12 | 35/40 (A-172, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.78×** | +6.4 | 2e-08 | 35/45 (PANC-1, AsPC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.7 | 2e-06 | 32/47 (A549, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.52×** | +4.7 | 3e-04 | 28/48 (KATO III, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.51×** | +4.5 | 5e-04 | 27/48 (SHP-77, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.7 | 0.017 | 24/45 (RKO, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.37×** | +3.5 | 0.033 | 23/48 (SHP-77, A549, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.2 | 0.073 | 1/48 (NCI-H661) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.52× | +3.0 | 0.12 | 22/48 (RKO, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~73% of this change | 1.33× | +3.0 | 0.12 | 21/47 (C-33 A, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10266.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.470×** | -4.4 | 0.007 | 27/48 (NCI-H1792, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.771×** | -4.1 | 0.011 | 25/47 (MIA PaCa-2, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.628×** | -4.0 | 0.011 | 28/48 (SNU-1, LS 180, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.708×** | -3.8 | 0.017 | 27/47 (hTERT-HPNE, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.526×** | -3.7 | 0.022 | 28/47 (A-427, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10266. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 23.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.55× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-427 (line)]] | wt | 60.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.319× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.459× (z -9.8) |
| [[A498 (line)]] | wt | 21.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A549 (line)]] | wt | 28.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.61× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +8.7) | — |
| [[KATO III (line)]] | alt | 57.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 35.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 19.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.33× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[PANC-1 (line)]] | alt | 42.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SNU-423 (line)]] | alt | 26.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HEC-1-A (line)]] | alt | 37.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HT-29 (line)]] | alt | 43.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LoVo (line)]] | wt | 26.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H1792 (line)]] | alt | 55.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.50× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H23 (line)]] | alt | 97.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SHP-77 (line)]] | alt | 37.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW1417 (line)]] | alt | 45.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW480 (line)]] | alt | 44.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[AN3 CA (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10266), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPAA1]] | +0.69 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[AP2M1]] | +0.62 | +0.61 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_PI3K_AKT_MTOR_SIGNALING |
| [[SLC25A39]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[NAGA]] | +0.61 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[LYPLA2]] | +0.59 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[PRKACA]] | +0.59 | +0.50 / +0.44 | both halves | 3e-05 | pathway: DARPP-32 events; STRING 693 |
| [[BSG]] | +0.58 | +0.58 / +0.47 | both halves | 2e-05 | STRING 436 |
| [[CLIC1]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[TUBG1]] | +0.58 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[CORO1B]] | +0.58 | +0.40 / +0.64 | both halves | 4e-05 | ⚠ same locus (14.3 kb, same strand: neighbours can correlate without regulation) |
| [[EIF4EBP2]] | +0.58 | +0.61 / +0.36 | both halves | 9e-05 |  |
| [[VAMP3]] | +0.57 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[RTL8C]] | +0.56 | +0.53 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC2]] | -0.62 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[TAF1D]] | -0.61 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[LINC01012]] | -0.60 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[NSA2]] | -0.58 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[RBM25]] | -0.54 | -0.51 / -0.42 | both halves | 4e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[SRSF11]] ⚠ | -0.53 | -0.48 / -0.48 | both halves | 2e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; ⚠ in the vector space only through flagged drug-doses |
| [[EPB41L4A-AS1]] | -0.52 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[MAP4K5]] | -0.52 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[TPD52L1]] | -0.51 | -0.40 / -0.56 | both halves | 4e-05 |  |
| [[C3orf33]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[RBM27]] | -0.50 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[IWS1]] | -0.50 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[OSBPL1A]] | -0.49 | -0.44 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises PPP1CA's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers PPP1CA's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PLP2]] | C | PLP2 activity raises PPP1CA's level | lines that do not express PLP2 (4) vs lines expressing it (46) | 1.41× lower at baseline in the lines without PLP2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OTULINL, C12orf75; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.491). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.9, -27.8); signed map (-27.4, -40.0). **Vector** length 74.4, 18.9% of its response variance represented; |z| ≥ 3 in 651 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +3.7 | +4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +3.6 | +4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +0.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.8 | +2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +0.3 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +1.4 | +2.9 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.8 | -3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.7 | -4.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.7 | -2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -1.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 catalytic subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:67,398,181-67,421,183 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PP1A, PP-1A, PP1alpha; previously PPP1A |
| Gene groups (HGNC) | Protein phosphatase catalytic subunits |
| Hallmark sets | TGF_BETA_SIGNALING, PI3K_AKT_MTOR_SIGNALING |
| Reactome | 22 pathways, smallest: Triglyceride catabolism; Phosphorylation and nuclear translocation of the CRY:PER:kinase complex; Maturation of hRSV A proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P62136](https://www.uniprot.org/uniprotkb/P62136) (Serine/threonine-protein phosphatase PP1-alpha catalytic subunit):

> Protein phosphatase that associates with over 200 regulatory proteins to form highly specific holoenzymes which dephosphorylate hundreds of biological targets. Protein phosphatase 1 (PP1) is essential for cell division, transcription elongation, and participates in the regulation of glycogen metabolism, muscle contractility and protein synthesis. Involved in regulation of ionic conductances and long-term synaptic plasticity. May play an important role in dephosphorylating substrates such as the …

**Summary**, from NCBI Gene [5499](https://www.ncbi.nlm.nih.gov/gene/5499):

> The protein encoded by this gene is one of the three catalytic subunits of protein phosphatase 1 (PP1). This broadly expressed gene encodes the alpha subunit of the PP1 complex that associates with over 200 regulatory proteins to form holoenzymes which dephosphorylate their biological targets with high specificity. PP1 is a serine/threonine specific protein phosphatase known to be involved in the regulation of a variety of cellular processes, such as cell division, glycogen metabolism, muscle …

**Accessions** — [HGNC:9281](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9281) · Entrez [5499](https://www.ncbi.nlm.nih.gov/gene/5499) · UniProt [P62136](https://www.uniprot.org/uniprotkb/P62136) · Ensembl [ENSG00000172531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172531)

## Data

Gene col 10266: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10266); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10266, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10266]; `tensor/DDL_lfc|DDL_z.npy` [10266]; `embed/gene_vectors.npy` [10266]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10266 or target_col == 10266). Every well: [[PPP1CA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1CA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
