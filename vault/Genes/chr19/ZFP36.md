---
symbol: "ZFP36"
type: "gene"
col: 4857
ensembl_id: "ENSG00000128016"
name: "ZFP36 zinc finger CCCH-type"
location: "19q13.2"
module: 109
arm: "+"
pooled_cpm: 78.5
n_lines_expressing: 47
n_dd_up: 21
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 10
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# ZFP36

*ZFP36 zinc finger CCCH-type* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 11.5× (z +32.7, q 0e+00, up in 44 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.577× (z -5.2, q 1e-04, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JUNB]] (+0.77, fdr 7e-06), [[ZC3H12A]] (+0.70, fdr 7e-06), [[SOCS3]] (+0.69, fdr 7e-06); moves opposite to [[EIF4ENIF1]] (-0.56, fdr 3e-05), [[ASB7]] (-0.52, fdr 3e-05), [[MED4]] (-0.52, fdr 3e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AASS]] → it (grade B ⚠); 10 go from it, the strongest it → cells under [[Ouabain (Octahydrate) (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4857.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **11.5×** | +32.7 | 0e+00 | 44/44 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **12.5×** | +23.0 | 0e+00 | 44/44 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.70×** | +11.9 | 2e-30 | 39/44 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.48×** | +11.8 | 4e-30 | 44/45 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.27×** | +11.2 | 4e-27 | 39/42 (NCI-H460, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.10×** | +10.7 | 8e-25 | 41/43 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.72×** | +9.5 | 2e-19 | 35/45 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.67×** | +9.3 | 1e-18 | 36/44 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +9.0 | 1e-17 | 29/38 (RPMI-7951, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.58×** | +8.3 | 6e-15 | 32/38 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.34×** | +8.0 | 5e-14 | 37/45 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.16×** | +7.3 | 1e-11 | 35/44 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +4.6 | 2e-04 | 30/45 (MIA PaCa-2, LS 180, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.63×** | +4.6 | 2e-04 | 30/45 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +4.4 | 4e-04 | 26/44 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +4.2 | 9e-04 | 24/45 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.23×** | +4.0 | 0.002 | 24/46 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.003 | 26/45 (SW480, HEC-1-A, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.013 | 26/46 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pemigatinib (drug)]] 0.05 µM |  | **1.40×** | +2.9 | 0.097 | 18/45 (AsPC-1, SW 900, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4857.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.577×** | -5.2 | 1e-04 | 31/45 (HT-29, hTERT-HPNE, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.423×** | -4.3 | 0.006 | 30/42 (SW48, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.672×** | -3.8 | 0.024 | 27/44 (C32, HT-29, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.666×** | -3.7 | 0.024 | 25/43 (NCI-H23, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.655×** | -3.7 | 0.024 | 25/47 (SW48, C32, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.763×** | -3.6 | 0.026 | 23/45 (SW48, CFPAC-1, …) | top dose only | low cells (technical?) |
| [[NG25 (drug)]] 0.5 µM |  | **0.618×** | -3.3 | 0.090 | 21/45 (A-427, NCI-H460, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.707× | -3.1 | 0.13 | 20/45 (SW48, SW480, …) | inconsistent across doses | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 0.798× | -3.0 | 0.13 | 20/45 (C32, HT-29, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.718× | -3.0 | 0.13 | 22/47 (HT-29, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.792× | -3.0 | 0.13 | 13/45 (SHP-77, C32, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4857. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 53.5 | 17 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.5× (z +25.2) | — |
| [[PANC-1 (line)]] | alt | 509 | 12 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 32.3× (z +35.4) | — |
| [[NCI-H1573 (line)]] | alt | 50.5 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +24.1) | — |
| [[SW 900 (line)]] | alt | 57.6 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +22.4) | — |
| [[AsPC-1 (line)]] | alt | 79.6 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +28.4) | — |
| [[SW480 (line)]] | alt | 25.5 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +16.8) | — |
| [[HEC-1-A (line)]] | alt | 40.1 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 30.0× (z +31.0) | — |
| [[HS-578T (line)]] | alt | 45.3 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +18.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 41.5 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +25.8) | — |
| [[SW48 (line)]] | wt | 106 | 6 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 12.8× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 85.1 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 26.0× (z +23.6) | — |
| [[hTERT-HPNE (line)]] | wt | 55.4 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 25.1× (z +25.1) | — |
| [[NCI-H1792 (line)]] | alt | 26.7 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +16.9) | — |
| [[NCI-H2347 (line)]] | alt | 32.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +23.1) | — |
| [[A498 (line)]] | wt | 70.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +26.9) | — |
| [[RPMI-7951 (line)]] | alt | 42.7 | 5 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 26.1× (z +15.7) | — |
| [[A-172 (line)]] | wt | 50.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +18.5) | — |
| [[HOP62 (line)]] | alt | 53.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +23.3) | — |
| [[LOX-IMVI (line)]] | wt | 31.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +14.7) | — |
| [[A-427 (line)]] | wt | 26.5 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 7.98× (z +11.8) | — |
| [[A549 (line)]] | wt | 139 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +22.5) | — |
| [[H4 (line)]] | wt | 36.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +14.7) | — |
| [[HepG2_C3A (line)]] | wt | 69.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +18.3) | — |
| [[Hs 766T (line)]] | wt | 53.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +19.9) | — |
| [[HT-29 (line)]] | alt | 179 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -9.5) |
| [[J82 (line)]] | alt | 32.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.2× (z +20.3) | — |
| [[KATO III (line)]] | alt | 59.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +16.5) | — |
| [[LoVo (line)]] | wt | 42.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +16.0) | — |
| [[NCI-H2030 (line)]] | alt | 41.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +22.8) | — |
| [[NCI-H23 (line)]] | alt | 22.1 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 5.57× (z +8.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 50.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +24.1) | — |
| [[SNU-423 (line)]] | alt | 43.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +19.7) | — |
| [[BT-474 (line)]] | alt | 64.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.30× (z +16.8) | — |
| [[CFPAC-1 (line)]] | alt | 81.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +23.1) | — |
| [[COLO 205 (line)]] | alt | 74.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 69.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +15.4) | — |
| [[NCI-H661 (line)]] | alt | 68.9 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0562× (z -8.5) |
| [[SW 1088 (line)]] | alt | 26.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.1× (z +9.2) | — |
| [[SW 1271 (line)]] | alt | 21.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 83.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +15.8) | — |
| [[AN3 CA (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.60 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4857), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUNB]] | +0.77 | +0.71 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 847 |
| [[ZC3H12A]] | +0.70 | +0.72 / +0.71 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 644 |
| [[SOCS3]] | +0.69 | +0.58 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 565 |
| [[DUSP1]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 934 |
| [[TIPARP]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 | same gene group; pathway: HALLMARK_HYPOXIA; STRING 493 |
| [[FOS]] | +0.60 | +0.49 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE; STRING 878 |
| [[IER2]] | +0.58 | +0.51 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 736 |
| [[PTPRN2]] | +0.58 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[EGR1]] | +0.57 | +0.47 / +0.61 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 798 |
| [[TRIB1]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 412 |
| [[TNKS1BP1]] | +0.56 | +0.56 / +0.49 | both halves | 1e-05 | STRING 505 |
| [[CSRNP1]] | +0.55 | +0.51 / +0.57 | both halves | 1e-05 | STRING 659 |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4ENIF1]] | -0.56 | -0.43 / -0.61 | both halves | 3e-05 | STRING 507 |
| [[ASB7]] | -0.52 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[MED4]] | -0.52 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[FBXW11]] | -0.52 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[KLHDC10]] | -0.52 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[PDSS2]] | -0.51 | -0.37 / -0.53 | both halves | 7e-05 |  |
| [[EYA3]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[MFSD8]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[TRAPPC13]] | -0.50 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[MCM9]] | -0.50 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[NUP54]] | -0.49 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[CNPY2]] | -0.49 | -0.25 / -0.53 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AASS]] | B | AASS activity lowers ZFP36's level | lines that do not express AASS (7) vs lines expressing it (43) | 2.08× higher at baseline in the lines without AASS | 0.029 | ⚠ within organs, on part of the lines; also absent: LINC00159, ZNF391, DISC1 |
| [[PDLIM3]] | B | PDLIM3 activity lowers ZFP36's level | lines that do not express PDLIM3 (18) vs lines expressing it (32) | 1.37× higher at baseline in the lines without PDLIM3 | 0.078 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, SOX5, PTX3 |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Ouabain (Octahydrate) (drug)]] 0.05 µM | C | ZFP36 activity raises the cells' numbers under Ouabain (Octahydrate) 0.05 µM (protects the cells) | lines that do not express ZFP36 (3) vs lines expressing it (45) | the lines without ZFP36: 0.69× the cells of the other lines | 0.026 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: FTH1, CDC42EP1, ENSG00000284716 |
| cells under [[Epirubicin (hydrochloride) (drug)]] 5 µM | C | ZFP36 activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express ZFP36 (3) vs lines expressing it (45) | the lines without ZFP36: 0.28× the cells of the other lines | 0.028 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: FTH1, CDC42EP1, ENSG00000284716 |
| cells under [[Niclosamide (olamine) (drug)]] 5 µM | C | ZFP36 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express ZFP36 (3) vs lines expressing it (45) | the lines without ZFP36: 0.36× the cells of the other lines | 0.037 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: FTH1, CDC42EP1, ENSG00000284716 |
| cells under [[Hydroxyfasudil (drug)]] 5 µM | C | ZFP36 activity lowers the cells' numbers under Hydroxyfasudil 5 µM (makes them more sensitive) | lines that do not express ZFP36 (3) vs lines expressing it (45) | the lines without ZFP36: 1.35× the cells of the other lines | 0.039 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: FTH1, CDC42EP1, ENSG00000284716 |
| cells under [[Pentoxifylline (drug)]] 0.5 µM | C | ZFP36 activity raises the cells' numbers under Pentoxifylline 0.5 µM (protects the cells) | lines that do not express ZFP36 (3) vs lines expressing it (45) | the lines without ZFP36: 0.75× the cells of the other lines | 0.053 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: FTH1, CDC42EP1, ENSG00000284716 |
| cells under [[Infigratinib (drug)]] 5 µM | C | ZFP36 activity raises the cells' numbers under Infigratinib 5 µM (protects the cells) | lines that do not express ZFP36 (3) vs lines expressing it (45) | the lines without ZFP36: 0.58× the cells of the other lines | 0.068 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: FTH1, CDC42EP1, ENSG00000284716 |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | C | ZFP36 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express ZFP36 (3) vs lines expressing it (45) | the lines without ZFP36: 0.75× the cells of the other lines | 0.070 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: FTH1, CDC42EP1, ENSG00000284716 |
| cells under [[Radotinib (drug)]] 5 µM | C | ZFP36 activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express ZFP36 (3) vs lines expressing it (45) | the lines without ZFP36: 0.82× the cells of the other lines | 0.084 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: FTH1, CDC42EP1, ENSG00000284716 |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | C | ZFP36 activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express ZFP36 (3) vs lines expressing it (45) | the lines without ZFP36: 0.79× the cells of the other lines | 0.090 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: FTH1, CDC42EP1, ENSG00000284716 |
| cells under [[Vortioxetine (drug)]] 0.5 µM | C | ZFP36 activity lowers the cells' numbers under Vortioxetine 0.5 µM (makes them more sensitive) | lines that do not express ZFP36 (3) vs lines expressing it (45) | the lines without ZFP36: 1.33× the cells of the other lines | 0.092 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: FTH1, CDC42EP1, ENSG00000284716 |

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.5, 8.3); signed map (11.2, 28.7). **Vector** length 120, 40.3% of its response variance represented; |z| ≥ 3 in 1,225 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NGF-stimulated transcription* (reactome, mean cos +0.53 to 9); *Nuclear Events (kinase and transcription factor activation)* (reactome, mean cos +0.53 to 9); *Signaling by NTRK1 (TRKA)* (reactome, mean cos +0.53 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +4.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.4 | +23.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +32.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +11.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.4 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.3 | +1.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.1 | +1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +2.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -3.7 |
|  | [[NG25 (drug)]] 5 µM |  | -5.1 | -4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.6 | -2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.8 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -1.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ZFP36 zinc finger CCCH-type |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:39,406,847-39,409,407 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIS11, G0S24, TTP, NUP475 |
| Gene groups (HGNC) | Zinc fingers CCCH-type |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, HYPOXIA, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 3 pathways, smallest: Tristetraprolin (TTP, ZFP36) binds and destabilizes mRNA; Regulation of mRNA stability by proteins that bind AU-rich elements; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P26651](https://www.uniprot.org/uniprotkb/P26651) (mRNA decay activator protein ZFP36):

> Zinc-finger RNA-binding protein that destabilizes several cytoplasmic AU-rich element (ARE)-containing mRNA transcripts by promoting their poly(A) tail removal or deadenylation, and hence provide a mechanism for attenuating protein synthesis. Acts as an 3'-untranslated region (UTR) ARE mRNA-binding adapter protein to communicate signaling events to the mRNA decay machinery. Recruits deadenylase CNOT7 (and probably the CCR4-NOT complex) via association with CNOT1, and hence promotes ARE-mediated …

**Summary**, from NCBI Gene [7538](https://www.ncbi.nlm.nih.gov/gene/7538):

> Enables several functions, including 14-3-3 protein binding activity; mRNA 3'-UTR AU-rich region binding activity; and protein-RNA sequence-specific adaptor activity. Involved in several processes, including cellular response to cytokine stimulus; cellular response to epidermal growth factor stimulus; and regulation of gene expression. Acts upstream of or within mRNA catabolic process. Located in cytoplasmic ribonucleoprotein granule; cytosol; and nucleus. Part of ribonucleoprotein complex. …

**Accessions** — [HGNC:12862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12862) · Entrez [7538](https://www.ncbi.nlm.nih.gov/gene/7538) · UniProt [P26651](https://www.uniprot.org/uniprotkb/P26651) · Ensembl [ENSG00000128016](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128016)

## Data

Gene col 4857: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4857); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4857, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4857]; `tensor/DDL_lfc|DDL_z.npy` [4857]; `embed/gene_vectors.npy` [4857]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4857 or target_col == 4857). Every well: [[ZFP36 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFP36.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
