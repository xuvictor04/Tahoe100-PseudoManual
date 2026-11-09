---
symbol: "CTSV"
type: "gene"
col: 5948
ensembl_id: "ENSG00000136943"
name: "cathepsin V"
location: "9q22.33"
module: 1
arm: "-"
pooled_cpm: 10.61
n_lines_expressing: 44
n_dd_up: 25
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# CTSV

*cathepsin V* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.16× (z +30.8, q 0e+00, up in 40 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 0.641× (z -5.9, q 2e-06, down in 23 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNAS]] (+0.61, fdr 3e-05), [[VAMP1]] (+0.60, fdr 1e-05), [[KLHL15]] (+0.56, fdr 3e-05); moves opposite to [[DNAJA3]] (-0.57, fdr 3e-05), [[REXO4]] (-0.56, fdr 5e-05), [[TATDN1]] (-0.55, fdr 4e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[IQCD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5948.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.16×** | +30.8 | 0e+00 | 40/40 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **3.68×** | +17.3 | 0e+00 | 38/41 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.44×** | +16.4 | 0e+00 | 39/41 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.08×** | +14.4 | 2e-44 | 10/16 (KATO III, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.81×** | +13.7 | 9e-41 | 24/28 (NCI-H1573, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +12.4 | 3e-33 | 31/37 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.54×** | +12.4 | 3e-33 | 33/41 (SW480, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.87×** | +11.7 | 8e-30 | 30/41 (J82, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.44×** | +11.4 | 4e-28 | 32/38 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +9.7 | 1e-20 | 29/41 (SW1417, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **2.06×** | +9.2 | 2e-18 | 24/34 (J82, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +8.3 | 4e-15 | 24/42 (A-172, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.93×** | +8.0 | 4e-14 | 15/22 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +7.7 | 8e-13 | 23/41 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +5.9 | 2e-07 | 22/41 (BT-474, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +4.3 | 5e-04 | 19/41 (SW1417, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.37×** | +4.2 | 7e-04 | 8/40 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.001 | 14/41 (HOP62, C32, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +3.9 | 0.003 | 7/40 (SW1417, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.010 | 4/40 (LoVo, CFPAC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.045 | 5/37 (HT-29, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.20× | +2.9 | 0.075 | 6/41 (NCI-H23, RKO, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5948.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.641×** | -5.9 | 2e-06 | 23/40 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.685×** | -5.0 | 1e-04 | 14/41 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.785×** | -4.5 | 0.001 | 17/41 (AN3 CA, MIA PaCa-2, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.822×** | -3.7 | 0.035 | 11/41 (RKO, A498, …) | top dose only |  |
| [[Pentagastrin (drug)]] 0.5 µM |  | 0.796× | -3.0 | 0.28 | 5/40 (HepG2/C3A, HT-29, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5948. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.3 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.07× (z +18.8) | — |
| [[KATO III (line)]] | alt | 24.7 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.01× (z +17.5) | — |
| [[HT-29 (line)]] | alt | 13.9 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.45× (z +16.6) | — |
| [[LoVo (line)]] | wt | 6.11 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.74× (z +12.7) | — |
| [[SW1417 (line)]] | alt | 47.5 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.73× (z +10.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.3) | — |
| [[A-172 (line)]] | wt | 12.3 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +10.7) | [[Homoharringtonine (drug)]] 0.05 µM 0.231× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 23.8 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +13.9) | — |
| [[Hs 766T (line)]] | wt | 6.76 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.18× (z +9.9) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0976× (z -8.9) |
| [[J82 (line)]] | alt | 18.2 | 3 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 5.02× (z +15.4) | — |
| [[NCI-H1573 (line)]] | alt | 8.01 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.64× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[PANC-1 (line)]] | alt | 8.96 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +14.4) | — |
| [[HOP62 (line)]] | alt | 4.81 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +11.9) | — |
| [[A-427 (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.219× (z -9.1) ⚠ cell-cycle shift, explains ~79% of this change |
| [[A549 (line)]] | wt | 5.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.4× (z +15.9) | — |
| [[AsPC-1 (line)]] | alt | 2.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 6.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +11.7) | — |
| [[C-33 A (line)]] | alt | 21.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +11.8) | — |
| [[HCT15 (line)]] | alt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.83× (z +11.5) | — |
| [[LS 180 (line)]] | wt | 9.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.52× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 13.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.31× (z +16.0) | — |
| [[RKO (line)]] | wt | 7.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.77× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 8.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.73× (z +11.0) | — |
| [[A498 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5948), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | +0.61 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[VAMP1]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[KLHL15]] | +0.56 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[ITM2C]] | +0.56 | +0.35 / +0.61 | both halves | 1e-04 |  |
| [[GGH]] | +0.55 | +0.44 / +0.58 | both halves | 3e-05 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[FBLN1]] | +0.52 | +0.49 / +0.43 | both halves | 3e-05 | pathway: Extracellular matrix organization |
| [[PRCP]] | +0.52 | +0.39 / +0.54 | both halves | 5e-05 | pathway: HALLMARK_COMPLEMENT |
| [[BSG]] | +0.52 | +0.41 / +0.45 | both halves | 4e-05 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[PROCA1]] | +0.51 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[GAB1]] | +0.51 | +0.50 / +0.40 | both halves | 4e-05 |  |
| [[IQCD]] | +0.51 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[ITM2B]] | +0.50 | +0.43 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJA3]] | -0.57 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[REXO4]] | -0.56 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[TATDN1]] | -0.55 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[METTL2A]] | -0.53 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[CHMP6]] | -0.52 | -0.32 / -0.62 | both halves | 2e-04 |  |
| [[ACSF3]] | -0.50 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[DPH5]] | -0.50 | -0.29 / -0.48 | both halves | 3e-04 |  |
| [[ADRM1]] | -0.49 | -0.41 / -0.38 | both halves | 6e-05 | pathway: Antigen processing-Cross presentation |
| [[RRS1]] | -0.49 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[ERCC4]] | -0.49 | -0.25 / -0.42 | both halves | 4e-04 |  |
| [[CIAO1]] | -0.49 | -0.29 / -0.45 | both halves | 3e-04 |  |
| [[CAAP1]] | -0.49 | -0.32 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CTSV's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NPTXR]] | B | NPTXR activity raises CTSV's level | lines that do not express NPTXR (11) vs lines expressing it (39) | 1.72× lower at baseline in the lines without NPTXR | 0.042 | ⚠ within organs, on part of the lines; also absent: WNT9A, RAB6B, MAPK8IP2; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IQCD]] | B | CTSV activity raises IQCD's level | lines that do not express CTSV (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without CTSV | 0.057 | ⚠ within organs, on part of the lines; also absent: RASSF7, BMP8B, ZDHHC11B; maybe low, not absent |
| [[EIF4G3]] | C | CTSV's natural level weakens EIF4G3's drug response | CTSV's natural level across 43 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.14; direction not clear | 0.089 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.451). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-42.4, -1.3); signed map (1.5, 15.7). **Vector** length 69.7, 12.5% of its response variance represented; |z| ≥ 3 in 1,001 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +30.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.9 | +11.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +3.0 | +14.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.2 | +2.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.1 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -3.7 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | cathepsin V |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:97,029,677-97,156,556 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CTSU; previously CTSL2 |
| Gene groups (HGNC) | Cathepsins; Elastases; Cysteine endopeptidases |
| Hallmark sets | COAGULATION, UV_RESPONSE_UP, COMPLEMENT |
| Reactome | 18 pathways, smallest: RUNX1 regulates transcription of genes involved in differentiation of keratinocytes; Trafficking and processing of endosomal TLR; Endosomal/Vacuolar pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [O60911](https://www.uniprot.org/uniprotkb/O60911) (Cathepsin L2):

> Cysteine protease. May have an important role in corneal physiology.

**Summary**, from NCBI Gene [1515](https://www.ncbi.nlm.nih.gov/gene/1515):

> The protein encoded by this gene, a member of the peptidase C1 family, is a lysosomal cysteine proteinase that may play an important role in corneal physiology. This gene is expressed in colorectal and breast carcinomas but not in normal colon, mammary gland, or peritumoral tissues, suggesting a possible role for this gene in tumor processes. Alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:2538](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2538) · Entrez [1515](https://www.ncbi.nlm.nih.gov/gene/1515) · UniProt [O60911](https://www.uniprot.org/uniprotkb/O60911) · Ensembl [ENSG00000136943](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136943)

## Data

Gene col 5948: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5948); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5948, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5948]; `tensor/DDL_lfc|DDL_z.npy` [5948]; `embed/gene_vectors.npy` [5948]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5948 or target_col == 5948). Every well: [[CTSV — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTSV.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
