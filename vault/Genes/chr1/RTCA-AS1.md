---
symbol: "RTCA-AS1"
type: "gene"
col: 13409
ensembl_id: "ENSG00000224616"
name: "RTCA antisense RNA 1"
location: "1p21.2"
module: 35
arm: "+"
pooled_cpm: 2.97
n_lines_expressing: 49
n_dd_up: 36
n_dd_down: 16
n_dd_up_clean: 27
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# RTCA-AS1

*RTCA antisense RNA 1* — 1p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.22× (z +27.1, q 0e+00, up in 36 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.541× (z -5.6, q 1e-05, down in 21 of 45 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.588× (z -4.9, q 3e-04, down in 19 of 40 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRIG2-DT]] (+0.71, fdr 7e-06), [[CDNF]] (+0.70, fdr 7e-06), [[GEMIN7-AS1]] (+0.68, fdr 7e-06); moves opposite to [[SMARCA4]] (-0.58, fdr 3e-05), [[AFG3L2]] (-0.56, fdr 4e-04), [[EEFSEC]] (-0.55, fdr 1e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13409.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.22×** | +27.1 | 0e+00 | 36/36 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.93×** | +14.0 | 7e-42 | 26/28 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.42×** | +10.7 | 1e-24 | 24/33 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.20×** | +10.1 | 8e-22 | 26/43 (NCI-H460, KATO III, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **2.93×** | +9.8 | 2e-20 | 34/44 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.69×** | +8.3 | 9e-15 | 0/3 | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.48×** | +8.3 | 1e-14 | 30/42 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.89×** | +8.2 | 2e-14 | 27/42 (HEC-1-A, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.45×** | +8.1 | 2e-14 | 11/17 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **2.36×** | +7.5 | 4e-12 | 10/17 (NCI-H1573, HS-578T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.08×** | +6.6 | 2e-09 | 14/39 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.09×** | +6.6 | 2e-09 | 20/44 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.95×** | +6.1 | 5e-08 | 16/43 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +6.0 | 9e-08 | 1/1 (A498) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.8 | 2e-07 | 11/44 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.78×** | +5.2 | 6e-06 | 16/45 (KATO III, C-33 A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +4.3 | 4e-04 | 10/40 (LoVo, HS-578T, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.61×** | +4.3 | 5e-04 | 8/40 (NCI-H23, C-33 A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.40×** | +4.1 | 0.001 | 13/43 (SW480, Hs 766T, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **2.27×** | +3.9 | 0.003 | 2/41 (A-172, A498) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13409.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.541×** | -5.6 | 1e-05 | 21/45 (KATO III, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.588×** | -4.9 | 3e-04 | 19/40 (LoVo, COLO 205, …) | two highest doses | cell-cycle shift (explains ~18% here); position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.592×** | -4.8 | 3e-04 | 15/43 (SK-MEL-2, RKO, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.603×** | -4.7 | 5e-04 | 16/40 (C-33 A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.717×** | -4.3 | 0.002 | 14/42 (HT-29, A-427, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.410×** | -4.3 | 0.002 | 14/39 (LS 180, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.636×** | -4.2 | 0.002 | 14/29 (NCI-H23, NCI-H1573, …) | two highest doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.641×** | -4.1 | 0.003 | 15/45 (NCI-H23, SW 900, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.426×** | -4.1 | 0.003 | 13/30 (NCI-H1573, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.661×** | -3.7 | 0.013 | 12/41 (NCI-H2347, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.673×** | -3.6 | 0.017 | 9/45 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.684×** | -3.5 | 0.022 | 8/45 (AN3 CA, LoVo, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.499×** | -3.3 | 0.037 | 3/30 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.510×** | -3.2 | 0.050 | 8/30 (LoVo, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.707×** | -3.2 | 0.052 | 10/36 (NCI-H460, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.68 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13409. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 4.53 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +14.4) | — |
| [[C-33 A (line)]] | alt | 11.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +9.2) | [[Captopril (drug)]] 0.5 µM 0.0549× (z -11.4) |
| [[HT-29 (line)]] | alt | 4.11 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +11.3) | [[Asciminib (drug)]] 0.05 µM 0.0526× (z -9.7) |
| [[LoVo (line)]] | wt | 2.62 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.6× (z +12.4) | [[Digitoxin (drug)]] 0.5 µM 0.0663× (z -9.1) |
| [[LS 180 (line)]] | wt | 5.42 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.7× (z +14.1) | [[Nimesulide (drug)]] 5 µM 0.0815× (z -8.9) ⚠ toxic; unreliable plate only |
| [[NCI-H460 (line)]] | wt | 2.69 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +13.5) | — |
| [[A-172 (line)]] | wt | 2.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.6× (z +10.2) | — |
| [[A498 (line)]] | wt | 3.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.33× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 2.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.23× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 5.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +14.8) | — |
| [[HOP62 (line)]] | alt | 1.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 2.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.07× (z +8.7) | — |
| [[J82 (line)]] | alt | 1.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +8.5) | — |
| [[KATO III (line)]] | alt | 2.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.92× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 5.37 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.09× (z +9.2) ⚠ position not correctable | — |
| [[Panc 03.27 (line)]] | alt | 2.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.72× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 1.86 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0495× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13409), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRIG2-DT]] | +0.71 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[CDNF]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[GEMIN7-AS1]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 | same gene group |
| [[C2CD5-AS1]] | +0.65 | +0.53 / +0.58 | both halves | 1e-05 | same gene group |
| [[PAXBP1-AS1]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 | same gene group |
| [[HSPE1-MOB4]] | +0.63 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[HNRNPK-AS1]] | +0.63 | +0.51 / +0.33 | both halves | 1e-04 | same gene group |
| [[GAS2]] | +0.62 | +0.65 / +0.39 | both halves | 6e-05 |  |
| [[KCTD21-AS1]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 | same gene group |
| [[CCNO-DT]] | +0.61 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[MKLN1-AS]] | +0.61 | +0.58 / +0.51 | both halves | 1e-05 | same gene group |
| [[UPK2]] | +0.60 | +0.60 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCA4]] | -0.58 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[AFG3L2]] | -0.56 | -0.24 / -0.46 | both halves | 4e-04 |  |
| [[EEFSEC]] | -0.55 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[MIS18A]] | -0.54 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[NF2]] | -0.52 | -0.39 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RTCA-AS1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (8.8, 26.3); signed map (34.4, -2.5). **Vector** length 54.1, 7.61% of its response variance represented; |z| ≥ 3 in 1,088 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +27.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.6 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +8.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +5.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -4.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.0 | +6.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.7 | +3.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.6 | -4.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -4.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.3 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.2 | -3.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | RTCA antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p21.2 — chr1:100,251,528-100,266,182 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50573](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50573) · Entrez [100506007](https://www.ncbi.nlm.nih.gov/gene/100506007) · Ensembl [ENSG00000224616](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224616)

## Data

Gene col 13409: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13409); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13409, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13409]; `tensor/DDL_lfc|DDL_z.npy` [13409]; `embed/gene_vectors.npy` [13409]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13409 or target_col == 13409). Every well: [[RTCA-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTCA-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
