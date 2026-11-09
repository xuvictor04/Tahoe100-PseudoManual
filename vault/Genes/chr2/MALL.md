---
symbol: "MALL"
type: "gene"
col: 6843
ensembl_id: "ENSG00000144063"
name: "mal, T cell differentiation protein like"
location: "2q13"
module: 34
arm: "+"
pooled_cpm: 9.03
n_lines_expressing: 29
n_dd_up: 0
n_dd_down: 24
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 23
direction_downstream: 34
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# MALL

*mal, T cell differentiation protein like* — 2q13

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.219× (z -13.7, q 7e-40, down in 25 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATG16L1]] (+0.66, fdr 7e-06), [[ANO1]] (+0.64, fdr 1e-05), [[GJB3]] (+0.63, fdr 1e-05); moves opposite to [[ATP5MC2]] (-0.50, fdr 6e-05), [[RAB13]] (-0.49, fdr 4e-05), [[ZBTB20]] (-0.49, fdr 5e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[C6orf141]] → it (grade B ⚠); 34 go from it, the strongest it → [[ANXA11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6843.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.66× | +3.1 | 0.70 | 12/26 (SW480, HOP62, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 1.64× | +3.0 | 0.70 | 11/26 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6843.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.219×** | -13.7 | 7e-40 | 25/26 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.133×** | -12.9 | 2e-35 | 26/27 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.139×** | -12.6 | 6e-34 | 25/26 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.207×** | -10.0 | 2e-21 | 26/26 (HOP62, HT-29, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.271×** | -8.0 | 1e-13 | 23/26 (HOP62, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.461×** | -7.0 | 3e-10 | 23/26 (SNU-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.355×** | -6.6 | 3e-09 | 20/26 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.503×** | -4.6 | 3e-04 | 16/27 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.500×** | -4.4 | 6e-04 | 16/27 (NCI-H1792, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.525×** | -4.1 | 0.002 | 15/27 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.581×** | -4.1 | 0.002 | 19/26 (LoVo, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.550×** | -3.8 | 0.007 | 13/26 (SW 900, A-172, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.543×** | -3.8 | 0.007 | 15/27 (LoVo, Hs 766T, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.542×** | -3.8 | 0.007 | 15/26 (MIA PaCa-2, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.544×** | -3.7 | 0.007 | 16/26 (LS 180, HOP62, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.550×** | -3.7 | 0.009 | 16/26 (LoVo, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.667×** | -3.2 | 0.046 | 12/26 (LoVo, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.605×** | -3.1 | 0.061 | 14/26 (SNU-1, SW48, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6843. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 7.68 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0416× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 44.6 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.0297× (z -16.1) |
| [[CFPAC-1 (line)]] | alt | 24.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0892× (z -12.4) |
| [[HT-29 (line)]] | alt | 22.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0581× (z -10.8) |
| [[LoVo (line)]] | wt | 31.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -14.3) |
| [[SNU-1 (line)]] | wt | 24.0 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0721× (z -14.5) |
| [[A-172 (line)]] | wt | 18.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 20.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0271× (z -14.9) |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -10.2) |
| [[HCT15 (line)]] | alt | 18.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0861× (z -12.0) |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0749× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 18.6 | 0 | 2 | — | [[Trametinib (drug)]] 5 µM 0.0807× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 3.17 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0846× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 3.92 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.0546× (z -10.2) |
| [[LS 180 (line)]] | wt | 17.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0719× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 9.54 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0443× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 7.60 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -12.0) |
| [[PANC-1 (line)]] | alt | 7.46 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0517× (z -12.1) |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0623× (z -8.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW48 (line)]] | wt | 26.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0587× (z -9.7) |
| [[SW480 (line)]] | alt | 5.88 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.106× (z -9.9) |
| [[A-427 (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.741 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.763 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.868 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.949 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.829 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.810 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.902 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.727 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.877 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.758 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.774 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 10.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6843), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG16L1]] | +0.66 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ANO1]] | +0.64 | +0.68 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[GJB3]] | +0.63 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[HS3ST1]] | +0.63 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[ITGB4]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[SERPINB5]] | +0.62 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[FERMT1]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[TGFA]] | +0.61 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[PADI1]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[MPRIP]] | +0.60 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[EPHA2-AS1]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[TMC7]] | +0.58 | +0.60 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MC2]] | -0.50 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[RAB13]] | -0.49 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ZBTB20]] | -0.49 | -0.53 / -0.39 | both halves | 5e-05 | same gene group |
| [[MME-AS1]] | -0.48 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[NOP53]] | -0.48 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[NCOA1]] | -0.48 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[SUMO4]] | -0.47 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[NACA4P]] ⚠ | -0.47 | -0.34 / -0.49 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TTBK2]] | -0.47 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[SNHG32]] | -0.46 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[LACTB]] | -0.45 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[UBXN1]] | -0.45 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[KMT2A]] | -0.45 | -0.39 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 8, C 15. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C6orf141]] | B | C6orf141 activity raises MALL's level | lines that do not express C6orf141 (21) vs lines expressing it (29) | 2.55× lower at baseline in the lines without C6orf141 | 0.013 | ⚠ within organs, on part of the lines; also absent: ADAM8, ENSG00000251584, SAMD12-AS1 |
| [[RPH3AL]] | B | RPH3AL activity raises MALL's level | lines that do not express RPH3AL (10) vs lines expressing it (40) | 3.36× lower at baseline in the lines without RPH3AL | 0.066 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, PATJ; maybe low, not absent |
| [[SEMA3B]] | B | SEMA3B activity raises MALL's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.36× lower at baseline in the lines without SEMA3B | 0.082 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[DUSP4]] | B | DUSP4 activity raises MALL's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.32× lower at baseline in the lines without DUSP4 | 0.084 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[ABCC3]] | B | ABCC3 activity raises MALL's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.69× lower at baseline in the lines without ABCC3 | 0.090 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[EVA1A-AS]] | B | EVA1A-AS activity raises MALL's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 1.60× lower at baseline in the lines without EVA1A-AS | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[LEMD1]] | B | LEMD1 activity raises MALL's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 2.47× lower at baseline in the lines without LEMD1 | 0.097 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[PLEK2]] | B | PLEK2 activity raises MALL's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.34× lower at baseline in the lines without PLEK2 | 0.097 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[TINAGL1]] | C | TINAGL1 activity raises MALL's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 3.81× lower at baseline in the lines without TINAGL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19; co-absent with the target |
| [[LASTR]] | C | LASTR activity raises MALL's level | lines that do not express LASTR (22) vs lines expressing it (28) | 3.74× lower at baseline in the lines without LASTR | 0.003 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent; co-absent with the target |
| [[MYEOV]] | C | MYEOV activity raises MALL's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 3.60× lower at baseline in the lines without MYEOV | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2; co-absent with the target |
| [[HS3ST1]] | C | HS3ST1 activity raises MALL's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 4.16× lower at baseline in the lines without HS3ST1 | 0.011 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4; co-absent with the target |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 19, C 15. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA11]] | B | MALL activity raises ANXA11's level | lines that do not express MALL (21) vs lines expressing it (29) | 2.84× lower at baseline in the lines without MALL | 0.002 | ⚠ within organs, on part of the lines; also absent: SDR16C5, SPNS2, CLDN4 |
| [[KRT8]] | B | MALL activity raises KRT8's level | lines that do not express MALL (21) vs lines expressing it (29) | 2.91× lower at baseline in the lines without MALL | 0.004 | ⚠ within organs, on part of the lines; also absent: SDR16C5, SPNS2, CLDN4 |
| [[ABCC3]] | B | MALL activity raises ABCC3's level | lines that do not express MALL (21) vs lines expressing it (29) | 3.26× lower at baseline in the lines without MALL | 0.008 | ⚠ within organs, on part of the lines; also absent: SDR16C5, SPNS2, CLDN4 |
| [[DLG3]] | B | MALL activity raises DLG3's level | lines that do not express MALL (21) vs lines expressing it (29) | 2.63× lower at baseline in the lines without MALL | 0.014 | ⚠ within organs, on part of the lines; also absent: SDR16C5, SPNS2, CLDN4 |
| [[MYO18A]] | B | MALL activity raises MYO18A's level | lines that do not express MALL (21) vs lines expressing it (29) | 1.67× lower at baseline in the lines without MALL | 0.019 | ⚠ within organs, on part of the lines; also absent: SDR16C5, SPNS2, CLDN4 |
| [[DLG3]] | B | MALL activity strengthens DLG3's drug response | lines that do not express MALL (17) vs lines expressing it (25) | the lines without MALL respond 0.44× as strongly (z diff +2.95); strongest at Homoharringtonine 5 µM: 0.68x vs 0.30x (z diff +5.3) | 0.039 | ⚠ within organs, on part of the lines; also absent: SDR16C5, SPNS2, CLDN4; target measured in part of the lines; artifact flags |
| [[F2RL1]] | B | MALL activity raises F2RL1's level | lines that do not express MALL (21) vs lines expressing it (29) | 3.05× lower at baseline in the lines without MALL | 0.042 | ⚠ within organs, on part of the lines; also absent: SDR16C5, SPNS2, CLDN4 |
| [[SEMA3B]] | B | MALL activity raises SEMA3B's level | lines that do not express MALL (21) vs lines expressing it (29) | 2.14× lower at baseline in the lines without MALL | 0.048 | ⚠ within organs, on part of the lines; also absent: SDR16C5, SPNS2, CLDN4 |
| [[MET]] | B | MALL activity raises MET's level | lines that do not express MALL (21) vs lines expressing it (29) | 2.88× lower at baseline in the lines without MALL | 0.048 | ⚠ within organs, on part of the lines; also absent: SDR16C5, SPNS2, CLDN4 |
| [[ITGA6]] | B | MALL activity raises ITGA6's level | lines that do not express MALL (21) vs lines expressing it (29) | 2.63× lower at baseline in the lines without MALL | 0.049 | ⚠ within organs, on part of the lines; also absent: SDR16C5, SPNS2, CLDN4 |
| [[CD58]] | B | MALL activity raises CD58's level | lines that do not express MALL (21) vs lines expressing it (29) | 1.51× lower at baseline in the lines without MALL | 0.049 | ⚠ within organs, on part of the lines; also absent: SDR16C5, SPNS2, CLDN4 |
| cells under [[Vinblastine (sulfate) (drug)]] 0.5 µM | B | MALL activity raises the cells' numbers under Vinblastine (sulfate) 0.5 µM (protects the cells) | lines that do not express MALL (21) vs lines expressing it (27) | the lines without MALL: 0.81× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: SDR16C5, SPNS2, CLDN4 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.547). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.8, 52.7); signed map (2.5, 38.8). **Vector** length 77.7, 23.7% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.4 | +0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.4 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.8 | +0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.4 | +0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | -2.9 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -4.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.0 | -4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.8 | -2.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.8 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | mal, T cell differentiation protein like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q13 — chr2:110,083,870-110,116,022 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BENE |
| Gene groups (HGNC) | MARVEL domain containing; MicroRNA protein coding host genes |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

UniProt [Q13021](https://www.uniprot.org/uniprotkb/Q13021) carries no function annotation.

**Summary**, from NCBI Gene [7851](https://www.ncbi.nlm.nih.gov/gene/7851):

> This gene encodes an element of the machinery for raft-mediated trafficking in endothelial cells. The encoded protein, a member of the MAL proteolipid family, predominantly localizes in glycolipid- and cholesterol-enriched membrane (GEM) rafts. It interacts with caveolin-1. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6818](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6818) · Entrez [7851](https://www.ncbi.nlm.nih.gov/gene/7851) · UniProt [Q13021](https://www.uniprot.org/uniprotkb/Q13021) · Ensembl [ENSG00000144063](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144063)

## Data

Gene col 6843: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6843); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6843, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6843]; `tensor/DDL_lfc|DDL_z.npy` [6843]; `embed/gene_vectors.npy` [6843]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6843 or target_col == 6843). Every well: [[MALL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MALL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
