---
symbol: "ZNF286A"
type: "gene"
col: 11927
ensembl_id: "ENSG00000187607"
name: "zinc finger protein 286A"
location: "17p12"
module: 33
arm: "+"
pooled_cpm: 17.3
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# ZNF286A

*zinc finger protein 286A* — 17p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.43× (z +7.5, q 5e-11, up in 28 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.22× (z +5.8, q 7e-07, up in 18 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.763× (z -8.0, q 5e-13, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOXO3B]] (+0.75, fdr 7e-06), [[RABGGTB]] (+0.56, fdr 7e-05), [[SORD]] (+0.55, fdr 2e-05); moves opposite to [[DLEU2]] (-0.49, fdr 5e-05), [[KDM6A]] (-0.48, fdr 0.001, ⚠ one half only (not replicated)), [[TJP2]] (-0.48, fdr 1e-04), [[ANXA2R-AS1]] (-0.47, fdr 3e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[BRSK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11927.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +7.5 | 5e-11 | 28/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.28×** | +7.3 | 9e-11 | 27/47 (A549, A498, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +7.0 | 5e-10 | 22/44 (A498, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.8 | 7e-07 | 18/47 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.33×** | +5.6 | 2e-06 | 20/47 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +5.4 | 5e-06 | 17/47 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **1.21×** | +4.0 | 0.006 | 10/46 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.20×** | +3.8 | 0.010 | 14/46 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.20× | +3.8 | 0.010 | 5/47 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.19× | +3.7 | 0.013 | 12/46 (C32, MIA PaCa-2, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.013 | 3/45 (LOX-IMVI, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | 1.18× | +3.5 | 0.019 | 8/44 (NCI-H2030, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.023 | 3/47 (NCI-H2030, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.047 | 1/43 (LoVo) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.072 | 1/45 (LOX-IMVI) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11927.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.763×** | -8.0 | 5e-13 | 26/47 (RPMI-7951, C32, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.679×** | -7.8 | 1e-12 | 30/47 (C32, C-33 A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.735×** | -6.2 | 8e-08 | 22/46 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.782×** | -5.2 | 3e-05 | 21/46 (hTERT-HPNE, BT-474, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.797×** | -4.6 | 5e-04 | 19/47 (A-427, C32, …) | all doses, stronger at high dose | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.753×** | -4.3 | 0.002 | 14/46 (CFPAC-1, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.765×** | -4.0 | 0.005 | 11/45 (SK-MEL-2, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.774×** | -3.8 | 0.008 | 13/44 (AN3 CA, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.846× | -3.5 | 0.026 | 16/47 (H4, LS 180, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.855× | -3.3 | 0.054 | 12/47 (A-427, H4, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.899× | -3.2 | 0.075 | 18/46 (MIA PaCa-2, NCI-H23, …) | top dose only | composition shift |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.817× | -3.0 | 0.11 | 11/46 (RPMI-7951, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11927. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 21.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -9.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 17.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Allantoin (drug)]] 0.5 µM 0.144× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 26.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -21.8) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 41.9 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -9.8) |
| [[A-427 (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.279× (z -8.9) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A498 (line)]] | wt | 24.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 20.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 13.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.139× (z -10.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 20.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -10.7) |
| [[SNU-1 (line)]] | wt | 18.5 | 0 | 1 | — | [[LJI308 (drug)]] 0.5 µM 0.0782× (z -8.5) |
| [[A-172 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11927), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXO3B]] | +0.75 | +0.65 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[RABGGTB]] | +0.56 | +0.38 / +0.61 | both halves | 7e-05 |  |
| [[SORD]] | +0.55 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[CSNK2A1]] | +0.53 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[EIF3M]] | +0.52 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[NKRF]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[SH3PXD2B]] | +0.52 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[FAM234B]] | +0.51 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[ZNF169]] | +0.51 | +0.42 / +0.55 | both halves | 4e-05 | same gene group |
| [[DFFA]] | +0.50 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[ZNF133]] | +0.50 | +0.47 / +0.50 | both halves | 2e-05 | same gene group |
| [[ZNF875]] | +0.50 | +0.41 / +0.58 | both halves | 4e-05 | same gene group |

## Genes that move opposite

*16 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLEU2]] | -0.49 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[KDM6A]] | -0.48 | -0.17 / -0.53 | ⚠ one half (not replicated) | 0.001 |  |
| [[TJP2]] | -0.48 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[ANXA2R-AS1]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[RMI2]] | -0.46 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[SNHG31]] | -0.46 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[ITFG1]] | -0.45 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[EPS15-AS1]] | -0.44 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[ARID4A]] | -0.44 | -0.24 / -0.51 | both halves | 5e-04 |  |
| [[ATAD2B]] | -0.44 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[PRKCA]] | -0.44 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[RAP2C-AS1]] | -0.43 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[KIAA2026]] | -0.43 | -0.28 / -0.43 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BRSK1]] | B | BRSK1 activity raises ZNF286A's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 1.88× lower at baseline in the lines without BRSK1 | 0.026 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[TJP2]] | B | TJP2 activity lowers ZNF286A's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 1.55× higher at baseline in the lines without TJP2 | 0.031 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises ZNF286A's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.459). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.1, -41.1); signed map (-10.5, -57.3). **Vector** length 69.9, 11.4% of its response variance represented; |z| ≥ 3 in 822 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.7 | +7.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +7.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +7.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +5.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +3.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.1 | +3.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -6.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -8.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -2.9 | -5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | -4.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.4 | -4.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 286A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p12 — chr17:15,699,577-15,720,787 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1874; previously ZNF286 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBT8](https://www.uniprot.org/uniprotkb/Q9HBT8) (Zinc finger protein 286A):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [57335](https://www.ncbi.nlm.nih.gov/gene/57335):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13501](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13501) · Entrez [57335](https://www.ncbi.nlm.nih.gov/gene/57335) · UniProt [Q9HBT8](https://www.uniprot.org/uniprotkb/Q9HBT8) · Ensembl [ENSG00000187607](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187607)

## Data

Gene col 11927: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11927); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11927, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11927]; `tensor/DDL_lfc|DDL_z.npy` [11927]; `embed/gene_vectors.npy` [11927]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11927 or target_col == 11927). Every well: [[ZNF286A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF286A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
