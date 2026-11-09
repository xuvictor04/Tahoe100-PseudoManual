---
symbol: "PTPN22"
type: "gene"
col: 5525
ensembl_id: "ENSG00000134242"
name: "protein tyrosine phosphatase non-receptor type 22"
location: "1p13.2"
module: 8
arm: "+"
pooled_cpm: 6.96
n_lines_expressing: 42
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 18
direction_downstream: 5
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PTPN22

*protein tyrosine phosphatase non-receptor type 22* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.44× (z +20.7, q 0e+00, up in 26 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.695× (z -4.3, q 0.008, down in 14 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCL2L15]] (+0.77, fdr 7e-06, ⚠ same locus), [[MUC20]] (+0.65, fdr 1e-05), [[SPATA6L]] (+0.65, fdr 1e-05), [[MGAM2]] (+0.63, fdr 3e-05); moves opposite to [[FAHD2CP]] (-0.50, fdr 2e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[KCNE3]] → it (grade B ⚠); 5 go from it, the strongest it → [[ADCY4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5525.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.44×** | +20.7 | 0e+00 | 26/32 (SW1417, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.95×** | +16.3 | 0e+00 | 24/34 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.55×** | +15.7 | 0e+00 | 31/37 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.97×** | +12.9 | 6e-36 | 27/35 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.05×** | +12.7 | 5e-35 | 5/10 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +9.1 | 6e-18 | 12/29 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +9.1 | 9e-18 | 7/23 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +8.1 | 4e-14 | 8/23 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.88×** | +7.5 | 5e-12 | 13/37 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.5 | 3e-09 | 7/37 (SW1417, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.61×** | +5.0 | 3e-05 | 1/14 (LoVo) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +4.8 | 6e-05 | 8/36 (LOX-IMVI, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.51×** | +4.7 | 1e-04 | 6/28 (HEC-1-A, SW1417, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.7 | 1e-04 | 3/26 (HEC-1-A, SW 900, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.46×** | +4.5 | 3e-04 | 12/36 (NCI-H1792, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +3.9 | 0.003 | 10/37 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.86×** | +3.8 | 0.004 | 2/33 (NCI-H1792, NCI-H2347) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.006 | 3/35 (LoVo, RPMI-7951, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.014 | 6/39 (COLO 205, HT-29, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +3.4 | 0.020 | 2/35 (A498, SK-MEL-2) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.67×** | +3.2 | 0.043 | 4/24 (LS 180, SW480, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.047 | 3/35 (A-172, COLO 205, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.055 | 3/35 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5525.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.695×** | -4.3 | 0.008 | 14/35 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.717×** | -3.8 | 0.028 | 11/33 (COLO 205, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.729×** | -3.8 | 0.028 | 13/36 (SW480, CFPAC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.732×** | -3.7 | 0.028 | 13/37 (KATO III, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | 0.768× | -3.2 | 0.18 | 11/32 (SW48, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Rosiglitazone (drug)]] 5 µM |  | 0.770× | -3.0 | 0.25 | 8/35 (SW 900, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5525. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 64.7 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0444× (z -27.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.146× (z -11.4) |
| [[KATO III (line)]] | alt | 13.0 | 0 | 6 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0364× (z -14.3) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0654× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 54.3 | 2 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.94× (z +11.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -10.0) |
| [[A498 (line)]] | wt | 3.82 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.80× (z +10.3) | — |
| [[HEC-1-A (line)]] | alt | 3.72 | 2 | 0 | [[Auranofin (drug)]] 5 µM 21.8× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 2.22 | 1 | 0 | [[Auranofin (drug)]] 5 µM 19.4× (z +10.0) | — |
| [[LoVo (line)]] | wt | 9.83 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.44× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 10.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.69× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 7.07 | 0 | 1 | — | [[Rapamycin (drug)]] 0.5 µM 0.0578× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 4.05 | 1 | 0 | [[Auranofin (drug)]] 5 µM 17.2× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 2.53 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0680× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 3.69 | 1 | 0 | [[Auranofin (drug)]] 5 µM 19.9× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 9.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +9.2) | — |
| [[SW48 (line)]] | wt | 14.4 | 0 | 1 | — | [[Ponatinib (drug)]] 0.5 µM 0.0562× (z -9.7) |
| [[A-172 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5525), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL2L15]] | +0.77 | +0.85 / +0.69 | both halves | 7e-06 | STRING 478; ⚠ same locus (5.1 kb, same strand: neighbours can correlate without regulation) |
| [[MUC20]] | +0.65 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[SPATA6L]] | +0.65 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[MGAM2]] | +0.63 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[IGFL2-AS1]] | +0.63 | +0.57 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[HNF1A-AS1]] | +0.63 | +0.74 / +0.45 | both halves | 3e-05 |  |
| [[RNF183]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[UNC5CL]] | +0.61 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[SMIM2-AS1]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[RAMP1]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ARSL]] | +0.60 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[MUC12]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[BCAR3-AS1]] | +0.60 | +0.67 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAHD2CP]] | -0.50 | -0.29 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 18, C 0. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNE3]] | B | KCNE3 activity raises PTPN22's level | lines that do not express KCNE3 (37) vs lines expressing it (13) | 2.93× lower at baseline in the lines without KCNE3 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SKAP1, SLC5A1, VWA2 |
| [[C9orf152]] | B | C9orf152 activity raises PTPN22's level | lines that do not express C9orf152 (32) vs lines expressing it (18) | 2.21× lower at baseline in the lines without C9orf152 | 0.013 | ⚠ within organs, on part of the lines; also absent: AGR3, MYO7B, KRT17; maybe low, not absent |
| [[UGT1A8]], [[UGT1A9]] | B | UGT1A8, UGT1A9 activity raises PTPN22's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 1.87× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.023 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent genes |
| [[TOP2A]] | B | TOP2A activity lowers PTPN22's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RNF183]] | B | RNF183 activity raises PTPN22's level | lines that do not express RNF183 (36) vs lines expressing it (14) | 2.29× lower at baseline in the lines without RNF183 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, LINC02964, VIL1 |
| [[AGR3]] | B | AGR3 activity raises PTPN22's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 2.61× lower at baseline in the lines without AGR3 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[TNFSF14]] | B | TNFSF14 activity raises PTPN22's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 1.11× lower at baseline in the lines without TNFSF14 | 0.036 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[PTPRB]] | B | PTPRB activity raises PTPN22's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 1.70× lower at baseline in the lines without PTPRB | 0.039 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[STEAP4]] | B | STEAP4 activity raises PTPN22's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.01× lower at baseline in the lines without STEAP4 | 0.065 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[LINC01559]] | B | LINC01559 activity raises PTPN22's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 2.40× lower at baseline in the lines without LINC01559 | 0.071 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17 |
| [[LINC02343]] | B | LINC02343 activity raises PTPN22's level | lines that do not express LINC02343 (7) vs lines expressing it (43) | 1.87× lower at baseline in the lines without LINC02343 | 0.072 | ⚠ within organs, on part of the lines; also absent: PRAF2; maybe low, not absent |
| [[GRHL2]] | B | GRHL2 activity raises PTPN22's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 2.19× lower at baseline in the lines without GRHL2 | 0.075 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY4]] | B | PTPN22 activity raises ADCY4's level | lines that do not express PTPN22 (8) vs lines expressing it (42) | 2.02× lower at baseline in the lines without PTPN22 | 0.058 | ⚠ within organs, on part of the lines; also absent: PTPRE; maybe low, not absent |
| [[LINC01811]] | B | PTPN22 activity weakens LINC01811's drug response | lines that do not express PTPN22 (6) vs lines expressing it (32) | the lines without PTPN22 respond 1.70× as strongly (z diff -1.85); strongest at Doxorubicin (hydrochloride) 5 µM: 6.56x vs 2.94x (z diff -2.7) | 0.058 | ⚠ within organs, on part of the lines; also absent: PTPRE; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CNGA1]] | B | PTPN22 activity raises CNGA1's level | lines that do not express PTPN22 (8) vs lines expressing it (42) | 1.76× lower at baseline in the lines without PTPN22 | 0.062 | ⚠ within organs, on part of the lines; also absent: PTPRE; maybe low, not absent |
| [[MROH7]] | B | PTPN22 activity raises MROH7's level | lines that do not express PTPN22 (8) vs lines expressing it (42) | 2.18× lower at baseline in the lines without PTPN22 | 0.081 | ⚠ within organs, on part of the lines; also absent: PTPRE; maybe low, not absent |
| [[PTPRB]] | B | PTPN22 activity raises PTPRB's level | lines that do not express PTPN22 (8) vs lines expressing it (42) | 3.25× lower at baseline in the lines without PTPN22 | 0.091 | ⚠ within organs, on part of the lines; also absent: PTPRE; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.649). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.3, 52.8); signed map (60.0, 0.8). **Vector** length 81.2, 16.3% of its response variance represented; |z| ≥ 3 in 1,084 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.7 | +15.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.4 | +12.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +16.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +20.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.3 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.5 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -1.7 | +2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.5 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase non-receptor type 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:113,813,811-113,871,753 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Lyp, Lyp1, Lyp2; previously PTPN8 |
| Gene groups (HGNC) | Protein tyrosine phosphatases non-receptor type |
| Reactome | 4 pathways, smallest: Translocation of ZAP-70 to Immunological synapse; Phosphorylation of CD3 and TCR zeta chains; TCR signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2R2](https://www.uniprot.org/uniprotkb/Q9Y2R2) (Tyrosine-protein phosphatase non-receptor type 22):

> Acts as a negative regulator of T-cell receptor (TCR) signaling by direct dephosphorylation of the Src family kinases LCK and FYN, ITAMs of the TCRz/CD3 complex, as well as ZAP70, VAV, VCP and other key signaling molecules. Associates with and probably dephosphorylates CBL. Dephosphorylates LCK at its activating 'Tyr-394' residue. Dephosphorylates ZAP70 at its activating 'Tyr-493' residue. Dephosphorylates the immune system activator SKAP2. Positively regulates toll-like receptor (TLR)-induced …

**Summary**, from NCBI Gene [26191](https://www.ncbi.nlm.nih.gov/gene/26191):

> This gene encodes of member of the non-receptor class 4 subfamily of the protein-tyrosine phosphatase family. The encoded protein is a lymphoid-specific intracellular phosphatase that associates with the molecular adapter protein CBL and may be involved in regulating CBL function in the T-cell receptor signaling pathway. Mutations in this gene may be associated with a range of autoimmune disorders including Type 1 Diabetes, rheumatoid arthritis, systemic lupus erythematosus and Graves' disease. …

**Accessions** — [HGNC:9652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9652) · Entrez [26191](https://www.ncbi.nlm.nih.gov/gene/26191) · UniProt [Q9Y2R2](https://www.uniprot.org/uniprotkb/Q9Y2R2) · Ensembl [ENSG00000134242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134242)

## Data

Gene col 5525: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5525); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5525, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5525]; `tensor/DDL_lfc|DDL_z.npy` [5525]; `embed/gene_vectors.npy` [5525]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5525 or target_col == 5525). Every well: [[PTPN22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPN22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
