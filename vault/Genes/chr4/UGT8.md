---
symbol: "UGT8"
type: "gene"
col: 10508
ensembl_id: "ENSG00000174607"
name: "UDP glycosyltransferase 8"
location: "4q26"
module: 55
arm: "+"
pooled_cpm: 24.42
n_lines_expressing: 29
n_dd_up: 10
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 18
direction_downstream: 6
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# UGT8

*UDP glycosyltransferase 8* — 4q26

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.63× (z +14.0, q 1e-41, up in 19 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.638× (z -13.0, q 1e-35, down in 21 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF128]] (+0.70, fdr 7e-06), [[MECOM]] (+0.62, fdr 2e-05), [[VSNL1]] (+0.61, fdr 1e-05); moves opposite to [[CEP104]] (-0.55, fdr 3e-05), [[FBXL9P]] (-0.52, fdr 4e-05), [[CC2D1B]] (-0.50, fdr 3e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[PRSS12]] → it (grade B ⚠); 6 go from it, the strongest it → [[SCML2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10508.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +14.0 | 1e-41 | 19/27 (A498, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +13.1 | 1e-36 | 18/27 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +8.5 | 3e-15 | 12/27 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.33×** | +5.8 | 9e-07 | 12/27 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +4.7 | 3e-04 | 7/26 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +4.3 | 0.002 | 9/27 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.21×** | +3.8 | 0.012 | 10/26 (SHP-77, KATO III, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.017 | 5/24 (SW48, A498, …) | top dose only | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **1.20×** | +3.6 | 0.021 | 7/24 (HT-29, LoVo, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.039 | 5/27 (NCI-H23, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10508.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.638×** | -13.0 | 1e-35 | 21/27 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.541×** | -12.5 | 1e-33 | 20/27 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.689×** | -7.6 | 5e-12 | 18/27 (LS 180, C32, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.791×** | -4.8 | 2e-04 | 10/26 (H4, CHP-212, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.799×** | -4.6 | 5e-04 | 14/24 (SHP-77, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.941× | -4.2 | 0.002 | 2/27 (HOP62, SW 1271) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.815×** | -4.2 | 0.002 | 14/27 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.807×** | -4.2 | 0.002 | 5/27 (COLO 205, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.814×** | -4.1 | 0.003 | 12/27 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.825×** | -3.9 | 0.005 | 14/27 (C32, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.830×** | -3.7 | 0.012 | 9/27 (SK-MEL-2, KATO III, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -3.5 | 0.021 | 11/26 (LoVo, H4, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.855× | -3.2 | 0.058 | 10/27 (LS 180, LoVo, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.850× | -3.1 | 0.066 | 12/26 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.899× | -3.1 | 0.066 | 4/27 (CFPAC-1, COLO 205, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.748×** | -3.1 | 0.066 | 10/27 (LoVo, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.864× | -3.0 | 0.085 | 6/27 (H4, C32, …) | rises with dose |  |
| [[Resveratrol (drug)]] 5 µM |  | 0.902× | -3.0 | 0.085 | 6/27 (Panc 03.27, SW1417, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.817×** | -2.9 | 0.090 | 5/26 (HT-29, CFPAC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.818×** | -2.9 | 0.092 | 9/25 (SHP-77, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10508. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 121 | 1 (1 ⚠) | 4 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.92× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Bortezomib (drug)]] 0.05 µM 0.351× (z -9.5) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.511× (z -9.2) |
| [[COLO 205 (line)]] | alt | 87.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.414× (z -9.8) |
| [[KATO III (line)]] | alt | 82.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -15.7) |
| [[LoVo (line)]] | wt | 106 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -21.3) |
| [[C32 (line)]] | wt | 36.8 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 55.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -15.2) |
| [[LS 180 (line)]] | wt | 73.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 14.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -10.7) |
| [[RKO (line)]] | wt | 89.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -20.8) |
| [[A498 (line)]] | wt | 13.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 10.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 32.8 | 1 | 0 | [[Tucidinostat (drug)]] 0.5 µM 2.71× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -12.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 37.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.63 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.32 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.52 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10508), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF128]] | +0.70 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[MECOM]] | +0.62 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[VSNL1]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[NMU]] | +0.60 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[HPSE]] | +0.59 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[PLS1]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[ILDR2]] | +0.58 | +0.36 / +0.66 | both halves | 9e-05 |  |
| [[RNF43]] | +0.57 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[LRP4]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[MANSC1]] | +0.56 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[RAPGEF5]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[PIK3C2B]] | +0.56 | +0.47 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP104]] | -0.55 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[FBXL9P]] | -0.52 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[CC2D1B]] | -0.50 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[ITCH]] | -0.49 | -0.34 / -0.51 | both halves | 1e-04 | same gene group |
| [[ZNF621]] | -0.49 | -0.62 / -0.31 | both halves | 2e-04 |  |
| [[CCDC90B]] | -0.49 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[TECPR2]] | -0.49 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[CYP20A1]] | -0.48 | -0.59 / -0.29 | both halves | 2e-04 |  |
| [[TSG101]] | -0.48 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[SMIM12]] | -0.48 | -0.63 / -0.24 | both halves | 4e-04 |  |
| [[HGSNAT]] | -0.47 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[LTO1]] | -0.47 | -0.55 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 15, C 3. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS12]] | B | PRSS12 activity raises UGT8's level | lines that do not express PRSS12 (19) vs lines expressing it (31) | 2.51× lower at baseline in the lines without PRSS12 | 0.019 | ⚠ within organs, on part of the lines; also absent: MOXD1, TLL1, ENSG00000289884 |
| [[SLC40A1]] | B | SLC40A1 activity raises UGT8's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.45× lower at baseline in the lines without SLC40A1 | 0.027 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[ST6GALNAC1]] | B | ST6GALNAC1 activity raises UGT8's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 3.35× lower at baseline in the lines without ST6GALNAC1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| [[ENPP4]] | B | ENPP4 activity raises UGT8's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 3.28× lower at baseline in the lines without ENPP4 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |
| [[GPR160]] | B | GPR160 activity raises UGT8's level | lines that do not express GPR160 (8) vs lines expressing it (42) | 4.17× lower at baseline in the lines without GPR160 | 0.064 | ⚠ within organs, on part of the lines; also absent: PNPLA4, PRKCZ; maybe low, not absent |
| [[UGT1A1]] | B | UGT1A1 activity raises UGT8's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 2.51× lower at baseline in the lines without UGT1A1 | 0.067 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1 |
| [[ATP8A1]] | B | ATP8A1 activity raises UGT8's level | lines that do not express ATP8A1 (13) vs lines expressing it (37) | 3.05× lower at baseline in the lines without ATP8A1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENPP4, TSPAN12, KLHL32; maybe low, not absent |
| [[SMPDL3B]] | B | SMPDL3B activity raises UGT8's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 2.96× lower at baseline in the lines without SMPDL3B | 0.076 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[C4orf19]] | B | C4orf19 activity raises UGT8's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 1.85× lower at baseline in the lines without C4orf19 | 0.079 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[SNTB1]] | B | SNTB1 activity raises UGT8's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 3.09× lower at baseline in the lines without SNTB1 | 0.082 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979 |
| [[AGR3]] | B | AGR3 activity raises UGT8's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 3.62× lower at baseline in the lines without AGR3 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[MUC3A]] | B | MUC3A activity raises UGT8's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 3.12× lower at baseline in the lines without MUC3A | 0.088 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCML2]] | B | UGT8 activity lowers SCML2's level | lines that do not express UGT8 (21) vs lines expressing it (29) | 2.21× higher at baseline in the lines without UGT8 | 0.009 | ⚠ within organs, on part of the lines; also absent: CCSER1, JPH1, ABO |
| [[RAPGEF5]] | B | UGT8 activity raises RAPGEF5's level | lines that do not express UGT8 (21) vs lines expressing it (29) | 2.58× lower at baseline in the lines without UGT8 | 0.046 | ⚠ within organs, on part of the lines; also absent: CCSER1, JPH1, ABO |
| [[DAB2IP]] | B | UGT8 activity raises DAB2IP's level | lines that do not express UGT8 (21) vs lines expressing it (29) | 1.44× lower at baseline in the lines without UGT8 | 0.074 | ⚠ within organs, on part of the lines; also absent: CCSER1, JPH1, ABO |
| [[C4orf19]] | B | UGT8 activity raises C4orf19's level | lines that do not express UGT8 (21) vs lines expressing it (29) | 2.04× lower at baseline in the lines without UGT8 | 0.078 | ⚠ within organs, on part of the lines; also absent: CCSER1, JPH1, ABO |
| [[CPVL]] | B | UGT8 activity raises CPVL's level | lines that do not express UGT8 (21) vs lines expressing it (29) | 1.35× lower at baseline in the lines without UGT8 | 0.083 | ⚠ within organs, on part of the lines; also absent: CCSER1, JPH1, ABO |
| [[PRSS12]] | B | UGT8 activity raises PRSS12's level | lines that do not express UGT8 (21) vs lines expressing it (29) | 3.04× lower at baseline in the lines without UGT8 | 0.083 | ⚠ within organs, on part of the lines; also absent: CCSER1, JPH1, ABO |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.519). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.0, 50.1); signed map (64.9, 2.6). **Vector** length 71.5, 17.4% of its response variance represented; |z| ≥ 3 in 635 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +14.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +13.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.1 | +8.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.7 | +4.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +3.2 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.4 | +1.0 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.3 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.9 | -12.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.8 | -13.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.7 | -3.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -0.4 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | UDP glycosyltransferase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q26 — chr4:114,598,770-114,678,225 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CGT |
| Gene groups (HGNC) | UDP glucuronosyltransferases; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Glycosphingolipid biosynthesis; Glycosphingolipid metabolism; Sphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16880](https://www.uniprot.org/uniprotkb/Q16880) (2-hydroxyacylsphingosine 1-beta-galactosyltransferase):

> Catalyzes the transfer of galactose to ceramide, a key enzymatic step in the biosynthesis of galactocerebrosides, which are abundant sphingolipids of the myelin membrane of the central nervous system and peripheral nervous system. Galactosylates both hydroxy- and non-hydroxy fatty acid-containing ceramides and diglycerides (By similarity).

**Summary**, from NCBI Gene [7368](https://www.ncbi.nlm.nih.gov/gene/7368):

> The protein encoded by this gene belongs to the UDP-glycosyltransferase family. It catalyzes the transfer of galactose to ceramide, a key enzymatic step in the biosynthesis of galactocerebrosides, which are abundant sphingolipids of the myelin membrane of the central and peripheral nervous systems. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:12555](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12555) · Entrez [7368](https://www.ncbi.nlm.nih.gov/gene/7368) · UniProt [Q16880](https://www.uniprot.org/uniprotkb/Q16880) · Ensembl [ENSG00000174607](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174607)

## Data

Gene col 10508: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10508); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10508, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10508]; `tensor/DDL_lfc|DDL_z.npy` [10508]; `embed/gene_vectors.npy` [10508]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10508 or target_col == 10508). Every well: [[UGT8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UGT8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
