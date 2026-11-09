---
symbol: "EPSTI1"
type: "gene"
col: 5415
ensembl_id: "ENSG00000133106"
name: "epithelial stromal interaction 1"
location: "13q14.11"
module: 32
arm: "+"
pooled_cpm: 71.39
n_lines_expressing: 25
n_dd_up: 18
n_dd_down: 33
n_dd_up_clean: 16
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 38
direction_downstream: 96
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# EPSTI1

*epithelial stromal interaction 1* — 13q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 2.18× (z +7.9, q 1e-12, up in 22 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.205× (z -16.8, q 0e+00, down in 23 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XAF1]] (+0.93, fdr 7e-06), [[OAS2]] (+0.91, fdr 7e-06), [[SAMD9L]] (+0.91, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 38 arrows point to it, the strongest [[CTSS]] → it (grade B ⚠); 96 go from it, the strongest it → [[IFI44]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5415.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **2.18×** | +7.9 | 1e-12 | 22/22 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +5.6 | 5e-06 | 3/24 (J82, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **1.64×** | +5.4 | 2e-05 | 21/24 (Hs 766T, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.51×** | +5.1 | 4e-05 | 19/23 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.62×** | +5.1 | 4e-05 | 21/22 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.46×** | +5.1 | 4e-05 | 21/23 (Hs 766T, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.63×** | +5.0 | 6e-05 | 20/23 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.38×** | +4.6 | 4e-04 | 21/24 (Hs 766T, Panc 03.27, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +4.3 | 0.001 | 19/23 (NCI-H2347, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.50×** | +4.3 | 0.001 | 18/24 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.48×** | +3.9 | 0.004 | 17/23 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.010 | 18/25 (CFPAC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +3.3 | 0.037 | 2/19 (J82, LS 180) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[venetoclax (drug)]] 0.05 µM |  | **1.39×** | +3.3 | 0.039 | 17/24 (Panc 03.27, AsPC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.099 | 11/23 (AsPC-1, HS-578T, …) | rises with dose |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.099 | 9/23 (A498, SNU-423, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.099 | 20/23 (AsPC-1, CFPAC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 4 with an alert ⚠; shown: the 15 strongest. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5415.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.205×** | -16.8 | 0e+00 | 23/23 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.278×** | -13.5 | 3e-39 | 22/23 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.292×** | -13.0 | 2e-36 | 23/23 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.459×** | -11.7 | 3e-29 | 21/23 (CFPAC-1, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.371×** | -10.5 | 1e-23 | 21/23 (SNU-423, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.394×** | -9.9 | 5e-21 | 22/23 (LoVo, SNU-423, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.534×** | -9.4 | 5e-19 | 20/24 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.430×** | -8.5 | 2e-15 | 21/23 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.458×** | -8.3 | 9e-15 | 20/23 (LoVo, A498, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.595×** | -7.8 | 5e-13 | 20/24 (LoVo, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.500×** | -7.3 | 1e-11 | 21/23 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.521×** | -6.9 | 2e-10 | 22/24 (RPMI-7951, LoVo, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.546×** | -6.4 | 7e-09 | 21/24 (LoVo, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.572×** | -5.9 | 1e-07 | 20/23 (COLO 205, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.683×** | -5.7 | 4e-07 | 20/24 (Panc 03.27, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5415. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 182 | 0 | 24 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0303× (z -26.7) |
| [[SNU-423 (line)]] | alt | 137 | 0 | 21 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0423× (z -23.1) |
| [[A498 (line)]] | wt | 109 | 0 | 17 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0490× (z -20.0) |
| [[RPMI-7951 (line)]] | alt | 217 | 0 | 17 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0444× (z -23.8) |
| [[A-172 (line)]] | wt | 97.3 | 2 (1 ⚠) | 14 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 5.01× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.0458× (z -20.5) |
| [[COLO 205 (line)]] | alt | 1,879 | 0 | 16 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0285× (z -32.3) |
| [[NCI-H2347 (line)]] | alt | 63.9 | 4 (2 ⚠) | 12 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.17× (z +11.9) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.86× (z +11.5) | [[Tofacitinib (drug)]] 5 µM 0.195× (z -16.7) |
| [[KATO III (line)]] | alt | 124 | 0 | 13 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0663× (z -17.8) |
| [[NCI-H1792 (line)]] | alt | 45.5 | 0 | 13 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0581× (z -16.4) |
| [[NCI-H23 (line)]] | alt | 53.0 | 0 | 13 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.116× (z -15.7) |
| [[HS-578T (line)]] | alt | 63.9 | 1 (1 ⚠) | 11 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.02× (z +9.2) ⚠ cell-cycle shift, explains ~11% of this change | [[Belinostat (drug)]] 5 µM 0.0589× (z -18.7) |
| [[Panc 03.27 (line)]] | alt | 184 | 0 | 12 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.113× (z -16.3) |
| [[CFPAC-1 (line)]] | alt | 104 | 0 | 11 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.131× (z -17.9) |
| [[AsPC-1 (line)]] | alt | 107 | 0 | 9 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.119× (z -19.0) |
| [[Hs 766T (line)]] | wt | 97.7 | 0 | 8 | — | [[Panobinostat (drug)]] 5 µM 0.0929× (z -16.0) |
| [[HepG2_C3A (line)]] | wt | 71.3 | 0 | 7 | — | [[Belinostat (drug)]] 5 µM 0.0518× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 37.1 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -14.2) |
| [[J82 (line)]] | alt | 62.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.91× (z +12.2) ⚠ toxic; transcription drop | [[Tofacitinib (drug)]] 5 µM 0.263× (z -11.1) |
| [[SW 900 (line)]] | alt | 64.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.124× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 0 | 3 | — | [[Belinostat (drug)]] 0.5 µM 0.0794× (z -12.0) |
| [[SW1417 (line)]] | alt | 56.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -11.8) |
| [[LS 180 (line)]] | wt | 24.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -10.6) |
| [[A-427 (line)]] | wt | 4.78 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.15 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.97 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.20 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.08 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.41 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.86 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.75 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.37 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.53 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.04 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 9.54 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.71 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.10 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.02 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.89 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.09 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.95 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5415), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XAF1]] | +0.93 | +0.85 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 862 |
| [[OAS2]] | +0.91 | +0.83 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 891 |
| [[SAMD9L]] | +0.91 | +0.81 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 890 |
| [[MX2]] | +0.91 | +0.83 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 667 |
| [[TRIM22]] | +0.91 | +0.88 / +0.90 | both halves | 7e-06 | STRING 550 |
| [[IFIT3]] | +0.90 | +0.81 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 897 |
| [[SLC15A3]] | +0.90 | +0.84 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[MX1]] | +0.90 | +0.83 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 915 |
| [[IFI35]] | +0.89 | +0.81 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 661 |
| [[OAS1]] | +0.89 | +0.79 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 808 |
| [[IFI44L]] | +0.89 | +0.79 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 921 |
| [[IFI44]] | +0.88 | +0.77 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 909 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 19, C 19. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSS]] | B | CTSS activity raises EPSTI1's level | lines that do not express CTSS (15) vs lines expressing it (35) | 4.51× lower at baseline in the lines without CTSS | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[FBXO39]] | B | FBXO39 activity raises EPSTI1's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 3.67× lower at baseline in the lines without FBXO39 | 0.013 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[OASL]] | B | OASL activity raises EPSTI1's level | lines that do not express OASL (10) vs lines expressing it (40) | 4.61× lower at baseline in the lines without OASL | 0.019 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[SLC15A3]] | B | SLC15A3 activity raises EPSTI1's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 3.74× lower at baseline in the lines without SLC15A3 | 0.022 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[IFI44]] | B | IFI44 activity raises EPSTI1's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 3.47× lower at baseline in the lines without IFI44 | 0.024 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[GBP1]] | B | GBP1 activity raises EPSTI1's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 3.40× lower at baseline in the lines without GBP1 | 0.025 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[ETV7]] | B | ETV7 activity raises EPSTI1's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 3.05× lower at baseline in the lines without ETV7 | 0.026 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[XAF1]] | B | XAF1 activity raises EPSTI1's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 3.61× lower at baseline in the lines without XAF1 | 0.038 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[BST2]] | B | BST2 activity raises EPSTI1's level | lines that do not express BST2 (18) vs lines expressing it (32) | 3.24× lower at baseline in the lines without BST2 | 0.052 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[MAP2K1]] | B | MAP2K1 activity lowers EPSTI1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[IFI6]] | B | IFI6 activity raises EPSTI1's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 3.35× lower at baseline in the lines without IFI6 | 0.057 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[CMPK2]] | B | CMPK2 activity raises EPSTI1's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.71× lower at baseline in the lines without CMPK2 | 0.064 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |

### Downstream of this gene

*96 arrows, 96 of them with an alert ⚠; grade A 0, B 79, C 17. Shown: the 12 strongest; 84 more arrows (84 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI44]] | B | EPSTI1 activity raises IFI44's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 3.36× lower at baseline in the lines without EPSTI1 | 0.001 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[UBA7]] | B | EPSTI1 activity raises UBA7's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.35× lower at baseline in the lines without EPSTI1 | 0.002 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[RSAD2]] | B | EPSTI1 activity raises RSAD2's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 3.74× lower at baseline in the lines without EPSTI1 | 0.002 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[NLRC5]] | B | EPSTI1 activity raises NLRC5's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.17× lower at baseline in the lines without EPSTI1 | 0.004 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[DDX60]] | B | EPSTI1 activity raises DDX60's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.51× lower at baseline in the lines without EPSTI1 | 0.005 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[HERC6]] | B | EPSTI1 activity raises HERC6's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.22× lower at baseline in the lines without EPSTI1 | 0.006 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[MX2]] | B | EPSTI1 activity raises MX2's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 4.23× lower at baseline in the lines without EPSTI1 | 0.006 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[OASL]] | B | EPSTI1 activity raises OASL's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.80× lower at baseline in the lines without EPSTI1 | 0.006 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[GBP1]] | B | EPSTI1 activity raises GBP1's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 3.60× lower at baseline in the lines without EPSTI1 | 0.006 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[XAF1]] | B | EPSTI1 activity raises XAF1's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 4.02× lower at baseline in the lines without EPSTI1 | 0.006 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[APOL6]] | B | EPSTI1 activity raises APOL6's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.60× lower at baseline in the lines without EPSTI1 | 0.007 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[MYD88]] | B | EPSTI1 activity raises MYD88's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 1.95× lower at baseline in the lines without EPSTI1 | 0.007 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.917). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.7, 53.1); signed map (63.9, 31.0). **Vector** length 143, 51.2% of its response variance represented; |z| ≥ 3 in 1,101 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.85 to 23); *Interferon Signaling* (reactome, mean cos +0.80 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.82 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.2 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +7.2 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.9 | +7.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.6 | +5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.4 | +5.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.4 | +5.4 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -7.6 | -7.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -7.1 | -6.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.0 | -11.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -6.6 | -6.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -6.4 | -9.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -5.9 | -8.3 |

## What is on record

|  |  |
|---|---|
| Name | epithelial stromal interaction 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.11 — chr13:42,886,388-42,992,271 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BRESI1, MGC29634 |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 4 pathways, smallest: RND1 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96J88](https://www.uniprot.org/uniprotkb/Q96J88) (Epithelial-stromal interaction protein 1):

> Plays a role in M1 macrophage polarization and is required for the proper regulation of gene expression during M1 versus M2 macrophage differentiation (By similarity). Might play a role in RELA/p65 and STAT1 phosphorylation and nuclear localization upon activation of macrophages (By similarity).

**Summary**, from NCBI Gene [94240](https://www.ncbi.nlm.nih.gov/gene/94240):

> The protein encoded by this gene has been shown to promote tumor invasion and metastasis in some invasive cancer cells when overexpressed. Expression of this gene has been shown to be upregulated by direct binding of the Kruppel like factor 8 protein to promoter sequences. The translated protein interacts with the amino terminal region of the valosin containing protein gene product, resulting in the nuclear translocation of the nuclear factor kappa B subunit 1 gene product, and activation of …

**Accessions** — [HGNC:16465](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16465) · Entrez [94240](https://www.ncbi.nlm.nih.gov/gene/94240) · UniProt [Q96J88](https://www.uniprot.org/uniprotkb/Q96J88) · Ensembl [ENSG00000133106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133106)

## Data

Gene col 5415: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5415); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5415, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5415]; `tensor/DDL_lfc|DDL_z.npy` [5415]; `embed/gene_vectors.npy` [5415]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5415 or target_col == 5415). Every well: [[EPSTI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPSTI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
