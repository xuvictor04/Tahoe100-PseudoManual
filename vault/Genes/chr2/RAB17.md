---
symbol: "RAB17"
type: "gene"
col: 4579
ensembl_id: "ENSG00000124839"
name: "RAB17, member RAS oncogene family"
location: "2q37.3"
module: 27
arm: "+"
pooled_cpm: 11.89
n_lines_expressing: 28
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 32
direction_downstream: 17
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# RAB17

*RAB17, member RAS oncogene family* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.37× (z +6.0, q 1e-06, up in 12 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.679× (z -5.2, q 1e-04, down in 10 of 25 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.793× (z -4.4, q 0.003, down in 16 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (HCT15 0.250×, SW48 0.199×, KATO III 0.348×, HT-29 0.428×, …); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (HepG2/C3A 0.215×, NCI-H1573 0.180×; ⚠ toxic; cell-cycle shift, explains ~9% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.264×, C32 0.174×; ⚠ cell-cycle shift, explains ~28% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.167×); [[Binimetinib (drug)]] 5 µM in 1 line (C32 0.184×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGMO]] (+0.56, fdr 1e-05), [[LOXL4]] (+0.55, fdr 2e-05), [[DIP2C-AS1]] (+0.49, fdr 4e-05); moves opposite to [[MIB1]] (-0.44, fdr 4e-05), [[CCM2]] (-0.43, fdr 6e-05), [[SRR]] (-0.39, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[CGN]] → it (grade B ⚠); 17 go from it, the strongest it → [[SNTB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4579.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +6.0 | 1e-06 | 12/24 (NCI-H2347, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +5.9 | 1e-06 | 14/25 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.27×** | +4.5 | 0.001 | 12/25 (LS 180, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +4.4 | 0.001 | 4/17 (HEC-1-A, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +4.1 | 0.004 | 3/20 (NCI-H2347, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.52×** | +4.0 | 0.005 | 3/23 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.009 | 11/25 (NCI-H2347, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.012 | 10/25 (LoVo, SW480, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.015 | 9/25 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.025 | 10/25 (KATO III, LoVo, …) | two highest doses | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.027 | 10/25 (RPMI-7951, LS 180, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.045 | 8/25 (HT-29, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Thymol (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.057 | 6/24 (HEC-1-A, HCT15, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.17× | +3.0 | 0.090 | 9/25 (HT-29, A-427, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.25×** | +3.0 | 0.090 | 11/25 (LS 180, KATO III, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4579.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (HCT15 0.250×, SW48 0.199×, KATO III 0.348×, HT-29 0.428×, …); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (HepG2/C3A 0.215×, NCI-H1573 0.180×; ⚠ toxic; cell-cycle shift, explains ~9% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.264×, C32 0.174×; ⚠ cell-cycle shift, explains ~28% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.167×); [[Binimetinib (drug)]] 5 µM in 1 line (C32 0.184×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.679×** | -5.2 | 1e-04 | 10/25 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.793×** | -4.4 | 0.003 | 16/24 (HCT15, SW48, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.746×** | -3.9 | 0.013 | 9/25 (SW480, RPMI-7951, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.572×** | -3.9 | 0.013 | 7/25 (KATO III, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.777× | -3.3 | 0.13 | 7/25 (C32, SK-MEL-2, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.795× | -3.1 | 0.19 | 8/25 (C32, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4579. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 35.1 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -9.3) |
| [[SHP-77 (line)]] | alt | 22.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -13.6) |
| [[SW1417 (line)]] | alt | 33.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -8.9) |
| [[C32 (line)]] | wt | 28.9 | 0 | 2 (1 ⚠) | — | [[Binimetinib (drug)]] 5 µM 0.184× (z -9.1) |
| [[A-427 (line)]] | wt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.16× (z +10.8) | — |
| [[HCT15 (line)]] | alt | 36.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 63.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.215× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~9% of this change |
| [[HOP62 (line)]] | alt | 3.00 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0746× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 24.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -9.6) |
| [[LS 180 (line)]] | wt | 20.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.180× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~9% of this change |
| [[NCI-H2347 (line)]] | alt | 9.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +13.6) | — |
| [[SK-MEL-2 (line)]] | alt | 71.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -9.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 6.66 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0946× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 17.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -9.8) |
| [[SW480 (line)]] | alt | 27.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -9.1) |
| [[A-172 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.895 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.872 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.951 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.971 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.68 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4579), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGMO]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[LOXL4]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 | **novel candidate** |
| [[DIP2C-AS1]] | +0.49 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[AEBP1]] | +0.49 | +0.41 / +0.37 | both halves | 7e-05 |  |
| [[LNX1]] | +0.49 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[ESPN]] | +0.48 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[FKBP9P1-1]] | +0.47 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[PWWP3B]] | +0.47 | +0.37 / +0.42 | both halves | 8e-05 |  |
| [[SLC7A8]] | +0.47 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[IL11RA]] | +0.47 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[SELENOP]] | +0.47 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[PPP1R3B-DT]] | +0.46 | +0.32 / +0.46 | both halves | 1e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIB1]] | -0.44 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[CCM2]] | -0.43 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[SRR]] | -0.39 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[PRR14L]] | -0.38 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[UBE2F-SCLY]] | -0.38 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[HGSNAT]] | -0.37 | -0.24 / -0.48 | both halves | 5e-04 |  |
| [[DNAJC9]] | -0.37 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[IL9RP3]] | -0.36 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[MAP3K20]] | -0.36 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[MSL1]] | -0.36 | -0.26 / -0.45 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 18, C 14. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CGN]] | B | CGN activity raises RAB17's level | lines that do not express CGN (21) vs lines expressing it (29) | 3.12× lower at baseline in the lines without CGN | 0.008 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[ANO9]] | B | ANO9 activity raises RAB17's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 2.83× lower at baseline in the lines without ANO9 | 0.009 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[SORL1]] | B | SORL1 activity raises RAB17's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.95× lower at baseline in the lines without SORL1 | 0.009 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[SCIN]] | B | SCIN activity raises RAB17's level | lines that do not express SCIN (22) vs lines expressing it (28) | 1.98× lower at baseline in the lines without SCIN | 0.019 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[DCDC2]] | B | DCDC2 activity raises RAB17's level | lines that do not express DCDC2 (25) vs lines expressing it (25) | 2.35× lower at baseline in the lines without DCDC2 | 0.026 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |
| [[LAPTM5]] | B | LAPTM5 activity raises RAB17's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 1.88× lower at baseline in the lines without LAPTM5 | 0.027 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2 |
| [[OPRD1]] | B | OPRD1 activity raises RAB17's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 2.51× lower at baseline in the lines without OPRD1 | 0.031 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |
| [[TSHZ2]] | B | TSHZ2 activity raises RAB17's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 1.80× lower at baseline in the lines without TSHZ2 | 0.038 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5 |
| [[F5]] | B | F5 activity raises RAB17's level | lines that do not express F5 (39) vs lines expressing it (11) | 2.86× lower at baseline in the lines without F5 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPX2, FGA, CPLX2 |
| [[RNF128]] | B | RNF128 activity raises RAB17's level | lines that do not express RNF128 (23) vs lines expressing it (27) | 2.81× lower at baseline in the lines without RNF128 | 0.047 | ⚠ within organs, on part of the lines; also absent: AZGP1, RNF43, PROM1 |
| [[C4orf19]] | B | C4orf19 activity raises RAB17's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 2.86× lower at baseline in the lines without C4orf19 | 0.048 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[CFI]] | B | CFI activity raises RAB17's level | lines that do not express CFI (31) vs lines expressing it (19) | 1.22× lower at baseline in the lines without CFI | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1 |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 7, C 10. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNTB1]] | B | RAB17 activity raises SNTB1's level | lines that do not express RAB17 (22) vs lines expressing it (28) | 3.82× lower at baseline in the lines without RAB17 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MAL2, TNNT2, BSPRY |
| [[CGN]] | B | RAB17 activity raises CGN's level | lines that do not express RAB17 (22) vs lines expressing it (28) | 3.08× lower at baseline in the lines without RAB17 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MAL2, TNNT2, BSPRY |
| [[RNF128]] | B | RAB17 activity raises RNF128's level | lines that do not express RAB17 (22) vs lines expressing it (28) | 3.23× lower at baseline in the lines without RAB17 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MAL2, TNNT2, BSPRY |
| [[SCIN]] | B | RAB17 activity raises SCIN's level | lines that do not express RAB17 (22) vs lines expressing it (28) | 1.96× lower at baseline in the lines without RAB17 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MAL2, TNNT2, BSPRY |
| [[SORL1]] | B | RAB17 activity raises SORL1's level | lines that do not express RAB17 (22) vs lines expressing it (28) | 3.31× lower at baseline in the lines without RAB17 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MAL2, TNNT2, BSPRY |
| [[ANO9]] | B | RAB17 activity raises ANO9's level | lines that do not express RAB17 (22) vs lines expressing it (28) | 2.67× lower at baseline in the lines without RAB17 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MAL2, TNNT2, BSPRY |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | RAB17 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express RAB17 (22) vs lines expressing it (26) | the lines without RAB17: 1.11× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MAL2, TNNT2, BSPRY |
| [[FAAH2]] | C | RAB17 activity raises FAAH2's level | lines that do not express RAB17 (22) vs lines expressing it (28) | 5.14× lower at baseline in the lines without RAB17 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MAL2, TNNT2, BSPRY; co-absent with the target |
| [[LNX1]] | C | RAB17 activity raises LNX1's level | lines that do not express RAB17 (22) vs lines expressing it (28) | 3.79× lower at baseline in the lines without RAB17 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MAL2, TNNT2, BSPRY; co-absent with the target |
| [[SLC7A8]] | C | RAB17 activity raises SLC7A8's level | lines that do not express RAB17 (22) vs lines expressing it (28) | 2.49× lower at baseline in the lines without RAB17 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MAL2, TNNT2, BSPRY; co-absent with the target |
| [[FGD3]] | C | RAB17 activity raises FGD3's level | lines that do not express RAB17 (22) vs lines expressing it (28) | 2.02× lower at baseline in the lines without RAB17 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MAL2, TNNT2, BSPRY; co-absent with the target |
| [[FGF9]] | C | RAB17 activity raises FGF9's level | lines that do not express RAB17 (22) vs lines expressing it (28) | 2.62× lower at baseline in the lines without RAB17 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MAL2, TNNT2, BSPRY; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.446). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (54.2, 30.5); signed map (28.6, 37.1). **Vector** length 70.7, 18.9% of its response variance represented; |z| ≥ 3 in 561 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +4.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +2.6 |
| fall | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -3.1 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.6 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -5.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | RAB17, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:237,574,322-237,601,614 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 1 pathways, smallest: RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0T7](https://www.uniprot.org/uniprotkb/Q9H0T7) (Ras-related protein Rab-17):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different set of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion (By similarity). RAB17 is involved in transcytosis, the directed movement of endocytosed material through the cell and …

**Summary**, from NCBI Gene [64284](https://www.ncbi.nlm.nih.gov/gene/64284):

> The Rab subfamily of small GTPases plays an important role in the regulation of membrane trafficking. RAB17 is an epithelial cell-specific GTPase (Lutcke et al., 1993 [PubMed 8486736]).[supplied by OMIM, Oct 2009]

**Accessions** — [HGNC:16523](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16523) · Entrez [64284](https://www.ncbi.nlm.nih.gov/gene/64284) · UniProt [Q9H0T7](https://www.uniprot.org/uniprotkb/Q9H0T7) · Ensembl [ENSG00000124839](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124839)

## Data

Gene col 4579: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4579); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4579, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4579]; `tensor/DDL_lfc|DDL_z.npy` [4579]; `embed/gene_vectors.npy` [4579]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4579 or target_col == 4579). Every well: [[RAB17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
