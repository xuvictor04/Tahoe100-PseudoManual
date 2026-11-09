---
symbol: "MFAP3L"
type: "gene"
col: 12752
ensembl_id: "ENSG00000198948"
name: "microfibril associated protein 3 like"
location: "4q33"
module: 133
arm: "+"
pooled_cpm: 4.38
n_lines_expressing: 41
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 9
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# MFAP3L

*microfibril associated protein 3 like* — 4q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.24× (z +30.2, q 0e+00, up in 30 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.639× (z -4.6, q 0.003, down in 18 of 38 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.682× (z -3.9, q 0.026, down in 11 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.0906×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0590×; ⚠ cell-cycle shift, explains ~40% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.292×; ⚠ cell-cycle shift, would explain all of this change); [[Capmatinib (drug)]] 5 µM in 1 line (A-427 0.0541×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HAGLR]] (+0.57, fdr 1e-05), [[RBPMS2]] (+0.56, fdr 2e-04), [[L3MBTL3]] (+0.55, fdr 5e-05); moves opposite to [[PKN2]] (-0.52, fdr 2e-04), [[SPG11]] (-0.49, fdr 2e-04), [[IFT88]] (-0.48, fdr 1e-04).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[PACC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12752.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.24×** | +30.2 | 0e+00 | 30/30 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.00×** | +14.1 | 2e-42 | 31/37 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.79×** | +13.5 | 4e-39 | 32/38 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.32×** | +12.0 | 4e-31 | 28/36 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.24×** | +11.9 | 1e-30 | 29/37 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.01×** | +10.7 | 7e-25 | 19/26 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.71×** | +10.1 | 5e-22 | 30/38 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +7.0 | 2e-10 | 18/29 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.96×** | +6.8 | 7e-10 | 20/31 (HEC-1-A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **3.31×** | +6.3 | 1e-08 | 17/34 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.89×** | +6.2 | 3e-08 | 9/20 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.69×** | +5.3 | 5e-06 | 12/37 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +5.2 | 7e-06 | 16/33 (NCI-H460, A498, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.68×** | +5.2 | 7e-06 | 14/34 (A498, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.0 | 3e-05 | 9/37 (A-172, A498, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +4.6 | 2e-04 | 14/28 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.001 | 7/36 (C-33 A, LoVo, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.005 | 9/37 (A-427, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12752.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.0906×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0590×; ⚠ cell-cycle shift, explains ~40% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.292×; ⚠ cell-cycle shift, would explain all of this change); [[Capmatinib (drug)]] 5 µM in 1 line (A-427 0.0541×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.639×** | -4.6 | 0.003 | 18/38 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.682×** | -3.9 | 0.026 | 11/34 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | 0.557× | -3.1 | 0.34 | 9/32 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.744× | -3.0 | 0.35 | 10/36 (NCI-H1573, PANC-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12752. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 4.92 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.0906× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A498 (line)]] | wt | 6.16 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +15.6) | — |
| [[LoVo (line)]] | wt | 12.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +14.0) | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -8.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 7.57 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.45× (z +13.4) | — |
| [[A-172 (line)]] | wt | 2.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +8.7) | — |
| [[A-427 (line)]] | wt | 13.8 | 0 | 1 | — | [[Capmatinib (drug)]] 5 µM 0.0541× (z -8.6) |
| [[A549 (line)]] | wt | 2.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.1× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 3.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 6.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.90× (z +13.0) | — |
| [[hTERT-HPNE (line)]] | wt | 1.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.4× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 3.96 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0590× (z -10.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H460 (line)]] | wt | 2.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.5× (z +14.6) | — |
| [[RKO (line)]] | wt | 4.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.57× (z +8.7) | — |
| [[SW480 (line)]] | alt | 1.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.35× (z +10.9) | — |
| [[AN3 CA (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.683 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.511 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.975 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12752), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAGLR]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[RBPMS2]] | +0.56 | +0.29 / +0.59 | both halves | 2e-04 |  |
| [[L3MBTL3]] | +0.55 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[KLHL25]] | +0.54 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[AAK1]] | +0.54 | +0.34 / +0.60 | both halves | 1e-04 |  |
| [[MOCOS]] | +0.53 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[SLC47A1]] | +0.52 | +0.39 / +0.56 | both halves | 6e-05 |  |
| [[ZNF536]] | +0.52 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[SLC6A9]] | +0.51 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[SLC1A4]] | +0.51 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[SGPP1]] | +0.51 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[SCAMP5]] | +0.50 | +0.44 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKN2]] | -0.52 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[SPG11]] | -0.49 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[IFT88]] | -0.48 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[NFX1]] | -0.48 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[CEP295]] | -0.45 | -0.28 / -0.32 | both halves | 3e-04 |  |
| [[LINC01473]] | -0.44 | -0.35 / -0.29 | both halves | 2e-04 |  |
| [[R3HDM2]] | -0.43 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[BPTF]] | -0.43 | -0.19 / -0.51 | ⚠ one half (not replicated) | 9e-04 |  |
| [[SPEF2]] | -0.43 | -0.33 / -0.28 | both halves | 3e-04 |  |
| [[MKS1]] | -0.43 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[CHMP4A]] | -0.42 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[METTL25B]] | -0.42 | -0.26 / -0.33 | both halves | 4e-04 |  |
| [[HELQ]] | -0.42 | -0.26 / -0.38 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MFAP3L's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PACC1]] | B | MFAP3L activity raises PACC1's level | lines that do not express MFAP3L (9) vs lines expressing it (41) | 1.92× lower at baseline in the lines without MFAP3L | 0.001 | ⚠ within organs, on part of the lines; also absent: CRACD, FILIP1, TSPAN33; maybe low, not absent |
| [[TSPAN17]] | B | MFAP3L activity raises TSPAN17's level | lines that do not express MFAP3L (9) vs lines expressing it (41) | 1.50× lower at baseline in the lines without MFAP3L | 0.028 | ⚠ within organs, on part of the lines; also absent: CRACD, FILIP1, TSPAN33; maybe low, not absent |
| [[B3GALNT2]] | B | MFAP3L activity raises B3GALNT2's level | lines that do not express MFAP3L (9) vs lines expressing it (41) | 1.47× lower at baseline in the lines without MFAP3L | 0.033 | ⚠ within organs, on part of the lines; also absent: CRACD, FILIP1, TSPAN33; maybe low, not absent |
| [[UBE2F]] | B | MFAP3L activity weakens UBE2F's drug response | lines that do not express MFAP3L (9) vs lines expressing it (39) | the lines without MFAP3L respond 1.43× as strongly (z diff -1.03); strongest at Panobinostat 0.5 µM: 2.61x vs 1.87x (z diff -2.1) | 0.035 | ⚠ within organs, on part of the lines; also absent: CRACD, FILIP1, TSPAN33; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ME2]] | B | MFAP3L activity raises ME2's level | lines that do not express MFAP3L (9) vs lines expressing it (41) | 1.89× lower at baseline in the lines without MFAP3L | 0.040 | ⚠ within organs, on part of the lines; also absent: CRACD, FILIP1, TSPAN33; maybe low, not absent |
| [[USP46]] | B | MFAP3L activity raises USP46's level | lines that do not express MFAP3L (9) vs lines expressing it (41) | 1.51× lower at baseline in the lines without MFAP3L | 0.054 | ⚠ within organs, on part of the lines; also absent: CRACD, FILIP1, TSPAN33; maybe low, not absent |
| [[KLHL25]] | B | MFAP3L activity raises KLHL25's level | lines that do not express MFAP3L (9) vs lines expressing it (41) | 1.44× lower at baseline in the lines without MFAP3L | 0.054 | ⚠ within organs, on part of the lines; also absent: CRACD, FILIP1, TSPAN33; maybe low, not absent |
| [[TRIM33]] | B | MFAP3L activity raises TRIM33's level | lines that do not express MFAP3L (9) vs lines expressing it (41) | 1.23× lower at baseline in the lines without MFAP3L | 0.070 | ⚠ within organs, on part of the lines; also absent: CRACD, FILIP1, TSPAN33; maybe low, not absent |
| [[USB1]] | B | MFAP3L activity raises USB1's level | lines that do not express MFAP3L (9) vs lines expressing it (41) | 1.27× lower at baseline in the lines without MFAP3L | 0.079 | ⚠ within organs, on part of the lines; also absent: CRACD, FILIP1, TSPAN33; maybe low, not absent |

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.447). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-17.6, 43.4); signed map (-10.1, 21.8). **Vector** length 52.3, 8.13% of its response variance represented; |z| ≥ 3 in 898 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +30.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +12.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | +3.0 | +3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +5.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.8 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.1 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -2.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -1.2 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -0.8 | -1.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -0.7 | -1.4 |
|  | [[AZD-8055 (drug)]] 5 µM |  | -0.7 | +0.1 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -0.7 | -0.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | microfibril associated protein 3 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q33 — chr4:169,986,597-170,033,031 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0626, NYD-sp9 |
| Gene groups (HGNC) | I-set domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O75121](https://www.uniprot.org/uniprotkb/O75121) (Microfibrillar-associated protein 3-like):

> May participate in the nuclear signaling of EGFR and MAPK1/ERK2. May a have a role in metastasis.

**Summary**, from NCBI Gene [9848](https://www.ncbi.nlm.nih.gov/gene/9848):

> Located in several cellular components, including cell junction; nucleoplasm; and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29083](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29083) · Entrez [9848](https://www.ncbi.nlm.nih.gov/gene/9848) · UniProt [O75121](https://www.uniprot.org/uniprotkb/O75121) · Ensembl [ENSG00000198948](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198948)

## Data

Gene col 12752: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12752); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12752, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12752]; `tensor/DDL_lfc|DDL_z.npy` [12752]; `embed/gene_vectors.npy` [12752]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12752 or target_col == 12752). Every well: [[MFAP3L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFAP3L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
