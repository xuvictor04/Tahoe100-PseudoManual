---
symbol: "ZC3H12A"
type: "gene"
col: 8798
ensembl_id: "ENSG00000163874"
name: "zinc finger CCCH-type containing 12A"
location: "1p34.3"
module: 14
arm: "+"
pooled_cpm: 21.9
n_lines_expressing: 45
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 26
direction_downstream: 24
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# ZC3H12A

*zinc finger CCCH-type containing 12A* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.96× (z +27.0, q 0e+00, up in 42 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.643× (z -5.3, q 6e-05, down in 27 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFAIP3]] (+0.75, fdr 7e-06), [[SOCS3]] (+0.72, fdr 7e-06), [[NFKBIA]] (+0.71, fdr 7e-06); moves opposite to [[VKORC1L1]] (-0.50, fdr 3e-05), [[COG5]] (-0.50, fdr 2e-05), [[DIP2A]] (-0.50, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[C3]] → it (grade B ⚠); 24 go from it, the strongest it → [[EPAS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8798.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.96×** | +27.0 | 0e+00 | 42/42 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.94×** | +15.7 | 0e+00 | 41/42 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.71×** | +15.6 | 0e+00 | 37/42 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.08×** | +8.7 | 4e-16 | 30/42 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.66×** | +8.1 | 7e-14 | 34/43 (PANC-1, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.95×** | +7.9 | 2e-13 | 30/43 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +7.9 | 2e-13 | 31/38 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +7.5 | 4e-12 | 29/43 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +6.5 | 5e-09 | 23/41 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +6.3 | 2e-08 | 31/43 (HEC-1-A, Hs 766T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.63×** | +5.4 | 4e-06 | 13/31 (J82, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.36×** | +5.3 | 4e-06 | 23/41 (HS-578T, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +5.1 | 1e-05 | 25/42 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.43×** | +4.3 | 8e-04 | 20/42 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.39×** | +3.9 | 0.004 | 17/43 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.010 | 20/43 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.024 | 17/43 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Pemigatinib (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.053 | 4/41 (HS-578T, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8798.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.643×** | -5.3 | 6e-05 | 27/42 (HT-29, LoVo, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.440×** | -5.2 | 7e-05 | 26/40 (CFPAC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.740×** | -3.6 | 0.050 | 18/43 (SNU-423, SW 900, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.751×** | -3.5 | 0.077 | 17/42 (SK-MEL-2, RPMI-7951, …) | rises with dose |  |
| [[Sulfisoxazole (drug)]] 5 µM |  | 0.828× | -3.2 | 0.13 | 16/43 (NCI-H460, SW 900, …) | inconsistent across doses | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.774× | -3.1 | 0.16 | 15/42 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.836× | -3.1 | 0.16 | 16/43 (MIA PaCa-2, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8798. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 44.5 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.72× (z +23.2) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 31.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +21.7) | — |
| [[NCI-H460 (line)]] | wt | 17.5 | 5 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 5.68× (z +11.4) | — |
| [[AsPC-1 (line)]] | alt | 20.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +23.7) | — |
| [[HEC-1-A (line)]] | alt | 20.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +15.7) | — |
| [[hTERT-HPNE (line)]] | wt | 20.6 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +19.1) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0696× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 55.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.17× (z +21.2) | — |
| [[HOP62 (line)]] | alt | 31.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.52× (z +15.6) | — |
| [[J82 (line)]] | alt | 28.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +16.3) | — |
| [[NCI-H2347 (line)]] | alt | 22.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 19.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +17.0) | — |
| [[PANC-1 (line)]] | alt | 11.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +23.3) | — |
| [[SW 900 (line)]] | alt | 34.5 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +11.6) | [[Auranofin (drug)]] 5 µM 0.209× (z -9.3) |
| [[A-172 (line)]] | wt | 9.37 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +12.4) | — |
| [[A549 (line)]] | wt | 50.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +12.4) | — |
| [[BT-474 (line)]] | alt | 27.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +13.3) | — |
| [[COLO 205 (line)]] | alt | 48.7 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.76× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 50.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +15.7) | — |
| [[LoVo (line)]] | wt | 12.3 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 7.18× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 24.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +14.3) | — |
| [[RPMI-7951 (line)]] | alt | 21.5 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 10.4× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 42.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +16.0) | [[Auranofin (drug)]] 5 µM 0.270× (z -8.5) |
| [[C32 (line)]] | wt | 8.47 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0788× (z -8.8) |
| [[H4 (line)]] | wt | 21.6 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0803× (z -10.6) |
| [[HCT15 (line)]] | alt | 13.7 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0743× (z -9.3) |
| [[Hs 766T (line)]] | wt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 44.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +9.1) | — |
| [[KATO III (line)]] | alt | 8.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +13.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 13.6 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.68× (z +8.9) ⚠ position not correctable | — |
| [[NCI-H1573 (line)]] | alt | 43.1 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.90× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 8.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +11.9) | — |
| [[SW1417 (line)]] | alt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +10.4) | — |
| [[SW48 (line)]] | wt | 20.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.74× (z +10.8) | — |
| [[A-427 (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.37 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8798), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFAIP3]] | +0.75 | +0.68 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 708 |
| [[SOCS3]] | +0.72 | +0.71 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NFKBIA]] | +0.71 | +0.67 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 530 |
| [[ZFP36]] | +0.70 | +0.72 / +0.71 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 644 |
| [[BCL9L]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[BCL3]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 617 |
| [[EBI3]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[SBNO2]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[SOD2]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[C3]] | +0.63 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[NFKBIE]] | +0.63 | +0.65 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TIPARP]] | +0.62 | +0.54 / +0.67 | both halves | 1e-05 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VKORC1L1]] | -0.50 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[COG5]] | -0.50 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[DIP2A]] | -0.50 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[VPS53]] | -0.49 | -0.40 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 23, C 3. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C3]] | B | C3 activity raises ZC3H12A's level | lines that do not express C3 (32) vs lines expressing it (18) | 2.66× lower at baseline in the lines without C3 | 0.002 | ⚠ within organs, on part of the lines; also absent: TNFSF14, CP, CARD11 |
| [[CCL20]] | B | CCL20 activity raises ZC3H12A's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 2.17× lower at baseline in the lines without CCL20 | 0.003 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[TNFSF14]] | B | TNFSF14 activity raises ZC3H12A's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 2.60× lower at baseline in the lines without TNFSF14 | 0.007 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[CSF3]] | B | CSF3 activity raises ZC3H12A's level | lines that do not express CSF3 (27) vs lines expressing it (23) | 2.26× lower at baseline in the lines without CSF3 | 0.008 | ⚠ within organs, on part of the lines; also absent: CCBE1, LOX, RRAD |
| [[CXCL2]] | B | CXCL2 activity raises ZC3H12A's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 2.41× lower at baseline in the lines without CXCL2 | 0.008 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[EREG]] | B | EREG activity raises ZC3H12A's level | lines that do not express EREG (26) vs lines expressing it (24) | 1.66× lower at baseline in the lines without EREG | 0.009 | ⚠ within organs, on part of the lines; also absent: DPP4, IL20RA, HS3ST1 |
| [[SAA2-SAA4]], [[SAA4]] | B | SAA2-SAA4, SAA4 activity raises ZC3H12A's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 2.38× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.012 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[RHCG]] | B | RHCG activity raises ZC3H12A's level | lines that do not express RHCG (33) vs lines expressing it (17) | 1.77× lower at baseline in the lines without RHCG | 0.015 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[EPAS1]] | B | EPAS1 activity raises ZC3H12A's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 2.61× lower at baseline in the lines without EPAS1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[LINC02015]] | B | LINC02015 activity raises ZC3H12A's level | lines that do not express LINC02015 (27) vs lines expressing it (23) | 1.90× lower at baseline in the lines without LINC02015 | 0.022 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, CRLF2, PXDN |
| [[ETS2]] | B | ETS2 activity raises ZC3H12A's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 2.53× lower at baseline in the lines without ETS2 | 0.027 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[SAA2]] | B | SAA2 activity raises ZC3H12A's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 2.39× lower at baseline in the lines without SAA2 | 0.029 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3 |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 21, C 3. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPAS1]] | B | ZC3H12A activity raises EPAS1's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 4.99× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[CXCL1]] | B | ZC3H12A activity raises CXCL1's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 4.16× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[TNFAIP3]] | B | ZC3H12A activity raises TNFAIP3's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 3.41× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[SQOR]] | B | ZC3H12A activity raises SQOR's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 3.16× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[CXCL2]] | B | ZC3H12A activity raises CXCL2's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 2.83× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[TNKS1BP1]] | B | ZC3H12A activity raises TNKS1BP1's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 2.56× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[TNIP1]] | B | ZC3H12A activity raises TNIP1's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 2.50× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[CSRNP1]] | B | ZC3H12A activity raises CSRNP1's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 2.32× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[SBNO2]] | B | ZC3H12A activity raises SBNO2's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 1.94× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[MOB3C]] | B | ZC3H12A activity raises MOB3C's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 1.93× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[JAK1]] | B | ZC3H12A activity raises JAK1's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 1.88× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[TANK]] | B | ZC3H12A activity raises TANK's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 1.84× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.2, 8.3); signed map (11.5, 28.7). **Vector** length 112, 29.8% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NF-kB* (control, mean cos +0.55 to 12); *IkBA variant leads to EDA-ID* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.3 | +15.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +27.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.9 | +5.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.2 | +7.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.0 | +1.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.6 | +1.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.6 | +0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.5 | +1.3 |
| fall | [[NG25 (drug)]] 5 µM |  | -4.5 | -5.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.6 | -3.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.3 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -5.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCCH-type containing 12A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:37,474,580-37,484,377 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23231, MCPIP1, Regnase-1 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; MicroRNA protein coding host genes |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 7 pathways, smallest: Regulation of CDH19 Expression and Function; Regulation of Expression and Function of Type II Classical Cadherins; Regulation of Homotypic Cell-Cell Adhesion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5D1E8](https://www.uniprot.org/uniprotkb/Q5D1E8) (Endoribonuclease ZC3H12A):

> Endoribonuclease involved in various biological functions such as cellular inflammatory response and immune homeostasis, glial differentiation of neuroprogenitor cells, cell death of cardiomyocytes, adipogenesis and angiogenesis. Functions as an endoribonuclease involved in mRNA decay. Modulates the inflammatory response by promoting the degradation of a set of translationally active cytokine-induced inflammation-related mRNAs, such as IL6 and IL12B, during the early phase of inflammation. …

**Summary**, from NCBI Gene [80149](https://www.ncbi.nlm.nih.gov/gene/80149):

> ZC3H12A is an MCP1 (CCL2; MIM 158105)-induced protein that acts as a transcriptional activator and causes cell death of cardiomyocytes, possibly via induction of genes associated with apoptosis.[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:26259](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26259) · Entrez [80149](https://www.ncbi.nlm.nih.gov/gene/80149) · UniProt [Q5D1E8](https://www.uniprot.org/uniprotkb/Q5D1E8) · Ensembl [ENSG00000163874](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163874)

## Data

Gene col 8798: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8798); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8798, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8798]; `tensor/DDL_lfc|DDL_z.npy` [8798]; `embed/gene_vectors.npy` [8798]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8798 or target_col == 8798). Every well: [[ZC3H12A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZC3H12A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
