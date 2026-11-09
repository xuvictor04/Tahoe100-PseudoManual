---
symbol: "GTF2H1"
type: "gene"
col: 3165
ensembl_id: "ENSG00000110768"
name: "general transcription factor IIH subunit 1"
location: "11p15.1"
module: 88
arm: "+"
pooled_cpm: 51.48
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 8
n_dd_up_clean: 13
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# GTF2H1

*general transcription factor IIH subunit 1* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.36× (z +26.8, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.647× (z -9.6, q 4e-19, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCPH1]] (+0.76, fdr 7e-06), [[LINC00571]] (+0.76, fdr 7e-06), [[METTL6]] (+0.75, fdr 1e-05); moves opposite to [[RIMS3]] (-0.71, fdr 1e-05), [[POGLUT2]] (-0.68, fdr 1e-05), [[WASF3]] (-0.68, fdr 5e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SLC9A6]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3165.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.36×** | +26.8 | 0e+00 | 46/48 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.19×** | +17.3 | 0e+00 | 43/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.94×** | +14.0 | 2e-42 | 40/48 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +10.8 | 3e-25 | 41/48 (HT-29, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +8.5 | 2e-15 | 34/48 (NCI-H23, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +8.1 | 5e-14 | 35/48 (A-172, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +7.3 | 2e-11 | 31/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +6.9 | 4e-10 | 28/48 (COLO 205, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +5.7 | 9e-07 | 25/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +5.7 | 9e-07 | 25/49 (A498, J82, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.25×** | +4.9 | 4e-05 | 25/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.27×** | +4.9 | 4e-05 | 21/44 (Hs 766T, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +4.8 | 7e-05 | 20/39 (J82, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM |  | **1.24×** | +4.8 | 7e-05 | 19/48 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +4.5 | 3e-04 | 21/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +4.2 | 9e-04 | 22/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 5 µM |  | 1.20× | +3.8 | 0.004 | 15/48 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.035 | 9/48 (BT-474, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3165.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.647×** | -9.6 | 4e-19 | 40/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.671×** | -8.8 | 4e-16 | 38/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.725×** | -7.1 | 2e-10 | 30/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.798×** | -7.0 | 3e-10 | 28/48 (SW480, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.782×** | -5.4 | 6e-06 | 24/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.807×** | -4.7 | 2e-04 | 22/48 (Hs 766T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.712×** | -3.9 | 0.007 | 13/48 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.722×** | -3.8 | 0.012 | 12/48 (A498, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.890× | -3.6 | 0.017 | 7/48 (LoVo, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3165. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 39.1 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.97× (z +32.7) | — |
| [[A-172 (line)]] | wt | 52.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +24.3) | — |
| [[A498 (line)]] | wt | 70.0 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +15.2) | [[Panobinostat (drug)]] 0.5 µM 0.557× (z -8.5) |
| [[PANC-1 (line)]] | alt | 75.9 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +17.6) | [[Panobinostat (drug)]] 5 µM 0.450× (z -12.9) |
| [[SW480 (line)]] | alt | 65.8 | 3 | 3 | [[Auranofin (drug)]] 5 µM 2.18× (z +10.9) | [[Tucidinostat (drug)]] 5 µM 0.626× (z -9.3) |
| [[J82 (line)]] | alt | 74.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +27.7) | — |
| [[LoVo (line)]] | wt | 40.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +14.5) | — |
| [[COLO 205 (line)]] | alt | 61.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +14.2) | — |
| [[HOP62 (line)]] | alt | 42.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +19.8) | — |
| [[Hs 766T (line)]] | wt | 58.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +26.2) | — |
| [[HT-29 (line)]] | alt | 75.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +13.4) | — |
| [[NCI-H1573 (line)]] | alt | 34.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +17.8) | — |
| [[NCI-H2347 (line)]] | alt | 35.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +21.3) | — |
| [[A-427 (line)]] | wt | 59.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.8) | — |
| [[H4 (line)]] | wt | 75.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +12.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.326× (z -8.9) ⚠ toxic |
| [[HS-578T (line)]] | alt | 39.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +13.8) | — |
| [[hTERT-HPNE (line)]] | wt | 45.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +12.2) | — |
| [[LOX-IMVI (line)]] | wt | 54.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +14.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 66.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +14.9) | — |
| [[NCI-H1792 (line)]] | alt | 34.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +12.2) | — |
| [[NCI-H23 (line)]] | alt | 55.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.4) | — |
| [[RPMI-7951 (line)]] | alt | 57.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +15.7) | — |
| [[SK-MEL-2 (line)]] | alt | 52.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +15.8) | — |
| [[SNU-1 (line)]] | wt | 63.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.10× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -12.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 42.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.8) | — |
| [[AsPC-1 (line)]] | alt | 47.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.3) | — |
| [[C32 (line)]] | wt | 46.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 63.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.7) | — |
| [[HepG2_C3A (line)]] | wt | 36.8 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.257× (z -8.7) ⚠ cell-cycle shift, explains ~6% of this change |
| [[KATO III (line)]] | alt | 36.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 45.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.6) | — |
| [[NCI-H661 (line)]] | alt | 39.9 | 0 | 1 | — | [[ML264 (drug)]] 0.05 µM 0.0618× (z -9.3) |
| [[SNU-423 (line)]] | alt | 78.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +18.4) | — |
| [[SW 900 (line)]] | alt | 22.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3165), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCPH1]] | +0.76 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[LINC00571]] | +0.76 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[METTL6]] | +0.75 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[C11orf58]] | +0.75 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[TRMT13]] | +0.73 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[LZIC]] | +0.73 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[INO80D]] | +0.73 | +0.69 / +0.51 | both halves | 1e-05 | pathway: Global Genome Nucleotide Excision Repair (GG-NER) |
| [[TMEM192]] | +0.73 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.73 | +0.76 / +0.43 | both halves | 3e-05 |  |
| [[C1orf43]] | +0.72 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[BPTF]] | +0.72 | +0.85 / +0.54 | both halves | 1e-05 |  |
| [[ZNF764]] | +0.72 | +0.77 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIMS3]] | -0.71 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[POGLUT2]] | -0.68 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[WASF3]] | -0.68 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[PDXP]] | -0.68 | -0.58 / -0.59 | both halves | 8e-06 |  |
| [[SEMA4F]] | -0.67 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[OSTF1]] | -0.66 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[IDH2]] | -0.66 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[YIF1B]] | -0.66 | -0.62 / -0.29 | both halves | 2e-04 |  |
| [[METAP1]] | -0.65 | -0.73 / -0.37 | both halves | 8e-05 |  |
| [[SLC9A6]] | -0.64 | -0.65 / -0.41 | both halves | 4e-05 |  |
| [[HDAC3]] | -0.64 | -0.67 / -0.48 | both halves | 2e-05 | pathway: Epigenetic regulation of gene expression |
| [[ATP7B]] | -0.64 | -0.62 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises GTF2H1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises GTF2H1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC9A6]] | C | GTF2H1's natural level strengthens SLC9A6's drug response | GTF2H1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse -0.06; direction not clear | 0.052 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.801). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-0.0, 9.0); signed map (18.7, -20.3). **Vector** length 119, 31.8% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.9 | +17.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.5 | +26.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.8 | +10.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.0 | +14.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.8 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +5.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.2 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +1.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -7.3 | -7.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.1 | -8.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.1 | -9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.2 | -7.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.3 | -5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -3.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.6 | -3.9 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -2.2 | -2.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIH subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:18,322,295-18,367,045 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BTF2, P62, TFIIH |
| Gene groups (HGNC) | Nucleotide excision repair; General transcription factor IIH complex subunits |
| Hallmark sets | DNA_REPAIR, MTORC1_SIGNALING |
| Reactome | 42 pathways, smallest: RNA Pol II CTD phosphorylation and interaction with CE during HIV infection; RNA Pol II CTD phosphorylation and interaction with CE; mRNA Capping |
| Matched by | ensembl_id |

**Function**, from UniProt [P32780](https://www.uniprot.org/uniprotkb/P32780) (General transcription factor IIH subunit 1):

> Component of the general transcription and DNA repair factor IIH (TFIIH) core complex, which is involved in general and transcription-coupled nucleotide excision repair (NER) of damaged DNA and, when complexed to CAK, in RNA transcription by RNA polymerase II. In NER, TFIIH acts by opening DNA around the lesion to allow the excision of the damaged oligonucleotide and its replacement by a new DNA fragment. In transcription, TFIIH has an essential role in transcription initiation. When the …

**Summary**, from NCBI Gene [2965](https://www.ncbi.nlm.nih.gov/gene/2965):

> Enables nuclear thyroid hormone receptor binding activity. Involved in positive regulation of DNA-templated transcription and transcription initiation at RNA polymerase II promoter. Located in nucleoplasm. Part of transcription factor TFIIH core complex and transcription factor TFIIH holo complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:4655](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4655) · Entrez [2965](https://www.ncbi.nlm.nih.gov/gene/2965) · UniProt [P32780](https://www.uniprot.org/uniprotkb/P32780) · Ensembl [ENSG00000110768](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110768)

## Data

Gene col 3165: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3165); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3165, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3165]; `tensor/DDL_lfc|DDL_z.npy` [3165]; `embed/gene_vectors.npy` [3165]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3165 or target_col == 3165). Every well: [[GTF2H1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2H1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
