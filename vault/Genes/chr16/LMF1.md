---
symbol: "LMF1"
type: "gene"
col: 2339
ensembl_id: "ENSG00000103227"
name: "lipase maturation factor 1"
location: "16p13.3"
module: 5
arm: "+"
pooled_cpm: 30.03
n_lines_expressing: 48
n_dd_up: 0
n_dd_down: 32
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# LMF1

*lipase maturation factor 1* — 16p13.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.489× (z -13.2, q 6e-37, down in 34 of 45 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.633× (z -8.4, q 5e-15, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHMP6]] (+0.65, fdr 1e-05), [[MRPL45P2]] (+0.61, fdr 9e-06), [[MFSD14CP-1]] (+0.60, fdr 1e-05); moves opposite to [[SGCE]] (-0.59, fdr 1e-05), [[TMEM14A]] (-0.53, fdr 4e-05), [[FAM102B]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PRDM16]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2339.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 0.5 µM |  | 1.32× | +3.7 | 0.14 | 17/46 (LoVo, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.30× | +3.4 | 0.19 | 19/46 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.29× | +3.1 | 0.34 | 14/44 (SW480, C-33 A, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.18× | +3.0 | 0.34 | 7/46 (A549, MIA PaCa-2, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2339.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.489×** | -13.2 | 6e-37 | 34/45 (A549, HEC-1-A, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.443×** | -10.6 | 7e-24 | 39/46 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.460×** | -10.1 | 9e-22 | 35/44 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.454×** | -9.3 | 1e-18 | 36/43 (SNU-423, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -8.4 | 5e-15 | 31/45 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.493×** | -8.3 | 7e-15 | 28/46 (NCI-H1792, A549, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.639×** | -8.2 | 1e-14 | 39/46 (C32, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.546×** | -7.9 | 2e-13 | 34/46 (NCI-H23, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.568×** | -7.4 | 1e-11 | 32/46 (A-172, NCI-H23, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.345×** | -7.3 | 2e-11 | 39/46 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.598×** | -6.7 | 1e-09 | 35/46 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.599×** | -6.7 | 1e-09 | 34/45 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.592×** | -6.3 | 1e-08 | 22/38 (A549, NCI-H23, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.642×** | -5.8 | 3e-07 | 29/46 (A-172, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.651×** | -5.6 | 9e-07 | 25/46 (NCI-H460, AN3 CA, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.658×** | -5.4 | 2e-06 | 28/46 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.499×** | -4.7 | 6e-05 | 25/44 (KATO III, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.729×** | -4.1 | 9e-04 | 24/46 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.737×** | -4.0 | 0.002 | 22/46 (KATO III, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.744×** | -3.8 | 0.002 | 16/45 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Aprepitant (drug)]] 0.05 µM |  | **0.791×** | -3.0 | 0.045 | 15/46 (SW 1271, Panc 03.27, …) | inconsistent across doses |  |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.795×** | -3.0 | 0.053 | 16/46 (LOX-IMVI, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.786×** | -2.8 | 0.081 | 10/46 (SW480, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2339. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 46.8 | 0 | 9 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.376× (z -10.8) |
| [[SW480 (line)]] | alt | 43.7 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -14.5) |
| [[A-172 (line)]] | wt | 65.3 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -14.2) |
| [[LoVo (line)]] | wt | 34.7 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[NCI-H460 (line)]] | wt | 41.1 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[A549 (line)]] | wt | 37.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -17.2) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 25.6 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -8.8) |
| [[KATO III (line)]] | alt | 38.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[SW48 (line)]] | wt | 49.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0879× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 29.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.321× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 32.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -16.9) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 40.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -12.6) |
| [[AN3 CA (line)]] | alt | 41.6 | 0 | 2 (1 ⚠) | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0656× (z -11.2) |
| [[BT-474 (line)]] | alt | 50.7 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -10.7) ⚠ cell-cycle shift, explains ~41% of this change |
| [[CHP-212 (line)]] | wt | 36.1 | 0 | 2 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0700× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Hydroxyurea (drug)]] 0.05 µM 0.0771× (z -9.6) |
| [[H4 (line)]] | wt | 40.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.110× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[HCT15 (line)]] | alt | 52.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[LS 180 (line)]] | wt | 29.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.241× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[NCI-H23 (line)]] | alt | 47.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[SNU-423 (line)]] | alt | 22.0 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0677× (z -13.8) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.221× (z -8.5) |
| [[A-427 (line)]] | wt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -8.7) ⚠ cell-cycle shift, explains ~49% of this change |
| [[C-33 A (line)]] | alt | 42.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -9.0) ⚠ cell-cycle shift, explains ~49% of this change |
| [[Hs 766T (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HT-29 (line)]] | alt | 27.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -11.1) ⚠ cell-cycle shift, explains ~49% of this change |
| [[hTERT-HPNE (line)]] | wt | 9.87 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.5 µM 0.0959× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[NCI-H2030 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.176× (z -9.0) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 35.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -9.7) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SW 900 (line)]] | alt | 26.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -11.1) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SW1417 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -9.3) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A498 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.54 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.57 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2339), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP6]] | +0.65 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[MRPL45P2]] | +0.61 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[MFSD14CP-1]] | +0.60 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[MZF1]] | +0.58 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[GUSBP11]] | +0.57 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[NUTM2B-AS1]] | +0.57 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[METTL2B]] | +0.56 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[C1orf159]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[PIGL]] | +0.56 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[TRAPPC12]] | +0.55 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[TEX22]] | +0.55 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[FBXO10]] | +0.55 | +0.58 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGCE]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[TMEM14A]] | -0.53 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[FAM102B]] | -0.53 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[CAT]] | -0.52 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[MDH1]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[PRCP]] | -0.51 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[APAF1]] | -0.51 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[ADD3]] | -0.50 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[POGLUT2]] | -0.50 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[LINC00888]] | -0.49 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[CYB5A]] | -0.49 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ORC4]] | -0.48 | -0.57 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRDM16]] | B | PRDM16 activity raises LMF1's level | lines that do not express PRDM16 (18) vs lines expressing it (32) | 1.68× lower at baseline in the lines without PRDM16 | 0.040 | ⚠ within organs, on part of the lines; also absent: FBXO2, HAS3, PTPRN2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.451). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (6.6, -11.0); signed map (1.0, -5.2). **Vector** length 63.9, 12.8% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.7 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.1 | -6.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.6 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.5 | -1.4 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | -1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | -0.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.9 | -8.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.8 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -4.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.6 | -0.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | lipase maturation factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:853,634-981,318 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12681, JFP11, FLJ22302, TMEM112A; previously C16orf26, TMEM112 |
| Reactome | 4 pathways, smallest: Assembly of active LPL and LIPC lipase complexes; Plasma lipoprotein remodeling; Plasma lipoprotein assembly, remodeling, and clearance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96S06](https://www.uniprot.org/uniprotkb/Q96S06) (Lipase maturation factor 1):

> Involved in the maturation of specific proteins in the endoplasmic reticulum. Required for maturation and transport of active lipoprotein lipase (LPL) through the secretory pathway. Each LMF1 molecule chaperones 50 or more molecules of LPL.

**Summary**, from NCBI Gene [64788](https://www.ncbi.nlm.nih.gov/gene/64788):

> Involved in triglyceride metabolic process. Predicted to be active in endoplasmic reticulum membrane. Implicated in familial lipase maturation factor 1 deficiency. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14154](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14154) · Entrez [64788](https://www.ncbi.nlm.nih.gov/gene/64788) · UniProt [Q96S06](https://www.uniprot.org/uniprotkb/Q96S06) · Ensembl [ENSG00000103227](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103227)

## Data

Gene col 2339: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2339); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2339, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2339]; `tensor/DDL_lfc|DDL_z.npy` [2339]; `embed/gene_vectors.npy` [2339]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2339 or target_col == 2339). Every well: [[LMF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
