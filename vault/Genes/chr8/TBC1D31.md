---
symbol: "TBC1D31"
type: "gene"
col: 8012
ensembl_id: "ENSG00000156787"
name: "TBC1 domain family member 31"
location: "8q24.13"
module: 6
arm: "+"
pooled_cpm: 31.38
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# TBC1D31

*TBC1 domain family member 31* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +18.1, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.440× (z -8.6, q 4e-15, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF15]] (+0.70, fdr 7e-06), [[CCDC14]] (+0.69, fdr 7e-06), [[VRK1]] (+0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8012.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +18.1 | 0e+00 | 44/47 (LS 180, RKO, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.99×** | +13.8 | 7e-41 | 42/48 (A498, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.81×** | +12.0 | 1e-30 | 38/47 (HT-29, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.85×** | +11.9 | 2e-30 | 33/47 (NCI-H460, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.77×** | +11.4 | 3e-28 | 38/48 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +9.5 | 3e-19 | 34/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.56×** | +8.6 | 9e-16 | 24/37 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **1.51×** | +8.2 | 1e-14 | 30/44 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.51×** | +8.2 | 1e-14 | 35/47 (HEC-1-A, RKO, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.03×** | +7.4 | 6e-12 | 33/48 (HT-29, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.45×** | +7.2 | 3e-11 | 30/48 (SW480, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **1.44×** | +7.1 | 7e-11 | 26/44 (HEC-1-A, HT-29, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +5.6 | 9e-07 | 20/48 (HEC-1-A, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +5.5 | 2e-06 | 19/48 (HEC-1-A, NCI-H2347, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +5.3 | 5e-06 | 23/48 (HS-578T, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +4.9 | 2e-05 | 21/48 (NCI-H2347, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +4.0 | 0.002 | 10/48 (HS-578T, SK-MEL-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.031 | 7/48 (NCI-H23, C-33 A, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | 1.19× | +3.1 | 0.042 | 6/48 (Hs 766T, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.043 | 4/48 (SW480, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.045 | 1/47 (HS-578T) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | 1.16× | +3.0 | 0.060 | 5/48 (A549, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8012.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.440×** | -8.6 | 4e-15 | 30/48 (SHP-77, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.684×** | -7.6 | 6e-12 | 25/46 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.500×** | -7.3 | 6e-11 | 27/47 (HOP62, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.740×** | -6.0 | 2e-07 | 22/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.746×** | -5.9 | 4e-07 | 23/48 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.829×** | -5.3 | 9e-06 | 24/48 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.801×** | -4.5 | 6e-04 | 18/48 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.786×** | -3.5 | 0.039 | 15/44 (HepG2/C3A, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -3.2 | 0.10 | 17/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | 0.746× | -3.1 | 0.12 | 10/45 (PANC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.852× | -3.0 | 0.13 | 10/48 (MIA PaCa-2, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8012. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 12.5 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.66× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +9.2) | [[Saquinavir (drug)]] 0.5 µM 0.205× (z -9.6) |
| [[PANC-1 (line)]] | alt | 50.5 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.342× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.417× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 27.5 | 2 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.373× (z -9.2) |
| [[SW480 (line)]] | alt | 36.6 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.8) | [[Digitoxin (drug)]] 0.5 µM 0.444× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.460× (z -8.6) |
| [[RKO (line)]] | wt | 52.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[A498 (line)]] | wt | 53.4 | 2 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +9.5) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[AN3 CA (line)]] | alt | 37.2 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.109× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Monocrotaline (drug)]] 0.05 µM 0.102× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 28.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +8.7) | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.164× (z -9.1) |
| [[LoVo (line)]] | wt | 19.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 19.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.179× (z -12.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 21.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.0) | — |
| [[A549 (line)]] | wt | 31.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +9.9) | — |
| [[C32 (line)]] | wt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +9.4) | — |
| [[H4 (line)]] | wt | 29.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.277× (z -9.0) |
| [[HOP62 (line)]] | alt | 31.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.422× (z -11.0) |
| [[HS-578T (line)]] | alt | 39.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 64.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +8.8) | — |
| [[KATO III (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.261× (z -10.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 36.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.248× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 23.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 31.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 29.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +10.1) | — |
| [[SNU-1 (line)]] | wt | 24.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8012), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF15]] | +0.70 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[CCDC14]] | +0.69 | +0.72 / +0.63 | both halves | 7e-06 | same gene group; STRING 746 |
| [[VRK1]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[TMPO]] | +0.68 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[ZWILCH]] | +0.68 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[PBK]] | +0.67 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[CENPH]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[KNTC1]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[RAD51AP1]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[MELK]] | +0.66 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[FANCI]] | +0.66 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[CENPN]] | +0.66 | +0.56 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TBC1D31's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP1]] | B | TOP1 activity lowers TBC1D31's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DSCC1]] | C | DSCC1 activity raises TBC1D31's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.77× lower at baseline in the lines without DSCC1 | 0.098 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.596). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-38.7, -45.3); signed map (-39.9, -48.5). **Vector** length 89.8, 21.0% of its response variance represented; |z| ≥ 3 in 1,150 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Resolution of D-loop Structures through Holliday Junction Intermediates* (reactome, mean cos +0.51 to 12); *Resolution of D-Loop Structures* (reactome, mean cos +0.51 to 12); *Resolution of D-loop Structures through Synthesis-Dependent Strand Annealing (SDSA)* (reactome, mean cos +0.53 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | +3.6 | +8.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.4 | +11.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.3 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | +3.3 | +8.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +1.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.2 | +1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +1.0 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +1.8 | +3.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.7 | +0.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.4 | -5.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.9 | -5.9 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.0 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -3.1 | +11.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -4.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.5 | -2.0 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -2.5 | -2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:123,041,968-123,152,153 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC21654, Gm85; previously WDR67 |
| Gene groups (HGNC) | WD repeat domain containing; TBC1 domain family members; Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DN5](https://www.uniprot.org/uniprotkb/Q96DN5) (TBC1 domain family member 31):

> Molecular adapter which is involved in cilium biogenesis. Part of a functional complex including OFD1 a centriolar protein involved in cilium assembly. Could regulate the cAMP-dependent phosphorylation of OFD1, and its subsequent ubiquitination by PJA2 which ultimately leads to its proteasomal degradation.

**Summary**, from NCBI Gene [93594](https://www.ncbi.nlm.nih.gov/gene/93594):

> Enables molecular adaptor activity. Involved in cilium assembly. Located in centriolar satellite and ciliary basal body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30888](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30888) · Entrez [93594](https://www.ncbi.nlm.nih.gov/gene/93594) · UniProt [Q96DN5](https://www.uniprot.org/uniprotkb/Q96DN5) · Ensembl [ENSG00000156787](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156787)

## Data

Gene col 8012: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8012); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8012, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8012]; `tensor/DDL_lfc|DDL_z.npy` [8012]; `embed/gene_vectors.npy` [8012]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8012 or target_col == 8012). Every well: [[TBC1D31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
