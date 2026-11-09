---
symbol: "CTDSPL"
type: "gene"
col: 6915
ensembl_id: "ENSG00000144677"
name: "CTD small phosphatase like"
location: "3p22.2"
module: 18
arm: "+"
pooled_cpm: 83.5
n_lines_expressing: 45
n_dd_up: 4
n_dd_down: 31
n_dd_up_clean: 4
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CTDSPL

*CTD small phosphatase like* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Filgotinib (drug)]] 5 µM: 1.25× (z +4.3, q 0.009, up in 20 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.391× (z -25.4, q 0e+00, down in 42 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA9-AS1]] (+0.66, fdr 7e-06, ⚠ same locus), [[ZNF704]] (+0.60, fdr 7e-06), [[ZNRF3]] (+0.58, fdr 1e-05), [[OSBPL10]] (+0.57, fdr 1e-05); moves opposite to [[FAM149B1]] (-0.50, fdr 7e-05), [[NIT1]] (-0.48, fdr 8e-05), [[YJU2B]] (-0.47, fdr 2e-04).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[CMTM7]] → it (grade B ⚠); 3 go from it, the strongest it → [[CMTM7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6915.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | **1.25×** | +4.3 | 0.009 | 20/43 (SW1417, SW48, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.017 | 17/43 (COLO 205, HT-29, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.043 | 13/42 (Panc 03.27, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.14× | +3.6 | 0.043 | 13/44 (COLO 205, SNU-423, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.043 | 11/43 (A549, NCI-H23, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.20× | +3.4 | 0.058 | 17/44 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | composition shift |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.17 | 11/43 (SW1417, HOP62, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.0 | 0.18 | 14/43 (BT-474, RKO, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 11 with an alert ⚠; shown: the 15 strongest. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6915.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.391×** | -25.4 | 0e+00 | 42/43 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.378×** | -18.7 | 0e+00 | 40/43 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.394×** | -17.8 | 0e+00 | 37/43 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.403×** | -17.4 | 0e+00 | 36/43 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.397×** | -17.0 | 0e+00 | 40/43 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.488×** | -13.8 | 5e-41 | 39/43 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.515×** | -12.7 | 5e-35 | 31/43 (SW480, SW48, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.642×** | -12.0 | 3e-31 | 28/44 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.324×** | -11.3 | 1e-27 | 36/44 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.598×** | -9.9 | 4e-21 | 32/43 (SW48, A-427, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.628×** | -8.6 | 6e-16 | 28/42 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.676×** | -7.5 | 3e-12 | 33/43 (SW48, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -7.0 | 8e-11 | 30/45 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.700×** | -6.8 | 3e-10 | 28/43 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.804×** | -5.9 | 1e-07 | 25/44 (HT-29, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6915. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 336 | 0 | 23 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0696× (z -31.2) |
| [[SK-MEL-2 (line)]] | alt | 195 | 0 | 17 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.185× (z -14.1) |
| [[SW48 (line)]] | wt | 418 | 0 | 16 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -28.1) |
| [[HEC-1-A (line)]] | alt | 237 | 0 | 12 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.289× (z -21.6) |
| [[HT-29 (line)]] | alt | 90.7 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -23.5) |
| [[A-172 (line)]] | wt | 74.5 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -25.3) |
| [[A-427 (line)]] | wt | 92.3 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -24.3) |
| [[LS 180 (line)]] | wt | 96.6 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -19.3) |
| [[LoVo (line)]] | wt | 99.7 | 0 | 8 | — | [[Panobinostat (drug)]] 0.5 µM 0.221× (z -17.0) |
| [[RKO (line)]] | wt | 63.8 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -24.7) |
| [[SNU-1 (line)]] | wt | 93.4 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -16.7) |
| [[SW1417 (line)]] | alt | 329 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -17.2) |
| [[C-33 A (line)]] | alt | 82.3 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -17.5) |
| [[HepG2_C3A (line)]] | wt | 113 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -18.1) |
| [[Panc 03.27 (line)]] | alt | 144 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -15.7) |
| [[HS-578T (line)]] | alt | 40.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -10.9) |
| [[PANC-1 (line)]] | alt | 29.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -25.9) |
| [[A498 (line)]] | wt | 36.1 | 0 | 4 | — | [[Harringtonine (drug)]] 0.5 µM 0.275× (z -13.2) |
| [[COLO 205 (line)]] | alt | 69.2 | 1 (1 ⚠) | 3 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.27× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -14.7) |
| [[Hs 766T (line)]] | wt | 70.1 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -12.3) |
| [[KATO III (line)]] | alt | 75.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -13.4) |
| [[A549 (line)]] | wt | 27.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -15.9) |
| [[HOP62 (line)]] | alt | 40.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -14.2) |
| [[MIA PaCa-2 (line)]] | alt | 39.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -10.8) |
| [[BT-474 (line)]] | alt | 36.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 24.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -11.5) |
| [[SNU-423 (line)]] | alt | 49.8 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.312× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 33.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.278× (z -9.8) |
| [[C32 (line)]] | wt | 75.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.329× (z -9.1) |
| [[J82 (line)]] | alt | 29.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 54.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -15.7) |
| [[SW 1271 (line)]] | alt | 83.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0434× (z -12.9) |
| [[AN3 CA (line)]] | alt | 110 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 20.0 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.87 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6915), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA9-AS1]] | +0.66 | +0.68 / +0.71 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[ZNF704]] | +0.60 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ZNRF3]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[OSBPL10]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[CMTM7]] | +0.56 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[GMPS]] | +0.55 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[HADH]] | +0.54 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[FARP1]] | +0.54 | +0.61 / +0.45 | both halves | 3e-05 | same gene group |
| [[STRBP]] | +0.54 | +0.46 / +0.38 | both halves | 6e-05 |  |
| [[TMTC4]] | +0.54 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[RAPGEF5]] | +0.53 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[LRP6]] | +0.53 | +0.40 / +0.48 | both halves | 4e-05 |  |
| [[MSH2]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM149B1]] | -0.50 | -0.57 / -0.37 | both halves | 7e-05 |  |
| [[NIT1]] | -0.48 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[YJU2B]] | -0.47 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[IL32]] | -0.47 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[MAF]] | -0.47 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[PIGA]] | -0.46 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[OTUD7B]] | -0.46 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[ZNF160]] | -0.45 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[FAM220A]] | -0.45 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[TRAFD1]] | -0.44 | -0.52 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CMTM7]] | B | CMTM7 activity raises CTDSPL's level | lines that do not express CMTM7 (5) vs lines expressing it (45) | 2.74× lower at baseline in the lines without CMTM7 | 0.022 | ⚠ within organs, on part of the lines; also absent: EPB41L2, FAM3C2P, P3H1 |
| [[TOP2A]] | B | TOP2A activity raises CTDSPL's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[JAK1]], [[JAK3]] | B | JAK1, JAK3 activity lowers CTDSPL's level | compounds that target JAK1, JAK3: 2 of 2 raise it (Filgotinib, Tofacitinib) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |
| [[JAK2]] | B | JAK2 activity lowers CTDSPL's level | compounds that target JAK2: 2 of 3 raise it (Filgotinib, Tofacitinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[SRC]] | B | SRC activity lowers CTDSPL's level | compounds that target SRC: 2 of 3 raise it (NG25, Ponatinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[TGFBR3]] | B | TGFBR3 activity raises CTDSPL's level | lines that do not express TGFBR3 (6) vs lines expressing it (44) | 2.72× lower at baseline in the lines without TGFBR3 | 0.098 | ⚠ within organs, on part of the lines; also absent: LRP1, AMN; maybe low, not absent |
| [[ITGA9-AS1]] | C | ITGA9-AS1 activity raises CTDSPL's level | lines that do not express ITGA9-AS1 (6) vs lines expressing it (44) | 3.99× lower at baseline in the lines without ITGA9-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: CTDSPL, SLC43A2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CMTM7]] | B | CTDSPL activity raises CMTM7's level | lines that do not express CTDSPL (5) vs lines expressing it (45) | 3.48× lower at baseline in the lines without CTDSPL | 0.047 | ⚠ within organs, on part of the lines; also absent: ITGA9-AS1, SLC43A2, PLAAT3; maybe low, not absent |
| [[TGFBR3]] | B | CTDSPL activity raises TGFBR3's level | lines that do not express CTDSPL (5) vs lines expressing it (45) | 2.76× lower at baseline in the lines without CTDSPL | 0.086 | ⚠ within organs, on part of the lines; also absent: ITGA9-AS1, SLC43A2, PLAAT3; maybe low, not absent |
| [[ITGA9-AS1]] | C | CTDSPL activity raises ITGA9-AS1's level | lines that do not express CTDSPL (5) vs lines expressing it (45) | 3.74× lower at baseline in the lines without CTDSPL | 0.024 | ⚠ within organs, on part of the lines; also absent: ITGA9-AS1, SLC43A2, PLAAT3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.483). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.2, 39.4); signed map (11.0, -1.8). **Vector** length 111, 33.3% of its response variance represented; |z| ≥ 3 in 1,304 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +1.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.5 | -0.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +2.9 | -5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.7 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +0.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +2.2 | +4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +4.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.6 | -13.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.6 | -9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -18.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.9 | -17.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.8 | -7.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.3 | -1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | CTD small phosphatase like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:37,861,880-37,984,469 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HYA22, SCP3, PSR1, RBSP3; previously C3orf8 |
| Gene groups (HGNC) | CTD family phosphatases; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O15194](https://www.uniprot.org/uniprotkb/O15194) (CTD small phosphatase-like protein):

> Recruited by REST to neuronal genes that contain RE-1 elements, leading to neuronal gene silencing in non-neuronal cells (By similarity). Preferentially catalyzes the dephosphorylation of 'Ser-5' within the tandem 7 residue repeats in the C-terminal domain (CTD) of the largest RNA polymerase II subunit POLR2A. Negatively regulates RNA polymerase II transcription, possibly by controlling the transition from initiation/capping to processive transcript elongation.

**Summary**, from NCBI Gene [10217](https://www.ncbi.nlm.nih.gov/gene/10217):

> Predicted to enable RNA polymerase II CTD heptapeptide repeat phosphatase activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to act upstream of or within negative regulation of G1/S transition of mitotic cell cycle and negative regulation of protein phosphorylation. Located in extracellular exosome. Biomarker of lung non-small cell carcinoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16890](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16890) · Entrez [10217](https://www.ncbi.nlm.nih.gov/gene/10217) · UniProt [O15194](https://www.uniprot.org/uniprotkb/O15194) · Ensembl [ENSG00000144677](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144677)

## Data

Gene col 6915: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6915); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6915, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6915]; `tensor/DDL_lfc|DDL_z.npy` [6915]; `embed/gene_vectors.npy` [6915]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6915 or target_col == 6915). Every well: [[CTDSPL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTDSPL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
