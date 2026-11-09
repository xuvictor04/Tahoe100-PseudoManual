---
symbol: "THOC3"
type: "gene"
col: 580
ensembl_id: "ENSG00000051596"
name: "THO complex subunit 3"
location: "5q35.2"
module: 40
arm: "+"
pooled_cpm: 15.93
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# THOC3

*THO complex subunit 3* — 5q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.21× (z +11.5, q 1e-27, up in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.46× (z +5.4, q 4e-06, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.516× (z -13.6, q 2e-39, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OXNAD1]] (+0.73, fdr 7e-06), [[IER3IP1]] (+0.73, fdr 7e-06), [[RNF121]] (+0.72, fdr 7e-06); moves opposite to [[LIG4]] (-0.66, fdr 7e-06), [[CACNA2D1]] (-0.64, fdr 1e-05), [[SKIL]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[EBF1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 580.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.21×** | +11.5 | 1e-27 | 45/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.62×** | +9.8 | 2e-20 | 32/46 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.94×** | +9.6 | 2e-19 | 39/47 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.83×** | +8.7 | 4e-16 | 38/48 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.75×** | +7.4 | 2e-11 | 33/43 (NCI-H2030, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.61×** | +6.9 | 6e-10 | 24/38 (SHP-77, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.54×** | +5.7 | 1e-06 | 21/46 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +5.4 | 4e-06 | 23/47 (LOX-IMVI, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.42×** | +4.7 | 2e-04 | 13/33 (SHP-77, SW1417, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **1.42×** | +4.7 | 2e-04 | 13/27 (MIA PaCa-2, A-172, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +4.3 | 9e-04 | 16/48 (CFPAC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.35×** | +4.0 | 0.003 | 17/48 (A-427, LS 180, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.35×** | +4.0 | 0.003 | 9/45 (A-172, C32, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.003 | 13/48 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +3.9 | 0.004 | 16/42 (LOX-IMVI, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.005 | 16/48 (MIA PaCa-2, AN3 CA, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.013 | 14/45 (Panc 03.27, KATO III, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.026 | 7/45 (NCI-H23, NCI-H460, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Decitabine (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.059 | 9/47 (NCI-H23, CFPAC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +2.9 | 0.092 | 8/47 (NCI-H460, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 580.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.516×** | -13.6 | 2e-39 | 39/47 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.496×** | -10.2 | 7e-22 | 30/46 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.521×** | -9.5 | 5e-19 | 36/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.607×** | -7.3 | 6e-11 | 31/47 (KATO III, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.597×** | -6.9 | 6e-10 | 27/48 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.668×** | -5.9 | 4e-07 | 26/47 (AsPC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.756×** | -4.1 | 0.003 | 17/48 (H4, LS 180, …) | all doses, flat |  |
| [[Tirabrutinib (drug)]] 0.05 µM |  | **0.768×** | -3.6 | 0.026 | 7/48 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.786×** | -3.5 | 0.026 | 10/48 (SW 1088, SW480, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.788×** | -3.2 | 0.071 | 13/47 (NCI-H2030, A549, …) | rises with dose |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.789×** | -3.2 | 0.071 | 11/47 (SNU-423, AsPC-1, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.792×** | -3.1 | 0.078 | 7/48 (SW480, NCI-H1573, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.811×** | -3.1 | 0.097 | 8/47 (NCI-H2347, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 580. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 14.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -17.3) |
| [[A-172 (line)]] | wt | 14.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 9.44 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0723× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -9.3) |
| [[PANC-1 (line)]] | alt | 10.3 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +10.3) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A498 (line)]] | wt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -9.5) |
| [[AN3 CA (line)]] | alt | 30.8 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0911× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -11.5) |
| [[H4 (line)]] | wt | 35.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 42.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -10.1) |
| [[HOP62 (line)]] | alt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -16.4) |
| [[Hs 766T (line)]] | wt | 7.33 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.124× (z -8.5) ⚠ transcription drop |
| [[hTERT-HPNE (line)]] | wt | 7.70 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0746× (z -8.7) |
| [[J82 (line)]] | alt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.3) |
| [[LS 180 (line)]] | wt | 19.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.3) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 25.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -15.8) |
| [[NCI-H2347 (line)]] | alt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -9.1) |
| [[SNU-1 (line)]] | wt | 12.5 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0729× (z -9.5) |
| [[A-427 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 580), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OXNAD1]] | +0.73 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.73 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[RNF121]] | +0.72 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[SDHAP1]] | +0.70 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[CYB561D2]] | +0.69 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[MED26]] | +0.69 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[SHQ1]] | +0.69 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[RARS2]] | +0.67 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[PPIH]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[CRLS1]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SGSM3]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIG4]] | -0.66 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[CACNA2D1]] | -0.64 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[SKIL]] | -0.63 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[TIA1]] | -0.62 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[BAZ2B]] | -0.61 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[VEZF1]] | -0.59 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[FGF2]] | -0.58 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[HNRNPK]] | -0.58 | -0.40 / -0.53 | both halves | 5e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[FKRP]] | -0.58 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[DHRS12]] | -0.57 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[SYNPO]] | -0.57 | -0.53 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EBF1]] | B | EBF1 activity lowers THOC3's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 1.35× higher at baseline in the lines without EBF1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4 |
| [[TOP2A]] | B | TOP2A activity lowers THOC3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CUZD1]] | B | CUZD1 activity raises THOC3's level | lines that do not express CUZD1 (9) vs lines expressing it (41) | 1.11× lower at baseline in the lines without CUZD1 | 0.085 | ⚠ within organs, on part of the lines; also absent: FAM24B, C10orf88B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.761). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-0.5, -17.2); signed map (-46.9, 7.0). **Vector** length 89.8, 19.2% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +2.9 | +9.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.8 | +11.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.0 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.4 | +0.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.4 | -13.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.8 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.3 | -4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.2 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -0.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.3 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | THO complex subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:175,917,873-176,034,680 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TEX1, MGC5469 |
| Gene groups (HGNC) | WD repeat domain containing; THO complex |
| Reactome | 5 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA 3'-end processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96J01](https://www.uniprot.org/uniprotkb/Q96J01) (THO complex subunit 3):

> Component of the THO subcomplex of the TREX complex which is thought to couple mRNA transcription, processing and nuclear export, and which specifically associates with spliced mRNA and not with unspliced pre-mRNA. Required for efficient export of polyadenylated RNA and spliced mRNA. The THOC1-THOC2-THOC3 core complex alone is sufficient to bind export factor NXF1-NXT1 and promote ATPase activity of DDX39B. TREX is recruited to spliced mRNAs by a transcription-independent mechanism, binds to …

**Summary**, from NCBI Gene [84321](https://www.ncbi.nlm.nih.gov/gene/84321):

> This gene encodes a component of the nuclear THO transcription elongation complex, which is part of the larger transcription export (TREX) complex that couples messenger RNA processing and export. In humans, the transcription export complex is recruited to the 5'-end of messenger RNAs in a splicing- and cap-dependent manner. Studies of a related complex in mouse suggest that the metazoan transcription export complex is involved in cell differentiation and development. A pseudogene of this gene …

**Accessions** — [HGNC:19072](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19072) · Entrez [84321](https://www.ncbi.nlm.nih.gov/gene/84321) · UniProt [Q96J01](https://www.uniprot.org/uniprotkb/Q96J01) · Ensembl [ENSG00000051596](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000051596)

## Data

Gene col 580: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 580); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 580, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 580]; `tensor/DDL_lfc|DDL_z.npy` [580]; `embed/gene_vectors.npy` [580]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 580 or target_col == 580). Every well: [[THOC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THOC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
