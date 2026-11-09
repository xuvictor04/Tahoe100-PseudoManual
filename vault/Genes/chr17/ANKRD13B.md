---
symbol: "ANKRD13B"
type: "gene"
col: 12652
ensembl_id: "ENSG00000198720"
name: "ankyrin repeat domain 13B"
location: "17q11.2"
module: 18
arm: "+"
pooled_cpm: 8.02
n_lines_expressing: 47
n_dd_up: 29
n_dd_down: 5
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 13
direction_downstream: 18
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ANKRD13B

*ankyrin repeat domain 13B* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.03× (z +13.6, q 1e-39, up in 32 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.447× (z -15.5, q 0e+00, down in 32 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADCY3]] (+0.71, fdr 7e-06), [[CAPN15]] (+0.68, fdr 7e-06), [[TSEN54]] (+0.66, fdr 7e-06); moves opposite to [[YIPF6]] (-0.56, fdr 1e-05), [[NDUFA5]] (-0.56, fdr 2e-05), [[ZNF776]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[NT5M]] → it (grade B ⚠); 18 go from it, the strongest it → [[ADCY3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12652.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +13.6 | 1e-39 | 32/40 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +9.0 | 7e-17 | 21/31 (SW1417, J82, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.71×** | +7.3 | 5e-11 | 23/41 (KATO III, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +6.8 | 2e-09 | 24/43 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +6.2 | 7e-08 | 18/44 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.60×** | +6.1 | 8e-08 | 18/40 (A549, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +5.5 | 3e-06 | 22/44 (HOP62, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.44×** | +4.8 | 1e-04 | 5/13 (SW480, HS-578T, …) | inconsistent across doses | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.85×** | +4.4 | 7e-04 | 2/15 (A498, MIA PaCa-2) | top dose only | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +4.3 | 9e-04 | 10/44 (NCI-H1792, SNU-423, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.37×** | +4.3 | 0.001 | 14/44 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +4.2 | 0.001 | 9/43 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.38×** | +4.2 | 0.001 | 15/43 (A549, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.35×** | +4.1 | 0.002 | 17/44 (NCI-H1573, HOP62, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +4.1 | 0.002 | 14/44 (NCI-H460, SW480, …) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.73×** | +3.9 | 0.003 | 5/36 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.003 | 15/43 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.48×** | +3.8 | 0.005 | 5/35 (RKO, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.56×** | +3.2 | 0.037 | 4/37 (RKO, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.040 | 4/40 (SW 900, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.062 | 2/40 (A498, SHP-77) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +3.0 | 0.062 | 6/43 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.062 | 6/43 (NCI-H460, SW1417, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12652.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.447×** | -15.5 | 0e+00 | 32/40 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.552×** | -7.8 | 2e-12 | 22/42 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.620×** | -6.3 | 5e-08 | 18/40 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.741×** | -4.1 | 0.006 | 13/44 (KATO III, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.604×** | -3.6 | 0.035 | 19/43 (MIA PaCa-2, AN3 CA, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 0.655× | -3.0 | 0.24 | 8/35 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12652. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 10.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -14.2) |
| [[A549 (line)]] | wt | 10.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 10.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -9.5) |
| [[A498 (line)]] | wt | 6.56 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 7.97 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -8.5) |
| [[J82 (line)]] | alt | 4.47 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0788× (z -14.5) |
| [[LoVo (line)]] | wt | 5.88 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.115× (z -10.8) ⚠ cell-cycle shift, explains ~80% of this change |
| [[MIA PaCa-2 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.616× (z -11.1) ⚠ position not correctable |
| [[PANC-1 (line)]] | alt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -10.6) |
| [[RKO (line)]] | wt | 16.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.127× (z -11.5) |
| [[SW1417 (line)]] | alt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -11.8) |
| [[SW480 (line)]] | alt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -13.9) |
| [[A-427 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12652), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADCY3]] | +0.71 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[CAPN15]] | +0.68 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[TSEN54]] | +0.66 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[GARNL3]] | +0.66 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[SSBP4]] | +0.66 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[UCK2]] | +0.65 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[PALS2]] | +0.65 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[MACROD1]] | +0.63 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[PPARGC1B]] | +0.63 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[PRKX]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[PTDSS2]] | +0.60 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[SLC27A4]] | +0.60 | +0.62 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIPF6]] | -0.56 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[NDUFA5]] | -0.56 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[ZNF776]] | -0.56 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[CGGBP1]] | -0.55 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[LARP7]] | -0.55 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[ZC3H11A]] | -0.54 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[TIA1]] | -0.54 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[OCIAD1]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[SUB1]] | -0.53 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[DZIP3]] | -0.53 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[XRN1]] | -0.52 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[LZIC]] | -0.52 | -0.53 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 10, C 3. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity raises ANKRD13B's level | lines that do not express NT5M (7) vs lines expressing it (43) | 2.40× lower at baseline in the lines without NT5M | 0.011 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[PHF21B]] | B | PHF21B activity raises ANKRD13B's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 1.71× lower at baseline in the lines without PHF21B | 0.014 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2 |
| [[BRSK2]] | B | BRSK2 activity raises ANKRD13B's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.87× lower at baseline in the lines without BRSK2 | 0.014 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[ADCY3]] | B | ADCY3 activity raises ANKRD13B's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.83× lower at baseline in the lines without ADCY3 | 0.020 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[GALNT14]] | B | GALNT14 activity lowers ANKRD13B's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.33× higher at baseline in the lines without GALNT14 | 0.035 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[LRP3]] | B | LRP3 activity raises ANKRD13B's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 2.07× lower at baseline in the lines without LRP3 | 0.042 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[WNK2]] | B | WNK2 activity raises ANKRD13B's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.74× lower at baseline in the lines without WNK2 | 0.055 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[MSI1]] | B | MSI1 activity raises ANKRD13B's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.83× lower at baseline in the lines without MSI1 | 0.055 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[BEGAIN]] | B | BEGAIN activity raises ANKRD13B's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 1.72× lower at baseline in the lines without BEGAIN | 0.074 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |
| [[PROCR]] | B | PROCR activity lowers ANKRD13B's level | lines that do not express PROCR (8) vs lines expressing it (42) | 1.50× higher at baseline in the lines without PROCR | 0.097 | ⚠ within organs, on part of the lines; also absent: ATP2B4, RNF135, LAMB1; maybe low, not absent |
| [[NCS1]] | C | NCS1 activity raises ANKRD13B's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 3.18× lower at baseline in the lines without NCS1 | 0.008 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent; co-absent with the target |
| [[PPARGC1B]] | C | PPARGC1B activity raises ANKRD13B's level | lines that do not express PPARGC1B (3) vs lines expressing it (47) | 3.37× lower at baseline in the lines without PPARGC1B | 0.095 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, SPDL1, ARHGAP10; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 0, C 18. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | C | ANKRD13B activity raises ADCY3's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 2.90× lower at baseline in the lines without ANKRD13B | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[NPDC1]] | C | ANKRD13B activity raises NPDC1's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 2.55× lower at baseline in the lines without ANKRD13B | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[IMPDH1]] | C | ANKRD13B activity raises IMPDH1's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 2.19× lower at baseline in the lines without ANKRD13B | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[SMIM13]] | C | ANKRD13B activity raises SMIM13's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 2.19× lower at baseline in the lines without ANKRD13B | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[GIT1]] | C | ANKRD13B activity raises GIT1's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 2.00× lower at baseline in the lines without ANKRD13B | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[ZDHHC8]] | C | ANKRD13B activity raises ZDHHC8's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 2.00× lower at baseline in the lines without ANKRD13B | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[B4GALT2]] | C | ANKRD13B activity raises B4GALT2's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 1.91× lower at baseline in the lines without ANKRD13B | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[FOXK2]] | C | ANKRD13B activity raises FOXK2's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 1.85× lower at baseline in the lines without ANKRD13B | 0.068 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[NCLN]] | C | ANKRD13B activity raises NCLN's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 2.01× lower at baseline in the lines without ANKRD13B | 0.072 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[EBPL]] | C | ANKRD13B activity raises EBPL's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 1.70× lower at baseline in the lines without ANKRD13B | 0.077 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[PPARGC1B]] | C | ANKRD13B activity raises PPARGC1B's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 3.07× lower at baseline in the lines without ANKRD13B | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; co-absent with the target |
| [[ANKS6]] | C | ANKRD13B activity raises ANKS6's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 2.03× lower at baseline in the lines without ANKRD13B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-2.3, -1.2); signed map (-5.0, -55.1). **Vector** length 78.4, 15.3% of its response variance represented; |z| ≥ 3 in 807 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +13.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.3 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +9.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -15.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.0 | -7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -6.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.4 | -3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 13B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:29,589,769-29,614,761 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25555 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YJ7](https://www.uniprot.org/uniprotkb/Q86YJ7) (Ankyrin repeat domain-containing protein 13B):

> Ubiquitin-binding protein that specifically recognizes and binds 'Lys-63'-linked ubiquitin. Does not bind 'Lys-48'-linked ubiquitin. Positively regulates the internalization of ligand-activated EGFR by binding to the Ub moiety of ubiquitinated EGFR at the cell membrane.

**Summary**, from NCBI Gene [124930](https://www.ncbi.nlm.nih.gov/gene/124930):

> Enables ubiquitin-modified protein reader activity. Involved in negative regulation of receptor internalization. Located in endosome; perinuclear region of cytoplasm; and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26363](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26363) · Entrez [124930](https://www.ncbi.nlm.nih.gov/gene/124930) · UniProt [Q86YJ7](https://www.uniprot.org/uniprotkb/Q86YJ7) · Ensembl [ENSG00000198720](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198720)

## Data

Gene col 12652: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12652); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12652, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12652]; `tensor/DDL_lfc|DDL_z.npy` [12652]; `embed/gene_vectors.npy` [12652]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12652 or target_col == 12652). Every well: [[ANKRD13B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD13B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
