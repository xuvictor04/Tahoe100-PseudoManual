---
symbol: "SLC2A3"
type: "gene"
col: 680
ensembl_id: "ENSG00000059804"
name: "solute carrier family 2 member 3"
location: "12p13.31"
module: 134
arm: "+"
pooled_cpm: 271.99
n_lines_expressing: 35
n_dd_up: 9
n_dd_down: 45
n_dd_up_clean: 8
n_dd_down_clean: 37
in_vector_space: true
direction_upstream: 3
direction_downstream: 12
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# SLC2A3

*solute carrier family 2 member 3* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.67× (z +8.1, q 3e-13, up in 29 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 45 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.288× (z -19.6, q 0e+00, down in 30 of 33 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM117B]] (+0.71, fdr 1e-05), [[ANKRD37]] (+0.70, fdr 9e-06), [[KIAA1958]] (+0.70, fdr 7e-06); moves opposite to [[ANKRD18B]] (-0.63, fdr 1e-04), [[FAIM]] (-0.61, fdr 8e-05), [[PBLD]] (-0.60, fdr 3e-04).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 12 go from it, the strongest it → [[PFKFB4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 680.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +8.1 | 3e-13 | 29/33 (NCI-H2347, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +7.1 | 4e-10 | 30/34 (NCI-H2347, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.13×** | +6.7 | 5e-09 | 29/34 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.84×** | +6.1 | 2e-07 | 22/33 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **2.17×** | +4.5 | 6e-04 | 28/33 (CHP-212, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.008 | 24/34 (SW 900, A549, …) | top dose only | plate-row cell shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.24×** | +3.4 | 0.050 | 21/33 (J82, SK-MEL-2, …) | top dose only |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.067 | 21/33 (SW 900, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.082 | 17/33 (Hs 766T, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 45 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 680.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.288×** | -19.6 | 0e+00 | 30/33 (HCT15, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.366×** | -15.8 | 0e+00 | 33/34 (SW1417, HCT15, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.321×** | -12.7 | 2e-34 | 31/33 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.371×** | -10.6 | 4e-24 | 32/33 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.378×** | -10.4 | 2e-23 | 30/30 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.435×** | -9.3 | 2e-18 | 31/34 (NCI-H2347, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.429×** | -9.1 | 1e-17 | 30/32 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.564×** | -9.0 | 1e-17 | 30/33 (SW1417, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.459×** | -8.3 | 5e-15 | 30/33 (HepG2/C3A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.483×** | -7.8 | 4e-13 | 31/35 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.528×** | -7.1 | 6e-11 | 32/33 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.545×** | -6.7 | 7e-10 | 29/33 (HCT15, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.689×** | -5.8 | 2e-07 | 30/33 (A549, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.569×** | -5.8 | 3e-07 | 25/31 (NCI-H2347, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.616×** | -5.4 | 3e-06 | 25/33 (A-172, LOX-IMVI, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.635×** | -5.1 | 2e-05 | 27/33 (NCI-H1792, J82, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.730×** | -4.9 | 3e-05 | 25/34 (C32, J82, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.709×** | -4.6 | 1e-04 | 26/33 (C32, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.655×** | -4.5 | 2e-04 | 26/33 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 680. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 294 | 2 | 13 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.48× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.0952× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.246× (z -20.7) |
| [[NCI-H460 (line)]] | wt | 506 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -28.9) |
| [[HepG2_C3A (line)]] | wt | 397 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0311× (z -33.7) |
| [[NCI-H23 (line)]] | alt | 697 | 1 | 10 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 12.3× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -22.7) |
| [[SW480 (line)]] | alt | 1,101 | 2 | 9 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.3× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -21.7) |
| [[HCT15 (line)]] | alt | 685 | 1 | 9 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.47× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.0468× (z -37.0) |
| [[SK-MEL-2 (line)]] | alt | 186 | 5 (2 ⚠) | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.15× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 3.79× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.0568× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -10.6) |
| [[SW1417 (line)]] | alt | 352 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -24.8) |
| [[C32 (line)]] | wt | 400 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -14.8) |
| [[A549 (line)]] | wt | 146 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -22.1) |
| [[CHP-212 (line)]] | wt | 245 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0576× (z -24.5) |
| [[Hs 766T (line)]] | wt | 152 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -20.7) |
| [[J82 (line)]] | alt | 284 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -22.2) |
| [[MIA PaCa-2 (line)]] | alt | 132 | 1 | 5 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.08× (z +10.5) | [[Adagrasib (drug)]] 0.05 µM 0.570× (z -12.9) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.0) |
| [[RKO (line)]] | wt | 92.4 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -19.3) |
| [[A-172 (line)]] | wt | 164 | 3 (1 ⚠) | 2 | [[Tucidinostat (drug)]] 5 µM 2.69× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -9.4) |
| [[A-427 (line)]] | wt | 1,198 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 12.2× (z +16.7) | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -10.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 357 | 1 | 4 | [[Tucidinostat (drug)]] 5 µM 2.13× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -17.2) |
| [[CFPAC-1 (line)]] | alt | 74.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -13.4) |
| [[HOP62 (line)]] | alt | 497 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 500 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -12.1) |
| [[SNU-423 (line)]] | alt | 195 | 2 (1 ⚠) | 3 | [[Panobinostat (drug)]] 5 µM 3.49× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.40× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -13.8) |
| [[SW 900 (line)]] | alt | 307 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -12.6) |
| [[hTERT-HPNE (line)]] | wt | 449 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 101 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -15.5) |
| [[NCI-H2030 (line)]] | alt | 446 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -20.6) |
| [[A498 (line)]] | wt | 100 | 2 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.97× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.61× (z +8.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -9.0) |
| [[AN3 CA (line)]] | alt | 230 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -10.5) |
| [[H4 (line)]] | wt | 313 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.52× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H661 (line)]] | alt | 385 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 199 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -10.4) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 441 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 31.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 18.6 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 23.7 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 21.4 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 52.3 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 28.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 19.5 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 20.8 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 19.3 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 31.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 363 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.8 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 21.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 23.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 317 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 680), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM117B]] | +0.71 | +0.75 / +0.57 | both halves | 1e-05 |  |
| [[ANKRD37]] | +0.70 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[KIAA1958]] | +0.70 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[RALGAPA2]] | +0.69 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[ZFYVE28]] | +0.67 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.66 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[NDRG1]] | +0.66 | +0.69 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[HK1]] | +0.66 | +0.65 / +0.44 | both halves | 3e-05 | pathway: HALLMARK_HYPOXIA; STRING 737 |
| [[HILPDA]] | +0.66 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[CARHSP1]] | +0.65 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[RERE]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[SH3GL3]] | +0.64 | +0.62 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD18B]] | -0.63 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[FAIM]] | -0.61 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[PBLD]] | -0.60 | -0.59 / -0.28 | both halves | 3e-04 |  |
| [[DLG5]] | -0.60 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[AP5M1]] | -0.60 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[EFCAB2]] | -0.60 | -0.54 / -0.26 | both halves | 4e-04 |  |
| [[NNT]] | -0.59 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[SLC25A21]] | -0.58 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[GTF3C6]] | -0.58 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[BRPF3]] | -0.58 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[PRDM11]] | -0.57 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[ARFGAP2]] | -0.56 | -0.47 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SLC2A3's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.3% of all compounds | 0.010 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[SGSM1]] | B | SGSM1 activity lowers SLC2A3's level | lines that do not express SGSM1 (6) vs lines expressing it (44) | 2.69× higher at baseline in the lines without SGSM1 | 0.063 | ⚠ within organs, on part of the lines; also absent: DANT2, KCNIP3, PIK3C2B; maybe low, not absent |
| [[PYGO1]] | B | PYGO1 activity raises SLC2A3's level | lines that do not express PYGO1 (16) vs lines expressing it (34) | 3.42× lower at baseline in the lines without PYGO1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A; also absent: MIR130AHG, RBMS3, TCF7L1 |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PFKFB4]] | B | SLC2A3 activity raises PFKFB4's level | lines that do not express SLC2A3 (15) vs lines expressing it (35) | 1.98× lower at baseline in the lines without SLC2A3 | 0.015 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| [[SLC27A1]] | B | SLC2A3 activity raises SLC27A1's level | lines that do not express SLC2A3 (15) vs lines expressing it (35) | 1.45× lower at baseline in the lines without SLC2A3 | 0.019 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| [[VKORC1]] | B | SLC2A3 activity raises VKORC1's level | lines that do not express SLC2A3 (15) vs lines expressing it (35) | 1.94× lower at baseline in the lines without SLC2A3 | 0.021 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| [[CEP170]] | B | SLC2A3 activity raises CEP170's level | lines that do not express SLC2A3 (15) vs lines expressing it (35) | 2.13× lower at baseline in the lines without SLC2A3 | 0.021 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| [[CCDC47]] | B | SLC2A3 activity raises CCDC47's level | lines that do not express SLC2A3 (15) vs lines expressing it (35) | 1.30× lower at baseline in the lines without SLC2A3 | 0.034 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| [[WDR54]] | B | SLC2A3 activity raises WDR54's level | lines that do not express SLC2A3 (15) vs lines expressing it (35) | 1.97× lower at baseline in the lines without SLC2A3 | 0.043 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| [[PYGO1]] | B | SLC2A3 activity raises PYGO1's level | lines that do not express SLC2A3 (15) vs lines expressing it (35) | 3.23× lower at baseline in the lines without SLC2A3 | 0.061 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| [[ATRN]] | B | SLC2A3 activity raises ATRN's level | lines that do not express SLC2A3 (15) vs lines expressing it (35) | 1.70× lower at baseline in the lines without SLC2A3 | 0.062 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| [[TNFRSF10D]] | B | SLC2A3 activity lowers TNFRSF10D's level | lines that do not express SLC2A3 (15) vs lines expressing it (35) | 1.02× higher at baseline in the lines without SLC2A3 | 0.071 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| cells under [[Procainamide (hydrochloride) (drug)]] 0.5 µM | B | SLC2A3 activity lowers the cells' numbers under Procainamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express SLC2A3 (15) vs lines expressing it (33) | the lines without SLC2A3: 1.19× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| cells under [[Mifepristone (drug)]] 0.5 µM | B | SLC2A3 activity raises the cells' numbers under Mifepristone 0.5 µM (protects the cells) | lines that do not express SLC2A3 (15) vs lines expressing it (33) | the lines without SLC2A3: 0.85× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| [[EFCAB2]] | B | SLC2A3 activity raises EFCAB2's level | lines that do not express SLC2A3 (15) vs lines expressing it (35) | 1.46× lower at baseline in the lines without SLC2A3 | 0.099 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.769). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.9, -12.6); signed map (-35.4, 27.7). **Vector** length 136, 43.8% of its response variance represented; |z| ≥ 3 in 1,341 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.8 | +1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.7 | +1.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +8.6 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +8.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +7.2 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | -0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.6 | +2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +4.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.9 | +0.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.2 | -8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.5 | -19.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -12.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | -10.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.0 | -9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.7 | -6.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.4 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.9 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 2 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:7,919,230-8,019,007 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GLUT3 |
| Gene groups (HGNC) | Solute carrier family 2 |
| Hallmark sets | IL2_STAT5_SIGNALING, HYPOXIA, TNFA_SIGNALING_VIA_NFKB, MTORC1_SIGNALING |
| Reactome | 10 pathways, smallest: Vitamin C (ascorbate) metabolism; Cellular hexose transport; MECP2 regulates neuronal receptors and channels |
| Matched by | ensembl_id |

**Function**, from UniProt [P11169](https://www.uniprot.org/uniprotkb/P11169) (Solute carrier family 2, facilitated glucose transporter member 3):

> Facilitative glucose transporter. Can also mediate the uptake of various other monosaccharides across the cell membrane. Mediates the uptake of glucose, 2-deoxyglucose, galactose, mannose, xylose and fucose, and probably also dehydroascorbate. Does not mediate fructose transport. Required for mesendoderm differentiation (By similarity).

**Summary**, from NCBI Gene [6515](https://www.ncbi.nlm.nih.gov/gene/6515):

> Enables D-glucose binding activity; dehydroascorbic acid transmembrane transporter activity; and hexose transmembrane transporter activity. Involved in D-glucose import across plasma membrane; galactose transmembrane transport; and transport across blood-brain barrier. Located in plasma membrane. Biomarker of Alzheimer's disease; acanthosis nigricans; diabetes mellitus; and type 2 diabetes mellitus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11007](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11007) · Entrez [6515](https://www.ncbi.nlm.nih.gov/gene/6515) · UniProt [P11169](https://www.uniprot.org/uniprotkb/P11169) · Ensembl [ENSG00000059804](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000059804)

## Data

Gene col 680: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 680); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 680, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 680]; `tensor/DDL_lfc|DDL_z.npy` [680]; `embed/gene_vectors.npy` [680]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 680 or target_col == 680). Every well: [[SLC2A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC2A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
