---
symbol: "TRAF6"
type: "gene"
col: 10561
ensembl_id: "ENSG00000175104"
name: "TNF receptor associated factor 6"
location: "11p12"
module: 30
arm: "+"
pooled_cpm: 25.84
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# TRAF6

*TNF receptor associated factor 6* — 11p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.76× (z +7.0, q 1e-09, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.339× (z -12.9, q 2e-35, down in 31 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.754× (z -5.0, q 1e-04, down in 28 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SW1417 0.155×, A549 0.153×, AsPC-1 0.195×, A498 0.224×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 0.132×, A498 0.104×, KATO III 0.111×, LoVo 0.144×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-172 0.0640×, SW480 0.257×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0639×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.378×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (AN3 CA 0.0832×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS33B]] (+0.61, fdr 1e-05), [[PLD2]] (+0.61, fdr 7e-06), [[FBXO7]] (+0.61, fdr 7e-06); moves opposite to [[NSUN6]] (-0.63, fdr 7e-06), [[PPIEL]] (-0.57, fdr 1e-05), [[PPIEL-1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10561.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.76×** | +7.0 | 1e-09 | 35/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +5.8 | 2e-06 | 30/46 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.53×** | +5.2 | 3e-05 | 29/47 (SW1417, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +4.4 | 0.002 | 22/47 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +4.2 | 0.002 | 29/47 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.82×** | +3.9 | 0.010 | 21/47 (A498, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.37×** | +3.7 | 0.019 | 20/47 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.091 | 17/47 (A498, RKO, …) | rises with dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.32×** | +3.2 | 0.091 | 13/47 (A549, LS 180, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 1.59× | +3.0 | 0.12 | 15/45 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | 1.28× | +3.0 | 0.12 | 14/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.28× | +3.0 | 0.12 | 7/47 (HEC-1-A, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10561.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SW1417 0.155×, A549 0.153×, AsPC-1 0.195×, A498 0.224×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 0.132×, A498 0.104×, KATO III 0.111×, LoVo 0.144×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-172 0.0640×, SW480 0.257×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0639×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.378×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (AN3 CA 0.0832×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.339×** | -12.9 | 2e-35 | 31/33 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.387×** | -11.8 | 1e-29 | 38/40 (SW1417, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.636×** | -5.2 | 4e-05 | 25/38 (A-172, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.754×** | -5.0 | 1e-04 | 28/46 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.814×** | -3.6 | 0.035 | 24/48 (A-172, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.838× | -3.1 | 0.16 | 18/48 (A-172, SNU-423, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | 0.780× | -3.1 | 0.16 | 13/47 (HCT15, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10561. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 36.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0640× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.378× (z -10.0) |
| [[HOP62 (line)]] | alt | 23.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -10.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 23.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.104× (z -17.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 28.3 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.111× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 32.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 40.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -11.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 38.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -17.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 16.6 | 0 | 2 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0639× (z -16.2) |
| [[PANC-1 (line)]] | alt | 20.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +11.4) | — |
| [[A549 (line)]] | wt | 30.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -14.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 31.3 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0832× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -12.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -9.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 37.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -9.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -9.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 25.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -10.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -13.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 17.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -9.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 45.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -16.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10561), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS33B]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[PLD2]] | +0.61 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[FBXO7]] | +0.61 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[ZNF852]] | +0.61 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[STX7]] | +0.59 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[FPGT]] | +0.58 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[OTULIN]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 | pathway: Death Receptor Signaling; STRING 426 |
| [[NBPF1]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[NDFIP1]] | +0.57 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[CNEP1R1]] | +0.56 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[TBC1D13]] | +0.55 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[LTA4H]] | +0.54 | +0.62 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSUN6]] | -0.63 | -0.66 / -0.63 | both halves | 7e-06 |  |
| [[PPIEL]] | -0.57 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[PPIEL-1]] | -0.56 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[ETF1]] | -0.56 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[MYLK2]] | -0.55 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[TRIM72]] | -0.55 | -0.60 / -0.49 | both halves | 1e-05 | same gene group |
| [[AZU1]] | -0.55 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[DDX18]] | -0.54 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[IDI2-AS1]] | -0.53 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[PILRA]] | -0.53 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[R3HDM2]] | -0.52 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[ERCC1]] | -0.52 | -0.52 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers TRAF6's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-7.5, -9.9); signed map (-32.8, -16.8). **Vector** length 62.7, 11.5% of its response variance represented; |z| ≥ 3 in 796 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +2.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.6 | -1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.4 | -0.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.6 | +1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.6 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | +0.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.7 | -5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -1.5 | -11.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | +3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | +1.3 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor associated factor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p12 — chr11:36,483,769-36,510,272 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNF85 |
| Gene groups (HGNC) | Ring finger proteins; TNF receptor associated factors; Zinc fingers TRAF-type; RING finger E3 ubiquitin protein ligases |
| Reactome | 72 pathways, smallest: IRAK2 mediated activation of TAK1 complex; Alpha-protein kinase 1 signaling pathway; Regulated proteolysis of p75NTR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4K3](https://www.uniprot.org/uniprotkb/Q9Y4K3) (TNF receptor-associated factor 6):

> E3 ubiquitin ligase that, together with UBE2N and UBE2V1, mediates the synthesis of 'Lys-63'-linked-polyubiquitin chains conjugated to proteins, such as ECSIT, IKBKG, IRAK1, AKT1 and AKT2. Also mediates ubiquitination of free/unanchored polyubiquitin chain that leads to MAP3K7 activation. Leads to the activation of NF-kappa-B and JUN. Seems to also play a role in dendritic cells (DCs) maturation and/or activation (By similarity). Represses c-Myb-mediated transactivation, in B-lymphocytes. …

**Summary**, from NCBI Gene [7189](https://www.ncbi.nlm.nih.gov/gene/7189):

> The protein encoded by this gene is a member of the TNF receptor associated factor (TRAF) protein family. TRAF proteins are associated with, and mediate signal transduction from, members of the TNF receptor superfamily. This protein has an amino terminal RING domain which is followed by four zinc-finger motifs, a central coiled-coil region and a highly conserved carboxyl terminal domain, known as the TRAF-C domain and mediates signaling from members of the TNF receptor superfamily as well as …

**Accessions** — [HGNC:12036](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12036) · Entrez [7189](https://www.ncbi.nlm.nih.gov/gene/7189) · UniProt [Q9Y4K3](https://www.uniprot.org/uniprotkb/Q9Y4K3) · Ensembl [ENSG00000175104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175104)

## Data

Gene col 10561: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10561); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10561, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10561]; `tensor/DDL_lfc|DDL_z.npy` [10561]; `embed/gene_vectors.npy` [10561]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10561 or target_col == 10561). Every well: [[TRAF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
