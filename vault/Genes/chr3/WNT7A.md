---
symbol: "WNT7A"
type: "gene"
col: 7836
ensembl_id: "ENSG00000154764"
name: "Wnt family member 7A"
location: "3p25.1"
module: 34
arm: "+"
pooled_cpm: 4.92
n_lines_expressing: 11
n_dd_up: 26
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 10
direction_downstream: 32
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# WNT7A

*Wnt family member 7A* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.54× (z +9.9, q 2e-20, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.93× (z +6.3, q 4e-08, up in 0 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[(S)-Crizotinib (drug)]] 0.05 µM: 0.479× (z -4.3, q 0.008, down in 0 of 9 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CARD10]] (+0.62, fdr 1e-05), [[TINAGL1]] (+0.61, fdr 1e-05), [[ARHGAP29]] (+0.59, fdr 2e-05); moves opposite to [[BATF]] (-0.48, fdr 1e-04), [[PTPN2]] (-0.46, fdr 4e-05), [[LINC02432]] (-0.46, fdr 5e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[LAMC2]] → it (grade C ⚠); 32 go from it, the strongest it → [[NET1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7836.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.54×** | +9.9 | 2e-20 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.96×** | +9.4 | 2e-18 | 1/8 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.87×** | +7.8 | 1e-12 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +6.3 | 4e-08 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.30×** | +5.7 | 2e-06 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.82×** | +5.0 | 4e-05 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.72×** | +4.9 | 9e-05 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.50×** | +4.5 | 6e-04 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.91×** | +4.4 | 6e-04 | 0/9 | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +4.3 | 9e-04 | 0/7 | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.55×** | +4.2 | 0.001 | 3/9 (CFPAC-1, SW1417, …) | top dose only | composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.81×** | +4.0 | 0.002 | 3/9 (J82, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.81×** | +3.7 | 0.010 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.6 | 0.013 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.68×** | +3.5 | 0.017 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.033 | 0/9 | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +3.2 | 0.049 | 2/9 (Panc 03.27, SW1417) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.90×** | +3.1 | 0.053 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.57×** | +3.1 | 0.061 | 1/9 (SW480) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.57×** | +3.1 | 0.061 | 0/9 | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +3.0 | 0.070 | 1/9 (CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Erythromycin (drug)]] 5 µM |  | **1.54×** | +2.9 | 0.074 | 0/9 | top dose only | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.54×** | +2.9 | 0.074 | 0/9 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7836.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | **0.479×** | -4.3 | 0.008 | 0/9 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.487×** | -4.2 | 0.008 | 6/9 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.632×** | -3.5 | 0.089 | 7/9 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.563× | -3.3 | 0.12 | 0/9 | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 0.644× | -3.0 | 0.21 | 4/9 (Hs 766T, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.634× | -3.0 | 0.21 | 0/9 | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.596× | -3.0 | 0.21 | 1/9 (J82) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7836. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 89.4 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0363× (z -23.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0660× (z -19.0) |
| [[HEC-1-A (line)]] | alt | 40.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -10.5) |
| [[A-172 (line)]] | wt | 0.319 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.295 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.785 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.438 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.386 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.446 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.396 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.403 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.444 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.937 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7836), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARD10]] | +0.62 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[TINAGL1]] | +0.61 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[ARHGAP29]] | +0.59 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[CARD11]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[ATG9B]] | +0.58 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[HS3ST1]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[SLC45A3]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[MYH16]] | +0.57 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[WNT7B]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 | same gene group; pathway: Class B/2 (Secretin family receptors); STRING 689 |
| [[OSBPL3]] | +0.56 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[TGFA]] | +0.56 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[PADI1]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BATF]] | -0.48 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[PTPN2]] | -0.46 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[LINC02432]] | -0.46 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[C1RL]] | -0.45 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[SLPI]] | -0.43 | -0.33 / -0.41 | both halves | 1e-04 | pathway: HALLMARK_KRAS_SIGNALING_UP |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMC2]] | C | LAMC2 activity raises WNT7A's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 2.24× lower at baseline in the lines without LAMC2 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1; co-absent with the target |
| [[TTC9]] | C | TTC9 activity raises WNT7A's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 2.16× lower at baseline in the lines without TTC9 | 0.045 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2; co-absent with the target |
| [[CNTNAP3C]] | C | CNTNAP3C activity raises WNT7A's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 1.95× lower at baseline in the lines without CNTNAP3C | 0.058 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA; co-absent with the target |
| [[TINAGL1]] | C | TINAGL1 activity raises WNT7A's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.12× lower at baseline in the lines without TINAGL1 | 0.061 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19; co-absent with the target |
| [[NES]] | C | NES activity raises WNT7A's level | lines that do not express NES (26) vs lines expressing it (24) | 1.97× lower at baseline in the lines without NES | 0.067 | ⚠ within organs, on part of the lines; also absent: LAPTM5, CSPG4, ENSG00000230490; co-absent with the target |
| [[GJB3]] | C | GJB3 activity raises WNT7A's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 2.50× lower at baseline in the lines without GJB3 | 0.067 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10; co-absent with the target |
| [[HS3ST1]] | C | HS3ST1 activity raises WNT7A's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 2.30× lower at baseline in the lines without HS3ST1 | 0.081 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4; co-absent with the target |
| [[SPNS2]] | C | SPNS2 activity raises WNT7A's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 2.03× lower at baseline in the lines without SPNS2 | 0.082 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N; co-absent with the target |
| [[ZBED2]] | C | ZBED2 activity raises WNT7A's level | lines that do not express ZBED2 (39) vs lines expressing it (11) | 3.56× lower at baseline in the lines without ZBED2 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPON1, ENSG00000289850, KLK11; co-absent with the target |
| [[WNT7B]] | C | WNT7B activity raises WNT7A's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.99× lower at baseline in the lines without WNT7B | 0.089 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG; co-absent with the target |

### Downstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 18, C 14. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NET1]] | B | WNT7A activity raises NET1's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 2.54× lower at baseline in the lines without WNT7A | 0.008 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[ATG9B]] | B | WNT7A activity raises ATG9B's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 3.01× lower at baseline in the lines without WNT7A | 0.008 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[FRMD5]] | B | WNT7A activity raises FRMD5's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 1.67× lower at baseline in the lines without WNT7A | 0.034 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[OSBPL3]] | B | WNT7A activity raises OSBPL3's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 1.80× lower at baseline in the lines without WNT7A | 0.039 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[SOX13]] | B | WNT7A activity raises SOX13's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 1.80× lower at baseline in the lines without WNT7A | 0.044 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[TSPAN14]] | B | WNT7A activity raises TSPAN14's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 1.57× lower at baseline in the lines without WNT7A | 0.045 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[MED15]] | B | WNT7A activity raises MED15's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 1.37× lower at baseline in the lines without WNT7A | 0.046 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[TGFA]] | B | WNT7A activity raises TGFA's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 2.88× lower at baseline in the lines without WNT7A | 0.051 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[PLEKHG3]] | B | WNT7A activity raises PLEKHG3's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 1.70× lower at baseline in the lines without WNT7A | 0.060 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[TLDC2]] | B | WNT7A activity raises TLDC2's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 1.81× lower at baseline in the lines without WNT7A | 0.071 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[FAM3C]] | B | WNT7A activity raises FAM3C's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 1.94× lower at baseline in the lines without WNT7A | 0.074 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[CMTM7]] | B | WNT7A activity raises CMTM7's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 1.94× lower at baseline in the lines without WNT7A | 0.076 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.3, 60.3); signed map (-0.8, 41.7). **Vector** length 43.0, 17.8% of its response variance represented; |z| ≥ 3 in 269 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +1.8 | +3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.5 | +1.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +1.3 | -0.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +0.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +1.0 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.0 | -0.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +0.9 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.9 | +2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.9 | +0.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -1.3 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | Wnt family member 7A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:13,816,258-13,880,071 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Wnt-7a |
| Gene groups (HGNC) | Wnt family |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 5 pathways, smallest: WNT ligand biogenesis and trafficking; Class B/2 (Secretin family receptors); GPCR ligand binding |
| Matched by | ensembl_id |

**Function**, from UniProt [O00755](https://www.uniprot.org/uniprotkb/O00755) (Protein Wnt-7a):

> Ligand for members of the frizzled family of seven transmembrane receptors that functions in the canonical Wnt/beta-catenin signaling pathway (By similarity). Plays an important role in embryonic development, including dorsal versus ventral patterning during limb development, skeleton development and urogenital tract development. Required for central nervous system (CNS) angiogenesis and blood-brain barrier regulation. Required for normal, sexually dimorphic development of the Mullerian ducts, …

**Summary**, from NCBI Gene [7476](https://www.ncbi.nlm.nih.gov/gene/7476):

> This gene is a member of the WNT gene family, which consists of structurally related genes that encode secreted signaling proteins. These proteins have been implicated in oncogenesis and in several developmental processes, including regulation of cell fate and patterning during embryogenesis. This gene is involved in the development of the anterior-posterior axis in the female reproductive tract, and also plays a critical role in uterine smooth muscle pattering and maintenance of adult uterine …

**Accessions** — [HGNC:12786](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12786) · Entrez [7476](https://www.ncbi.nlm.nih.gov/gene/7476) · UniProt [O00755](https://www.uniprot.org/uniprotkb/O00755) · Ensembl [ENSG00000154764](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154764)

## Data

Gene col 7836: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7836); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7836, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7836]; `tensor/DDL_lfc|DDL_z.npy` [7836]; `embed/gene_vectors.npy` [7836]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7836 or target_col == 7836). Every well: [[WNT7A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WNT7A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
