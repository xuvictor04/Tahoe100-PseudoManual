---
symbol: "COL17A1"
type: "gene"
col: 799
ensembl_id: "ENSG00000065618"
name: "collagen type XVII alpha 1 chain"
location: "10q25.1"
module: 73
arm: "+"
pooled_cpm: 36.96
n_lines_expressing: 16
n_dd_up: 20
n_dd_down: 15
n_dd_up_clean: 9
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 52
direction_downstream: 76
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# COL17A1

*collagen type XVII alpha 1 chain* — 10q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.34× (z +20.6, q 0e+00, up in 11 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +10.1, q 7e-22, up in 1 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.557× (z -7.2, q 4e-10, down in 13 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INPP1]] (+0.66, fdr 1e-05), [[EHF]] (+0.66, fdr 2e-05), [[SPON1]] (+0.65, fdr 7e-06); moves opposite to [[YIPF1]] (-0.46, fdr 4e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 52 arrows point to it, the strongest [[PCDH11X]] → it (grade B ⚠); 76 go from it, the strongest it → [[LMO7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 799.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.34×** | +20.6 | 0e+00 | 11/13 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.06×** | +16.6 | 0e+00 | 10/13 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.01×** | +12.6 | 7e-34 | 9/13 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.04×** | +12.4 | 2e-33 | 9/14 (COLO 205, NCI-H2347, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +10.1 | 7e-22 | 1/14 (NCI-H2347) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.8 | 7e-13 | 7/14 (MIA PaCa-2, LS 180, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.87×** | +6.7 | 1e-09 | 7/9 (NCI-H2347, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +6.7 | 1e-09 | 6/14 (NCI-H2347, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +6.2 | 3e-08 | 3/14 (NCI-H2347, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.57×** | +5.6 | 1e-06 | 6/14 (COLO 205, SW1417, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **1.43×** | +4.4 | 5e-04 | 2/14 (NCI-H2347, SW1417) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.40×** | +4.1 | 0.002 | 0/14 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.39×** | +4.1 | 0.002 | 6/14 (COLO 205, SW1417, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.39×** | +3.9 | 0.003 | 2/14 (SW48, SW1417) | top dose only |  |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.042 | 0/14 | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.050 | 2/14 (LS 180, SW48) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.071 | 5/14 (COLO 205, LS 180, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.41×** | +3.0 | 0.075 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.087 | 0/14 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 799.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.557×** | -7.2 | 4e-10 | 13/14 (LoVo, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.586×** | -6.6 | 2e-08 | 13/14 (LoVo, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.607×** | -5.7 | 3e-06 | 6/14 (MIA PaCa-2, LS 180, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.676×** | -4.8 | 2e-04 | 12/14 (LoVo, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.763×** | -4.6 | 6e-04 | 4/14 (Panc 03.27, LS 180, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.700×** | -4.4 | 0.001 | 8/14 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.701×** | -4.3 | 0.001 | 12/14 (LoVo, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.695×** | -4.1 | 0.003 | 0/14 | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.721×** | -4.0 | 0.004 | 7/14 (LoVo, HT-29, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.725×** | -3.9 | 0.005 | 12/14 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.726×** | -3.9 | 0.005 | 0/14 | two highest doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.707×** | -3.9 | 0.005 | 7/14 (Panc 03.27, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.774×** | -3.1 | 0.078 | 2/14 (KATO III, COLO 205) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.778×** | -3.1 | 0.090 | 10/14 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Encorafenib (drug)]] 5 µM |  | **0.621×** | -3.0 | 0.097 | 1/14 (LoVo) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 799. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 94.3 | 1 (1 ⚠) | 12 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +8.9) ⚠ cell-cycle shift, explains ~40% of this change | [[Panobinostat (drug)]] 5 µM 0.0932× (z -18.3) |
| [[Hs 766T (line)]] | wt | 377 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.201× (z -14.0) |
| [[AsPC-1 (line)]] | alt | 378 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.9) ⚠ cell-cycle shift, explains ~40% of this change | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -13.2) |
| [[KATO III (line)]] | alt | 88.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.260× (z -10.1) |
| [[LS 180 (line)]] | wt | 97.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 47.2 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +14.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 24.8 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 42.4× (z +24.1) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[Panc 03.27 (line)]] | alt | 96.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 82.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -14.5) |
| [[SW1417 (line)]] | alt | 56.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 42.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 33.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.249× (z -12.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 118 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0572× (z -10.3) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 4.31 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.91 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.65 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.10 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.25 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.82 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.00 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.64 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.98 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.74 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.07 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.72 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.98 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 799), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP1]] | +0.66 | +0.54 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[EHF]] | +0.66 | +0.72 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[SPON1]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[CTSE]] | +0.65 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[SULF2]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[MUC2]] | +0.64 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[C4BPB]] | +0.63 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[CEACAM6]] | +0.62 | +0.55 / +0.74 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[HTR1D]] | +0.62 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[MUC17]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[LAD1]] | +0.61 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[ACSL5]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIPF1]] | -0.46 | -0.41 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 3, C 49. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDH11X]] | B | PCDH11X activity raises COL17A1's level | lines that do not express PCDH11X (15) vs lines expressing it (35) | 3.32× lower at baseline in the lines without PCDH11X | 0.016 | ⚠ within organs, on part of the lines; also absent: XDH, CRYBG2, SPATA6L; maybe low, not absent |
| [[SEPTIN9-DT]] | B | SEPTIN9-DT activity raises COL17A1's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 3.38× lower at baseline in the lines without SEPTIN9-DT | 0.074 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[RIN2]] | B | RIN2 activity raises COL17A1's level | lines that do not express RIN2 (9) vs lines expressing it (41) | 2.23× lower at baseline in the lines without RIN2 | 0.077 | ⚠ within organs, on part of the lines; also absent: ANTXR2; maybe low, not absent |
| [[SERPINB5]] | C | SERPINB5 activity raises COL17A1's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 11.56× lower at baseline in the lines without SERPINB5 | 5e-05 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; co-absent with the target |
| [[FGFBP1]] | C | FGFBP1 activity raises COL17A1's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 11.35× lower at baseline in the lines without FGFBP1 | 9e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5; co-absent with the target |
| [[KLK10]] | C | KLK10 activity raises COL17A1's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 9.74× lower at baseline in the lines without KLK10 | 3e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6; co-absent with the target |
| [[CEACAM6]] | C | CEACAM6 activity raises COL17A1's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 9.36× lower at baseline in the lines without CEACAM6 | 6e-04 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; co-absent with the target |
| [[EHF]] | C | EHF activity raises COL17A1's level | lines that do not express EHF (27) vs lines expressing it (23) | 6.80× lower at baseline in the lines without EHF | 0.001 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3; co-absent with the target |
| [[CYP3A5]] | C | CYP3A5 activity raises COL17A1's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 5.25× lower at baseline in the lines without CYP3A5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A; co-absent with the target |
| [[TSPAN1]] | C | TSPAN1 activity raises COL17A1's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 6.27× lower at baseline in the lines without TSPAN1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6; co-absent with the target |
| [[TSPAN8]] | C | TSPAN8 activity raises COL17A1's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 6.70× lower at baseline in the lines without TSPAN8 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17; co-absent with the target |
| [[ITGB4]] | C | ITGB4 activity raises COL17A1's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 5.92× lower at baseline in the lines without ITGB4 | 0.004 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3; co-absent with the target |

### Downstream of this gene

*76 arrows, 76 of them with an alert ⚠; grade A 0, B 30, C 46. Shown: the 12 strongest; 64 more arrows (64 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMO7]] | B | COL17A1 activity raises LMO7's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 5.71× lower at baseline in the lines without COL17A1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[LMO7DN]] | B | COL17A1 activity raises LMO7DN's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 3.25× lower at baseline in the lines without COL17A1 | 8e-04 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[EPS8L1]] | B | COL17A1 activity raises EPS8L1's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 3.82× lower at baseline in the lines without COL17A1 | 0.003 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[PFKFB2]] | B | COL17A1 activity raises PFKFB2's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 2.61× lower at baseline in the lines without COL17A1 | 0.004 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[MET]] | B | COL17A1 activity raises MET's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 3.36× lower at baseline in the lines without COL17A1 | 0.005 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[KRT8]] | B | COL17A1 activity raises KRT8's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 4.06× lower at baseline in the lines without COL17A1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[ADAP1]] | B | COL17A1 activity raises ADAP1's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 2.90× lower at baseline in the lines without COL17A1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[MFSD6]] | B | COL17A1 activity raises MFSD6's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 2.32× lower at baseline in the lines without COL17A1 | 0.012 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[PERP]] | B | COL17A1 activity raises PERP's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 2.49× lower at baseline in the lines without COL17A1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[EPS8L1]] | B | COL17A1 activity strengthens EPS8L1's drug response | lines that do not express COL17A1 (22) vs lines expressing it (12) | the lines without COL17A1 respond 0.40× as strongly (z diff +2.36); strongest at Panobinostat 5 µM: 0.81x vs 0.21x (z diff +6.7) | 0.014 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1; target measured in part of the lines; artifact flags |
| cells under [[Filgotinib (drug)]] 0.05 µM | B | COL17A1 activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express COL17A1 (34) vs lines expressing it (14) | the lines without COL17A1: 1.27× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| cells under [[Entecavir (monohydrate) (drug)]] 5 µM | B | COL17A1 activity lowers the cells' numbers under Entecavir (monohydrate) 5 µM (makes them more sensitive) | lines that do not express COL17A1 (34) vs lines expressing it (14) | the lines without COL17A1: 1.27× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.748). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.0, 49.3); signed map (67.8, 8.3). **Vector** length 71.2, 27.4% of its response variance represented; |z| ≥ 3 in 489 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +16.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +20.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +5.4 | +12.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.5 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | -3.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -5.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -1.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | collagen type XVII alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.1 — chr10:104,031,286-104,085,880 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BP180; previously BPAG2 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Transmembrane collagens |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 12 pathways, smallest: Type I hemidesmosome assembly; Collagen chain trimerization; Collagen degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMD9](https://www.uniprot.org/uniprotkb/Q9UMD9) (Collagen alpha-1(XVII) chain):

> May play a role in the integrity of hemidesmosome and the attachment of basal keratinocytes to the underlying basement membrane.; The 120 kDa linear IgA disease antigen is an anchoring filament component involved in dermal-epidermal cohesion. Is the target of linear IgA bullous dermatosis autoantibodies.

**Summary**, from NCBI Gene [1308](https://www.ncbi.nlm.nih.gov/gene/1308):

> This gene encodes the alpha chain of type XVII collagen. Unlike most collagens, collagen XVII is a transmembrane protein. Collagen XVII is a structural component of hemidesmosomes, multiprotein complexes at the dermal-epidermal basement membrane zone that mediate adhesion of keratinocytes to the underlying membrane. Mutations in this gene are associated with both generalized atrophic benign and junctional epidermolysis bullosa. Two homotrimeric forms of type XVII collagen exist. The full length …

**Accessions** — [HGNC:2194](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2194) · Entrez [1308](https://www.ncbi.nlm.nih.gov/gene/1308) · UniProt [Q9UMD9](https://www.uniprot.org/uniprotkb/Q9UMD9) · Ensembl [ENSG00000065618](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065618)

## Data

Gene col 799: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 799); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 799, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 799]; `tensor/DDL_lfc|DDL_z.npy` [799]; `embed/gene_vectors.npy` [799]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 799 or target_col == 799). Every well: [[COL17A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL17A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
