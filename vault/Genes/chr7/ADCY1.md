---
symbol: "ADCY1"
type: "gene"
col: 8998
ensembl_id: "ENSG00000164742"
name: "adenylate cyclase 1"
location: "7p12.3"
module: 82
arm: "+"
pooled_cpm: 10.65
n_lines_expressing: 26
n_dd_up: 18
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# ADCY1

*adenylate cyclase 1* — 7p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.12× (z +15.4, q 0e+00, up in 9 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.12× (z +14.4, q 2e-44, up in 16 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.578× (z -10.5, q 5e-23, down in 18 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RET]] (+0.70, fdr 7e-06), [[VASH1]] (+0.65, fdr 7e-06), [[SEPTIN3]] (+0.64, fdr 7e-06); moves opposite to [[FCF1]] (-0.52, fdr 5e-05), [[DNAL4]] (-0.49, fdr 4e-05), [[KRBOX4]] (-0.47, fdr 3e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[NUP210]] → it (grade B ⚠); 8 go from it, the strongest it → [[LINC00937]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8998.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.12×** | +15.4 | 0e+00 | 9/16 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.12×** | +14.4 | 2e-44 | 16/22 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.85×** | +13.6 | 4e-40 | 10/15 (C32, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.98×** | +9.3 | 3e-18 | 13/21 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.00×** | +8.7 | 5e-16 | 5/15 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.55×** | +8.4 | 3e-15 | 2/22 (NCI-H460, A549) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.53×** | +5.8 | 7e-07 | 11/22 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.46×** | +5.1 | 2e-05 | 12/23 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.40×** | +4.4 | 7e-04 | 5/20 (NCI-H460, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **1.38×** | +4.2 | 0.001 | 4/19 (A549, NCI-H2347, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.31×** | +3.7 | 0.012 | 6/22 (A549, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +3.6 | 0.015 | 1/19 (SNU-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.015 | 5/22 (SK-MEL-2, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.30×** | +3.5 | 0.016 | 12/23 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.025 | 4/21 (SK-MEL-2, C32, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.062 | 0/19 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8998.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.578×** | -10.5 | 5e-23 | 18/21 (SK-MEL-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.531×** | -8.2 | 5e-14 | 18/23 (A-427, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.612×** | -6.6 | 6e-09 | 18/21 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.616×** | -6.6 | 8e-09 | 10/23 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.480×** | -4.9 | 1e-04 | 15/22 (C-33 A, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.729×** | -4.0 | 0.005 | 15/21 (NCI-H23, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.572×** | -3.7 | 0.015 | 11/20 (A-427, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.762×** | -3.7 | 0.017 | 6/21 (RPMI-7951, SK-MEL-2, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.774×** | -3.5 | 0.033 | 8/23 (A-172, BT-474, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.775×** | -3.3 | 0.052 | 1/22 (A-172) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.786×** | -3.1 | 0.096 | 7/24 (A-172, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | **0.782×** | -3.1 | 0.098 | 2/22 (NCI-H2030, CHP-212) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.854× | -3.0 | 0.11 | 8/23 (AN3 CA, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8998. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.56 | 7 (5 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 5.60× (z +12.1) | — |
| [[NCI-H23 (line)]] | alt | 25.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -19.9) |
| [[A-172 (line)]] | wt | 18.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -13.8) |
| [[A-427 (line)]] | wt | 58.2 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.151× (z -17.7) |
| [[C-33 A (line)]] | alt | 63.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0804× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0808× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 78.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0424× (z -36.7) |
| [[LoVo (line)]] | wt | 17.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -19.2) |
| [[RPMI-7951 (line)]] | alt | 18.9 | 0 | 2 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.115× (z -10.9) |
| [[SNU-1 (line)]] | wt | 19.4 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0943× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.110× (z -9.2) |
| [[A549 (line)]] | wt | 15.9 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 8.46× (z +10.7) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[AN3 CA (line)]] | alt | 35.3 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0708× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -13.7) |
| [[NCI-H1792 (line)]] | alt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 8.23 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.59× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 81.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.272× (z -11.8) |
| [[SW 900 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -13.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 0.874 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.887 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.880 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.30 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8998), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RET]] | +0.70 | +0.64 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[VASH1]] | +0.65 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[SEPTIN3]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[DPYSL5]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[JAKMIP1]] | +0.64 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[GNAO1]] | +0.64 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[DGCR5]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[MED12L]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[SLC6A17]] | +0.60 | +0.45 / +0.72 | both halves | 3e-05 |  |
| [[LINC00937]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[LMX1B]] | +0.59 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[KCNQ2]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 | pathway: Neuronal System |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCF1]] | -0.52 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[DNAL4]] | -0.49 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[KRBOX4]] | -0.47 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[ZNF226]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ZMAT2]] | -0.46 | -0.30 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUP210]] | B | NUP210 activity raises ADCY1's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 2.13× lower at baseline in the lines without NUP210 | 0.044 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A |
| [[EBF4]] | B | EBF4 activity raises ADCY1's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 3.08× lower at baseline in the lines without EBF4 | 0.069 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[ANKRD6]] | C | ANKRD6 activity raises ADCY1's level | lines that do not express ANKRD6 (16) vs lines expressing it (34) | 4.04× lower at baseline in the lines without ANKRD6 | 0.056 | ⚠ within organs, on part of the lines; also absent: MAP9, RIMKLB, TUB; co-absent with the target |
| [[RET]] | C | RET activity raises ADCY1's level | lines that do not express RET (28) vs lines expressing it (22) | 3.52× lower at baseline in the lines without RET | 0.064 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1; co-absent with the target |
| [[DOCK3]] | C | DOCK3 activity raises ADCY1's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 4.09× lower at baseline in the lines without DOCK3 | 0.094 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1; co-absent with the target |
| [[CHD5]] | C | CHD5 activity raises ADCY1's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 2.69× lower at baseline in the lines without CHD5 | 0.097 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00937]] | B | ADCY1 activity raises LINC00937's level | lines that do not express ADCY1 (24) vs lines expressing it (26) | 1.88× lower at baseline in the lines without ADCY1 | 0.032 | ⚠ within organs, on part of the lines; also absent: LHX2, GAS7, GHR |
| [[RASGEF1C]] | B | ADCY1 activity raises RASGEF1C's level | lines that do not express ADCY1 (24) vs lines expressing it (26) | 2.54× lower at baseline in the lines without ADCY1 | 0.038 | ⚠ within organs, on part of the lines; also absent: LHX2, GAS7, GHR |
| [[ADGRL1]] | B | ADCY1 activity raises ADGRL1's level | lines that do not express ADCY1 (24) vs lines expressing it (26) | 2.05× lower at baseline in the lines without ADCY1 | 0.079 | ⚠ within organs, on part of the lines; also absent: LHX2, GAS7, GHR |
| [[PARD6G]] | B | ADCY1 activity raises PARD6G's level | lines that do not express ADCY1 (24) vs lines expressing it (26) | 2.29× lower at baseline in the lines without ADCY1 | 0.092 | ⚠ within organs, on part of the lines; also absent: LHX2, GAS7, GHR |
| [[ANKRD6]] | C | ADCY1 activity raises ANKRD6's level | lines that do not express ADCY1 (24) vs lines expressing it (26) | 3.39× lower at baseline in the lines without ADCY1 | 0.031 | ⚠ within organs, on part of the lines; also absent: LHX2, GAS7, GHR; co-absent with the target |
| [[LHX2]] | C | ADCY1 activity raises LHX2's level | lines that do not express ADCY1 (24) vs lines expressing it (26) | 3.11× lower at baseline in the lines without ADCY1 | 0.043 | ⚠ within organs, on part of the lines; also absent: LHX2, GAS7, GHR; co-absent with the target |
| [[KIF26A]] | C | ADCY1 activity raises KIF26A's level | lines that do not express ADCY1 (24) vs lines expressing it (26) | 2.56× lower at baseline in the lines without ADCY1 | 0.071 | ⚠ within organs, on part of the lines; also absent: LHX2, GAS7, GHR; co-absent with the target |
| [[MED12L]] | C | ADCY1 activity raises MED12L's level | lines that do not express ADCY1 (24) vs lines expressing it (26) | 3.90× lower at baseline in the lines without ADCY1 | 0.078 | ⚠ within organs, on part of the lines; also absent: LHX2, GAS7, GHR; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.690). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.9, 38.8); signed map (26.9, 27.3). **Vector** length 61.7, 14.9% of its response variance represented; |z| ≥ 3 in 615 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +14.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +15.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.4 | +8.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +0.9 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.1 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.6 | -6.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -3.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.1 | -0.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | adenylate cyclase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p12.3 — chr7:45,574,140-45,723,116 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AC1; previously DFNB44 |
| Gene groups (HGNC) | Adenylate cyclases |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 45 pathways, smallest: Adenylate cyclase activating pathway; CREB1 phosphorylation through the activation of Adenylate Cyclase; Adenylate cyclase inhibitory pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08828](https://www.uniprot.org/uniprotkb/Q08828) (Adenylate cyclase type 1):

> Catalyzes the formation of the signaling molecule cAMP in response to G protein signaling. Mediates responses to increased cellular Ca(2+)/calmodulin levels (By similarity). May be involved in regulatory processes in the central nervous system. May play a role in memory and learning. Plays a role in the regulation of the circadian rhythm of daytime contrast sensitivity probably by modulating the rhythmic synthesis of cyclic AMP in the retina (By similarity).

**Summary**, from NCBI Gene [107](https://www.ncbi.nlm.nih.gov/gene/107):

> This gene encodes a member of the of adenylate cyclase gene family that is primarily expressed in the brain. This protein is regulated by calcium/calmodulin concentration and may be involved in brain development. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:232](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:232) · Entrez [107](https://www.ncbi.nlm.nih.gov/gene/107) · UniProt [Q08828](https://www.uniprot.org/uniprotkb/Q08828) · Ensembl [ENSG00000164742](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164742)

## Data

Gene col 8998: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8998); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8998, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8998]; `tensor/DDL_lfc|DDL_z.npy` [8998]; `embed/gene_vectors.npy` [8998]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8998 or target_col == 8998). Every well: [[ADCY1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADCY1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
