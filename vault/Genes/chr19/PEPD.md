---
symbol: "PEPD"
type: "gene"
col: 4516
ensembl_id: "ENSG00000124299"
name: "peptidase D"
location: "19q13.11"
module: 65
arm: "-"
pooled_cpm: 26.55
n_lines_expressing: 50
n_dd_up: 43
n_dd_down: 0
n_dd_up_clean: 30
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# PEPD

*peptidase D* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.29× (z +27.9, q 0e+00, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (SNU-1 0.250×; ⚠ cell-cycle shift, explains ~0% of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (AN3 CA 0.116×); [[Docetaxel (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.226×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Sonidegib (drug)]] 5 µM in 1 line (HepG2/C3A 0.0550×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VAC14]] (+0.71, fdr 7e-06), [[RBM19]] (+0.63, fdr 1e-05), [[OSTM1]] (+0.60, fdr 7e-06); moves opposite to [[MTF2]] (-0.65, fdr 7e-06), [[ZNF14]] (-0.62, fdr 2e-05), [[NUP54]] (-0.61, fdr 7e-06).
> It sits in the **-** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EID2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 57 in all, 20 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4516.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.29×** | +27.9 | 0e+00 | 44/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **4.18×** | +23.7 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.71×** | +21.7 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.05×** | +18.5 | 0e+00 | 44/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.82×** | +17.2 | 0e+00 | 43/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.24×** | +13.4 | 6e-39 | 38/47 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +12.1 | 7e-32 | 34/47 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.96×** | +11.2 | 4e-27 | 37/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.92×** | +10.8 | 1e-25 | 40/47 (PANC-1, J82, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.02×** | +10.7 | 3e-25 | 31/40 (SW480, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.91×** | +10.7 | 6e-25 | 36/47 (A-172, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +10.1 | 2e-22 | 40/47 (PANC-1, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +9.8 | 3e-21 | 27/35 (SW480, A-427, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.81×** | +9.8 | 6e-21 | 35/44 (NCI-H1792, A549, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.70×** | +8.8 | 7e-17 | 38/47 (HOP62, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.64×** | +7.7 | 3e-13 | 34/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +7.4 | 4e-12 | 30/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.3 | 9e-12 | 29/48 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +7.1 | 4e-11 | 33/48 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +5.9 | 8e-08 | 25/48 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (SNU-1 0.250×; ⚠ cell-cycle shift, explains ~0% of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (AN3 CA 0.116×); [[Docetaxel (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.226×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Sonidegib (drug)]] 5 µM in 1 line (HepG2/C3A 0.0550×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4516. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 34.9 | 9 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.19× (z +17.5) | — |
| [[A-172 (line)]] | wt | 23.5 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +18.3) | — |
| [[HOP62 (line)]] | alt | 24.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +15.2) | — |
| [[HT-29 (line)]] | alt | 24.2 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 7.13× (z +13.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 31.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +18.0) | — |
| [[NCI-H1792 (line)]] | alt | 24.2 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +13.2) | — |
| [[NCI-H460 (line)]] | wt | 22.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +26.0) | — |
| [[SW480 (line)]] | alt | 27.4 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.48× (z +16.9) | — |
| [[COLO 205 (line)]] | alt | 11.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +14.9) | — |
| [[LS 180 (line)]] | wt | 18.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 13.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +13.2) | — |
| [[CFPAC-1 (line)]] | alt | 12.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +12.3) | — |
| [[Hs 766T (line)]] | wt | 16.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.85× (z +15.8) | — |
| [[HS-578T (line)]] | alt | 22.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +14.6) | — |
| [[hTERT-HPNE (line)]] | wt | 31.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.34× (z +15.8) | [[Docetaxel (drug)]] 0.05 µM 0.226× (z -9.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 29.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.83× (z +13.5) | — |
| [[LoVo (line)]] | wt | 28.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +14.6) | — |
| [[LOX-IMVI (line)]] | wt | 29.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +14.5) | — |
| [[SNU-1 (line)]] | wt | 28.9 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +11.1) | [[Selinexor (drug)]] 5 µM 0.250× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 18.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.61× (z +11.5) | — |
| [[A549 (line)]] | wt | 34.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.67× (z +14.4) | — |
| [[HEC-1-A (line)]] | alt | 23.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.67× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 26.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.10× (z +12.6) | — |
| [[A-427 (line)]] | wt | 40.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.78× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.90× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 28.8 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 4.62× (z +9.0) | [[Sonidegib (drug)]] 5 µM 0.0550× (z -8.9) |
| [[J82 (line)]] | alt | 33.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +17.8) | — |
| [[NCI-H1573 (line)]] | alt | 17.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +16.5) | — |
| [[NCI-H2030 (line)]] | alt | 31.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +12.1) | — |
| [[RKO (line)]] | wt | 40.7 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.97× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 27.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +13.0) | — |
| [[SNU-423 (line)]] | alt | 30.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +12.6) | — |
| [[AN3 CA (line)]] | alt | 45.9 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.116× (z -9.1) |
| [[BT-474 (line)]] | alt | 19.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.57× (z +9.4) | — |
| [[H4 (line)]] | wt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.34× (z +11.5) | — |
| [[NCI-H23 (line)]] | alt | 35.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.21× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +15.9) | — |
| [[Panc 03.27 (line)]] | alt | 25.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 28.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 16.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4516), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAC14]] | +0.71 | +0.72 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[RBM19]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[OSTM1]] | +0.60 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[SLC36A1]] | +0.60 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[CTNS]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[NPIPB4]] | +0.59 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[CLCN7]] | +0.58 | +0.70 / +0.40 | both halves | 5e-05 |  |
| [[CEP170B]] | +0.56 | +0.37 / +0.63 | both halves | 8e-05 |  |
| [[SLC35F6]] | +0.56 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[IGF2R]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[PEA15]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[HEXB]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTF2]] | -0.65 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[ZNF14]] | -0.62 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[NUP54]] | -0.61 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[ABHD10]] | -0.60 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[ORC4]] | -0.59 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[ZNF230]] | -0.58 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[TADA1]] | -0.58 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[AFTPH]] | -0.57 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[KLHL28]] | -0.55 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[GEMIN2]] | -0.55 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[ATG4C]] | -0.55 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[RIOK2]] | -0.54 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EID2B]] | B | EID2B activity raises PEPD's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.40× lower at baseline in the lines without EID2B | 0.010 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PEPD's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **-** arm (projection on the module's main direction -0.595). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-12.2, -20.4); signed map (7.4, -8.4). **Vector** length 89.4, 22.7% of its response variance represented; |z| ≥ 3 in 1,283 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.1 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +9.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.7 | +17.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.6 | +13.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +6.2 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +10.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +7.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.9 | +4.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.9 | +2.7 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | +0.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | peptidase D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:33,386,950-33,521,823 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | M24 metallopeptidase family |
| Matched by | ensembl_id |

**Function**, from UniProt [P12955](https://www.uniprot.org/uniprotkb/P12955) (Xaa-Pro dipeptidase):

> Dipeptidase that catalyzes the hydrolysis of dipeptides with a prolyl (Xaa-Pro) or hydroxyprolyl residue in the C-terminal position. The preferred dipeptide substrate is Gly-Pro, but other Xaa-Pro dipeptides, such as Ala-Pro, Met-Pro, Phe-Pro, Val-Pro and Leu-Pro, can be cleaved. Plays an important role in collagen metabolism because the high level of iminoacids in collagen.

**Summary**, from NCBI Gene [5184](https://www.ncbi.nlm.nih.gov/gene/5184):

> This gene encodes a member of the peptidase family. The protein forms a homodimer that hydrolyzes dipeptides or tripeptides with C-terminal proline or hydroxyproline residues. The enzyme serves an important role in the recycling of proline, and may be rate limiting for the production of collagen. Mutations in this gene result in prolidase deficiency, which is characterized by the excretion of large amount of di- and tri-peptides containing proline. Multiple transcript variants encoding …

**Accessions** — [HGNC:8840](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8840) · Entrez [5184](https://www.ncbi.nlm.nih.gov/gene/5184) · UniProt [P12955](https://www.uniprot.org/uniprotkb/P12955) · Ensembl [ENSG00000124299](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124299)

## Data

Gene col 4516: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4516); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4516, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4516]; `tensor/DDL_lfc|DDL_z.npy` [4516]; `embed/gene_vectors.npy` [4516]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4516 or target_col == 4516). Every well: [[PEPD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEPD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
