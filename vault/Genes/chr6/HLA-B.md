---
symbol: "HLA-B"
type: "gene"
col: 13981
ensembl_id: "ENSG00000234745"
name: "major histocompatibility complex, class I, B"
location: "6p21.33"
module: 70
arm: "+"
pooled_cpm: 417.31
n_lines_expressing: 41
n_dd_up: 8
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 22
direction_downstream: 12
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# HLA-B

*major histocompatibility complex, class I, B* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.01× (z +6.5, q 5e-08, up in 30 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +6.4, q 5e-08, up in 33 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-427 5.16×, J82 3.13×, SW 900 3.02×, HOP62 3.49×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (HOP62 2.57×, NCI-H2030 2.51×, AsPC-1 3.10×, PANC-1 2.64×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 5.15×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.524× (z -6.0, q 1e-06, down in 37 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B2M]] (+0.86, fdr 7e-06), [[HLA-A]] (+0.86, fdr 7e-06), [[HLA-F]] (+0.83, fdr 7e-06); moves opposite to [[CCT2]] (-0.61, fdr 1e-05), [[PRKDC]] (-0.58, fdr 1e-05), [[PGAM5]] (-0.58, fdr 1e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[C15orf48]] → it (grade B ⚠); 12 go from it, the strongest it → [[HLA-E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13981.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-427 5.16×, J82 3.13×, SW 900 3.02×, HOP62 3.49×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (HOP62 2.57×, NCI-H2030 2.51×, AsPC-1 3.10×, PANC-1 2.64×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 5.15×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.01×** | +6.5 | 5e-08 | 30/40 (A-427, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +6.4 | 5e-08 | 33/40 (HOP62, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +4.6 | 7e-04 | 24/36 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.63×** | +4.5 | 8e-04 | 33/39 (NCI-H460, J82, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.61×** | +4.4 | 0.001 | 33/39 (KATO III, CFPAC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.8 | 0.013 | 31/38 (NCI-H2030, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.48×** | +3.5 | 0.041 | 24/39 (NCI-H460, COLO 205, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.050 | 24/39 (HOP62, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13981.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.524×** | -6.0 | 1e-06 | 37/39 (MIA PaCa-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.561×** | -5.4 | 2e-05 | 34/39 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.601×** | -4.7 | 4e-04 | 34/39 (COLO 205, MIA PaCa-2, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.598×** | -4.6 | 7e-04 | 32/40 (hTERT-HPNE, SW 1088, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.718×** | -4.3 | 0.002 | 26/40 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.632×** | -4.2 | 0.002 | 36/39 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.457×** | -3.7 | 0.016 | 30/40 (MIA PaCa-2, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.674×** | -3.7 | 0.018 | 30/39 (MIA PaCa-2, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.477×** | -3.5 | 0.028 | 27/39 (MIA PaCa-2, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.693×** | -3.4 | 0.038 | 30/39 (NCI-H1573, BT-474, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.695×** | -3.4 | 0.039 | 21/40 (BT-474, MIA PaCa-2, …) | rises with dose |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.680×** | -3.3 | 0.046 | 35/39 (SK-MEL-2, SW 900, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.711×** | -3.2 | 0.068 | 24/39 (A549, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.716×** | -3.1 | 0.079 | 21/39 (MIA PaCa-2, COLO 205, …) | top dose only |  |
| [[Folic acid (drug)]] 5 µM |  | **0.792×** | -3.1 | 0.085 | 27/39 (CFPAC-1, hTERT-HPNE, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13981. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 535 | 0 | 4 | — | [[Tofacitinib (drug)]] 5 µM 0.259× (z -13.3) |
| [[BT-474 (line)]] | alt | 246 | 0 | 3 | — | [[TAK-901 (drug)]] 0.05 µM 0.132× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 114 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 787 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.296× (z -10.1) |
| [[HOP62 (line)]] | alt | 233 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +10.1) | — |
| [[J82 (line)]] | alt | 1,993 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 119 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.16× (z +12.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 141 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.15× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HCT15 (line)]] | alt | 213 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 401 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 360 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 311 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.07× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H596 (line)]] | alt | 327 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.171× (z -8.5) |
| [[PANC-1 (line)]] | alt | 218 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 268 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.409× (z -10.0) |
| [[SW 900 (line)]] | alt | 760 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 741 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 674 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 186 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 112 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 613 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1,013 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 74.6 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 560 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 52.5 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 120 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 476 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 541 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 60.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1,202 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 345 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 535 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 99.8 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 66.1 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 353 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 390 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.0 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 745 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 102 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1,008 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 180 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1,398 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1,665 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 312 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 58.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13981), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B2M]] | +0.86 | +0.82 / +0.87 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 999 |
| [[HLA-A]] | +0.86 | +0.84 / +0.84 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 999 |
| [[HLA-F]] | +0.83 | +0.78 / +0.85 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 982 |
| [[HLA-E]] | +0.83 | +0.75 / +0.82 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 994 |
| [[ISG15]] | +0.79 | +0.75 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[PSME2]] | +0.78 | +0.62 / +0.80 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[IFI27]] | +0.78 | +0.68 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[TRIM5]] | +0.77 | +0.74 / +0.74 | both halves | 7e-06 | pathway: Interferon Signaling |
| [[PSMB9]] | +0.76 | +0.68 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 798 |
| [[IRF7]] | +0.75 | +0.66 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 400 |
| [[PLEKHA4]] | +0.75 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[IFI6]] | +0.74 | +0.71 / +0.79 | both halves | 7e-06 | pathway: Interferon Signaling |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT2]] | -0.61 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.58 | -0.52 / -0.56 | both halves | 1e-05 | pathway: E3 ubiquitin ligases ubiquitinate target proteins |
| [[PGAM5]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[IPO8]] | -0.57 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[OPA1]] | -0.57 | -0.44 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 19, C 3. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C15orf48]] | B | C15orf48 activity raises HLA-B's level | lines that do not express C15orf48 (25) vs lines expressing it (25) | 3.05× lower at baseline in the lines without C15orf48 | 7e-04 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG |
| [[GBP4]] | B | GBP4 activity raises HLA-B's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 3.88× lower at baseline in the lines without GBP4 | 0.003 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[C1R]] | B | C1R activity raises HLA-B's level | lines that do not express C1R (20) vs lines expressing it (30) | 3.22× lower at baseline in the lines without C1R | 0.007 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, LOX, RRAD |
| [[NKX3-1]] | B | NKX3-1 activity raises HLA-B's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 3.29× lower at baseline in the lines without NKX3-1 | 0.016 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[HCP5]] | B | HCP5 activity raises HLA-B's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 2.12× lower at baseline in the lines without HCP5 | 0.021 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[GBP4]] | B | GBP4 activity strengthens HLA-B's drug response | lines that do not express GBP4 (12) vs lines expressing it (28) | the lines without GBP4 respond 0.87× as strongly (z diff +0.11); strongest at Auranofin 5 µM: 0.73x vs 0.54x (z diff +2.6) | 0.036 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1; target measured in part of the lines; both ways; artifact flags |
| [[GBP1]] | B | GBP1 activity raises HLA-B's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 3.01× lower at baseline in the lines without GBP1 | 0.038 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[CASP10]] | B | CASP10 activity raises HLA-B's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.26× lower at baseline in the lines without CASP10 | 0.039 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[TRIM22]] | B | TRIM22 activity strengthens HLA-B's drug response | lines that do not express TRIM22 (11) vs lines expressing it (29) | the lines without TRIM22 respond 0.93× as strongly (z diff +0.09); strongest at Auranofin 5 µM: 0.74x vs 0.55x (z diff +2.9) | 0.055 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1; target measured in part of the lines; both ways; artifact flags |
| [[CD74]] | B | CD74 activity raises HLA-B's level | lines that do not express CD74 (31) vs lines expressing it (19) | 1.93× lower at baseline in the lines without CD74 | 0.058 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[OAS1]] | B | OAS1 activity strengthens HLA-B's drug response | lines that do not express OAS1 (9) vs lines expressing it (31) | the lines without OAS1 respond 0.87× as strongly (z diff +0.13); strongest at Auranofin 5 µM: 0.75x vs 0.56x (z diff +2.7) | 0.059 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[IL15RA]] | B | IL15RA activity raises HLA-B's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 2.75× lower at baseline in the lines without IL15RA | 0.069 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 10, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-E]] | B | HLA-B activity raises HLA-E's level | lines that do not express HLA-B (9) vs lines expressing it (41) | 2.53× lower at baseline in the lines without HLA-B | 0.004 | ⚠ within organs, on part of the lines; also absent: HLA-F, UBE2L6 |
| [[HLA-A]] | B | HLA-B activity raises HLA-A's level | lines that do not express HLA-B (9) vs lines expressing it (41) | 2.61× lower at baseline in the lines without HLA-B | 0.008 | ⚠ within organs, on part of the lines; also absent: HLA-F, UBE2L6 |
| [[IFITM3]] | B | HLA-B activity raises IFITM3's level | lines that do not express HLA-B (9) vs lines expressing it (41) | 2.98× lower at baseline in the lines without HLA-B | 0.022 | ⚠ within organs, on part of the lines; also absent: HLA-F, UBE2L6 |
| [[C15orf48]] | B | HLA-B activity raises C15orf48's level | lines that do not express HLA-B (9) vs lines expressing it (41) | 4.17× lower at baseline in the lines without HLA-B | 0.045 | ⚠ within organs, on part of the lines; also absent: HLA-F, UBE2L6 |
| [[RFX1]] | B | HLA-B activity raises RFX1's level | lines that do not express HLA-B (9) vs lines expressing it (41) | 1.29× lower at baseline in the lines without HLA-B | 0.067 | ⚠ within organs, on part of the lines; also absent: HLA-F, UBE2L6 |
| [[PSMB8]] | B | HLA-B activity raises PSMB8's level | lines that do not express HLA-B (9) vs lines expressing it (41) | 1.88× lower at baseline in the lines without HLA-B | 0.071 | ⚠ within organs, on part of the lines; also absent: HLA-F, UBE2L6 |
| [[IFI44L]] | B | HLA-B activity raises IFI44L's level | lines that do not express HLA-B (9) vs lines expressing it (41) | 3.29× lower at baseline in the lines without HLA-B | 0.085 | ⚠ within organs, on part of the lines; also absent: HLA-F, UBE2L6 |
| [[APOBEC3F]] | B | HLA-B activity raises APOBEC3F's level | lines that do not express HLA-B (9) vs lines expressing it (41) | 1.73× lower at baseline in the lines without HLA-B | 0.086 | ⚠ within organs, on part of the lines; also absent: HLA-F, UBE2L6 |
| [[TRANK1]] | B | HLA-B activity raises TRANK1's level | lines that do not express HLA-B (9) vs lines expressing it (41) | 2.56× lower at baseline in the lines without HLA-B | 0.089 | ⚠ within organs, on part of the lines; also absent: HLA-F, UBE2L6 |
| [[DHX58]] | B | HLA-B activity raises DHX58's level | lines that do not express HLA-B (9) vs lines expressing it (41) | 2.27× lower at baseline in the lines without HLA-B | 0.090 | ⚠ within organs, on part of the lines; also absent: HLA-F, UBE2L6 |
| [[HLA-F]] | C | HLA-B activity raises HLA-F's level | lines that do not express HLA-B (9) vs lines expressing it (41) | 3.15× lower at baseline in the lines without HLA-B | 0.008 | ⚠ within organs, on part of the lines; also absent: HLA-F, UBE2L6; co-absent with the target |
| [[UBE2L6]] | C | HLA-B activity raises UBE2L6's level | lines that do not express HLA-B (9) vs lines expressing it (41) | 2.85× lower at baseline in the lines without HLA-B | 0.063 | ⚠ within organs, on part of the lines; also absent: HLA-F, UBE2L6; co-absent with the target |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.828). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.6, 50.3); signed map (64.3, 27.9). **Vector** length 120, 47.8% of its response variance represented; |z| ≥ 3 in 855 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.64 to 19); *allograft rejection* (hallmark, mean cos +0.65 to 11); *Non-canonical inflammasome activation* (reactome, mean cos +0.61 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +4.9 | +4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.6 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.1 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.1 | -4.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.2 | -4.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.1 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.4 | +6.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.0 | -3.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.4 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | major histocompatibility complex, class I, B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,353,872-31,367,067 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously AS |
| Gene groups (HGNC) | Histocompatibility complex; C1-set domain containing; MicroRNA protein coding host genes |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Reactome | 21 pathways, smallest: Endosomal/Vacuolar pathway; DAP12 interactions; Antigen Presentation: Folding, assembly and peptide loading of class I MHC |
| Matched by | ensembl_id |

**Function**, from UniProt [P01889](https://www.uniprot.org/uniprotkb/P01889) (HLA class I histocompatibility antigen, B alpha chain):

> Antigen-presenting major histocompatibility complex class I (MHCI) molecule. In complex with B2M/beta 2 microglobulin displays primarily viral and tumor-derived peptides on antigen-presenting cells for recognition by alpha-beta T cell receptor (TCR) on HLA-B-restricted CD8-positive T cells, guiding antigen-specific T cell immune response to eliminate infected or transformed cells. May also present self-peptides derived from the signal sequence of secreted or membrane proteins, although T cells …

**Summary**, from NCBI Gene [3106](https://www.ncbi.nlm.nih.gov/gene/3106):

> HLA-B belongs to the HLA class I heavy chain paralogues. This class I molecule is a heterodimer consisting of a heavy chain and a light chain (beta-2 microglobulin). The heavy chain is anchored in the membrane. Class I molecules play a central role in the immune system by presenting peptides derived from the endoplasmic reticulum lumen. They are expressed in nearly all cells. The heavy chain is approximately 45 kDa and its gene contains 8 exons. Exon 1 encodes the leader peptide, exon 2 and 3 …

**Accessions** — [HGNC:4932](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4932) · Entrez [3106](https://www.ncbi.nlm.nih.gov/gene/3106) · UniProt [P01889](https://www.uniprot.org/uniprotkb/P01889) · Ensembl [ENSG00000234745](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234745)

## Data

Gene col 13981: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13981); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13981, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13981]; `tensor/DDL_lfc|DDL_z.npy` [13981]; `embed/gene_vectors.npy` [13981]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13981 or target_col == 13981). Every well: [[HLA-B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HLA-B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
