---
symbol: "EPHA1-AS1"
type: "gene"
col: 13695
ensembl_id: "ENSG00000229153"
name: "EPHA1 antisense RNA 1"
location: "7q35"
module: 53
arm: "+"
pooled_cpm: 4.09
n_lines_expressing: 44
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 20
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# EPHA1-AS1

*EPHA1 antisense RNA 1* — 7q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.24× (z +18.8, q 0e+00, up in 28 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Neratinib (maleate) (drug)]] 5 µM: 0.706× (z -4.6, q 0.003, down in 12 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CATSPERD]] (+0.79, fdr 7e-06), [[NUP210L]] (+0.77, fdr 7e-06), [[PPP1R36]] (+0.74, fdr 1e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 20 go from it, the strongest it → [[LHX4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13695.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.24×** | +18.8 | 0e+00 | 28/30 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **5.87×** | +16.3 | 0e+00 | 30/33 (HEC-1-A, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.92×** | +14.0 | 5e-42 | 24/31 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.89×** | +8.3 | 1e-14 | 25/36 (A498, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +7.9 | 2e-13 | 5/15 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +7.7 | 1e-12 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +6.6 | 4e-09 | 1/6 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.00×** | +6.4 | 1e-08 | 14/33 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +6.0 | 1e-07 | 12/30 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +5.1 | 2e-05 | 11/31 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.8 | 8e-05 | 7/36 (SW1417, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +4.8 | 9e-05 | 10/38 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.67×** | +4.7 | 1e-04 | 3/5 (A498, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +4.6 | 2e-04 | 8/26 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Belzutifan (drug)]] 5 µM |  | **2.51×** | +4.4 | 4e-04 | 3/18 (A498, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.41×** | +4.2 | 8e-04 | 3/27 (HOP62, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.50×** | +3.3 | 0.026 | 3/22 (NCI-H1792, RPMI-7951, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +3.1 | 0.067 | 12/38 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.87×** | +3.0 | 0.074 | 3/27 (BT-474, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13695.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.706×** | -4.6 | 0.003 | 12/39 (A498, BT-474, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.460×** | -3.8 | 0.049 | 5/24 (LoVo, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.687×** | -3.5 | 0.095 | 1/39 (hTERT-HPNE) | two highest doses |  |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | 0.702× | -3.3 | 0.14 | 4/31 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.706× | -3.2 | 0.14 | 13/37 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.716× | -3.1 | 0.18 | 8/40 (BT-474, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Carbamazepine (drug)]] 0.5 µM |  | 0.722× | -3.0 | 0.20 | 9/33 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13695. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.46 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +15.2) | — |
| [[HEC-1-A (line)]] | alt | 3.61 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.88× (z +10.6) | — |
| [[SW480 (line)]] | alt | 1.68 | 2 | 0 | [[Auranofin (drug)]] 5 µM 21.4× (z +9.8) | — |
| [[A498 (line)]] | wt | 2.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +9.9) | — |
| [[BT-474 (line)]] | alt | 6.67 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0506× (z -8.6) ⚠ cell-cycle shift, explains ~9% of this change |
| [[C32 (line)]] | wt | 2.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.7× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 2.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +10.9) | — |
| [[LS 180 (line)]] | wt | 3.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.42× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 8.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 5.09 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0836× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 4.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.9× (z +11.5) | — |
| [[SW1417 (line)]] | alt | 2.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +8.5) | — |
| [[A-172 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.899 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.987 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.830 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.954 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13695), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CATSPERD]] | +0.79 | +0.71 / +0.81 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.77 | +0.67 / +0.79 | both halves | 7e-06 |  |
| [[PPP1R36]] | +0.74 | +0.57 / +0.78 | both halves | 1e-05 |  |
| [[KIF17]] | +0.73 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[LINC00393]] | +0.72 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[FER1L6]] | +0.72 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[ELAVL3]] | +0.71 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[SH2D4B]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.71 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[IL12RB2]] | +0.71 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[GRAMD2A]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[SEMA4A]] | +0.70 | +0.76 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EPHA1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TNNT2]] | B | TNNT2 activity raises EPHA1-AS1's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 1.82× lower at baseline in the lines without TNNT2 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[KRT86]] | B | KRT86 activity raises EPHA1-AS1's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 1.75× lower at baseline in the lines without KRT86 | 0.030 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[FAM3B]] | B | FAM3B activity raises EPHA1-AS1's level | lines that do not express FAM3B (12) vs lines expressing it (38) | 1.58× lower at baseline in the lines without FAM3B | 0.032 | ⚠ within organs, on part of the lines; also absent: TXNIP, CADPS2, PLAC4; maybe low, not absent |
| [[FBXW10B]] | B | FBXW10B activity raises EPHA1-AS1's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 1.82× lower at baseline in the lines without FBXW10B | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[LMO7DN]] | B | LMO7DN activity raises EPHA1-AS1's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.61× lower at baseline in the lines without LMO7DN | 0.080 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 20, C 0. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LHX4]] | B | EPHA1-AS1 activity lowers LHX4's level | lines that do not express EPHA1-AS1 (6) vs lines expressing it (44) | 1.56× higher at baseline in the lines without EPHA1-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| [[LNP1]] | B | EPHA1-AS1 activity lowers LNP1's level | lines that do not express EPHA1-AS1 (6) vs lines expressing it (44) | 1.85× higher at baseline in the lines without EPHA1-AS1 | 0.015 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| [[AXDND1]] | B | EPHA1-AS1 activity lowers AXDND1's level | lines that do not express EPHA1-AS1 (6) vs lines expressing it (44) | 2.22× higher at baseline in the lines without EPHA1-AS1 | 0.016 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| [[PEBP4]] | B | EPHA1-AS1 activity raises PEBP4's level | lines that do not express EPHA1-AS1 (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without EPHA1-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| cells under [[Homoharringtonine (drug)]] 5 µM | B | EPHA1-AS1 activity raises the cells' numbers under Homoharringtonine 5 µM (protects the cells) | lines that do not express EPHA1-AS1 (6) vs lines expressing it (42) | the lines without EPHA1-AS1: 0.32× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| [[KRT86]] | B | EPHA1-AS1 activity raises KRT86's level | lines that do not express EPHA1-AS1 (6) vs lines expressing it (44) | 3.19× lower at baseline in the lines without EPHA1-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| cells under [[Epirubicin (hydrochloride) (drug)]] 5 µM | B | EPHA1-AS1 activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express EPHA1-AS1 (6) vs lines expressing it (42) | the lines without EPHA1-AS1: 0.48× the cells of the other lines | 0.048 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| [[CELF5]] | B | EPHA1-AS1 activity lowers CELF5's level | lines that do not express EPHA1-AS1 (6) vs lines expressing it (44) | 1.34× higher at baseline in the lines without EPHA1-AS1 | 0.056 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| cells under [[Idarubicin (hydrochloride) (drug)]] 5 µM | B | EPHA1-AS1 activity raises the cells' numbers under Idarubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express EPHA1-AS1 (6) vs lines expressing it (42) | the lines without EPHA1-AS1: 0.51× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| cells under [[Homoharringtonine (drug)]] 0.5 µM | B | EPHA1-AS1 activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express EPHA1-AS1 (6) vs lines expressing it (42) | the lines without EPHA1-AS1: 0.40× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| cells under [[4EGI-1 (drug)]] 5 µM | B | EPHA1-AS1 activity lowers the cells' numbers under 4EGI-1 5 µM (makes them more sensitive) | lines that do not express EPHA1-AS1 (6) vs lines expressing it (42) | the lines without EPHA1-AS1: 1.35× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| [[UCKL1-AS1]] | B | EPHA1-AS1 activity raises UCKL1-AS1's level | lines that do not express EPHA1-AS1 (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without EPHA1-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.819). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.6, -14.6); signed map (20.9, 12.4). **Vector** length 61.3, 10.2% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.1 | +16.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +14.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +18.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +4.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | -1.8 |
| fall | [[Radotinib (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[NG25 (drug)]] 5 µM |  | -1.7 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -2.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | EPHA1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q35 — chr7:143,407,784-143,523,449 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27799) · Entrez [285965](https://www.ncbi.nlm.nih.gov/gene/285965) · Ensembl [ENSG00000229153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229153)

## Data

Gene col 13695: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13695); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13695, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13695]; `tensor/DDL_lfc|DDL_z.npy` [13695]; `embed/gene_vectors.npy` [13695]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13695 or target_col == 13695). Every well: [[EPHA1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHA1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
