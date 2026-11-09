---
symbol: "AADACP1"
type: "gene"
col: 14243
ensembl_id: "ENSG00000240602"
name: "arylacetamide deacetylase pseudogene 1"
location: "3q25.1"
module: 81
arm: "+"
pooled_cpm: 83.46
n_lines_expressing: 18
n_dd_up: 1
n_dd_down: 33
n_dd_up_clean: 0
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 11
direction_downstream: 16
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# AADACP1

*arylacetamide deacetylase pseudogene 1* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.75× (z +4.1, q 0.020, up in 1 of 17 measured lines) ⚠ toxic; transcription drop.
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.545× (z -6.4, q 1e-07, down in 11 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AADAC]] (+0.88, fdr 7e-06, ⚠ same locus), [[GJA1]] (+0.71, fdr 7e-06), [[FAM107B]] (+0.70, fdr 7e-06), [[SERPIND1]] (+0.70, fdr 1e-05); moves opposite to [[STOM]] (-0.58, fdr 1e-05), [[EDN2]] (-0.57, fdr 1e-05), [[FLVCR2]] (-0.53, fdr 1e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[RAI14]] → it (grade B ⚠); 16 go from it, the strongest it → [[AADACL2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14243.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +4.1 | 0.020 | 1/17 (NCI-H2122) | inconsistent across doses | cell-cycle shift (explains ~16% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, none with an alert; shown: the 15 strongest. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14243.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.545×** | -6.4 | 1e-07 | 11/16 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.430×** | -6.3 | 1e-07 | 15/16 (Panc 03.27, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.413×** | -6.1 | 2e-07 | 13/16 (NCI-H2030, SK-MEL-2, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.494×** | -5.2 | 2e-05 | 13/16 (NCI-H2030, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.496×** | -5.2 | 2e-05 | 15/16 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.498×** | -5.0 | 6e-05 | 10/16 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.513×** | -4.9 | 6e-05 | 12/16 (NCI-H460, A498, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.627×** | -4.8 | 1e-04 | 12/16 (NCI-H2030, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.544×** | -4.4 | 8e-04 | 12/17 (NCI-H2030, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.565×** | -4.2 | 0.001 | 12/16 (A498, SW 900, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.566×** | -4.2 | 0.001 | 14/16 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.581×** | -4.0 | 0.003 | 13/16 (A498, SW 900, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.584×** | -4.0 | 0.003 | 11/16 (A498, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Anethole trithione (drug)]] 5 µM |  | **0.685×** | -4.0 | 0.003 | 10/16 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.565×** | -3.9 | 0.003 | 11/15 (A498, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14243. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 262 | 0 | 16 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.284× (z -19.0) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0872× (z -14.7) |
| [[A498 (line)]] | wt | 58.0 | 0 | 13 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Betamethasone dipropionate (drug)]] 0.05 µM 0.177× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 328 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0964× (z -21.2) |
| [[NCI-H1792 (line)]] | alt | 759 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0343× (z -23.9) |
| [[A549 (line)]] | wt | 684 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -15.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.235× (z -12.1) |
| [[SW 900 (line)]] | alt | 95.2 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -13.1) |
| [[H4 (line)]] | wt | 179 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0969× (z -13.5) |
| [[A-172 (line)]] | wt | 104 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0824× (z -15.5) |
| [[AsPC-1 (line)]] | alt | 188 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0260× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[Panc 03.27 (line)]] | alt | 168 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.108× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 28.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -13.1) |
| [[CFPAC-1 (line)]] | alt | 208 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.143× (z -8.7) |
| [[KATO III (line)]] | alt | 52.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -9.4) |
| [[A-427 (line)]] | wt | 5.14 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.63 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.43 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.59 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.34 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.85 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.95 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.26 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 15.6 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 14.4 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.00 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.55 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.25 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.89 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 86.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.25 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.50 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.18 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.81 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 18.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.94 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.19 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.49 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14243), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AADAC]] | +0.88 | +0.89 / +0.87 | both halves | 7e-06 | ⚠ same locus (29.7 kb, same strand: neighbours can correlate without regulation) |
| [[GJA1]] | +0.71 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[FAM107B]] | +0.70 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[SERPIND1]] | +0.70 | +0.57 / +0.74 | both halves | 1e-05 | **novel candidate** |
| [[MMP1]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[IL1B]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[ITGA2]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[MARCHF3]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SLC35F3]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[CRLF2]] | +0.61 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[TM4SF1]] | +0.60 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[TMEM158]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[SEMA3A]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STOM]] | -0.58 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[EDN2]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[FLVCR2]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[MIRLET7BHG]] | -0.51 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ACSL1]] | -0.49 | -0.45 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 6, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAI14]] | B | RAI14 activity raises AADACP1's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 3.90× lower at baseline in the lines without RAI14 | 0.067 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[SERPIND1]] | B | SERPIND1 activity raises AADACP1's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 2.18× lower at baseline in the lines without SERPIND1 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[S100A16]] | B | S100A16 activity raises AADACP1's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 2.63× lower at baseline in the lines without S100A16 | 0.094 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[FAM107B]] | B | FAM107B activity raises AADACP1's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 3.03× lower at baseline in the lines without FAM107B | 0.097 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[CD44]] | B | CD44 activity raises AADACP1's level | lines that do not express CD44 (15) vs lines expressing it (35) | 3.52× lower at baseline in the lines without CD44 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[MAP2K1]] | B | MAP2K1 activity raises AADACP1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[AADAC]] | C | AADAC activity raises AADACP1's level | lines that do not express AADAC (34) vs lines expressing it (16) | 15.66× lower at baseline in the lines without AADAC | 2e-05 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610; co-absent with the target |
| [[GCKR]] | C | GCKR activity raises AADACP1's level | lines that do not express GCKR (24) vs lines expressing it (26) | 4.58× lower at baseline in the lines without GCKR | 0.015 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent; co-absent with the target |
| [[IGFBP3]] | C | IGFBP3 activity raises AADACP1's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 4.00× lower at baseline in the lines without IGFBP3 | 0.020 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF; co-absent with the target |
| [[ANXA10]] | C | ANXA10 activity raises AADACP1's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 4.34× lower at baseline in the lines without ANXA10 | 0.068 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP; co-absent with the target |
| [[CA2]] | C | CA2 activity raises AADACP1's level | lines that do not express CA2 (27) vs lines expressing it (23) | 2.65× lower at baseline in the lines without CA2 | 0.069 | ⚠ within organs, on part of the lines; also absent: CCDC68, SCEL, MUC4; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 8, C 8. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AADACL2-AS1]] | B | AADACP1 activity raises AADACL2-AS1's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 1.78× lower at baseline in the lines without AADACP1 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1 |
| [[FAM107B]] | B | AADACP1 activity raises FAM107B's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 3.08× lower at baseline in the lines without AADACP1 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1 |
| [[WNT7B]] | B | AADACP1 activity raises WNT7B's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 2.43× lower at baseline in the lines without AADACP1 | 0.025 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1 |
| [[MARCHF3]] | B | AADACP1 activity raises MARCHF3's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 1.77× lower at baseline in the lines without AADACP1 | 0.044 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1 |
| [[RGS2]] | B | AADACP1 activity raises RGS2's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 2.01× lower at baseline in the lines without AADACP1 | 0.082 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1 |
| [[NHS]] | B | AADACP1 activity raises NHS's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 2.84× lower at baseline in the lines without AADACP1 | 0.085 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1 |
| [[GABRE]] | B | AADACP1 activity raises GABRE's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 2.19× lower at baseline in the lines without AADACP1 | 0.088 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1 |
| [[S100A16]] | B | AADACP1 activity raises S100A16's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 1.60× lower at baseline in the lines without AADACP1 | 0.091 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1 |
| [[AADAC]] | C | AADACP1 activity raises AADAC's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 7.63× lower at baseline in the lines without AADACP1 | 3e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1; co-absent with the target |
| [[GCKR]] | C | AADACP1 activity raises GCKR's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 1.43× lower at baseline in the lines without AADACP1 | 0.041 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1; co-absent with the target |
| [[CA2]] | C | AADACP1 activity raises CA2's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 2.70× lower at baseline in the lines without AADACP1 | 0.048 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1; co-absent with the target |
| [[CRTAC1]] | C | AADACP1 activity raises CRTAC1's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 2.66× lower at baseline in the lines without AADACP1 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1; co-absent with the target |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.772). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.6, 15.7); signed map (18.9, 52.6). **Vector** length 93.9, 34.0% of its response variance represented; |z| ≥ 3 in 786 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *KRAS signaling up* (hallmark, mean cos +0.56 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +0.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +0.5 |
|  | [[Thymol (drug)]] 5 µM |  | +1.5 | +1.9 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.5 | -6.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.3 | -4.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.3 | -4.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.2 | -4.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.1 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | arylacetamide deacetylase pseudogene 1 |
| Locus type | pseudogene |
| Location | 3q25.1 — chr3:151,770,474-151,784,421 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50305) · Entrez [201651](https://www.ncbi.nlm.nih.gov/gene/201651) · Ensembl [ENSG00000240602](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240602)

## Data

Gene col 14243: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14243); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14243, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14243]; `tensor/DDL_lfc|DDL_z.npy` [14243]; `embed/gene_vectors.npy` [14243]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14243 or target_col == 14243). Every well: [[AADACP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AADACP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
