---
symbol: "USB1"
type: "gene"
col: 2301
ensembl_id: "ENSG00000103005"
name: "U6 snRNA biogenesis phosphodiesterase 1"
location: "16q21"
module: 199
arm: "+"
pooled_cpm: 16.47
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/199"]
generated_by: "tahoemap"
---

# USB1

*U6 snRNA biogenesis phosphodiesterase 1* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.99× (z +32.1, q 0e+00, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.358×; ⚠ cell-cycle shift, explains ~21% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.120×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (AsPC-1 0.159×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXW2]] (+0.66, fdr 1e-05), [[CPSF4]] (+0.64, fdr 2e-05), [[PACC1]] (+0.62, fdr 1e-05); moves opposite to [[ANKRD26]] (-0.65, fdr 8e-05), [[GTF2IRD2B]] (-0.64, fdr 1e-05), [[ZC3H6]] (-0.64, fdr 3e-05).
> It is in [[Module 199]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TMEM154]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 19 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2301.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.99×** | +32.1 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.73×** | +31.3 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.57×** | +27.2 | 0e+00 | 47/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.27×** | +20.4 | 0e+00 | 22/22 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.70×** | +17.8 | 0e+00 | 34/38 (HOP62, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.30×** | +14.9 | 0e+00 | 44/48 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.96×** | +12.0 | 2e-31 | 38/46 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.95×** | +11.5 | 7e-29 | 32/44 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.85×** | +10.2 | 1e-22 | 24/31 (HOP62, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.45×** | +9.4 | 2e-19 | 27/46 (A549, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +9.1 | 3e-18 | 30/48 (A498, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.54×** | +8.7 | 1e-16 | 33/48 (A498, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +8.7 | 1e-16 | 34/47 (HOP62, NCI-H460, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +8.2 | 1e-14 | 29/41 (HT-29, NCI-H1792, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +8.0 | 5e-14 | 26/48 (HOP62, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +5.1 | 7e-06 | 18/47 (LoVo, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 6e-04 | 14/46 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.005 | 8/47 (HOP62, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 1.13× | +3.1 | 0.033 | 5/48 (HOP62, A498, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.25×** | +2.8 | 0.087 | 4/45 (SHP-77, RPMI-7951, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2301.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.358×; ⚠ cell-cycle shift, explains ~21% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.120×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (AsPC-1 0.159×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.878× | -3.3 | 0.48 | 22/47 (NCI-H2030, HCT15, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | 0.726× | -3.0 | 0.61 | 11/45 (LS 180, HCT15, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.70 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2301. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 16.7 | 7 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.95× (z +16.2) | — |
| [[A549 (line)]] | wt | 17.7 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 8.58× (z +13.2) | — |
| [[A498 (line)]] | wt | 45.7 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.48× (z +12.9) | — |
| [[NCI-H460 (line)]] | wt | 18.5 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.48× (z +16.7) | — |
| [[PANC-1 (line)]] | alt | 13.3 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.97× (z +13.7) | — |
| [[AsPC-1 (line)]] | alt | 7.54 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 7.91× (z +9.8) | [[Thymol (drug)]] 0.5 µM 0.159× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 28.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.18× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[LoVo (line)]] | wt | 10.5 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.71× (z +10.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 12.4 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 11.0× (z +12.9) | — |
| [[NCI-H2030 (line)]] | alt | 40.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.94× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -13.6) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A-172 (line)]] | wt | 8.94 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.27× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 6.78 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.92× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 11.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.55× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 11.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 11.1× (z +11.3) | — |
| [[HS-578T (line)]] | alt | 12.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.55× (z +10.9) | — |
| [[HT-29 (line)]] | alt | 13.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.17× (z +10.8) | — |
| [[J82 (line)]] | alt | 23.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.42× (z +12.0) | — |
| [[KATO III (line)]] | alt | 11.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.00× (z +11.9) | — |
| [[LOX-IMVI (line)]] | wt | 12.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.74× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 12.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 9.22× (z +13.1) | — |
| [[NCI-H1792 (line)]] | alt | 7.52 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.60× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 18.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.02× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.40× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 11.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.29× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 16.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.02× (z +10.5) | — |
| [[SW480 (line)]] | alt | 16.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.81× (z +19.7) | — |
| [[A-427 (line)]] | wt | 20.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.65× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 8.76 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 14.2× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 23.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.54× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 11.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.79× (z +9.4) | — |
| [[RKO (line)]] | wt | 32.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.02× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 9.72 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 10.4× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 9.30 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.69× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2301), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW2]] | +0.66 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[CPSF4]] | +0.64 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[PACC1]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[TBC1D24]] | +0.62 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[TRABD]] | +0.61 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[CAP1]] | +0.61 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[FAM91A1]] | +0.61 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[SH3GLB2]] | +0.61 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[ANKRD52]] | +0.61 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[BCAP31]] | +0.60 | +0.55 / +0.38 | both halves | 7e-05 |  |
| [[TSPAN17]] | +0.60 | +0.65 / +0.33 | both halves | 1e-04 |  |
| [[PPM1F]] | +0.60 | +0.57 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD26]] | -0.65 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[GTF2IRD2B]] | -0.64 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[ZC3H6]] | -0.64 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[HELQ]] | -0.63 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[PPIG]] | -0.63 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[DNAJC27]] | -0.63 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[GUCY2C-AS1]] | -0.63 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[CCDC174]] | -0.61 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[C11orf71]] | -0.61 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[ZNF764]] | -0.61 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[ZMYM5]] | -0.61 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[OXA1L-DT]] | -0.61 | -0.59 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM154]] | B | TMEM154 activity lowers USB1's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 1.21× higher at baseline in the lines without TMEM154 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[TOP2A]] | B | TOP2A activity lowers USB1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[STRIP2]] | B | STRIP2 activity lowers USB1's level | lines that do not express STRIP2 (6) vs lines expressing it (44) | 1.16× higher at baseline in the lines without STRIP2 | 0.069 | ⚠ within organs, on part of the lines; also absent: STK31, HLA-F-AS1, MIR181A2HG; maybe low, not absent |
| [[MFAP3L]] | B | MFAP3L activity raises USB1's level | lines that do not express MFAP3L (9) vs lines expressing it (41) | 1.27× lower at baseline in the lines without MFAP3L | 0.079 | ⚠ within organs, on part of the lines; also absent: CRACD, FILIP1, TSPAN33; maybe low, not absent |
| [[CCDC69]] | B | CCDC69 activity lowers USB1's level | lines that do not express CCDC69 (11) vs lines expressing it (39) | 1.03× higher at baseline in the lines without CCDC69 | 0.086 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 199]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.694). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.3, 11.7); signed map (-42.8, -10.8). **Vector** length 73.7, 14.7% of its response variance represented; |z| ≥ 3 in 1,114 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +3.9 | +17.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +3.6 | +20.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.5 | +27.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +31.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -7.9 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.1 | +0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +1.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.5 | +9.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.6 | -0.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.6 | -0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | U6 snRNA biogenesis phosphodiesterase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:57,999,546-58,021,618 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13154, HVSL1, Mpn1; previously C16orf57 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQ65](https://www.uniprot.org/uniprotkb/Q9BQ65) (U6 snRNA phosphodiesterase 1):

> 3'-5' RNA exonuclease that trims the 3' end of oligo(U) and oligo(A) tracts of the pre-U6 small nuclear RNA (snRNA) molecule, leading to the formation of a mature U6 snRNA 3' end-terminated with a 2',3'-cyclic phosphate. Participates in the U6 snRNA 3' end processing that prevents U6 snRNA degradation. In addition also removes uridines from the 3' end of U6atac snRNA and possibly the vault RNA VTRNA1-1.

**Summary**, from NCBI Gene [79650](https://www.ncbi.nlm.nih.gov/gene/79650):

> This gene encodes a protein with several conserved domains, however, its exact function is not known. Mutations in this gene are associated with poikiloderma with neutropenia (PN), which shows phenotypic overlap with Rothmund-Thomson syndrome (RTS) caused by mutations in the RECQL4 gene. It is believed that this gene product interacts with RECQL4 protein via SMAD4 proteins, explaining the partial clinical overlap between PN and RTS. Alternatively spliced transcript variants encoding different …

**Accessions** — [HGNC:25792](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25792) · Entrez [79650](https://www.ncbi.nlm.nih.gov/gene/79650) · UniProt [Q9BQ65](https://www.uniprot.org/uniprotkb/Q9BQ65) · Ensembl [ENSG00000103005](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103005)

## Data

Gene col 2301: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2301); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2301, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2301]; `tensor/DDL_lfc|DDL_z.npy` [2301]; `embed/gene_vectors.npy` [2301]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2301 or target_col == 2301). Every well: [[USB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
