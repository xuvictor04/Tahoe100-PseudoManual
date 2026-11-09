---
symbol: "DNAAF10"
type: "gene"
col: 14370
ensembl_id: "ENSG00000243667"
name: "dynein axonemal assembly factor 10"
location: "2p14"
module: 83
arm: "+"
pooled_cpm: 14.11
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# DNAAF10

*dynein axonemal assembly factor 10* — 2p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.23× (z +16.4, q 0e+00, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.582× (z -7.8, q 3e-12, down in 28 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.652× (z -6.2, q 1e-07, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSTF3]] (+0.76, fdr 1e-05), [[ANXA2R-OT1]] (+0.73, fdr 1e-05), [[MSANTD2]] (+0.69, fdr 3e-05); moves opposite to [[USP2]] (-0.66, fdr 3e-05), [[LIFR]] (-0.63, fdr 3e-05), [[STARD5]] (-0.61, fdr 2e-04).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[LENG8-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14370.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +16.4 | 0e+00 | 41/46 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +9.5 | 6e-19 | 32/46 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +7.9 | 4e-13 | 34/48 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +7.3 | 3e-11 | 26/48 (SW1417, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +6.1 | 1e-07 | 20/37 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +5.8 | 8e-07 | 22/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +5.4 | 4e-06 | 12/24 (A-172, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +5.1 | 3e-05 | 16/31 (SHP-77, HT-29, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.40×** | +4.6 | 2e-04 | 17/41 (CFPAC-1, KATO III, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +4.4 | 6e-04 | 17/48 (NCI-H1792, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.21×** | +3.9 | 0.004 | 20/48 (NCI-H1573, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.007 | 10/48 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.075 | 13/47 (C-33 A, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 1.23× | +3.0 | 0.11 | 10/46 (NCI-H23, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14370.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.582×** | -7.8 | 3e-12 | 28/45 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.587×** | -7.4 | 4e-11 | 25/44 (HCT15, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.652×** | -6.2 | 1e-07 | 23/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.736×** | -4.4 | 0.001 | 14/47 (C-33 A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.737×** | -4.4 | 0.001 | 20/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.574×** | -4.2 | 0.003 | 13/44 (PANC-1, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.732×** | -4.1 | 0.003 | 13/48 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.601×** | -3.8 | 0.009 | 12/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.847× | -3.4 | 0.044 | 8/48 (SHP-77, AN3 CA, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.798×** | -3.1 | 0.096 | 9/47 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift |
| [[Tomivosertib (drug)]] 5 µM |  | 0.665× | -3.1 | 0.11 | 5/48 (SNU-1, CHP-212, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14370. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 24.3 | 1 | 7 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -20.3) |
| [[SW480 (line)]] | alt | 20.4 | 3 | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +12.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.364× (z -9.8) |
| [[A-172 (line)]] | wt | 15.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.28× (z +9.0) ⚠ toxic; transcription drop | [[5-Azacytidine (drug)]] 0.5 µM 0.177× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.116× (z -13.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 10.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +9.2) | [[Pemetrexed (drug)]] 5 µM 0.0405× (z -15.0) |
| [[SW1417 (line)]] | alt | 13.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.06× (z +11.8) | — |
| [[AsPC-1 (line)]] | alt | 4.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.35× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.233× (z -8.5) ⚠ toxic |
| [[C32 (line)]] | wt | 9.40 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0827× (z -10.7) |
| [[H4 (line)]] | wt | 18.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.146× (z -8.5) |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0873× (z -10.8) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -12.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 8.92 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.0679× (z -9.9) |
| [[HOP62 (line)]] | alt | 16.3 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 8.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +8.5) | — |
| [[J82 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.104× (z -9.7) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0779× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 8.10 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0782× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 24.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 15.2 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.164× (z -9.0) |
| [[SNU-423 (line)]] | alt | 9.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 6.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.12× (z +9.6) | — |
| [[A-427 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14370), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSTF3]] | +0.76 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[ANXA2R-OT1]] | +0.73 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[MSANTD2]] | +0.69 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[DUS2]] | +0.68 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[C10orf88]] | +0.68 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[CENPL]] | +0.67 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[WDR33]] | +0.66 | +0.63 / +0.38 | both halves | 7e-05 | same gene group |
| [[ALG8]] | +0.66 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ACAD9]] | +0.65 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[MYLK-AS1]] | +0.64 | +0.68 / +0.34 | both halves | 1e-04 |  |
| [[PIGW]] | +0.63 | +0.54 / +0.37 | both halves | 8e-05 |  |
| [[YARS2]] | +0.63 | +0.52 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP2]] | -0.66 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[LIFR]] | -0.63 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[STARD5]] | -0.61 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[SMARCD3]] | -0.60 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[SNN]] | -0.60 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[MAST3]] | -0.59 | -0.54 / -0.20 | both halves | 7e-04 |  |
| [[ALAD]] | -0.59 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[ARRB2]] | -0.58 | -0.50 / -0.24 | both halves | 4e-04 |  |
| [[FOXO6]] | -0.58 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[RALGAPA2]] | -0.58 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[CYRIA]] | -0.58 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[DOK4]] | -0.58 | -0.57 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DNAAF10's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NR3C2]] | B | NR3C2 activity lowers DNAAF10's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.39× higher at baseline in the lines without NR3C2 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LENG8-AS1]] | C | DNAAF10's natural level strengthens LENG8-AS1's drug response | DNAAF10's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.00; direction clear | 0.073 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others |
| [[METTL4]] | C | DNAAF10's natural level strengthens METTL4's drug response | DNAAF10's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.15; direction not clear | 0.085 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.744). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-2.5, 20.3); signed map (17.5, -19.7). **Vector** length 72.8, 12.9% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +16.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +9.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | +1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | +0.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal assembly factor 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p14 — chr2:68,122,936-68,157,549 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31741, Monad; previously WDR92 |
| Gene groups (HGNC) | WD repeat domain containing; Axonemal dynein assembly factors; PAQosome accessory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MX6](https://www.uniprot.org/uniprotkb/Q96MX6) (Dynein axonemal assembly factor 10):

> Key assembly factor specifically required for the stability of axonemal dynein heavy chains in cytoplasm.

**Summary**, from NCBI Gene [116143](https://www.ncbi.nlm.nih.gov/gene/116143):

> This gene encodes a protein with two WD40 repeat domains thought to be involved in an apoptosis via activation of caspase-3. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:25176](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25176) · Entrez [116143](https://www.ncbi.nlm.nih.gov/gene/116143) · UniProt [Q96MX6](https://www.uniprot.org/uniprotkb/Q96MX6) · Ensembl [ENSG00000243667](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243667)

## Data

Gene col 14370: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14370); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14370, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14370]; `tensor/DDL_lfc|DDL_z.npy` [14370]; `embed/gene_vectors.npy` [14370]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14370 or target_col == 14370). Every well: [[DNAAF10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAAF10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
