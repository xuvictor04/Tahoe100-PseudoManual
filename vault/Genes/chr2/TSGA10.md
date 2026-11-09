---
symbol: "TSGA10"
type: "gene"
col: 5787
ensembl_id: "ENSG00000135951"
name: "testis specific 10"
location: "2q11.2"
module: 10
arm: "+"
pooled_cpm: 21.64
n_lines_expressing: 49
n_dd_up: 45
n_dd_down: 1
n_dd_up_clean: 37
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# TSGA10

*testis specific 10* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.34× (z +38.7, q 0e+00, up in 44 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.744× (z -4.1, q 0.025, down in 21 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (C-33 A 0.250×).
> Its strongest partners by |cos| (72 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 28 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AK9]] (+0.77, fdr 1e-05), [[PPP1R12A-AS2]] (+0.76, fdr 1e-04), [[LINC00571]] (+0.75, fdr 5e-04); moves opposite to [[TAF5L]] (-0.71, fdr 1e-05), [[NR2C1]] (-0.69, fdr 2e-04), [[PHKA2]] (-0.68, fdr 6e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5787.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.34×** | +38.7 | 0e+00 | 44/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.52×** | +33.2 | 0e+00 | 45/45 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.21×** | +21.8 | 0e+00 | 46/46 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.82×** | +18.4 | 0e+00 | 42/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.75×** | +17.5 | 0e+00 | 40/45 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.27×** | +16.3 | 0e+00 | 42/46 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.24×** | +15.7 | 0e+00 | 40/47 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.67×** | +12.9 | 2e-36 | 38/45 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.51×** | +12.6 | 1e-34 | 41/46 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.34×** | +11.7 | 1e-29 | 39/46 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.06×** | +9.9 | 3e-21 | 37/46 (NCI-H460, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +9.6 | 4e-20 | 22/30 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +8.9 | 2e-17 | 28/41 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.81×** | +8.1 | 2e-14 | 35/46 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.79×** | +8.0 | 4e-14 | 36/46 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +7.3 | 1e-11 | 29/47 (SW 900, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.70×** | +7.1 | 3e-11 | 33/46 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5787.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (C-33 A 0.250×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.744×** | -4.1 | 0.025 | 21/45 (HepG2/C3A, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5787. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.9 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 26.8× (z +28.8) | — |
| [[A-172 (line)]] | wt | 11.7 | 8 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.8× (z +16.8) | — |
| [[A498 (line)]] | wt | 9.06 | 8 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.6× (z +19.1) | — |
| [[HOP62 (line)]] | alt | 14.2 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.1× (z +24.0) | — |
| [[LoVo (line)]] | wt | 28.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.18× (z +24.6) | — |
| [[SW 900 (line)]] | alt | 20.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.96× (z +18.5) | — |
| [[SW480 (line)]] | alt | 38.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +20.7) | — |
| [[HEC-1-A (line)]] | alt | 72.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +13.4) | — |
| [[SW1417 (line)]] | alt | 25.4 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +14.5) | — |
| [[AsPC-1 (line)]] | alt | 9.46 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.41× (z +14.4) | — |
| [[C32 (line)]] | wt | 16.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.34× (z +14.5) | — |
| [[HT-29 (line)]] | alt | 28.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.58× (z +14.6) | — |
| [[J82 (line)]] | alt | 10.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +19.0) | — |
| [[LS 180 (line)]] | wt | 27.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.05× (z +16.3) | — |
| [[NCI-H1573 (line)]] | alt | 23.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +18.0) | — |
| [[NCI-H23 (line)]] | alt | 38.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +14.2) | — |
| [[NCI-H2347 (line)]] | alt | 20.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.10× (z +17.8) | — |
| [[Panc 03.27 (line)]] | alt | 23.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.09× (z +14.4) | — |
| [[PANC-1 (line)]] | alt | 10.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +18.8) | — |
| [[RKO (line)]] | wt | 31.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.11× (z +16.1) | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +14.7) | — |
| [[A-427 (line)]] | wt | 27.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 49.6 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +9.9) | [[Ixazomib citrate (drug)]] 5 µM 0.250× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 23.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +17.2) | — |
| [[H4 (line)]] | wt | 16.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.73× (z +11.2) | — |
| [[hTERT-HPNE (line)]] | wt | 8.28 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 17.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.94× (z +16.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.41 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +15.6) | — |
| [[SK-MEL-2 (line)]] | alt | 28.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.76× (z +20.9) | — |
| [[SNU-423 (line)]] | alt | 12.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.31× (z +16.7) | — |
| [[SW48 (line)]] | wt | 14.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +13.7) | — |
| [[A549 (line)]] | wt | 10.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.08× (z +13.6) | — |
| [[BT-474 (line)]] | alt | 34.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +11.6) | — |
| [[COLO 205 (line)]] | alt | 48.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +15.3) | — |
| [[HCT15 (line)]] | alt | 68.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +12.3) | — |
| [[HepG2_C3A (line)]] | wt | 38.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +13.1) | — |
| [[Hs 766T (line)]] | wt | 12.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +16.1) | — |
| [[KATO III (line)]] | alt | 20.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 6.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.32× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +15.9) | — |
| [[SHP-77 (line)]] | alt | 23.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +14.3) | — |
| [[AN3 CA (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5787), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 22 of them with an alert (⚠; 22 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AK9]] | +0.77 | +0.87 / +0.49 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.76 | +0.84 / +0.34 | both halves | 1e-04 |  |
| [[LINC00571]] | +0.75 | +0.79 / +0.23 | both halves | 5e-04 |  |
| [[CCDC90B-AS1]] | +0.75 | +0.82 / +0.28 | both halves | 3e-04 |  |
| [[PKN2-AS1]] | +0.74 | +0.83 / +0.25 | both halves | 4e-04 |  |
| [[PDCL3P4]] | +0.74 | +0.84 / +0.40 | both halves | 5e-05 |  |
| [[ARRDC3-AS1]] | +0.74 | +0.84 / +0.36 | both halves | 1e-04 |  |
| [[MMADHC-DT]] | +0.73 | +0.81 / +0.21 | both halves | 7e-04 |  |
| [[RFX3-DT]] | +0.73 | +0.79 / +0.35 | both halves | 1e-04 |  |
| [[PATL2]] | +0.73 | +0.85 / +0.28 | both halves | 3e-04 |  |
| [[TMEM202-AS1]] | +0.73 | +0.83 / +0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[OXA1L-DT]] | +0.73 | +0.80 / +0.24 | both halves | 4e-04 |  |
| [[UFL1-AS1]] | +0.73 | +0.81 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF5L]] | -0.71 | -0.73 / -0.51 | both halves | 1e-05 |  |
| [[NR2C1]] | -0.69 | -0.72 / -0.29 | both halves | 2e-04 |  |
| [[PHKA2]] | -0.68 | -0.68 / -0.38 | both halves | 6e-05 |  |
| [[ANKRD27]] | -0.68 | -0.72 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[PBX4]] | -0.68 | -0.64 / -0.22 | both halves | 6e-04 |  |
| [[GTF2E2]] | -0.67 | -0.71 / -0.31 | both halves | 2e-04 |  |
| [[TSEN54]] | -0.67 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[LRFN3]] | -0.66 | -0.68 / -0.23 | both halves | 5e-04 |  |
| [[L2HGDH]] | -0.66 | -0.61 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[RNF216]] | -0.65 | -0.72 / -0.30 | both halves | 2e-04 |  |
| [[GNA12]] | -0.65 | -0.70 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[MAST3]] | -0.65 | -0.67 / -0.00 | ⚠ one half (not replicated) | 0.009 |  |
| [[BRF1]] | -0.64 | -0.62 / -0.21 | both halves | 7e-04 |  |
| [[BRAT1]] | -0.64 | -0.56 / -0.27 | both halves | 3e-04 |  |
| [[POLRMT]] | -0.64 | -0.65 / -0.29 | both halves | 3e-04 |  |
| [[LPCAT4]] | -0.64 | -0.70 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TSGA10's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.8% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[LINC00869-1]] | B | LINC00869-1 activity raises TSGA10's level | lines that do not express LINC00869-1 (7) vs lines expressing it (43) | 2.20× lower at baseline in the lines without LINC00869-1 | 0.067 | ⚠ within organs, on part of the lines; also absent: OSBPL10, STPG2, EIF4E3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.714). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.3, 13.4); signed map (24.6, -7.6). **Vector** length 88.0, 23.3% of its response variance represented; |z| ≥ 3 in 1,400 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +18.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +15.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +21.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +38.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +12.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +4.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +8.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.2 | +5.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.2 | +12.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.0 | +11.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.6 | +16.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.3 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | +4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | testis specific 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:98,997,261-99,154,964 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CEP4L, CT79 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZW7](https://www.uniprot.org/uniprotkb/Q9BZW7) (Testis-specific gene 10 protein):

> Plays a role in spermatogenesis. When overexpressed, prevents nuclear localization of HIF1A (By similarity).

**Summary**, from NCBI Gene [80705](https://www.ncbi.nlm.nih.gov/gene/80705):

> Predicted to enable structural molecule activity. Predicted to be involved in spermatogenesis. Located in centriole. Implicated in spermatogenic failure 26. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14927](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14927) · Entrez [80705](https://www.ncbi.nlm.nih.gov/gene/80705) · UniProt [Q9BZW7](https://www.uniprot.org/uniprotkb/Q9BZW7) · Ensembl [ENSG00000135951](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135951)

## Data

Gene col 5787: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5787); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5787, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5787]; `tensor/DDL_lfc|DDL_z.npy` [5787]; `embed/gene_vectors.npy` [5787]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5787 or target_col == 5787). Every well: [[TSGA10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSGA10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
