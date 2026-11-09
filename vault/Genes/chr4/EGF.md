---
symbol: "EGF"
type: "gene"
col: 6244
ensembl_id: "ENSG00000138798"
name: "epidermal growth factor"
location: "4q25"
module: 117
arm: "+"
pooled_cpm: 7.82
n_lines_expressing: 27
n_dd_up: 28
n_dd_down: 10
n_dd_up_clean: 22
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# EGF

*epidermal growth factor* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.43× (z +13.3, q 2e-37, up in 15 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Betamethasone dipropionate (drug)]] 0.5 µM: 0.612× (z -5.2, q 8e-05, down in 13 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPS2]] (+0.72, fdr 7e-06), [[CYP4F11]] (+0.69, fdr 7e-06), [[TLR6]] (+0.67, fdr 7e-06); moves opposite to [[FCHO2]] (-0.50, fdr 3e-05), [[SPATA33]] (-0.49, fdr 5e-05), [[SRD5A1]] (-0.49, fdr 5e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PALLD]] → it (grade B ⚠); 4 go from it, the strongest it → [[SLC10A7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6244.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.43×** | +13.3 | 2e-37 | 15/22 (LS 180, BT-474, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.07×** | +11.2 | 1e-26 | 22/23 (NCI-H1573, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.11×** | +11.1 | 1e-26 | 19/23 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.41×** | +9.3 | 3e-18 | 20/23 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.33×** | +8.9 | 4e-17 | 18/24 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.32×** | +8.9 | 8e-17 | 3/19 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.21×** | +8.1 | 7e-14 | 4/13 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +6.7 | 2e-09 | 17/23 (BT-474, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +5.9 | 2e-07 | 11/22 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.8 | 3e-07 | 2/23 (HEC-1-A, HepG2/C3A) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +5.7 | 5e-07 | 1/17 (RPMI-7951) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +5.3 | 7e-06 | 11/23 (C32, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +5.2 | 1e-05 | 11/24 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.0 | 3e-05 | 10/24 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.76×** | +4.2 | 8e-04 | 7/23 (NCI-H1573, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +4.0 | 0.002 | 10/22 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.30×** | +3.9 | 0.003 | 9/24 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.007 | 11/23 (SK-MEL-2, LS 180, …) | top dose only | cell-cycle shift (explains ~12% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6244.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.612×** | -5.2 | 8e-05 | 13/22 (AN3 CA, NCI-H2347, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.614×** | -5.1 | 8e-05 | 10/24 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.765×** | -4.0 | 0.011 | 14/24 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.770×** | -3.9 | 0.014 | 7/24 (H4, NCI-H2347, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.698×** | -3.8 | 0.017 | 10/24 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.702×** | -3.7 | 0.018 | 4/24 (NCI-H2347, CFPAC-1, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.703×** | -3.6 | 0.028 | 10/23 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.630×** | -3.5 | 0.035 | 3/25 (NCI-H1573, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.738×** | -3.2 | 0.082 | 8/24 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.742×** | -3.1 | 0.093 | 10/23 (H4, HT-29, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.737× | -3.1 | 0.10 | 6/22 (SK-MEL-2, H4, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.749× | -3.1 | 0.11 | 5/24 (NCI-H460, NCI-H661, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.817× | -3.0 | 0.11 | 10/24 (NCI-H661, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6244. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 64.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0570× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -9.8) |
| [[LS 180 (line)]] | wt | 43.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 38.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.23× (z +12.5) | — |
| [[C32 (line)]] | wt | 34.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.75× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 8.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 5.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -11.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.590 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.965 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.982 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.778 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.862 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.751 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.814 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.996 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.872 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.950 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.880 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6244), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPS2]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[CYP4F11]] | +0.69 | +0.59 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[TLR6]] | +0.67 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[PIR]] | +0.65 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[ZSCAN31]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[TDO2]] | +0.64 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[VEGFD]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation; STRING 509 |
| [[TLR1]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[TRIM16L]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[BHMT2]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ALOX12P2-1]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[AKR1C3]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 | pathway: Signaling by Nuclear Receptors |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHO2]] | -0.50 | -0.53 / -0.46 | both halves | 3e-05 | pathway: Cargo recognition for clathrin-mediated endocytosis |
| [[SPATA33]] | -0.49 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[SRD5A1]] | -0.49 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[PACS2]] | -0.46 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[BCL7C]] | -0.46 | -0.46 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PALLD]] | B | PALLD activity raises EGF's level | lines that do not express PALLD (11) vs lines expressing it (39) | 2.99× lower at baseline in the lines without PALLD | 0.031 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, PAG1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers EGF's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01060]] | B | LINC01060 activity raises EGF's level | lines that do not express LINC01060 (29) vs lines expressing it (21) | 2.35× lower at baseline in the lines without LINC01060 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000260289, ENSG00000287598, NTM |
| [[BHMT2]] | C | BHMT2 activity raises EGF's level | lines that do not express BHMT2 (40) vs lines expressing it (10) | 2.02× lower at baseline in the lines without BHMT2 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, LINC01320, CP; co-absent with the target |
| [[CDH7]] | C | CDH7 activity raises EGF's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 2.74× lower at baseline in the lines without CDH7 | 0.048 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC10A7]] | B | EGF activity raises SLC10A7's level | lines that do not express EGF (23) vs lines expressing it (27) | 1.43× lower at baseline in the lines without EGF | 0.021 | ⚠ within organs, on part of the lines; also absent: LNX1, LAMB4, GNAS-AS1 |
| [[PALLD]] | B | EGF activity raises PALLD's level | lines that do not express EGF (23) vs lines expressing it (27) | 2.48× lower at baseline in the lines without EGF | 0.024 | ⚠ within organs, on part of the lines; also absent: LNX1, LAMB4, GNAS-AS1 |
| [[CPA6]] | B | EGF activity raises CPA6's level | lines that do not express EGF (23) vs lines expressing it (27) | 2.08× lower at baseline in the lines without EGF | 0.035 | ⚠ within organs, on part of the lines; also absent: LNX1, LAMB4, GNAS-AS1 |
| [[SLC9A9]] | B | EGF activity raises SLC9A9's level | lines that do not express EGF (23) vs lines expressing it (27) | 1.84× lower at baseline in the lines without EGF | 0.051 | ⚠ within organs, on part of the lines; also absent: LNX1, LAMB4, GNAS-AS1 |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-6.6, 48.2); signed map (50.4, -8.8). **Vector** length 64.8, 15.9% of its response variance represented; |z| ≥ 3 in 673 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *xenobiotic metabolism* (hallmark, mean cos +0.51 to 7); *Synthesis of bile acids and bile salts via 27-hydroxycholesterol* (reactome, mean cos +0.51 to 3); *Synthesis of bile acids and bile salts via 24-hydroxycholesterol* (reactome, mean cos +0.51 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +11.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.9 | +11.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.9 | +9.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.4 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +4.0 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -5.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.8 | -2.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | epidermal growth factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:109,912,883-110,013,766 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | EGF ligand family |
| Hallmark sets | KRAS_SIGNALING_DN, G2M_CHECKPOINT |
| Reactome | 68 pathways, smallest: Developmental Cell Lineages of the Integumentary System; Developmental Lineage of Mammary Gland Luminal Epithelial Cells; Developmental Lineage of Mammary Gland Myoepithelial Cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P01133](https://www.uniprot.org/uniprotkb/P01133) (Pro-epidermal growth factor):

> EGF stimulates the growth of various epidermal and epithelial tissues in vivo and in vitro and of some fibroblasts in cell culture. Magnesiotropic hormone that stimulates magnesium reabsorption in the renal distal convoluted tubule via engagement of EGFR and activation of the magnesium channel TRPM6. Can induce neurite outgrowth in motoneurons of the pond snail Lymnaea stagnalis in vitro.

**Summary**, from NCBI Gene [1950](https://www.ncbi.nlm.nih.gov/gene/1950):

> This gene encodes a member of the epidermal growth factor superfamily. The encoded preproprotein is proteolytically processed to generate the 53-amino acid epidermal growth factor peptide. This protein acts a potent mitogenic factor that plays an important role in the growth, proliferation and differentiation of numerous cell types. This protein acts by binding with high affinity to the cell surface receptor, epidermal growth factor receptor. Defects in this gene are the cause of hypomagnesemia …

**Accessions** — [HGNC:3229](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3229) · Entrez [1950](https://www.ncbi.nlm.nih.gov/gene/1950) · UniProt [P01133](https://www.uniprot.org/uniprotkb/P01133) · Ensembl [ENSG00000138798](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138798)

## Data

Gene col 6244: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6244); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6244, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6244]; `tensor/DDL_lfc|DDL_z.npy` [6244]; `embed/gene_vectors.npy` [6244]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6244 or target_col == 6244). Every well: [[EGF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EGF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
