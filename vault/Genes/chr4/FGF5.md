---
symbol: "FGF5"
type: "gene"
col: 6212
ensembl_id: "ENSG00000138675"
name: "fibroblast growth factor 5"
location: "4q21.21"
module: 13
arm: "+"
pooled_cpm: 10.68
n_lines_expressing: 22
n_dd_up: 28
n_dd_down: 19
n_dd_up_clean: 18
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 33
direction_downstream: 32
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# FGF5

*fibroblast growth factor 5* — 4q21.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.51× (z +14.9, q 0e+00, up in 10 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.559× (z -6.7, q 1e-08, down in 9 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAMTS6]] (+0.70, fdr 7e-06), [[EVA1A]] (+0.69, fdr 7e-06), [[RDUR]] (+0.69, fdr 7e-06); moves opposite to [[TSC22D3]] (-0.58, fdr 1e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 33 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 32 go from it, the strongest it → [[FMNL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6212.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.51×** | +14.9 | 0e+00 | 10/19 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.17×** | +12.7 | 2e-34 | 8/12 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.62×** | +11.0 | 6e-26 | 7/14 (hTERT-HPNE, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +9.7 | 3e-20 | 6/18 (RPMI-7951, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.69×** | +8.9 | 9e-17 | 6/13 (MIA PaCa-2, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.64×** | +8.0 | 1e-13 | 13/19 (SW 900, H4, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.98×** | +7.5 | 4e-12 | 10/18 (hTERT-HPNE, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.96×** | +7.1 | 9e-11 | 11/17 (SW 900, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +7.0 | 1e-10 | 4/20 (PANC-1, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +5.7 | 6e-07 | 8/18 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.63×** | +5.6 | 1e-06 | 13/19 (C32, SW 900, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +5.5 | 2e-06 | 6/18 (HS-578T, MIA PaCa-2, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.92×** | +5.3 | 4e-06 | 9/17 (SW 900, H4, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.61×** | +5.2 | 7e-06 | 14/18 (A-172, C32, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.57×** | +5.2 | 9e-06 | 12/18 (HS-578T, SW 900, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.009 | 4/20 (MIA PaCa-2, RKO, …) | top dose only |  |
| [[Elagolix sodium (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.026 | 0/18 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.034 | 4/17 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.0 | 0.062 | 6/18 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6212.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.559×** | -6.7 | 1e-08 | 9/18 (A-172, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.592×** | -6.0 | 5e-07 | 10/18 (A-172, HOP62, …) | two highest doses | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.601×** | -5.9 | 9e-07 | 7/18 (HOP62, H4, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.630×** | -5.3 | 2e-05 | 10/19 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.638×** | -5.0 | 7e-05 | 11/18 (A-172, J82, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.655×** | -4.9 | 1e-04 | 12/18 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.633×** | -4.9 | 1e-04 | 10/17 (RKO, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.687×** | -4.3 | 1e-03 | 8/18 (A-172, H4, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.902× | -4.3 | 1e-03 | 4/20 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **0.691×** | -4.3 | 0.001 | 11/20 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.697×** | -4.2 | 0.002 | 10/19 (A-172, HOP62, …) | two highest doses | position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -3.9 | 0.004 | 7/18 (A-172, HOP62, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.717×** | -3.8 | 0.006 | 6/18 (H4, A-172, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.802×** | -3.6 | 0.012 | 10/19 (A-172, HOP62, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.735×** | -3.6 | 0.014 | 7/19 (A-172, hTERT-HPNE, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.725×** | -3.4 | 0.022 | 8/18 (A-172, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6212. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 43.1 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.126× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Budesonide (drug)]] 0.5 µM 0.132× (z -12.5) |
| [[HOP62 (line)]] | alt | 20.8 | 0 | 4 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.583× (z -9.9) ⚠ position not correctable · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 0.188× (z -9.2) |
| [[SW 900 (line)]] | alt | 8.87 | 1 | 2 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 5.22× (z +9.0) | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0495× (z -11.6) |
| [[hTERT-HPNE (line)]] | wt | 140 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0886× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 38.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0848× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.08× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 17.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +8.5) | — |
| [[RKO (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.687 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.789 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.920 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.797 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.898 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.670 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.682 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 134 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.689 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.739 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.765 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.961 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.941 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.818 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.726 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.684 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6212), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS6]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[EVA1A]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[RDUR]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[SAMD3]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[LINC00973]] | +0.66 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[NAV3]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[TMEM200A]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[PDCD1LG2]] | +0.63 | +0.58 / +0.64 | both halves | 8e-06 | same gene group |
| [[IL11]] | +0.63 | +0.55 / +0.66 | both halves | 1e-05 | STRING 447 |
| [[NTNG1]] | +0.63 | +0.54 / +0.69 | both halves | 1e-05 | **novel candidate** |
| [[SCHIP1]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[VEPH1]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D3]] | -0.58 | -0.55 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 1, C 32. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers FGF5's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.8% of all compounds | 0.028 | ⚠ off-target possible; 3 compounds |
| [[CFAP299]] | C | CFAP299 activity raises FGF5's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 6.31× lower at baseline in the lines without CFAP299 | 3e-04 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2; co-absent with the target |
| [[SPOCD1]] | C | SPOCD1 activity raises FGF5's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 5.01× lower at baseline in the lines without SPOCD1 | 0.001 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1; co-absent with the target |
| [[LINC00702]] | C | LINC00702 activity raises FGF5's level | lines that do not express LINC00702 (25) vs lines expressing it (25) | 5.64× lower at baseline in the lines without LINC00702 | 0.002 | ⚠ within organs, on part of the lines; also absent: FGF5, ENSG00000253553, LNCOG; co-absent with the target |
| [[PSG5]] | C | PSG5 activity raises FGF5's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 6.09× lower at baseline in the lines without PSG5 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises FGF5's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 5.68× lower at baseline in the lines without INSYN2B | 0.005 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[VEPH1]] | C | VEPH1 activity raises FGF5's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 3.43× lower at baseline in the lines without VEPH1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC; co-absent with the target |
| [[LAMA1]] | C | LAMA1 activity raises FGF5's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 4.32× lower at baseline in the lines without LAMA1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1; co-absent with the target |
| [[DGKI]] | C | DGKI activity raises FGF5's level | lines that do not express DGKI (27) vs lines expressing it (23) | 3.73× lower at baseline in the lines without DGKI | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent; co-absent with the target |
| [[MIR155HG]] | C | MIR155HG activity raises FGF5's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 4.02× lower at baseline in the lines without MIR155HG | 0.010 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises FGF5's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 4.06× lower at baseline in the lines without FRMD4A | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[ADTRP]] | C | ADTRP activity raises FGF5's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 4.34× lower at baseline in the lines without ADTRP | 0.015 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2; co-absent with the target |

### Downstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 10, C 22. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FMNL3]] | B | FGF5 activity raises FMNL3's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 3.26× lower at baseline in the lines without FGF5 | 0.003 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702 |
| [[CD44]] | B | FGF5 activity raises CD44's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 4.52× lower at baseline in the lines without FGF5 | 0.006 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702 |
| [[RGMB]] | B | FGF5 activity raises RGMB's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 2.09× lower at baseline in the lines without FGF5 | 0.009 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702 |
| [[NOTCH2]] | B | FGF5 activity raises NOTCH2's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 2.02× lower at baseline in the lines without FGF5 | 0.035 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702 |
| [[ETS1]] | B | FGF5 activity raises ETS1's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 3.04× lower at baseline in the lines without FGF5 | 0.049 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702 |
| [[TRIO]] | B | FGF5 activity raises TRIO's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 1.81× lower at baseline in the lines without FGF5 | 0.050 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702 |
| [[EVC]] | B | FGF5 activity raises EVC's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 3.04× lower at baseline in the lines without FGF5 | 0.063 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702 |
| [[EVA1A]] | B | FGF5 activity raises EVA1A's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 2.76× lower at baseline in the lines without FGF5 | 0.066 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702 |
| [[RGMB]] | B | FGF5 activity weakens RGMB's drug response | lines that do not express FGF5 (27) vs lines expressing it (20) | the lines without FGF5 respond 2.03× as strongly (z diff -1.57); strongest at Idarubicin (hydrochloride) 5 µM: 2.16x vs 0.95x (z diff -6.3) | 0.068 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702; target measured in part of the lines; artifact flags |
| [[GPR68]] | B | FGF5 activity raises GPR68's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 2.01× lower at baseline in the lines without FGF5 | 0.099 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702 |
| [[CFAP299]] | C | FGF5 activity raises CFAP299's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 4.44× lower at baseline in the lines without FGF5 | 4e-04 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702; co-absent with the target |
| [[INSYN2B]] | C | FGF5 activity raises INSYN2B's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 7.37× lower at baseline in the lines without FGF5 | 7e-04 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.566). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.6, 13.6); signed map (17.8, 46.7). **Vector** length 70.3, 22.6% of its response variance represented; |z| ≥ 3 in 557 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +14.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +9.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +8.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +7.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -6.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.6 | -3.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.5 | -3.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.5 | -5.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.4 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | fibroblast growth factor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.21 — chr4:80,266,639-80,336,680 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Receptor ligands; Fibroblast growth factor family |
| Reactome | 57 pathways, smallest: FGFRL1 modulation of FGFR1 signaling; Signaling by activated point mutants of FGFR1; Activated point mutants of FGFR2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P12034](https://www.uniprot.org/uniprotkb/P12034) (Fibroblast growth factor 5):

> Plays an important role in the regulation of cell proliferation and cell differentiation. Required for normal regulation of the hair growth cycle. Functions as an inhibitor of hair elongation by promoting progression from anagen, the growth phase of the hair follicle, into catagen the apoptosis-induced regression phase (By similarity).

**Summary**, from NCBI Gene [2250](https://www.ncbi.nlm.nih.gov/gene/2250):

> The protein encoded by this gene is a member of the fibroblast growth factor (FGF) family. FGF family members possess broad mitogenic and cell survival activities, and are involved in a variety of biological processes, including embryonic development, cell growth, morphogenesis, tissue repair, tumor growth and invasion. This gene was identified as an oncogene, which confers transforming potential when transfected into mammalian cells. Targeted disruption of the homolog of this gene in mouse …

**Accessions** — [HGNC:3683](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3683) · Entrez [2250](https://www.ncbi.nlm.nih.gov/gene/2250) · UniProt [P12034](https://www.uniprot.org/uniprotkb/P12034) · Ensembl [ENSG00000138675](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138675)

## Data

Gene col 6212: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6212); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6212, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6212]; `tensor/DDL_lfc|DDL_z.npy` [6212]; `embed/gene_vectors.npy` [6212]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6212 or target_col == 6212). Every well: [[FGF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGF5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
