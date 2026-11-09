---
symbol: "UBE2L3"
type: "gene"
col: 11710
ensembl_id: "ENSG00000185651"
name: "ubiquitin conjugating enzyme E2 L3"
location: "22q11.21"
module: 36
arm: "+"
pooled_cpm: 65.06
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# UBE2L3

*ubiquitin conjugating enzyme E2 L3* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.47× (z +19.4, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.658× (z -10.4, q 1e-22, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNRPD3]] (+0.68, fdr 1e-05), [[PSMB2]] (+0.67, fdr 7e-06), [[TRRAP]] (+0.64, fdr 7e-06); moves opposite to [[ING1]] (-0.55, fdr 1e-05), [[GCAT]] (-0.54, fdr 2e-05), [[PIM3]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11710.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.47×** | +19.4 | 0e+00 | 48/49 (SW480, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.03×** | +18.1 | 0e+00 | 44/48 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.96×** | +16.7 | 0e+00 | 47/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.81×** | +14.7 | 0e+00 | 46/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +14.5 | 1e-45 | 43/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +13.8 | 4e-41 | 46/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.76×** | +13.2 | 8e-38 | 44/48 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.51×** | +10.2 | 2e-22 | 40/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +9.9 | 4e-21 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +8.6 | 7e-16 | 37/48 (LoVo, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +7.4 | 1e-11 | 28/43 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.47×** | +6.8 | 4e-10 | 36/49 (C32, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.66×** | +6.5 | 3e-09 | 24/36 (NCI-H1573, PANC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +5.1 | 1e-05 | 0/49 | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~13% of this change | **1.23×** | +4.9 | 4e-05 | 23/47 (LoVo, HepG2/C3A, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.5 µM |  | 1.18× | +2.9 | 0.086 | 5/48 (PANC-1, NCI-H23, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11710.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.658×** | -10.4 | 1e-22 | 37/48 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.680×** | -9.6 | 2e-19 | 37/48 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.745×** | -7.3 | 4e-11 | 33/48 (SW1417, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.767×** | -6.6 | 5e-09 | 32/48 (SW1417, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.872× | -4.8 | 1e-04 | 19/49 (Panc 03.27, RKO, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.876× | -4.7 | 3e-04 | 13/48 (SW1417, SNU-423, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.722×** | -4.2 | 0.002 | 20/49 (HEC-1-A, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.879× | -3.2 | 0.091 | 14/49 (NCI-H2347, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11710. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 46.8 | 10 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +15.5) | — |
| [[SW480 (line)]] | alt | 68.7 | 10 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.52× (z +15.2) | — |
| [[KATO III (line)]] | alt | 79.3 | 7 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.471× (z -9.6) |
| [[LoVo (line)]] | wt | 63.0 | 9 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.87× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +13.6) | — |
| [[NCI-H1573 (line)]] | alt | 72.0 | 8 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.3× (z +14.5) | — |
| [[SW1417 (line)]] | alt | 102 | 4 (1 ⚠) | 4 | [[Digitoxin (drug)]] 5 µM 2.04× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 3.82× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.405× (z -13.1) |
| [[HOP62 (line)]] | alt | 78.4 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.47× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.30× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 70.3 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.08× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +11.7) | — |
| [[NCI-H460 (line)]] | wt | 61.9 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 55.5 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 127 | 3 | 2 | [[TAK-901 (drug)]] 5 µM 5.97× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.485× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 76.7 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 4.51× (z +11.4) | — |
| [[AsPC-1 (line)]] | alt | 54.3 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.17× (z +11.3) | — |
| [[LOX-IMVI (line)]] | wt | 46.3 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.68× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 87.7 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 6.42× (z +12.0) | — |
| [[NCI-H23 (line)]] | alt | 67.0 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.38× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.34× (z +8.7) | — |
| [[RKO (line)]] | wt | 73.7 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 7.07× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[HS-578T (line)]] | alt | 85.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.71× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 45.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.74× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 87.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.42× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.311× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[A498 (line)]] | wt | 58.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.29× (z +9.8) | — |
| [[A549 (line)]] | wt | 49.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.32× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | — |
| [[AN3 CA (line)]] | alt | 84.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 59.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.68× (z +9.1) | — |
| [[C32 (line)]] | wt | 69.7 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.41× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 58.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.70× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 67.8 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.21× (z +8.5) | — |
| [[J82 (line)]] | alt | 52.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 47.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.37× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 53.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 33.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SNU-423 (line)]] | alt | 69.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.22× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 53.1 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0703× (z -9.0) |
| [[SW48 (line)]] | wt | 82.6 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.55× (z +12.0) | — |
| [[A-172 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 76.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 61.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11710), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPD3]] | +0.68 | +0.76 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[PSMB2]] | +0.67 | +0.72 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[TRRAP]] | +0.64 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[MRPS15]] | +0.64 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[PEX26]] | +0.63 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[PSMB3]] | +0.63 | +0.77 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[CDC123]] | +0.63 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[KPNA6]] | +0.61 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[STX16-NPEPL1]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[SMIM7]] | +0.58 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[USP5]] | +0.58 | +0.58 / +0.61 | both halves | 7e-06 | pathway: Protein ubiquitination |
| [[PSMD1]] | +0.58 | +0.54 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ING1]] | -0.55 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[GCAT]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[PIM3]] | -0.54 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[BTG1]] | -0.54 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[LACTB]] | -0.52 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[N4BP3]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[RELA]] | -0.50 | -0.37 / -0.37 | both halves | 8e-05 | pathway: Death Receptor Signaling |
| [[TRIM36]] | -0.49 | -0.44 / -0.57 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[TCAF1]] | -0.49 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ACTR1B]] | -0.49 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[NBPF19]] | -0.48 | -0.47 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises UBE2L3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.493). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-15.9, -10.7); signed map (-26.4, -24.9). **Vector** length 85.2, 20.9% of its response variance represented; |z| ≥ 3 in 1,185 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.9 | +13.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.8 | +16.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.4 | +13.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +19.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.8 | +18.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.4 | +6.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.2 | +3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +0.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.8 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -0.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.7 | -2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -1.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | +0.4 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 L3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:21,549,447-21,624,034 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UBCH7 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 18 pathways, smallest: RIPK1-mediated regulated necrosis; Regulation of necroptotic cell death; Synthesis of active ubiquitin: roles of E1 and E2 enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [P68036](https://www.uniprot.org/uniprotkb/P68036) (Ubiquitin-conjugating enzyme E2 L3):

> Ubiquitin-conjugating enzyme E2 that specifically acts with HECT-type and RBR family E3 ubiquitin-protein ligases. Does not function with most RING-containing E3 ubiquitin-protein ligases because it lacks intrinsic E3-independent reactivity with lysine; in contrast, it has activity with the RBR family E3 enzymes, such as PRKN, RNF31 and ARIH1, that function like RING-HECT hybrids. Accepts ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins. Mediates …

**Summary**, from NCBI Gene [7332](https://www.ncbi.nlm.nih.gov/gene/7332):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes (E1s), ubiquitin-conjugating enzymes (E2s) and ubiquitin-protein ligases (E3s). This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. This enzyme is demonstrated to participate in the ubiquitination of p53, c-Fos, and the NF-kB precursor p105 in …

**Accessions** — [HGNC:12488](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12488) · Entrez [7332](https://www.ncbi.nlm.nih.gov/gene/7332) · UniProt [P68036](https://www.uniprot.org/uniprotkb/P68036) · Ensembl [ENSG00000185651](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185651)

## Data

Gene col 11710: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11710); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11710, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11710]; `tensor/DDL_lfc|DDL_z.npy` [11710]; `embed/gene_vectors.npy` [11710]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11710 or target_col == 11710). Every well: [[UBE2L3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2L3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
