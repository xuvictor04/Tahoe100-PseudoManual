---
symbol: "PRKG1"
type: "gene"
col: 11694
ensembl_id: "ENSG00000185532"
name: "protein kinase cGMP-dependent 1"
location: "10q11.23-q21.1"
module: 9
arm: "+"
pooled_cpm: 96.53
n_lines_expressing: 27
n_dd_up: 24
n_dd_down: 8
n_dd_up_clean: 20
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 11
direction_downstream: 9
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PRKG1

*protein kinase cGMP-dependent 1* — 10q11.23-q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.46× (z +21.0, q 0e+00, up in 18 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.712× (z -5.6, q 1e-05, down in 14 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOX5]] (+0.60, fdr 1e-05), [[RGS7]] (+0.59, fdr 1e-05), [[ATRNL1]] (+0.58, fdr 1e-05); moves opposite to [[ENTPD5]] (-0.50, fdr 9e-05), [[TBCCD1]] (-0.49, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[RALYL]] → it (grade B ⚠); 9 go from it, the strongest it → [[CDK14]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11694.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.46×** | +21.0 | 0e+00 | 18/25 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +18.3 | 0e+00 | 13/26 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.41×** | +14.5 | 3e-45 | 19/26 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +11.4 | 5e-28 | 11/25 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.98×** | +11.2 | 3e-27 | 16/25 (HOP62, SW 900, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.03×** | +10.4 | 2e-23 | 16/25 (CFPAC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +8.2 | 2e-14 | 2/24 (HS-578T, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.9 | 4e-10 | 8/27 (SW480, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +6.4 | 1e-08 | 9/25 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +5.6 | 1e-06 | 5/21 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +5.1 | 2e-05 | 17/24 (SW480, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.8 | 8e-05 | 12/22 (NCI-H1573, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +4.2 | 0.001 | 11/26 (NCI-H23, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.30×** | +4.1 | 0.002 | 9/25 (HOP62, H4, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.002 | 8/25 (CFPAC-1, SHP-77, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +3.9 | 0.004 | 6/24 (SW480, NCI-H1573, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.009 | 8/25 (SW480, NCI-H1573, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.009 | 8/25 (J82, NCI-H1573, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.023 | 7/26 (SW 900, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11694.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.712×** | -5.6 | 1e-05 | 14/24 (LOX-IMVI, AN3 CA, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.743×** | -4.7 | 8e-04 | 17/24 (LOX-IMVI, COLO 205, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.602×** | -4.4 | 0.002 | 19/26 (LOX-IMVI, AN3 CA, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.764×** | -4.3 | 0.003 | 8/25 (LOX-IMVI, AN3 CA, …) | rises with dose | plate-row cell shift |
| [[Mebendazole (drug)]] 5 µM |  | **0.766×** | -4.2 | 0.003 | 9/25 (SW 900, hTERT-HPNE, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.620×** | -4.1 | 0.004 | 14/25 (LOX-IMVI, AN3 CA, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.663×** | -3.5 | 0.032 | 11/25 (SW 900, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.824×** | -3.2 | 0.099 | 3/25 (AsPC-1, HOP62, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11694. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 1,244 | 0 | 14 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.120× (z -17.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -16.0) |
| [[AN3 CA (line)]] | alt | 2,564 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0225× (z -26.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -17.5) |
| [[COLO 205 (line)]] | alt | 220 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0373× (z -28.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.262× (z -16.5) |
| [[NCI-H23 (line)]] | alt | 26.1 | 7 (3 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.38× (z +14.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0866× (z -13.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 112 | 3 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.93× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -11.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 43.0 | 4 | 0 | [[Auranofin (drug)]] 5 µM 5.10× (z +12.8) | — |
| [[hTERT-HPNE (line)]] | wt | 1,246 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -11.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 25.8 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 3.50× (z +14.1) | — |
| [[A-427 (line)]] | wt | 33.0 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.92× (z +12.9) | — |
| [[A498 (line)]] | wt | 33.9 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 2.64× (z +10.5) | — |
| [[AsPC-1 (line)]] | alt | 201 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.252× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 56.4 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.46× (z +12.9) | — |
| [[J82 (line)]] | alt | 58.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +15.8) | — |
| [[BT-474 (line)]] | alt | 35.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +13.5) | — |
| [[HS-578T (line)]] | alt | 24.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +12.3) | — |
| [[C32 (line)]] | wt | 58.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.23× (z +9.8) | — |
| [[CHP-212 (line)]] | wt | 204 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 26.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.45× (z +11.4) | — |
| [[SW 900 (line)]] | alt | 108 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.98× (z +10.8) | — |
| [[A-172 (line)]] | wt | 13.7 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 14.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 23.3 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 13.8 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 184 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.82 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.73 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 22.5 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 17.7 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.2 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.4 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 18.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11694), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOX5]] | +0.60 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[RGS7]] | +0.59 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[ATRNL1]] | +0.58 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[CDK14]] | +0.57 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[LINC01320]] | +0.56 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[FAT3]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[MSR1]] | +0.55 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[TLL1]] | +0.55 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[CNTN4]] | +0.55 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[FOXP2]] | +0.55 | +0.55 / +0.61 | both halves | 1e-05 | same gene group |
| [[PHACTR1]] | +0.54 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[SORCS1]] | +0.54 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENTPD5]] | -0.50 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[TBCCD1]] | -0.49 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RALYL]] | B | RALYL activity raises PRKG1's level | lines that do not express RALYL (17) vs lines expressing it (33) | 2.47× lower at baseline in the lines without RALYL | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |
| [[CDK14]] | B | CDK14 activity raises PRKG1's level | lines that do not express CDK14 (11) vs lines expressing it (39) | 3.58× lower at baseline in the lines without CDK14 | 0.071 | ⚠ within organs, on part of the lines; also absent: BNIP3, DYNC1I1, SPART-AS1; maybe low, not absent |
| [[LY96]] | B | LY96 activity raises PRKG1's level | lines that do not express LY96 (18) vs lines expressing it (32) | 2.32× lower at baseline in the lines without LY96 | 0.092 | ⚠ within organs, on part of the lines; also absent: SOX5, ENSG00000287100, ENSG00000287622; maybe low, not absent |
| [[LSAMP]] | B | LSAMP activity raises PRKG1's level | lines that do not express LSAMP (19) vs lines expressing it (31) | 2.65× lower at baseline in the lines without LSAMP | 0.099 | ⚠ within organs, on part of the lines; also absent: FRG1JP, ENSG00000289153, CA9; maybe low, not absent |
| [[NETO1]] | C | NETO1 activity raises PRKG1's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 6.77× lower at baseline in the lines without NETO1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[PPFIA2]] | C | PPFIA2 activity raises PRKG1's level | lines that do not express PPFIA2 (20) vs lines expressing it (30) | 3.34× lower at baseline in the lines without PPFIA2 | 0.044 | ⚠ within organs, on part of the lines; also absent: CASC20, ENSG00000285330, GHR; maybe low, not absent; co-absent with the target |
| [[PRLR]] | C | PRLR activity raises PRKG1's level | lines that do not express PRLR (29) vs lines expressing it (21) | 2.78× lower at baseline in the lines without PRLR | 0.045 | ⚠ within organs, on part of the lines; also absent: DSCAM, CTNND2, AFP; maybe low, not absent; co-absent with the target |
| [[PGR]] | C | PGR activity raises PRKG1's level | lines that do not express PGR (36) vs lines expressing it (14) | 2.94× lower at baseline in the lines without PGR | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent; co-absent with the target |
| [[PHACTR1]] | C | PHACTR1 activity raises PRKG1's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 2.31× lower at baseline in the lines without PHACTR1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L; co-absent with the target |
| [[FGF13]] | C | FGF13 activity raises PRKG1's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 2.16× lower at baseline in the lines without FGF13 | 0.069 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11; co-absent with the target |
| [[LINC02360]] | C | LINC02360 activity raises PRKG1's level | lines that do not express LINC02360 (33) vs lines expressing it (17) | 2.42× lower at baseline in the lines without LINC02360 | 0.096 | ⚠ within organs, on part of the lines; also absent: MAGEB2, LINC01905, AJAP1; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDK14]] | B | PRKG1 activity raises CDK14's level | lines that do not express PRKG1 (23) vs lines expressing it (27) | 2.93× lower at baseline in the lines without PRKG1 | 0.018 | ⚠ within organs, on part of the lines; also absent: NTNG1, CAMK4, DSCAM; maybe low, not absent |
| [[TSHZ2]] | B | PRKG1 activity raises TSHZ2's level | lines that do not express PRKG1 (23) vs lines expressing it (27) | 2.70× lower at baseline in the lines without PRKG1 | 0.039 | ⚠ within organs, on part of the lines; also absent: NTNG1, CAMK4, DSCAM; maybe low, not absent |
| [[SLC9A9]] | B | PRKG1 activity raises SLC9A9's level | lines that do not express PRKG1 (23) vs lines expressing it (27) | 1.88× lower at baseline in the lines without PRKG1 | 0.064 | ⚠ within organs, on part of the lines; also absent: NTNG1, CAMK4, DSCAM; maybe low, not absent |
| [[ZFPM2]] | B | PRKG1 activity raises ZFPM2's level | lines that do not express PRKG1 (23) vs lines expressing it (27) | 2.03× lower at baseline in the lines without PRKG1 | 0.095 | ⚠ within organs, on part of the lines; also absent: NTNG1, CAMK4, DSCAM; maybe low, not absent |
| [[SOX5]] | C | PRKG1 activity raises SOX5's level | lines that do not express PRKG1 (23) vs lines expressing it (27) | 2.91× lower at baseline in the lines without PRKG1 | 0.032 | ⚠ within organs, on part of the lines; also absent: NTNG1, CAMK4, DSCAM; maybe low, not absent; co-absent with the target |
| [[PHACTR1]] | C | PRKG1 activity raises PHACTR1's level | lines that do not express PRKG1 (23) vs lines expressing it (27) | 2.37× lower at baseline in the lines without PRKG1 | 0.049 | ⚠ within organs, on part of the lines; also absent: NTNG1, CAMK4, DSCAM; maybe low, not absent; co-absent with the target |
| [[PPFIA2]] | C | PRKG1 activity raises PPFIA2's level | lines that do not express PRKG1 (23) vs lines expressing it (27) | 2.16× lower at baseline in the lines without PRKG1 | 0.054 | ⚠ within organs, on part of the lines; also absent: NTNG1, CAMK4, DSCAM; maybe low, not absent; co-absent with the target |
| [[MARK1]] | C | PRKG1 activity raises MARK1's level | lines that do not express PRKG1 (23) vs lines expressing it (27) | 2.41× lower at baseline in the lines without PRKG1 | 0.066 | ⚠ within organs, on part of the lines; also absent: NTNG1, CAMK4, DSCAM; maybe low, not absent; co-absent with the target |
| [[ADAMTS3]] | C | PRKG1 activity raises ADAMTS3's level | lines that do not express PRKG1 (23) vs lines expressing it (27) | 2.49× lower at baseline in the lines without PRKG1 | 0.092 | ⚠ within organs, on part of the lines; also absent: NTNG1, CAMK4, DSCAM; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.0, 30.9); signed map (35.2, 25.7). **Vector** length 79.1, 20.4% of its response variance represented; |z| ≥ 3 in 731 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.9 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.4 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +9.2 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +9.0 | +21.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +18.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.7 | +11.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +5.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -3.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.3 | -1.7 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -2.2 | -0.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase cGMP-dependent 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.23-q21.1 — chr10:50,990,888-52,298,423 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PGK, PKG, PKG1; previously PRKGR1B, PRKG1B |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Protein kinase G family |
| Reactome | 13 pathways, smallest: cGMP effects; Rap1 signalling; Nitric oxide stimulates guanylate cyclase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13976](https://www.uniprot.org/uniprotkb/Q13976) (cGMP-dependent protein kinase 1):

> Serine/threonine protein kinase that acts as a key mediator of the nitric oxide (NO)/cGMP signaling pathway. GMP binding activates PRKG1, which phosphorylates serines and threonines on many cellular proteins. Numerous protein targets for PRKG1 phosphorylation are implicated in modulating cellular calcium, but the contribution of each of these targets may vary substantially among cell types. Proteins that are phosphorylated by PRKG1 regulate platelet activation and adhesion, smooth muscle …

**Summary**, from NCBI Gene [5592](https://www.ncbi.nlm.nih.gov/gene/5592):

> Mammals have three different isoforms of cyclic GMP-dependent protein kinase (Ialpha, Ibeta, and II). These PRKG isoforms act as key mediators of the nitric oxide/cGMP signaling pathway and are important components of many signal transduction processes in diverse cell types. This PRKG1 gene on human chromosome 10 encodes the soluble Ialpha and Ibeta isoforms of PRKG by alternative transcript splicing. A separate gene on human chromosome 4, PRKG2, encodes the membrane-bound PRKG isoform II. The …

**Accessions** — [HGNC:9414](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9414) · Entrez [5592](https://www.ncbi.nlm.nih.gov/gene/5592) · UniProt [Q13976](https://www.uniprot.org/uniprotkb/Q13976) · Ensembl [ENSG00000185532](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185532)

## Data

Gene col 11694: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11694); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11694, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11694]; `tensor/DDL_lfc|DDL_z.npy` [11694]; `embed/gene_vectors.npy` [11694]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11694 or target_col == 11694). Every well: [[PRKG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
