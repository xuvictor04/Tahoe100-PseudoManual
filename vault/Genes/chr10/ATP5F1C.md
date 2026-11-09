---
symbol: "ATP5F1C"
type: "gene"
col: 9151
ensembl_id: "ENSG00000165629"
name: "ATP synthase F1 subunit gamma"
location: "10p14"
module: 57
arm: "+"
pooled_cpm: 58.35
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# ATP5F1C

*ATP synthase F1 subunit gamma* — 10p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.23× (z +13.8, q 1e-40, up in 43 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.28× (z +4.3, q 0.001, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.635× (z -11.1, q 8e-26, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHB]] (+0.76, fdr 7e-06), [[NDRG3]] (+0.76, fdr 7e-06), [[MRS2]] (+0.75, fdr 7e-06); moves opposite to [[SP2]] (-0.66, fdr 1e-05), [[MEPCE]] (-0.64, fdr 2e-05), [[ARMC5]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF888]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9151.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.23×** | +13.8 | 1e-40 | 43/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +11.9 | 2e-30 | 40/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +7.0 | 6e-10 | 33/45 (A549, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.37×** | +5.5 | 5e-06 | 30/48 (NCI-H1792, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.36×** | +5.3 | 1e-05 | 31/48 (NCI-H23, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.32×** | +4.8 | 1e-04 | 31/48 (NCI-H1792, BT-474, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.30×** | +4.4 | 0.001 | 25/47 (A-172, NCI-H1792, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +4.3 | 0.001 | 26/48 (HEC-1-A, HOP62, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.55×** | +3.9 | 0.007 | 24/47 (RPMI-7951, SW 900, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.5 | 0.028 | 14/48 (AsPC-1, LOX-IMVI, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | 1.20× | +3.1 | 0.083 | 16/47 (A549, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.20× | +3.1 | 0.083 | 13/47 (A-172, H4, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.083 | 16/48 (HOP62, A498, …) | top dose only |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.20×** | +3.1 | 0.085 | 14/47 (HOP62, SW 900, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.085 | 17/48 (HOP62, C32, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.41×** | +3.0 | 0.085 | 16/46 (LS 180, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.0 | 0.095 | 10/48 (HOP62, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9151.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.635×** | -11.1 | 8e-26 | 36/48 (NCI-H1792, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.828×** | -4.6 | 0.001 | 23/48 (HepG2/C3A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.793×** | -4.0 | 0.012 | 24/48 (H4, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.803×** | -3.6 | 0.038 | 20/48 (AN3 CA, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.830× | -3.2 | 0.15 | 19/48 (SNU-1, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.838× | -3.0 | 0.22 | 21/48 (NCI-H460, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9151. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 48.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +14.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -12.4) |
| [[A498 (line)]] | wt | 81.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -12.9) |
| [[A549 (line)]] | wt | 74.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -8.6) |
| [[LoVo (line)]] | wt | 66.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 58.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -16.0) |
| [[AN3 CA (line)]] | alt | 66.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.106× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 70.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -14.4) |
| [[HepG2_C3A (line)]] | wt | 57.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -9.6) |
| [[HOP62 (line)]] | alt | 44.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -11.1) |
| [[J82 (line)]] | alt | 56.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 57.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 70.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 58.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -11.0) |
| [[PANC-1 (line)]] | alt | 45.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.33× (z +13.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 60.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -14.7) |
| [[SNU-423 (line)]] | alt | 45.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +11.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 68.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 54.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +10.8) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 55.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +8.7) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 50.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +9.7) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 69.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.4) |
| [[H4 (line)]] | wt | 37.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -11.6) |
| [[HS-578T (line)]] | alt | 52.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 60.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 49.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 62.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 50.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -8.9) |
| [[SW 900 (line)]] | alt | 51.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -8.6) |
| [[SW480 (line)]] | alt | 65.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +10.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 87.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 78.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 88.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9151), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHB]] | +0.76 | +0.72 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 968 |
| [[NDRG3]] | +0.76 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[MRS2]] | +0.75 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[PLA2G12A]] | +0.71 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[SKIC3]] | +0.71 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[CAT]] | +0.71 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[STX7]] | +0.70 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[VDAC3]] | +0.69 | +0.72 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 697 |
| [[LTA4H]] | +0.69 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[RAB4A]] | +0.69 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[HBS1L]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SP2]] | -0.66 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[MEPCE]] | -0.64 | -0.65 / -0.46 | both halves | 2e-05 |  |
| [[ARMC5]] | -0.63 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[CLCF1]] | -0.63 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[KDM6B]] | -0.63 | -0.57 / -0.50 | both halves | 1e-05 | STRING 901 |
| [[THUMPD3-AS1]] | -0.63 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[DPH1-AS1]] | -0.62 | -0.64 / -0.57 | both halves | 1e-05 |  |
| [[TLNRD1]] | -0.62 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[ZNF274]] | -0.62 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[GPR137]] | -0.62 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[ZNF341-AS1]] | -0.61 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[RBBP6]] | -0.61 | -0.55 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF888]] | B | ZNF888 activity lowers ATP5F1C's level | lines that do not express ZNF888 (6) vs lines expressing it (44) | 1.30× higher at baseline in the lines without ZNF888 | 0.0997 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF816, ZNF468, ZNF701 |
| [[GSTM4]] | C | GSTM4 activity raises ATP5F1C's level | lines that do not express GSTM4 (4) vs lines expressing it (46) | 1.26× lower at baseline in the lines without GSTM4 | 0.022 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC00888, KIF3C, GGH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.830). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.1, -7.6); signed map (-33.4, -13.7). **Vector** length 94.5, 25.1% of its response variance represented; |z| ≥ 3 in 629 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.5 | +5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +2.5 |
|  | [[NG25 (drug)]] 5 µM |  | +3.4 | +3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +4.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +0.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.4 | -11.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.7 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.9 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | +1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase F1 subunit gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p14 — chr10:7,788,147-7,807,815 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ATP5CL1, ATP5C, ATP5C1 |
| Gene groups (HGNC) | Mitochondrial complex V: ATP synthase subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 6 pathways, smallest: Formation of ATP by chemiosmotic coupling; Cristae formation; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P36542](https://www.uniprot.org/uniprotkb/P36542) (ATP synthase F(1) complex subunit gamma, mitochondrial):

> Subunit gamma, of the mitochondrial membrane ATP synthase complex (F(1)F(0) ATP synthase or Complex V) that produces ATP from ADP in the presence of a proton gradient across the membrane which is generated by electron transport complexes of the respiratory chain. ATP synthase complex consist of a soluble F(1) head domain - the catalytic core - and a membrane F(1) domain - the membrane proton channel. These two domains are linked by a central stalk rotating inside the F(1) region and a …

**Summary**, from NCBI Gene [509](https://www.ncbi.nlm.nih.gov/gene/509):

> This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic portion of mitochondrial ATP synthase consists of 5 different subunits (alpha, beta, gamma, …

**Accessions** — [HGNC:833](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:833) · Entrez [509](https://www.ncbi.nlm.nih.gov/gene/509) · UniProt [P36542](https://www.uniprot.org/uniprotkb/P36542) · Ensembl [ENSG00000165629](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165629)

## Data

Gene col 9151: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9151); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9151, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9151]; `tensor/DDL_lfc|DDL_z.npy` [9151]; `embed/gene_vectors.npy` [9151]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9151 or target_col == 9151). Every well: [[ATP5F1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP5F1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
