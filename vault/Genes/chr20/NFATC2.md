---
symbol: "NFATC2"
type: "gene"
col: 2069
ensembl_id: "ENSG00000101096"
name: "nuclear factor of activated T cells 2"
location: "20q13.2"
module: 14
arm: "+"
pooled_cpm: 49.37
n_lines_expressing: 39
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 22
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# NFATC2

*nuclear factor of activated T cells 2* — 20q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.48× (z +16.1, q 0e+00, up in 29 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 0.722× (z -4.2, q 0.013, down in 20 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 3 lines (C32 0.131×, LOX-IMVI 0.172×, RPMI-7951 0.163×); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.177×, HT-29 0.158×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (CFPAC-1 0.170×, KATO III 0.271×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (RPMI-7951 0.132×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (SW48 0.0725×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAK]] (+0.64, fdr 7e-06), [[OSR2]] (+0.57, fdr 1e-05), [[DUSP10]] (+0.55, fdr 1e-05); moves opposite to [[C8orf76]] (-0.53, fdr 2e-05), [[STARD3]] (-0.52, fdr 2e-05), [[GPR89A]] (-0.50, fdr 5e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SLC43A3]] → it (grade B ⚠); 22 go from it, the strongest it → [[LGALS3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2069.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.48×** | +16.1 | 0e+00 | 29/37 (BT-474, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.99×** | +13.5 | 4e-39 | 35/37 (A-172, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.83×** | +10.6 | 7e-24 | 25/37 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.17×** | +7.9 | 5e-13 | 24/37 (A-172, KATO III, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **2.08×** | +7.5 | 9e-12 | 24/37 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.11×** | +7.4 | 1e-11 | 26/37 (BT-474, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +6.2 | 5e-08 | 23/34 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.84×** | +6.1 | 9e-08 | 23/37 (SNU-423, BT-474, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +5.8 | 3e-07 | 19/37 (SW1417, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +5.8 | 3e-07 | 26/37 (A-172, SW1417, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +5.8 | 4e-07 | 18/35 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +3.7 | 0.009 | 17/37 (SW1417, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Gefitinib (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.029 | 15/37 (NCI-H460, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2069.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 3 lines (C32 0.131×, LOX-IMVI 0.172×, RPMI-7951 0.163×); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.177×, HT-29 0.158×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (CFPAC-1 0.170×, KATO III 0.271×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (RPMI-7951 0.132×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (SW48 0.0725×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.722×** | -4.2 | 0.013 | 20/37 (NCI-H1792, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[vincristine (drug)]] 0.5 µM |  | 0.625× | -3.3 | 0.26 | 15/36 (C32, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | 0.779× | -3.1 | 0.34 | 17/37 (HS-578T, SNU-423, …) | inconsistent across doses |  |
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.736× | -3.0 | 0.38 | 11/37 (HOP62, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2069. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 46.3 | 5 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0912× (z -17.2) ⚠ toxic; cell-cycle shift, explains ~22% of this change |
| [[SW1417 (line)]] | alt | 32.5 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +16.8) | — |
| [[A-172 (line)]] | wt | 15.5 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +16.8) | — |
| [[NCI-H2347 (line)]] | alt | 56.5 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 112 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -12.1) |
| [[HT-29 (line)]] | alt | 38.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +16.8) | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 118 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 21.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.8× (z +20.3) | — |
| [[LoVo (line)]] | wt | 14.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +12.7) | — |
| [[NCI-H1573 (line)]] | alt | 18.9 | 3 (2 ⚠) | 0 | [[Peretinoin (drug)]] 5 µM 7.48× (z +11.6) | — |
| [[PANC-1 (line)]] | alt | 14.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.77× (z +13.4) | — |
| [[RPMI-7951 (line)]] | alt | 228 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.132× (z -10.6) |
| [[SW480 (line)]] | alt | 57.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.320× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 54.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +17.5) | — |
| [[HepG2_C3A (line)]] | wt | 130 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.11× (z +16.2) | — |
| [[HS-578T (line)]] | alt | 92.0 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 5 µM 0.242× (z -8.7) |
| [[J82 (line)]] | alt | 67.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +12.3) | — |
| [[Panc 03.27 (line)]] | alt | 39.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.88× (z +17.7) | — |
| [[A549 (line)]] | wt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.43× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 104 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -9.3) |
| [[LS 180 (line)]] | wt | 12.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.75× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 7.44× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.167× (z -9.4) ⚠ transcription drop |
| [[SW48 (line)]] | wt | 29.9 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0725× (z -10.2) |
| [[A-427 (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.34 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.54 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.87 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 299 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.94 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.43 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.31 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.44 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.72 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2069), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAK]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[OSR2]] | +0.57 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[DUSP10]] | +0.55 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[KLF4]] | +0.55 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[CFAP210]] | +0.54 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[RASSF5]] | +0.53 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[SFR1]] | +0.53 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[ATF3]] | +0.53 | +0.54 / +0.54 | both halves | 1e-05 | STRING 434 |
| [[TAGLN2]] | +0.52 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[APOBEC3A]] | +0.52 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[RND1]] | +0.52 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[CDKN2B]] | +0.52 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C8orf76]] | -0.53 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[STARD3]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[GPR89A]] | -0.50 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[UBOX5]] | -0.50 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[HERC2P3]] | -0.49 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[SLC30A6]] | -0.49 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[GTF3C2]] | -0.49 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ADPGK]] | -0.48 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[PARGP1]] | -0.48 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[DCUN1D5]] | -0.47 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[TNPO3]] | -0.47 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[STX16-NPEPL1]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC43A3]] | B | SLC43A3 activity raises NFATC2's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 2.84× lower at baseline in the lines without SLC43A3 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261 |
| [[GATA6]] | B | GATA6 activity raises NFATC2's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 2.41× lower at baseline in the lines without GATA6 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[MARCKS]] | B | MARCKS activity raises NFATC2's level | lines that do not express MARCKS (10) vs lines expressing it (40) | 3.42× lower at baseline in the lines without MARCKS | 0.057 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |
| [[RASSF5]] | B | RASSF5 activity raises NFATC2's level | lines that do not express RASSF5 (5) vs lines expressing it (45) | 3.61× lower at baseline in the lines without RASSF5 | 0.069 | ⚠ within organs, on part of the lines; also absent: NAT1, WWC3, ZMIZ1; maybe low, not absent |
| [[LGALS3]] | B | LGALS3 activity raises NFATC2's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 2.43× lower at baseline in the lines without LGALS3 | 0.0997 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 22, C 0. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALS3]] | B | NFATC2 activity raises LGALS3's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 2.60× lower at baseline in the lines without NFATC2 | 0.015 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[IQCB1]] | B | NFATC2 activity lowers IQCB1's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 1.34× higher at baseline in the lines without NFATC2 | 0.030 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[LMNA]] | B | NFATC2 activity raises LMNA's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 1.60× lower at baseline in the lines without NFATC2 | 0.030 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[TSPAN15]] | B | NFATC2 activity raises TSPAN15's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 2.01× lower at baseline in the lines without NFATC2 | 0.038 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[LYST]] | B | NFATC2 activity raises LYST's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 1.58× lower at baseline in the lines without NFATC2 | 0.040 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[KLF4]] | B | NFATC2 activity raises KLF4's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without NFATC2 | 0.046 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[ZFHX2]] | B | NFATC2 activity lowers ZFHX2's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 1.67× higher at baseline in the lines without NFATC2 | 0.048 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[SMAD7]] | B | NFATC2 activity raises SMAD7's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 1.73× lower at baseline in the lines without NFATC2 | 0.048 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| cells under [[Niclosamide (olamine) (drug)]] 5 µM | B | NFATC2 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express NFATC2 (11) vs lines expressing it (37) | the lines without NFATC2: 0.57× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[FNDC3B]] | B | NFATC2 activity raises FNDC3B's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 1.68× lower at baseline in the lines without NFATC2 | 0.058 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[ABTB2]] | B | NFATC2 activity raises ABTB2's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 2.31× lower at baseline in the lines without NFATC2 | 0.065 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[GEM]] | B | NFATC2 activity strengthens GEM's drug response | lines that do not express NFATC2 (8) vs lines expressing it (32) | the lines without NFATC2 respond 0.60× as strongly (z diff +2.15); strongest at Homoharringtonine 0.5 µM: 1.94x vs 4.85x (z diff +3.7) | 0.066 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.6, 3.9); signed map (4.4, 21.4). **Vector** length 107, 26.2% of its response variance represented; |z| ≥ 3 in 1,125 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +13.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +16.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.4 | +5.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +0.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +1.8 | +2.9 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.1 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.2 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -1.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | +1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -2.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | nuclear factor of activated T cells 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.2 — chr20:51,386,957-51,562,831 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NF-ATP, NFATp, NFAT1 |
| Gene groups (HGNC) | Nuclear factors of activated T-cells; MicroRNA protein coding host genes; IPT domain containing |
| Reactome | 14 pathways, smallest: RUNX1 and FOXP3 control the development of regulatory T lymphocytes (Tregs); Calcineurin activates NFAT; CLEC7A (Dectin-1) induces NFAT activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13469](https://www.uniprot.org/uniprotkb/Q13469) (Nuclear factor of activated T-cells, cytoplasmic 2):

> Plays a role in the inducible expression of cytokine genes in T-cells, especially in the induction of the IL-2, IL-3, IL-4, TNF or GM-CSF. Promotes invasive migration through the activation of GPC6 expression and WNT5A signaling pathway. Is involved in the negative regulation of chondrogenesis. Recruited by AKAP5 to ORAI1 pore-forming subunit of CRAC channels in Ca(2+) signaling microdomains where store-operated Ca(2+) influx is coupled to calmodulin and calcineurin signaling and activation of …

**Summary**, from NCBI Gene [4773](https://www.ncbi.nlm.nih.gov/gene/4773):

> This gene is a member of the nuclear factor of activated T cells (NFAT) family. The product of this gene is a DNA-binding protein with a REL-homology region (RHR) and an NFAT-homology region (NHR). This protein is present in the cytosol and only translocates to the nucleus upon T cell receptor (TCR) stimulation, where it becomes a member of the nuclear factors of activated T cells transcription complex. This complex plays a central role in inducing gene transcription during the immune response. …

**Accessions** — [HGNC:7776](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7776) · Entrez [4773](https://www.ncbi.nlm.nih.gov/gene/4773) · UniProt [Q13469](https://www.uniprot.org/uniprotkb/Q13469) · Ensembl [ENSG00000101096](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101096)

## Data

Gene col 2069: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2069); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2069, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2069]; `tensor/DDL_lfc|DDL_z.npy` [2069]; `embed/gene_vectors.npy` [2069]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2069 or target_col == 2069). Every well: [[NFATC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFATC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
