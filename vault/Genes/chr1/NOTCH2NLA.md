---
symbol: "NOTCH2NLA"
type: "gene"
col: 15438
ensembl_id: "ENSG00000264343"
name: "notch 2 N-terminal like A"
location: "1q21.1"
module: 226
arm: "+"
pooled_cpm: 12.75
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/226"]
generated_by: "tahoemap"
---

# NOTCH2NLA

*notch 2 N-terminal like A* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.32× (z +23.0, q 0e+00, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.447× (z -10.9, q 5e-25, down in 21 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.742× (z -4.0, q 0.007, down in 14 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBPF14]] (+0.83, fdr 7e-06), [[NBPF10]] (+0.74, fdr 7e-06, ⚠ same locus), [[NOTCH2NLB]] (+0.72, fdr 7e-06), [[NBPF26]] (+0.71, fdr 7e-06); moves opposite to [[TRRAP]] (-0.55, fdr 1e-05), [[ADPGK]] (-0.55, fdr 1e-05), [[VTI1A]] (-0.54, fdr 1e-05).
> It is in [[Module 226]], a single-armed module (NOTCH2 Activation and Transmission of Signal to the Nucleus).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SPOCD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15438.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.32×** | +23.0 | 0e+00 | 42/44 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.45×** | +11.7 | 4e-29 | 38/44 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.71×** | +9.3 | 3e-18 | 36/44 (NCI-H2347, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +7.2 | 8e-11 | 28/46 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +6.4 | 2e-08 | 20/40 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +5.4 | 6e-06 | 21/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +4.6 | 3e-04 | 13/45 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +4.6 | 3e-04 | 18/42 (HEC-1-A, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.005 | 17/42 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.9 | 0.006 | 16/41 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.013 | 8/42 (A-172, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.6 | 0.013 | 14/38 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.060 | 10/44 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | 1.25× | +3.0 | 0.10 | 7/41 (A-427, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15438.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.447×** | -10.9 | 5e-25 | 21/30 (C32, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.633×** | -6.0 | 6e-07 | 16/22 (HOP62, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.646×** | -5.5 | 8e-06 | 15/27 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.742×** | -4.0 | 0.007 | 14/43 (HT-29, H4, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.818×** | -3.9 | 0.011 | 17/45 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 0.05 µM |  | **0.736×** | -3.8 | 0.011 | 12/42 (BT-474, AsPC-1, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.762×** | -3.7 | 0.018 | 10/46 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.766×** | -3.6 | 0.020 | 12/43 (CHP-212, HOP62, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | **0.832×** | -3.5 | 0.026 | 12/45 (A-172, NCI-H2347, …) | top dose only | position effect removed |
| [[Esmolol (hydrochloride) (drug)]] 0.5 µM |  | **0.776×** | -3.4 | 0.032 | 10/42 (J82, BT-474, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -3.3 | 0.042 | 8/46 (HOP62, KATO III, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.791×** | -3.2 | 0.064 | 10/44 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.791×** | -3.2 | 0.064 | 10/45 (KATO III, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15438. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 14.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.85× (z +20.8) | [[Dinaciclib (drug)]] 5 µM 0.260× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 28.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.316× (z -8.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 20.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +13.4) | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -9.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 19.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -9.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 7.87 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.40× (z +9.9) | [[Docetaxel (drug)]] 0.05 µM 0.151× (z -8.9) ⚠ transcription drop; cell-cycle shift, explains ~9% of this change |
| [[NCI-H23 (line)]] | alt | 18.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +9.5) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.165× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 15.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +13.7) | — |
| [[RKO (line)]] | wt | 13.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +9.0) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.119× (z -9.9) |
| [[A-172 (line)]] | wt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +11.1) | — |
| [[A-427 (line)]] | wt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +9.3) | — |
| [[A498 (line)]] | wt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +12.3) | — |
| [[A549 (line)]] | wt | 9.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +11.8) | — |
| [[AsPC-1 (line)]] | alt | 8.08 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0524× (z -12.9) |
| [[C32 (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -9.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 26.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 8.79 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0880× (z -8.7) |
| [[HOP62 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -12.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 12.3 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 0.5 µM 0.0485× (z -13.6) |
| [[hTERT-HPNE (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0822× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 5.76 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0816× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 17.6 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0813× (z -9.4) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 8.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 8.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -9.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 4.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15438), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF14]] | +0.83 | +0.83 / +0.80 | both halves | 7e-06 |  |
| [[NBPF10]] | +0.74 | +0.69 / +0.73 | both halves | 7e-06 | STRING 431; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[NOTCH2NLB]] | +0.72 | +0.62 / +0.77 | both halves | 7e-06 | pathway: Expression of NOTCH2NL genes; STRING 410 |
| [[NBPF26]] | +0.71 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[NBPF19]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 | STRING 668 |
| [[NOTCH2]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 | pathway: NOTCH2 Activation and Transmission of Signal to the Nucleus |
| [[NOTCH2NLC]] | +0.63 | +0.52 / +0.67 | both halves | 1e-05 | pathway: Expression of NOTCH2NL genes |
| [[CCDC148]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[NFKBIE]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[FAM110A]] | +0.54 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[COL5A3]] | +0.52 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[PDGFB]] | +0.50 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[FMNL3]] | +0.50 | +0.51 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRRAP]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[ADPGK]] | -0.55 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[VTI1A]] | -0.54 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[GTF3C3]] | -0.52 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[IPO11]] | -0.52 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[POLR3E]] | -0.51 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[HERC2]] | -0.50 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[ALG3]] | -0.50 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[PSMB2]] | -0.49 | -0.47 / -0.41 | both halves | 4e-05 | pathway: Signaling by NOTCH |
| [[PSMB3]] | -0.49 | -0.52 / -0.42 | both halves | 4e-05 | pathway: Signaling by NOTCH |
| [[TYW1]] | -0.49 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[PDS5A]] | -0.49 | -0.52 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPOCD1]] | B | SPOCD1 activity raises NOTCH2NLA's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 1.73× lower at baseline in the lines without SPOCD1 | 0.022 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1 |
| [[PIR]] | B | PIR activity lowers NOTCH2NLA's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.27× higher at baseline in the lines without PIR | 0.093 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |
| [[PGM5P2]] | B | PGM5P2 activity raises NOTCH2NLA's level | lines that do not express PGM5P2 (9) vs lines expressing it (41) | 1.44× lower at baseline in the lines without PGM5P2 | 0.097 | ⚠ within organs, on part of the lines; also absent: PGM5P2-1, PALM2AKAP2, FKBP7; maybe low, not absent |
| [[TMEM132D]] | B | TMEM132D activity lowers NOTCH2NLA's level | lines that do not express TMEM132D (29) vs lines expressing it (21) | 1.41× higher at baseline in the lines without TMEM132D | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000271955, ENSG00000287211, GABRG2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 226]] — NOTCH2 Activation and Transmission of Signal to the Nucleus; 9 genes; every member is in the + arm (projection on the module's main direction 0.885). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.4, -29.5); signed map (44.5, -15.5). **Vector** length 64.3, 10.5% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +23.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.6 | +11.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +3.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.0 | +9.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.9 | +0.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +0.8 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.8 | +2.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.6 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.3 | -10.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -0.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | notch 2 N-terminal like A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.1 — chr1:146,146,203-146,229,041 (-) |
| Ensembl biotype | protein_coding |
| Also known as | N2N; previously NOTCH2NL |
| Reactome | 6 pathways, smallest: Expression of NOTCH2NL genes; NOTCH2 Activation and Transmission of Signal to the Nucleus; Signaling by NOTCH2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z3S9](https://www.uniprot.org/uniprotkb/Q7Z3S9) (Notch homolog 2 N-terminal-like protein A):

> Human-specific protein that promotes neural progenitor proliferation and evolutionary expansion of the brain neocortex by regulating the Notch signaling pathway. Able to promote neural progenitor self-renewal, possibly by down-regulating neuronal differentiation genes, thereby delaying the differentiation of neuronal progenitors and leading to an overall final increase in neuronal production. Acts by enhancing the Notch signaling pathway via two different mechanisms that probably work in …

**Summary**, from NCBI Gene [388677](https://www.ncbi.nlm.nih.gov/gene/388677):

> Enables Notch binding activity. Involved in cerebral cortex development and positive regulation of Notch signaling pathway. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:31862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31862) · Entrez [388677](https://www.ncbi.nlm.nih.gov/gene/388677) · UniProt [Q7Z3S9](https://www.uniprot.org/uniprotkb/Q7Z3S9) · Ensembl [ENSG00000264343](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000264343)

## Data

Gene col 15438: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15438); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15438, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15438]; `tensor/DDL_lfc|DDL_z.npy` [15438]; `embed/gene_vectors.npy` [15438]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15438 or target_col == 15438). Every well: [[NOTCH2NLA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOTCH2NLA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
