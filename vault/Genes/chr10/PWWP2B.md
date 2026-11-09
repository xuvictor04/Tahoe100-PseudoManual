---
symbol: "PWWP2B"
type: "gene"
col: 10166
ensembl_id: "ENSG00000171813"
name: "PWWP domain containing 2B"
location: "10q26.3"
module: 20
arm: "-"
pooled_cpm: 5.27
n_lines_expressing: 47
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 33
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# PWWP2B

*PWWP domain containing 2B* — 10q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 2.23× (z +7.9, q 2e-12, up in 23 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.608× (z -7.4, q 8e-11, down in 22 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.110×, A-172 0.215×, HCT15 0.155×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (Panc 03.27 0.0556×, MIA PaCa-2 0.111×, HT-29 0.219×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HT-29 0.115×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC18]] (+0.65, fdr 1e-05), [[ZNF579]] (+0.64, fdr 7e-06), [[LRRC8E]] (+0.63, fdr 1e-05); moves opposite to [[TM9SF3]] (-0.56, fdr 1e-05), [[TMEM30A]] (-0.55, fdr 1e-05), [[TMBIM6]] (-0.53, fdr 2e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CBFA2T3]] → it (grade B ⚠); 33 go from it, the strongest it → cells under [[Imiquimod (maleate) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10166.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **2.23×** | +7.9 | 2e-12 | 23/40 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.03×** | +7.3 | 6e-11 | 26/43 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.89×** | +6.6 | 9e-09 | 22/43 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +5.4 | 8e-06 | 2/7 (CFPAC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.04×** | +5.3 | 1e-05 | 16/31 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.002 | 16/36 (HepG2/C3A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.2 | 0.002 | 8/26 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.8 | 0.008 | 4/35 (SW48, AN3 CA, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +3.8 | 0.008 | 6/24 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.010 | 18/41 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.014 | 13/37 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.014 | 7/32 (SW48, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.61×** | +3.5 | 0.017 | 4/28 (LS 180, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +3.5 | 0.019 | 8/44 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.5 | 0.019 | 4/26 (NCI-H1792, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.59×** | +3.4 | 0.021 | 3/41 (SW 900, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.58×** | +3.4 | 0.024 | 6/37 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.052 | 5/39 (AN3 CA, SW 900, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.061 | 4/45 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.069 | 4/44 (SW1417, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10166.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.110×, A-172 0.215×, HCT15 0.155×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (Panc 03.27 0.0556×, MIA PaCa-2 0.111×, HT-29 0.219×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HT-29 0.115×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.608×** | -7.4 | 8e-11 | 22/34 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.706×** | -3.7 | 0.072 | 13/42 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | 0.526× | -3.3 | 0.13 | 8/40 (LoVo, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.721× | -3.3 | 0.13 | 18/36 (Panc 03.27, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.555× | -3.1 | 0.24 | 9/36 (PANC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10166. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 20.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -14.8) |
| [[A-172 (line)]] | wt | 6.30 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -9.1) |
| [[HCT15 (line)]] | alt | 8.00 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 7.29 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0556× (z -10.9) |
| [[SW48 (line)]] | wt | 9.61 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0534× (z -10.1) ⚠ cell-cycle shift, explains ~66% of this change |
| [[A-427 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10166), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC18]] | +0.65 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ZNF579]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[LRRC8E]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[GFER]] | +0.61 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[SLC26A11]] | +0.60 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[GRHPR]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[GTF2IRD1]] | +0.58 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[CARMIL2]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[NAPRT]] | +0.57 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ETNK2]] | +0.56 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[CAMKK1]] | +0.56 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[KLF11]] | +0.55 | +0.54 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM9SF3]] | -0.56 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[TMEM30A]] | -0.55 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[TMBIM6]] | -0.53 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[ANTXR1]] | -0.52 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[RECQL]] | -0.51 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[AIDA]] | -0.50 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[PDIA3]] | -0.50 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ILF2]] | -0.50 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[ACTL6A]] | -0.49 | -0.48 / -0.43 | both halves | 3e-05 | pathway: ATP-dependent chromatin remodelers |
| [[CD164]] | -0.48 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[TMX1]] | -0.48 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[MLEC]] | -0.47 | -0.53 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CBFA2T3]] | B | CBFA2T3 activity raises PWWP2B's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 1.48× lower at baseline in the lines without CBFA2T3 | 0.050 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[MISP]] | B | MISP activity raises PWWP2B's level | lines that do not express MISP (23) vs lines expressing it (27) | 1.64× lower at baseline in the lines without MISP | 0.096 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 0, C 33. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Imiquimod (maleate) (drug)]] 0.5 µM | C | PWWP2B activity raises the cells' numbers under Imiquimod (maleate) 0.5 µM (protects the cells) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 0.60× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| cells under [[Ferulic acid (drug)]] 0.5 µM | C | PWWP2B activity raises the cells' numbers under Ferulic acid 0.5 µM (protects the cells) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 0.53× the cells of the other lines | 0.010 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| cells under [[Digitoxin (drug)]] 0.05 µM | C | PWWP2B activity raises the cells' numbers under Digitoxin 0.05 µM (protects the cells) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 0.43× the cells of the other lines | 0.018 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| cells under [[Pemetrexed (drug)]] 5 µM | C | PWWP2B activity raises the cells' numbers under Pemetrexed 5 µM (protects the cells) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 0.64× the cells of the other lines | 0.021 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| cells under [[Doxycycline (monohydrate) (drug)]] 0.5 µM | C | PWWP2B activity raises the cells' numbers under Doxycycline (monohydrate) 0.5 µM (protects the cells) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 0.63× the cells of the other lines | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| cells under [[Gallic acid (drug)]] 0.05 µM | C | PWWP2B activity raises the cells' numbers under Gallic acid 0.05 µM (protects the cells) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 0.58× the cells of the other lines | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| cells under [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM | C | PWWP2B activity raises the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.5 µM (protects the cells) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 0.68× the cells of the other lines | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| cells under [[Vortioxetine (drug)]] 5 µM | C | PWWP2B activity raises the cells' numbers under Vortioxetine 5 µM (protects the cells) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 0.69× the cells of the other lines | 0.033 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| cells under [[Citalopram (hydrobromide) (drug)]] 0.05 µM | C | PWWP2B activity lowers the cells' numbers under Citalopram (hydrobromide) 0.05 µM (makes them more sensitive) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 1.46× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| cells under [[Rucaparib (phosphate) (drug)]] 5 µM | C | PWWP2B activity lowers the cells' numbers under Rucaparib (phosphate) 5 µM (makes them more sensitive) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 1.48× the cells of the other lines | 0.035 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| cells under [[Menadione (drug)]] 0.5 µM | C | PWWP2B activity raises the cells' numbers under Menadione 0.5 µM (protects the cells) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 0.77× the cells of the other lines | 0.038 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| cells under [[Sulfatinib (drug)]] 0.5 µM | C | PWWP2B activity raises the cells' numbers under Sulfatinib 0.5 µM (protects the cells) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 0.72× the cells of the other lines | 0.039 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.398). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-46.5, 16.1); signed map (-0.6, -12.0). **Vector** length 66.8, 11.5% of its response variance represented; |z| ≥ 3 in 771 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +4.7 | +7.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.0 | +7.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +6.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +2.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +2.3 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.4 | -3.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.3 | -2.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.2 | -2.7 |
|  | [[Alpelisib (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | PWWP domain containing 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.3 — chr10:132,397,168-132,417,859 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA432J24.1, FLJ46823; previously PWWP2 |
| Gene groups (HGNC) | PWWP domain containing |
| Reactome | 5 pathways, smallest: NuRD complex assembly; CHD3, CHD4, CHD5 subfamily; CHD chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NUJ5](https://www.uniprot.org/uniprotkb/Q6NUJ5) (PWWP domain-containing protein 2B):

> Chromatin-binding protein that acts as an adapter between distinct nucleosome components (H3K36me3 or H2A.Z) and chromatin-modifying complexes, contributing to the regulation of the levels of histone acetylation at actively transcribed genes. Competes with CHD4 and MBD3 for interaction with MTA1 to form a NuRD subcomplex, preventing the formation of full NuRD complex (containing CHD4 and MBD3), leading to recruitment of HDACs to gene promoters resulting in turn in the deacetylation of nearby …

**Summary**, from NCBI Gene [170394](https://www.ncbi.nlm.nih.gov/gene/170394):

> Enables NuRD complex binding activity. Predicted to be involved in chromatin remodeling; positive regulation of transcription elongation by RNA polymerase II; and regulation of cold-induced thermogenesis. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25150](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25150) · Entrez [170394](https://www.ncbi.nlm.nih.gov/gene/170394) · UniProt [Q6NUJ5](https://www.uniprot.org/uniprotkb/Q6NUJ5) · Ensembl [ENSG00000171813](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171813)

## Data

Gene col 10166: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10166); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10166, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10166]; `tensor/DDL_lfc|DDL_z.npy` [10166]; `embed/gene_vectors.npy` [10166]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10166 or target_col == 10166). Every well: [[PWWP2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PWWP2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
