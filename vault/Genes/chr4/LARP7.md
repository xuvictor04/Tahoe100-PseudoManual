---
symbol: "LARP7"
type: "gene"
col: 10518
ensembl_id: "ENSG00000174720"
name: "La ribonucleoprotein 7, transcriptional regulator"
location: "4q25"
module: 51
arm: "+"
pooled_cpm: 72.5
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# LARP7

*La ribonucleoprotein 7, transcriptional regulator* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.97× (z +9.8, q 9e-20, up in 42 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.28× (z +3.5, q 0.025, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.599× (z -7.3, q 1e-10, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LZIC]] (+0.76, fdr 7e-06), [[CWC22]] (+0.75, fdr 7e-06), [[RBM23]] (+0.75, fdr 7e-06); moves opposite to [[NME2]] (-0.69, fdr 1e-05), [[PLEKHA8]] (-0.68, fdr 7e-06), [[NUTF2]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PRR5-ARHGAP8]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10518.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.97×** | +9.8 | 9e-20 | 42/49 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +8.2 | 5e-14 | 40/44 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.47×** | +5.6 | 4e-06 | 33/48 (C32, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.46×** | +5.2 | 2e-05 | 36/48 (C32, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.28×** | +5.0 | 6e-05 | 31/48 (C32, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.38×** | +4.6 | 4e-04 | 31/48 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +4.3 | 0.002 | 31/45 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.31×** | +3.9 | 0.008 | 35/48 (C32, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.025 | 26/48 (RKO, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.037 | 25/48 (C32, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.037 | 25/48 (LS 180, hTERT-HPNE, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.50×** | +3.1 | 0.099 | 25/47 (RKO, H4, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10518.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.599×** | -7.3 | 1e-10 | 42/48 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.652×** | -6.1 | 3e-07 | 41/48 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.728×** | -4.5 | 1e-03 | 31/48 (Panc 03.27, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.730×** | -4.5 | 1e-03 | 35/48 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.756×** | -3.9 | 0.008 | 29/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.823×** | -3.9 | 0.008 | 21/49 (SNU-1, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -3.8 | 0.013 | 25/48 (A-172, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.778×** | -3.6 | 0.025 | 26/48 (NCI-H460, J82, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -3.5 | 0.026 | 1/49 (AN3 CA) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.630×** | -3.5 | 0.031 | 26/49 (AsPC-1, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.789×** | -3.4 | 0.037 | 26/48 (NCI-H1573, SW1417, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.799×** | -3.2 | 0.066 | 23/48 (Hs 766T, SW 1088, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.796×** | -3.1 | 0.090 | 20/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10518. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 69.5 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 93.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +10.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 59.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C32 (line)]] | wt | 82.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[J82 (line)]] | alt | 57.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 117 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | [[Belinostat (drug)]] 5 µM 0.419× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 69.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +11.1) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.384× (z -9.0) |
| [[SW480 (line)]] | alt | 60.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +12.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 77.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -10.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[COLO 205 (line)]] | alt | 108 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.389× (z -8.6) |
| [[HOP62 (line)]] | alt | 63.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 78.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 92.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 78.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 70.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -8.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Panc 03.27 (line)]] | alt | 82.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +9.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 60.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +9.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 85.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -11.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SHP-77 (line)]] | alt | 50.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.32× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -12.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 1088 (line)]] | alt | 95.2 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0814× (z -9.5) |
| [[AN3 CA (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 79.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 76.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 82.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 72.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 80.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 79.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10518), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LZIC]] | +0.76 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[CWC22]] | +0.75 | +0.72 / +0.73 | both halves | 7e-06 | STRING 476 |
| [[RBM23]] | +0.75 | +0.79 / +0.65 | both halves | 7e-06 | same gene group |
| [[ZNF518A]] | +0.75 | +0.81 / +0.57 | both halves | 1e-05 |  |
| [[TRIP11]] | +0.74 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[EPC1]] | +0.74 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[ACIN1]] | +0.74 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[OCIAD1]] | +0.73 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[LINC00174]] | +0.73 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[BPTF]] | +0.73 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[USP16]] | +0.73 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[C11orf58]] | +0.73 | +0.75 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NME2]] | -0.69 | -0.69 / -0.55 | both halves | 1e-05 |  |
| [[PLEKHA8]] | -0.68 | -0.70 / -0.58 | both halves | 7e-06 |  |
| [[NUTF2]] | -0.68 | -0.71 / -0.61 | both halves | 7e-06 |  |
| [[WRNIP1]] | -0.66 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[METAP1]] | -0.66 | -0.72 / -0.53 | both halves | 1e-05 |  |
| [[RNF4]] | -0.66 | -0.69 / -0.53 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | -0.65 | -0.69 / -0.55 | both halves | 1e-05 |  |
| [[ZDHHC9]] | -0.65 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[COLGALT1]] | -0.65 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[PIGF]] | -0.64 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[TENT4A]] | -0.64 | -0.67 / -0.59 | both halves | 7e-06 |  |
| [[GRB2]] | -0.64 | -0.66 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRR5-ARHGAP8]] | C | PRR5-ARHGAP8 activity raises LARP7's level | lines that do not express PRR5-ARHGAP8 (4) vs lines expressing it (46) | 1.49× lower at baseline in the lines without PRR5-ARHGAP8 | 0.040 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: NECTIN1, PLEKHG3, SNED1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.794). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.9, 9.5); signed map (7.5, -19.4). **Vector** length 104, 32.3% of its response variance represented; |z| ≥ 3 in 716 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +10.9 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +9.7 | +5.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +7.8 | +5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.1 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.0 | +1.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.0 | -3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.6 | -4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.4 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.0 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.1 | -1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[Lopinavir (drug)]] 5 µM |  | -1.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | La ribonucleoprotein 7, transcriptional regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:112,637,077-112,657,696 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HDCMA18P, PIP7S, DKFZP564K112 |
| Gene groups (HGNC) | La ribonucleoproteins; RNA binding motif containing; 7SK snRNP complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4G0J3](https://www.uniprot.org/uniprotkb/Q4G0J3) (La-related protein 7):

> RNA-binding protein that specifically binds distinct small nuclear RNA (snRNAs) and regulates their processing and function. Specifically binds the 7SK snRNA (7SK RNA) and acts as a core component of the 7SK ribonucleoprotein (RNP) complex, thereby acting as a negative regulator of transcription elongation by RNA polymerase II. The 7SK RNP complex sequesters the positive transcription elongation factor b (P-TEFb) in a large inactive 7SK RNP complex preventing RNA polymerase II phosphorylation …

**Summary**, from NCBI Gene [51574](https://www.ncbi.nlm.nih.gov/gene/51574):

> This gene encodes a protein which is found in the 7SK snRNP (small nuclear ribonucleoprotein). This snRNP complex inhibits a cyclin-dependent kinase, positive transcription elongation factor b, which is required for paused RNA polymerase II at a promoter to begin transcription elongation. A pseudogene of this gene is located on chromosome 3. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2012]

**Accessions** — [HGNC:24912](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24912) · Entrez [51574](https://www.ncbi.nlm.nih.gov/gene/51574) · UniProt [Q4G0J3](https://www.uniprot.org/uniprotkb/Q4G0J3) · Ensembl [ENSG00000174720](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174720)

## Data

Gene col 10518: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10518); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10518, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10518]; `tensor/DDL_lfc|DDL_z.npy` [10518]; `embed/gene_vectors.npy` [10518]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10518 or target_col == 10518). Every well: [[LARP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LARP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
