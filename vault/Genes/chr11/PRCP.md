---
symbol: "PRCP"
type: "gene"
col: 6029
ensembl_id: "ENSG00000137509"
name: "prolylcarboxypeptidase"
location: "11q14"
module: 29
arm: "+"
pooled_cpm: 35.82
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PRCP

*prolylcarboxypeptidase* — 11q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.03× (z +22.3, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.693× (z -8.1, q 2e-13, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACADSB]] (+0.67, fdr 7e-06), [[ITM2B]] (+0.65, fdr 1e-05), [[SH3BGRL]] (+0.62, fdr 1e-05); moves opposite to [[RRP7A]] (-0.71, fdr 1e-05), [[PWP2]] (-0.63, fdr 1e-05), [[RRP7BP-1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MYL9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6029.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +22.3 | 0e+00 | 45/48 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +13.8 | 5e-41 | 31/48 (LoVo, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +11.1 | 4e-26 | 40/48 (AsPC-1, RKO, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +10.4 | 3e-23 | 30/48 (SNU-423, HS-578T, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +9.0 | 3e-17 | 30/46 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +8.4 | 4e-15 | 22/38 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +8.0 | 1e-13 | 29/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.8 | 1e-09 | 29/48 (LOX-IMVI, A-172, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +6.3 | 2e-08 | 25/48 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.32×** | +6.2 | 3e-08 | 31/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +5.6 | 1e-06 | 23/48 (SW1417, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.28×** | +5.5 | 2e-06 | 21/48 (PANC-1, SW1417, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.23×** | +4.6 | 2e-04 | 19/48 (SW1417, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.47×** | +4.5 | 3e-04 | 20/48 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.2 | 9e-04 | 13/33 (SNU-423, hTERT-HPNE, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +4.2 | 1e-03 | 15/48 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.13× | +3.3 | 0.031 | 5/48 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.10× | +3.0 | 0.077 | 4/48 (HOP62, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6029.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.693×** | -8.1 | 2e-13 | 33/48 (HOP62, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.743×** | -6.6 | 1e-08 | 28/48 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.746×** | -6.5 | 1e-08 | 28/48 (HOP62, H4, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.748×** | -6.4 | 2e-08 | 26/48 (PANC-1, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.791×** | -5.2 | 2e-05 | 24/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.780×** | -5.1 | 3e-05 | 19/47 (A498, RPMI-7951, …) | all doses, flat | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.816×** | -4.5 | 5e-04 | 22/48 (NCI-H1573, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.7 | 0.014 | 14/48 (PANC-1, SW 1271, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.848× | -3.7 | 0.016 | 10/48 (SW480, H4, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.858× | -3.3 | 0.062 | 19/48 (HOP62, A-172, …) | all doses, flat | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | 0.862× | -3.2 | 0.081 | 15/48 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Tranilast (drug)]] 0.05 µM |  | 0.863× | -3.0 | 0.11 | 8/48 (AN3 CA, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6029. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 44.7 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +20.6) | — |
| [[AN3 CA (line)]] | alt | 71.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -9.5) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.330× (z -9.1) |
| [[HS-578T (line)]] | alt | 51.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +18.0) | — |
| [[SW480 (line)]] | alt | 45.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.0) | — |
| [[A-427 (line)]] | wt | 48.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -16.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 52.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 30.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 24.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +18.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 39.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +13.3) | — |
| [[NCI-H2030 (line)]] | alt | 64.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +16.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.455× (z -9.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H23 (line)]] | alt | 28.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.1) | — |
| [[SNU-1 (line)]] | wt | 45.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -11.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 44.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +11.4) | — |
| [[SW1417 (line)]] | alt | 40.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +10.6) | — |
| [[A-172 (line)]] | wt | 43.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +15.4) | — |
| [[A498 (line)]] | wt | 31.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +13.6) | — |
| [[A549 (line)]] | wt | 38.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +8.9) | — |
| [[AsPC-1 (line)]] | alt | 13.2 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.97× (z +8.7) | — |
| [[C32 (line)]] | wt | 42.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.312× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 12.8 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0841× (z -10.5) |
| [[HOP62 (line)]] | alt | 29.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.366× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 43.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.5) | — |
| [[J82 (line)]] | alt | 39.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.1) | — |
| [[LoVo (line)]] | wt | 24.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +19.9) | — |
| [[LS 180 (line)]] | wt | 36.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 30.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +18.3) | — |
| [[Panc 03.27 (line)]] | alt | 38.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.9) | — |
| [[RKO (line)]] | wt | 41.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 41.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 37.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +11.1) | — |
| [[BT-474 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6029), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACADSB]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[ITM2B]] | +0.65 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[SH3BGRL]] | +0.62 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ATP6AP1]] | +0.62 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[DDOST]] | +0.62 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[SGCE]] | +0.61 | +0.39 / +0.68 | both halves | 6e-05 |  |
| [[ATRAID]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[BPNT1]] | +0.60 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[GNAS]] | +0.59 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[AGA]] | +0.59 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[MMP2]] | +0.58 | +0.25 / +0.57 | both halves | 4e-04 |  |
| [[TWSG1]] | +0.58 | +0.45 / +0.69 | both halves | 3e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP7A]] | -0.71 | -0.54 / -0.71 | both halves | 1e-05 |  |
| [[PWP2]] | -0.63 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[RRP7BP-1]] | -0.61 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[REXO4]] | -0.60 | -0.34 / -0.68 | both halves | 1e-04 |  |
| [[UBL4A]] | -0.59 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[SURF6]] | -0.58 | -0.30 / -0.68 | both halves | 2e-04 |  |
| [[EIF5B]] | -0.58 | -0.37 / -0.56 | both halves | 9e-05 |  |
| [[DNTTIP2]] | -0.58 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[METTL2A]] | -0.58 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[ADRM1]] | -0.58 | -0.37 / -0.67 | both halves | 7e-05 |  |
| [[EXOSC4]] | -0.58 | -0.56 / -0.51 | both halves | 1e-05 | STRING 427 |
| [[CIAO1]] | -0.57 | -0.40 / -0.59 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYL9]] | B | MYL9 activity raises PRCP's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.27× lower at baseline in the lines without MYL9 | 0.035 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[CERCAM]] | B | CERCAM activity raises PRCP's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 1.49× lower at baseline in the lines without CERCAM | 0.064 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[TOP2A]] | B | TOP2A activity lowers PRCP's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CRTAP]] | C | CRTAP activity raises PRCP's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without CRTAP | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.597). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.7, -19.5); signed map (-24.4, -36.8). **Vector** length 98.2, 22.2% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.9 | +11.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +22.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +6.5 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +4.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.0 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +2.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.1 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -6.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.1 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | prolylcarboxypeptidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14 — chr11:82,822,936-82,970,584 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PCP, HUMPCP |
| Gene groups (HGNC) | Minor histocompatibility antigens; M14 carboxypeptidases |
| Hallmark sets | COMPLEMENT |
| Reactome | 3 pathways, smallest: FXIIa activates plasma kallikrein-kinin system; Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P42785](https://www.uniprot.org/uniprotkb/P42785) (Lysosomal Pro-X carboxypeptidase):

> Cleaves C-terminal amino acids linked to proline in peptides such as angiotensin II, III and des-Arg9-bradykinin. This cleavage occurs at acidic pH, but enzymatic activity is retained with some substrates at neutral pH.

**Summary**, from NCBI Gene [5547](https://www.ncbi.nlm.nih.gov/gene/5547):

> This gene encodes a member of the peptidase S28 family of serine exopeptidases. The encoded preproprotein is proteolytically processed to generate the mature lysosomal prolylcarboxypeptidase. This enzyme cleaves C-terminal amino acids linked to proline in peptides such as angiotension II, III and des-Arg9-bradykinin. The cleavage occurs at acidic pH, but the enzyme activity is retained with some substrates at neutral pH. This enzyme has been shown to be an activator of the cell …

**Accessions** — [HGNC:9344](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9344) · Entrez [5547](https://www.ncbi.nlm.nih.gov/gene/5547) · UniProt [P42785](https://www.uniprot.org/uniprotkb/P42785) · Ensembl [ENSG00000137509](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137509)

## Data

Gene col 6029: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6029); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6029, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6029]; `tensor/DDL_lfc|DDL_z.npy` [6029]; `embed/gene_vectors.npy` [6029]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6029 or target_col == 6029). Every well: [[PRCP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRCP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
