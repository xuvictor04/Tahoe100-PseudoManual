---
symbol: "PTGS2"
type: "gene"
col: 1060
ensembl_id: "ENSG00000073756"
name: "prostaglandin-endoperoxide synthase 2"
location: "1q31.1"
module: 112
arm: "+"
pooled_cpm: 90.06
n_lines_expressing: 23
n_dd_up: 18
n_dd_down: 63
n_dd_up_clean: 10
n_dd_down_clean: 59
in_vector_space: true
direction_upstream: 25
direction_downstream: 50
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# PTGS2

*prostaglandin-endoperoxide synthase 2* — 1q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.08× (z +12.4, q 3e-32, up in 18 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 63 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.450× (z -9.5, q 2e-18, down in 18 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CXCL8]] (+0.70, fdr 7e-06), [[IL6]] (+0.70, fdr 7e-06), [[IL1A]] (+0.69, fdr 8e-06); moves opposite to [[CMKLR2]] (-0.49, fdr 3e-05), [[FGD4]] (-0.47, fdr 1e-04).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[ANTXR2]] → it (grade B ⚠); 50 go from it, the strongest it → [[EXT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1060.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.08×** | +12.4 | 3e-32 | 18/21 (A498, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.96×** | +8.0 | 2e-13 | 18/22 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +7.5 | 9e-12 | 7/20 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +7.3 | 5e-11 | 7/22 (HOP62, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +7.0 | 3e-10 | 9/21 (A498, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +5.6 | 2e-06 | 7/20 (LoVo, HOP62, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.52×** | +5.0 | 5e-05 | 15/21 (A498, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.16×** | +4.8 | 1e-04 | 16/22 (LoVo, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.31×** | +4.6 | 3e-04 | 11/21 (HT-29, CFPAC-1, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +4.2 | 0.001 | 10/21 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.38×** | +3.8 | 0.006 | 8/21 (A498, HOP62, …) | all doses, stronger at high dose |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.011 | 10/21 (HS-578T, Hs 766T, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.33×** | +3.4 | 0.026 | 2/21 (RPMI-7951, HS-578T) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.32×** | +3.3 | 0.041 | 13/21 (NCI-H1792, A498, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.048 | 4/23 (HOP62, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Gemcitabine (drug)]] 5 µM |  | **1.43×** | +3.1 | 0.060 | 4/21 (HOP62, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.42×** | +3.0 | 0.096 | 1/21 (HOP62) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.42×** | +3.0 | 0.096 | 2/21 (HS-578T, NCI-H1792) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 65 in all, 5 with an alert ⚠; shown: the 15 strongest. 63 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1060.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.450×** | -9.5 | 2e-18 | 18/21 (C32, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.500×** | -8.2 | 7e-14 | 18/21 (SW 900, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.619×** | -8.0 | 2e-13 | 18/21 (hTERT-HPNE, CHP-212, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.533×** | -7.5 | 1e-11 | 21/21 (SW 900, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.556×** | -6.9 | 4e-10 | 11/21 (NCI-H1792, A498, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.543×** | -6.7 | 2e-09 | 11/21 (C32, H4, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.672×** | -6.6 | 3e-09 | 13/21 (NCI-H1792, A549, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.589×** | -6.5 | 7e-09 | 15/23 (NCI-H2030, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.580×** | -6.4 | 7e-09 | 19/21 (C32, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.588×** | -6.3 | 2e-08 | 19/21 (NCI-H1573, HS-578T, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.595×** | -6.1 | 4e-08 | 16/21 (NCI-H1792, A498, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.601×** | -6.0 | 9e-08 | 12/21 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.702×** | -5.8 | 2e-07 | 12/21 (NCI-H2030, C32, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.617×** | -5.7 | 4e-07 | 13/21 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.601×** | -5.6 | 1e-06 | 9/20 (A549, NCI-H1792, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1060. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 390 | 4 (2 ⚠) | 20 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.43× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.156× (z -12.3) |
| [[HS-578T (line)]] | alt | 126 | 0 | 17 (1 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.0581× (z -14.0) |
| [[A549 (line)]] | wt | 304 | 0 | 14 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.160× (z -11.3) |
| [[C32 (line)]] | wt | 364 | 0 | 13 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -16.1) |
| [[SW 900 (line)]] | alt | 1,870 | 0 | 11 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0610× (z -17.7) |
| [[A498 (line)]] | wt | 28.7 | 5 (2 ⚠) | 3 | [[Tucidinostat (drug)]] 5 µM 13.9× (z +19.2) | [[Clobetasol propionate (drug)]] 0.5 µM 0.141× (z -10.1) |
| [[LoVo (line)]] | wt | 37.4 | 2 (1 ⚠) | 3 | [[TAK-901 (drug)]] 5 µM 26.3× (z +10.3) | [[Belinostat (drug)]] 5 µM 0.196× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 113 | 0 | 5 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.471× (z -16.8) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.217× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 114 | 4 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.87× (z +12.9) | — |
| [[CHP-212 (line)]] | wt | 78.1 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0366× (z -11.6) |
| [[HOP62 (line)]] | alt | 77.0 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 9.23× (z +18.8) | — |
| [[NCI-H1573 (line)]] | alt | 386 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.105× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 169 | 0 | 2 | — | [[Ponatinib (drug)]] 5 µM 0.223× (z -8.9) |
| [[SNU-423 (line)]] | alt | 27.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +11.1) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 4.15× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 30.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +13.1) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[LOX-IMVI (line)]] | wt | 40.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 67.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.19× (z +8.6) | — |
| [[SW 1088 (line)]] | alt | 237 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.05 µM 0.0287× (z -10.8) |
| [[A-172 (line)]] | wt | 5.72 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 18.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.04 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.96 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.89 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 209 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.21 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.98 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.12 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.86 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 19.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.66 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.61 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.28 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.52 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.49 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.81 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.94 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.95 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1060), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXCL8]] | +0.70 | +0.63 / +0.75 | both halves | 7e-06 | pathway: Interleukin-10 signaling; STRING 975 |
| [[IL6]] | +0.70 | +0.64 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 960 |
| [[IL1A]] | +0.69 | +0.58 / +0.73 | both halves | 8e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 823 |
| [[INHBA]] | +0.68 | +0.72 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[IL1B]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP; STRING 974 |
| [[GJA1]] | +0.66 | +0.61 / +0.69 | both halves | 7e-06 | STRING 470 |
| [[IER3]] | +0.64 | +0.58 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 429 |
| [[TFPI2]] | +0.63 | +0.65 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[NPTX1]] | +0.62 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SERPINE2]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[STC1]] | +0.61 | +0.64 / +0.64 | both halves | 7e-06 | STRING 419 |
| [[LIF]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP; STRING 466 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMKLR2]] | -0.49 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[FGD4]] | -0.47 | -0.54 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 7, C 18. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANTXR2]] | B | ANTXR2 activity raises PTGS2's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 4.80× lower at baseline in the lines without ANTXR2 | 0.030 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[BCL11B]] | B | BCL11B activity raises PTGS2's level | lines that do not express BCL11B (18) vs lines expressing it (32) | 3.36× lower at baseline in the lines without BCL11B | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000249111, HLA-V-1, ENSG00000272297; maybe low, not absent |
| [[FAM107B]] | B | FAM107B activity raises PTGS2's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.60× lower at baseline in the lines without FAM107B | 0.063 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[CEMIP]] | B | CEMIP activity raises PTGS2's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 3.59× lower at baseline in the lines without CEMIP | 0.067 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[SMOX]] | B | SMOX activity raises PTGS2's level | lines that do not express SMOX (6) vs lines expressing it (44) | 3.31× lower at baseline in the lines without SMOX | 0.074 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[MEIS1]] | B | MEIS1 activity raises PTGS2's level | lines that do not express MEIS1 (11) vs lines expressing it (39) | 4.21× lower at baseline in the lines without MEIS1 | 0.098 | ⚠ within organs, on part of the lines; also absent: LINC01798, DYNC1I1, CAMK4 |
| [[ANKRD29]] | B | ANKRD29 activity raises PTGS2's level | lines that do not express ANKRD29 (19) vs lines expressing it (31) | 3.76× lower at baseline in the lines without ANKRD29 | 0.099 | ⚠ within organs, on part of the lines; also absent: NHS, PI3, GPR37 |
| [[ANXA10]] | C | ANXA10 activity raises PTGS2's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 6.54× lower at baseline in the lines without ANXA10 | 0.001 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP; co-absent with the target |
| [[SERPINE2]] | C | SERPINE2 activity raises PTGS2's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 5.27× lower at baseline in the lines without SERPINE2 | 0.003 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12; co-absent with the target |
| [[ADAM12]] | C | ADAM12 activity raises PTGS2's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 7.27× lower at baseline in the lines without ADAM12 | 0.010 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |
| [[PLA2G4A]] | C | PLA2G4A activity raises PTGS2's level | lines that do not express PLA2G4A (22) vs lines expressing it (28) | 4.73× lower at baseline in the lines without PLA2G4A | 0.011 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3; co-absent with the target |
| [[BCL2A1]] | C | BCL2A1 activity raises PTGS2's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 6.07× lower at baseline in the lines without BCL2A1 | 0.019 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1; co-absent with the target |

### Downstream of this gene

*50 arrows, 50 of them with an alert ⚠; grade A 0, B 29, C 21. Shown: the 12 strongest; 38 more arrows (38 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EXT1]] | B | PTGS2 activity raises EXT1's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.08× lower at baseline in the lines without PTGS2 | 0.001 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[ARSJ]] | B | PTGS2 activity raises ARSJ's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.92× lower at baseline in the lines without PTGS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[NFKBIZ]] | B | PTGS2 activity raises NFKBIZ's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.02× lower at baseline in the lines without PTGS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[SMOX]] | B | PTGS2 activity raises SMOX's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.86× lower at baseline in the lines without PTGS2 | 0.003 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[TPBG]] | B | PTGS2 activity raises TPBG's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.73× lower at baseline in the lines without PTGS2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[CD82]] | B | PTGS2 activity raises CD82's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.61× lower at baseline in the lines without PTGS2 | 0.010 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[HMGN2P46]] | B | PTGS2 activity raises HMGN2P46's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.73× lower at baseline in the lines without PTGS2 | 0.020 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[SYNJ2]] | B | PTGS2 activity raises SYNJ2's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 1.78× lower at baseline in the lines without PTGS2 | 0.033 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| cells under [[Arbutin (drug)]] 5 µM | B | PTGS2 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express PTGS2 (27) vs lines expressing it (21) | the lines without PTGS2: 0.81× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[IER3]] | B | PTGS2 activity raises IER3's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 1.95× lower at baseline in the lines without PTGS2 | 0.041 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[CEMIP]] | B | PTGS2 activity raises CEMIP's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.46× lower at baseline in the lines without PTGS2 | 0.042 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[ANTXR2]] | B | PTGS2 activity raises ANTXR2's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.43× lower at baseline in the lines without PTGS2 | 0.042 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.709). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.1, 14.2); signed map (18.9, 51.0). **Vector** length 110, 33.3% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *inflammatory response* (hallmark, mean cos +0.61 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +12.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.2 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +0.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.3 | +0.1 |
|  | [[Thymol (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | -0.4 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -5.0 | -7.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.4 | -6.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.3 | -8.0 |
|  | [[NG25 (drug)]] 5 µM |  | -4.0 | -3.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.8 | -5.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.8 | -6.6 |

## What is on record

|  |  |
|---|---|
| Name | prostaglandin-endoperoxide synthase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q31.1 — chr1:186,671,791-186,680,922 (-) |
| Ensembl biotype | protein_coding |
| Also known as | COX2 |
| Gene groups (HGNC) | Prostaglandin-endoperoxide synthase family |
| Hallmark sets | KRAS_SIGNALING_UP, INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 12 pathways, smallest: Synthesis of 15-eicosatetraenoic acid derivatives; Biosynthesis of EPA-derived SPMs; Biosynthesis of DHA-derived SPMs |
| Matched by | ensembl_id |

**Function**, from UniProt [P35354](https://www.uniprot.org/uniprotkb/P35354) (Prostaglandin G/H synthase 2):

> Dual cyclooxygenase and peroxidase in the biosynthesis pathway of prostanoids, a class of C20 oxylipins mainly derived from arachidonate ((5Z,8Z,11Z,14Z)-eicosatetraenoate, AA, C20:4(n-6)), with a particular role in the inflammatory response. The cyclooxygenase activity oxygenates AA to the hydroperoxy endoperoxide prostaglandin G2 (PGG2), and the peroxidase activity reduces PGG2 to the hydroxy endoperoxide prostaglandin H2 (PGH2), the precursor of all 2-series prostaglandins and thromboxanes. …

**Summary**, from NCBI Gene [5743](https://www.ncbi.nlm.nih.gov/gene/5743):

> Prostaglandin-endoperoxide synthase (PTGS), also known as cyclooxygenase, is the key enzyme in prostaglandin biosynthesis, and acts both as a dioxygenase and as a peroxidase. There are two isozymes of PTGS: a constitutive PTGS1 and an inducible PTGS2, which differ in their regulation of expression and tissue distribution. This gene encodes the inducible isozyme. It is regulated by specific stimulatory events, suggesting that it is responsible for the prostanoid biosynthesis involved in …

**Accessions** — [HGNC:9605](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9605) · Entrez [5743](https://www.ncbi.nlm.nih.gov/gene/5743) · UniProt [P35354](https://www.uniprot.org/uniprotkb/P35354) · Ensembl [ENSG00000073756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073756)

## Data

Gene col 1060: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1060); `tables/drug_effects.parquet` (83 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1060, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1060]; `tensor/DDL_lfc|DDL_z.npy` [1060]; `embed/gene_vectors.npy` [1060]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1060 or target_col == 1060). Every well: [[PTGS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTGS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
