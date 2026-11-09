---
symbol: "SEC14L2"
type: "gene"
col: 1842
ensembl_id: "ENSG00000100003"
name: "SEC14 like lipid binding 2"
location: "22q12.2"
module: 97
arm: "+"
pooled_cpm: 31.43
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 21
n_dd_up_clean: 12
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# SEC14L2

*SEC14 like lipid binding 2* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Betamethasone dipropionate (drug)]] 5 µM: 1.33× (z +4.6, q 0.002, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.612× (z -11.8, q 1e-29, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC9]] (+0.67, fdr 7e-06), [[ITGA5]] (+0.63, fdr 1e-05), [[GLRX]] (+0.61, fdr 2e-05); moves opposite to [[PTPRK]] (-0.57, fdr 3e-05), [[ARHGAP42]] (-0.55, fdr 4e-05), [[PBRM1]] (-0.55, fdr 3e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LOX]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1842.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.33×** | +4.6 | 0.002 | 22/48 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.30×** | +4.5 | 0.002 | 19/48 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.29×** | +4.3 | 0.003 | 21/48 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.19× | +4.2 | 0.003 | 19/48 (Hs 766T, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.003 | 10/48 (CFPAC-1, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.26×** | +4.0 | 0.007 | 17/48 (NCI-H1573, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Econazole (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.010 | 14/48 (NCI-H1573, HS-578T, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.010 | 18/48 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.047 | 16/45 (H4, HS-578T, …) | all doses, flat | position effect removed |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.059 | 13/48 (HOP62, NCI-H460, …) | top dose only | plate-row cell shift |
| [[DTP3 (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.060 | 7/45 (MIA PaCa-2, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.060 | 14/48 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.060 | 12/48 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.089 | 17/48 (NCI-H1573, hTERT-HPNE, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1842.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.612×** | -11.8 | 1e-29 | 37/48 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.573×** | -9.5 | 6e-19 | 28/48 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.857× | -9.4 | 1e-18 | 12/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.592×** | -9.0 | 5e-17 | 30/48 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.597×** | -8.5 | 3e-15 | 32/45 (NCI-H2347, H4, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.643×** | -7.2 | 4e-11 | 27/48 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.732×** | -5.3 | 9e-06 | 21/41 (SNU-1, HS-578T, …) | two highest doses | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.756×** | -4.8 | 1e-04 | 22/46 (RPMI-7951, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **0.750×** | -4.7 | 2e-04 | 17/33 (HS-578T, SNU-423, …) | two highest doses | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.827×** | -4.6 | 3e-04 | 19/48 (RKO, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.765×** | -4.6 | 3e-04 | 22/48 (SW480, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.772×** | -4.4 | 5e-04 | 21/48 (HS-578T, A549, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.777×** | -4.3 | 7e-04 | 19/48 (H4, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.838× | -4.2 | 0.001 | 19/48 (NCI-H2347, CFPAC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.825×** | -4.2 | 0.001 | 16/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **0.790×** | -4.0 | 0.002 | 18/48 (CFPAC-1, HS-578T, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.793×** | -3.8 | 0.005 | 17/47 (NCI-H2347, A549, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **0.801×** | -3.7 | 0.007 | 18/48 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Brimonidine (drug)]] 0.5 µM |  | **0.819×** | -3.4 | 0.019 | 9/47 (SW 900, SW 1088, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.823×** | -3.3 | 0.023 | 15/48 (MIA PaCa-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1842. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 104 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -21.1) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.241× (z -20.3) |
| [[HS-578T (line)]] | alt | 113 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -14.4) |
| [[NCI-H2347 (line)]] | alt | 29.7 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.250× (z -10.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.458× (z -9.0) |
| [[HOP62 (line)]] | alt | 42.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 51.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.414× (z -8.6) |
| [[SNU-1 (line)]] | wt | 68.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -20.0) |
| [[A498 (line)]] | wt | 44.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.279× (z -11.2) |
| [[A549 (line)]] | wt | 33.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 61.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -8.9) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.345× (z -8.6) |
| [[H4 (line)]] | wt | 20.5 | 0 | 2 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0796× (z -11.3) |
| [[Hs 766T (line)]] | wt | 82.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 27.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -11.6) |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 1 | — | [[Bestatin (hydrochloride) (drug)]] 0.05 µM 0.0570× (z -8.8) |
| [[HCT15 (line)]] | alt | 26.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -8.9) |
| [[J82 (line)]] | alt | 26.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 21.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -16.2) |
| [[NCI-H1792 (line)]] | alt | 54.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -10.2) ⚠ cell-cycle shift, explains ~5% of this change |
| [[NCI-H460 (line)]] | wt | 25.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -9.2) |
| [[SNU-423 (line)]] | alt | 59.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[A-172 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1842), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC9]] | +0.67 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[ITGA5]] | +0.63 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[GLRX]] | +0.61 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[UGP2]] | +0.59 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[ANGPTL4]] | +0.58 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[PTPN1]] | +0.57 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[TLR2]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[PXYLP1]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[MAP2K1]] | +0.56 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[TANC2]] | +0.54 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[PACSIN2]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[COPS8]] | +0.53 | +0.57 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRK]] | -0.57 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[ARHGAP42]] | -0.55 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[PBRM1]] | -0.55 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[PER3]] | -0.53 | -0.58 / -0.40 | both halves | 4e-05 |  |
| [[AMIGO2]] | -0.52 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[STAG1]] | -0.52 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[EXPH5]] | -0.51 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ADGRA3]] | -0.49 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[EDIL3-DT]] | -0.48 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[SYTL2]] | -0.48 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[MID1]] | -0.48 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[PARD3B]] | -0.48 | -0.50 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LOX]] | B | LOX activity raises SEC14L2's level | lines that do not express LOX (31) vs lines expressing it (19) | 1.77× lower at baseline in the lines without LOX | 0.050 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[MT2A]] | B | MT2A activity raises SEC14L2's level | lines that do not express MT2A (9) vs lines expressing it (41) | 1.90× lower at baseline in the lines without MT2A | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000289942, TRAF1, MT1X |
| [[MT1X]] | B | MT1X activity raises SEC14L2's level | lines that do not express MT1X (5) vs lines expressing it (45) | 2.32× lower at baseline in the lines without MT1X | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RABGEF1P3, KIFC3, ENSG00000255031; its own permutation p |
| [[TREM1]] | B | TREM1 activity raises SEC14L2's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 1.54× lower at baseline in the lines without TREM1 | 0.067 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[SRPX]] | B | SRPX activity raises SEC14L2's level | lines that do not express SRPX (22) vs lines expressing it (28) | 1.27× lower at baseline in the lines without SRPX | 0.074 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[ARAP2]] | B | ARAP2 activity lowers SEC14L2's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 2.12× higher at baseline in the lines without ARAP2 | 0.085 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |
| [[MAP2K1]] | B | MAP2K1 activity raises SEC14L2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.511). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.6, 11.9); signed map (15.1, 35.7). **Vector** length 105, 24.9% of its response variance represented; |z| ≥ 3 in 1,112 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dexamethasone (drug)]] 5 µM |  | +4.2 | +4.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +4.1 | +4.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +4.1 | +3.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +2.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.4 | +4.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +3.3 | +4.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.6 | -8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | -4.1 | -4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.9 | -5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -11.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.6 | -4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -2.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.7 | -3.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.5 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | SEC14 like lipid binding 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:30,396,941-30,425,303 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAP, SPF, KIAA1186, KIAA1658, TAP1; previously C22orf6 |
| Gene groups (HGNC) | SEC14 family |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [O76054](https://www.uniprot.org/uniprotkb/O76054) (SEC14-like protein 2):

> Carrier protein. Binds to some hydrophobic molecules and promotes their transfer between the different cellular sites. Binds with high affinity to alpha-tocopherol. Also binds with a weaker affinity to other tocopherols and to tocotrienols. May have a transcriptional activatory activity via its association with alpha-tocopherol. Probably recognizes and binds some squalene structure, suggesting that it may regulate cholesterol biosynthesis by increasing the transfer of squalene to a metabolic …

**Summary**, from NCBI Gene [23541](https://www.ncbi.nlm.nih.gov/gene/23541):

> This gene encodes a cytosolic protein which belongs to a family of lipid-binding proteins including Sec14p, alpha-tocopherol transfer protein, and cellular retinol-binding protein. The encoded protein stimulates squalene monooxygenase which is a downstream enzyme in the cholesterol biosynthetic pathway. Alternatively spliced transcript variants encoding different isoforms have been identified for this gene. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:10699](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10699) · Entrez [23541](https://www.ncbi.nlm.nih.gov/gene/23541) · UniProt [O76054](https://www.uniprot.org/uniprotkb/O76054) · Ensembl [ENSG00000100003](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100003)

## Data

Gene col 1842: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1842); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1842, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1842]; `tensor/DDL_lfc|DDL_z.npy` [1842]; `embed/gene_vectors.npy` [1842]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1842 or target_col == 1842). Every well: [[SEC14L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC14L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
