---
symbol: "RRAGD"
type: "gene"
col: 359
ensembl_id: "ENSG00000025039"
name: "Ras related GTP binding D"
location: "6q15"
module: 45
arm: "+"
pooled_cpm: 19.3
n_lines_expressing: 36
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 14
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 14
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# RRAGD

*Ras related GTP binding D* — 6q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 1.77× (z +9.9, q 3e-20, up in 23 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.604× (z -8.7, q 3e-15, down in 20 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX2]] (+0.70, fdr 7e-06), [[FLVCR2]] (+0.64, fdr 8e-06), [[WDSUB1]] (+0.63, fdr 8e-06); moves opposite to [[DDX5]] (-0.59, fdr 1e-05), [[HNRNPAB]] (-0.59, fdr 1e-05), [[SLFNL1-AS1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 14 go from it, the strongest it → [[ENTREP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 359.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.77×** | +9.9 | 3e-20 | 23/34 (PANC-1, MIA PaCa-2, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **2.14×** | +9.3 | 4e-18 | 28/34 (NCI-H460, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.95×** | +8.2 | 6e-14 | 27/32 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.68×** | +6.4 | 3e-08 | 26/33 (LoVo, NCI-H2347, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.02×** | +4.5 | 9e-04 | 19/33 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.29×** | +4.3 | 0.001 | 14/34 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +4.3 | 0.001 | 14/32 (NCI-H2030, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.004 | 17/33 (PANC-1, SNU-423, …) | top dose only | plate-row cell shift |
| [[venetoclax (drug)]] 5 µM |  | **1.86×** | +4.0 | 0.004 | 13/32 (SK-MEL-2, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.011 | 16/32 (SHP-77, SW480, …) | top dose only |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.055 | 7/33 (NCI-H1792, PANC-1, …) | top dose only | plate-row cell shift |
| [[Terfenadine (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.055 | 11/34 (J82, A-172, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.055 | 10/33 (NCI-H460, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.071 | 4/32 (NCI-H460, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 359.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.604×** | -8.7 | 3e-15 | 20/32 (MIA PaCa-2, HCT15, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -7.1 | 3e-10 | 22/32 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.593×** | -6.1 | 2e-07 | 21/33 (SNU-423, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.604×** | -5.9 | 5e-07 | 20/31 (MIA PaCa-2, BT-474, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.655×** | -4.7 | 2e-04 | 16/27 (A-172, NCI-H661, …) | inconsistent across doses | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.766×** | -4.6 | 4e-04 | 16/34 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.687×** | -4.3 | 0.001 | 19/32 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.717×** | -4.0 | 0.004 | 15/33 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.732×** | -3.8 | 0.010 | 14/32 (NCI-H2030, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.734×** | -3.7 | 0.010 | 17/34 (MIA PaCa-2, SHP-77, …) | rises with dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.743×** | -3.6 | 0.016 | 15/32 (A-172, SHP-77, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.776×** | -3.1 | 0.099 | 8/34 (CFPAC-1, A498, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.777× | -3.0 | 0.10 | 12/34 (A-172, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 359. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 69.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -17.2) |
| [[MIA PaCa-2 (line)]] | alt | 53.6 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -11.8) |
| [[A-172 (line)]] | wt | 34.0 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 17.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.95× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.138× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 85.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0631× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 17.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 38.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 31.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -9.3) |
| [[SNU-423 (line)]] | alt | 52.6 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 15.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 6.65 | 0 | 1 | — | [[Simotinib (drug)]] 0.5 µM 0.124× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 36.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.2) |
| [[PANC-1 (line)]] | alt | 12.3 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.38× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 78.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.282× (z -8.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.53 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 20.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 359), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX2]] | +0.70 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[FLVCR2]] | +0.64 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[WDSUB1]] | +0.63 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[VPS37D]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 | pathway: Autophagy |
| [[THAP8]] | +0.62 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ADM]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[DUSP15]] | +0.61 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[ZNF292]] | +0.61 | +0.70 / +0.46 | both halves | 3e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[DIXDC1]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[WDFY1]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[CLN8-AS1]] | +0.60 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[VEGFB]] | +0.59 | +0.61 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX5]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[HNRNPAB]] | -0.59 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[KPNA4]] | -0.56 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[CPSF3]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[CTPS1]] | -0.52 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[GEN1]] | -0.52 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[ANKMY1]] | -0.52 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[TIMM23B-AGAP6]] | -0.52 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[ATR]] | -0.52 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[MSS51]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[XRCC5]] | -0.51 | -0.48 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RRAGD's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DUSP15]] | B | DUSP15 activity raises RRAGD's level | lines that do not express DUSP15 (15) vs lines expressing it (35) | 2.73× lower at baseline in the lines without DUSP15 | 0.017 | ⚠ within organs, on part of the lines; also absent: DLK2, ETNK2, C11orf96 |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENTREP1]] | B | RRAGD activity raises ENTREP1's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 2.73× lower at baseline in the lines without RRAGD | 0.006 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |
| [[STK32A]] | B | RRAGD activity raises STK32A's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 2.90× lower at baseline in the lines without RRAGD | 0.013 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |
| [[ZNF14]] | B | RRAGD activity raises ZNF14's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 2.26× lower at baseline in the lines without RRAGD | 0.025 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |
| [[DHRS13]] | B | RRAGD activity raises DHRS13's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 1.50× lower at baseline in the lines without RRAGD | 0.036 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |
| [[LINC00674]] | B | RRAGD activity raises LINC00674's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 1.43× lower at baseline in the lines without RRAGD | 0.046 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |
| [[ZNF540]] | B | RRAGD activity raises ZNF540's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 1.89× lower at baseline in the lines without RRAGD | 0.050 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |
| [[PMS2CL]] | B | RRAGD activity raises PMS2CL's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 1.31× lower at baseline in the lines without RRAGD | 0.055 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |
| [[HRK]] | B | RRAGD activity raises HRK's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 1.74× lower at baseline in the lines without RRAGD | 0.056 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |
| [[SNX30]] | B | RRAGD activity raises SNX30's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 1.18× lower at baseline in the lines without RRAGD | 0.061 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |
| [[STX7]] | B | RRAGD activity raises STX7's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 1.12× lower at baseline in the lines without RRAGD | 0.063 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |
| [[USP30]] | B | RRAGD activity raises USP30's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 1.25× lower at baseline in the lines without RRAGD | 0.076 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |
| [[TMEM38B]] | B | RRAGD activity raises TMEM38B's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 1.29× lower at baseline in the lines without RRAGD | 0.088 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.605). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (8.6, -10.2); signed map (-25.1, -7.7). **Vector** length 99.9, 29.7% of its response variance represented; |z| ≥ 3 in 688 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.5 | +9.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.7 | +8.2 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +5.3 | +9.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.6 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +1.2 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -3.5 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -6.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -4.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.0 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | Ras related GTP binding D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q15 — chr6:89,364,616-89,412,273 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP761H171, bA11D8.2.1 |
| Gene groups (HGNC) | Ras related GTP binding proteins |
| Hallmark sets | IL2_STAT5_SIGNALING, GLYCOLYSIS, HYPOXIA |
| Reactome | 15 pathways, smallest: mTORC1-mediated signalling; Energy dependent regulation of mTOR by LKB1-AMPK; MTOR signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQL2](https://www.uniprot.org/uniprotkb/Q9NQL2) (Ras-related GTP-binding protein D):

> Guanine nucleotide-binding protein that plays a crucial role in the cellular response to amino acid availability through regulation of the mTORC1 signaling cascade. Forms heterodimeric Rag complexes with RagA/RRAGA or RagB/RRAGB and cycles between an inactive GTP-bound and an active GDP-bound form: RagD/RRAGD is in its active form when GDP-bound RagD/RRAGD forms a complex with GTP-bound RagA/RRAGA (or RagB/RRAGB) and in an inactive form when GTP-bound RagD/RRAGD heterodimerizes with GDP-bound …

**Summary**, from NCBI Gene [58528](https://www.ncbi.nlm.nih.gov/gene/58528):

> RRAGD is a monomeric guanine nucleotide-binding protein, or G protein. By binding GTP or GDP, small G proteins act as molecular switches in numerous cell processes and signaling pathways.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:19903](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19903) · Entrez [58528](https://www.ncbi.nlm.nih.gov/gene/58528) · UniProt [Q9NQL2](https://www.uniprot.org/uniprotkb/Q9NQL2) · Ensembl [ENSG00000025039](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000025039)

## Data

Gene col 359: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 359); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 359, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 359]; `tensor/DDL_lfc|DDL_z.npy` [359]; `embed/gene_vectors.npy` [359]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 359 or target_col == 359). Every well: [[RRAGD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRAGD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
