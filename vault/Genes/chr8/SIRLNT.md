---
symbol: "SIRLNT"
type: "gene"
col: 14843
ensembl_id: "ENSG00000253802"
name: "SIRT1 regulating lncRNA tumor promoter"
location: "8p11.21"
module: 19
arm: "+"
pooled_cpm: 5.62
n_lines_expressing: 18
n_dd_up: 20
n_dd_down: 15
n_dd_up_clean: 11
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 25
direction_downstream: 71
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SIRLNT

*SIRT1 regulating lncRNA tumor promoter* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 8.29× (z +15.9, q 0e+00, up in 4 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.72× (z +4.1, q 0.005, up in 8 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.463× (z -5.8, q 3e-06, down in 8 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C5orf46]] (+0.78, fdr 7e-06), [[LINC01411]] (+0.74, fdr 7e-06), [[LYPLAL1-DT]] (+0.69, fdr 1e-05); moves opposite to [[FOXC2]] (-0.64, fdr 1e-05), [[CCND3]] (-0.58, fdr 1e-05), [[ITGA10]] (-0.57, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[FGD4]] → it (grade B ⚠); 71 go from it, the strongest it → [[B3GNT9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14843.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **8.29×** | +15.9 | 0e+00 | 4/9 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.69×** | +14.7 | 0e+00 | 3/5 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.10×** | +9.7 | 4e-20 | 3/7 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +4.8 | 2e-04 | 3/8 (A498, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.72×** | +4.1 | 0.005 | 8/14 (H4, A-172, …) | two highest doses | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **1.67×** | +3.7 | 0.017 | 1/14 (A549) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +3.7 | 0.017 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.62×** | +3.6 | 0.017 | 1/13 (HOP62) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.6 | 0.017 | 1/12 (A-172) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.52×** | +3.6 | 0.017 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.58×** | +3.4 | 0.032 | 2/14 (A549, RPMI-7951) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.037 | 4/15 (NCI-H460, H4, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.59×** | +3.3 | 0.037 | 10/14 (H4, HOP62, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.55×** | +3.3 | 0.040 | 2/14 (A549, A-172) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +3.3 | 0.040 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.063 | 4/13 (hTERT-HPNE, SNU-423, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.55×** | +3.1 | 0.075 | 5/15 (NCI-H460, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +3.0 | 0.079 | 1/14 (A-172) | top dose only |  |
| [[Capmatinib (drug)]] 5 µM |  | **2.15×** | +3.0 | 0.082 | 2/10 (H4, A-172) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.089 | 3/15 (HS-578T, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14843.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.463×** | -5.8 | 3e-06 | 8/15 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.466×** | -5.7 | 3e-06 | 13/15 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.503×** | -5.2 | 5e-05 | 11/15 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.554×** | -4.4 | 0.001 | 10/14 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.577×** | -4.0 | 0.007 | 12/15 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.589×** | -4.0 | 0.007 | 11/15 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.594×** | -3.9 | 0.008 | 10/15 (HOP62, H4, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.620×** | -3.6 | 0.024 | 8/15 (HS-578T, H4, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.622×** | -3.6 | 0.024 | 13/15 (H4, HS-578T, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.636×** | -3.4 | 0.040 | 11/15 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.627×** | -3.4 | 0.041 | 7/14 (H4, HS-578T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.641×** | -3.3 | 0.041 | 6/13 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.658×** | -3.1 | 0.075 | 7/15 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **0.663×** | -3.1 | 0.082 | 11/15 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.640×** | -3.1 | 0.082 | 9/13 (HOP62, HS-578T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14843. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 16.9 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0506× (z -16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0313× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 49.0 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0623× (z -22.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -12.2) |
| [[HS-578T (line)]] | alt | 48.8 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0513× (z -15.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.175× (z -8.9) |
| [[H4 (line)]] | wt | 39.8 | 0 | 4 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0142× (z -15.3) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SNU-423 (line)]] | alt | 7.84 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0864× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 7.66 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.876 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.640 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.794 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.689 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.834 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.575 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.962 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.594 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.664 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.555 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14843), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C5orf46]] | +0.78 | +0.76 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[LINC01411]] | +0.74 | +0.72 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[LYPLAL1-DT]] | +0.69 | +0.56 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[VSTM4]] | +0.66 | +0.70 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[GJA1]] | +0.64 | +0.66 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[SHISAL1]] | +0.62 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[BMPER]] | +0.62 | +0.66 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[ARHGEF6]] | +0.61 | +0.67 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[MAF]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[NCKAP5]] | +0.59 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[TMOD1]] | +0.58 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ADAMTS16]] | +0.58 | +0.54 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXC2]] | -0.64 | -0.54 / -0.68 | both halves | 1e-05 | **novel candidate** |
| [[CCND3]] | -0.58 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[ITGA10]] | -0.57 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[ADAMTS9]] | -0.54 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[MT1E]] | -0.53 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[ZMYND8]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[RTN4RL1]] | -0.52 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[HS3ST3B1]] | -0.51 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[PTX3]] | -0.51 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[COPS8]] | -0.50 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[KLF9]] | -0.50 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[MT2A]] | -0.50 | -0.42 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 1, C 24. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGD4]] | B | FGD4 activity lowers SIRLNT's level | lines that do not express FGD4 (10) vs lines expressing it (40) | 1.88× higher at baseline in the lines without FGD4 | 0.015 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| [[SRGN]] | C | SRGN activity raises SIRLNT's level | lines that do not express SRGN (30) vs lines expressing it (20) | 3.67× lower at baseline in the lines without SRGN | 0.006 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3; co-absent with the target |
| [[SPOCK1]] | C | SPOCK1 activity raises SIRLNT's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 3.33× lower at baseline in the lines without SPOCK1 | 0.009 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |
| [[NID2]] | C | NID2 activity raises SIRLNT's level | lines that do not express NID2 (32) vs lines expressing it (18) | 2.98× lower at baseline in the lines without NID2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1; co-absent with the target |
| [[COL15A1]] | C | COL15A1 activity raises SIRLNT's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 2.97× lower at baseline in the lines without COL15A1 | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |
| [[ABI3BP]] | C | ABI3BP activity raises SIRLNT's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 3.11× lower at baseline in the lines without ABI3BP | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; co-absent with the target |
| [[TENM2]] | C | TENM2 activity raises SIRLNT's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 2.96× lower at baseline in the lines without TENM2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1; co-absent with the target |
| [[FOXC2]] | C | FOXC2 activity raises SIRLNT's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 2.95× lower at baseline in the lines without FOXC2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises SIRLNT's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 3.14× lower at baseline in the lines without C5orf46 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[ADAMTS6]] | C | ADAMTS6 activity raises SIRLNT's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 2.39× lower at baseline in the lines without ADAMTS6 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2; co-absent with the target |
| [[IGFN1]] | C | IGFN1 activity raises SIRLNT's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 2.83× lower at baseline in the lines without IGFN1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9; co-absent with the target |
| [[PDE3A]] | C | PDE3A activity raises SIRLNT's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 2.68× lower at baseline in the lines without PDE3A | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |

### Downstream of this gene

*71 arrows, 71 of them with an alert ⚠; grade A 0, B 35, C 36. Shown: the 12 strongest; 59 more arrows (59 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B3GNT9]] | B | SIRLNT activity raises B3GNT9's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 1.72× lower at baseline in the lines without SIRLNT | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[LARP6]] | B | SIRLNT activity raises LARP6's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 2.66× lower at baseline in the lines without SIRLNT | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[IGFBP6]] | B | SIRLNT activity raises IGFBP6's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 3.33× lower at baseline in the lines without SIRLNT | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| cells under [[Procainamide (hydrochloride) (drug)]] 5 µM | B | SIRLNT activity raises the cells' numbers under Procainamide (hydrochloride) 5 µM (protects the cells) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 0.79× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| cells under [[Ivermectin (drug)]] 0.5 µM | B | SIRLNT activity lowers the cells' numbers under Ivermectin 0.5 µM (makes them more sensitive) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 1.24× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[FGD4]] | B | SIRLNT activity lowers FGD4's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 2.50× higher at baseline in the lines without SIRLNT | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[EML1]] | B | SIRLNT activity raises EML1's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 3.47× lower at baseline in the lines without SIRLNT | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| cells under [[Lactate (calcium) (drug)]] 0.05 µM | B | SIRLNT activity raises the cells' numbers under Lactate (calcium) 0.05 µM (protects the cells) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 0.78× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[TMOD1]] | B | SIRLNT activity raises TMOD1's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 2.79× lower at baseline in the lines without SIRLNT | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[LINC00536]] | B | SIRLNT activity raises LINC00536's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 2.79× lower at baseline in the lines without SIRLNT | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| cells under [[Dihydroartemisinin (drug)]] 5 µM | B | SIRLNT activity lowers the cells' numbers under Dihydroartemisinin 5 µM (makes them more sensitive) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 1.43× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| cells under [[Carbamazepine (drug)]] 0.5 µM | B | SIRLNT activity lowers the cells' numbers under Carbamazepine 0.5 µM (makes them more sensitive) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 1.26× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.460). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.0, 17.3); signed map (23.6, 49.3). **Vector** length 62.2, 21.4% of its response variance represented; |z| ≥ 3 in 496 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +15.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.0 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.3 | -5.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.8 | -3.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.7 | -3.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.7 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | SIRT1 regulating lncRNA tumor promoter |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8p11.21 — chr8:40,298,697-40,353,133 (-) |
| Ensembl biotype | lncRNA |
| Also known as | lncRNA-PRLB |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53902](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53902) · Entrez [112543493](https://www.ncbi.nlm.nih.gov/gene/112543493) · Ensembl [ENSG00000253802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253802)

## Data

Gene col 14843: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14843); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14843, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14843]; `tensor/DDL_lfc|DDL_z.npy` [14843]; `embed/gene_vectors.npy` [14843]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14843 or target_col == 14843). Every well: [[SIRLNT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIRLNT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
