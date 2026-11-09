---
symbol: "HCP5"
type: "gene"
col: 13040
ensembl_id: "ENSG00000206337"
name: "HLA complex P5"
location: "6p21.33"
module: 70
arm: "+"
pooled_cpm: 8.47
n_lines_expressing: 26
n_dd_up: 31
n_dd_down: 9
n_dd_up_clean: 22
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 12
direction_downstream: 25
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# HCP5

*HLA complex P5* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.19× (z +26.5, q 0e+00, up in 24 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.348× (z -6.3, q 2e-07, down in 18 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HLA-F]] (+0.71, fdr 7e-06), [[LINC02068]] (+0.70, fdr 1e-05), [[PATL2]] (+0.69, fdr 7e-06); moves opposite to [[BICD2]] (-0.64, fdr 4e-05), [[HERC2P9]] (-0.59, fdr 2e-05), [[ANKRD27]] (-0.59, fdr 2e-04).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[GBP1]] → it (grade B ⚠); 25 go from it, the strongest it → [[TNK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13040.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.19×** | +26.5 | 0e+00 | 24/24 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.79×** | +25.3 | 0e+00 | 22/24 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.98×** | +15.1 | 0e+00 | 24/24 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.32×** | +13.6 | 9e-40 | 22/24 (A498, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.98×** | +12.4 | 2e-33 | 19/24 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.97×** | +10.9 | 1e-25 | 20/24 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +10.0 | 1e-21 | 15/22 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.43×** | +9.7 | 1e-20 | 16/21 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.33×** | +9.6 | 4e-20 | 19/24 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +8.3 | 6e-15 | 5/15 (LoVo, HOP62, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +8.0 | 7e-14 | 17/24 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.91×** | +7.4 | 8e-12 | 18/24 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.9 | 2e-10 | 13/24 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.82×** | +6.8 | 3e-10 | 12/24 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +6.3 | 1e-08 | 19/24 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.67×** | +5.9 | 2e-07 | 15/24 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.56×** | +5.1 | 1e-05 | 15/24 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +4.5 | 2e-04 | 10/24 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13040.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.348×** | -6.3 | 2e-07 | 18/20 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.694×** | -5.9 | 9e-07 | 17/24 (NCI-H2030, NCI-H460, …) | rises with dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.770×** | -4.2 | 0.004 | 13/24 (LoVo, A498, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **0.702×** | -4.1 | 0.007 | 16/24 (SW48, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.712×** | -3.9 | 0.011 | 11/23 (LoVo, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.802×** | -3.6 | 0.032 | 16/24 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | **0.749×** | -3.3 | 0.074 | 0/24 | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.753×** | -3.3 | 0.080 | 5/24 (COLO 205, A-172, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.757×** | -3.2 | 0.088 | 1/24 (NCI-H460) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.770× | -3.0 | 0.15 | 9/24 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13040. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.25 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +19.2) | — |
| [[HEC-1-A (line)]] | alt | 40.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +19.0) | — |
| [[J82 (line)]] | alt | 27.5 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.45× (z +18.0) | [[Auranofin (drug)]] 5 µM 0.263× (z -8.5) |
| [[KATO III (line)]] | alt | 29.5 | 3 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.94× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[LoVo (line)]] | wt | 13.7 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +12.4) | [[Belinostat (drug)]] 0.5 µM 0.223× (z -8.8) |
| [[A498 (line)]] | wt | 16.0 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +9.6) | [[Auranofin (drug)]] 5 µM 0.186× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 19.2 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.99× (z +14.8) | [[Auranofin (drug)]] 5 µM 0.210× (z -9.2) |
| [[COLO 205 (line)]] | alt | 54.0 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +12.0) | [[Auranofin (drug)]] 5 µM 0.0981× (z -13.5) |
| [[NCI-H2347 (line)]] | alt | 12.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +12.7) | — |
| [[SW 900 (line)]] | alt | 10.4 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +9.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0876× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 3.35 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 2.51 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.01× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 7.14 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.02× (z +12.2) | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0884× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 21.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.88× (z +13.1) | — |
| [[SNU-423 (line)]] | alt | 12.9 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 8.18× (z +9.8) | — |
| [[A-172 (line)]] | wt | 4.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 7.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 6.27 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0468× (z -11.8) |
| [[SW48 (line)]] | wt | 21.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +12.2) | — |
| [[A-427 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.793 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.704 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.710 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.873 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.810 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.901 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.681 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.793 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.957 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.861 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 13.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13040), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLA-F]] | +0.71 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[LINC02068]] | +0.70 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[PATL2]] | +0.69 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[NFKB2]] | +0.68 | +0.56 / +0.76 | both halves | 1e-05 |  |
| [[LINC02605]] | +0.68 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[CTSS]] | +0.68 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[HLA-H]] | +0.67 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[TRIM69]] | +0.67 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[HLA-A]] | +0.66 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[CXCL3]] | +0.65 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[HLA-B]] | +0.65 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[IRF1]] | +0.64 | +0.57 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BICD2]] | -0.64 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[HERC2P9]] | -0.59 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ANKRD27]] | -0.59 | -0.61 / -0.32 | both halves | 2e-04 |  |
| [[PWWP3A]] | -0.58 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[TYW1]] | -0.57 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[PSMD9]] | -0.57 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[VKORC1L1]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[PRKAR2A]] | -0.56 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[HERC2P2]] | -0.56 | -0.41 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP1]] | B | GBP1 activity raises HCP5's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.27× lower at baseline in the lines without GBP1 | 0.010 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[CXCL3]] | B | CXCL3 activity raises HCP5's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 2.73× lower at baseline in the lines without CXCL3 | 0.026 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[TOP2A]] | B | TOP2A activity lowers HCP5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CTSS]] | B | CTSS activity raises HCP5's level | lines that do not express CTSS (15) vs lines expressing it (35) | 2.36× lower at baseline in the lines without CTSS | 0.040 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[KMO]] | B | KMO activity raises HCP5's level | lines that do not express KMO (18) vs lines expressing it (32) | 1.47× lower at baseline in the lines without KMO | 0.051 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[HLA-F]] | B | HLA-F activity raises HCP5's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 1.89× lower at baseline in the lines without HLA-F | 0.054 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[C21orf91]] | B | C21orf91 activity raises HCP5's level | lines that do not express C21orf91 (5) vs lines expressing it (45) | 2.97× lower at baseline in the lines without C21orf91 | 0.076 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[SYNPO2]] | B | SYNPO2 activity raises HCP5's level | lines that do not express SYNPO2 (5) vs lines expressing it (45) | 3.09× lower at baseline in the lines without SYNPO2 | 0.093 | ⚠ within organs, on part of the lines; also absent: RIPOR3, PER3, TESK2; maybe low, not absent |
| [[RHOV]] | C | RHOV activity raises HCP5's level | lines that do not express RHOV (23) vs lines expressing it (27) | 3.09× lower at baseline in the lines without RHOV | 0.005 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6; co-absent with the target |
| [[CD74]] | C | CD74 activity raises HCP5's level | lines that do not express CD74 (31) vs lines expressing it (19) | 2.68× lower at baseline in the lines without CD74 | 0.007 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5; co-absent with the target |
| [[OVOL1]] | C | OVOL1 activity raises HCP5's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 3.06× lower at baseline in the lines without OVOL1 | 0.012 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[TNFSF14]] | C | TNFSF14 activity raises HCP5's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 2.37× lower at baseline in the lines without TNFSF14 | 0.060 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 22, C 3. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNK1]] | B | HCP5 activity raises TNK1's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 1.80× lower at baseline in the lines without HCP5 | 0.002 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[HLA-F]] | B | HCP5 activity raises HLA-F's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 2.39× lower at baseline in the lines without HCP5 | 0.010 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[PSMB8]] | B | HCP5 activity raises PSMB8's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 1.97× lower at baseline in the lines without HCP5 | 0.015 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[HLA-B]] | B | HCP5 activity raises HLA-B's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 2.12× lower at baseline in the lines without HCP5 | 0.021 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[STAP2]] | B | HCP5 activity raises STAP2's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 2.13× lower at baseline in the lines without HCP5 | 0.021 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[DIAPH2-AS1]] | B | HCP5 activity raises DIAPH2-AS1's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 1.64× lower at baseline in the lines without HCP5 | 0.032 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[LINC02068]] | B | HCP5 activity raises LINC02068's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 1.51× lower at baseline in the lines without HCP5 | 0.034 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[BHLHE40]] | B | HCP5 activity raises BHLHE40's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 1.44× lower at baseline in the lines without HCP5 | 0.037 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[NR1D1]] | B | HCP5 activity raises NR1D1's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 1.49× lower at baseline in the lines without HCP5 | 0.040 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[LINC02605]] | B | HCP5 activity strengthens LINC02605's drug response | lines that do not express HCP5 (16) vs lines expressing it (17) | the lines without HCP5 respond 0.78× as strongly (z diff +0.85); strongest at Harringtonine 0.5 µM: 2.84x vs 4.23x (z diff +1.7) | 0.042 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451; target measured in part of the lines; artifact flags |
| [[ETV7]] | B | HCP5 activity raises ETV7's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 1.82× lower at baseline in the lines without HCP5 | 0.043 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[ZNF341-AS1]] | B | HCP5 activity raises ZNF341-AS1's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 1.68× lower at baseline in the lines without HCP5 | 0.049 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.9, 6.0); signed map (41.9, 6.9). **Vector** length 76.5, 20.3% of its response variance represented; |z| ≥ 3 in 743 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antigen processing-Cross presentation* (reactome, mean cos +0.58 to 14); *Interferon gamma signaling* (reactome, mean cos +0.59 to 13); *Endosomal/Vacuolar pathway* (reactome, mean cos +0.65 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +26.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +25.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +13.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +9.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.5 | +10.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +6.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +2.3 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.5 | -3.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +0.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.3 | -3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -5.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.8 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | HLA complex P5 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p21.33 — chr6:31,463,170-31,478,936 (+) |
| Ensembl biotype | lncRNA |
| Also known as | D6S2650E, P5-1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

UniProt [Q6MZN7](https://www.uniprot.org/uniprotkb/Q6MZN7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:21659](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21659) · Entrez [10866](https://www.ncbi.nlm.nih.gov/gene/10866) · UniProt [Q6MZN7](https://www.uniprot.org/uniprotkb/Q6MZN7) · Ensembl [ENSG00000206337](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206337)

## Data

Gene col 13040: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13040); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13040, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13040]; `tensor/DDL_lfc|DDL_z.npy` [13040]; `embed/gene_vectors.npy` [13040]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13040 or target_col == 13040). Every well: [[HCP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HCP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
