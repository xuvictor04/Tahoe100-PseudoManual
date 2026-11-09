---
symbol: "MYT1"
type: "gene"
col: 12135
ensembl_id: "ENSG00000196132"
name: "myelin transcription factor 1"
location: "20q13.33"
module: 128
arm: "+"
pooled_cpm: 3.65
n_lines_expressing: 25
n_dd_up: 36
n_dd_down: 5
n_dd_up_clean: 22
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 16
direction_downstream: 25
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# MYT1

*myelin transcription factor 1* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.12× (z +24.3, q 0e+00, up in 6 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.432× (z -8.9, q 4e-16, down in 15 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPTB]] (+0.66, fdr 7e-06), [[EMID1]] (+0.64, fdr 7e-06), [[CACNA2D2]] (+0.61, fdr 7e-06).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[EPHA10]] → it (grade B ⚠); 25 go from it, the strongest it → [[FSD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12135.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.12×** | +24.3 | 0e+00 | 6/17 (A498, A549, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.94×** | +20.4 | 0e+00 | 8/16 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.66×** | +14.5 | 1e-45 | 13/20 (HT-29, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.12×** | +14.3 | 3e-44 | 2/5 (SHP-77, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.85×** | +11.0 | 3e-26 | 10/19 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +10.5 | 1e-23 | 5/11 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.82×** | +10.1 | 5e-22 | 4/6 (A498, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.24×** | +8.5 | 1e-15 | 8/19 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.16×** | +8.1 | 3e-14 | 11/18 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +6.8 | 5e-10 | 3/12 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +6.1 | 7e-08 | 6/19 (NCI-H23, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +5.5 | 2e-06 | 12/20 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.69×** | +5.5 | 2e-06 | 5/19 (PANC-1, HT-29, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.2 | 6e-06 | 0/20 | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +4.7 | 1e-04 | 3/16 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.23×** | +4.4 | 4e-04 | 2/17 (A498, NCI-H23) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +4.0 | 0.001 | 10/19 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.001 | 10/20 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.68×** | +3.9 | 0.003 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.011 | 2/19 (SW480, NCI-H2030) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12135.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.432×** | -8.9 | 4e-16 | 15/19 (SW480, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.508×** | -7.2 | 2e-10 | 15/21 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.652×** | -4.5 | 0.001 | 9/20 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.685×** | -4.0 | 0.008 | 9/18 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.722×** | -3.5 | 0.059 | 11/18 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.739× | -3.2 | 0.12 | 6/20 (MIA PaCa-2, H4, …) | inconsistent across doses |  |
| [[Bestatin (drug)]] 0.5 µM |  | 0.742× | -3.2 | 0.12 | 1/20 (A-172) | inconsistent across doses |  |
| [[Aspirin (drug)]] 0.5 µM |  | 0.749× | -3.1 | 0.14 | 4/20 (SW 900, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12135. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 16.9 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.103× (z -14.6) |
| [[NCI-H2030 (line)]] | alt | 5.13 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0343× (z -12.8) |
| [[SHP-77 (line)]] | alt | 33.1 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -18.9) |
| [[A-427 (line)]] | wt | 18.0 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0434× (z -17.1) |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0526× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0911× (z -10.4) |
| [[A-172 (line)]] | wt | 5.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +13.1) | — |
| [[PANC-1 (line)]] | alt | 1.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +10.1) | — |
| [[A498 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.770 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.547 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.635 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.513 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.585 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.891 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.775 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.814 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.535 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12135), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTB]] | +0.66 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[EMID1]] | +0.64 | +0.63 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[CACNA2D2]] | +0.61 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[SEPTIN3]] | +0.60 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[DPYSL5]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ADGRB1]] | +0.59 | +0.49 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[LRRC4B]] | +0.58 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[JPH3]] | +0.58 | +0.55 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[FXYD6]] | +0.58 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[ADAM22]] | +0.58 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[KCNQ2]] | +0.57 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[EPHA10]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 3, C 13. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA10]] | B | EPHA10 activity raises MYT1's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 2.06× lower at baseline in the lines without EPHA10 | 0.066 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |
| [[PSD2]] | B | PSD2 activity raises MYT1's level | lines that do not express PSD2 (13) vs lines expressing it (37) | 2.02× lower at baseline in the lines without PSD2 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, CACNA1C, SSC5D; maybe low, not absent |
| [[KLHL14]] | B | KLHL14 activity raises MYT1's level | lines that do not express KLHL14 (37) vs lines expressing it (13) | 2.08× lower at baseline in the lines without KLHL14 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55 |
| [[NFASC]] | C | NFASC activity raises MYT1's level | lines that do not express NFASC (27) vs lines expressing it (23) | 2.28× lower at baseline in the lines without NFASC | 0.003 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A; co-absent with the target |
| [[CHD5]] | C | CHD5 activity raises MYT1's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 2.57× lower at baseline in the lines without CHD5 | 0.008 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent; co-absent with the target |
| [[LINC02428]] | C | LINC02428 activity raises MYT1's level | lines that do not express LINC02428 (32) vs lines expressing it (18) | 1.80× lower at baseline in the lines without LINC02428 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ENSG00000287598, ENSG00000287474; co-absent with the target |
| [[DPYSL5]] | C | DPYSL5 activity raises MYT1's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.78× lower at baseline in the lines without DPYSL5 | 0.017 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises MYT1's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 2.34× lower at baseline in the lines without GABRG2 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[LMX1B]] | C | LMX1B activity raises MYT1's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 2.05× lower at baseline in the lines without LMX1B | 0.038 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2; co-absent with the target |
| [[NOTUM]] | C | NOTUM activity raises MYT1's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 2.14× lower at baseline in the lines without NOTUM | 0.040 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7; co-absent with the target |
| [[LAMC3]] | C | LAMC3 activity raises MYT1's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 2.31× lower at baseline in the lines without LAMC3 | 0.046 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2; co-absent with the target |
| [[NOVA2]] | C | NOVA2 activity raises MYT1's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 1.97× lower at baseline in the lines without NOVA2 | 0.049 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 12, C 13. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSD1]] | B | MYT1 activity raises FSD1's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 2.02× lower at baseline in the lines without MYT1 | 0.012 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[KIF3C]] | B | MYT1 activity raises KIF3C's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 1.89× lower at baseline in the lines without MYT1 | 0.037 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[EPHA10]] | B | MYT1 activity raises EPHA10's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 1.66× lower at baseline in the lines without MYT1 | 0.043 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[TMEM150C]] | B | MYT1 activity raises TMEM150C's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 2.05× lower at baseline in the lines without MYT1 | 0.046 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[ERICH6-AS1]] | B | MYT1 activity raises ERICH6-AS1's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 1.40× lower at baseline in the lines without MYT1 | 0.049 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[LRRC4B]] | B | MYT1 activity raises LRRC4B's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 2.03× lower at baseline in the lines without MYT1 | 0.059 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[CACNA1B]] | B | MYT1 activity raises CACNA1B's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 2.32× lower at baseline in the lines without MYT1 | 0.067 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[EFHD1]] | B | MYT1 activity raises EFHD1's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 1.66× lower at baseline in the lines without MYT1 | 0.075 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[CYB5RL]] | B | MYT1 activity raises CYB5RL's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 1.25× lower at baseline in the lines without MYT1 | 0.086 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[GNAO1]] | B | MYT1 activity raises GNAO1's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 1.73× lower at baseline in the lines without MYT1 | 0.090 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[SEMA6B]] | B | MYT1 activity raises SEMA6B's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 2.19× lower at baseline in the lines without MYT1 | 0.095 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[PSD2]] | B | MYT1 activity raises PSD2's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 1.59× lower at baseline in the lines without MYT1 | 0.097 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.0, 39.1); signed map (24.9, 26.6). **Vector** length 45.6, 9.68% of its response variance represented; |z| ≥ 3 in 560 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.4 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +14.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +8.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -8.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.5 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -2.0 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.9 | -3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | myelin transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:64,102,394-64,242,253 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MTF1, MYTI, ZC2HC4A, NZF2, ZC2H2C1; previously PLPB1 |
| Gene groups (HGNC) | Zinc fingers C2H2C-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01538](https://www.uniprot.org/uniprotkb/Q01538) (Myelin transcription factor 1):

> Binds to the promoter region of genes encoding proteolipid proteins of the central nervous system. May play a role in the development of neurons and oligodendroglia in the CNS. May regulate a critical transition point in oligodendrocyte lineage development by modulating oligodendrocyte progenitor proliferation relative to terminal differentiation and up-regulation of myelin gene transcription.

**Summary**, from NCBI Gene [4661](https://www.ncbi.nlm.nih.gov/gene/4661):

> The protein encoded by this gene is a member of a family of neural specific, zinc finger-containing DNA-binding proteins. The protein binds to the promoter regions of proteolipid proteins of the central nervous system and plays a role in the developing nervous system. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7622](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7622) · Entrez [4661](https://www.ncbi.nlm.nih.gov/gene/4661) · UniProt [Q01538](https://www.uniprot.org/uniprotkb/Q01538) · Ensembl [ENSG00000196132](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196132)

## Data

Gene col 12135: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12135); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12135, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12135]; `tensor/DDL_lfc|DDL_z.npy` [12135]; `embed/gene_vectors.npy` [12135]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12135 or target_col == 12135). Every well: [[MYT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
