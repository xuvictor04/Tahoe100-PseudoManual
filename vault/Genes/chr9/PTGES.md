---
symbol: "PTGES"
type: "gene"
col: 7271
ensembl_id: "ENSG00000148344"
name: "prostaglandin E synthase"
location: "9q34.11"
module: 167
arm: "+"
pooled_cpm: 10.93
n_lines_expressing: 33
n_dd_up: 27
n_dd_down: 19
n_dd_up_clean: 25
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 6
direction_downstream: 33
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# PTGES

*prostaglandin E synthase* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.84× (z +8.9, q 2e-16, up in 19 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.500× (z -7.1, q 5e-10, down in 17 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AVPI1]] (+0.63, fdr 7e-06), [[NFIL3]] (+0.61, fdr 1e-05), [[TYMP]] (+0.61, fdr 1e-05); moves opposite to [[MAPKAP1]] (-0.49, fdr 5e-05), [[GBX2-AS1]] (-0.48, fdr 8e-05), [[CCT6A]] (-0.45, fdr 4e-05).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[RAB27B]] → it (grade B ⚠); 33 go from it, the strongest it → [[HLA-E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7271.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +8.9 | 2e-16 | 19/30 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.01×** | +7.2 | 2e-10 | 21/30 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Retinoic acid (drug)]] 5 µM |  | **1.38×** | +4.7 | 6e-04 | 15/30 (NCI-H2347, SW 900, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +4.5 | 8e-04 | 8/24 (NCI-H2030, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.54×** | +4.5 | 9e-04 | 14/30 (SW 900, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.81×** | +4.4 | 0.001 | 12/26 (J82, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +4.3 | 0.001 | 10/25 (A498, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.008 | 12/30 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.8 | 0.009 | 5/31 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.009 | 9/29 (A-172, HOP62, …) | rises with dose | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.66×** | +3.7 | 0.009 | 7/27 (NCI-H460, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.016 | 10/30 (Panc 03.27, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.016 | 11/30 (MIA PaCa-2, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.60×** | +3.5 | 0.022 | 7/30 (Hs 766T, NCI-H1792, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.024 | 8/27 (Hs 766T, RPMI-7951, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.025 | 6/28 (Hs 766T, H4, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.028 | 10/30 (NCI-H460, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.028 | 10/30 (AsPC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7271.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.500×** | -7.1 | 5e-10 | 17/30 (SNU-423, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.517×** | -6.5 | 2e-08 | 15/26 (RPMI-7951, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.539×** | -6.4 | 3e-08 | 19/30 (RPMI-7951, SW 900, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.600×** | -5.3 | 2e-05 | 17/28 (RPMI-7951, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.619×** | -4.9 | 9e-05 | 14/29 (RPMI-7951, SW 900, …) | rises with dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.645×** | -4.5 | 6e-04 | 10/30 (NCI-H460, A498, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.412×** | -4.2 | 0.002 | 13/28 (A549, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.754×** | -4.1 | 0.003 | 14/30 (NCI-H1573, CHP-212, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.678×** | -4.0 | 0.004 | 13/30 (A549, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.681×** | -3.8 | 0.008 | 16/28 (COLO 205, NCI-H460, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.774×** | -3.7 | 0.010 | 15/30 (MIA PaCa-2, RPMI-7951, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.720×** | -3.4 | 0.034 | 13/30 (A498, RPMI-7951, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.724×** | -3.3 | 0.038 | 9/30 (A549, RPMI-7951, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.730×** | -3.2 | 0.048 | 11/30 (CHP-212, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.736×** | -3.2 | 0.060 | 8/30 (H4, NCI-H1573, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.528×** | -3.0 | 0.079 | 8/27 (A498, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 0.5 µM |  | **0.664×** | -3.0 | 0.079 | 3/31 (A498, HOP62, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.531×** | -3.0 | 0.079 | 10/30 (NCI-H1792, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7271. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 42.3 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0469× (z -22.5) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0441× (z -16.3) |
| [[SNU-423 (line)]] | alt | 22.3 | 1 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.45× (z +8.7) | [[Ixazomib citrate (drug)]] 5 µM 0.0396× (z -16.0) |
| [[CHP-212 (line)]] | wt | 79.3 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -10.7) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.132× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 15.5 | 2 (1 ⚠) | 2 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.95× (z +11.2) ⚠ position not correctable · without an alert: [[Tucidinostat (drug)]] 5 µM 3.89× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0469× (z -21.9) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.244× (z -10.1) |
| [[A549 (line)]] | wt | 36.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.141× (z -11.2) |
| [[SW 900 (line)]] | alt | 29.6 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.149× (z -10.3) |
| [[COLO 205 (line)]] | alt | 6.56 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0562× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 23.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0564× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 18.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -13.6) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -13.4) |
| [[BT-474 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -9.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 12.8 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0678× (z -8.7) |
| [[HS-578T (line)]] | alt | 4.99 | 0 | 1 | — | [[Peretinoin (drug)]] 0.5 µM 0.0581× (z -9.2) |
| [[J82 (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +9.1) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[NCI-H1792 (line)]] | alt | 30.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.219× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 7.25 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -9.6) ⚠ cell-cycle shift, explains ~54% of this change |
| [[NCI-H23 (line)]] | alt | 5.43 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -8.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SW1417 (line)]] | alt | 5.61 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0774× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.786 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.875 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.815 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.832 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.898 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.885 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.985 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.92 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7271), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVPI1]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[NFIL3]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[TYMP]] | +0.61 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[CFB]] | +0.58 | +0.57 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[GPCPD1]] | +0.57 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[RHOV]] | +0.56 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[THEMIS2]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[C3]] | +0.55 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[C1R]] | +0.54 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[BMF]] | +0.54 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[ACO1]] | +0.54 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[PLD1]] | +0.54 | +0.42 / +0.58 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAP1]] | -0.49 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[GBX2-AS1]] | -0.48 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[CCT6A]] | -0.45 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[MSANTD2]] | -0.45 | -0.34 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB27B]] | B | RAB27B activity raises PTGES's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 2.31× lower at baseline in the lines without RAB27B | 0.038 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[RHCG]] | B | RHCG activity raises PTGES's level | lines that do not express RHCG (33) vs lines expressing it (17) | 2.75× lower at baseline in the lines without RHCG | 0.041 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[AQP3]] | B | AQP3 activity raises PTGES's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 2.09× lower at baseline in the lines without AQP3 | 0.088 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[RHOV]] | B | RHOV activity raises PTGES's level | lines that do not express RHOV (23) vs lines expressing it (27) | 1.32× lower at baseline in the lines without RHOV | 0.093 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[NOD2]] | C | NOD2 activity raises PTGES's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 2.98× lower at baseline in the lines without NOD2 | 0.030 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2; co-absent with the target |
| [[BDKRB2]] | C | BDKRB2 activity raises PTGES's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 2.33× lower at baseline in the lines without BDKRB2 | 0.053 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003; co-absent with the target |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 28, C 5. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-E]] | B | PTGES activity raises HLA-E's level | lines that do not express PTGES (17) vs lines expressing it (33) | 1.74× lower at baseline in the lines without PTGES | 0.004 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[RAB9A]] | B | PTGES activity raises RAB9A's level | lines that do not express PTGES (17) vs lines expressing it (33) | 1.57× lower at baseline in the lines without PTGES | 0.008 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[CEBPB]] | B | PTGES activity raises CEBPB's level | lines that do not express PTGES (17) vs lines expressing it (33) | 1.91× lower at baseline in the lines without PTGES | 0.011 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[NAMPT]] | B | PTGES activity raises NAMPT's level | lines that do not express PTGES (17) vs lines expressing it (33) | 2.01× lower at baseline in the lines without PTGES | 0.012 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[B2M]] | B | PTGES activity raises B2M's level | lines that do not express PTGES (17) vs lines expressing it (33) | 1.87× lower at baseline in the lines without PTGES | 0.018 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[HLA-F]] | B | PTGES activity raises HLA-F's level | lines that do not express PTGES (17) vs lines expressing it (33) | 2.00× lower at baseline in the lines without PTGES | 0.020 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[RNF114]] | B | PTGES activity raises RNF114's level | lines that do not express PTGES (17) vs lines expressing it (33) | 1.39× lower at baseline in the lines without PTGES | 0.025 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[RHOV]] | B | PTGES activity raises RHOV's level | lines that do not express PTGES (17) vs lines expressing it (33) | 2.16× lower at baseline in the lines without PTGES | 0.026 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[ODF3B]] | B | PTGES activity raises ODF3B's level | lines that do not express PTGES (17) vs lines expressing it (33) | 1.71× lower at baseline in the lines without PTGES | 0.032 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[BCL3]] | B | PTGES activity raises BCL3's level | lines that do not express PTGES (17) vs lines expressing it (33) | 1.82× lower at baseline in the lines without PTGES | 0.034 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[TOM1]] | B | PTGES activity raises TOM1's level | lines that do not express PTGES (17) vs lines expressing it (33) | 1.58× lower at baseline in the lines without PTGES | 0.039 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[CCT6A]] | B | PTGES activity lowers CCT6A's level | lines that do not express PTGES (17) vs lines expressing it (33) | 1.45× higher at baseline in the lines without PTGES | 0.040 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.7, 17.6); signed map (17.7, 26.2). **Vector** length 81.4, 19.7% of its response variance represented; |z| ≥ 3 in 855 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +7.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.5 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +4.4 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.2 | +3.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.9 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.0 | -6.4 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.1 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -2.1 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -4.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | prostaglandin E synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:129,738,331-129,753,042 (-) |
| Ensembl biotype | protein_coding |
| Also known as | mPGES-1, MGST-IV, PIG12, MGST1-L1, TP53I12; previously MGST1L1 |
| Gene groups (HGNC) | MAPEG superfamily; Prostaglandin E synthases |
| Hallmark sets | XENOBIOTIC_METABOLISM, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: Synthesis of Prostaglandins (PG) and Thromboxanes (TX); Arachidonate metabolism; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O14684](https://www.uniprot.org/uniprotkb/O14684) (Prostaglandin E synthase):

> Terminal enzyme of the cyclooxygenase (COX)-2-mediated prostaglandin E2 (PGE2) biosynthetic pathway. Catalyzes the glutathione-dependent oxidoreduction of prostaglandin endoperoxide H2 (PGH2) to prostaglandin E2 (PGE2) in response to inflammatory stimuli. Similarly, catalyzes the conversion of PGH3 (derived from eicosapentaenoate (EPA, C20:5n-3)) to PGE3, though PGH2 remains the preferred substrate. Plays a key role in inflammation response, fever and pain (By similarity). Also catalyzes the …

**Summary**, from NCBI Gene [9536](https://www.ncbi.nlm.nih.gov/gene/9536):

> The protein encoded by this gene is a glutathione-dependent prostaglandin E synthase. The expression of this gene has been shown to be induced by proinflammatory cytokine interleukin 1 beta (IL1B). Its expression can also be induced by tumor suppressor protein TP53, and may be involved in TP53 induced apoptosis. Knockout studies in mice suggest that this gene may contribute to the pathogenesis of collagen-induced arthritis and mediate acute pain during inflammatory responses. [provided by …

**Accessions** — [HGNC:9599](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9599) · Entrez [9536](https://www.ncbi.nlm.nih.gov/gene/9536) · UniProt [O14684](https://www.uniprot.org/uniprotkb/O14684) · Ensembl [ENSG00000148344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148344)

## Data

Gene col 7271: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7271); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7271, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7271]; `tensor/DDL_lfc|DDL_z.npy` [7271]; `embed/gene_vectors.npy` [7271]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7271 or target_col == 7271). Every well: [[PTGES — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTGES.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
