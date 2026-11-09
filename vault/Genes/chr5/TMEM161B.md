---
symbol: "TMEM161B"
type: "gene"
col: 8894
ensembl_id: "ENSG00000164180"
name: "transmembrane protein 161B"
location: "5q14.3"
module: 57
arm: "+"
pooled_cpm: 74.65
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# TMEM161B

*transmembrane protein 161B* — 5q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.15× (z +12.8, q 2e-34, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.507× (z -15.2, q 0e+00, down in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.639× (z -14.2, q 2e-43, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VTA1]] (+0.73, fdr 7e-06), [[ZNF322]] (+0.64, fdr 7e-06), [[SDHB]] (+0.64, fdr 1e-05); moves opposite to [[PLA2G4C]] (-0.53, fdr 4e-05), [[DNMT3A]] (-0.53, fdr 3e-05), [[MICALL2]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8894.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.15×** | +12.8 | 2e-34 | 46/49 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.12×** | +8.3 | 2e-14 | 35/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +6.5 | 2e-08 | 31/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.28×** | +5.5 | 6e-06 | 28/48 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +5.4 | 8e-06 | 27/48 (LoVo, A498, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.0 | 0.005 | 18/37 (NCI-H1573, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | 1.11× | +3.3 | 0.085 | 12/48 (HT-29, SW48, …) | rises with dose | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.085 | 11/48 (LoVo, C32, …) | top dose only | noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | 1.11× | +3.2 | 0.087 | 2/48 (Panc 03.27, SW1417) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.1 | 0.11 | 17/48 (NCI-H2030, LoVo, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.15× | +3.0 | 0.12 | 7/48 (A549, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8894.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.507×** | -15.2 | 0e+00 | 44/49 (NCI-H23, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.503×** | -14.8 | 0e+00 | 39/43 (RPMI-7951, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.639×** | -14.2 | 2e-43 | 38/49 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.644×** | -9.1 | 1e-17 | 29/45 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.714×** | -7.6 | 5e-12 | 34/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.716×** | -7.2 | 6e-11 | 30/48 (PANC-1, A498, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **0.744×** | -6.6 | 3e-09 | 33/48 (NCI-H2347, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.773×** | -5.6 | 2e-06 | 28/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -4.8 | 1e-04 | 25/50 (NCI-H2347, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.803×** | -4.8 | 1e-04 | 24/47 (NCI-H2347, HEC-1-A, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.810×** | -4.7 | 1e-04 | 25/48 (SNU-1, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.873× | -4.3 | 7e-04 | 17/48 (NCI-H1792, LoVo, …) | top dose only | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.820×** | -4.3 | 8e-04 | 23/48 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.852× | -3.3 | 0.036 | 13/48 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.873× | -3.1 | 0.081 | 9/47 (HOP62, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8894. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 107 | 3 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.57× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.344× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 122 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -15.8) |
| [[HOP62 (line)]] | alt | 71.3 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.02× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -11.0) |
| [[A498 (line)]] | wt | 56.7 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -17.6) |
| [[PANC-1 (line)]] | alt | 74.5 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.551× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 70.7 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -14.5) |
| [[HEC-1-A (line)]] | alt | 36.4 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.61× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 71.1 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.92× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 81.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 97.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -19.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 76.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -10.3) |
| [[SW480 (line)]] | alt | 87.6 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.41× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.425× (z -13.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 81.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -24.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 73.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -18.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 64.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -11.5) |
| [[J82 (line)]] | alt | 73.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -10.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 57.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -10.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 67.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.417× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 67.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -21.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 80.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -11.5) |
| [[A-172 (line)]] | wt | 48.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -14.8) |
| [[A549 (line)]] | wt | 65.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -14.5) |
| [[BT-474 (line)]] | alt | 41.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -12.2) |
| [[C-33 A (line)]] | alt | 74.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -9.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 97.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -11.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 115 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.98× (z +8.5) | — |
| [[H4 (line)]] | wt | 75.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -8.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 50.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.280× (z -9.9) ⚠ toxic |
| [[HS-578T (line)]] | alt | 54.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.395× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LOX-IMVI (line)]] | wt | 72.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -16.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 61.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 61.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -13.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 75.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0406× (z -31.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.422× (z -10.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 63.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.140× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SW48 (line)]] | wt | 53.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -9.6) |
| [[AN3 CA (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 86.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 91.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8894), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VTA1]] | +0.73 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[ZNF322]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[SDHB]] | +0.64 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[MED23]] | +0.63 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ATG5]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[TIMM23]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SMIM8]] | +0.60 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[TIMM17A]] | +0.60 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[AQR]] | +0.60 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[ZNF112]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[TAF5L]] | +0.60 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[DDX55]] | +0.60 | +0.52 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLA2G4C]] | -0.53 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[DNMT3A]] | -0.53 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[MICALL2]] | -0.52 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[GYG1]] | -0.52 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[NFKBIB]] | -0.51 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[APLF]] | -0.51 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[HIVEP1]] | -0.50 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[LINC00910]] | -0.49 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[STK11]] | -0.49 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[GCNT4]] | -0.49 | -0.38 / -0.46 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TMEM161B's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers TMEM161B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.543). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.3, -7.3); signed map (-34.5, -24.9). **Vector** length 96.1, 24.0% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.0 | +12.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.9 | +5.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +6.0 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.5 | +8.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.1 | +6.5 |
|  | [[EX229 (drug)]] 5 µM |  | +3.3 | +3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +1.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.2 | -0.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -14.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -6.2 | -7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.5 | -4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 161B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.3 — chr5:88,189,633-88,269,476 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33214 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDZ6](https://www.uniprot.org/uniprotkb/Q8NDZ6) (Transmembrane protein 161B):

> Essential for maintaining normal cardiac rhythm in the developing heart and for neonatal survival (By similarity). Inhibits potassium and calcium currents in the cardiomyocytes, this assists in timely action potential repolarization and thereby maintains normal cardiac rhythm (By similarity).

**Summary**, from NCBI Gene [153396](https://www.ncbi.nlm.nih.gov/gene/153396):

> Predicted to enable nucleic acid binding activity. Predicted to be involved in regulation of cardiac muscle cell action potential and regulation of heart rate. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28483](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28483) · Entrez [153396](https://www.ncbi.nlm.nih.gov/gene/153396) · UniProt [Q8NDZ6](https://www.uniprot.org/uniprotkb/Q8NDZ6) · Ensembl [ENSG00000164180](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164180)

## Data

Gene col 8894: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8894); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8894, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8894]; `tensor/DDL_lfc|DDL_z.npy` [8894]; `embed/gene_vectors.npy` [8894]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8894 or target_col == 8894). Every well: [[TMEM161B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM161B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
