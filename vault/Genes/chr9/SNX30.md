---
symbol: "SNX30"
type: "gene"
col: 7247
ensembl_id: "ENSG00000148158"
name: "sorting nexin family member 30"
location: "9q32"
module: 45
arm: "+"
pooled_cpm: 41.34
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# SNX30

*sorting nexin family member 30* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.78× (z +8.8, q 9e-16, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.661× (z -6.1, q 6e-07, down in 29 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.676× (z -6.0, q 6e-07, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THRA]] (+0.67, fdr 1e-05), [[STX7]] (+0.64, fdr 1e-05), [[VAT1]] (+0.62, fdr 1e-05); moves opposite to [[AGAP6]] (-0.64, fdr 1e-05), [[TAF2]] (-0.64, fdr 1e-05), [[BMS1P4-1]] (-0.64, fdr 3e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[SLC43A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7247.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +8.8 | 9e-16 | 34/47 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +7.2 | 2e-10 | 34/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +6.1 | 2e-07 | 27/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.05×** | +5.6 | 3e-06 | 36/47 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +5.0 | 7e-05 | 26/47 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.5 | 6e-04 | 22/47 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +4.3 | 0.001 | 25/47 (C32, HOP62, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 1.19× | +3.7 | 0.014 | 18/47 (RPMI-7951, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +3.4 | 0.038 | 15/47 (RKO, HT-29, …) | top dose only |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.057 | 12/47 (C32, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +3.2 | 0.073 | 10/47 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.076 | 19/47 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7247.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.661×** | -6.1 | 6e-07 | 29/46 (CFPAC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.676×** | -6.0 | 6e-07 | 33/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.692×** | -5.6 | 4e-06 | 28/47 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.699×** | -5.5 | 5e-06 | 23/44 (RKO, Panc 03.27, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.690×** | -5.5 | 5e-06 | 24/39 (SK-MEL-2, HEC-1-A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.716×** | -4.7 | 2e-04 | 22/41 (LS 180, NCI-H2347, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.767×** | -3.9 | 0.008 | 23/47 (BT-474, SW48, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.783×** | -3.6 | 0.023 | 23/47 (AN3 CA, LoVo, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.856× | -3.4 | 0.048 | 19/47 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.796×** | -3.3 | 0.054 | 22/47 (NCI-H460, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.818× | -3.1 | 0.10 | 18/47 (A549, A-172, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | 0.678× | -3.1 | 0.10 | 15/46 (NCI-H2347, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7247. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 18.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.96× (z +10.3) | — |
| [[A498 (line)]] | wt | 32.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 78.8 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.107× (z -8.8) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 67.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[LS 180 (line)]] | wt | 59.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[MIA PaCa-2 (line)]] | alt | 55.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 51.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[RKO (line)]] | wt | 46.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[RPMI-7951 (line)]] | alt | 36.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.254× (z -9.2) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 59.1 | 0 | 1 | — | [[Sonidegib (drug)]] 5 µM 0.0852× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 77.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[A-172 (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 56.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7247), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THRA]] | +0.67 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[STX7]] | +0.64 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[VAT1]] | +0.62 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[SLC25A23]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[MGAT4A]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[FAM102B]] | +0.61 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ZDHHC20]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[CAT]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[TMEM185A]] | +0.61 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[PIP4P2]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SORT1]] | +0.60 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ATP8A1]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGAP6]] | -0.64 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[TAF2]] | -0.64 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[BMS1P4-1]] | -0.64 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[CSTF3]] | -0.63 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[CDK12]] | -0.60 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[MTG2]] | -0.59 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[MRPL45P2]] | -0.58 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[DNAJC11]] | -0.57 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[DNTTIP2]] | -0.57 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[PSMD7]] | -0.56 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[EMG1]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[FAF2]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC43A1]] | B | SLC43A1 activity raises SNX30's level | lines that do not express SLC43A1 (9) vs lines expressing it (41) | 1.84× lower at baseline in the lines without SLC43A1 | 0.014 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FZD4]] | B | FZD4 activity raises SNX30's level | lines that do not express FZD4 (9) vs lines expressing it (41) | 1.85× lower at baseline in the lines without FZD4 | 0.017 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MPP1]] | B | MPP1 activity raises SNX30's level | lines that do not express MPP1 (7) vs lines expressing it (43) | 1.33× lower at baseline in the lines without MPP1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ZNF566, ELOVL5, PALM2AKAP2 |
| [[SLC43A1]] | B | SLC43A1 activity weakens SNX30's drug response | lines that do not express SLC43A1 (8) vs lines expressing it (39) | the lines without SLC43A1 respond 1.69× as strongly (z diff -1.37); strongest at Panobinostat 0.5 µM: 1.91x vs 1.36x (z diff -3.0) | 0.045 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[RRAGD]] | B | RRAGD activity raises SNX30's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 1.18× lower at baseline in the lines without RRAGD | 0.061 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |
| [[PSMB5]] | B | PSMB5 activity raises SNX30's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GJA3]] | B | GJA3 activity raises SNX30's level | lines that do not express GJA3 (17) vs lines expressing it (33) | 1.33× lower at baseline in the lines without GJA3 | 0.091 | ⚠ within organs, on part of the lines; also absent: GBX1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SNX30's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers SNX30's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (2.3, -7.1); signed map (-28.8, -5.4). **Vector** length 90.3, 20.5% of its response variance represented; |z| ≥ 3 in 948 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +4.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.8 | +3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.8 | +5.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.7 | +3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +5.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +2.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -4.8 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.2 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -3.5 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -0.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin family member 30 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:112,750,760-112,881,671 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATG24A |
| Gene groups (HGNC) | Sorting nexins; Autophagy related; PX-BAR domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VWJ9](https://www.uniprot.org/uniprotkb/Q5VWJ9) (Sorting nexin-30):

> Involved in the regulation of endocytosis and in several stages of intracellular trafficking. Together with SNX4, involved in autophagosome assembly.

**Summary**, from NCBI Gene [401548](https://www.ncbi.nlm.nih.gov/gene/401548):

> Predicted to enable phosphatidylinositol binding activity. Involved in positive regulation of autophagosome assembly and protein transport. Is active in early endosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23685](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23685) · Entrez [401548](https://www.ncbi.nlm.nih.gov/gene/401548) · UniProt [Q5VWJ9](https://www.uniprot.org/uniprotkb/Q5VWJ9) · Ensembl [ENSG00000148158](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148158)

## Data

Gene col 7247: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7247); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7247, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7247]; `tensor/DDL_lfc|DDL_z.npy` [7247]; `embed/gene_vectors.npy` [7247]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7247 or target_col == 7247). Every well: [[SNX30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
