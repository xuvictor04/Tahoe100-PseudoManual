---
symbol: "ITGB6"
type: "gene"
col: 3636
ensembl_id: "ENSG00000115221"
name: "integrin subunit beta 6"
location: "2q24.2"
module: 8
arm: "+"
pooled_cpm: 29.57
n_lines_expressing: 18
n_dd_up: 17
n_dd_down: 17
n_dd_up_clean: 12
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 132
direction_downstream: 171
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ITGB6

*integrin subunit beta 6* — 2q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.08× (z +17.4, q 0e+00, up in 5 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +10.6, q 4e-24, up in 3 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.528× (z -9.8, q 4e-20, down in 14 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM45B]] (+0.82, fdr 7e-06), [[MPZL2]] (+0.76, fdr 7e-06), [[CATSPERB]] (+0.75, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 132 arrows point to it, the strongest [[ELF3-AS1]] → it (grade B ⚠); 171 go from it, the strongest it → [[FAM83E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3636.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.08×** | +17.4 | 0e+00 | 5/16 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.91×** | +15.9 | 0e+00 | 3/14 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +11.3 | 3e-27 | 4/14 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +10.6 | 4e-24 | 3/16 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.84×** | +9.5 | 3e-19 | 1/16 (AsPC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.74×** | +6.1 | 9e-08 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.0 | 2e-07 | 0/17 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.43×** | +5.5 | 2e-06 | 0/16 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.5 | 4e-04 | 2/16 (AsPC-1, SW480) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.005 | 7/16 (AsPC-1, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.009 | 4/16 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.31×** | +3.7 | 0.009 | 5/16 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +3.5 | 0.017 | 0/15 | top dose only | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.033 | 1/16 (A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.047 | 1/16 (CFPAC-1) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.051 | 2/16 (CFPAC-1, A498) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.051 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.072 | 0/17 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3636.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.528×** | -9.8 | 4e-20 | 14/16 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.647×** | -6.7 | 6e-09 | 11/16 (Panc 03.27, NCI-H1573, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.712×** | -5.2 | 3e-05 | 7/16 (SW1417, Panc 03.27, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.752×** | -4.4 | 0.002 | 11/16 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.762×** | -4.2 | 0.003 | 7/16 (Panc 03.27, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.769×** | -4.0 | 0.005 | 15/16 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.771×** | -4.0 | 0.005 | 13/16 (LS 180, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.774×** | -3.9 | 0.006 | 7/16 (Panc 03.27, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.770×** | -3.9 | 0.007 | 13/16 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.780×** | -3.8 | 0.008 | 0/16 | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.631×** | -3.7 | 0.011 | 4/16 (NCI-H1573, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 0.5 µM |  | **0.730×** | -3.5 | 0.026 | 1/16 (CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.653×** | -3.4 | 0.026 | 9/16 (NCI-H2347, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.788×** | -3.4 | 0.028 | 0/16 | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.05 µM |  | **0.801×** | -3.1 | 0.063 | 0/16 | inconsistent across doses |  |
| [[Penfluridol (drug)]] 5 µM |  | **0.811×** | -3.1 | 0.070 | 4/16 (BT-474, A498, …) | top dose only |  |
| [[crizotinib (drug)]] 5 µM |  | **0.813×** | -3.1 | 0.073 | 3/16 (SW1417, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3636. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 193 | 0 | 21 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 182 | 0 | 10 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.202× (z -12.6) |
| [[HT-29 (line)]] | alt | 91.9 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -22.0) |
| [[LoVo (line)]] | wt | 52.3 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -15.6) |
| [[HEC-1-A (line)]] | alt | 171 | 0 | 5 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.245× (z -11.9) |
| [[KATO III (line)]] | alt | 57.8 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -14.8) |
| [[LS 180 (line)]] | wt | 65.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -13.6) |
| [[COLO 205 (line)]] | alt | 134 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -19.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -13.4) |
| [[NCI-H1573 (line)]] | alt | 45.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0664× (z -24.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0956× (z -15.2) |
| [[SW1417 (line)]] | alt | 57.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 49.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 80.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 7.85 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.168× (z -11.4) |
| [[A-172 (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.51 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3636), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM45B]] | +0.82 | +0.82 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[MPZL2]] | +0.76 | +0.77 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[CATSPERB]] | +0.75 | +0.74 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[TSPAN1]] | +0.75 | +0.82 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[SLC28A3]] | +0.75 | +0.70 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[ST14]] | +0.74 | +0.71 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[TMC5]] | +0.73 | +0.71 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ADGRF1]] | +0.73 | +0.70 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[CEACAM5]] | +0.73 | +0.72 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[TC2N]] | +0.71 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[ALOX5]] | +0.69 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.69 | +0.73 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*132 arrows, 132 of them with an alert ⚠; grade A 0, B 12, C 120. Shown: the 12 strongest; 120 more arrows (120 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises ITGB6's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 4.00× lower at baseline in the lines without ELF3-AS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[LGALS9]] | B | LGALS9 activity raises ITGB6's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 3.64× lower at baseline in the lines without LGALS9 | 0.034 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[INPP4B]] | B | INPP4B activity raises ITGB6's level | lines that do not express INPP4B (10) vs lines expressing it (40) | 2.28× lower at baseline in the lines without INPP4B | 0.035 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[TJP2]] | B | TJP2 activity raises ITGB6's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 3.69× lower at baseline in the lines without TJP2 | 0.038 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[SPATA6L]] | B | SPATA6L activity raises ITGB6's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 3.75× lower at baseline in the lines without SPATA6L | 0.042 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[SLC44A3]] | B | SLC44A3 activity raises ITGB6's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.53× lower at baseline in the lines without SLC44A3 | 0.049 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[SOX12]] | B | SOX12 activity lowers ITGB6's level | lines that do not express SOX12 (5) vs lines expressing it (45) | 14.56× higher at baseline in the lines without SOX12 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENAH, ACOT12, SSBP2; maybe low, not absent |
| [[STS]] | B | STS activity raises ITGB6's level | lines that do not express STS (11) vs lines expressing it (39) | 2.91× lower at baseline in the lines without STS | 0.055 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[PROM2]] | B | PROM2 activity raises ITGB6's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 3.03× lower at baseline in the lines without PROM2 | 0.070 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[LMO7]] | B | LMO7 activity raises ITGB6's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 3.53× lower at baseline in the lines without LMO7 | 0.071 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[MTUS1]] | B | MTUS1 activity raises ITGB6's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 3.09× lower at baseline in the lines without MTUS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[TOP2A]] | B | TOP2A activity lowers ITGB6's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*171 arrows, 171 of them with an alert ⚠; grade A 0, B 47, C 124. Shown: the 12 strongest; 159 more arrows (159 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83E]] | B | ITGB6 activity raises FAM83E's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 4.32× lower at baseline in the lines without ITGB6 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[ELF3-AS1]] | B | ITGB6 activity raises ELF3-AS1's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 4.15× lower at baseline in the lines without ITGB6 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[TJP2]] | B | ITGB6 activity raises TJP2's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 4.10× lower at baseline in the lines without ITGB6 | 7e-04 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[LMO7]] | B | ITGB6 activity raises LMO7's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 4.76× lower at baseline in the lines without ITGB6 | 8e-04 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[LGALS9]] | B | ITGB6 activity raises LGALS9's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 3.48× lower at baseline in the lines without ITGB6 | 8e-04 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[ELMO3]] | B | ITGB6 activity raises ELMO3's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 2.73× lower at baseline in the lines without ITGB6 | 0.001 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[SLC44A3]] | B | ITGB6 activity raises SLC44A3's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 3.36× lower at baseline in the lines without ITGB6 | 0.001 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[STS]] | B | ITGB6 activity raises STS's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 3.01× lower at baseline in the lines without ITGB6 | 0.002 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[USP6NL]] | B | ITGB6 activity raises USP6NL's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 2.04× lower at baseline in the lines without ITGB6 | 0.002 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[PROM2]] | B | ITGB6 activity raises PROM2's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 2.94× lower at baseline in the lines without ITGB6 | 0.003 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[TNFRSF21]] | B | ITGB6 activity raises TNFRSF21's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 4.13× lower at baseline in the lines without ITGB6 | 0.003 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[GAREM1]] | B | ITGB6 activity raises GAREM1's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 3.29× lower at baseline in the lines without ITGB6 | 0.004 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.7, 56.2); signed map (59.5, 7.3). **Vector** length 92.7, 40.4% of its response variance represented; |z| ≥ 3 in 543 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *O-linked glycosylation of mucins* (reactome, mean cos +0.50 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +15.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +17.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +10.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | +1.3 | +3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.2 | +3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +1.5 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -6.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -5.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit beta 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.2 — chr2:160,099,667-160,271,888 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Integrin beta subunits |
| Reactome | 8 pathways, smallest: Molecules associated with elastic fibres; Elastic fibre formation; TGF-beta receptor signaling activates SMADs |
| Matched by | ensembl_id |

**Function**, from UniProt [P18564](https://www.uniprot.org/uniprotkb/P18564) (Integrin beta-6):

> Integrin alpha-V:beta-6 (ITGAV:ITGB6) is a receptor for fibronectin and cytotactin. It recognizes the sequence R-G-D in its ligands. Internalization of integrin alpha-V/beta-6 via clathrin-mediated endocytosis promotes carcinoma cell invasion. ITGAV:ITGB6 acts as a receptor for fibrillin-1 (FBN1) and mediates R-G-D-dependent cell adhesion to FBN1. Integrin alpha-V:beta-6 (ITGAV:ITGB6) mediates R-G-D-dependent release of transforming growth factor beta-1 (TGF-beta-1) from regulatory …

**Summary**, from NCBI Gene [3694](https://www.ncbi.nlm.nih.gov/gene/3694):

> This gene encodes a protein that is a member of the integrin superfamily. Members of this family are adhesion receptors that function in signaling from the extracellular matrix to the cell. Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain. The encoded protein forms a dimer with an alpha v chain and this heterodimer can bind to ligands like fibronectin and transforming growth factor beta 1. Alternate splicing results in multiple transcript …

**Accessions** — [HGNC:6161](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6161) · Entrez [3694](https://www.ncbi.nlm.nih.gov/gene/3694) · UniProt [P18564](https://www.uniprot.org/uniprotkb/P18564) · Ensembl [ENSG00000115221](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115221)

## Data

Gene col 3636: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3636); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3636, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3636]; `tensor/DDL_lfc|DDL_z.npy` [3636]; `embed/gene_vectors.npy` [3636]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3636 or target_col == 3636). Every well: [[ITGB6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGB6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
