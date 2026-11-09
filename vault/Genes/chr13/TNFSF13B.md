---
symbol: "TNFSF13B"
type: "gene"
col: 2252
ensembl_id: "ENSG00000102524"
name: "TNF superfamily member 13b"
location: "13q33.3"
module: 37
arm: "+"
pooled_cpm: 16.04
n_lines_expressing: 48
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# TNFSF13B

*TNF superfamily member 13b* — 13q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +10.0, q 6e-21, up in 32 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.551× (z -8.4, q 3e-14, down in 27 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR49]] (+0.72, fdr 7e-06), [[CASS4]] (+0.71, fdr 1e-05), [[LINC00640]] (+0.69, fdr 7e-06); moves opposite to [[PDHA1]] (-0.53, fdr 7e-05), [[FAAP100]] (-0.53, fdr 6e-05), [[TTLL12]] (-0.53, fdr 5e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2252.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +10.0 | 6e-21 | 32/43 (SHP-77, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +7.8 | 1e-12 | 28/43 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.5 | 8e-06 | 22/45 (Panc 03.27, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +5.3 | 2e-05 | 19/46 (COLO 205, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +5.3 | 2e-05 | 19/45 (LS 180, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +5.2 | 2e-05 | 21/46 (LoVo, J82, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +4.9 | 7e-05 | 22/44 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.93×** | +4.8 | 9e-05 | 20/44 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.003 | 15/45 (HOP62, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.22×** | +3.9 | 0.006 | 15/46 (Panc 03.27, J82, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.6 | 0.014 | 15/39 (SHP-77, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.015 | 10/46 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.032 | 11/44 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +3.2 | 0.048 | 15/43 (SW480, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.068 | 10/44 (hTERT-HPNE, HCT15, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2252.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.551×** | -8.4 | 3e-14 | 27/43 (CFPAC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.584×** | -7.5 | 1e-11 | 24/36 (LOX-IMVI, NCI-H1573, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.778×** | -5.0 | 1e-04 | 19/43 (A-172, HS-578T, …) | top dose only | composition shift |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.747×** | -4.0 | 0.011 | 13/45 (RKO, J82, …) | top dose only | plate-row cell shift |
| [[Berbamine (drug)]] 0.05 µM |  | **0.783×** | -3.4 | 0.061 | 13/46 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **0.774×** | -3.4 | 0.061 | 10/45 (NCI-H1573, SW 1088, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.771×** | -3.3 | 0.075 | 11/45 (NCI-H2347, RPMI-7951, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~68% of this change | 0.804× | -3.1 | 0.13 | 14/41 (LS 180, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | 0.797× | -3.1 | 0.13 | 13/24 (HT-29, KATO III, …) | all doses, flat | composition shift |
| [[vincristine (drug)]] 5 µM |  | 0.660× | -3.0 | 0.13 | 6/39 (CFPAC-1, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.807× | -3.0 | 0.13 | 16/45 (NCI-H2347, CFPAC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2252. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 23.3 | 2 (2 ⚠) | 6 (4 ⚠) | [[Harringtonine (drug)]] 0.5 µM 6.02× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Tofacitinib (drug)]] 0.5 µM 0.174× (z -9.6) |
| [[SHP-77 (line)]] | alt | 9.07 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.17× (z +9.7) | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0803× (z -9.7) |
| [[SW48 (line)]] | wt | 24.2 | 0 | 3 | — | [[Drospirenone (drug)]] 0.5 µM 0.0907× (z -10.6) |
| [[A-172 (line)]] | wt | 11.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -15.3) ⚠ cell-cycle shift, explains ~87% of this change |
| [[HT-29 (line)]] | alt | 32.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[KATO III (line)]] | alt | 20.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[LOX-IMVI (line)]] | wt | 27.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0845× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.263× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 54.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[PANC-1 (line)]] | alt | 14.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SNU-423 (line)]] | alt | 12.2 | 0 | 2 (1 ⚠) | — | [[Pemetrexed (drug)]] 5 µM 0.0753× (z -11.6) |
| [[A498 (line)]] | wt | 8.33 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -8.5) ⚠ cell-cycle shift, explains ~87% of this change |
| [[A549 (line)]] | wt | 6.88 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0970× (z -9.1) ⚠ cell-cycle shift, explains ~98% of this change |
| [[BT-474 (line)]] | alt | 8.17 | 0 | 1 | — | [[Nevirapine (drug)]] 0.05 µM 0.0864× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 18.4 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.144× (z -10.9) |
| [[COLO 205 (line)]] | alt | 61.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HEC-1-A (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HS-578T (line)]] | alt | 9.68 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -13.1) ⚠ cell-cycle shift, explains ~87% of this change |
| [[LS 180 (line)]] | wt | 44.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[MIA PaCa-2 (line)]] | alt | 4.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[RPMI-7951 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.145× (z -8.7) |
| [[A-427 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.46 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2252), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR49]] | +0.72 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[CASS4]] | +0.71 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[LINC00640]] | +0.69 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[KLRD1]] | +0.68 | +0.65 / +0.49 | both halves | 1e-05 | same gene group |
| [[DCAF4L1]] | +0.68 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[LINC02762]] | +0.67 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[LVRN]] | +0.66 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[LINC02680]] | +0.66 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PLSCR2]] | +0.65 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[SNX31]] | +0.65 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[PSMD6-AS2]] | +0.65 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[BORCS7-ASMT]] | +0.65 | +0.60 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDHA1]] | -0.53 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[FAAP100]] | -0.53 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[TTLL12]] | -0.53 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[RNFT2]] | -0.52 | -0.40 / -0.27 | both halves | 3e-04 |  |
| [[CSRP1]] | -0.52 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[BCKDK]] | -0.52 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[APEH]] | -0.52 | -0.40 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA3]] | B | CA3 activity raises TNFSF13B's level | lines that do not express CA3 (10) vs lines expressing it (40) | 2.03× lower at baseline in the lines without CA3 | 0.032 | ⚠ within organs, on part of the lines; also absent: CA13, NAALADL2, PLSCR2 |
| [[CADPS2]] | B | CADPS2 activity raises TNFSF13B's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.72× lower at baseline in the lines without CADPS2 | 0.033 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |
| [[CORIN]] | B | CORIN activity raises TNFSF13B's level | lines that do not express CORIN (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without CORIN | 0.099 | ⚠ within organs, on part of the lines; also absent: TNNI3K, WDR49, ENSG00000229195; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.9, -17.8); signed map (10.6, 4.2). **Vector** length 97.0, 20.9% of its response variance represented; |z| ≥ 3 in 987 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +7.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.0 | +5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.5 | +5.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.2 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +2.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.3 | -8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -5.2 | -5.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -3.7 | -3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -3.7 | -7.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -1.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.1 | -0.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.0 | -3.3 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | -2.0 | -3.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.8 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | TNF superfamily member 13b |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q33.3 — chr13:108,251,240-108,308,484 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BAFF, THANK, BLYS, TALL-1, TALL1, CD257; previously TNFSF20 |
| Gene groups (HGNC) | CD molecules; Tumor necrosis factor superfamily |
| Reactome | 7 pathways, smallest: TNF receptor superfamily (TNFSF) members mediating non-canonical NF-kB pathway; TNFs bind their physiological receptors; TNFR2 non-canonical NF-kB pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y275](https://www.uniprot.org/uniprotkb/Q9Y275) (Tumor necrosis factor ligand superfamily member 13B):

> Cytokine that binds to TNFRSF13B/TACI and TNFRSF17/BCMA. TNFSF13/APRIL binds to the same 2 receptors. Together, they form a 2 ligands -2 receptors pathway involved in the stimulation of B- and T-cell function and the regulation of humoral immunity. A third B-cell specific BAFF-receptor (BAFFR/BR3) promotes the survival of mature B-cells and the B-cell response.; Isoform 2 seems to inhibit isoform 1 secretion and bioactivity.; [Isoform 3]: Acts as a transcription factor for its own parent gene, …

**Summary**, from NCBI Gene [10673](https://www.ncbi.nlm.nih.gov/gene/10673):

> The protein encoded by this gene is a cytokine that belongs to the tumor necrosis factor (TNF) ligand family. This cytokine is a ligand for receptors TNFRSF13B/TACI, TNFRSF17/BCMA, and TNFRSF13C/BAFFR. This cytokine is expressed in B cell lineage cells, and acts as a potent B cell activator. It has been also shown to play an important role in the proliferation and differentiation of B cells. Alternatively spliced transcript variants encoding distinct isoforms have been identified. [provided by …

**Accessions** — [HGNC:11929](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11929) · Entrez [10673](https://www.ncbi.nlm.nih.gov/gene/10673) · UniProt [Q9Y275](https://www.uniprot.org/uniprotkb/Q9Y275) · Ensembl [ENSG00000102524](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102524)

## Data

Gene col 2252: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2252); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2252, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2252]; `tensor/DDL_lfc|DDL_z.npy` [2252]; `embed/gene_vectors.npy` [2252]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2252 or target_col == 2252). Every well: [[TNFSF13B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFSF13B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
