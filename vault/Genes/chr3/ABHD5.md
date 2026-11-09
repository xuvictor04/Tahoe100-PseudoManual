---
symbol: "ABHD5"
type: "gene"
col: 227
ensembl_id: "ENSG00000011198"
name: "abhydrolase domain containing 5, lysophosphatidic acid acyltransferase"
location: "3p21.33"
module: 93
arm: "+"
pooled_cpm: 38.98
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# ABHD5

*abhydrolase domain containing 5, lysophosphatidic acid acyltransferase* — 3p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.50× (z +23.7, q 0e+00, up in 43 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 0.102×, SW48 0.201×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRDM2]] (+0.65, fdr 1e-05), [[GCH1]] (+0.60, fdr 7e-06), [[NUFIP2]] (+0.58, fdr 3e-05); moves opposite to [[THOC1]] (-0.53, fdr 4e-05), [[COA1]] (-0.52, fdr 1e-04), [[BRD7]] (-0.52, fdr 1e-04).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 227.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.50×** | +23.7 | 0e+00 | 43/47 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +18.1 | 0e+00 | 46/49 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.54×** | +12.5 | 2e-33 | 42/47 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +11.1 | 2e-26 | 46/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.36×** | +11.0 | 3e-26 | 45/48 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.02×** | +9.4 | 7e-19 | 41/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +7.9 | 2e-13 | 39/49 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +7.8 | 3e-13 | 40/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +7.6 | 2e-12 | 31/48 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +7.4 | 6e-12 | 35/48 (PANC-1, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +5.8 | 3e-07 | 26/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +5.7 | 5e-07 | 32/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +5.4 | 4e-06 | 30/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.57×** | +5.2 | 1e-05 | 26/48 (LoVo, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.46×** | +5.1 | 1e-05 | 26/48 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +5.0 | 2e-05 | 29/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +4.9 | 3e-05 | 29/48 (J82, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.5 | 2e-04 | 25/48 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +4.2 | 6e-04 | 25/48 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 0.102×, SW48 0.201×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 227. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.8 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +20.3) | — |
| [[LoVo (line)]] | wt | 39.9 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +24.7) | — |
| [[PANC-1 (line)]] | alt | 16.3 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +17.2) | — |
| [[HEC-1-A (line)]] | alt | 59.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +23.0) | — |
| [[HOP62 (line)]] | alt | 22.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.87× (z +18.4) | — |
| [[J82 (line)]] | alt | 56.6 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +12.4) | — |
| [[LS 180 (line)]] | wt | 32.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +15.3) | — |
| [[A498 (line)]] | wt | 32.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +17.3) | — |
| [[AsPC-1 (line)]] | alt | 29.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +11.1) | — |
| [[C32 (line)]] | wt | 47.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.28× (z +22.5) | — |
| [[LOX-IMVI (line)]] | wt | 26.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.32× (z +16.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +11.2) | — |
| [[SW1417 (line)]] | alt | 84.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +14.1) | — |
| [[SW48 (line)]] | wt | 35.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[SW480 (line)]] | alt | 34.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +17.1) | — |
| [[BT-474 (line)]] | alt | 24.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 27.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +14.0) | — |
| [[hTERT-HPNE (line)]] | wt | 47.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.92× (z +15.0) | — |
| [[KATO III (line)]] | alt | 28.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +12.7) | — |
| [[NCI-H1573 (line)]] | alt | 27.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +15.4) | — |
| [[NCI-H1792 (line)]] | alt | 66.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +13.5) | — |
| [[NCI-H23 (line)]] | alt | 19.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 89.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +12.4) | — |
| [[Panc 03.27 (line)]] | alt | 52.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +12.5) | — |
| [[RPMI-7951 (line)]] | alt | 39.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 35.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[SNU-1 (line)]] | wt | 21.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +10.0) | — |
| [[A-172 (line)]] | wt | 26.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +10.9) | — |
| [[A549 (line)]] | wt | 31.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 65.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +11.1) | — |
| [[COLO 205 (line)]] | alt | 24.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +12.0) | — |
| [[H4 (line)]] | wt | 14.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 14.4 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.70× (z +9.1) ⚠ unreliable plate only | — |
| [[HS-578T (line)]] | alt | 46.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 66.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.6) | — |
| [[RKO (line)]] | wt | 40.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +12.6) | — |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +15.8) | — |
| [[SNU-423 (line)]] | alt | 42.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.4) | — |
| [[SW 900 (line)]] | alt | 50.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +10.3) | — |
| [[A-427 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 79.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 227), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM2]] | +0.65 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[GCH1]] | +0.60 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[NUFIP2]] | +0.58 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[SLC9A1]] | +0.57 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[LINC00910]] | +0.57 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[ADPRHL1]] | +0.57 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[CSRNP2]] | +0.55 | +0.57 / +0.37 | both halves | 8e-05 |  |
| [[C6orf62]] | +0.54 | +0.53 / +0.38 | both halves | 7e-05 |  |
| [[MFSD2B]] | +0.53 | +0.55 / +0.38 | both halves | 6e-05 |  |
| [[CHCHD7]] | +0.53 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[FAM151B]] | +0.53 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[NXF1]] | +0.53 | +0.52 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC1]] | -0.53 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[COA1]] | -0.52 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[BRD7]] | -0.52 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[DLD]] | -0.51 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[PXMP4]] | -0.51 | -0.47 / -0.22 | both halves | 6e-04 |  |
| [[MRPS31P5-1]] | -0.51 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[GTF3C1]] | -0.50 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[PAK4]] | -0.50 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[NAA40]] | -0.50 | -0.53 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[SPATA6]] | -0.50 | -0.41 / -0.22 | both halves | 6e-04 |  |
| [[MEST]] | -0.49 | -0.47 / -0.37 | both halves | 9e-05 |  |
| [[EHMT2]] | -0.48 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[VTA1]] | -0.48 | -0.36 / -0.39 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ABHD5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MEST]] | B | MEST activity raises ABHD5's level | lines that do not express MEST (17) vs lines expressing it (33) | 1.41× lower at baseline in the lines without MEST | 0.099 | ⚠ within organs, on part of the lines; also absent: COPG2IT1, CHDH, IL17RB |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.574). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.3, -26.6); signed map (4.3, 17.1). **Vector** length 92.1, 24.6% of its response variance represented; |z| ≥ 3 in 1,197 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +18.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +11.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.6 | +3.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.1 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +7.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.7 | +2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +2.4 | +1.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -5.1 | +5.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -4.5 | +5.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -4.3 | +4.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.5 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -0.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +0.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | abhydrolase domain containing 5, lysophosphatidic acid acyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.33 — chr3:43,690,108-43,734,371 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-58, NCIE2 |
| Gene groups (HGNC) | Abhydrolase domain containing; Acyltransferases |
| Reactome | 3 pathways, smallest: Triglyceride catabolism; Triglyceride metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WTS1](https://www.uniprot.org/uniprotkb/Q8WTS1) (1-acylglycerol-3-phosphate O-acyltransferase ABHD5):

> Coenzyme A-dependent lysophosphatidic acid acyltransferase that catalyzes the transfer of an acyl group on a lysophosphatidic acid. Functions preferentially with 1-oleoyl-lysophosphatidic acid followed by 1-palmitoyl-lysophosphatidic acid, 1-stearoyl-lysophosphatidic acid and 1-arachidonoyl-lysophosphatidic acid as lipid acceptor. Functions preferentially with arachidonoyl-CoA followed by oleoyl-CoA as acyl group donors (By similarity). Functions in phosphatidic acid biosynthesis. May regulate …

**Summary**, from NCBI Gene [51099](https://www.ncbi.nlm.nih.gov/gene/51099):

> The protein encoded by this gene belongs to a large family of proteins defined by an alpha/beta hydrolase fold, and contains three sequence motifs that correspond to a catalytic triad found in the esterase/lipase/thioesterase subfamily. It differs from other members of this subfamily in that its putative catalytic triad contains an asparagine instead of the serine residue. Mutations in this gene have been associated with Chanarin-Dorfman syndrome, a triglyceride storage disease with impaired …

**Accessions** — [HGNC:21396](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21396) · Entrez [51099](https://www.ncbi.nlm.nih.gov/gene/51099) · UniProt [Q8WTS1](https://www.uniprot.org/uniprotkb/Q8WTS1) · Ensembl [ENSG00000011198](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011198)

## Data

Gene col 227: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 227); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 227, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 227]; `tensor/DDL_lfc|DDL_z.npy` [227]; `embed/gene_vectors.npy` [227]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 227 or target_col == 227). Every well: [[ABHD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
