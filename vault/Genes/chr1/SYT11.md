---
symbol: "SYT11"
type: "gene"
col: 5364
ensembl_id: "ENSG00000132718"
name: "synaptotagmin 11"
location: "1q22"
module: 82
arm: "+"
pooled_cpm: 8.35
n_lines_expressing: 25
n_dd_up: 32
n_dd_down: 8
n_dd_up_clean: 24
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 11
direction_downstream: 15
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# SYT11

*synaptotagmin 11* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 25.9× (z +38.8, q 0e+00, up in 23 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.666× (z -4.9, q 7e-04, down in 12 of 22 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOVA2]] (+0.67, fdr 7e-06), [[ZMAT4]] (+0.63, fdr 1e-05), [[TMEM108]] (+0.61, fdr 1e-05); moves opposite to [[MSANTD2]] (-0.59, fdr 8e-05), [[ANXA2R-OT1]] (-0.53, fdr 1e-04), [[PRDM5]] (-0.52, fdr 4e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[GAMT]] → it (grade B ⚠); 15 go from it, the strongest it → [[TTLL7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5364.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **25.9×** | +38.8 | 0e+00 | 23/23 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **16.3×** | +33.3 | 0e+00 | 22/23 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **6.16×** | +30.6 | 0e+00 | 23/23 (SW480, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **5.65×** | +20.6 | 0e+00 | 22/22 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.90×** | +16.2 | 0e+00 | 22/23 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.71×** | +11.9 | 2e-30 | 19/23 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.48×** | +10.8 | 2e-25 | 2/17 (SK-MEL-2, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +9.2 | 2e-18 | 6/20 (SW480, C-33 A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +8.0 | 6e-14 | 4/19 (A-172, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +6.7 | 1e-09 | 1/10 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +6.0 | 1e-07 | 0/16 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.36×** | +5.4 | 4e-06 | 8/22 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.74×** | +4.7 | 1e-04 | 2/17 (NCI-H2030, SHP-77) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +4.5 | 3e-04 | 4/22 (C-33 A, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.42×** | +4.2 | 0.001 | 10/23 (C32, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.41×** | +4.1 | 0.001 | 9/22 (SK-MEL-2, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.002 | 2/23 (SW480, hTERT-HPNE) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.002 | 5/21 (A-427, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5364.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.666×** | -4.9 | 7e-04 | 12/22 (PANC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.674×** | -4.7 | 7e-04 | 14/22 (NCI-H2030, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.683×** | -4.6 | 0.001 | 15/22 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.712×** | -4.1 | 0.007 | 5/22 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.723×** | -3.9 | 0.013 | 19/23 (NCI-H23, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -3.5 | 0.044 | 4/23 (SW 900, AN3 CA, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.750×** | -3.4 | 0.048 | 9/23 (PANC-1, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.753×** | -3.4 | 0.050 | 2/22 (SHP-77, NCI-H1792) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.755×** | -3.4 | 0.050 | 14/21 (CHP-212, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5364. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 6.58 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 24.2× (z +17.8) | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -11.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 51.7 | 0 | 4 (2 ⚠) | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0773× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 14.5 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 10.0× (z +13.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.212× (z -9.1) |
| [[SHP-77 (line)]] | alt | 52.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.56× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[CFPAC-1 (line)]] | alt | 3.08 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 22.0× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 4.84 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 17.5× (z +14.1) | — |
| [[A-427 (line)]] | wt | 7.26 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 8.62× (z +8.9) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.127× (z -8.5) |
| [[C-33 A (line)]] | alt | 26.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.85× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 5.59 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 12.2× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 17.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.83× (z +9.6) | — |
| [[A-172 (line)]] | wt | 141 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.83× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 6.02 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.0× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 3.51 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 16.4× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 7.20 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.98× (z +8.5) | — |
| [[A498 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.815 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.842 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.933 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.865 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.814 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.983 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.984 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5364), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOVA2]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[ZMAT4]] | +0.63 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[TMEM108]] | +0.61 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[ARHGAP28]] | +0.61 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[JAKMIP1]] | +0.60 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[GNAO1]] | +0.59 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[MAP6]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[FSD1]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[ATP1A3]] | +0.57 | +0.31 / +0.63 | both halves | 2e-04 |  |
| [[MAPT]] | +0.56 | +0.36 / +0.51 | both halves | 1e-04 | STRING 545 |
| [[KIF5C]] | +0.56 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[GUCY1B1]] | +0.56 | +0.43 / +0.52 | both halves | 3e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |

## Genes that move opposite

*11 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSANTD2]] | -0.59 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[ANXA2R-OT1]] | -0.53 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[PRDM5]] | -0.52 | -0.25 / -0.54 | both halves | 4e-04 |  |
| [[IGF2BP1]] | -0.50 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[NAF1]] | -0.49 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[RAB28]] | -0.49 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[DNAAF10]] | -0.48 | -0.28 / -0.25 | both halves | 4e-04 |  |
| [[EFCAB2]] | -0.48 | -0.05 / -0.54 | ⚠ one half (not replicated) | 0.005 |  |
| [[AVEN]] | -0.47 | -0.15 / -0.45 | ⚠ not reproduced | 0.001 |  |
| [[ACAD9]] | -0.47 | -0.22 / -0.41 | both halves | 6e-04 |  |
| [[TNPO2]] | -0.47 | -0.23 / -0.34 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAMT]] | B | GAMT activity raises SYT11's level | lines that do not express GAMT (11) vs lines expressing it (39) | 3.04× lower at baseline in the lines without GAMT | 0.025 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: HDGFL3, HLTF, EHD3 |
| [[PRDM5]] | B | PRDM5 activity raises SYT11's level | lines that do not express PRDM5 (13) vs lines expressing it (37) | 1.26× lower at baseline in the lines without PRDM5 | 0.082 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| [[ESYT3]] | B | ESYT3 activity raises SYT11's level | lines that do not express ESYT3 (15) vs lines expressing it (35) | 2.00× lower at baseline in the lines without ESYT3 | 0.089 | ⚠ within organs, on part of the lines; also absent: BEND6, ENSG00000224905, ZNF354C; maybe low, not absent |
| [[P2RX7]] | B | P2RX7 activity raises SYT11's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 2.04× lower at baseline in the lines without P2RX7 | 0.091 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |
| [[FSD1]] | C | FSD1 activity raises SYT11's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 3.58× lower at baseline in the lines without FSD1 | 0.005 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2; co-absent with the target |
| [[NFASC]] | C | NFASC activity raises SYT11's level | lines that do not express NFASC (27) vs lines expressing it (23) | 3.38× lower at baseline in the lines without NFASC | 0.009 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A; co-absent with the target |
| [[KIF1A]] | C | KIF1A activity raises SYT11's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 3.18× lower at baseline in the lines without KIF1A | 0.017 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7; co-absent with the target |
| [[LINC01518]] | C | LINC01518 activity raises SYT11's level | lines that do not express LINC01518 (36) vs lines expressing it (14) | 3.63× lower at baseline in the lines without LINC01518 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000285822, CCDC144NL-AS1, PHF2P2; co-absent with the target |
| [[NOVA2]] | C | NOVA2 activity raises SYT11's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 3.75× lower at baseline in the lines without NOVA2 | 0.055 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1; co-absent with the target |
| [[MAP1A]] | C | MAP1A activity raises SYT11's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 3.31× lower at baseline in the lines without MAP1A | 0.081 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent; co-absent with the target |
| [[JAKMIP2]] | C | JAKMIP2 activity raises SYT11's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 2.86× lower at baseline in the lines without JAKMIP2 | 0.092 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 8, C 7. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTLL7]] | B | SYT11 activity raises TTLL7's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 3.41× lower at baseline in the lines without SYT11 | 0.008 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1 |
| [[ADGRA2]] | B | SYT11 activity raises ADGRA2's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 2.23× lower at baseline in the lines without SYT11 | 0.033 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1 |
| [[SYN1]] | B | SYT11 activity raises SYN1's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 1.47× lower at baseline in the lines without SYT11 | 0.036 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1 |
| [[FLNB]] | B | SYT11 activity lowers FLNB's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 1.80× higher at baseline in the lines without SYT11 | 0.037 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1 |
| [[EFCAB2]] | B | SYT11 activity raises EFCAB2's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 1.36× lower at baseline in the lines without SYT11 | 0.061 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1 |
| [[HSPA2]] | B | SYT11 activity raises HSPA2's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 2.06× lower at baseline in the lines without SYT11 | 0.081 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1 |
| [[TUBB2B]] | B | SYT11 activity raises TUBB2B's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 2.55× lower at baseline in the lines without SYT11 | 0.084 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1 |
| [[TMEFF2]] | B | SYT11 activity raises TMEFF2's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 1.67× lower at baseline in the lines without SYT11 | 0.097 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1 |
| [[MAP1A]] | C | SYT11 activity raises MAP1A's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 3.64× lower at baseline in the lines without SYT11 | 0.013 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1; co-absent with the target |
| [[FSD1]] | C | SYT11 activity raises FSD1's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 2.87× lower at baseline in the lines without SYT11 | 0.018 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1; co-absent with the target |
| [[NFASC]] | C | SYT11 activity raises NFASC's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 3.62× lower at baseline in the lines without SYT11 | 0.033 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1; co-absent with the target |
| [[GNAO1]] | C | SYT11 activity raises GNAO1's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 2.77× lower at baseline in the lines without SYT11 | 0.044 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.690). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.8, 31.0); signed map (33.9, 33.5). **Vector** length 48.3, 9.39% of its response variance represented; |z| ≥ 3 in 598 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +30.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +16.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +33.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +5.4 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.6 | -4.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.7 | -4.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.3 | -3.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.0 | -0.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | synaptotagmin 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,859,567-155,885,199 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0080, MGC10881, MGC17226, DKFZp781D015 |
| Gene groups (HGNC) | Synaptotagmins |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 4 pathways, smallest: Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BT88](https://www.uniprot.org/uniprotkb/Q9BT88) (Synaptotagmin-11):

> Synaptotagmin family member involved in vesicular and membrane trafficking which does not bind Ca(2+). Inhibits clathrin-mediated and bulk endocytosis, functions to ensure precision in vesicle retrieval. Plays an important role in dopamine transmission by regulating endocytosis and the vesicle-recycling process. Essential component of a neuronal vesicular trafficking pathway that differs from the synaptic vesicle trafficking pathway but is crucial for development and synaptic plasticity. In …

**Summary**, from NCBI Gene [23208](https://www.ncbi.nlm.nih.gov/gene/23208):

> This gene is a member of the synaptotagmin gene family and encodes a protein similar to other family members that are known calcium sensors and mediate calcium-dependent regulation of membrane trafficking in synaptic transmission. The encoded protein is also a substrate for ubiquitin-E3-ligase parkin. The gene has previously been referred to as synaptotagmin XII but has been renamed synaptotagmin XI to be consistent with mouse and rat official nomenclature. [provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:19239](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19239) · Entrez [23208](https://www.ncbi.nlm.nih.gov/gene/23208) · UniProt [Q9BT88](https://www.uniprot.org/uniprotkb/Q9BT88) · Ensembl [ENSG00000132718](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132718)

## Data

Gene col 5364: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5364); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5364, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5364]; `tensor/DDL_lfc|DDL_z.npy` [5364]; `embed/gene_vectors.npy` [5364]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5364 or target_col == 5364). Every well: [[SYT11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYT11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
