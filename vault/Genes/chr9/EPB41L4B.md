---
symbol: "EPB41L4B"
type: "gene"
col: 1737
ensembl_id: "ENSG00000095203"
name: "erythrocyte membrane protein band 4.1 like 4B"
location: "9q31.3"
module: 204
arm: "+"
pooled_cpm: 35.96
n_lines_expressing: 41
n_dd_up: 15
n_dd_down: 16
n_dd_up_clean: 14
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/204"]
generated_by: "tahoemap"
---

# EPB41L4B

*erythrocyte membrane protein band 4.1 like 4B* — 9q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.75× (z +11.4, q 2e-27, up in 24 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.454× (z -15.6, q 0e+00, down in 30 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D2B]] (+0.66, fdr 7e-06), [[LRP5L]] (+0.64, fdr 9e-06), [[VGLL4]] (+0.63, fdr 1e-05); moves opposite to [[SLC36A4]] (-0.57, fdr 2e-05), [[BACH1]] (-0.55, fdr 2e-05), [[TAF2]] (-0.55, fdr 2e-05).
> It is in [[Module 204]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PLEKHA7]] → it (grade B ⚠); 2 go from it, the strongest it → [[UBTD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1737.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +11.4 | 2e-27 | 24/38 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +8.9 | 2e-16 | 27/39 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +7.0 | 7e-10 | 20/38 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.83×** | +5.0 | 9e-05 | 18/39 (RKO, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +4.5 | 1e-03 | 18/39 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.2 | 0.003 | 18/39 (NCI-H2347, A498, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.003 | 16/39 (AsPC-1, NCI-H1792, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.29×** | +4.0 | 0.004 | 13/39 (NCI-H460, NCI-H2030, …) | all doses, flat |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.55×** | +3.6 | 0.021 | 11/38 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.040 | 11/39 (A549, NCI-H1573, …) | rises with dose |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.040 | 9/38 (NCI-H23, SNU-1, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.040 | 12/38 (A549, NCI-H1573, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.047 | 6/38 (PANC-1, LS 180, …) | top dose only | plate-row cell shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.23×** | +3.1 | 0.079 | 14/37 (NCI-H460, A498, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.079 | 11/38 (NCI-H1573, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1737.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.454×** | -15.6 | 0e+00 | 30/38 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.455×** | -12.3 | 1e-32 | 30/38 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.719×** | -5.2 | 4e-05 | 23/39 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.744×** | -4.6 | 5e-04 | 20/35 (C-33 A, SW48, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.762×** | -4.3 | 0.002 | 17/38 (SNU-1, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.765×** | -4.2 | 0.003 | 16/39 (SW 1088, AsPC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.775×** | -4.0 | 0.005 | 17/38 (A498, NCI-H2347, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.774×** | -3.9 | 0.008 | 18/37 (SHP-77, SW480, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.634×** | -3.7 | 0.011 | 17/35 (PANC-1, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.773×** | -3.7 | 0.011 | 16/29 (HEC-1-A, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.780×** | -3.7 | 0.012 | 16/37 (NCI-H2347, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.788×** | -3.6 | 0.014 | 16/27 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.788×** | -3.6 | 0.014 | 18/39 (COLO 205, SNU-1, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.813×** | -3.2 | 0.048 | 11/38 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.858× | -3.1 | 0.067 | 14/39 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.822×** | -3.1 | 0.076 | 9/39 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.866× | -3.0 | 0.096 | 9/39 (BT-474, Panc 03.27, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.697×** | -3.0 | 0.096 | 11/36 (PANC-1, SW 900, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1737. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 31.8 | 10 | 3 (2 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 3.52× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -13.7) |
| [[NCI-H1573 (line)]] | alt | 21.0 | 7 | 2 | [[Dexamethasone (drug)]] 0.5 µM 5.01× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.0876× (z -19.5) |
| [[PANC-1 (line)]] | alt | 69.2 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -28.6) |
| [[SNU-1 (line)]] | wt | 35.7 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0961× (z -12.9) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.256× (z -10.5) |
| [[A498 (line)]] | wt | 28.4 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +9.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -11.7) |
| [[LoVo (line)]] | wt | 56.7 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -14.5) |
| [[SW480 (line)]] | alt | 57.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.478× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 19.5 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.75× (z +16.2) | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -11.4) |
| [[SW48 (line)]] | wt | 61.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -11.6) |
| [[A-427 (line)]] | wt | 23.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -10.4) |
| [[C-33 A (line)]] | alt | 45.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -11.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 131 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -17.3) |
| [[HEC-1-A (line)]] | alt | 31.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -14.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 119 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 31.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -16.5) |
| [[SHP-77 (line)]] | alt | 62.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 23.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 29.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 69.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -10.6) |
| [[HT-29 (line)]] | alt | 32.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 22.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -14.6) |
| [[Panc 03.27 (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -12.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 31.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +12.6) | — |
| [[A-172 (line)]] | wt | 6.87 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.12 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.44 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.75 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.02 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.96 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.13 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 119 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1737), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D2B]] | +0.66 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[LRP5L]] | +0.64 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[VGLL4]] | +0.63 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[RREB1]] | +0.61 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[LRRC1]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[NRG2]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[HERC3]] | +0.59 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[CHPT1]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[CASZ1]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[PTPRJ]] | +0.57 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[USP3]] | +0.57 | +0.66 / +0.40 | both halves | 5e-05 |  |
| [[NFIA]] | +0.57 | +0.60 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC36A4]] | -0.57 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[BACH1]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[TAF2]] | -0.55 | -0.60 / -0.46 | both halves | 2e-05 |  |
| [[ZNF140]] | -0.54 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.52 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.52 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[NEK1]] | -0.52 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[SETX]] | -0.51 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[LYRM2]] | -0.51 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[ZSCAN5A]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ANKLE2]] | -0.50 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[HDX]] | -0.50 | -0.54 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHA7]] | B | PLEKHA7 activity raises EPB41L4B's level | lines that do not express PLEKHA7 (8) vs lines expressing it (42) | 2.53× lower at baseline in the lines without PLEKHA7 | 0.023 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CASZ1]] | B | CASZ1 activity raises EPB41L4B's level | lines that do not express CASZ1 (10) vs lines expressing it (40) | 2.89× lower at baseline in the lines without CASZ1 | 0.054 | ⚠ within organs, on part of the lines; also absent: SBK1, CPLX1, LLGL2; maybe low, not absent |
| [[LGR4]] | B | LGR4 activity raises EPB41L4B's level | lines that do not express LGR4 (7) vs lines expressing it (43) | 2.70× lower at baseline in the lines without LGR4 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBTD1]] | B | EPB41L4B activity lowers UBTD1's level | lines that do not express EPB41L4B (9) vs lines expressing it (41) | 1.41× higher at baseline in the lines without EPB41L4B | 0.060 | ⚠ within organs, on part of the lines; also absent: MYRF, GRTP1, MARVELD2; maybe low, not absent; its own permutation p |
| [[GLUD1]] | B | EPB41L4B activity lowers GLUD1's level | lines that do not express EPB41L4B (9) vs lines expressing it (41) | 1.07× higher at baseline in the lines without EPB41L4B | 0.089 | ⚠ within organs, on part of the lines; also absent: MYRF, GRTP1, MARVELD2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 204]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.679). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.54; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.5, -5.6); signed map (-21.1, 18.1). **Vector** length 111, 28.8% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +11.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +7.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.0 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +4.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.4 | +2.0 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +3.1 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -15.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.2 | -12.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -3.1 | -3.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.0 | -4.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -5.2 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Thymol (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | erythrocyte membrane protein band 4.1 like 4B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.3 — chr9:109,171,974-109,321,059 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EHM2, LULU2 |
| Gene groups (HGNC) | FERM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H329](https://www.uniprot.org/uniprotkb/Q9H329) (Band 4.1-like protein 4B):

> Up-regulates the activity of the Rho guanine nucleotide exchange factor ARHGEF18 (By similarity). Involved in the regulation of the circumferential actomyosin belt in epithelial cells. Promotes cellular adhesion, migration and motility in vitro and may play a role in wound healing. May have a role in mediating cytoskeletal changes associated with steroid-induced cell differentiation.

**Summary**, from NCBI Gene [54566](https://www.ncbi.nlm.nih.gov/gene/54566):

> Predicted to be a structural constituent of cytoskeleton. Involved in several processes, including positive regulation of cell adhesion; positive regulation of keratinocyte migration; and wound healing. Acts upstream of or within actomyosin structure organization. Located in apical part of cell and cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19818](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19818) · Entrez [54566](https://www.ncbi.nlm.nih.gov/gene/54566) · UniProt [Q9H329](https://www.uniprot.org/uniprotkb/Q9H329) · Ensembl [ENSG00000095203](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095203)

## Data

Gene col 1737: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1737); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1737, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1737]; `tensor/DDL_lfc|DDL_z.npy` [1737]; `embed/gene_vectors.npy` [1737]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1737 or target_col == 1737). Every well: [[EPB41L4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPB41L4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
