---
symbol: "RAB23"
type: "gene"
col: 3336
ensembl_id: "ENSG00000112210"
name: "RAB23, member RAS oncogene family"
location: "6p12.1-p11.2"
module: 25
arm: "+"
pooled_cpm: 15.32
n_lines_expressing: 48
n_dd_up: 25
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# RAB23

*RAB23, member RAS oncogene family* — 6p12.1-p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.80× (z +9.4, q 2e-18, up in 16 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.36× (z +7.3, q 7e-11, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.601× (z -8.5, q 8e-15, down in 25 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.631× (z -7.7, q 3e-12, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLAIN2]] (+0.56, fdr 2e-05), [[BVES]] (+0.56, fdr 1e-05), [[SNX7]] (+0.56, fdr 1e-05); moves opposite to [[BIN3]] (-0.52, fdr 2e-05), [[GCDH]] (-0.51, fdr 7e-05), [[POLR2J4]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3336.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +9.4 | 2e-18 | 16/26 (SW 900, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.37×** | +7.4 | 3e-11 | 24/44 (SW480, RKO, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +7.3 | 7e-11 | 27/46 (C32, A-427, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +6.9 | 5e-10 | 24/45 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.51×** | +6.9 | 6e-10 | 20/35 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.51×** | +6.6 | 3e-09 | 23/37 (SW480, HCT15, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +6.3 | 2e-08 | 19/46 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.46×** | +6.3 | 2e-08 | 20/45 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.45×** | +6.1 | 5e-08 | 20/45 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +6.0 | 9e-08 | 1/46 (MIA PaCa-2) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.45×** | +6.0 | 1e-07 | 21/44 (SW480, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.43×** | +6.0 | 1e-07 | 22/46 (CFPAC-1, NCI-H460, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +5.8 | 3e-07 | 20/46 (CFPAC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.41×** | +5.7 | 6e-07 | 20/46 (CFPAC-1, NCI-H460, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.26×** | +5.5 | 2e-06 | 17/46 (J82, CFPAC-1, …) | top dose only | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.3 | 4e-06 | 19/46 (SW480, HEC-1-A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +5.1 | 9e-06 | 15/46 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +4.9 | 3e-05 | 15/45 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.31×** | +4.1 | 0.001 | 12/46 (C32, SW480, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.002 | 5/46 (A-172, PANC-1, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.006 | 4/42 (A498, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.020 | 12/43 (A549, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.021 | 8/45 (C32, NCI-H460, …) | all doses, flat |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **1.20×** | +2.8 | 0.092 | 1/45 (C32) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3336.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.601×** | -8.5 | 8e-15 | 25/43 (NCI-H2030, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.631×** | -7.7 | 3e-12 | 26/46 (SW 900, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.682×** | -6.4 | 2e-08 | 23/44 (SNU-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.684×** | -6.4 | 3e-08 | 21/46 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.518×** | -5.8 | 9e-07 | 16/46 (LOX-IMVI, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.749×** | -4.9 | 1e-04 | 20/45 (LS 180, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.780×** | -4.2 | 0.002 | 12/45 (C-33 A, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.787×** | -4.0 | 0.004 | 14/46 (hTERT-HPNE, SW48, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.857× | -3.7 | 0.014 | 18/44 (LOX-IMVI, HOP62, …) | top dose only | composition shift |
| [[Trimetrexate (drug)]] 0.5 µM |  | **0.819×** | -3.4 | 0.041 | 12/45 (LOX-IMVI, SHP-77, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.748×** | -3.4 | 0.041 | 8/46 (H4, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.686×** | -3.3 | 0.041 | 9/42 (SW 900, HOP62, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.813×** | -3.3 | 0.041 | 20/44 (NCI-H1792, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.770× | -3.0 | 0.10 | 5/44 (SW1417, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3336. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 12.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0483× (z -20.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 18.9 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.249× (z -9.5) |
| [[A-427 (line)]] | wt | 24.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[H4 (line)]] | wt | 18.3 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0841× (z -9.5) |
| [[HCT15 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0719× (z -10.3) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 21.8 | 0 | 1 | — | [[Pimitespib (drug)]] 5 µM 0.0895× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 6.02 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0795× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.317× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 8.59 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.280× (z -8.6) |
| [[SW 900 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -11.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 11.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A498 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.26 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3336), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLAIN2]] | +0.56 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[BVES]] | +0.56 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[SNX7]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[LPGAT1]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SSX2IP]] | +0.55 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[SGCB]] | +0.54 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[DCK]] | +0.54 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[ICMT]] | +0.53 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[EXOC5]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[RBBP8]] | +0.52 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[COX11]] | +0.52 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[OGFRL1]] | +0.52 | +0.46 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BIN3]] | -0.52 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[GCDH]] | -0.51 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[POLR2J4]] | -0.50 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[UXT]] | -0.50 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[CWC25]] | -0.49 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[ACOX3]] | -0.48 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[TRMT44]] | -0.48 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ENDOV]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[TM9SF4]] | -0.47 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[IGBP1]] | -0.47 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[ECSIT]] | -0.47 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[PILRB]] | -0.45 | -0.45 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RAB23's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NECTIN3]] | B | NECTIN3 activity raises RAB23's level | lines that do not express NECTIN3 (11) vs lines expressing it (39) | 1.76× lower at baseline in the lines without NECTIN3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CD96, NECTIN3-AS1, GPR176 |
| [[OGFRL1]] | B | OGFRL1 activity raises RAB23's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 1.57× lower at baseline in the lines without OGFRL1 | 0.067 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.497). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.1, -34.5); signed map (-18.3, -39.5). **Vector** length 75.4, 13.0% of its response variance represented; |z| ≥ 3 in 1,027 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +6.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | +0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.4 | +6.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +2.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.7 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +7.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.1 | +4.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.6 | +0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +5.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | +2.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -3.0 | -3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.9 | -3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.4 | -8.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | -4.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.0 | -3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.7 | -2.5 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | RAB23, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.1-p11.2 — chr6:57,186,992-57,222,307 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 1 pathways, smallest: RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULC3](https://www.uniprot.org/uniprotkb/Q9ULC3) (Ras-related protein Rab-23):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different set of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. In conjunction with IFT57 and KIF17, it drives the localization of specific G protein-coupled receptors, such as the …

**Summary**, from NCBI Gene [51715](https://www.ncbi.nlm.nih.gov/gene/51715):

> This gene encodes a small GTPase of the Ras superfamily. Rab proteins are involved in the regulation of diverse cellular functions associated with intracellular membrane trafficking, including autophagy and immune response to bacterial infection. The encoded protein may play a role in central nervous system development by antagonizing sonic hedgehog signaling. Disruption of this gene has been implicated in Carpenter syndrome as well as cancer. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:14263](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14263) · Entrez [51715](https://www.ncbi.nlm.nih.gov/gene/51715) · UniProt [Q9ULC3](https://www.uniprot.org/uniprotkb/Q9ULC3) · Ensembl [ENSG00000112210](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112210)

## Data

Gene col 3336: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3336); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3336, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3336]; `tensor/DDL_lfc|DDL_z.npy` [3336]; `embed/gene_vectors.npy` [3336]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3336 or target_col == 3336). Every well: [[RAB23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
