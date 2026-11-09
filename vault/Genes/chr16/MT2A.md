---
symbol: "MT2A"
type: "gene"
col: 4590
ensembl_id: "ENSG00000125148"
name: "metallothionein 2A"
location: "16q13"
module: 113
arm: "+"
pooled_cpm: 785.17
n_lines_expressing: 41
n_dd_up: 11
n_dd_down: 16
n_dd_up_clean: 10
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 8
direction_downstream: 9
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# MT2A

*metallothionein 2A* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Betamethasone dipropionate (drug)]] 5 µM: 2.59× (z +4.6, q 0.001, up in 32 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.344× (z -7.7, q 1e-11, down in 38 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MT1X]] (+0.91, fdr 7e-06), [[ANGPTL4]] (+0.79, fdr 7e-06), [[MT1E]] (+0.78, fdr 7e-06, ⚠ read-through risk), [[ID1]] (+0.67, fdr 1e-05); moves opposite to [[MATN2]] (-0.60, fdr 1e-05), [[PGRMC1]] (-0.58, fdr 3e-05), [[BBOX1-AS1]] (-0.55, fdr 3e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 9 go from it, the strongest it → [[SLC25A37]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4590.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.59×** | +4.6 | 0.001 | 32/40 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **2.49×** | +4.6 | 0.001 | 27/39 (NCI-H2347, Hs 766T, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **2.30×** | +4.2 | 0.005 | 27/39 (Hs 766T, NCI-H2347, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.28×** | +4.1 | 0.005 | 27/39 (Hs 766T, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **2.18×** | +3.9 | 0.010 | 27/39 (NCI-H2347, Hs 766T, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **2.05×** | +3.6 | 0.023 | 26/39 (NCI-H2347, Hs 766T, …) | all doses, flat | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **2.05×** | +3.6 | 0.023 | 27/39 (NCI-H2347, Hs 766T, …) | all doses, flat | position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +3.6 | 0.023 | 28/39 (Panc 03.27, NCI-H2347, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **2.02×** | +3.5 | 0.024 | 26/39 (Hs 766T, NCI-H2347, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **1.95×** | +3.4 | 0.040 | 31/39 (PANC-1, A549, …) | top dose only | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.42×** | +3.4 | 0.040 | 27/39 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4590.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.344×** | -7.7 | 1e-11 | 38/40 (RKO, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.436×** | -6.0 | 8e-07 | 35/39 (C32, J82, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.361×** | -5.2 | 4e-05 | 37/39 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.409×** | -4.4 | 0.002 | 37/39 (SW 1088, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.385×** | -4.2 | 0.003 | 36/41 (SK-MEL-2, A-172, …) | all doses, flat | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.419×** | -4.1 | 0.004 | 38/39 (HepG2/C3A, BT-474, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.451×** | -3.9 | 0.008 | 30/38 (HepG2/C3A, A-172, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.214×** | -3.8 | 0.010 | 36/40 (A549, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.483×** | -3.7 | 0.014 | 25/39 (NCI-H23, H4, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.496×** | -3.6 | 0.021 | 32/39 (BT-474, HCT15, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.633×** | -3.2 | 0.061 | 35/39 (BT-474, HCT15, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.276×** | -3.2 | 0.061 | 31/40 (HepG2/C3A, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.277×** | -3.2 | 0.061 | 26/39 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.644×** | -3.2 | 0.061 | 27/39 (J82, SW48, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.286×** | -3.1 | 0.072 | 33/41 (HepG2/C3A, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.540×** | -3.0 | 0.092 | 23/39 (A-172, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +1.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4590. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 722 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.201× (z -10.0) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -9.5) |
| [[J82 (line)]] | alt | 1,813 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -10.2) |
| [[RKO (line)]] | wt | 1,410 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -11.0) |
| [[A549 (line)]] | wt | 990 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -9.1) |
| [[H4 (line)]] | wt | 1,206 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 982 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 1,218 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -10.9) |
| [[HOP62 (line)]] | alt | 1,245 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 641 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HS-578T (line)]] | alt | 1,577 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 1,892 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 875 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 678 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 682 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 1088 (line)]] | alt | 2,160 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -9.0) |
| [[SW 900 (line)]] | alt | 1,036 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -10.2) |
| [[SW480 (line)]] | alt | 381 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 1,225 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 60.5 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 508 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 438 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 131 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 341 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 95.7 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1,791 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 94.8 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 432 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 74.7 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 698 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 87.9 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 195 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 693 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 303 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 541 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4,194 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 493 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 391 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 501 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 334 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 668 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 460 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 558 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 979 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 324 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 223 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 447 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 80.0 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 328 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4590), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1X]] | +0.91 | +0.87 / +0.88 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 866 |
| [[ANGPTL4]] | +0.79 | +0.71 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[MT1E]] | +0.78 | +0.70 / +0.78 | both halves | 7e-06 | same gene group; pathway: HALLMARK_HYPOXIA; STRING 829; ⚠ **readthrough risk**: MT1E lies 16.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[MT1A]] | +0.72 | +0.60 / +0.68 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 429; ⚠ same locus (29.2 kb, same strand: neighbours can correlate without regulation) |
| [[MT1F]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 772; ⚠ same locus (48.2 kb, same strand: neighbours can correlate without regulation) |
| [[ID1]] | +0.67 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[IRX3]] | +0.66 | +0.61 / +0.77 | both halves | 7e-06 |  |
| [[ZMYND8]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[CCL20]] | +0.66 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[OSBPL5]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[TANC2]] | +0.64 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[CEBPB]] | +0.63 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[SAA1]] | +0.63 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[IRS2]] | +0.62 | +0.51 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[TBC1D8]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MATN2]] | -0.60 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[PGRMC1]] | -0.58 | -0.44 / -0.55 | both halves | 3e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[BBOX1-AS1]] | -0.55 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[LDB1]] | -0.54 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[NNT]] | -0.53 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[C5orf15]] | -0.53 | -0.29 / -0.42 | both halves | 3e-04 |  |
| [[SETD7]] | -0.52 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[NAXD]] | -0.51 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[INPPL1]] | -0.51 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[PAPOLA]] | -0.51 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[EIF4G2]] | -0.51 | -0.32 / -0.37 | both halves | 1e-04 | pathway: Interferon Signaling |
| [[MOB1A]] | -0.51 | -0.34 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises MT2A's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.0% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[ITPRIP]] | B | ITPRIP activity raises MT2A's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 2.63× lower at baseline in the lines without ITPRIP | 0.030 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[NIBAN2]] | B | NIBAN2 activity raises MT2A's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 4.18× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[SLC16A2]] | B | SLC16A2 activity raises MT2A's level | lines that do not express SLC16A2 (14) vs lines expressing it (36) | 2.46× lower at baseline in the lines without SLC16A2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A3, LOXL2, ENSG00000234405 |
| [[SLC25A37]] | B | SLC25A37 activity raises MT2A's level | lines that do not express SLC25A37 (5) vs lines expressing it (45) | 2.89× lower at baseline in the lines without SLC25A37 | 0.086 | ⚠ within organs, on part of the lines; also absent: SSBP2, TP53I13; maybe low, not absent |
| [[FOXC2]] | B | FOXC2 activity raises MT2A's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 2.28× lower at baseline in the lines without FOXC2 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT |
| [[ITGA10]] | B | ITGA10 activity raises MT2A's level | lines that do not express ITGA10 (9) vs lines expressing it (41) | 2.37× lower at baseline in the lines without ITGA10 | 0.097 | ⚠ within organs, on part of the lines; also absent: SLC17A7, ZEB1, BOLA3-DT; maybe low, not absent |
| [[MT1X]] | C | MT1X activity raises MT2A's level | lines that do not express MT1X (5) vs lines expressing it (45) | 6.97× lower at baseline in the lines without MT1X | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RABGEF1P3, KIFC3, ENSG00000255031; co-absent with the target; its own permutation p |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A37]] | B | MT2A activity raises SLC25A37's level | lines that do not express MT2A (9) vs lines expressing it (41) | 2.71× lower at baseline in the lines without MT2A | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000289942, TRAF1, MT1X |
| [[ITPRIP]] | B | MT2A activity raises ITPRIP's level | lines that do not express MT2A (9) vs lines expressing it (41) | 2.84× lower at baseline in the lines without MT2A | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000289942, TRAF1, MT1X |
| [[SGSM2]] | B | MT2A activity raises SGSM2's level | lines that do not express MT2A (9) vs lines expressing it (41) | 1.27× lower at baseline in the lines without MT2A | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000289942, TRAF1, MT1X |
| [[SEC14L2]] | B | MT2A activity raises SEC14L2's level | lines that do not express MT2A (9) vs lines expressing it (41) | 1.90× lower at baseline in the lines without MT2A | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000289942, TRAF1, MT1X |
| [[ARL4A]] | B | MT2A activity lowers ARL4A's level | lines that do not express MT2A (9) vs lines expressing it (41) | 2.00× higher at baseline in the lines without MT2A | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000289942, TRAF1, MT1X |
| [[ELOB]] | B | MT2A activity lowers ELOB's level | lines that do not express MT2A (9) vs lines expressing it (41) | 1.33× higher at baseline in the lines without MT2A | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000289942, TRAF1, MT1X |
| [[PHC2]] | B | MT2A activity raises PHC2's level | lines that do not express MT2A (9) vs lines expressing it (41) | 1.93× lower at baseline in the lines without MT2A | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000289942, TRAF1, MT1X |
| [[DSC2]] | B | MT2A activity lowers DSC2's level | lines that do not express MT2A (9) vs lines expressing it (41) | 3.39× higher at baseline in the lines without MT2A | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000289942, TRAF1, MT1X |
| [[MT1X]] | C | MT2A activity raises MT1X's level | lines that do not express MT2A (9) vs lines expressing it (41) | 4.14× lower at baseline in the lines without MT2A | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000289942, TRAF1, MT1X; co-absent with the target |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.823). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.5, 13.2); signed map (14.4, 31.6). **Vector** length 142, 57.8% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.8 | +1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +0.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +5.2 | +3.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +5.0 | +3.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.0 | +4.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +5.0 | +4.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +4.8 | +4.2 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.6 | -0.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.2 | -0.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.7 | +1.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -6.5 | -6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.5 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.4 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.1 | -3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.0 | -2.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -4.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | metallothionein 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:56,608,584-56,609,497 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MT2 |
| Gene groups (HGNC) | Metallothioneins |
| Hallmark sets | XENOBIOTIC_METABOLISM, INTERFERON_GAMMA_RESPONSE, HYPOXIA, G2M_CHECKPOINT |
| Reactome | 6 pathways, smallest: Metallothioneins bind metals; Response to metal ions; Interferon gamma signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P02795](https://www.uniprot.org/uniprotkb/P02795) (Metallothionein-2):

> Metallothioneins have a high content of cysteine residues that bind various heavy metals; these proteins are transcriptionally regulated by both heavy metals and glucocorticoids.

**Summary**, from NCBI Gene [4502](https://www.ncbi.nlm.nih.gov/gene/4502):

> This gene is a member of the metallothionein family of genes. Proteins encoded by this gene family are low in molecular weight, are cysteine-rich, lack aromatic residues, and bind divalent heavy metal ions, altering the intracellular concentration of heavy metals in the cell. These proteins act as anti-oxidants, protect against hydroxyl free radicals, are important in homeostatic control of metal in the cell, and play a role in detoxification of heavy metals. The encoded protein interacts with …

**Accessions** — [HGNC:7406](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7406) · Entrez [4502](https://www.ncbi.nlm.nih.gov/gene/4502) · UniProt [P02795](https://www.uniprot.org/uniprotkb/P02795) · Ensembl [ENSG00000125148](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125148)

## Data

Gene col 4590: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4590); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4590, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4590]; `tensor/DDL_lfc|DDL_z.npy` [4590]; `embed/gene_vectors.npy` [4590]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4590 or target_col == 4590). Every well: [[MT2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
