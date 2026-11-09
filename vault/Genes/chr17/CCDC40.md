---
symbol: "CCDC40"
type: "gene"
col: 6534
ensembl_id: "ENSG00000141519"
name: "coiled-coil domain 40 molecular ruler complex subunit"
location: "17q25.3"
module: 205
arm: "+"
pooled_cpm: 13.82
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 31
n_dd_up_clean: 10
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/205"]
generated_by: "tahoemap"
---

# CCDC40

*coiled-coil domain 40 molecular ruler complex subunit* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +12.7, q 2e-34, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (10 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 5 µM: 0.631× (z -7.2, q 5e-10, down in 30 of 47 measured lines) ⚠ position correction uncertain. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.663× (z -6.4, q 5e-08, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF9]] (+0.72, fdr 7e-06), [[ZNF487]] (+0.62, fdr 1e-05), [[CFAP210]] (+0.61, fdr 7e-06); moves opposite to [[ZSCAN26]] (-0.51, fdr 3e-05), [[PRDM4]] (-0.50, fdr 3e-05), [[PFDN1]] (-0.50, fdr 3e-05).
> It is in [[Module 205]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IFNLR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6534.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +12.7 | 2e-34 | 33/46 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +7.2 | 2e-10 | 20/27 (SK-MEL-2, HOP62, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.89×** | +7.0 | 5e-10 | 29/46 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +6.8 | 1e-09 | 13/21 (NCI-H460, KATO III, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.61×** | +5.2 | 2e-05 | 26/47 (SW480, A498, …) | all doses, flat | position effect removed |
| [[Darinaparsin (drug)]] 5 µM |  | **1.35×** | +4.7 | 3e-04 | 18/47 (NCI-H2030, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.49×** | +4.4 | 9e-04 | 15/38 (LoVo, NCI-H460, …) | all doses, flat | composition shift |
| [[Levobupivacaine (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.2 | 0.002 | 17/46 (A549, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.43×** | +3.9 | 0.006 | 16/46 (A-172, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.42×** | +3.9 | 0.007 | 16/46 (CFPAC-1, COLO 205, …) | rises with dose | position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.018 | 6/47 (RPMI-7951, A-427, …) | rises with dose | position effect removed |
| [[Gefitinib (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.018 | 9/47 (PANC-1, A-427, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.37×** | +3.4 | 0.025 | 8/46 (SW480, LOX-IMVI, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.036 | 10/46 (SW480, HS-578T, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +3.3 | 0.041 | 16/46 (Panc 03.27, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Levobupivacaine (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.057 | 11/46 (A549, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6534.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 5 µM | ⚠ position correction uncertain | **0.631×** | -7.2 | 5e-10 | 30/47 (A549, KATO III, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.663×** | -6.4 | 5e-08 | 29/47 (HT-29, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.588×** | -5.8 | 1e-06 | 22/44 (PANC-1, A549, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.498×** | -5.5 | 6e-06 | 22/44 (PANC-1, HS-578T, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.609×** | -5.5 | 6e-06 | 25/46 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[vincristine (drug)]] 0.05 µM |  | **0.598×** | -5.3 | 9e-06 | 25/46 (HT-29, KATO III, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.624×** | -5.2 | 2e-05 | 25/46 (Hs 766T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.628×** | -5.1 | 2e-05 | 28/46 (HS-578T, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.729×** | -4.9 | 6e-05 | 20/47 (HEC-1-A, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.645×** | -4.8 | 8e-05 | 22/44 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.734×** | -4.8 | 8e-05 | 23/46 (A498, A549, …) | all doses, flat | composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.657×** | -4.6 | 2e-04 | 25/47 (COLO 205, PANC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.660×** | -4.4 | 5e-04 | 20/46 (HT-29, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.674×** | -4.3 | 6e-04 | 22/46 (KATO III, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.689×** | -4.1 | 0.002 | 19/46 (KATO III, SW 900, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.498×** | -4.0 | 0.002 | 20/46 (SK-MEL-2, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.779×** | -3.9 | 0.003 | 21/47 (A498, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.703×** | -3.9 | 0.003 | 21/46 (SNU-1, A-172, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.718×** | -3.6 | 0.008 | 13/46 (AN3 CA, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.712×** | -3.5 | 0.011 | 10/47 (PANC-1, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6534. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 19.5 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +10.3) | [[Docetaxel (drug)]] 5 µM 0.273× (z -10.3) ⚠ position correction uncertain |
| [[A-172 (line)]] | wt | 8.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +9.7) | — |
| [[A498 (line)]] | wt | 23.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -10.2) ⚠ cell-cycle shift, explains ~78% of this change |
| [[CHP-212 (line)]] | wt | 29.0 | 0 | 1 | — | [[Afatinib (drug)]] 0.05 µM 0.157× (z -9.0) |
| [[HCT15 (line)]] | alt | 10.9 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0634× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 7.94 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.222× (z -10.5) |
| [[HT-29 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 5 µM 0.242× (z -8.7) ⚠ position correction uncertain |
| [[KATO III (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 5 µM 0.322× (z -9.1) ⚠ position correction uncertain |
| [[LoVo (line)]] | wt | 9.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 9.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -11.5) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H460 (line)]] | wt | 9.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +10.2) | — |
| [[SK-MEL-2 (line)]] | alt | 24.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +8.7) | — |
| [[SW480 (line)]] | alt | 17.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +10.7) | — |
| [[A-427 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6534), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF9]] | +0.72 | +0.62 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ZNF487]] | +0.62 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[CFAP210]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[PPIL6]] | +0.58 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[ANKRD42]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[RRP12]] | +0.53 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[CSPP1]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[CCDC157]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[DPAGT1]] | +0.52 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[RNF213-AS1]] | +0.51 | +0.34 / +0.61 | both halves | 1e-04 |  |
| [[FOSB]] | +0.51 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[MIPEP]] | +0.51 | +0.52 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN26]] | -0.51 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[PRDM4]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[PFDN1]] | -0.50 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[ZNF182]] | -0.48 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[MARCHF7]] | -0.48 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[PHAX]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[PDRG1]] | -0.48 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[GORAB]] | -0.47 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ZSCAN12]] | -0.47 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[NAT1]] | -0.47 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[ZNF23]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[FUNDC1]] | -0.47 | -0.48 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFNLR1]] | B | IFNLR1 activity lowers CCDC40's level | lines that do not express IFNLR1 (18) vs lines expressing it (32) | 1.41× higher at baseline in the lines without IFNLR1 | 0.076 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |
| [[SPATA17]] | C | SPATA17 activity raises CCDC40's level | lines that do not express SPATA17 (3) vs lines expressing it (47) | 2.95× lower at baseline in the lines without SPATA17 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ITPR2-AS1, ITPR2, SYCP2L; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 205]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-41.6, 21.9); signed map (-19.1, 4.4). **Vector** length 99.5, 22.0% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +7.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +3.7 | +4.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.5 | -0.3 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | +2.7 | +3.4 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +2.7 | +5.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.3 | +2.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.7 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.3 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.8 | -3.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.4 | -4.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.4 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain 40 molecular ruler complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:80,036,632-80,100,613 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20753, KIAA1640, FLJ32021, CILD15, FAP172, CFAP172 |
| Gene groups (HGNC) | Cilia and flagella associated; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4G0X9](https://www.uniprot.org/uniprotkb/Q4G0X9) (Coiled-coil domain-containing protein 40):

> Required for assembly of dynein regulatory complex (DRC) and inner dynein arm (IDA) complexes, which are responsible for ciliary beat regulation, thereby playing a central role in motility in cilia and flagella. Probably acts together with CCDC39 to form a molecular ruler that determines the 96 nanometer (nm) repeat length and arrangements of components in cilia and flagella (By similarity). Not required for outer dynein arm complexes assembly. Required for axonemal recruitment of CCDC39.

**Summary**, from NCBI Gene [55036](https://www.ncbi.nlm.nih.gov/gene/55036):

> This gene encodes a protein that is necessary for motile cilia function. It functions in correct left-right axis formation by regulating the assembly of the inner dynein arm and the dynein regulatory complexes, which control ciliary beat. Mutations in this gene cause ciliary dyskinesia type 15, a disorder due to defects in cilia motility. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:26090](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26090) · Entrez [55036](https://www.ncbi.nlm.nih.gov/gene/55036) · UniProt [Q4G0X9](https://www.uniprot.org/uniprotkb/Q4G0X9) · Ensembl [ENSG00000141519](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141519)

## Data

Gene col 6534: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6534); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6534, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6534]; `tensor/DDL_lfc|DDL_z.npy` [6534]; `embed/gene_vectors.npy` [6534]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6534 or target_col == 6534). Every well: [[CCDC40 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC40.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
