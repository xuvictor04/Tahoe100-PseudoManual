---
symbol: "ADAT1"
type: "gene"
col: 787
ensembl_id: "ENSG00000065457"
name: "adenosine deaminase tRNA specific 1"
location: "16q23.1"
module: 5
arm: "+"
pooled_cpm: 13.61
n_lines_expressing: 49
n_dd_up: 26
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ADAT1

*adenosine deaminase tRNA specific 1* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.60× (z +18.6, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.658× (z -5.8, q 3e-06, down in 22 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPKAP1]] (+0.74, fdr 7e-06), [[CPSF3]] (+0.73, fdr 7e-06), [[DARS2]] (+0.71, fdr 7e-06); moves opposite to [[CAMLG]] (-0.68, fdr 8e-06), [[SIRT2]] (-0.66, fdr 1e-05), [[PLEKHH3]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 787.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.60×** | +18.6 | 0e+00 | 43/45 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +11.7 | 4e-29 | 33/45 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.34×** | +11.2 | 5e-27 | 20/24 (KATO III, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.22×** | +10.9 | 1e-25 | 31/37 (A-172, A498, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **2.17×** | +10.6 | 2e-24 | 38/46 (Hs 766T, A498, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.14×** | +10.1 | 8e-22 | 32/45 (SW480, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.13×** | +10.0 | 1e-21 | 38/46 (SW480, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.96×** | +9.3 | 1e-18 | 38/46 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.79×** | +8.0 | 7e-14 | 32/46 (A498, Hs 766T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.80×** | +7.5 | 4e-12 | 24/32 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.9 | 2e-10 | 31/47 (HOP62, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +5.9 | 2e-07 | 24/45 (RPMI-7951, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~60% of this change | **1.49×** | +5.3 | 6e-06 | 22/38 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.46×** | +5.2 | 8e-06 | 18/46 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.43×** | +4.9 | 3e-05 | 14/46 (SW480, HOP62, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +4.5 | 3e-04 | 19/45 (C-33 A, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +4.2 | 7e-04 | 13/47 (PANC-1, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +4.2 | 8e-04 | 15/45 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.33×** | +3.9 | 0.003 | 11/46 (KATO III, RKO, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.006 | 15/46 (NCI-H23, SNU-423, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.015 | 12/40 (NCI-H23, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +3.2 | 0.033 | 10/47 (HOP62, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.037 | 7/45 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 787.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.658×** | -5.8 | 3e-06 | 22/46 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.659×** | -5.7 | 3e-06 | 22/46 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.665×** | -5.6 | 4e-06 | 25/46 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.671×** | -5.5 | 6e-06 | 25/45 (KATO III, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.493×** | -5.1 | 4e-05 | 23/41 (A498, Hs 766T, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.761×** | -3.8 | 0.016 | 9/46 (NCI-H2030, KATO III, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.69 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 787. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.6 | 3 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +12.6) | [[Digitoxin (drug)]] 5 µM 0.304× (z -10.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 16.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[HepG2_C3A (line)]] | wt | 13.7 | 0 | 2 | — | [[Oxaprozin (drug)]] 0.5 µM 0.114× (z -9.5) |
| [[HOP62 (line)]] | alt | 10.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 13.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.313× (z -9.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 20.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -10.6) |
| [[A498 (line)]] | wt | 22.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 1 | — | [[Verapamil (drug)]] 0.05 µM 0.0298× (z -16.5) |
| [[CFPAC-1 (line)]] | alt | 5.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 8.53 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.5 µM 0.0726× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 8.96 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -8.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.260× (z -8.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.120× (z -12.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 9.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 16.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.205× (z -10.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 8.12 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -8.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 787), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAP1]] | +0.74 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[CPSF3]] | +0.73 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[DARS2]] | +0.71 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[PIGW]] | +0.68 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[PSME3]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[FGD5-AS1]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[POLDIP2]] | +0.67 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[ERH]] | +0.67 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[CYREN]] | +0.66 | +0.79 / +0.43 | both halves | 3e-05 |  |
| [[TASOR]] | +0.65 | +0.75 / +0.49 | both halves | 2e-05 |  |
| [[ALG8]] | +0.64 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[RNASEH1]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMLG]] | -0.68 | -0.66 / -0.57 | both halves | 8e-06 |  |
| [[SIRT2]] | -0.66 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.65 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[RPL18]] ⚠ | -0.65 | -0.50 / -0.59 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[KBTBD3]] | -0.64 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[RBIS]] | -0.64 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[TOMM7]] | -0.64 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[RPL35A]] | -0.63 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[ATP5MC2]] | -0.63 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[RPL37A]] ⚠ | -0.63 | -0.45 / -0.61 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS27A]] ⚠ | -0.63 | -0.45 / -0.62 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36]] | -0.63 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[PPP1R12B]] | -0.63 | -0.66 / -0.44 | both halves | 3e-05 |  |
| [[BLVRB]] | -0.62 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[VPS37D]] | -0.62 | -0.63 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ADAT1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.595). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.8, -32.7); signed map (-6.4, -40.1). **Vector** length 76.4, 14.8% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +6.2 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +6.2 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +5.4 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +18.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +4.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -0.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -5.6 |
|  | [[NG25 (drug)]] 5 µM |  | -2.9 | -5.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -1.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | adenosine deaminase tRNA specific 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:75,596,868-75,623,300 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Adenosine deaminases acting on RNA |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUB4](https://www.uniprot.org/uniprotkb/Q9BUB4) (tRNA-specific adenosine deaminase 1):

> Specifically deaminates adenosine-37 to inosine in tRNA-Ala.

**Summary**, from NCBI Gene [23536](https://www.ncbi.nlm.nih.gov/gene/23536):

> This gene is a member of the ADAR (adenosine deaminase acting on RNA) family. Using site-specific adenosine modification, proteins encoded by these genes participate in the pre-mRNA editing of nuclear transcripts. The protein encoded by this gene, tRNA-specific adenosine deaminase 1, is responsible for the deamination of adenosine 37 to inosine in eukaryotic tRNA. Alternatively spliced transcript variants have been described. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:228](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:228) · Entrez [23536](https://www.ncbi.nlm.nih.gov/gene/23536) · UniProt [Q9BUB4](https://www.uniprot.org/uniprotkb/Q9BUB4) · Ensembl [ENSG00000065457](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065457)

## Data

Gene col 787: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 787); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 787, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 787]; `tensor/DDL_lfc|DDL_z.npy` [787]; `embed/gene_vectors.npy` [787]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 787 or target_col == 787). Every well: [[ADAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
