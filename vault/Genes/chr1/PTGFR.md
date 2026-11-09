---
symbol: "PTGFR"
type: "gene"
col: 4336
ensembl_id: "ENSG00000122420"
name: "prostaglandin F receptor"
location: "1p31.1"
module: 13
arm: "+"
pooled_cpm: 8.3
n_lines_expressing: 22
n_dd_up: 18
n_dd_down: 11
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 39
direction_downstream: 57
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# PTGFR

*prostaglandin F receptor* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.60× (z +23.3, q 0e+00, up in 8 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.636× (z -5.8, q 3e-06, down in 14 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LOX]] (+0.76, fdr 7e-06), [[CA12]] (+0.71, fdr 7e-06), [[CARMN]] (+0.67, fdr 7e-06); moves opposite to [[PATJ]] (-0.49, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 39 arrows point to it, the strongest [[PATJ]] → it (grade B ⚠); 57 go from it, the strongest it → [[GPR176]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4336.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.60×** | +23.3 | 0e+00 | 8/16 (LOX-IMVI, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.21×** | +14.4 | 1e-44 | 13/19 (LOX-IMVI, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.74×** | +13.0 | 4e-36 | 0/15 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.96×** | +12.9 | 6e-36 | 1/12 (SW 900) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +10.7 | 1e-24 | 1/12 (NCI-H2030) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +8.7 | 3e-16 | 4/19 (LOX-IMVI, NCI-H2030, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +8.4 | 4e-15 | 2/17 (LOX-IMVI, NCI-H2030) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.83×** | +7.8 | 5e-13 | 11/18 (CFPAC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.7 | 2e-04 | 1/14 (SW 900) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.59×** | +4.3 | 0.001 | 0/13 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +4.2 | 0.002 | 0/11 | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.017 | 4/18 (LS 180, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.021 | 6/19 (SW 900, HOP62, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.030 | 7/17 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.040 | 4/19 (H4, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.071 | 2/19 (H4, hTERT-HPNE) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.085 | 1/14 (A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4336.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.636×** | -5.8 | 3e-06 | 14/19 (H4, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.675×** | -5.0 | 1e-04 | 10/19 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.681×** | -4.9 | 1e-04 | 11/19 (SW 900, H4, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.705×** | -4.5 | 0.001 | 12/19 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.720×** | -4.2 | 0.003 | 13/19 (H4, HS-578T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.730×** | -4.0 | 0.005 | 9/19 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.725×** | -3.9 | 0.008 | 9/17 (A-172, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.754×** | -3.6 | 0.020 | 10/19 (HOP62, SW 900, …) | all doses, stronger at high dose |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | **0.746×** | -3.5 | 0.031 | 0/19 | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.779×** | -3.2 | 0.079 | 2/19 (H4, HS-578T) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.776×** | -3.1 | 0.091 | 1/19 (Hs 766T) | top dose only | plate-row cell shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 0.791× | -3.0 | 0.12 | 10/19 (NCI-H1792, A-172, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4336. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 34.4 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.219× (z -10.1) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.377× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 83.8 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.263× (z -12.3) |
| [[RPMI-7951 (line)]] | alt | 85.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.3) |
| [[J82 (line)]] | alt | 8.90 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0556× (z -14.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 26.6 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0446× (z -17.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 7.78 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 29.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -10.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 6.58 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0450× (z -8.9) |
| [[HOP62 (line)]] | alt | 7.79 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.110× (z -9.9) ⚠ cell-cycle shift, explains ~23% of this change |
| [[LOX-IMVI (line)]] | wt | 7.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 8.28 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0849× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 0.562 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.985 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.873 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.908 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.778 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.775 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.751 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.770 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.860 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.699 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4336), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LOX]] | +0.76 | +0.76 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[CA12]] | +0.71 | +0.67 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[CARMN]] | +0.67 | +0.58 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[ARHGEF6]] | +0.67 | +0.69 / +0.57 | both halves | 9e-06 | **novel candidate** |
| [[OR9Q1]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[PRR16]] | +0.64 | +0.53 / +0.72 | both halves | 1e-05 | **novel candidate** |
| [[GPR173]] | +0.64 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[FBN1]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[ADAMTS2]] | +0.62 | +0.65 / +0.58 | both halves | 8e-06 | **novel candidate** |
| [[DAB2]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[SLC14A2]] | +0.62 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[COL5A1]] | +0.62 | +0.71 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATJ]] | -0.49 | -0.49 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 2, C 37. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PATJ]] | B | PATJ activity lowers PTGFR's level | lines that do not express PATJ (9) vs lines expressing it (41) | 4.57× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[PAPSS2]] | B | PAPSS2 activity raises PTGFR's level | lines that do not express PAPSS2 (15) vs lines expressing it (35) | 2.57× lower at baseline in the lines without PAPSS2 | 0.060 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, A4GALT, NT5E |
| [[LINC01411]] | C | LINC01411 activity raises PTGFR's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 8.20× lower at baseline in the lines without LINC01411 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[LOX]] | C | LOX activity raises PTGFR's level | lines that do not express LOX (31) vs lines expressing it (19) | 5.45× lower at baseline in the lines without LOX | 0.005 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411; co-absent with the target |
| [[EDNRA]] | C | EDNRA activity raises PTGFR's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 4.96× lower at baseline in the lines without EDNRA | 0.007 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12; co-absent with the target |
| [[ADAM12]] | C | ADAM12 activity raises PTGFR's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 5.32× lower at baseline in the lines without ADAM12 | 0.008 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises PTGFR's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 4.76× lower at baseline in the lines without COL5A1 | 0.008 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[WNT5A]] | C | WNT5A activity raises PTGFR's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 4.80× lower at baseline in the lines without WNT5A | 0.012 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[CA12]] | C | CA12 activity raises PTGFR's level | lines that do not express CA12 (29) vs lines expressing it (21) | 3.52× lower at baseline in the lines without CA12 | 0.014 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises PTGFR's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 4.91× lower at baseline in the lines without PAPPA | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises PTGFR's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 6.22× lower at baseline in the lines without APCDD1L | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[STAC]] | C | STAC activity raises PTGFR's level | lines that do not express STAC (25) vs lines expressing it (25) | 3.75× lower at baseline in the lines without STAC | 0.016 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11; co-absent with the target |

### Downstream of this gene

*57 arrows, 57 of them with an alert ⚠; grade A 0, B 11, C 46. Shown: the 12 strongest; 45 more arrows (45 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR176]] | B | PTGFR activity strengthens GPR176's drug response | lines that do not express PTGFR (11) vs lines expressing it (19) | the lines without PTGFR respond 0.32× as strongly (z diff +3.12); strongest at Panobinostat 0.5 µM: 1.15x vs 0.51x (z diff +6.2) | 0.009 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX; target measured in part of the lines; artifact flags |
| [[LINC01500]] | B | PTGFR activity raises LINC01500's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 1.91× lower at baseline in the lines without PTGFR | 0.032 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX |
| [[LTBP1]] | B | PTGFR activity raises LTBP1's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 2.30× lower at baseline in the lines without PTGFR | 0.041 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX |
| [[GSDME]] | B | PTGFR activity raises GSDME's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 3.46× lower at baseline in the lines without PTGFR | 0.057 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX |
| [[LPAR1]] | B | PTGFR activity raises LPAR1's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 3.45× lower at baseline in the lines without PTGFR | 0.060 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX |
| [[C1R]] | B | PTGFR activity strengthens C1R's drug response | lines that do not express PTGFR (11) vs lines expressing it (17) | the lines without PTGFR respond 0.49× as strongly (z diff +2.40); rises at some drug-doses, falls at others (32% from rises): Harringtonine 5 µM: 0.81x vs 0.25x (z diff +5.1); Homoharringtonine 5 µM: 0.43x vs 0.17x (z diff +5.0); Dinaciclib 0.5 µM: 0.69x vs 1.25x (z diff +2.6) | 0.063 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[LINC01119]] | B | PTGFR activity raises LINC01119's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 1.94× lower at baseline in the lines without PTGFR | 0.066 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX |
| [[PAPSS2]] | B | PTGFR activity raises PAPSS2's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 2.84× lower at baseline in the lines without PTGFR | 0.074 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX |
| [[IPO9-AS1]] | B | PTGFR activity raises IPO9-AS1's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 1.57× lower at baseline in the lines without PTGFR | 0.093 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX |
| [[RUNX2]] | B | PTGFR activity raises RUNX2's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 2.37× lower at baseline in the lines without PTGFR | 0.094 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX |
| [[LINC02882]] | B | PTGFR activity raises LINC02882's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 2.89× lower at baseline in the lines without PTGFR | 0.095 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX |
| [[GPR176]] | C | PTGFR activity raises GPR176's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 7.14× lower at baseline in the lines without PTGFR | 0.001 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.559). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.3, 20.5); signed map (27.7, 45.6). **Vector** length 68.5, 21.1% of its response variance represented; |z| ≥ 3 in 582 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +14.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +23.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +12.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.2 | +3.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.0 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -3.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | prostaglandin F receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:78,303,884-78,540,701 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FP |
| Gene groups (HGNC) | Prostaglandin receptors |
| Hallmark sets | KRAS_SIGNALING_DN, UV_RESPONSE_DN |
| Reactome | 6 pathways, smallest: Eicosanoid ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P43088](https://www.uniprot.org/uniprotkb/P43088) (Prostaglandin F2-alpha receptor):

> Receptor for prostaglandin F2-alpha (PGF2-alpha). The activity of this receptor is mediated by G proteins which activate a phosphatidylinositol-calcium second messenger system. Initiates luteolysis in the corpus luteum (By similarity). Isoforms 2 to 7 do not bind PGF2-alpha but are proposed to modulate signaling by participating in variant receptor complexes; heterodimers between isoform 1 and isoform 5 are proposed to be a receptor for prostamides including the synthetic analog bimatoprost.

**Summary**, from NCBI Gene [5737](https://www.ncbi.nlm.nih.gov/gene/5737):

> The protein encoded by this gene is member of the G-protein coupled receptor family. This protein is a receptor for prostaglandin F2-alpha (PGF2-alpha), which is known to be a potent luteolytic agent, and may also be involved in modulating intraocular pressure and smooth muscle contraction in uterus. Knockout studies in mice suggest that the interaction of PGF2-alpha with this receptor may initiate parturition in ovarian luteal cells and thus induce luteolysis. Two transcript variants encoding …

**Accessions** — [HGNC:9600](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9600) · Entrez [5737](https://www.ncbi.nlm.nih.gov/gene/5737) · UniProt [P43088](https://www.uniprot.org/uniprotkb/P43088) · Ensembl [ENSG00000122420](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122420)

## Data

Gene col 4336: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4336); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4336, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4336]; `tensor/DDL_lfc|DDL_z.npy` [4336]; `embed/gene_vectors.npy` [4336]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4336 or target_col == 4336). Every well: [[PTGFR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTGFR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
