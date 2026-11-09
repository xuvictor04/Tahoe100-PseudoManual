---
symbol: "PSD2"
type: "gene"
col: 7052
ensembl_id: "ENSG00000146005"
name: "pleckstrin and Sec7 domain containing 2"
location: "5q31.2"
module: 27
arm: "+"
pooled_cpm: 2.07
n_lines_expressing: 37
n_dd_up: 19
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 12
direction_downstream: 5
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# PSD2

*pleckstrin and Sec7 domain containing 2* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.25× (z +13.0, q 4e-36, up in 21 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.453× (z -6.3, q 2e-07, down in 12 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[F10]] (+0.81, fdr 7e-06), [[JAKMIP2-AS1]] (+0.75, fdr 7e-06), [[APCDD1]] (+0.73, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[FGF20]] → it (grade B ⚠); 5 go from it, the strongest it → [[AXIN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7052.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.25×** | +13.0 | 4e-36 | 21/27 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +9.4 | 2e-18 | 8/17 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.38×** | +9.2 | 9e-18 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.99×** | +8.6 | 1e-15 | 12/18 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.66×** | +7.6 | 2e-12 | 13/29 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +6.5 | 7e-09 | 7/19 (LoVo, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +5.3 | 9e-06 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.91×** | +5.0 | 3e-05 | 8/25 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +4.6 | 3e-04 | 9/30 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +4.4 | 6e-04 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.65×** | +3.7 | 0.013 | 3/27 (HOP62, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.87×** | +3.5 | 0.024 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.86×** | +3.4 | 0.024 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.56×** | +3.4 | 0.024 | 0/11 | inconsistent across doses | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +3.3 | 0.032 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +3.2 | 0.049 | 4/27 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.054 | 4/30 (C32, A498, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7052.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.453×** | -6.3 | 2e-07 | 12/25 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~15% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.520×** | -5.2 | 6e-05 | 8/20 (HepG2/C3A, SW480, …) | all doses, flat | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.584×** | -4.3 | 0.004 | 10/23 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.596×** | -4.1 | 0.006 | 11/29 (SW480, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.603×** | -4.0 | 0.007 | 10/30 (SW480, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.620×** | -3.8 | 0.014 | 13/28 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.634×** | -3.6 | 0.023 | 4/29 (LoVo, KATO III, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.05 µM |  | **0.644×** | -3.3 | 0.068 | 7/21 (SW480, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Naproxen (drug)]] 0.5 µM |  | **0.668×** | -3.2 | 0.084 | 4/30 (SW 900, H4, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.675×** | -3.1 | 0.098 | 8/25 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | 0.668× | -3.1 | 0.10 | 4/29 (SHP-77, SW480, …) | top dose only |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.681× | -3.1 | 0.11 | 4/30 (RPMI-7951, HepG2/C3A, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.683× | -3.0 | 0.11 | 3/27 (SW480, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7052. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 16.3 | 0 | 10 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0505× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.138× (z -12.7) |
| [[A-172 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.790 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.444 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.908 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.530 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.762 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.837 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.281 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.285 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.446 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.990 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.988 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.269 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.884 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.711 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.353 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.549 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.960 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7052), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[F10]] | +0.81 | +0.78 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[JAKMIP2-AS1]] | +0.75 | +0.77 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1]] | +0.73 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[NOTUM]] | +0.72 | +0.73 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[SLC30A10]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[FGF20]] | +0.66 | +0.64 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[ST18]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[NKD1]] | +0.65 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[IGFL4]] | +0.64 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[RIMBP2]] | +0.63 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[B3GAT1-DT]] | +0.63 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[LINC02058]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGF20]] | B | FGF20 activity raises PSD2's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 1.97× lower at baseline in the lines without FGF20 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG |
| [[NOTUM]] | B | NOTUM activity raises PSD2's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 1.66× lower at baseline in the lines without NOTUM | 0.016 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7 |
| [[COLGALT2]] | B | COLGALT2 activity raises PSD2's level | lines that do not express COLGALT2 (23) vs lines expressing it (27) | 1.53× lower at baseline in the lines without COLGALT2 | 0.029 | ⚠ within organs, on part of the lines; also absent: PRRX1, SYT11, GNAT3 |
| [[PHYHIPL]] | B | PHYHIPL activity raises PSD2's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 1.70× lower at baseline in the lines without PHYHIPL | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[AXIN2]] | B | AXIN2 activity raises PSD2's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 1.65× lower at baseline in the lines without AXIN2 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[IGFL4]] | B | IGFL4 activity raises PSD2's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 1.59× lower at baseline in the lines without IGFL4 | 0.071 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent |
| [[NKD1]] | B | NKD1 activity raises PSD2's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 1.79× lower at baseline in the lines without NKD1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981 |
| [[SORL1]] | B | SORL1 activity raises PSD2's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 1.34× lower at baseline in the lines without SORL1 | 0.075 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[LRRTM4]] | B | LRRTM4 activity raises PSD2's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 1.70× lower at baseline in the lines without LRRTM4 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973 |
| [[SERPINF1]] | B | SERPINF1 activity raises PSD2's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.39× lower at baseline in the lines without SERPINF1 | 0.088 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[MYT1]] | B | MYT1 activity raises PSD2's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 1.59× lower at baseline in the lines without MYT1 | 0.097 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[KRT5]] | C | KRT5 activity raises PSD2's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 1.98× lower at baseline in the lines without KRT5 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AXIN2]] | B | PSD2 activity raises AXIN2's level | lines that do not express PSD2 (13) vs lines expressing it (37) | 3.04× lower at baseline in the lines without PSD2 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, CACNA1C, SSC5D; maybe low, not absent |
| [[SLIT1]] | B | PSD2 activity raises SLIT1's level | lines that do not express PSD2 (13) vs lines expressing it (37) | 1.86× lower at baseline in the lines without PSD2 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, CACNA1C, SSC5D; maybe low, not absent |
| [[MYT1]] | B | PSD2 activity raises MYT1's level | lines that do not express PSD2 (13) vs lines expressing it (37) | 2.02× lower at baseline in the lines without PSD2 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, CACNA1C, SSC5D; maybe low, not absent |
| [[CD72]] | B | PSD2 activity raises CD72's level | lines that do not express PSD2 (13) vs lines expressing it (37) | 1.67× lower at baseline in the lines without PSD2 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, CACNA1C, SSC5D; maybe low, not absent |
| [[SERPINF1]] | B | PSD2 activity raises SERPINF1's level | lines that do not express PSD2 (13) vs lines expressing it (37) | 1.97× lower at baseline in the lines without PSD2 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, CACNA1C, SSC5D; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.6, 43.4); signed map (62.6, 16.3). **Vector** length 49.6, 9.79% of its response variance represented; |z| ≥ 3 in 710 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +13.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.2 | -4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.8 | -4.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -4.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -3.6 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin and Sec7 domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:139,795,808-139,844,466 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761B0514, EFA6C |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Pleckstrin and Sec7 domain containing |
| Matched by | ensembl_id |

UniProt [Q9BQI7](https://www.uniprot.org/uniprotkb/Q9BQI7) carries no function annotation.

**Summary**, from NCBI Gene [84249](https://www.ncbi.nlm.nih.gov/gene/84249):

> Predicted to enable guanyl-nucleotide exchange factor activity. Predicted to be involved in vesicle-mediated transport. Predicted to be located in cleavage furrow. Predicted to be active in ruffle membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19092](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19092) · Entrez [84249](https://www.ncbi.nlm.nih.gov/gene/84249) · UniProt [Q9BQI7](https://www.uniprot.org/uniprotkb/Q9BQI7) · Ensembl [ENSG00000146005](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146005)

## Data

Gene col 7052: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7052); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7052, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7052]; `tensor/DDL_lfc|DDL_z.npy` [7052]; `embed/gene_vectors.npy` [7052]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7052 or target_col == 7052). Every well: [[PSD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
