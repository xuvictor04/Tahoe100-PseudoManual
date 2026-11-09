---
symbol: "FOXC1"
type: "gene"
col: 611
ensembl_id: "ENSG00000054598"
name: "forkhead box C1"
location: "6p25.3"
module: 25
arm: "-"
pooled_cpm: 31.64
n_lines_expressing: 46
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# FOXC1

*forkhead box C1* — 6p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.21× (z +19.9, q 0e+00, up in 41 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.612× (z -4.8, q 9e-04, down in 24 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFAP2A]] (+0.58, fdr 1e-05), [[TOPORS]] (+0.57, fdr 3e-05), [[HOXC9]] (+0.57, fdr 2e-04); moves opposite to [[PDHA1]] (-0.59, fdr 1e-04), [[OPA1]] (-0.59, fdr 2e-05), [[API5]] (-0.58, fdr 2e-04).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SLC49A4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 611.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.21×** | +19.9 | 0e+00 | 41/44 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.77×** | +11.9 | 4e-30 | 37/42 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +7.3 | 7e-11 | 31/44 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +5.9 | 4e-07 | 28/43 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.46×** | +5.2 | 2e-05 | 25/44 (A498, AsPC-1, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.62×** | +4.7 | 3e-04 | 25/42 (CFPAC-1, A-172, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.57×** | +4.4 | 9e-04 | 22/41 (A-172, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.55×** | +4.3 | 0.001 | 23/43 (AsPC-1, HOP62, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.65×** | +3.6 | 0.021 | 19/43 (NCI-H2347, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.47×** | +3.5 | 0.030 | 18/44 (COLO 205, HS-578T, …) | rises with dose | composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.39×** | +3.2 | 0.069 | 14/43 (SW480, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.39×** | +3.2 | 0.069 | 13/44 (A-172, CFPAC-1, …) | all doses, flat | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.1 | 0.070 | 2/44 (NCI-H23, NCI-H460) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +3.1 | 0.070 | 16/44 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 611.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.612×** | -4.8 | 9e-04 | 24/44 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Folic acid (drug)]] 5 µM |  | **0.729×** | -4.4 | 0.003 | 28/44 (NCI-H661, NCI-H2347, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.469×** | -3.9 | 0.021 | 20/45 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.679×** | -3.8 | 0.021 | 20/43 (SHP-77, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.686×** | -3.7 | 0.026 | 22/44 (SHP-77, NCI-H1792, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 611. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 175 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -13.9) |
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 5 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.4× (z +18.2) | [[EX229 (drug)]] 0.05 µM 0.127× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 115 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -15.7) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.159× (z -14.0) |
| [[HOP62 (line)]] | alt | 10.5 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +16.9) | — |
| [[AN3 CA (line)]] | alt | 274 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -16.9) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.313× (z -9.8) |
| [[A-172 (line)]] | wt | 16.9 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.36× (z +17.2) | — |
| [[A498 (line)]] | wt | 32.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +12.8) | [[Selinexor (drug)]] 5 µM 0.417× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 58.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +12.2) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +11.9) | — |
| [[HT-29 (line)]] | alt | 23.5 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.78× (z +15.9) | — |
| [[SW480 (line)]] | alt | 21.9 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.13× (z +15.6) | — |
| [[CFPAC-1 (line)]] | alt | 52.1 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 7.59× (z +12.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 55.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +8.9) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[HepG2_C3A (line)]] | wt | 20.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.63× (z +13.5) | — |
| [[HS-578T (line)]] | alt | 25.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +10.9) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 27.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 18.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +14.6) | — |
| [[SK-MEL-2 (line)]] | alt | 22.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +10.6) | [[TAK-901 (drug)]] 5 µM 0.0455× (z -8.7) |
| [[A549 (line)]] | wt | 16.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.99× (z +16.4) | — |
| [[C-33 A (line)]] | alt | 19.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.68× (z +9.6) | — |
| [[C32 (line)]] | wt | 39.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +8.6) | — |
| [[H4 (line)]] | wt | 16.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.99× (z +11.1) | — |
| [[HCT15 (line)]] | alt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.83× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 30.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 46.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.46× (z +9.5) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[J82 (line)]] | alt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +17.8) | — |
| [[LoVo (line)]] | wt | 37.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.35× (z +13.9) | — |
| [[LS 180 (line)]] | wt | 9.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.83× (z +13.3) | — |
| [[NCI-H2030 (line)]] | alt | 12.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.02× (z +11.2) | — |
| [[NCI-H661 (line)]] | alt | 71.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0599× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[Panc 03.27 (line)]] | alt | 61.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +11.1) | — |
| [[PANC-1 (line)]] | alt | 15.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.70× (z +20.8) | — |
| [[SNU-423 (line)]] | alt | 8.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.81× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +8.6) | — |
| [[SW48 (line)]] | wt | 22.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +9.1) | — |
| [[A-427 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.03 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.31 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 611), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFAP2A]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 | pathway: Gastrulation; STRING 652 |
| [[TOPORS]] | +0.57 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[HOXC9]] | +0.57 | +0.30 / +0.50 | both halves | 2e-04 |  |
| [[MPLKIP]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[SLC49A4]] | +0.56 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[BAZ1A]] | +0.56 | +0.57 / +0.38 | both halves | 6e-05 |  |
| [[TFAP2A-AS1]] | +0.56 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[ZBED5]] | +0.56 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[MSX1]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 | pathway: Gastrulation |
| [[ZIC2]] | +0.55 | +0.35 / +0.53 | both halves | 1e-04 | pathway: Gastrulation |
| [[ARID4B]] | +0.55 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[TFAP2C]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDHA1]] | -0.59 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[OPA1]] | -0.59 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[API5]] | -0.58 | -0.30 / -0.65 | both halves | 2e-04 |  |
| [[USP14]] | -0.57 | -0.38 / -0.60 | both halves | 6e-05 |  |
| [[RPGRIP1L]] | -0.56 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ANXA6]] | -0.56 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[AGO1]] | -0.56 | -0.36 / -0.57 | both halves | 9e-05 |  |
| [[RSU1]] | -0.55 | -0.37 / -0.43 | both halves | 9e-05 |  |
| [[EFTUD2]] | -0.54 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[NOL10]] | -0.53 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[VAMP7]] | -0.53 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[CS]] | -0.52 | -0.30 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises FOXC1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers FOXC1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PELI2]] | B | PELI2 activity raises FOXC1's level | lines that do not express PELI2 (16) vs lines expressing it (34) | 1.33× lower at baseline in the lines without PELI2 | 0.074 | ⚠ within organs, on part of the lines; also absent: LINC02284, DNAJC12, ADAM28 |
| [[FZD7]] | C | FZD7 activity lowers FOXC1's level | lines that do not express FZD7 (3) vs lines expressing it (47) | 2.63× higher at baseline in the lines without FZD7 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: SPDL1, HOMER3, RBMS2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC49A4]] | C | FOXC1 activity lowers SLC49A4's level | lines that do not express FOXC1 (4) vs lines expressing it (46) | 1.45× higher at baseline in the lines without FOXC1 | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.393). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (19.6, -4.4); signed map (14.2, -7.0). **Vector** length 102, 27.0% of its response variance represented; |z| ≥ 3 in 784 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.9 | +19.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.5 | +11.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +5.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +5.2 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +2.4 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.3 | +2.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.2 | +1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +1.0 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -5.5 | -4.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.8 | -2.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.1 | -3.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.5 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -2.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.5 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box C1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.3 — chr6:1,609,915-1,613,897 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FREAC3, ARA, IGDA, IHG1; previously FKHL7, IRID1 |
| Gene groups (HGNC) | Forkhead boxes |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: Formation of intermediate mesoderm; Formation of the ureteric bud; Kidney development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12948](https://www.uniprot.org/uniprotkb/Q12948) (Forkhead box protein C1):

> DNA-binding transcriptional factor that plays a role in a broad range of cellular and developmental processes such as eye, bones, cardiovascular, kidney and skin development. Acts either as a transcriptional activator or repressor. Binds to the consensus binding site 5'-[G/C][A/T]AAA[T/C]AA[A/C]-3' in promoter of target genes. Upon DNA-binding, promotes DNA bending. Acts as a transcriptional coactivator. Stimulates Indian hedgehog (Ihh)-induced target gene expression mediated by the …

**Summary**, from NCBI Gene [2296](https://www.ncbi.nlm.nih.gov/gene/2296):

> This gene belongs to the forkhead family of transcription factors which is characterized by a distinct DNA-binding forkhead domain. The specific function of this gene has not yet been determined; however, it has been shown to play a role in the regulation of embryonic and ocular development. Mutations in this gene cause various glaucoma phenotypes including primary congenital glaucoma, autosomal dominant iridogoniodysgenesis anomaly, and Axenfeld-Rieger anomaly. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3800](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3800) · Entrez [2296](https://www.ncbi.nlm.nih.gov/gene/2296) · UniProt [Q12948](https://www.uniprot.org/uniprotkb/Q12948) · Ensembl [ENSG00000054598](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000054598)

## Data

Gene col 611: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 611); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 611, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 611]; `tensor/DDL_lfc|DDL_z.npy` [611]; `embed/gene_vectors.npy` [611]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 611 or target_col == 611). Every well: [[FOXC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
