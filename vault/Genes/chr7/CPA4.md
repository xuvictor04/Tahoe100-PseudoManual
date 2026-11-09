---
symbol: "CPA4"
type: "gene"
col: 4885
ensembl_id: "ENSG00000128510"
name: "carboxypeptidase A4"
location: "7q32.2"
module: 224
arm: "+"
pooled_cpm: 4.21
n_lines_expressing: 24
n_dd_up: 54
n_dd_down: 7
n_dd_up_clean: 41
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/224"]
generated_by: "tahoemap"
---

# CPA4

*carboxypeptidase A4* — 7q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 54 drug-doses (13 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 6.12× (z +20.5, q 0e+00, up in 21 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Budesonide (drug)]] 5 µM: 0.596× (z -4.2, q 0.016, down in 10 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOXD1]] (+0.65, fdr 1e-05), [[CREB5]] (+0.62, fdr 1e-05), [[ZMAT4]] (+0.62, fdr 1e-05); moves opposite to [[GYPC]] (-0.55, fdr 1e-05), [[FOXC2]] (-0.48, fdr 4e-05), [[ITGA10]] (-0.47, fdr 4e-05).
> It is in [[Module 224]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 10 go from it, the strongest it → cells under [[Vemurafenib (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 54 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4885.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **6.12×** | +20.5 | 0e+00 | 21/21 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.57×** | +16.5 | 0e+00 | 4/7 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **6.86×** | +15.4 | 0e+00 | 20/20 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.70×** | +13.9 | 9e-42 | 9/12 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.27×** | +13.3 | 4e-38 | 20/20 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.13×** | +10.5 | 1e-23 | 4/8 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.61×** | +10.2 | 1e-22 | 16/18 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.42×** | +9.8 | 7e-21 | 19/20 (NCI-H2030, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.54×** | +7.4 | 8e-12 | 15/20 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +6.0 | 1e-07 | 3/15 (C32, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.65×** | +5.6 | 1e-06 | 11/21 (A-172, C32, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **2.08×** | +5.6 | 1e-06 | 12/18 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.64×** | +5.4 | 3e-06 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.95×** | +5.3 | 5e-06 | 6/20 (A-172, HCT15, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +5.1 | 1e-05 | 4/12 (CFPAC-1, A-172, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +5.1 | 1e-05 | 5/20 (AN3 CA, C32, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.90×** | +4.9 | 3e-05 | 7/19 (HS-578T, A-172, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.53×** | +4.7 | 7e-05 | 7/20 (SK-MEL-2, C32, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.74×** | +4.4 | 3e-04 | 10/21 (A-172, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.73×** | +4.4 | 3e-04 | 8/18 (SK-MEL-2, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4885.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 5 µM |  | **0.596×** | -4.2 | 0.016 | 10/20 (HS-578T, H4, …) | top dose only |  |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **0.616×** | -3.8 | 0.030 | 7/19 (A498, AsPC-1, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.725×** | -3.7 | 0.030 | 7/20 (HS-578T, NCI-H2030, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.637×** | -3.7 | 0.030 | 6/18 (HS-578T, NCI-H2030, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.638×** | -3.6 | 0.030 | 9/19 (NCI-H2030, HS-578T, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **0.645×** | -3.6 | 0.035 | 6/21 (HS-578T, NCI-H2030, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -3.4 | 0.061 | 10/20 (HS-578T, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4885. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 17.3 | 4 (1 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 18.2× (z +17.1) | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.128× (z -8.6) ⚠ toxic |
| [[HOP62 (line)]] | alt | 1.54 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 32.3× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 37.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 11.1× (z +13.1) | — |
| [[NCI-H460 (line)]] | wt | 4.27 | 3 | 1 | [[Tucidinostat (drug)]] 5 µM 11.5× (z +13.2) | [[Clobetasol propionate (drug)]] 0.05 µM 0.0255× (z -14.1) |
| [[HS-578T (line)]] | alt | 24.3 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 7.50× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -11.1) ⚠ cell-cycle shift, explains ~24% of this change |
| [[J82 (line)]] | alt | 9.60 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 11.7× (z +12.8) | — |
| [[AN3 CA (line)]] | alt | 15.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 74.9× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 24.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.2× (z +9.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 1.49 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 66.3× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.80× (z +10.0) | — |
| [[A-427 (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.756 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.434 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.964 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.713 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.642 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.587 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.866 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.564 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.389 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.769 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.620 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4885), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOXD1]] | +0.65 | +0.53 / +0.77 | both halves | 1e-05 | **novel candidate** |
| [[CREB5]] | +0.62 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[ZMAT4]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[SYTL2]] | +0.60 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[ANOS1]] | +0.58 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[PLCXD2]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[NPPB]] | +0.56 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[ADAMTS16]] | +0.55 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[TRAK1]] | +0.55 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[GLRB]] | +0.52 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[C5orf46]] | +0.52 | +0.36 / +0.64 | both halves | 9e-05 |  |
| [[PKIA]] | +0.52 | +0.48 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GYPC]] | -0.55 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[FOXC2]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ITGA10]] | -0.47 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[MCCC1]] | -0.45 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[KANSL2]] | -0.45 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[ZMYND8]] | -0.43 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[CCND3]] | -0.43 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[PEX11B]] | -0.42 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[TNS2]] | -0.42 | -0.37 / -0.39 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers CPA4's level | compounds that target MAP2K1: 4 of 4 raise it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 10.4% of all compounds | 0.062 | ⚠ off-target possible; 4 compounds |
| [[FOXC2]] | C | FOXC2 activity raises CPA4's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 2.37× lower at baseline in the lines without FOXC2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT; co-absent with the target |
| [[EDIL3]] | C | EDIL3 activity raises CPA4's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 2.05× lower at baseline in the lines without EDIL3 | 0.041 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC; co-absent with the target |
| [[EDIL3-DT]] | C | EDIL3-DT activity raises CPA4's level | lines that do not express EDIL3-DT (25) vs lines expressing it (25) | 2.02× lower at baseline in the lines without EDIL3-DT | 0.092 | ⚠ within organs, on part of the lines; also absent: EDIL3, NALCN, DTNA; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Vemurafenib (drug)]] 5 µM | B | CPA4 activity raises the cells' numbers under Vemurafenib 5 µM (protects the cells) | lines that do not express CPA4 (26) vs lines expressing it (22) | the lines without CPA4: 0.85× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: GYPC, FLI1, IL6 |
| [[MCC]] | B | CPA4 activity raises MCC's level | lines that do not express CPA4 (26) vs lines expressing it (24) | 2.20× lower at baseline in the lines without CPA4 | 0.099 | ⚠ within organs, on part of the lines; also absent: GYPC, FLI1, IL6 |
| [[GYPC]] | C | CPA4 activity raises GYPC's level | lines that do not express CPA4 (26) vs lines expressing it (24) | 4.63× lower at baseline in the lines without CPA4 | 0.002 | ⚠ within organs, on part of the lines; also absent: GYPC, FLI1, IL6; co-absent with the target |
| [[NID2]] | C | CPA4 activity raises NID2's level | lines that do not express CPA4 (26) vs lines expressing it (24) | 2.88× lower at baseline in the lines without CPA4 | 0.018 | ⚠ within organs, on part of the lines; also absent: GYPC, FLI1, IL6; co-absent with the target |
| [[OR4F15]] | C | CPA4 activity raises OR4F15's level | lines that do not express CPA4 (26) vs lines expressing it (24) | 2.37× lower at baseline in the lines without CPA4 | 0.032 | ⚠ within organs, on part of the lines; also absent: GYPC, FLI1, IL6; co-absent with the target |
| [[EDIL3]] | C | CPA4 activity raises EDIL3's level | lines that do not express CPA4 (26) vs lines expressing it (24) | 4.10× lower at baseline in the lines without CPA4 | 0.042 | ⚠ within organs, on part of the lines; also absent: GYPC, FLI1, IL6; co-absent with the target |
| [[EDIL3-DT]] | C | CPA4 activity raises EDIL3-DT's level | lines that do not express CPA4 (26) vs lines expressing it (24) | 2.35× lower at baseline in the lines without CPA4 | 0.051 | ⚠ within organs, on part of the lines; also absent: GYPC, FLI1, IL6; co-absent with the target |
| [[C5orf46]] | C | CPA4 activity raises C5orf46's level | lines that do not express CPA4 (26) vs lines expressing it (24) | 1.73× lower at baseline in the lines without CPA4 | 0.084 | ⚠ within organs, on part of the lines; also absent: GYPC, FLI1, IL6; co-absent with the target |
| [[MOXD1]] | C | CPA4 activity raises MOXD1's level | lines that do not express CPA4 (26) vs lines expressing it (24) | 2.89× lower at baseline in the lines without CPA4 | 0.085 | ⚠ within organs, on part of the lines; also absent: GYPC, FLI1, IL6; co-absent with the target |
| [[FOXC2]] | C | CPA4 activity raises FOXC2's level | lines that do not express CPA4 (26) vs lines expressing it (24) | 2.65× lower at baseline in the lines without CPA4 | 0.086 | ⚠ within organs, on part of the lines; also absent: GYPC, FLI1, IL6; co-absent with the target |

## Where it sits

- **Module**: [[Module 224]] — hypoxia; 9 genes; every member is in the + arm (projection on the module's main direction 0.682). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.2, 18.0); signed map (32.4, 33.4). **Vector** length 61.7, 15.3% of its response variance represented; |z| ≥ 3 in 739 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +20.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +13.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +10.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +4.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +5.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +4.4 |
| fall | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.2 | -1.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.0 | -2.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.0 | -3.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -2.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | carboxypeptidase A4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.2 — chr7:130,293,134-130,324,180 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CPA3 |
| Gene groups (HGNC) | M14 carboxypeptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UI42](https://www.uniprot.org/uniprotkb/Q9UI42) (Carboxypeptidase A4):

> Metalloprotease that cleaves hydrophobic C-terminal residues with a preference for -Phe, -Leu, -Ile, -Met, -Tyr and -Val. May function in peptide hormone and/or neuropeptide catabolism.

**Summary**, from NCBI Gene [51200](https://www.ncbi.nlm.nih.gov/gene/51200):

> This gene is a member of the carboxypeptidase A/B subfamily, and it is located in a cluster with three other family members on chromosome 7. Carboxypeptidases are zinc-containing exopeptidases that catalyze the release of carboxy-terminal amino acids, and are synthesized as zymogens that are activated by proteolytic cleavage. This gene could be involved in the histone hyperacetylation pathway. It is imprinted and may be a strong candidate gene for prostate cancer aggressiveness. [provided by …

**Accessions** — [HGNC:15740](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15740) · Entrez [51200](https://www.ncbi.nlm.nih.gov/gene/51200) · UniProt [Q9UI42](https://www.uniprot.org/uniprotkb/Q9UI42) · Ensembl [ENSG00000128510](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128510)

## Data

Gene col 4885: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4885); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4885, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4885]; `tensor/DDL_lfc|DDL_z.npy` [4885]; `embed/gene_vectors.npy` [4885]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4885 or target_col == 4885). Every well: [[CPA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
