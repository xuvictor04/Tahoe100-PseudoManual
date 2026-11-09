---
symbol: "NUDT16"
type: "gene"
col: 12621
ensembl_id: "ENSG00000198585"
name: "nudix hydrolase 16"
location: "3q22.1"
module: 94
arm: "+"
pooled_cpm: 14.45
n_lines_expressing: 50
n_dd_up: 41
n_dd_down: 12
n_dd_up_clean: 30
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# NUDT16

*nudix hydrolase 16* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (11 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 2.57× (z +21.1, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.529× (z -10.3, q 3e-22, down in 32 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.565× (z -9.3, q 6e-18, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP15]] (+0.65, fdr 9e-06), [[ZNF44]] (+0.62, fdr 1e-05), [[TRPM4]] (+0.62, fdr 2e-04); moves opposite to [[LIMD1]] (-0.46, fdr 3e-05), [[VOPP1]] (-0.45, fdr 7e-05), [[C2CD3]] (-0.45, fdr 1e-04).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NGFR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12621.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **2.57×** | +21.1 | 0e+00 | 43/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **2.15×** | +17.1 | 0e+00 | 35/47 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.88×** | +17.1 | 0e+00 | 44/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **2.64×** | +15.7 | 0e+00 | 42/47 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.60×** | +15.4 | 0e+00 | 44/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +15.0 | 0e+00 | 35/46 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **2.50×** | +14.8 | 0e+00 | 45/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.44×** | +14.4 | 6e-45 | 43/47 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.06×** | +11.2 | 4e-27 | 35/46 (SW1417, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.85×** | +9.9 | 2e-21 | 37/47 (SW1417, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +9.0 | 2e-17 | 27/41 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.67×** | +8.3 | 7e-15 | 29/46 (HS-578T, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +7.4 | 5e-12 | 31/46 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM | ⚠ position correction uncertain | **1.58×** | +7.3 | 1e-11 | 22/47 (HEC-1-A, A-427, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +6.6 | 1e-09 | 17/36 (KATO III, LoVo, …) | two highest doses | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +6.3 | 8e-09 | 27/47 (LOX-IMVI, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.5 | 1e-06 | 20/47 (HEC-1-A, SW1417, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.86×** | +5.2 | 4e-06 | 12/48 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.32×** | +4.4 | 3e-04 | 16/47 (H4, NCI-H1792, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12621.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.529×** | -10.3 | 3e-22 | 32/46 (HCT15, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.565×** | -9.3 | 6e-18 | 32/47 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.491×** | -6.0 | 3e-07 | 26/48 (PANC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.708×** | -5.6 | 3e-06 | 22/47 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.526×** | -5.4 | 6e-06 | 22/43 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.721×** | -5.3 | 1e-05 | 24/47 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.775×** | -4.1 | 0.003 | 14/47 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.779×** | -4.1 | 0.003 | 14/47 (A-172, A498, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -3.9 | 0.007 | 4/48 (SHP-77, HCT15, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.781×** | -3.8 | 0.008 | 17/47 (SW480, SW1417, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.849× | -3.7 | 0.010 | 19/48 (NCI-H1573, SNU-1, …) | rises with dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.799×** | -3.7 | 0.011 | 6/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.820×** | -3.2 | 0.056 | 8/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.821×** | -3.1 | 0.092 | 9/48 (SHP-77, SW 1088, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12621. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 32.8 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +19.2) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +12.6) | — |
| [[PANC-1 (line)]] | alt | 15.9 | 6 | 0 | [[Selinexor (drug)]] 5 µM 3.65× (z +15.2) | — |
| [[SW480 (line)]] | alt | 21.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +12.2) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +11.4) | [[Lonafarnib (drug)]] 5 µM 0.144× (z -9.1) ⚠ toxic |
| [[A-172 (line)]] | wt | 14.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +13.3) ⚠ position correction uncertain · without an alert: [[Selinexor (drug)]] 5 µM 3.37× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 19.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +10.7) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 5.86× (z +10.6) | — |
| [[HEC-1-A (line)]] | alt | 24.1 | 3 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.48× (z +10.7) | — |
| [[A-427 (line)]] | wt | 21.4 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.23× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0671× (z -12.5) |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0878× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0912× (z -9.3) |
| [[KATO III (line)]] | alt | 17.0 | 2 | 0 | [[Selinexor (drug)]] 5 µM 3.80× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 10.5 | 2 | 0 | [[Selinexor (drug)]] 0.05 µM 6.03× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 11.3 | 2 | 0 | [[Selinexor (drug)]] 0.05 µM 3.54× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 19.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +9.9) ⚠ position correction uncertain | — |
| [[C-33 A (line)]] | alt | 9.72 | 1 | 0 | [[Selinexor (drug)]] 5 µM 6.11× (z +9.8) | — |
| [[C32 (line)]] | wt | 7.62 | 1 | 0 | [[Selinexor (drug)]] 5 µM 4.80× (z +8.9) | — |
| [[H4 (line)]] | wt | 11.0 | 1 (1 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 12.6× (z +8.6) ⚠ position correction uncertain | — |
| [[LoVo (line)]] | wt | 11.0 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.86× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 20.1 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.61× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.274× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 15.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +12.0) ⚠ position correction uncertain | — |
| [[Panc 03.27 (line)]] | alt | 22.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +13.2) ⚠ position correction uncertain | — |
| [[RKO (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -8.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 20.6 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.01× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0686× (z -9.5) ⚠ cell-cycle shift, explains ~9% of this change |
| [[A498 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12621), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP15]] | +0.65 | +0.57 / +0.73 | both halves | 9e-06 |  |
| [[ZNF44]] | +0.62 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[TRPM4]] | +0.62 | +0.32 / +0.70 | both halves | 2e-04 |  |
| [[SLC44A2]] | +0.60 | +0.36 / +0.68 | both halves | 1e-04 |  |
| [[SLC43A2]] | +0.59 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[ZNF433]] | +0.58 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[TATDN3]] | +0.57 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[ZNF442]] | +0.57 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[PCLO]] | +0.57 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[TRAPPC11]] | +0.56 | +0.39 / +0.66 | both halves | 5e-05 |  |
| [[SLC2A4RG]] | +0.55 | +0.38 / +0.68 | both halves | 6e-05 |  |
| [[CLN5]] | +0.55 | +0.62 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIMD1]] | -0.46 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[VOPP1]] | -0.45 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[C2CD3]] | -0.45 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[ASPH]] | -0.44 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[UBASH3B]] | -0.44 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[MANCR]] | -0.44 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[IQCJ-SCHIP1]] | -0.43 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[LINC01151]] | -0.43 | -0.29 / -0.53 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NGFR]] | B | NGFR activity raises NUDT16's level | lines that do not express NGFR (19) vs lines expressing it (31) | 1.24× lower at baseline in the lines without NGFR | 0.061 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11 |
| [[NR3C1]] | B | NR3C1 activity raises NUDT16's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 7.0% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[SLC44A2]] | C | SLC44A2 activity raises NUDT16's level | lines that do not express SLC44A2 (4) vs lines expressing it (46) | 1.70× lower at baseline in the lines without SLC44A2 | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC45, CLSPN, AURKB; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.699). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.0, 24.6); signed map (15.1, -16.3). **Vector** length 89.8, 20.5% of its response variance represented; |z| ≥ 3 in 1,316 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +11.9 | +21.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +9.2 | +15.7 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +6.6 | +14.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.2 | +8.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +11.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.2 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM | ⚠ position correction uncertain | +4.2 | +7.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.8 | +3.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.7 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -4.9 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -0.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | -10.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -5.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | nudix hydrolase 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1 — chr3:131,381,671-131,388,830 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31265 |
| Gene groups (HGNC) | Nudix hydrolase family |
| Reactome | 4 pathways, smallest: Phosphate bond hydrolysis by NUDT proteins; Purine catabolism; Nucleotide catabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DE0](https://www.uniprot.org/uniprotkb/Q96DE0) (U8 snoRNA-decapping enzyme):

> RNA-binding and decapping enzyme that catalyzes the cleavage of the cap structure of snoRNAs and mRNAs in a metal-dependent manner. Part of the U8 snoRNP complex that is required for the accumulation of mature 5.8S and 28S rRNA. Has diphosphatase activity and removes m7G and/or m227G caps from U8 snoRNA and leaves a 5'monophosphate on the RNA. Also catalyzes the cleavage of the cap structure on mRNAs. Does not hydrolyze cap analog structures like 7-methylguanosine nucleoside triphosphate …

**Summary**, from NCBI Gene [131870](https://www.ncbi.nlm.nih.gov/gene/131870):

> Enables several functions, including RNA binding activity; metal ion binding activity; and pyrophosphatase activity. Involved in RNA metabolic process and positive regulation of cell cycle process. Located in cytoplasm; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26442](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26442) · Entrez [131870](https://www.ncbi.nlm.nih.gov/gene/131870) · UniProt [Q96DE0](https://www.uniprot.org/uniprotkb/Q96DE0) · Ensembl [ENSG00000198585](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198585)

## Data

Gene col 12621: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12621); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12621, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12621]; `tensor/DDL_lfc|DDL_z.npy` [12621]; `embed/gene_vectors.npy` [12621]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12621 or target_col == 12621). Every well: [[NUDT16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
