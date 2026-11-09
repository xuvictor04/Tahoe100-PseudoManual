---
symbol: "FKBP9P1-1"
type: "gene"
col: 16546
ensembl_id: "ENSG00000291029"
name: ""
location: ""
module: 87
arm: "+"
pooled_cpm: 3.5
n_lines_expressing: 20
n_dd_up: 4
n_dd_down: 20
n_dd_up_clean: 0
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 13
direction_downstream: 53
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# FKBP9P1-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.29× (z +9.3, q 1e-17, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.391× (z -7.6, q 1e-11, down in 13 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FKBP9P1]] (+0.81, fdr 7e-06, ⚠ same locus), [[LEF1-AS1]] (+0.72, fdr 7e-06), [[LEF1]] (+0.66, fdr 7e-06), [[OPRD1]] (+0.66, fdr 1e-05).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[BLACAT1]] → it (grade B ⚠); 53 go from it, the strongest it → [[FKBP9P1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16546.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.29×** | +9.3 | 1e-17 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.28×** | +6.7 | 7e-09 | 1/9 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +6.4 | 3e-08 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.45×** | +5.2 | 3e-05 | 1/7 (Panc 03.27) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.51× | +3.3 | 0.10 | 0/11 | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.75× | +3.2 | 0.11 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 2.13× | +3.2 | 0.11 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 1.47× | +3.1 | 0.11 | 0/11 | inconsistent across doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 2.09× | +3.1 | 0.11 | 0/4 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16546.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.391×** | -7.6 | 1e-11 | 13/16 (SHP-77, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.379×** | -7.6 | 1e-11 | 14/15 (Panc 03.27, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.573×** | -6.4 | 3e-08 | 13/14 (SHP-77, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.465×** | -6.2 | 8e-08 | 11/15 (Panc 03.27, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.488×** | -5.8 | 7e-07 | 13/14 (Panc 03.27, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.520×** | -5.3 | 1e-05 | 12/16 (SHP-77, SW480, …) | all doses, flat | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.535×** | -5.1 | 3e-05 | 12/16 (SHP-77, Panc 03.27, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.557×** | -4.7 | 1e-04 | 13/16 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.566×** | -4.6 | 2e-04 | 13/16 (SHP-77, C32, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.585×** | -4.3 | 8e-04 | 8/16 (KATO III, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.404×** | -3.8 | 0.006 | 5/16 (SHP-77, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.617×** | -3.8 | 0.008 | 3/16 (CFPAC-1, KATO III, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.649×** | -3.5 | 0.020 | 7/16 (SW480, RPMI-7951, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.631×** | -3.5 | 0.021 | 8/16 (SK-MEL-2, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.670×** | -3.2 | 0.044 | 13/16 (H4, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.677×** | -3.2 | 0.056 | 4/11 (SHP-77, H4, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.635×** | -3.1 | 0.067 | 0/16 | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16546. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 31.5 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0458× (z -18.4) |
| [[SHP-77 (line)]] | alt | 44.2 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0136× (z -29.7) |
| [[Panc 03.27 (line)]] | alt | 30.8 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0158× (z -25.9) |
| [[H4 (line)]] | wt | 23.9 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0136× (z -13.8) |
| [[SW480 (line)]] | alt | 7.10 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0908× (z -15.4) |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -11.2) |
| [[KATO III (line)]] | alt | 5.55 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0368× (z -10.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0372× (z -10.4) |
| [[A-172 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.569 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.713 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.966 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.724 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.936 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.522 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.627 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.507 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.642 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.827 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.629 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16546), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP9P1]] | +0.81 | +0.84 / +0.74 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[LEF1-AS1]] | +0.72 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[LEF1]] | +0.66 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[OPRD1]] | +0.66 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[SHROOM4]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[C10orf90]] | +0.63 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[PTPRZ1]] | +0.62 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[LOXL4]] | +0.61 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SAMMSON]] | +0.61 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[MILR1]] | +0.59 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[SOX10]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[AGMO]] | +0.58 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[MIR3681HG]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 3, C 10. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BLACAT1]] | B | BLACAT1 activity raises FKBP9P1-1's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 2.00× lower at baseline in the lines without BLACAT1 | 0.032 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[SNTB1]] | B | SNTB1 activity raises FKBP9P1-1's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without SNTB1 | 0.044 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979 |
| [[RNF128]] | B | RNF128 activity raises FKBP9P1-1's level | lines that do not express RNF128 (23) vs lines expressing it (27) | 1.68× lower at baseline in the lines without RNF128 | 0.098 | ⚠ within organs, on part of the lines; also absent: AZGP1, RNF43, PROM1 |
| [[CFI]] | C | CFI activity raises FKBP9P1-1's level | lines that do not express CFI (31) vs lines expressing it (19) | 2.16× lower at baseline in the lines without CFI | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1; co-absent with the target |
| [[CCDC152]] | C | CCDC152 activity raises FKBP9P1-1's level | lines that do not express CCDC152 (30) vs lines expressing it (20) | 2.34× lower at baseline in the lines without CCDC152 | 0.033 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent; co-absent with the target |
| [[MILR1]] | C | MILR1 activity raises FKBP9P1-1's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 2.33× lower at baseline in the lines without MILR1 | 0.042 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1; co-absent with the target |
| [[EPHA3]] | C | EPHA3 activity raises FKBP9P1-1's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 2.01× lower at baseline in the lines without EPHA3 | 0.046 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491; co-absent with the target |
| [[GJB1]] | C | GJB1 activity raises FKBP9P1-1's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 2.15× lower at baseline in the lines without GJB1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B; co-absent with the target |
| [[NAA11]] | C | NAA11 activity raises FKBP9P1-1's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 2.41× lower at baseline in the lines without NAA11 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[MIR3667HG]] | C | MIR3667HG activity raises FKBP9P1-1's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 2.07× lower at baseline in the lines without MIR3667HG | 0.076 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[LAPTM5]] | C | LAPTM5 activity raises FKBP9P1-1's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 1.95× lower at baseline in the lines without LAPTM5 | 0.084 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2; co-absent with the target |
| [[INPP5D]] | C | INPP5D activity raises FKBP9P1-1's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 1.56× lower at baseline in the lines without INPP5D | 0.086 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5; co-absent with the target |

### Downstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 16, C 37. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FKBP9P1]] | B | FKBP9P1-1 activity raises FKBP9P1's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 2.78× lower at baseline in the lines without FKBP9P1-1 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[FMN1]] | B | FKBP9P1-1 activity raises FMN1's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 2.63× lower at baseline in the lines without FKBP9P1-1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[TRIB2]] | B | FKBP9P1-1 activity raises TRIB2's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 2.98× lower at baseline in the lines without FKBP9P1-1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[DIRC3]] | B | FKBP9P1-1 activity raises DIRC3's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 2.98× lower at baseline in the lines without FKBP9P1-1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[NELL1]] | B | FKBP9P1-1 activity raises NELL1's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 1.78× lower at baseline in the lines without FKBP9P1-1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[SETBP1]] | B | FKBP9P1-1 activity raises SETBP1's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 3.52× lower at baseline in the lines without FKBP9P1-1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[SORCS2]] | B | FKBP9P1-1 activity raises SORCS2's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 1.88× lower at baseline in the lines without FKBP9P1-1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[ALK]] | B | FKBP9P1-1 activity raises ALK's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 2.51× lower at baseline in the lines without FKBP9P1-1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[SNTB1]] | B | FKBP9P1-1 activity raises SNTB1's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 2.21× lower at baseline in the lines without FKBP9P1-1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[OPRD1]] | B | FKBP9P1-1 activity raises OPRD1's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 1.68× lower at baseline in the lines without FKBP9P1-1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[BLACAT1]] | B | FKBP9P1-1 activity raises BLACAT1's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 1.92× lower at baseline in the lines without FKBP9P1-1 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[FKBP9P1]] | B | FKBP9P1-1 activity strengthens FKBP9P1's drug response | lines that do not express FKBP9P1-1 (18) vs lines expressing it (17) | the lines without FKBP9P1-1 respond 0.49× as strongly (z diff +2.24); strongest at Homoharringtonine 5 µM: 0.34x vs 0.12x (z diff +4.4) | 0.075 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (53.5, 29.4); signed map (28.8, 38.1). **Vector** length 60.5, 19.0% of its response variance represented; |z| ≥ 3 in 534 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | -1.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.9 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +0.7 |
|  | [[Glycyrrhizic acid (drug)]] 0.05 µM |  | +1.3 | +1.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.7 | -3.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.5 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -0.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.3 | -3.1 |

## What is on record

> [!warning] No registry record
> FKBP9P1-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16546: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16546); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16546, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16546]; `tensor/DDL_lfc|DDL_z.npy` [16546]; `embed/gene_vectors.npy` [16546]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16546 or target_col == 16546). Every well: [[FKBP9P1-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FKBP9P1-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
