---
symbol: "KPNA7"
type: "gene"
col: 11680
ensembl_id: "ENSG00000185467"
name: "karyopherin subunit alpha 7"
location: "7q22.1"
module: 31
arm: "+"
pooled_cpm: 8.54
n_lines_expressing: 40
n_dd_up: 22
n_dd_down: 10
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 36
direction_downstream: 31
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# KPNA7

*karyopherin subunit alpha 7* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.14× (z +13.5, q 6e-39, up in 7 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.01× (z +12.2, q 2e-31, up in 21 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.456× (z -9.7, q 3e-19, down in 23 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO5B]] (+0.66, fdr 7e-06), [[ADGRF4]] (+0.62, fdr 1e-05), [[ARHGAP30]] (+0.62, fdr 1e-05); moves opposite to [[ANGEL1]] (-0.45, fdr 2e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 36 arrows point to it, the strongest [[CDH1]] → it (grade B ⚠); 31 go from it, the strongest it → [[ABTB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11680.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.14×** | +13.5 | 6e-39 | 7/12 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +12.2 | 2e-31 | 21/32 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +10.8 | 8e-25 | 22/37 (KATO III, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +9.4 | 1e-18 | 12/22 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +8.8 | 2e-16 | 4/15 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.84×** | +7.5 | 6e-12 | 21/35 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.72×** | +6.7 | 2e-09 | 15/37 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +6.3 | 2e-08 | 15/35 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +5.3 | 8e-06 | 9/31 (C32, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +5.0 | 3e-05 | 8/31 (HOP62, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +4.6 | 2e-04 | 12/34 (HOP62, AsPC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.6 | 2e-04 | 11/22 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.7 | 0.011 | 5/20 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.73×** | +3.5 | 0.016 | 11/24 (NCI-H2347, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.016 | 5/32 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.021 | 10/36 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.031 | 5/36 (KATO III, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.041 | 5/38 (SW480, PANC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.045 | 4/27 (A498, Hs 766T, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.077 | 0/27 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11680.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.456×** | -9.7 | 3e-19 | 23/37 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.566×** | -6.4 | 3e-08 | 19/35 (COLO 205, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.659×** | -5.1 | 5e-05 | 15/28 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.662×** | -5.1 | 6e-05 | 17/34 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.664×** | -4.6 | 4e-04 | 12/33 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.678×** | -4.6 | 4e-04 | 13/33 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.690×** | -4.2 | 0.002 | 14/35 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.736×** | -3.5 | 0.032 | 9/35 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.754×** | -3.5 | 0.032 | 11/37 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.763×** | -3.3 | 0.050 | 9/35 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.779× | -3.1 | 0.11 | 10/35 (C32, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11680. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 29.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -20.5) |
| [[CFPAC-1 (line)]] | alt | 22.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 49.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0497× (z -15.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 41.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.59× (z +10.7) | — |
| [[KATO III (line)]] | alt | 25.1 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.83× (z +10.2) | — |
| [[LoVo (line)]] | wt | 14.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0558× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0799× (z -11.4) |
| [[A-172 (line)]] | wt | 3.35 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 0.05 µM 0.0623× (z -9.1) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 5.37 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0796× (z -8.9) |
| [[COLO 205 (line)]] | alt | 25.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0479× (z -11.1) |
| [[HT-29 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0414× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 36.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -10.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 7.57 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0708× (z -13.3) |
| [[SNU-423 (line)]] | alt | 4.03 | 0 | 1 | — | [[5-Fluorouracil (drug)]] 0.05 µM 0.0607× (z -9.4) |
| [[A-427 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11680), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO5B]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[ADGRF4]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[ARHGAP30]] | +0.62 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[TRPV3]] | +0.61 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[ATG9B]] | +0.60 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[MROH3P]] | +0.59 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[NECTIN4]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[DHDH]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[PROSER2-AS1]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[CLDN4]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SLC35F4]] | +0.57 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[GP6]] | +0.57 | +0.62 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANGEL1]] | -0.45 | -0.47 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 35, C 1. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDH1]] | B | CDH1 activity raises KPNA7's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 3.80× lower at baseline in the lines without CDH1 | 5e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises KPNA7's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.43× lower at baseline in the lines without TMPRSS4 | 8e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[MROH3P]] | B | MROH3P activity raises KPNA7's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 3.47× lower at baseline in the lines without MROH3P | 1e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[IRF6]] | B | IRF6 activity raises KPNA7's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 3.14× lower at baseline in the lines without IRF6 | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[RNF39]] | B | RNF39 activity raises KPNA7's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 3.41× lower at baseline in the lines without RNF39 | 3e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[IL1RN]] | B | IL1RN activity raises KPNA7's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 2.93× lower at baseline in the lines without IL1RN | 6e-04 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[FAM83B]] | B | FAM83B activity raises KPNA7's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 2.64× lower at baseline in the lines without FAM83B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[RNF223]] | B | RNF223 activity raises KPNA7's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 3.20× lower at baseline in the lines without RNF223 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2 |
| [[MYO5B]] | B | MYO5B activity raises KPNA7's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 2.85× lower at baseline in the lines without MYO5B | 0.001 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[DAPP1]] | B | DAPP1 activity raises KPNA7's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 3.73× lower at baseline in the lines without DAPP1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[SULT2B1]] | B | SULT2B1 activity raises KPNA7's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 2.62× lower at baseline in the lines without SULT2B1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[CLDN4]] | B | CLDN4 activity raises KPNA7's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 3.04× lower at baseline in the lines without CLDN4 | 0.003 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 31, C 0. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABTB2]] | B | KPNA7 activity raises ABTB2's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 2.68× lower at baseline in the lines without KPNA7 | 0.006 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[UBE2H]] | B | KPNA7 activity raises UBE2H's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 1.80× lower at baseline in the lines without KPNA7 | 0.022 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[BARX2]] | B | KPNA7 activity raises BARX2's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 3.98× lower at baseline in the lines without KPNA7 | 0.025 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[CBR3-AS1]] | B | KPNA7 activity raises CBR3-AS1's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 2.24× lower at baseline in the lines without KPNA7 | 0.025 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[CLDN4]] | B | KPNA7 activity raises CLDN4's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 4.12× lower at baseline in the lines without KPNA7 | 0.025 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[ATG9B]] | B | KPNA7 activity raises ATG9B's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 2.49× lower at baseline in the lines without KPNA7 | 0.031 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[WFDC3]] | B | KPNA7 activity raises WFDC3's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 2.44× lower at baseline in the lines without KPNA7 | 0.033 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[LSMEM2]] | B | KPNA7 activity raises LSMEM2's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 2.04× lower at baseline in the lines without KPNA7 | 0.034 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[CDH1]] | B | KPNA7 activity raises CDH1's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 4.65× lower at baseline in the lines without KPNA7 | 0.037 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[RNF103-CHMP3]] | B | KPNA7 activity raises RNF103-CHMP3's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 2.54× lower at baseline in the lines without KPNA7 | 0.042 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[SEMA3B]] | B | KPNA7 activity raises SEMA3B's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 2.86× lower at baseline in the lines without KPNA7 | 0.048 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[DYSF]] | B | KPNA7 activity raises DYSF's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 1.88× lower at baseline in the lines without KPNA7 | 0.051 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.438). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.8, 58.4); signed map (55.5, 7.1). **Vector** length 80.5, 17.1% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +13.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +3.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.9 | -9.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -4.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.5 | -5.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -3.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | karyopherin subunit alpha 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:99,173,572-99,250,075 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IPOA8 |
| Gene groups (HGNC) | Armadillo repeat containing; Importins |
| Reactome | 10 pathways, smallest: NS1 Mediated Effects on Host Pathways; Maturation of DENV proteins; ISG15 antiviral mechanism |
| Matched by | ensembl_id |

**Function**, from UniProt [A9QM74](https://www.uniprot.org/uniprotkb/A9QM74) (Importin subunit alpha-8):

> Functions in nuclear protein import.

**Summary**, from NCBI Gene [402569](https://www.ncbi.nlm.nih.gov/gene/402569):

> The transport of molecules between the nucleus and the cytoplasm in eukaryotic cells is mediated by the nuclear pore complex (NPC), which consists of 60-100 proteins. Small molecules (up to 70 kD) can pass through the nuclear pore by nonselective diffusion while larger molecules are transported by an active process. The protein encoded by this gene belongs to the importin alpha family, and is involved in nuclear protein import, but exhibits different nuclear localization signal binding …

**Accessions** — [HGNC:21839](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21839) · Entrez [402569](https://www.ncbi.nlm.nih.gov/gene/402569) · UniProt [A9QM74](https://www.uniprot.org/uniprotkb/A9QM74) · Ensembl [ENSG00000185467](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185467)

## Data

Gene col 11680: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11680); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11680, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11680]; `tensor/DDL_lfc|DDL_z.npy` [11680]; `embed/gene_vectors.npy` [11680]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11680 or target_col == 11680). Every well: [[KPNA7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KPNA7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
