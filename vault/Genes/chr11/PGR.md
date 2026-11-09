---
symbol: "PGR"
type: "gene"
col: 1338
ensembl_id: "ENSG00000082175"
name: "progesterone receptor"
location: "11q22.1"
module: 155
arm: "+"
pooled_cpm: 2.35
n_lines_expressing: 14
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 14
direction_downstream: 23
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# PGR

*progesterone receptor* — 11q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.89× (z +12.0, q 3e-30, up in 4 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FUT9]] (+0.63, fdr 1e-05), [[PRLR]] (+0.60, fdr 1e-05), [[VIPR2]] (+0.58, fdr 5e-05); moves opposite to [[S100A8]] (-0.64, fdr 1e-05), [[S100A9]] (-0.61, fdr 1e-05), [[LINC01440]] (-0.59, fdr 1e-05).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[RALYL]] → it (grade B ⚠); 23 go from it, the strongest it → [[CNTNAP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1338.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.89×** | +12.0 | 3e-30 | 4/6 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.27×** | +10.2 | 7e-22 | 1/1 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.85×** | +9.4 | 9e-19 | 2/4 (BT-474, SHP-77) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.63×** | +6.4 | 3e-08 | 1/1 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.25×** | +6.1 | 1e-07 | 1/7 (BT-474) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.12×** | +5.7 | 1e-06 | 2/8 (NCI-H460, HOP62) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +5.3 | 9e-06 | 0/5 | top dose only | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.26×** | +4.3 | 1e-03 | 3/8 (HOP62, BT-474, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +4.2 | 0.002 | 0/4 | top dose only | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.17×** | +4.1 | 0.002 | 2/7 (HS-578T, hTERT-HPNE) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.09×** | +3.9 | 0.005 | 4/7 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.66×** | +3.8 | 0.006 | 3/7 (hTERT-HPNE, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.87×** | +3.8 | 0.007 | 1/2 (BT-474) | top dose only | noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +3.7 | 0.007 | 2/4 (NCI-H460, BT-474) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.96×** | +3.6 | 0.014 | 0/6 | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +3.5 | 0.014 | 2/8 (BT-474, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +3.3 | 0.035 | 1/8 (HOP62) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.35×** | +3.2 | 0.037 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +3.1 | 0.055 | 1/8 (BT-474) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1338.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Asciminib (drug)]] 0.5 µM |  | 0.528× | -3.4 | 0.21 | 0/8 | inconsistent across doses |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.535× | -3.4 | 0.21 | 4/8 (CHP-212, HS-578T, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1338. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.464 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.392 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.336 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.784 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.468 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.368 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.343 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.511 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.369 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.324 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.616 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.389 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.399 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.412 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.778 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.640 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.376 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1338), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 17 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUT9]] | +0.63 | +0.63 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[PRLR]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE; STRING 639 |
| [[VIPR2]] | +0.58 | +0.55 / +0.40 | both halves | 5e-05 | **novel candidate** |
| [[RALYL]] | +0.56 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[LRFN2]] | +0.52 | +0.63 / +0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[FGF13]] | +0.50 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[KCTD8]] | +0.50 | +0.60 / +0.29 | both halves | 2e-04 |  |
| [[ESRRG]] | +0.50 | +0.58 / +0.41 | both halves | 4e-05 | pathway: Nuclear Receptor transcription pathway |
| [[ANKRD30A]] | +0.49 | +0.29 / +0.60 | both halves | 2e-04 |  |
| [[NPAS3]] | +0.48 | +0.46 / +0.39 | both halves | 6e-05 |  |
| [[ERBB4]] | +0.48 | +0.46 / +0.47 | both halves | 3e-05 | pathway: ESR-mediated signaling; STRING 881 |
| [[CASC15]] | +0.47 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[LMO3]] | +0.47 | +0.59 / +0.24 | both halves | 4e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[S100A8]] | -0.64 | -0.57 / -0.69 | both halves | 1e-05 | **novel candidate** |
| [[S100A9]] | -0.61 | -0.56 / -0.59 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[LINC01440]] | -0.59 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[CES1]] | -0.50 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[FGB]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[SERPINB3]] | -0.49 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[SERPINB4]] | -0.49 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[GSDMC]] | -0.48 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[SPTSSB]] | -0.47 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[CDH3]] | -0.46 | -0.48 / -0.36 | both halves | 1e-04 | STRING 422 |
| [[EPHA1]] | -0.44 | -0.46 / -0.24 | both halves | 5e-04 |  |
| [[FLRT3]] | -0.43 | -0.31 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 1, C 13. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RALYL]] | B | RALYL activity raises PGR's level | lines that do not express RALYL (17) vs lines expressing it (33) | 1.67× lower at baseline in the lines without RALYL | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |
| [[PDZRN3]] | C | PDZRN3 activity raises PGR's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 2.01× lower at baseline in the lines without PDZRN3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises PGR's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 2.40× lower at baseline in the lines without RIT2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises PGR's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 2.10× lower at baseline in the lines without KCNB2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[MUC6]] | C | MUC6 activity raises PGR's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 5.13× lower at baseline in the lines without MUC6 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises PGR's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 2.51× lower at baseline in the lines without SYT4 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises PGR's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 1.71× lower at baseline in the lines without SRRM4 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[SOX6]] | C | SOX6 activity raises PGR's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 1.60× lower at baseline in the lines without SOX6 | 0.051 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises PGR's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 1.74× lower at baseline in the lines without ASCL1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises PGR's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.59× lower at baseline in the lines without RUNX1T1 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[FGF13]] | C | FGF13 activity raises PGR's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 1.91× lower at baseline in the lines without FGF13 | 0.071 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11; co-absent with the target |
| [[ACSS3]] | C | ACSS3 activity raises PGR's level | lines that do not express ACSS3 (31) vs lines expressing it (19) | 1.79× lower at baseline in the lines without ACSS3 | 0.077 | ⚠ within organs, on part of the lines; also absent: NTNG1, ENSG00000289884, HOPX; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 6, C 17. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNTNAP2]] | B | PGR activity raises CNTNAP2's level | lines that do not express PGR (36) vs lines expressing it (14) | 2.52× lower at baseline in the lines without PGR | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent |
| [[KCNMB2]] | B | PGR activity raises KCNMB2's level | lines that do not express PGR (36) vs lines expressing it (14) | 2.27× lower at baseline in the lines without PGR | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent |
| [[RALYL]] | B | PGR activity raises RALYL's level | lines that do not express PGR (36) vs lines expressing it (14) | 2.68× lower at baseline in the lines without PGR | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent |
| [[LINC02306]] | B | PGR activity raises LINC02306's level | lines that do not express PGR (36) vs lines expressing it (14) | 1.99× lower at baseline in the lines without PGR | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent |
| [[ESR1]] | B | PGR activity raises ESR1's level | lines that do not express PGR (36) vs lines expressing it (14) | 1.52× lower at baseline in the lines without PGR | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent |
| [[MYT1L]] | B | PGR activity raises MYT1L's level | lines that do not express PGR (36) vs lines expressing it (14) | 1.85× lower at baseline in the lines without PGR | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent |
| [[DOK6]] | C | PGR activity raises DOK6's level | lines that do not express PGR (36) vs lines expressing it (14) | 3.75× lower at baseline in the lines without PGR | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent; co-absent with the target |
| [[ACSS3]] | C | PGR activity raises ACSS3's level | lines that do not express PGR (36) vs lines expressing it (14) | 2.02× lower at baseline in the lines without PGR | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent; co-absent with the target |
| [[PDZRN3]] | C | PGR activity raises PDZRN3's level | lines that do not express PGR (36) vs lines expressing it (14) | 4.28× lower at baseline in the lines without PGR | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent; co-absent with the target |
| [[KCNB2]] | C | PGR activity raises KCNB2's level | lines that do not express PGR (36) vs lines expressing it (14) | 2.89× lower at baseline in the lines without PGR | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent; co-absent with the target |
| [[TENM2]] | C | PGR activity raises TENM2's level | lines that do not express PGR (36) vs lines expressing it (14) | 4.68× lower at baseline in the lines without PGR | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent; co-absent with the target |
| [[RUNX1T1]] | C | PGR activity raises RUNX1T1's level | lines that do not express PGR (36) vs lines expressing it (14) | 5.00× lower at baseline in the lines without PGR | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction -0.568). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.2, 36.4); signed map (44.7, 31.6). **Vector** length 20.1, 5.31% of its response variance represented; |z| ≥ 3 in 189 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.7 | +3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.7 | +1.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.7 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -1.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.5 | -1.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -0.5 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.5 | -1.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | progesterone receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.1 — chr11:101,029,624-101,129,813 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PR, NR3C3 |
| Gene groups (HGNC) | Nuclear receptor subfamily 3 group C |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 13 pathways, smallest: Nuclear signaling by ERBB4; SUMOylation of intracellular receptors; HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand |
| Matched by | ensembl_id |

**Function**, from UniProt [P06401](https://www.uniprot.org/uniprotkb/P06401) (Progesterone receptor):

> The steroid hormones and their receptors are involved in the regulation of eukaryotic gene expression and affect cellular proliferation and differentiation in target tissues. Depending on the isoform, progesterone receptor functions as a transcriptional activator or repressor.; [Isoform A]: Ligand-dependent transdominant repressor of steroid hormone receptor transcriptional activity including repression of its isoform B, MR and ER. Transrepressional activity may involve recruitment of …

**Summary**, from NCBI Gene [5241](https://www.ncbi.nlm.nih.gov/gene/5241):

> This gene encodes a member of the steroid receptor superfamily. The encoded protein mediates the physiological effects of progesterone, which plays a central role in reproductive events associated with the establishment and maintenance of pregnancy. This gene uses two distinct promotors and translation start sites in the first exon to produce several transcript variants, both protein coding and non-protein coding. Two of the isoforms (A and B) are identical except for an additional 165 amino …

**Accessions** — [HGNC:8910](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8910) · Entrez [5241](https://www.ncbi.nlm.nih.gov/gene/5241) · UniProt [P06401](https://www.uniprot.org/uniprotkb/P06401) · Ensembl [ENSG00000082175](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082175)

## Data

Gene col 1338: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1338); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1338, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1338]; `tensor/DDL_lfc|DDL_z.npy` [1338]; `embed/gene_vectors.npy` [1338]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1338 or target_col == 1338). Every well: [[PGR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
