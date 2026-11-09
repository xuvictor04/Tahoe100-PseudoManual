---
symbol: "VPS4A"
type: "gene"
col: 5347
ensembl_id: "ENSG00000132612"
name: "vacuolar protein sorting 4 homolog A"
location: "16q23.1"
module: 54
arm: "-"
pooled_cpm: 37.08
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# VPS4A

*vacuolar protein sorting 4 homolog A* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.67× (z +14.4, q 3e-44, up in 44 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.42× (z +5.1, q 3e-05, up in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 3.77×, NCI-H1792 4.45×, MIA PaCa-2 3.92×, HOP62 3.72×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (MIA PaCa-2 3.87×, NCI-H1573 4.05×, NCI-H1792 4.22×, HOP62 3.50×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.798× (z -4.7, q 0.002, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.201×, J82 0.341×); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.135×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATMIN]] (+0.62, fdr 1e-05), [[FLII]] (+0.61, fdr 7e-06), [[TWF1]] (+0.57, fdr 1e-05); moves opposite to [[IST1]] (-0.60, fdr 1e-05), [[SNHG19]] (-0.54, fdr 1e-05), [[PTMAP2]] (-0.54, fdr 8e-05, ⚠ PTMAP2 in the vector space only through flagged drug-doses), [[LINC01273]] (-0.52, fdr 4e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GPRC5C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5347.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 3.77×, NCI-H1792 4.45×, MIA PaCa-2 3.92×, HOP62 3.72×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (MIA PaCa-2 3.87×, NCI-H1573 4.05×, NCI-H1792 4.22×, HOP62 3.50×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +14.4 | 3e-44 | 44/46 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +12.3 | 1e-32 | 35/39 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +9.6 | 2e-19 | 37/43 (Hs 766T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.48×** | +5.7 | 1e-06 | 34/47 (HOP62, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +5.1 | 3e-05 | 30/48 (NCI-H2030, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.3 | 0.002 | 28/47 (MIA PaCa-2, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.5 | 0.032 | 0/48 | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.26×** | +3.4 | 0.056 | 20/48 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5347.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.201×, J82 0.341×); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.135×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.798×** | -4.7 | 0.002 | 26/48 (RKO, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | 0.835× | -3.7 | 0.050 | 21/48 (COLO 205, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | 0.650× | -3.3 | 0.12 | 15/48 (SNU-1, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.651× | -3.3 | 0.12 | 17/48 (SW48, AN3 CA, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.800× | -3.3 | 0.12 | 19/48 (NCI-H460, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5347. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 40.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +11.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 28.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.04× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 28.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +10.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 41.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +11.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 34.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +10.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 45.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 43.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 45.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +12.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 41.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +12.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 64.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +10.8) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 25.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +12.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 55.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -20.2) |
| [[SW480 (line)]] | alt | 57.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +10.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 57.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 37.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 34.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +8.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 37.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.135× (z -9.0) |
| [[HT-29 (line)]] | alt | 33.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +8.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 42.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -13.9) |
| [[LoVo (line)]] | wt | 33.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 33.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +11.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 34.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 31.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +11.1) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 34.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5347), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATMIN]] | +0.62 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[FLII]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[TWF1]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ABCF2]] | +0.57 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[PDAP1]] | +0.56 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[CEP170B]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ZNF770]] | +0.55 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[PAK2]] | +0.55 | +0.56 / +0.54 | both halves | 1e-05 | pathway: HIV Infection |
| [[AKAP11]] | +0.55 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[EIF2S1]] | +0.54 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[C1orf198]] | +0.54 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[LEMD2]] | +0.54 | +0.48 / +0.50 | both halves | 2e-05 | pathway: Mitotic Anaphase; STRING 640 |

## Genes that move opposite

*29 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IST1]] | -0.60 | -0.62 / -0.51 | both halves | 1e-05 | pathway: Mitotic Anaphase; STRING 988 |
| [[SNHG19]] | -0.54 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[PTMAP2]] ⚠ | -0.54 | -0.37 / -0.57 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LINC01273]] | -0.52 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[PRRT1]] | -0.52 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[SERF2]] | -0.51 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[GPRC5C]] | -0.51 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[MRPS24]] | -0.51 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[COX7A2]] ⚠ | -0.50 | -0.35 / -0.47 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[HOOK2]] | -0.50 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[CUTA]] | -0.49 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[KMT2E]] | -0.49 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[TBC1D22A-DT]] | -0.49 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[CAPN12]] | -0.49 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRC5C]] | B | GPRC5C activity lowers VPS4A's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 1.20× higher at baseline in the lines without GPRC5C | 0.042 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.317). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.3, -18.8); signed map (-7.3, -37.8). **Vector** length 67.6, 13.6% of its response variance represented; |z| ≥ 3 in 639 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.9 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +12.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +14.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.5 | +0.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -3.2 | -3.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | +0.3 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.4 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -1.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | vacuolar protein sorting 4 homolog A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:69,311,336-69,326,939 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VPS4, VPS4-1, FLJ22197, SKD2, SKD1, SKD1A |
| Gene groups (HGNC) | AAA ATPases; ESCRT-IV |
| Reactome | 17 pathways, smallest: Sealing of the nuclear envelope (NE) by ESCRT-III; Budding and maturation of HIV virion; Endosomal Sorting Complex Required For Transport (ESCRT) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UN37](https://www.uniprot.org/uniprotkb/Q9UN37) (Vacuolar protein sorting-associated protein 4A):

> Involved in late steps of the endosomal multivesicular bodies (MVB) pathway. Recognizes membrane-associated ESCRT-III assemblies and catalyzes their disassembly, possibly in combination with membrane fission. Redistributes the ESCRT-III components to the cytoplasm for further rounds of MVB sorting. MVBs contain intraluminal vesicles (ILVs) that are generated by invagination and scission from the limiting membrane of the endosome and mostly are delivered to lysosomes enabling degradation of …

**Summary**, from NCBI Gene [27183](https://www.ncbi.nlm.nih.gov/gene/27183):

> The protein encoded by this gene is a member of the AAA protein family (ATPases associated with diverse cellular activities), and is the homolog of the yeast Vps4 protein. In humans, two paralogs of the yeast protein have been identified. The former share a high degree of aa sequence similarity with each other, and also with yeast Vps4 and mouse Skd1 proteins. The mouse Skd1 (suppressor of K+ transport defect 1) has been shown to be really an yeast Vps4 ortholog. Functional studies indicate …

**Accessions** — [HGNC:13488](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13488) · Entrez [27183](https://www.ncbi.nlm.nih.gov/gene/27183) · UniProt [Q9UN37](https://www.uniprot.org/uniprotkb/Q9UN37) · Ensembl [ENSG00000132612](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132612)

## Data

Gene col 5347: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5347); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5347, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5347]; `tensor/DDL_lfc|DDL_z.npy` [5347]; `embed/gene_vectors.npy` [5347]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5347 or target_col == 5347). Every well: [[VPS4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
