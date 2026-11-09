---
symbol: "IGFN1"
type: "gene"
col: 8684
ensembl_id: "ENSG00000163395"
name: "immunoglobulin like and fibronectin type III domain containing 1"
location: "1q32.1"
module: 125
arm: "+"
pooled_cpm: 26.43
n_lines_expressing: 14
n_dd_up: 21
n_dd_down: 16
n_dd_up_clean: 14
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 15
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# IGFN1

*immunoglobulin like and fibronectin type III domain containing 1* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.25× (z +12.2, q 3e-31, up in 8 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.57× (z +5.4, q 9e-06, up in 2 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Triamcinolone (drug)]] 5 µM: 0.589× (z -6.3, q 2e-07, down in 12 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHISAL1]] (+0.74, fdr 7e-06), [[SLAMF7]] (+0.68, fdr 1e-05), [[LINC00536]] (+0.66, fdr 7e-06); moves opposite to [[FOXC2]] (-0.54, fdr 3e-05), [[ZMYND8]] (-0.53, fdr 4e-05), [[ITGA10]] (-0.52, fdr 3e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 15 go from it, the strongest it → [[MAFK]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8684.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.25×** | +12.2 | 3e-31 | 8/12 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.30×** | +11.8 | 1e-29 | 7/10 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.41×** | +5.8 | 1e-06 | 6/12 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +5.4 | 9e-06 | 2/12 (HOP62, AsPC-1) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +5.3 | 1e-05 | 6/12 (H4, J82, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +5.2 | 1e-05 | 8/12 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Retinoic acid (drug)]] 5 µM |  | **1.47×** | +4.6 | 3e-04 | 10/12 (RPMI-7951, HOP62, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.03×** | +4.2 | 0.002 | 2/12 (NCI-H460, HOP62) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.56×** | +3.7 | 0.012 | 7/12 (SK-MEL-2, NCI-H460, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.55×** | +3.7 | 0.012 | 3/12 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +3.6 | 0.015 | 2/12 (H4, HOP62) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +3.4 | 0.027 | 10/12 (A-172, A498, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +3.1 | 0.075 | 2/12 (HOP62, A-172) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.68×** | +3.1 | 0.075 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.078 | 5/12 (SK-MEL-2, RPMI-7951, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.0 | 0.078 | 5/12 (J82, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bexarotene (drug)]] 0.05 µM |  | **1.44×** | +3.0 | 0.078 | 4/12 (A-172, RPMI-7951, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.62×** | +2.9 | 0.099 | 2/12 (NCI-H460, HOP62) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.44×** | +2.9 | 0.099 | 6/12 (AsPC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8684.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Triamcinolone (drug)]] 5 µM |  | **0.589×** | -6.3 | 2e-07 | 12/12 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.509×** | -5.7 | 4e-06 | 11/12 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.434×** | -5.5 | 8e-06 | 10/12 (NCI-H460, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.536×** | -5.2 | 3e-05 | 10/12 (J82, A498, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.542×** | -5.1 | 3e-05 | 11/12 (NCI-H1792, SNU-423, …) | all doses, flat | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.552×** | -5.0 | 6e-05 | 8/12 (A498, J82, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.576×** | -4.6 | 3e-04 | 10/12 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.578×** | -4.5 | 5e-04 | 11/12 (SNU-423, NCI-H460, …) | all doses, flat | position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.587×** | -4.5 | 5e-04 | 11/12 (RPMI-7951, A549, …) | top dose only | position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.598×** | -4.1 | 0.002 | 11/12 (A549, SNU-423, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.615×** | -4.1 | 0.002 | 11/12 (SNU-423, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Quinestrol (drug)]] 5 µM |  | **0.715×** | -4.0 | 0.004 | 4/12 (A549, NCI-H460, …) | top dose only | position effect removed |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.651×** | -3.6 | 0.015 | 10/12 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.657×** | -3.5 | 0.018 | 7/12 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.660×** | -3.4 | 0.027 | 10/12 (A549, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.613×** | -3.2 | 0.044 | 2/12 (SK-MEL-2, AsPC-1) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8684. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 103 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0912× (z -9.3) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0992× (z -8.6) |
| [[A498 (line)]] | wt | 145 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 6.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 353 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 187 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.49 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.97 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.05 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.49 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.27 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.12 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8684), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHISAL1]] | +0.74 | +0.67 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[SLAMF7]] | +0.68 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[LINC00536]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[LINC02154]] | +0.65 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[ANKRD30B]] | +0.62 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[LINC01828]] | +0.62 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ROR1-AS1]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ENTHD1]] | +0.57 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[NGF]] | +0.57 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[PSG9]] | +0.57 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[TRAF1]] | +0.57 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[CREB5]] | +0.56 | +0.42 / +0.55 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXC2]] | -0.54 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[ZMYND8]] | -0.53 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[ITGA10]] | -0.52 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[COPS8]] | -0.51 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[CCND3]] | -0.49 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[PIK3R1]] | -0.48 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[RIPOR2]] | -0.47 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[TPCN1]] | -0.46 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ARMC8]] | -0.46 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[SAA1]] | -0.46 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ZHX3]] | -0.46 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[TNS2]] | -0.45 | -0.42 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers IGFN1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |
| [[LINC02154]] | C | LINC02154 activity raises IGFN1's level | lines that do not express LINC02154 (37) vs lines expressing it (13) | 3.86× lower at baseline in the lines without LINC02154 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FCRLA, ENSG00000234426, ENSG00000289530; co-absent with the target |
| [[SHISAL1]] | C | SHISAL1 activity raises IGFN1's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 2.91× lower at baseline in the lines without SHISAL1 | 0.090 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 6, C 9. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAFK]] | B | IGFN1 activity raises MAFK's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 1.88× lower at baseline in the lines without IGFN1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9 |
| [[TMOD1]] | B | IGFN1 activity raises TMOD1's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 2.96× lower at baseline in the lines without IGFN1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9 |
| [[CRYM]] | B | IGFN1 activity raises CRYM's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 2.29× lower at baseline in the lines without IGFN1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9 |
| [[RPLP0P2]] | B | IGFN1 activity raises RPLP0P2's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 2.04× lower at baseline in the lines without IGFN1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9 |
| [[MEGF6]] | B | IGFN1 activity raises MEGF6's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 1.72× lower at baseline in the lines without IGFN1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9 |
| [[LINC01828]] | B | IGFN1 activity raises LINC01828's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 2.82× lower at baseline in the lines without IGFN1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9 |
| [[ACKR3]] | C | IGFN1 activity raises ACKR3's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 3.56× lower at baseline in the lines without IGFN1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9; co-absent with the target |
| [[LINC02220]] | C | IGFN1 activity raises LINC02220's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 1.97× lower at baseline in the lines without IGFN1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9; co-absent with the target |
| [[SIRLNT]] | C | IGFN1 activity raises SIRLNT's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 2.83× lower at baseline in the lines without IGFN1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9; co-absent with the target |
| [[MAF]] | C | IGFN1 activity raises MAF's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 5.46× lower at baseline in the lines without IGFN1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9; co-absent with the target |
| [[LINC01411]] | C | IGFN1 activity raises LINC01411's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 5.86× lower at baseline in the lines without IGFN1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9; co-absent with the target |
| [[SHISAL1]] | C | IGFN1 activity raises SHISAL1's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 2.96× lower at baseline in the lines without IGFN1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9; co-absent with the target |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.8, 22.0); signed map (38.6, 23.2). **Vector** length 59.9, 23.5% of its response variance represented; |z| ≥ 3 in 442 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +5.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +4.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.5 | +2.2 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -5.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.6 | -4.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.5 | -2.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.5 | -5.7 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.4 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | immunoglobulin like and fibronectin type III domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:201,190,824-201,228,952 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434B1231, EEF1A2BP1 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing |
| Matched by | ensembl_id |

UniProt [Q86VF2](https://www.uniprot.org/uniprotkb/Q86VF2) carries no function annotation.

**Summary**, from NCBI Gene [91156](https://www.ncbi.nlm.nih.gov/gene/91156):

> Predicted to act upstream of or within myoblast differentiation and myoblast fusion. Predicted to be located in Z disc and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24607](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24607) · Entrez [91156](https://www.ncbi.nlm.nih.gov/gene/91156) · UniProt [Q86VF2](https://www.uniprot.org/uniprotkb/Q86VF2) · Ensembl [ENSG00000163395](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163395)

## Data

Gene col 8684: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8684); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8684, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8684]; `tensor/DDL_lfc|DDL_z.npy` [8684]; `embed/gene_vectors.npy` [8684]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8684 or target_col == 8684). Every well: [[IGFN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGFN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
