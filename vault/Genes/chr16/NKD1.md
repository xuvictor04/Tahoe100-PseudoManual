---
symbol: "NKD1"
type: "gene"
col: 6450
ensembl_id: "ENSG00000140807"
name: "NKD inhibitor of Wnt signaling pathway 1"
location: "16q12.1"
module: 27
arm: "+"
pooled_cpm: 171.63
n_lines_expressing: 16
n_dd_up: 8
n_dd_down: 22
n_dd_up_clean: 6
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 48
direction_downstream: 17
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# NKD1

*NKD inhibitor of Wnt signaling pathway 1* — 16q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.25× (z +7.1, q 6e-10, up in 5 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.51× (z +5.2, q 5e-05, up in 8 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.434× (z -7.3, q 2e-10, down in 12 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APCDD1]] (+0.80, fdr 7e-06), [[PROX1-AS1]] (+0.77, fdr 7e-06), [[CLRN3]] (+0.75, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 48 arrows point to it, the strongest [[HS3ST5]] → it (grade B ⚠); 17 go from it, the strongest it → [[NKD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6450.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +7.1 | 6e-10 | 5/15 (RKO, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +5.8 | 1e-06 | 6/11 (SW48, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +5.2 | 5e-05 | 8/14 (LS 180, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +4.6 | 5e-04 | 6/14 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.84×** | +3.8 | 0.015 | 2/14 (HCT15, SW48) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +3.8 | 0.015 | 6/14 (RPMI-7951, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 0.05 µM |  | **1.57×** | +3.7 | 0.018 | 8/14 (RKO, A-427, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.44×** | +3.2 | 0.099 | 3/14 (HCT15, RPMI-7951, …) | inconsistent across doses |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.42× | +3.1 | 0.12 | 3/14 (RKO, SW48, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.41× | +3.0 | 0.15 | 5/14 (HepG2/C3A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6450.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.434×** | -7.3 | 2e-10 | 12/14 (LS 180, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.487×** | -6.3 | 9e-08 | 11/14 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.477×** | -6.2 | 9e-08 | 12/14 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.511×** | -5.9 | 6e-07 | 10/14 (COLO 205, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.589×** | -4.6 | 4e-04 | 9/14 (COLO 205, LS 180, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.593×** | -4.6 | 5e-04 | 5/13 (SW480, RKO, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.374×** | -4.5 | 6e-04 | 6/14 (LS 180, COLO 205, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.639×** | -3.9 | 0.006 | 10/14 (HepG2/C3A, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.660×** | -3.6 | 0.018 | 8/14 (HepG2/C3A, COLO 205, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.750×** | -3.5 | 0.022 | 11/14 (SW480, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.677×** | -3.4 | 0.030 | 8/13 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.677×** | -3.4 | 0.030 | 10/14 (HepG2/C3A, SW480, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.677×** | -3.4 | 0.030 | 4/14 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.679×** | -3.3 | 0.046 | 3/14 (SW480, COLO 205, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.770×** | -3.2 | 0.049 | 10/15 (HepG2/C3A, COLO 205, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.684×** | -3.2 | 0.049 | 6/13 (HepG2/C3A, COLO 205, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.695×** | -3.2 | 0.049 | 3/14 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6450. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 746 | 0 | 16 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0815× (z -15.1) ⚠ toxic; cell-cycle shift, explains ~17% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -13.5) |
| [[COLO 205 (line)]] | alt | 360 | 0 | 13 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -14.2) |
| [[SW480 (line)]] | alt | 2,311 | 0 | 12 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -17.2) |
| [[LS 180 (line)]] | wt | 183 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -10.5) |
| [[A-172 (line)]] | wt | 25.5 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.7 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 17.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.9 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 26.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.9 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 37.8 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 25.6 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.2 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 22.5 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 21.1 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 36.2 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.0 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 17.3 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.7 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 19.3 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 27.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.5 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 18.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 396 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.0 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 18.8 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 15.8 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.7 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 38.8 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 26.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 30.9 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 343 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6450), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APCDD1]] | +0.80 | +0.71 / +0.84 | both halves | 7e-06 | STRING 612 |
| [[PROX1-AS1]] | +0.77 | +0.76 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[CLRN3]] | +0.75 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[GJB1]] | +0.74 | +0.70 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[IGFL4]] | +0.74 | +0.75 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[VWA2]] | +0.74 | +0.66 / +0.75 | both halves | 7e-06 |  |
| [[LINC02058]] | +0.74 | +0.69 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[AXIN2]] | +0.72 | +0.66 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_WNT_BETA_CATENIN_SIGNALING; STRING 927 |
| [[BMP4]] | +0.71 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[TFF3]] | +0.71 | +0.71 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[EDAR]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[LGR5]] | +0.69 | +0.72 / +0.67 | both halves | 7e-06 | STRING 520 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*48 arrows, 48 of them with an alert ⚠; grade A 0, B 2, C 46. Shown: the 12 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HS3ST5]] | B | HS3ST5 activity raises NKD1's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.40× lower at baseline in the lines without HS3ST5 | 0.057 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers NKD1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FGD5]] | C | FGD5 activity raises NKD1's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 3.13× lower at baseline in the lines without FGD5 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5; co-absent with the target |
| [[KRT23]] | C | KRT23 activity raises NKD1's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 4.57× lower at baseline in the lines without KRT23 | 0.004 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP; co-absent with the target |
| [[JAKMIP2-AS1]] | C | JAKMIP2-AS1 activity raises NKD1's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 2.74× lower at baseline in the lines without JAKMIP2-AS1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[KRT5]] | C | KRT5 activity raises NKD1's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 6.67× lower at baseline in the lines without KRT5 | 0.005 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[AFP]] | C | AFP activity raises NKD1's level | lines that do not express AFP (45) vs lines expressing it (5) | 5.60× lower at baseline in the lines without AFP | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target |
| [[PHYHIPL]] | C | PHYHIPL activity raises NKD1's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 3.27× lower at baseline in the lines without PHYHIPL | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |
| [[VSNL1]] | C | VSNL1 activity raises NKD1's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 4.30× lower at baseline in the lines without VSNL1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2; co-absent with the target |
| [[APCDD1]] | C | APCDD1 activity raises NKD1's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 5.12× lower at baseline in the lines without APCDD1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751; co-absent with the target |
| [[PEG3]] | C | PEG3 activity raises NKD1's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 2.24× lower at baseline in the lines without PEG3 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1; co-absent with the target |
| [[RIMBP2]] | C | RIMBP2 activity raises NKD1's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 2.49× lower at baseline in the lines without RIMBP2 | 0.013 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 5, C 12. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NKD2]] | B | NKD1 activity raises NKD2's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 2.84× lower at baseline in the lines without NKD1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981 |
| [[ZNRF3]] | B | NKD1 activity raises ZNRF3's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 3.03× lower at baseline in the lines without NKD1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981 |
| [[TGFBR3]] | B | NKD1 activity raises TGFBR3's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 2.25× lower at baseline in the lines without NKD1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981 |
| [[PSD2]] | B | NKD1 activity raises PSD2's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 1.79× lower at baseline in the lines without NKD1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981 |
| [[TSPOAP1-AS1]] | B | NKD1 activity raises TSPOAP1-AS1's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 1.68× lower at baseline in the lines without NKD1 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981 |
| [[HUNK]] | C | NKD1 activity raises HUNK's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 4.17× lower at baseline in the lines without NKD1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981; co-absent with the target |
| [[FAM83F]] | C | NKD1 activity raises FAM83F's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 4.31× lower at baseline in the lines without NKD1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981; co-absent with the target |
| [[AXIN2]] | C | NKD1 activity raises AXIN2's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 6.16× lower at baseline in the lines without NKD1 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981; co-absent with the target |
| [[VSNL1]] | C | NKD1 activity raises VSNL1's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 5.22× lower at baseline in the lines without NKD1 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981; co-absent with the target |
| [[ILDR2]] | C | NKD1 activity raises ILDR2's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 3.12× lower at baseline in the lines without NKD1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981; co-absent with the target |
| [[APCDD1]] | C | NKD1 activity raises APCDD1's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 2.57× lower at baseline in the lines without NKD1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981; co-absent with the target |
| [[ONECUT3]] | C | NKD1 activity raises ONECUT3's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 2.30× lower at baseline in the lines without NKD1 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.6, 44.6); signed map (63.2, 14.6). **Vector** length 68.8, 29.6% of its response variance represented; |z| ≥ 3 in 330 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +7.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.1 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.5 | +3.8 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.2 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.1 | +1.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +0.9 | +1.1 |
| fall | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.4 | -6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | NKD inhibitor of Wnt signaling pathway 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.1 — chr16:50,548,396-50,649,249 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | EF-hand domain containing |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969G9](https://www.uniprot.org/uniprotkb/Q969G9) (Protein naked cuticle homolog 1):

> Cell autonomous antagonist of the canonical Wnt signaling pathway. May activate a second Wnt signaling pathway that controls planar cell polarity.

**Summary**, from NCBI Gene [85407](https://www.ncbi.nlm.nih.gov/gene/85407):

> In the mouse, Nkd is a Dishevelled (see DVL1; MIM 601365)-binding protein that functions as a negative regulator of the Wnt (see WNT1; MIM 164820)-beta-catenin (see MIM 116806)-Tcf (see MIM 602272) signaling pathway.[supplied by OMIM, Jun 2003]

**Accessions** — [HGNC:17045](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17045) · Entrez [85407](https://www.ncbi.nlm.nih.gov/gene/85407) · UniProt [Q969G9](https://www.uniprot.org/uniprotkb/Q969G9) · Ensembl [ENSG00000140807](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140807)

## Data

Gene col 6450: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6450); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6450, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6450]; `tensor/DDL_lfc|DDL_z.npy` [6450]; `embed/gene_vectors.npy` [6450]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6450 or target_col == 6450). Every well: [[NKD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NKD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
