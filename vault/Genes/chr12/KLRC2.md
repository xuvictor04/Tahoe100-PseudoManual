---
symbol: "KLRC2"
type: "gene"
col: 13014
ensembl_id: "ENSG00000205809"
name: "killer cell lectin like receptor C2"
location: "12p13.2"
module: 223
arm: "+"
pooled_cpm: 6.03
n_lines_expressing: 23
n_dd_up: 15
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/223"]
generated_by: "tahoemap"
---

# KLRC2

*killer cell lectin like receptor C2* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.49× (z +19.2, q 0e+00, up in 15 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.466× (z -6.1, q 5e-07, down in 16 of 20 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLRC3]] (+0.95, fdr 7e-06, ⚠ same locus), [[KLRC4-KLRK1]] (+0.93, fdr 7e-06, ⚠ same locus), [[KLRK1]] (+0.89, fdr 7e-06, ⚠ same locus), [[BMP5]] (+0.69, fdr 7e-06), [[CXXC4]] (+0.67, fdr 7e-06), [[NR4A3]] (+0.64, fdr 1e-05); moves opposite to [[TPD52L2]] (-0.52, fdr 2e-05), [[GPR89A]] (-0.50, fdr 2e-05), [[ADPGK]] (-0.49, fdr 2e-05).
> It is in [[Module 223]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); 7 go from it, the strongest it → [[TIMM10B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13014.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.49×** | +19.2 | 0e+00 | 15/19 (BT-474, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.22×** | +11.0 | 1e-25 | 1/4 (NCI-H2030) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.51×** | +10.3 | 9e-23 | 17/21 (NCI-H1792, HCT15, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.58×** | +10.1 | 5e-22 | 10/18 (A-427, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.46×** | +10.1 | 7e-22 | 1/5 (NCI-H2030) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.40×** | +9.7 | 2e-20 | 5/8 (NCI-H2030, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.09×** | +8.6 | 6e-16 | 13/21 (BT-474, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.13×** | +6.0 | 1e-07 | 12/19 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.77×** | +4.5 | 4e-04 | 0/11 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.15×** | +4.3 | 8e-04 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.9 | 0.006 | 0/16 | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +3.7 | 0.012 | 1/6 (SW480) | rises with dose | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.76×** | +3.2 | 0.059 | 3/10 (NCI-H2030, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.059 | 2/21 (NCI-H2030, SW 900) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +3.0 | 0.090 | 3/21 (NCI-H460, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13014.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.466×** | -6.1 | 5e-07 | 16/20 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.541×** | -5.0 | 2e-04 | 13/21 (A-427, NCI-H23, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.618×** | -3.7 | 0.035 | 5/21 (NCI-H23, AsPC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.432×** | -3.5 | 0.051 | 9/19 (SHP-77, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.632×** | -3.5 | 0.051 | 11/19 (SW480, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.557×** | -3.4 | 0.070 | 7/21 (NCI-H2030, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.665×** | -3.3 | 0.070 | 6/21 (SHP-77, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.666×** | -3.3 | 0.070 | 9/18 (NCI-H23, NCI-H1573, …) | two highest doses |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.762× | -3.1 | 0.11 | 7/21 (A-427, NCI-H2030, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.770× | -3.0 | 0.14 | 10/21 (SK-MEL-2, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13014. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.5 | 0 | 7 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0828× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 73.5 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -11.0) |
| [[A-427 (line)]] | wt | 25.2 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 7.06× (z +10.9) | [[Bortezomib (drug)]] 0.05 µM 0.186× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 5.40 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.71× (z +9.0) | [[Ixazomib citrate (drug)]] 0.5 µM 0.0246× (z -10.4) |
| [[BT-474 (line)]] | alt | 1.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 132× (z +12.7) | — |
| [[HCT15 (line)]] | alt | 6.99 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0210× (z -11.8) |
| [[HepG2_C3A (line)]] | wt | 2.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.4× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 52.6 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.193× (z -9.2) |
| [[SHP-77 (line)]] | alt | 12.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -10.1) |
| [[SW 1271 (line)]] | alt | 30.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0747× (z -9.9) |
| [[SW 900 (line)]] | alt | 33.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.156× (z -8.9) |
| [[A-172 (line)]] | wt | 0.351 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.401 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.399 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.926 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.833 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.427 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.661 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.601 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.392 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.39 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13014), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLRC3]] | +0.95 | +0.96 / +0.93 | both halves | 7e-06 | same gene group; STRING 999; ⚠ same locus (6.3 kb, same strand: neighbours can correlate without regulation) |
| [[KLRC4-KLRK1]] | +0.93 | +0.94 / +0.91 | both halves | 7e-06 | ⚠ same locus (16.7 kb, same strand: neighbours can correlate without regulation) |
| [[KLRK1]] | +0.89 | +0.91 / +0.84 | both halves | 7e-06 | same gene group; pathway: DAP12 interactions; STRING 931; ⚠ same locus (35.0 kb, same strand: neighbours can correlate without regulation) |
| [[BMP5]] | +0.69 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[CXXC4]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[NR4A3]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CCDC148]] | +0.63 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[NR4A2]] | +0.62 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[ZFHX2]] | +0.61 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[CFAP300]] | +0.60 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[HES1]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[ID4]] | +0.59 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[IGFL4]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[BCL3]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[GASAL1]] | +0.57 | +0.67 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPD52L2]] | -0.52 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[GPR89A]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ADPGK]] | -0.49 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[ZNF595]] | -0.49 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[VPS53]] | -0.48 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[ITGB1BP1]] | -0.48 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[SRD5A1]] | -0.48 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[ZCCHC17]] | -0.48 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[C8orf76]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[CTDP1]] | -0.48 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[METTL3]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[TIMM10B]] | -0.47 | -0.39 / -0.42 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises KLRC2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[KLRC4-KLRK1]], [[KLRK1]] | C | KLRC4-KLRK1, KLRK1 activity raises KLRC2's level | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (21) | 4.88× lower at baseline in the lines without KLRC4-KLRK1, KLRK1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent with the target; co-absent genes |
| [[KLRC3]] | C | KLRC3 activity raises KLRC2's level | lines that do not express KLRC3 (27) vs lines expressing it (23) | 4.64× lower at baseline in the lines without KLRC3 | 4e-04 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4; co-absent with the target |
| [[IGFL4]] | C | IGFL4 activity raises KLRC2's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 2.52× lower at baseline in the lines without IGFL4 | 0.045 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TIMM10B]] | B | KLRC2 activity raises TIMM10B's level | lines that do not express KLRC2 (27) vs lines expressing it (23) | 1.12× lower at baseline in the lines without KLRC2 | 0.073 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRK1, TRPM2-AS |
| [[LINC01091]] | B | KLRC2 activity raises LINC01091's level | lines that do not express KLRC2 (27) vs lines expressing it (23) | 1.74× lower at baseline in the lines without KLRC2 | 0.085 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRK1, TRPM2-AS |
| [[MAP3K2-DT]] | B | KLRC2 activity raises MAP3K2-DT's level | lines that do not express KLRC2 (27) vs lines expressing it (23) | 1.32× lower at baseline in the lines without KLRC2 | 0.088 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRK1, TRPM2-AS |
| [[KLRC3]] | C | KLRC2 activity raises KLRC3's level | lines that do not express KLRC2 (27) vs lines expressing it (23) | 4.14× lower at baseline in the lines without KLRC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRK1, TRPM2-AS; co-absent with the target |
| [[KLRC4-KLRK1]] | C | KLRC2 activity raises KLRC4-KLRK1's level | lines that do not express KLRC2 (27) vs lines expressing it (23) | 3.87× lower at baseline in the lines without KLRC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRK1, TRPM2-AS; co-absent with the target |
| [[KLRK1]] | C | KLRC2 activity raises KLRK1's level | lines that do not express KLRC2 (27) vs lines expressing it (23) | 3.37× lower at baseline in the lines without KLRC2 | 0.002 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRK1, TRPM2-AS; co-absent with the target |
| [[IGFL4]] | C | KLRC2 activity raises IGFL4's level | lines that do not express KLRC2 (27) vs lines expressing it (23) | 2.22× lower at baseline in the lines without KLRC2 | 0.078 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRK1, TRPM2-AS; co-absent with the target |

## Where it sits

- **Module**: [[Module 223]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.933). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.4, 33.6); signed map (51.2, 19.9). **Vector** length 56.3, 13.6% of its response variance represented; |z| ≥ 3 in 594 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +19.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +10.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | -6.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.1 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -5.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.9 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | killer cell lectin like receptor C2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:10,426,854-10,442,300 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NKG2-C, CD159c, NKG2C |
| Gene groups (HGNC) | CD molecules; Killer cell lectin like receptors; C-type lectin domain containing |
| Reactome | 3 pathways, smallest: DAP12 signaling; DAP12 interactions; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P26717](https://www.uniprot.org/uniprotkb/P26717) (NKG2-C type II integral membrane protein):

> Immune activating receptor involved in self-nonself discrimination. In complex with KLRD1 on cytotoxic lymphocyte subsets, recognizes non-classical major histocompatibility (MHC) class Ib HLA-E loaded with signal sequence-derived peptides from non-classical MHC class Ib HLA-G molecules, likely playing a role in the generation and effector functions of adaptive natural killer (NK) cells and in maternal-fetal tolerance during pregnancy. Regulates the effector functions of terminally …

**Summary**, from NCBI Gene [3822](https://www.ncbi.nlm.nih.gov/gene/3822):

> Natural killer (NK) cells are lymphocytes that can mediate lysis of certain tumor cells and virus-infected cells without previous activation. They can also regulate specific humoral and cell-mediated immunity. NK cells preferentially express several calcium-dependent (C-type) lectins, which have been implicated in the regulation of NK cell function. The group, designated KLRC (NKG2) are expressed primarily in natural killer (NK) cells and encodes a family of transmembrane proteins characterized …

**Accessions** — [HGNC:6375](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6375) · Entrez [3822](https://www.ncbi.nlm.nih.gov/gene/3822) · UniProt [P26717](https://www.uniprot.org/uniprotkb/P26717) · Ensembl [ENSG00000205809](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205809)

## Data

Gene col 13014: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13014); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13014, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13014]; `tensor/DDL_lfc|DDL_z.npy` [13014]; `embed/gene_vectors.npy` [13014]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13014 or target_col == 13014). Every well: [[KLRC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLRC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
