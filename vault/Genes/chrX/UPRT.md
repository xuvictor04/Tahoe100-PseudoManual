---
symbol: "UPRT"
type: "gene"
col: 1727
ensembl_id: "ENSG00000094841"
name: "uracil phosphoribosyltransferase homolog"
location: "Xq13.3"
module: 105
arm: "+"
pooled_cpm: 32.05
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# UPRT

*uracil phosphoribosyltransferase homolog* — Xq13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[PF-06260933 (drug)]] 5 µM: 1.99× (z +7.0, q 1e-09, up in 30 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.484× (z -14.1, q 2e-42, down in 32 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.673× (z -10.9, q 2e-25, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DTNA]] (+0.57, fdr 2e-05), [[FAM210A]] (+0.54, fdr 2e-05), [[PPME1]] (+0.53, fdr 3e-05); moves opposite to [[TNRC18]] (-0.45, fdr 1e-04), [[MCM7]] (-0.39, fdr 1e-04), [[KLHL5]] (-0.39, fdr 2e-04).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF470]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1727.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PF-06260933 (drug)]] 5 µM |  | **1.99×** | +7.0 | 1e-09 | 30/45 (HOP62, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Roxadustat (drug)]] 5 µM |  | **1.35×** | +5.6 | 5e-06 | 23/45 (PANC-1, SNU-423, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +4.7 | 6e-04 | 19/47 (SW 900, SNU-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +4.4 | 0.001 | 18/45 (SW480, A549, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.4 | 0.001 | 18/47 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | 1.14× | +3.8 | 0.015 | 16/47 (KATO III, COLO 205, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1727.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.484×** | -14.1 | 2e-42 | 32/40 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.507×** | -12.7 | 2e-34 | 32/44 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.531×** | -11.8 | 4e-30 | 25/35 (LOX-IMVI, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.673×** | -10.9 | 2e-25 | 32/46 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.601×** | -9.1 | 7e-18 | 27/38 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.621×** | -8.9 | 6e-17 | 27/47 (SK-MEL-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.742×** | -8.2 | 2e-14 | 26/46 (LOX-IMVI, SNU-423, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.665×** | -7.9 | 2e-13 | 28/47 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.720×** | -6.4 | 1e-08 | 23/45 (HT-29, C-33 A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.717×** | -6.2 | 3e-08 | 26/46 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.717×** | -6.2 | 3e-08 | 25/45 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.912× | -6.0 | 8e-08 | 6/47 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.753×** | -5.5 | 2e-06 | 23/45 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.754×** | -5.5 | 2e-06 | 20/47 (CFPAC-1, SHP-77, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **0.779×** | -4.6 | 1e-04 | 23/43 (MIA PaCa-2, SW1417, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.807×** | -4.2 | 0.001 | 15/46 (MIA PaCa-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.844× | -3.1 | 0.046 | 10/47 (HOP62, H4, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.850× | -3.0 | 0.069 | 16/47 (C-33 A, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1727. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 139 | 0 | 9 (7 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.124× (z -21.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -20.0) |
| [[LOX-IMVI (line)]] | wt | 61.9 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -22.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 51.1 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -11.8) |
| [[HOP62 (line)]] | alt | 55.3 | 0 | 4 (4 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.604× (z -12.5) ⚠ position not correctable |
| [[C-33 A (line)]] | alt | 28.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.151× (z -9.9) |
| [[HCT15 (line)]] | alt | 70.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0939× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Hs 766T (line)]] | wt | 45.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 21.9 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -15.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 47.4 | 1 | 1 (1 ⚠) | [[Ponatinib (drug)]] 5 µM 2.87× (z +8.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.346× (z -8.5) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 40.6 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.241× (z -11.8) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.268× (z -11.0) |
| [[A-427 (line)]] | wt | 17.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -11.1) |
| [[A549 (line)]] | wt | 21.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[AsPC-1 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.257× (z -8.8) ⚠ toxic |
| [[C32 (line)]] | wt | 27.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -12.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0719× (z -8.5) |
| [[H4 (line)]] | wt | 52.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HT-29 (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.169× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[J82 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1792 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -11.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H2347 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.281× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H460 (line)]] | wt | 31.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.407× (z -9.3) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 23.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.404× (z -8.8) |
| [[SHP-77 (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SNU-1 (line)]] | wt | 20.7 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0780× (z -11.9) |
| [[SNU-423 (line)]] | alt | 48.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -12.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW1417 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.290× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~20% of this change |
| [[SW48 (line)]] | wt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 46.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1727), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTNA]] | +0.57 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[FAM210A]] | +0.54 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[PPME1]] | +0.53 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[SMAP1]] | +0.52 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[BNIP3]] | +0.51 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[DHRS13]] | +0.51 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[RIMKLA]] | +0.51 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[FAM162A]] | +0.49 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[ZNF215]] | +0.48 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[SLC2A3]] | +0.47 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[C2orf72]] | +0.47 | +0.32 / +0.53 | both halves | 2e-04 |  |
| [[CNST]] | +0.47 | +0.37 / +0.48 | both halves | 8e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC18]] | -0.45 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[MCM7]] | -0.39 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[KLHL5]] | -0.39 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[VCL]] | -0.38 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ATP11C]] | -0.38 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[JAK2]] | -0.37 | -0.25 / -0.46 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF470]] | B | ZNF470 activity raises UPRT's level | lines that do not express ZNF470 (18) vs lines expressing it (32) | 1.29× lower at baseline in the lines without ZNF470 | 0.034 | ⚠ within organs, on part of the lines; also absent: ZFP28, ZNF71, ZIM2-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.485). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.5, -19.1); signed map (-38.8, 24.9). **Vector** length 89.4, 19.1% of its response variance represented; |z| ≥ 3 in 1,060 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.3 | +4.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +4.5 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.6 | +2.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +1.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.8 | -12.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.5 | -6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -1.8 | -8.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -0.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -0.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | uracil phosphoribosyltransferase homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.3 — chrX:75,156,388-75,304,885 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp781E1243, MGC23937, FUR1, RP11-311P8.3 |
| Matched by | ensembl_id |

UniProt [Q96BW1](https://www.uniprot.org/uniprotkb/Q96BW1) carries no function annotation.

**Summary**, from NCBI Gene [139596](https://www.ncbi.nlm.nih.gov/gene/139596):

> This gene encodes uracil phosphoribosyltransferase, which catalyzes the conversion of uracil and 5-phosphoribosyl-1-R-diphosphate to uridine monophosphate (UMP). This reaction is an important part of nucleotide metabolism, specifically the pyrimidine salvage pathway. The enzyme localizes to the nucleus and cytoplasm. The protein is a potential target for rational design of drugs to treat parasitic infections and cancer. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:28334](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28334) · Entrez [139596](https://www.ncbi.nlm.nih.gov/gene/139596) · UniProt [Q96BW1](https://www.uniprot.org/uniprotkb/Q96BW1) · Ensembl [ENSG00000094841](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000094841)

## Data

Gene col 1727: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1727); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1727, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1727]; `tensor/DDL_lfc|DDL_z.npy` [1727]; `embed/gene_vectors.npy` [1727]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1727 or target_col == 1727). Every well: [[UPRT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UPRT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
