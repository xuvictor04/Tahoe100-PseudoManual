---
symbol: "MFF"
type: "gene"
col: 9731
ensembl_id: "ENSG00000168958"
name: "mitochondrial fission factor"
location: "2q36.3"
module: 41
arm: "+"
pooled_cpm: 99.94
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# MFF

*mitochondrial fission factor* — 2q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.36× (z +9.5, q 8e-19, up in 27 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Azithromycin (hydrate) (drug)]] 5 µM: 1.11× (z +4.4, q 0.002, up in 3 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (HEC-1-A 2.00×, COLO 205 2.30×, HT-29 1.77×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 1.75×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 1.80×).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.773× (z -7.6, q 2e-11, down in 28 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.788× (z -7.3, q 7e-11, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 10 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H460 0.192×, NCI-H2030 0.331×, A498 0.436×; ⚠ cell-cycle shift, explains ~16% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.386×, A498 0.433×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.215×; ⚠ cell-cycle shift, explains ~22% of this change); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H460 0.374×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.386×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.478×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UFSP2]] (+0.51, fdr 6e-05), [[FAM114A2]] (+0.51, fdr 3e-05), [[UFL1]] (+0.51, fdr 2e-05); moves opposite to [[GATAD2A]] (-0.47, fdr 4e-05), [[ARHGAP23]] (-0.47, fdr 3e-05), [[NOTCH1]] (-0.45, fdr 3e-04).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GTF2I-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9731.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (HEC-1-A 2.00×, COLO 205 2.30×, HT-29 1.77×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 1.75×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 1.80×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +9.5 | 8e-19 | 27/49 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +7.9 | 8e-13 | 25/44 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.11× | +4.4 | 0.002 | 3/49 (HT-29, KATO III, …) | rises with dose | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.28×** | +4.1 | 0.007 | 8/48 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.11× | +3.2 | 0.15 | 6/48 (A549, SW 1088, …) | two highest doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | 1.11× | +3.1 | 0.20 | 4/49 (HCT15, Hs 766T, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | 1.11× | +3.0 | 0.20 | 9/48 (HT-29, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9731.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 10 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H460 0.192×, NCI-H2030 0.331×, A498 0.436×; ⚠ cell-cycle shift, explains ~16% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.386×, A498 0.433×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.215×; ⚠ cell-cycle shift, explains ~22% of this change); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H460 0.374×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.386×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.478×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.773×** | -7.6 | 2e-11 | 28/47 (MIA PaCa-2, A498, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.788×** | -7.3 | 7e-11 | 28/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.792×** | -7.2 | 2e-10 | 23/48 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.852× | -6.9 | 6e-10 | 23/49 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.832×** | -5.6 | 2e-06 | 22/48 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -5.2 | 2e-05 | 19/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.842× | -5.1 | 3e-05 | 20/48 (NCI-H460, C32, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.845× | -5.0 | 5e-05 | 21/50 (NCI-H460, A498, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change | 0.852× | -4.9 | 5e-05 | 20/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.852× | -4.9 | 5e-05 | 19/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.853× | -4.9 | 5e-05 | 18/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.867× | -4.4 | 5e-04 | 17/48 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.906× | -4.3 | 8e-04 | 18/48 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | 0.884× | -3.8 | 0.007 | 14/48 (NCI-H460, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.902× | -3.1 | 0.062 | 11/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.904× | -3.1 | 0.076 | 13/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Almonertinib (mesylate) (drug)]] 0.05 µM |  | 0.900× | -3.0 | 0.089 | 5/48 (SW 1088, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9731. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 491 | 0 | 26 (19 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -36.0) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.374× (z -15.1) |
| [[A498 (line)]] | wt | 156 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -17.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 191 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -19.7) ⚠ cell-cycle shift, explains ~16% of this change |
| [[MIA PaCa-2 (line)]] | alt | 70.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +8.7) ⚠ toxic; transcription drop | [[Niclosamide (olamine) (drug)]] 5 µM 0.419× (z -10.4) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 98.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -13.0) ⚠ cell-cycle shift, explains ~16% of this change |
| [[AsPC-1 (line)]] | alt | 77.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -8.5) ⚠ cell-cycle shift, explains ~16% of this change |
| [[C32 (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -10.3) ⚠ cell-cycle shift, explains ~22% of this change |
| [[COLO 205 (line)]] | alt | 45.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 87.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 52.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 95.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 84.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -8.6) ⚠ cell-cycle shift, explains ~22% of this change |
| [[HT-29 (line)]] | alt | 59.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 65.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 81.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.487× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[NCI-H1573 (line)]] | alt | 117 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.80× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 67.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.75× (z +9.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 73.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -8.6) ⚠ cell-cycle shift, explains ~19% of this change |
| [[SHP-77 (line)]] | alt | 65.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.553× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 74.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.488× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[A-172 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 64.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 80.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 75.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 67.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9731), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UFSP2]] | +0.51 | +0.56 / +0.38 | both halves | 6e-05 |  |
| [[FAM114A2]] | +0.51 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[UFL1]] | +0.51 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[FRA10AC1]] | +0.51 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[SLC30A5]] | +0.49 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[SENP2]] | +0.49 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[PSMD5]] | +0.48 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[DYNC2LI1]] | +0.47 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[GTF2I-AS1]] | +0.47 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[TRAPPC11]] | +0.47 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[TYW5]] | +0.47 | +0.44 / +0.40 | both halves | 4e-05 |  |
| [[GPRIN3]] | +0.47 | +0.39 / +0.55 | both halves | 6e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATAD2A]] | -0.47 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ARHGAP23]] | -0.47 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[NOTCH1]] | -0.45 | -0.27 / -0.57 | both halves | 3e-04 |  |
| [[WNK2]] | -0.44 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[PSD4]] | -0.44 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[DNAJB6]] | -0.44 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[ELF4]] | -0.42 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[ANOS2P]] | -0.42 | -0.29 / -0.29 | both halves | 3e-04 |  |
| [[ARHGAP27]] | -0.42 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[SMG1P3]] | -0.42 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[LIPG]] | -0.42 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[ESRP2]] | -0.41 | -0.41 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GTF2I-AS1]] | B | GTF2I-AS1 activity raises MFF's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 2.00× lower at baseline in the lines without GTF2I-AS1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.431). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-36.4, -8.7); signed map (-17.0, -10.8). **Vector** length 92.5, 20.1% of its response variance represented; |z| ≥ 3 in 813 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | -4.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.5 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +9.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.3 | -5.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.9 | +2.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.5 | +1.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.0 | -7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -3.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -3.9 | -5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -3.2 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -2.5 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -3.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial fission factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.3 — chr2:227,325,151-227,357,833 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GL004; previously C2orf33 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZY8](https://www.uniprot.org/uniprotkb/Q9GZY8) (Mitochondrial fission factor):

> Plays a role in mitochondrial and peroxisomal fission. Promotes the recruitment and association of the fission mediator dynamin-related protein 1 (DNM1L) to the mitochondrial surface. May be involved in regulation of synaptic vesicle membrane dynamics by recruitment of DNM1L to clathrin-containing vesicles (By similarity).

**Summary**, from NCBI Gene [56947](https://www.ncbi.nlm.nih.gov/gene/56947):

> This is a nuclear gene encoding a protein that functions in mitochondrial and peroxisomal fission. The encoded protein recruits dynamin-1-like protein (DNM1L) to mitochondria. There are multiple pseudogenes for this gene on chromosomes 1, 5, and X. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2013]

**Accessions** — [HGNC:24858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24858) · Entrez [56947](https://www.ncbi.nlm.nih.gov/gene/56947) · UniProt [Q9GZY8](https://www.uniprot.org/uniprotkb/Q9GZY8) · Ensembl [ENSG00000168958](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168958)

## Data

Gene col 9731: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9731); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9731, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9731]; `tensor/DDL_lfc|DDL_z.npy` [9731]; `embed/gene_vectors.npy` [9731]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9731 or target_col == 9731). Every well: [[MFF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
