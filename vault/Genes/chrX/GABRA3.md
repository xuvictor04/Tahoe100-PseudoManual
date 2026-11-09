---
symbol: "GABRA3"
type: "gene"
col: 249
ensembl_id: "ENSG00000011677"
name: "gamma-aminobutyric acid type A receptor subunit alpha3"
location: "Xq28"
module: 108
arm: "+"
pooled_cpm: 11.72
n_lines_expressing: 24
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 27
direction_downstream: 20
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# GABRA3

*gamma-aminobutyric acid type A receptor subunit alpha3* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.16× (z +10.1, q 3e-21, up in 4 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.55× (z +8.8, q 6e-16, up in 4 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.500× (z -9.8, q 6e-20, down in 18 of 22 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAGEA3-DT]] (+0.84, fdr 7e-06), [[LINC01446]] (+0.68, fdr 7e-06), [[LINC01242]] (+0.66, fdr 9e-06); moves opposite to [[PDCD6P1]] (-0.43, fdr 2e-04).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[EPIC1]] → it (grade B ⚠); 20 go from it, the strongest it → [[CSMD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 249.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +10.1 | 3e-21 | 4/18 (SHP-77, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +8.8 | 6e-16 | 4/22 (SHP-77, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +8.2 | 5e-14 | 3/20 (J82, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +7.7 | 2e-12 | 1/12 (SW480) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +5.3 | 2e-05 | 5/22 (J82, SW1417, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.073 | 10/22 (NCI-H23, A-427, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.26× | +3.2 | 0.10 | 0/22 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 249.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.500×** | -9.8 | 6e-20 | 18/22 (NCI-H1573, A-172, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.733×** | -4.4 | 0.003 | 14/22 (A-172, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.713×** | -4.2 | 0.006 | 13/22 (A-427, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.749×** | -4.1 | 0.006 | 9/22 (A-427, H4, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.736×** | -4.0 | 0.007 | 11/20 (A-172, SK-MEL-2, …) | all doses, flat |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.741×** | -3.7 | 0.020 | 10/22 (C32, H4, …) | rises with dose | plate-row cell shift |
| [[Encorafenib (drug)]] 5 µM |  | **0.624×** | -3.5 | 0.040 | 0/22 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.786×** | -3.4 | 0.049 | 10/22 (H4, RPMI-7951, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.5 µM |  | **0.798×** | -3.2 | 0.092 | 3/22 (SK-MEL-2, A-172, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.801×** | -3.1 | 0.097 | 9/22 (H4, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 249. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 51.6 | 1 (1 ⚠) | 7 (5 ⚠) | [[Selinexor (drug)]] 5 µM 2.28× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -20.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0333× (z -14.0) |
| [[H4 (line)]] | wt | 39.7 | 0 | 7 (5 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0748× (z -15.1) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0339× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 57.6 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -13.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 51.0 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0733× (z -20.7) ⚠ toxic; cell-cycle shift, explains ~22% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.320× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 81.7 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0567× (z -23.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -9.7) |
| [[A-172 (line)]] | wt | 24.0 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -11.3) |
| [[HS-578T (line)]] | alt | 43.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -10.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -8.9) |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0402× (z -18.1) ⚠ toxic; cell-cycle shift, explains ~22% of this change |
| [[LOX-IMVI (line)]] | wt | 33.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 38.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -14.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 9.27 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.112× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~22% of this change |
| [[hTERT-HPNE (line)]] | wt | 26.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 249), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGEA3-DT]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[LINC01446]] | +0.68 | +0.74 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[LINC01242]] | +0.66 | +0.65 / +0.57 | both halves | 9e-06 | **novel candidate** |
| [[LINC02616]] | +0.62 | +0.57 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[KC6]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[LINC02267]] | +0.58 | +0.43 / +0.51 | both halves | 3e-05 | **novel candidate** |
| [[JAKMIP2]] | +0.57 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[LINC02377]] | +0.57 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[LINC00648]] | +0.57 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[MIR3171HG]] | +0.56 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[LINC01687]] | +0.56 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[MSC-AS1]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD6P1]] | -0.43 | -0.48 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 2, C 25. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPIC1]] | B | EPIC1 activity raises GABRA3's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 2.92× lower at baseline in the lines without EPIC1 | 0.023 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1 |
| [[CRMP1]] | B | CRMP1 activity raises GABRA3's level | lines that do not express CRMP1 (19) vs lines expressing it (31) | 2.72× lower at baseline in the lines without CRMP1 | 0.074 | ⚠ within organs, on part of the lines; also absent: JAM3, NHSL2, ENSG00000286033; maybe low, not absent |
| [[MAGEA3-DT]] | C | MAGEA3-DT activity raises GABRA3's level | lines that do not express MAGEA3-DT (29) vs lines expressing it (21) | 6.92× lower at baseline in the lines without MAGEA3-DT | 6e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRA3, LINC00648, LINC00470; co-absent with the target |
| [[LINC02616]] | C | LINC02616 activity raises GABRA3's level | lines that do not express LINC02616 (37) vs lines expressing it (13) | 5.90× lower at baseline in the lines without LINC02616 | 1e-03 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, ENSG00000287474, FCRLA; co-absent with the target |
| [[LINC00470]] | C | LINC00470 activity raises GABRA3's level | lines that do not express LINC00470 (38) vs lines expressing it (12) | 7.23× lower at baseline in the lines without LINC00470 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, ENSG00000287474, FCRLA; co-absent with the target |
| [[LINC00648]] | C | LINC00648 activity raises GABRA3's level | lines that do not express LINC00648 (35) vs lines expressing it (15) | 5.62× lower at baseline in the lines without LINC00648 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC00470, ANKRD20A8P, ZIC1; co-absent with the target |
| [[ANKRD20A8P]], [[FAM95A]] | C | ANKRD20A8P, FAM95A activity raises GABRA3's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 5.93× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[MIR548XHG]] | C | MIR548XHG activity raises GABRA3's level | lines that do not express MIR548XHG (38) vs lines expressing it (12) | 5.13× lower at baseline in the lines without MIR548XHG | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000291025, UBBP4-1, COX7B2; co-absent with the target |
| [[MGAT4C]] | C | MGAT4C activity raises GABRA3's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 3.77× lower at baseline in the lines without MGAT4C | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |
| [[LINC01060]] | C | LINC01060 activity raises GABRA3's level | lines that do not express LINC01060 (29) vs lines expressing it (21) | 3.81× lower at baseline in the lines without LINC01060 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000260289, ENSG00000287598, NTM; co-absent with the target |
| [[TPTE]] | C | TPTE activity raises GABRA3's level | lines that do not express TPTE (35) vs lines expressing it (15) | 4.09× lower at baseline in the lines without TPTE | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[LINC01446]] | C | LINC01446 activity raises GABRA3's level | lines that do not express LINC01446 (34) vs lines expressing it (16) | 3.66× lower at baseline in the lines without LINC01446 | 0.020 | ⚠ within organs, on part of the lines; also absent: GABRG2, BAGE2, ENSG00000253363; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 3, C 17. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSMD1]] | B | GABRA3 activity raises CSMD1's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 2.32× lower at baseline in the lines without GABRA3 | 0.046 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4 |
| [[LINC01524]] | B | GABRA3 activity raises LINC01524's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 2.50× lower at baseline in the lines without GABRA3 | 0.072 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4 |
| [[EPIC1]] | B | GABRA3 activity raises EPIC1's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 2.92× lower at baseline in the lines without GABRA3 | 0.081 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4 |
| [[MAGEA3-DT]] | C | GABRA3 activity raises MAGEA3-DT's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 8.47× lower at baseline in the lines without GABRA3 | 1e-04 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4; co-absent with the target |
| [[LRRTM4]] | C | GABRA3 activity raises LRRTM4's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 4.24× lower at baseline in the lines without GABRA3 | 0.001 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4; co-absent with the target |
| [[TPTE]] | C | GABRA3 activity raises TPTE's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 3.77× lower at baseline in the lines without GABRA3 | 0.008 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4; co-absent with the target |
| [[MIR548XHG]] | C | GABRA3 activity raises MIR548XHG's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 2.71× lower at baseline in the lines without GABRA3 | 0.011 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4; co-absent with the target |
| [[LINC02476]] | C | GABRA3 activity raises LINC02476's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 3.83× lower at baseline in the lines without GABRA3 | 0.011 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4; co-absent with the target |
| [[LINC00648]] | C | GABRA3 activity raises LINC00648's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 3.06× lower at baseline in the lines without GABRA3 | 0.013 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4; co-absent with the target |
| [[LINC00470]] | C | GABRA3 activity raises LINC00470's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 5.01× lower at baseline in the lines without GABRA3 | 0.017 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4; co-absent with the target |
| [[ANKRD20A8P]] | C | GABRA3 activity raises ANKRD20A8P's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 2.65× lower at baseline in the lines without GABRA3 | 0.047 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4; co-absent with the target |
| [[CCDC144NL-AS1]] | C | GABRA3 activity raises CCDC144NL-AS1's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 1.68× lower at baseline in the lines without GABRA3 | 0.048 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.775). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.4, 25.5); signed map (32.8, 43.7). **Vector** length 60.3, 15.6% of its response variance represented; |z| ≥ 3 in 504 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +5.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.0 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +0.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | -0.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.2 | -9.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.5 | -1.4 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -1.1 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +0.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.4 | -3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | gamma-aminobutyric acid type A receptor subunit alpha3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:152,166,234-152,451,315 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Gamma-aminobutyric acid type A receptor subunits; MicroRNA protein coding host genes |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 4 pathways, smallest: GABA receptor activation; Neurotransmitter receptors and postsynaptic signal transmission; Transmission across Chemical Synapses |
| Matched by | ensembl_id |

**Function**, from UniProt [P34903](https://www.uniprot.org/uniprotkb/P34903) (Gamma-aminobutyric acid receptor subunit alpha-3):

> Alpha subunit of the heteropentameric ligand-gated chloride channel gated by gamma-aminobutyric acid (GABA), a major inhibitory neurotransmitter in the brain. GABA-gated chloride channels, also named GABA(A) receptors (GABAAR), consist of five subunits arranged around a central pore and contain GABA active binding site(s) located at the alpha and beta subunit interface(s) (By similarity). When activated by GABA, GABAARs selectively allow the flow of chloride anions across the cell membrane down …

**Summary**, from NCBI Gene [2556](https://www.ncbi.nlm.nih.gov/gene/2556):

> GABA is the major inhibitory neurotransmitter in the mammalian brain where it acts at GABA-A receptors, which are ligand-gated chloride channels. Chloride conductance of these channels can be modulated by agents such as benzodiazepines that bind to the GABA-A receptor. At least 16 distinct subunits of GABA-A receptors have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4077](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4077) · Entrez [2556](https://www.ncbi.nlm.nih.gov/gene/2556) · UniProt [P34903](https://www.uniprot.org/uniprotkb/P34903) · Ensembl [ENSG00000011677](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011677)

## Data

Gene col 249: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 249); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 249, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 249]; `tensor/DDL_lfc|DDL_z.npy` [249]; `embed/gene_vectors.npy` [249]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 249 or target_col == 249). Every well: [[GABRA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GABRA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
