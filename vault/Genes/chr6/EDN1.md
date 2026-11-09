---
symbol: "EDN1"
type: "gene"
col: 1222
ensembl_id: "ENSG00000078401"
name: "endothelin 1"
location: "6p24.1"
module: 123
arm: "+"
pooled_cpm: 32.79
n_lines_expressing: 23
n_dd_up: 24
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 28
direction_downstream: 47
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# EDN1

*endothelin 1* — 6p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.99× (z +13.0, q 5e-36, up in 16 of 21 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 16.5× (z +12.3, q 2e-32, up in 21 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.475× (z -6.2, q 2e-07, down in 19 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AMOTL2]] (+0.68, fdr 7e-06), [[LATS2]] (+0.66, fdr 1e-05), [[SHROOM3]] (+0.64, fdr 7e-06); moves opposite to [[HYKK]] (-0.51, fdr 2e-04), [[LIMK1]] (-0.50, fdr 3e-05), [[NAP1L4]] (-0.46, fdr 5e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[USP43]] → it (grade B ⚠); 47 go from it, the strongest it → [[WWC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1222.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **2.99×** | +13.0 | 5e-36 | 16/21 (CFPAC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **16.5×** | +12.3 | 2e-32 | 21/22 (PANC-1, A549, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.78×** | +8.6 | 2e-15 | 14/21 (CFPAC-1, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.86×** | +8.5 | 3e-15 | 14/21 (A549, J82, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.43×** | +7.2 | 9e-11 | 9/19 (J82, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.26×** | +6.8 | 8e-10 | 11/20 (PANC-1, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.19×** | +6.6 | 3e-09 | 13/21 (A549, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +5.4 | 4e-06 | 8/20 (A549, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.84×** | +5.1 | 2e-05 | 14/21 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.85×** | +5.0 | 4e-05 | 16/21 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.55×** | +4.1 | 0.002 | 12/20 (SW48, NCI-H2347, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.60×** | +4.0 | 0.003 | 11/21 (A549, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.57×** | +3.8 | 0.007 | 12/20 (PANC-1, BT-474, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.007 | 5/21 (PANC-1, J82, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **2.55×** | +3.5 | 0.018 | 11/20 (NCI-H1573, PANC-1, …) | rises with dose | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.55×** | +3.4 | 0.023 | 12/21 (BT-474, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.023 | 8/21 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **2.11×** | +3.3 | 0.031 | 10/20 (NCI-H1573, HT-29, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.063 | 12/20 (NCI-H1573, A549, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.0 | 0.075 | 9/21 (A549, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.41×** | +2.9 | 0.097 | 13/21 (HT-29, LS 180, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1222.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.475×** | -6.2 | 2e-07 | 19/21 (A549, SW48, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.623×** | -4.0 | 0.020 | 19/21 (CFPAC-1, A549, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.630×** | -3.7 | 0.036 | 13/20 (A-427, SW48, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.649×** | -3.6 | 0.041 | 18/21 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.653×** | -3.6 | 0.041 | 13/20 (SW48, A-427, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.88 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1222. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 82.1 | 2 | 10 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 35.0× (z +9.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0271× (z -17.3) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0443× (z -15.5) |
| [[A549 (line)]] | wt | 64.2 | 7 (4 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +21.3) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 10.2× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.0868× (z -15.9) |
| [[CFPAC-1 (line)]] | alt | 140 | 4 (3 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.80× (z +24.9) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 22.2× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -15.7) |
| [[LoVo (line)]] | wt | 55.8 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0782× (z -14.7) |
| [[KATO III (line)]] | alt | 108 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0840× (z -14.7) |
| [[HT-29 (line)]] | alt | 69.3 | 0 | 6 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0816× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.147× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 70.6 | 4 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 9.49× (z +16.3) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 60.8× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -10.1) |
| [[A-427 (line)]] | wt | 233 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 22.1× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.167× (z -11.4) |
| [[PANC-1 (line)]] | alt | 32.7 | 4 (3 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 169× (z +16.7) | [[Panobinostat (drug)]] 5 µM 0.165× (z -11.2) |
| [[J82 (line)]] | alt | 45.8 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +14.9) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[NCI-H1573 (line)]] | alt | 35.3 | 3 (2 ⚠) | 1 | [[Peretinoin (drug)]] 5 µM 7.71× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.134× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 53.6 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 49.0× (z +12.9) | — |
| [[AsPC-1 (line)]] | alt | 46.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0695× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.124× (z -10.7) |
| [[BT-474 (line)]] | alt | 26.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.70× (z +11.9) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 63.1× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 37.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.118× (z -9.7) |
| [[SW1417 (line)]] | alt | 143 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.210× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0896× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 16.3 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 8.29× (z +9.2) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[A-172 (line)]] | wt | 4.67 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.78 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.04 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.40 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.11 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.43 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.09 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.55 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.78 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.79 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1222), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AMOTL2]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[LATS2]] | +0.66 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[SHROOM3]] | +0.64 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[ZFP36L2]] | +0.64 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[LINC01186]] | +0.60 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[RHOU]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[IL18]] | +0.59 | +0.50 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 451 |
| [[WWC1]] | +0.58 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[FOXQ1]] | +0.55 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[KLF4]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[PRKCH-AS1]] | +0.54 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[C6orf132]] | +0.54 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HYKK]] | -0.51 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[LIMK1]] | -0.50 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[NAP1L4]] | -0.46 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[BCAP31]] | -0.46 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[ST6GALNAC6]] | -0.45 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[DCUN1D4]] | -0.45 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[HSPB11]] | -0.45 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[CRYBB2P1]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 9, C 19. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[USP43]] | B | USP43 activity raises EDN1's level | lines that do not express USP43 (10) vs lines expressing it (40) | 4.06× lower at baseline in the lines without USP43 | 0.024 | ⚠ within organs, on part of the lines; also absent: LLGL2, KRTAP5-AS1, BTG3-AS1 |
| [[SH3RF2]] | B | SH3RF2 activity raises EDN1's level | lines that do not express SH3RF2 (16) vs lines expressing it (34) | 4.59× lower at baseline in the lines without SH3RF2 | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC01564, CAPG, LINC00857; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises EDN1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[WWC1]] | B | WWC1 activity raises EDN1's level | lines that do not express WWC1 (13) vs lines expressing it (37) | 3.89× lower at baseline in the lines without WWC1 | 0.045 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CHMP4C, LSR; maybe low, not absent |
| [[ANK3]] | B | ANK3 activity raises EDN1's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 2.45× lower at baseline in the lines without ANK3 | 0.057 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[PLK2]] | B | PLK2 activity raises EDN1's level | lines that do not express PLK2 (6) vs lines expressing it (44) | 4.36× lower at baseline in the lines without PLK2 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with ZFHX3, POLE |
| [[LINC01186]] | B | LINC01186 activity raises EDN1's level | lines that do not express LINC01186 (12) vs lines expressing it (38) | 3.37× lower at baseline in the lines without LINC01186 | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC01836, STXBP2, EEPD1 |
| [[SHROOM3]] | B | SHROOM3 activity raises EDN1's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 2.50× lower at baseline in the lines without SHROOM3 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[MARVELD2]] | B | MARVELD2 activity raises EDN1's level | lines that do not express MARVELD2 (14) vs lines expressing it (36) | 4.27× lower at baseline in the lines without MARVELD2 | 0.096 | ⚠ within organs, on part of the lines; also absent: CHMP4C, ARHGEF5, LLGL2; maybe low, not absent |
| [[LINC02331]] | C | LINC02331 activity raises EDN1's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 3.96× lower at baseline in the lines without LINC02331 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2; co-absent with the target |
| [[IL18]] | C | IL18 activity raises EDN1's level | lines that do not express IL18 (18) vs lines expressing it (32) | 5.21× lower at baseline in the lines without IL18 | 0.006 | ⚠ within organs, on part of the lines; also absent: LSR, SPINT2, LAMA3; co-absent with the target |
| [[GRHL2]] | C | GRHL2 activity raises EDN1's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 5.38× lower at baseline in the lines without GRHL2 | 0.006 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent with the target |

### Downstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 25, C 22. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WWC1]] | B | EDN1 activity raises WWC1's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 3.36× lower at baseline in the lines without EDN1 | 0.001 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[MARVELD2]] | B | EDN1 activity raises MARVELD2's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 3.24× lower at baseline in the lines without EDN1 | 0.005 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[TMEM265]] | B | EDN1 activity raises TMEM265's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 2.00× lower at baseline in the lines without EDN1 | 0.005 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[USP43]] | B | EDN1 activity raises USP43's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 3.00× lower at baseline in the lines without EDN1 | 0.005 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[KLF3]] | B | EDN1 activity raises KLF3's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 1.90× lower at baseline in the lines without EDN1 | 0.007 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[ZFP36L2]] | B | EDN1 activity raises ZFP36L2's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 1.98× lower at baseline in the lines without EDN1 | 0.013 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| cells under [[Docetaxel (Trihydrate) (drug)]] 5 µM | B | EDN1 activity raises the cells' numbers under Docetaxel (Trihydrate) 5 µM (protects the cells) | lines that do not express EDN1 (27) vs lines expressing it (21) | the lines without EDN1: 0.81× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[MUC12]] | B | EDN1 activity raises MUC12's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 1.85× lower at baseline in the lines without EDN1 | 0.032 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[CFLAR-AS1]] | B | EDN1 activity raises CFLAR-AS1's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 1.58× lower at baseline in the lines without EDN1 | 0.032 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[DCUN1D4]] | B | EDN1 activity lowers DCUN1D4's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 1.39× higher at baseline in the lines without EDN1 | 0.040 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[RHOU]] | B | EDN1 activity raises RHOU's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 1.79× lower at baseline in the lines without EDN1 | 0.046 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[KLF4]] | B | EDN1 activity raises KLF4's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 2.00× lower at baseline in the lines without EDN1 | 0.053 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.652). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.7, 12.5); signed map (49.1, 14.9). **Vector** length 91.4, 28.9% of its response variance represented; |z| ≥ 3 in 767 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Signaling by Hippo* (reactome, mean cos +0.64 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +12.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +5.5 | +13.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +4.4 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.2 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.3 | +5.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -2.6 | +3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -1.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.0 | -6.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.8 | -0.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | endothelin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.1 — chr6:12,290,361-12,297,194 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ET1 |
| Gene groups (HGNC) | Endothelins |
| Hallmark sets | KRAS_SIGNALING_DN, INFLAMMATORY_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 8 pathways, smallest: Transcriptional and post-translational regulation of MITF-M expression and activity; Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [P05305](https://www.uniprot.org/uniprotkb/P05305) (Endothelin-1):

> Endothelins are endothelium-derived vasoconstrictor peptides (By similarity). Probable ligand for G protein-coupled receptors EDNRA and EDNRB which activates PTK2B, BCAR1, BCAR3 and, GTPases RAP1 and RHOA cascade in glomerular mesangial cells. Also binds the DEAR/FBXW7-AS1 receptor. Promotes mesenteric arterial wall remodeling via activation of ROCK signaling and subsequent colocalization of NFATC3 with F-actin filaments (By similarity). NFATC3 then translocates to the nucleus where it …

**Summary**, from NCBI Gene [1906](https://www.ncbi.nlm.nih.gov/gene/1906):

> This gene encodes a preproprotein that is proteolytically processed to generate a secreted peptide that belongs to the endothelin/sarafotoxin family. This peptide is a potent vasoconstrictor and its cognate receptors are therapeutic targets in the treatment of pulmonary arterial hypertension. Aberrant expression of this gene may promote tumorigenesis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2015]

**Accessions** — [HGNC:3176](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3176) · Entrez [1906](https://www.ncbi.nlm.nih.gov/gene/1906) · UniProt [P05305](https://www.uniprot.org/uniprotkb/P05305) · Ensembl [ENSG00000078401](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078401)

## Data

Gene col 1222: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1222); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1222, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1222]; `tensor/DDL_lfc|DDL_z.npy` [1222]; `embed/gene_vectors.npy` [1222]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1222 or target_col == 1222). Every well: [[EDN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EDN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
