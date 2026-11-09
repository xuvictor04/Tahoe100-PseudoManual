---
symbol: "MAN1A1"
type: "gene"
col: 3301
ensembl_id: "ENSG00000111885"
name: "mannosidase alpha class 1A member 1"
location: "6q22.31"
module: 27
arm: "+"
pooled_cpm: 66.58
n_lines_expressing: 30
n_dd_up: 27
n_dd_down: 8
n_dd_up_clean: 23
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 15
direction_downstream: 8
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# MAN1A1

*mannosidase alpha class 1A member 1* — 6q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.03× (z +17.1, q 0e+00, up in 26 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.642× (z -7.3, q 2e-10, down in 18 of 27 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 0.691× (z -6.3, q 7e-08, down in 18 of 28 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NKD1]] (+0.58, fdr 1e-05), [[LMCD1]] (+0.56, fdr 1e-05), [[PCSK5]] (+0.56, fdr 1e-05); moves opposite to [[GLE1]] (-0.41, fdr 2e-04), [[ZNF70]] (-0.40, fdr 2e-04), [[SLC28A2-AS1]] (-0.40, fdr 3e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[RGCC]] → it (grade B ⚠); 8 go from it, the strongest it → [[ZNF703]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3301.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.03×** | +17.1 | 0e+00 | 26/28 (LS 180, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.23×** | +13.7 | 5e-40 | 19/28 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.18×** | +13.2 | 1e-37 | 25/28 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.10×** | +12.6 | 3e-34 | 19/28 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +12.3 | 7e-33 | 17/29 (HOP62, BT-474, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.05×** | +12.2 | 2e-32 | 20/28 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +11.0 | 3e-26 | 18/28 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +10.5 | 8e-24 | 26/29 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +6.7 | 1e-09 | 19/27 (LS 180, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.07×** | +6.5 | 5e-09 | 16/29 (LS 180, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +6.3 | 2e-08 | 19/28 (SHP-77, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +6.0 | 1e-07 | 13/27 (RPMI-7951, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +5.4 | 4e-06 | 8/24 (RPMI-7951, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +5.0 | 2e-05 | 14/28 (SW48, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.32×** | +4.5 | 2e-04 | 13/27 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 3e-04 | 16/28 (LoVo, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +4.3 | 5e-04 | 14/28 (LoVo, HOP62, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.3 | 6e-04 | 10/27 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3301.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.642×** | -7.3 | 2e-10 | 18/27 (HT-29, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.691×** | -6.3 | 7e-08 | 18/28 (CHP-212, SW480, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.772×** | -6.2 | 8e-08 | 15/29 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.748×** | -5.0 | 9e-05 | 13/28 (COLO 205, HepG2/C3A, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.778×** | -4.1 | 0.004 | 13/28 (SW480, A498, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.797×** | -3.9 | 0.009 | 9/27 (COLO 205, HT-29, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -3.9 | 0.009 | 9/28 (LOX-IMVI, HepG2/C3A, …) | top dose only | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.796×** | -3.6 | 0.021 | 10/27 (SW 900, A498, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.681×** | -3.4 | 0.038 | 13/29 (COLO 205, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | 0.706× | -3.1 | 0.11 | 12/26 (SNU-423, HT-29, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3301. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 364 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -10.4) |
| [[LoVo (line)]] | wt | 49.7 | 8 | 0 | [[Tucidinostat (drug)]] 5 µM 4.32× (z +16.9) | — |
| [[LS 180 (line)]] | wt | 29.4 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 7.69× (z +19.9) | — |
| [[HepG2_C3A (line)]] | wt | 644 | 1 | 5 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.96× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -12.1) |
| [[HT-29 (line)]] | alt | 161 | 1 | 5 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.00× (z +9.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.141× (z -18.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.417× (z -8.6) |
| [[SW1417 (line)]] | alt | 283 | 2 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.93× (z +10.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.372× (z -10.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -9.1) |
| [[BT-474 (line)]] | alt | 53.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 43.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 32.8 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.21× (z +10.4) | — |
| [[SW480 (line)]] | alt | 264 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -13.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 64.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.70× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.365× (z -9.4) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 314 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 38.9 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.77× (z +12.9) | — |
| [[HCT15 (line)]] | alt | 80.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 54.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +9.7) | — |
| [[J82 (line)]] | alt | 55.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.0) | — |
| [[SW48 (line)]] | wt | 289 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.02× (z +8.5) | — |
| [[A-172 (line)]] | wt | 15.3 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.02 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.21 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.53 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 13.0 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.61 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.06 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.89 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.63 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.76 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3301), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKD1]] | +0.58 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[LMCD1]] | +0.56 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[PCSK5]] | +0.56 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[PROX1]] | +0.54 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[SESN3]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ZNF703]] | +0.52 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[PROX1-AS1]] | +0.52 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[SPATA13]] | +0.51 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[KRT23]] | +0.51 | +0.50 / +0.30 | both halves | 2e-04 |  |
| [[ATP1B1]] | +0.51 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[TSHZ2]] | +0.50 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[CCR3]] | +0.50 | +0.33 / +0.49 | both halves | 1e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLE1]] | -0.41 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[ZNF70]] | -0.40 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[SLC28A2-AS1]] | -0.40 | -0.29 / -0.37 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 13, C 2. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGCC]] | B | RGCC activity raises MAN1A1's level | lines that do not express RGCC (25) vs lines expressing it (25) | 3.34× lower at baseline in the lines without RGCC | 0.007 | ⚠ within organs, on part of the lines; also absent: IL20RA, TINAGL1, CLIC5 |
| [[LINC00299]] | B | LINC00299 activity raises MAN1A1's level | lines that do not express LINC00299 (27) vs lines expressing it (23) | 2.60× lower at baseline in the lines without LINC00299 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC01814, TNNT2, ATP2C2 |
| [[ATP1B1]] | B | ATP1B1 activity raises MAN1A1's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 3.38× lower at baseline in the lines without ATP1B1 | 0.022 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[JAKMIP2-AS1]] | B | JAKMIP2-AS1 activity raises MAN1A1's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 2.00× lower at baseline in the lines without JAKMIP2-AS1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[ZNF608]] | B | ZNF608 activity raises MAN1A1's level | lines that do not express ZNF608 (12) vs lines expressing it (38) | 2.43× lower at baseline in the lines without ZNF608 | 0.042 | ⚠ within organs, on part of the lines; also absent: LINC01170, GDF15 |
| [[ST18]] | B | ST18 activity raises MAN1A1's level | lines that do not express ST18 (39) vs lines expressing it (11) | 3.01× lower at baseline in the lines without ST18 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent |
| [[PKHD1]] | B | PKHD1 activity raises MAN1A1's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 2.00× lower at baseline in the lines without PKHD1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent |
| [[TSHZ2]] | B | TSHZ2 activity raises MAN1A1's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 2.19× lower at baseline in the lines without TSHZ2 | 0.079 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5 |
| [[AHR]] | B | AHR activity raises MAN1A1's level | lines that do not express AHR (7) vs lines expressing it (43) | 3.65× lower at baseline in the lines without AHR | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[VSNL1]] | B | VSNL1 activity raises MAN1A1's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 2.51× lower at baseline in the lines without VSNL1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[LINC00511]] | B | LINC00511 activity raises MAN1A1's level | lines that do not express LINC00511 (12) vs lines expressing it (38) | 3.12× lower at baseline in the lines without LINC00511 | 0.090 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18 |
| [[HS3ST5]] | B | HS3ST5 activity raises MAN1A1's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.74× lower at baseline in the lines without HS3ST5 | 0.095 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF703]] | B | MAN1A1 activity raises ZNF703's level | lines that do not express MAN1A1 (20) vs lines expressing it (30) | 2.48× lower at baseline in the lines without MAN1A1 | 0.040 | ⚠ within organs, on part of the lines; also absent: BDKRB2, TMEM200A, EVA1A |
| [[LNX1]] | B | MAN1A1 activity raises LNX1's level | lines that do not express MAN1A1 (20) vs lines expressing it (30) | 2.26× lower at baseline in the lines without MAN1A1 | 0.073 | ⚠ within organs, on part of the lines; also absent: BDKRB2, TMEM200A, EVA1A |
| [[SEMA3C]] | B | MAN1A1 activity lowers SEMA3C's level | lines that do not express MAN1A1 (20) vs lines expressing it (30) | 1.68× higher at baseline in the lines without MAN1A1 | 0.088 | ⚠ within organs, on part of the lines; also absent: BDKRB2, TMEM200A, EVA1A |
| [[RASSF6]] | B | MAN1A1 activity raises RASSF6's level | lines that do not express MAN1A1 (20) vs lines expressing it (30) | 2.25× lower at baseline in the lines without MAN1A1 | 0.090 | ⚠ within organs, on part of the lines; also absent: BDKRB2, TMEM200A, EVA1A |
| cells under [[Docetaxel (drug)]] 5 µM | B | MAN1A1 activity raises the cells' numbers under Docetaxel 5 µM (protects the cells) | lines that do not express MAN1A1 (20) vs lines expressing it (28) | the lines without MAN1A1: 0.91× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: BDKRB2, TMEM200A, EVA1A |
| [[RGCC]] | B | MAN1A1 activity raises RGCC's level | lines that do not express MAN1A1 (20) vs lines expressing it (30) | 1.84× lower at baseline in the lines without MAN1A1 | 0.098 | ⚠ within organs, on part of the lines; also absent: BDKRB2, TMEM200A, EVA1A |
| [[LUM]] | C | MAN1A1 activity raises LUM's level | lines that do not express MAN1A1 (20) vs lines expressing it (30) | 2.44× lower at baseline in the lines without MAN1A1 | 0.018 | ⚠ within organs, on part of the lines; also absent: BDKRB2, TMEM200A, EVA1A; co-absent with the target |
| [[ITGA1]] | C | MAN1A1 activity raises ITGA1's level | lines that do not express MAN1A1 (20) vs lines expressing it (30) | 3.69× lower at baseline in the lines without MAN1A1 | 0.032 | ⚠ within organs, on part of the lines; also absent: BDKRB2, TMEM200A, EVA1A; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.500). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.8, 44.1); signed map (54.8, 12.6). **Vector** length 90.9, 25.0% of its response variance represented; |z| ≥ 3 in 855 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +17.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +10.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +4.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.7 | +13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +11.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +4.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +3.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.9 | +2.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.3 | -7.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.8 | -0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.5 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | mannosidase alpha class 1A member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.31 — chr6:119,177,205-119,349,761 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Mannosidases alpha class 1 |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 8 pathways, smallest: Progressive trimming of alpha-1,2-linked mannose residues from Man9/8/7GlcNAc2 to produce Man5GlcNAc2; N-glycan trimming and elongation in the cis-Golgi; Intra-Golgi traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [P33908](https://www.uniprot.org/uniprotkb/P33908) (Mannosyl-oligosaccharide 1,2-alpha-mannosidase IA):

> Involved in the maturation of Asn-linked oligosaccharides. Progressively trim alpha-1,2-linked mannose residues from Man(9)GlcNAc(2) to produce Man(5)GlcNAc(2).

**Summary**, from NCBI Gene [4121](https://www.ncbi.nlm.nih.gov/gene/4121):

> This gene encodes a class I mammalian Golgi 1,2-mannosidase which is a type II transmembrane protein. This protein catalyzes the hydrolysis of three terminal mannose residues from peptide-bound Man(9)-GlcNAc(2) oligosaccharides and belongs to family 47 of glycosyl hydrolases. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:6821](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6821) · Entrez [4121](https://www.ncbi.nlm.nih.gov/gene/4121) · UniProt [P33908](https://www.uniprot.org/uniprotkb/P33908) · Ensembl [ENSG00000111885](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111885)

## Data

Gene col 3301: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3301); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3301, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3301]; `tensor/DDL_lfc|DDL_z.npy` [3301]; `embed/gene_vectors.npy` [3301]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3301 or target_col == 3301). Every well: [[MAN1A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAN1A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
