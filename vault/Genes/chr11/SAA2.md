---
symbol: "SAA2"
type: "gene"
col: 5551
ensembl_id: "ENSG00000134339"
name: "serum amyloid A2"
location: "11p15.1"
module: 139
arm: "+"
pooled_cpm: 10.13
n_lines_expressing: 30
n_dd_up: 51
n_dd_down: 5
n_dd_up_clean: 49
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 19
direction_downstream: 13
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# SAA2

*serum amyloid A2* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 51 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 7.78× (z +16.9, q 0e+00, up in 26 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.491× (z -5.9, q 2e-06, down in 21 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAA2-SAA4]] (+0.98, fdr 7e-06, ⚠ same locus), [[SAA4]] (+0.97, fdr 7e-06, ⚠ same locus), [[SAA1]] (+0.94, fdr 7e-06, ⚠ same locus), [[C3]] (+0.73, fdr 7e-06), [[IRAK3]] (+0.69, fdr 1e-05), [[BCL6]] (+0.69, fdr 7e-06); moves opposite to [[HHIP]] (-0.50, fdr 2e-05), [[PTHLH]] (-0.50, fdr 4e-05), [[DCBLD2]] (-0.49, fdr 3e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[WFDC2]] → it (grade B ⚠); 13 go from it, the strongest it → [[SOD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 2 with an alert ⚠; shown: the 15 strongest. 51 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5551.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **7.78×** | +16.9 | 0e+00 | 26/26 (A498, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **8.58×** | +12.5 | 2e-33 | 21/26 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **7.24×** | +11.5 | 2e-28 | 23/26 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **6.73×** | +11.1 | 2e-26 | 20/27 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **6.42×** | +10.8 | 4e-25 | 26/26 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.54×** | +10.4 | 3e-23 | 15/25 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **4.49×** | +8.7 | 2e-16 | 20/26 (A498, A549, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **3.89×** | +7.9 | 2e-13 | 19/26 (A498, A549, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **2.47×** | +7.4 | 7e-12 | 20/26 (A498, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **3.77×** | +7.4 | 7e-12 | 20/26 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **3.41×** | +7.1 | 6e-11 | 19/26 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **3.37×** | +7.1 | 8e-11 | 20/26 (A498, SNU-423, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.30×** | +6.9 | 2e-10 | 19/26 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **3.28×** | +6.9 | 2e-10 | 18/26 (A498, SNU-423, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **3.11×** | +6.6 | 2e-09 | 19/26 (A498, SNU-423, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5551.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.491×** | -5.9 | 2e-06 | 21/26 (COLO 205, A498, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.493×** | -4.2 | 0.007 | 15/26 (SW 900, A498, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.494×** | -4.1 | 0.007 | 18/26 (COLO 205, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.515×** | -3.9 | 0.014 | 16/27 (COLO 205, A498, …) | top dose only | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.566×** | -3.3 | 0.093 | 13/24 (CFPAC-1, Panc 03.27, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.569× | -3.2 | 0.14 | 13/26 (A549, CFPAC-1, …) | top dose only |  |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | 0.597× | -3.0 | 0.20 | 11/27 (A498, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5551. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 55.8 | 15 | 10 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 17.4× (z +21.2) | [[Auranofin (drug)]] 5 µM 0.0592× (z -14.9) |
| [[COLO 205 (line)]] | alt | 64.8 | 2 | 13 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 6.45× (z +12.4) | [[Tofacitinib (drug)]] 5 µM 0.116× (z -14.3) |
| [[J82 (line)]] | alt | 19.6 | 8 | 0 | [[Tucidinostat (drug)]] 5 µM 45.4× (z +17.7) | — |
| [[A-172 (line)]] | wt | 10.4 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 43.9× (z +16.1) | — |
| [[CFPAC-1 (line)]] | alt | 38.0 | 3 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.77× (z +10.6) | [[Selinexor (drug)]] 5 µM 0.0715× (z -16.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.119× (z -9.1) |
| [[SW 900 (line)]] | alt | 17.9 | 2 | 4 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 14.4× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0477× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 4.23 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 77.6× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 7.45 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 14.9× (z +14.2) | — |
| [[SNU-423 (line)]] | alt | 41.6 | 2 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 10.8× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.0403× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.167× (z -9.2) |
| [[A549 (line)]] | wt | 21.2 | 3 | 1 | [[Tucidinostat (drug)]] 5 µM 8.45× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -9.9) |
| [[PANC-1 (line)]] | alt | 2.58 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 67.4× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 45.9 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 5.96× (z +12.5) | [[Auranofin (drug)]] 5 µM 0.117× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 3.24 | 2 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 7.24× (z +12.6) ⚠ position not correctable · without an alert: [[Tucidinostat (drug)]] 5 µM 53.7× (z +10.3) | — |
| [[HepG2_C3A (line)]] | wt | 10.00 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 10.5× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 2.81 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 131× (z +13.6) | — |
| [[SK-MEL-2 (line)]] | alt | 27.8 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.165× (z -8.6) |
| [[SW480 (line)]] | alt | 4.36 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.60× (z +9.5) | — |
| [[A-427 (line)]] | wt | 0.597 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.984 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.856 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.849 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.874 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.964 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.750 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.845 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.916 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.876 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5551), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAA2-SAA4]] | +0.98 | +0.97 / +0.99 | both halves | 7e-06 | STRING 753; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SAA4]] | +0.97 | +0.97 / +0.97 | both halves | 7e-06 | STRING 935; ⚠ same locus (2.4 kb, same strand: neighbours can correlate without regulation) |
| [[SAA1]] | +0.94 | +0.94 / +0.94 | both halves | 7e-06 | STRING 975; ⚠ same locus (17.6 kb: neighbours can correlate without regulation) |
| [[C3]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 | STRING 450 |
| [[IRAK3]] | +0.69 | +0.55 / +0.69 | both halves | 1e-05 | **novel candidate** |
| [[BCL6]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[NNMT]] | +0.69 | +0.64 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SLPI]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[TLR2]] | +0.67 | +0.55 / +0.65 | both halves | 1e-05 | STRING 615 |
| [[STOM]] | +0.66 | +0.70 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[NAMPT]] | +0.64 | +0.46 / +0.67 | both halves | 2e-05 |  |
| [[FGA]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 | STRING 432 |
| [[CEBPD]] | +0.63 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[BIRC3]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ACSL1]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HHIP]] | -0.50 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[PTHLH]] | -0.50 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[DCBLD2]] | -0.49 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[CAPN2]] | -0.48 | -0.47 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 11, C 8. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WFDC2]] | B | WFDC2 activity raises SAA2's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 2.28× lower at baseline in the lines without WFDC2 | 0.013 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[FGB]] | B | FGB activity raises SAA2's level | lines that do not express FGB (42) vs lines expressing it (8) | 3.11× lower at baseline in the lines without FGB | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2 |
| [[HLA-DRB1]] | B | HLA-DRB1 activity raises SAA2's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 2.25× lower at baseline in the lines without HLA-DRB1 | 0.021 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP |
| [[FGA]] | B | FGA activity raises SAA2's level | lines that do not express FGA (43) vs lines expressing it (7) | 3.69× lower at baseline in the lines without FGA | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG |
| [[SERPINA5]] | B | SERPINA5 activity raises SAA2's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 2.72× lower at baseline in the lines without SERPINA5 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[PDZK1IP1]] | B | PDZK1IP1 activity raises SAA2's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 2.38× lower at baseline in the lines without PDZK1IP1 | 0.062 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[SH3TC1]] | B | SH3TC1 activity raises SAA2's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 3.13× lower at baseline in the lines without SH3TC1 | 0.063 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[TOP2A]] | B | TOP2A activity lowers SAA2's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CCL20]] | B | CCL20 activity raises SAA2's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 2.59× lower at baseline in the lines without CCL20 | 0.094 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[PDGFRA]] | B | PDGFRA activity raises SAA2's level | compounds that target PDGFRA: 2 of 3 lower it (Ponatinib, c-Kit-IN-1) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[PTGES]] | B | PTGES activity raises SAA2's level | lines that do not express PTGES (17) vs lines expressing it (33) | 2.72× lower at baseline in the lines without PTGES | 0.099 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[SAA1]] | C | SAA1 activity raises SAA2's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 4.78× lower at baseline in the lines without SAA1 | 1e-04 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 9, C 4. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOD2]] | B | SAA2 activity raises SOD2's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 2.48× lower at baseline in the lines without SAA2 | 0.026 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3 |
| [[ZC3H12A]] | B | SAA2 activity raises ZC3H12A's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 2.39× lower at baseline in the lines without SAA2 | 0.029 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3 |
| [[SQOR]] | B | SAA2 activity raises SQOR's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 2.65× lower at baseline in the lines without SAA2 | 0.038 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3 |
| [[FTH1]] | B | SAA2 activity raises FTH1's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 2.31× lower at baseline in the lines without SAA2 | 0.044 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3 |
| [[ZMYND8]] | B | SAA2 activity raises ZMYND8's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 1.64× lower at baseline in the lines without SAA2 | 0.048 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3 |
| [[CEBPD]] | B | SAA2 activity raises CEBPD's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 1.91× lower at baseline in the lines without SAA2 | 0.059 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3 |
| [[CCND3]] | B | SAA2 activity raises CCND3's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 1.48× lower at baseline in the lines without SAA2 | 0.068 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3 |
| [[SERPINA3]] | B | SAA2 activity raises SERPINA3's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 2.32× lower at baseline in the lines without SAA2 | 0.085 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3 |
| [[TRIM29]] | B | SAA2 activity raises TRIM29's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 1.79× lower at baseline in the lines without SAA2 | 0.088 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3 |
| [[SAA2-SAA4]] | C | SAA2 activity raises SAA2-SAA4's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 4.08× lower at baseline in the lines without SAA2 | 6e-04 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3; co-absent with the target |
| [[SAA1]] | C | SAA2 activity raises SAA1's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 4.89× lower at baseline in the lines without SAA2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3; co-absent with the target |
| [[SAA4]] | C | SAA2 activity raises SAA4's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 2.78× lower at baseline in the lines without SAA2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3; co-absent with the target |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.908). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.5, 16.0); signed map (16.8, 28.8). **Vector** length 125, 38.8% of its response variance represented; |z| ≥ 3 in 1,261 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-4 and Interleukin-13 signaling* (reactome, mean cos +0.63 to 6); *interferon gamma response* (hallmark, mean cos +0.56 to 6); *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.60 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.1 | +16.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.7 | +10.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.5 | +8.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +5.0 | +7.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +5.0 | +7.1 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.8 | +6.9 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -6.0 | -5.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.9 | -4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.0 | -3.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.9 | -2.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | serum amyloid A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:18,239,223-18,248,668 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [P0DJI9](https://www.uniprot.org/uniprotkb/P0DJI9) (Serum amyloid A-2 protein):

> Major acute phase reactant.

**Summary**, from NCBI Gene [6289](https://www.ncbi.nlm.nih.gov/gene/6289):

> This gene encodes a member of the serum amyloid A family of apolipoproteins. The encoded preproprotein is proteolytically processed to generate the mature protein. This protein is a major acute phase protein that is highly expressed in response to inflammation and tissue injury. This protein also plays an important role in HDL metabolism and cholesterol homeostasis. High levels of this protein are associated with chronic inflammatory diseases including atherosclerosis, rheumatoid arthritis, …

**Accessions** — [HGNC:10514](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10514) · Entrez [6289](https://www.ncbi.nlm.nih.gov/gene/6289) · UniProt [P0DJI9](https://www.uniprot.org/uniprotkb/P0DJI9) · Ensembl [ENSG00000134339](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134339)

## Data

Gene col 5551: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5551); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5551, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5551]; `tensor/DDL_lfc|DDL_z.npy` [5551]; `embed/gene_vectors.npy` [5551]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5551 or target_col == 5551). Every well: [[SAA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
