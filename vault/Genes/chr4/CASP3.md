---
symbol: "CASP3"
type: "gene"
col: 8923
ensembl_id: "ENSG00000164305"
name: "caspase 3"
location: "4q35.1"
module: 148
arm: "+"
pooled_cpm: 33.64
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# CASP3

*caspase 3* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.86× (z +16.7, q 0e+00, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.852× (z -10.3, q 7e-22, down in 15 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.731× (z -6.0, q 3e-07, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FZD7]] (+0.58, fdr 3e-05), [[CSRNP2]] (+0.58, fdr 2e-05), [[LNPEP]] (+0.52, fdr 3e-05); moves opposite to [[KCNK15-AS1]] (-0.52, fdr 6e-05), [[MAP2K2]] (-0.50, fdr 4e-05), [[SLC23A2]] (-0.49, fdr 2e-04).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8923.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.86×** | +16.7 | 0e+00 | 35/47 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +13.4 | 1e-38 | 41/47 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +12.5 | 1e-33 | 35/47 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +8.7 | 3e-16 | 31/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +8.5 | 2e-15 | 36/47 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +7.9 | 2e-13 | 32/48 (C32, LS 180, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +6.6 | 4e-09 | 31/48 (SW 900, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +6.3 | 3e-08 | 26/47 (HOP62, LoVo, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.28×** | +4.7 | 2e-04 | 19/48 (LoVo, SW1417, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +4.7 | 2e-04 | 17/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.27×** | +4.6 | 2e-04 | 20/48 (LoVo, SW 900, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.5 | 4e-04 | 21/48 (A498, J82, …) | top dose only | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.25×** | +4.3 | 8e-04 | 20/48 (SW1417, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 0.001 | 15/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.21×** | +3.7 | 0.009 | 17/48 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Decitabine (drug)]] 5 µM |  | 1.20× | +3.3 | 0.030 | 11/47 (C32, HepG2/C3A, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +3.2 | 0.034 | 13/48 (PANC-1, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8923.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.852× | -10.3 | 7e-22 | 15/49 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.637×** | -8.6 | 2e-15 | 30/45 (PANC-1, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.642×** | -8.1 | 7e-14 | 20/36 (KATO III, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.592×** | -7.9 | 3e-13 | 28/42 (A549, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.731×** | -6.0 | 3e-07 | 25/48 (RKO, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.771×** | -3.5 | 0.037 | 15/46 (KATO III, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.777×** | -3.4 | 0.049 | 9/48 (LS 180, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.784×** | -3.3 | 0.064 | 15/48 (RKO, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.845× | -3.1 | 0.13 | 17/48 (J82, SW 1271, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8923. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 19.6 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.54× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -11.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 33.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +12.1) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.101× (z -8.5) ⚠ toxic |
| [[LoVo (line)]] | wt | 25.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -8.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 39.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +13.9) | — |
| [[HEC-1-A (line)]] | alt | 32.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.320× (z -9.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 30.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.5) | [[Lonafarnib (drug)]] 5 µM 0.127× (z -10.1) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 33.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 36.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.119× (z -17.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 26.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 36.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -12.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 40.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -9.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 29.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +14.0) | — |
| [[CFPAC-1 (line)]] | alt | 26.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +15.3) | — |
| [[COLO 205 (line)]] | alt | 32.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +12.5) | — |
| [[HepG2_C3A (line)]] | wt | 53.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.270× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[HT-29 (line)]] | alt | 23.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +8.5) | — |
| [[KATO III (line)]] | alt | 39.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -19.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 33.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.21× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 30.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +17.0) | — |
| [[NCI-H2030 (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.164× (z -14.4) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.638× (z -10.9) ⚠ position not correctable |
| [[NCI-H460 (line)]] | wt | 37.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -13.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 40.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.7) | — |
| [[RKO (line)]] | wt | 68.9 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.335× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 29.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 33.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 28.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +8.6) | — |
| [[SW480 (line)]] | alt | 35.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.0) | — |
| [[A-172 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8923), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FZD7]] | +0.58 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[CSRNP2]] | +0.58 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[LNPEP]] | +0.52 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[CPT2]] | +0.51 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[RHNO1]] | +0.50 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[NHSL1]] | +0.50 | +0.36 / +0.42 | both halves | 1e-04 |  |
| [[STBD1]] | +0.49 | +0.27 / +0.41 | both halves | 3e-04 |  |
| [[SS18]] | +0.49 | +0.50 / +0.37 | both halves | 9e-05 |  |
| [[MTR]] | +0.49 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[SLFN5]] | +0.48 | +0.51 / +0.24 | both halves | 4e-04 |  |
| [[UBE3B]] | +0.47 | +0.44 / +0.32 | both halves | 2e-04 |  |
| [[GNG12-AS1]] | +0.47 | +0.48 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNK15-AS1]] | -0.52 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[MAP2K2]] | -0.50 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[SLC23A2]] | -0.49 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[PKIG]] | -0.49 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[CDA]] | -0.48 | -0.37 / -0.46 | both halves | 7e-05 | pathway: HALLMARK_COMPLEMENT |
| [[TOMM20]] | -0.47 | -0.38 / -0.32 | both halves | 2e-04 | same gene group; STRING 587 |
| [[ARMH1]] | -0.46 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[PLD3]] | -0.46 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[SBF2]] | -0.46 | -0.53 / -0.26 | both halves | 4e-04 |  |
| [[LMTK3]] | -0.46 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[SMIM7]] | -0.45 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[ZNF567-DT]] | -0.45 | -0.18 / -0.40 | ⚠ not reproduced | 0.001 |  |
| [[HEMK1]] | -0.45 | -0.37 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CASP3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.448). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (20.7, -9.7); signed map (20.9, -8.0). **Vector** length 82.6, 16.8% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +13.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +8.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +16.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.7 | +8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.4 | -0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.4 | +2.6 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.8 | -7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.8 | -8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.7 | -8.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -0.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.6 | -6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.7 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | +1.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | caspase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:184,627,696-184,650,062 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CPP32, CPP32B, Yama, apopain |
| Gene groups (HGNC) | Caspases; Small nucleolar RNA protein coding host genes |
| Hallmark sets | APOPTOSIS, UV_RESPONSE_UP, COMPLEMENT, IL2_STAT5_SIGNALING, INTERFERON_GAMMA_RESPONSE |
| Reactome | 32 pathways, smallest: CASP5-mediated substrate cleavage; CASP4-mediated substrate cleavage; Activation of caspases through apoptosome-mediated cleavage |
| Matched by | ensembl_id |

**Function**, from UniProt [P42574](https://www.uniprot.org/uniprotkb/P42574) (Caspase-3):

> Thiol protease that acts as a major effector caspase involved in the execution phase of apoptosis. Following cleavage and activation by initiator caspases (CASP8, CASP9 and/or CASP10), mediates execution of apoptosis by catalyzing cleavage of many proteins. At the onset of apoptosis, it proteolytically cleaves poly(ADP-ribose) polymerase PARP1 at a '216-Asp-|-Gly-217' bond. Cleaves and activates sterol regulatory element binding proteins (SREBPs) between the basic helix-loop-helix leucine …

**Summary**, from NCBI Gene [836](https://www.ncbi.nlm.nih.gov/gene/836):

> The protein encoded by this gene is a cysteine-aspartic acid protease that plays a central role in the execution-phase of cell apoptosis. The encoded protein cleaves and inactivates poly(ADP-ribose) polymerase while it cleaves and activates sterol regulatory element binding proteins as well as caspases 6, 7, and 9. This protein itself is processed by caspases 8, 9, and 10. It is the predominant caspase involved in the cleavage of amyloid-beta 4A precursor protein, which is associated with …

**Accessions** — [HGNC:1504](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1504) · Entrez [836](https://www.ncbi.nlm.nih.gov/gene/836) · UniProt [P42574](https://www.uniprot.org/uniprotkb/P42574) · Ensembl [ENSG00000164305](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164305)

## Data

Gene col 8923: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8923); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8923, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8923]; `tensor/DDL_lfc|DDL_z.npy` [8923]; `embed/gene_vectors.npy` [8923]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8923 or target_col == 8923). Every well: [[CASP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
